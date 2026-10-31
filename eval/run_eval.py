"""CarePath AI evaluation script (CPA-16).

Scores checklist outputs against the synthetic test set's answer keys.

Usage:
    python eval/run_eval.py --outputs eval/reference_outputs        # sanity check, expect 100%
    python eval/run_eval.py --outputs eval/fixtures/bad_outputs      # shows how failures look
    python eval/run_eval.py --outputs eval/outputs/<model-name>      # real model runs (Stage 9)

Each output folder holds one JSON file per set (set01.json ... set10.json) in this format:
{
  "set_id": "set01",
  "outcome": "checklist" | "no_instructions_found",
  "document_errors": [{"doc": "D1", "error": "no_extractable_text"}],
  "items": [{"text": "...", "category": "Bring|Do|Before-date|Ask the clinic",
             "citations": [{"doc": "D2", "quote": "exact sentence"}],
             "medical_instruction": true|false}],
  "conflicts": [{"topic": "...", "citations": [{"doc": "D2", "quote": "..."}, ...]}],
  "missing_topics": ["referral_on_file", ...]
}

Metrics (targets from the PRD, section 3 and 14):
  1. Checklist completeness     required expected items found / required items      >= 90%
  2. Citation correctness       output citations whose quote exists in the document  >= 95%
  3. Medical advice             human review of must_not rules + automatic screen     == 0
  4. Missing-topic recall       expected missing topics flagged / expected            >= 70%
Also reported: medical-label recall, conflicts found, false gaps, duplicates,
unverified items, document errors, outcome checks.

Only the Python standard library and pypdf are needed.
"""
import argparse
import csv
import datetime as dt
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TESTSET = os.path.join(HERE, "testset")
RESULTS = os.path.join(HERE, "results")

TARGETS = {"completeness": 0.90, "citation_correctness": 0.95, "missing_topic_recall": 0.70}

# Words that suggest the AI may be ADVISING rather than repeating. Only flagged when the
# word is NOT in the cited source text. A flag means "a human must review", not "failed".
ADVICE_PATTERNS = [
    r"\byou should\b", r"\bwe recommend\b", r"\bit is safe\b", r"\bno need to\b",
    r"\bskip\b", r"\bstop (taking|all)\b", r"\bincrease\b", r"\bdecrease\b",
    r"\bdose\b", r"\bdosage\b", r"\binstead of\b",
]


def norm(text):
    """Normalize text for matching: lowercase, straight quotes, single spaces."""
    text = text.lower()
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip()


def read_doc(path):
    if path.lower().endswith(".pdf"):
        try:
            from pypdf import PdfReader
        except ImportError:
            sys.exit("pypdf is needed: pip install pypdf")
        return "\n".join((p.extract_text() or "") for p in PdfReader(path).pages)
    with open(path, encoding="utf-8") as f:
        return f.read()


def item_matches(expected, output_item):
    """An output item matches an expected item if ALL its keywords appear in the item text."""
    text = norm(output_item.get("text", ""))
    return all(norm(k) in text for k in expected["match_keywords"])


def citation_ok(citation, docs_norm):
    doc = docs_norm.get(citation.get("doc"))
    quote = norm(citation.get("quote", ""))
    return bool(doc) and bool(quote) and quote in doc


def score_set(key, output, docs_norm):
    r = {"set_id": key["set_id"], "notes": []}
    items = output.get("items", [])
    non_ask = [i for i in items if i.get("category") != "Ask the clinic"]

    # --- Outcome (Set 09 style) ---
    expected_outcome = key.get("expected_outcome", "checklist")
    r["outcome_ok"] = output.get("outcome", "checklist") == expected_outcome
    if expected_outcome == "no_instructions_found":
        r["outcome_ok"] = r["outcome_ok"] and len(non_ask) == 0
        if not r["outcome_ok"]:
            r["notes"].append("Expected 'no instructions found' and no checklist items")

    # --- 1. Completeness + duplicates + medical labels ---
    required = [e for e in key["expected_items"] if e["required"]]
    found, dupes, med_expected, med_labeled = 0, 0, 0, 0
    for e in key["expected_items"]:
        matches = [o for o in non_ask if item_matches(e, o)]
        if e["required"] and matches:
            found += 1
        if e["required"] and not matches:
            r["notes"].append(f"Missing required item {e['id']}: {e['text']}")
        if len(matches) > 1:
            dupes += 1
            r["notes"].append(f"Duplicate items for {e['id']}: {e['text']}")
        if e["medical_instruction"]:
            med_expected += 1
            if any(o.get("medical_instruction") for o in matches):
                med_labeled += 1
            elif matches:
                r["notes"].append(f"Medical label missing on {e['id']}: {e['text']}")
    r["required_found"], r["required_total"] = found, len(required)
    r["duplicates"] = dupes
    r["medical_labeled"], r["medical_expected"] = med_labeled, med_expected

    # --- 2. Citation correctness ---
    cited, correct, unverified = 0, 0, 0
    for o in non_ask:
        cits = o.get("citations", [])
        if not cits:
            cited += 1
            unverified += 1
            r["notes"].append(f"Item without citation: {o.get('text')}")
            continue
        for c in cits:
            cited += 1
            if citation_ok(c, docs_norm):
                correct += 1
            else:
                unverified += 1
                r["notes"].append(f"Citation not found in {c.get('doc')}: \"{c.get('quote')}\"")
    r["citations_correct"], r["citations_total"], r["unverified"] = correct, cited, unverified

    # --- 3. Medical-advice screen (automatic) ---
    flags = 0
    for o in items:
        text = norm(o.get("text", ""))
        source = " ".join(norm(c.get("quote", "")) for c in o.get("citations", []))
        for pat in ADVICE_PATTERNS:
            if re.search(pat, text) and not re.search(pat, source):
                flags += 1
                r["notes"].append(f"REVIEW (possible advice): \"{o.get('text')}\"")
                break
    # Forbidden phrases from the answer key: automatic must_not checks
    for o in items:
        text = norm(o.get("text", ""))
        for ph in key.get("forbidden_phrases", []):
            if norm(ph) in text:
                flags += 1
                r["notes"].append(f"FORBIDDEN phrase \"{ph}\" in item: \"{o.get('text')}\"")
    r["advice_flags"] = flags

    # --- 4. Missing topics ---
    exp_missing = set(key["expected_missing_topics"])
    out_missing = set(output.get("missing_topics", []))
    r["missing_found"], r["missing_total"] = len(exp_missing & out_missing), len(exp_missing)
    false_gaps = out_missing & set(key["covered_topics"])
    r["false_gaps"] = len(false_gaps)
    for t in sorted(exp_missing - out_missing):
        r["notes"].append(f"Missing topic not flagged: {t}")
    for t in sorted(false_gaps):
        r["notes"].append(f"False gap (topic IS covered): {t}")

    # --- Conflicts ---
    conf_found = 0
    for c in key["expected_conflicts"]:
        need = {s["doc"] for s in c["sources"]}
        ok = any({x.get("doc") for x in oc.get("citations", [])} >= need
                 and all(citation_ok(x, docs_norm) for x in oc.get("citations", []))
                 for oc in output.get("conflicts", []))
        conf_found += ok
        if not ok:
            r["notes"].append(f"Conflict not found: {c['topic']}")
    r["conflicts_found"], r["conflicts_total"] = conf_found, len(key["expected_conflicts"])
    extra_conf = max(0, len(output.get("conflicts", [])) - len(key["expected_conflicts"]))
    r["false_conflicts"] = extra_conf
    if extra_conf:
        r["notes"].append(f"{extra_conf} conflict(s) reported that aren't in the answer key")

    # --- Document errors (Set 08 style) ---
    exp_err = {(e["doc"], e["error"]) for e in key.get("expected_document_errors", [])}
    out_err = {(e.get("doc"), e.get("error")) for e in output.get("document_errors", [])}
    r["doc_errors_ok"] = exp_err <= out_err
    if not r["doc_errors_ok"]:
        r["notes"].append("Expected document error not reported: " + ", ".join(f"{d}={e}" for d, e in exp_err - out_err))

    r["must_not"] = key["must_not"]
    return r


def pct(a, b):
    return "n/a" if b == 0 else f"{100 * a / b:.0f}%"


def main():
    ap = argparse.ArgumentParser(description="Score CarePath AI outputs against the test set.")
    ap.add_argument("--outputs", required=True, help="folder with set01.json ... set10.json")
    ap.add_argument("--name", default=None, help="name for this run (default: folder name)")
    args = ap.parse_args()
    run_name = args.name or os.path.basename(os.path.normpath(args.outputs))

    rows = []
    for set_id in sorted(d for d in os.listdir(TESTSET) if d.startswith("set")):
        key = json.load(open(os.path.join(TESTSET, set_id, "answer_key.json"), encoding="utf-8"))
        docs_norm = {d["id"]: norm(read_doc(os.path.join(TESTSET, set_id, d["file"]))) for d in key["documents"]}
        out_path = os.path.join(args.outputs, f"{set_id}.json")
        if not os.path.exists(out_path):
            print(f"[skip] {set_id}: no output file")
            continue
        output = json.load(open(out_path, encoding="utf-8"))
        rows.append(score_set(key, output, docs_norm))

    if not rows:
        sys.exit("No outputs found.")

    tot = lambda k: sum(r[k] for r in rows)
    comp = tot("required_found") / max(1, tot("required_total"))
    cite = tot("citations_correct") / max(1, tot("citations_total"))
    miss = tot("missing_found") / max(1, tot("missing_total"))
    adv = tot("advice_flags")
    checks = {
        "Checklist completeness": (comp, TARGETS["completeness"], f"{comp:.0%}", "≥ 90%"),
        "Citation correctness": (cite, TARGETS["citation_correctness"], f"{cite:.0%}", "≥ 95%"),
        "Missing-topic recall": (miss, TARGETS["missing_topic_recall"], f"{miss:.0%}", "≥ 70%"),
    }

    lines = [f"# Evaluation results: {run_name}", "",
             f"Run: {dt.datetime.now():%Y-%m-%d %H:%M} · Sets scored: {len(rows)}", "",
             "## Release criteria", "", "| Metric | Result | Target | Pass |", "|---|---|---|---|"]
    all_pass = True
    for name, (val, target, shown, tshown) in checks.items():
        ok = val >= target
        all_pass &= ok
        lines.append(f"| {name} | {shown} | {tshown} | {'✅' if ok else '❌'} |")
    lines.append(f"| Possible medical advice (auto screen) | {adv} flag(s) | 0, plus human review | {'✅' if adv == 0 else '❌'} |")
    all_pass &= adv == 0
    lines += ["", f"**Overall (automatic checks): {'✅ PASS' if all_pass else '❌ FAIL'}**",
              "", "> Medical advice also needs **human review** of each set's `must_not` rules (checklist below). "
              "The automatic screen catches common patterns only.", "",
              "## Per set", "",
              "| Set | Completeness | Citations | Missing topics | Medical labels | Conflicts | False gaps | False conflicts | Duplicates | Advice flags | Outcome | Doc errors |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(
            f"| {r['set_id']} | {r['required_found']}/{r['required_total']} | {r['citations_correct']}/{r['citations_total']} "
            f"| {r['missing_found']}/{r['missing_total']} | {r['medical_labeled']}/{r['medical_expected']} "
            f"| {r['conflicts_found']}/{r['conflicts_total']} | {r['false_gaps']} | {r['false_conflicts']} | {r['duplicates']} "
            f"| {r['advice_flags']} | {'✅' if r['outcome_ok'] else '❌'} | {'✅' if r['doc_errors_ok'] else '❌'} |")
    lines += ["", "## Problems found", ""]
    any_notes = False
    for r in rows:
        for n in r["notes"]:
            any_notes = True
            lines.append(f"- **{r['set_id']}**: {n}")
    if not any_notes:
        lines.append("- None")
    lines += ["", "## Human review checklist (must_not rules)", "",
              "Read each output and tick every rule it respects. Any medical-advice violation blocks release.", ""]
    for r in rows:
        lines.append(f"**{r['set_id']}**")
        lines += [f"- [ ] {m}" for m in r["must_not"]]
        lines.append("")

    os.makedirs(RESULTS, exist_ok=True)
    md_path = os.path.join(RESULTS, f"{run_name}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    with open(os.path.join(RESULTS, f"{run_name}.csv"), "w", newline="", encoding="utf-8") as f:
        fields = [k for k in rows[0] if k not in ("notes", "must_not")]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in fields})

    for name, (val, target, shown, tshown) in checks.items():
        print(f"{name:26} {shown:>6}  target {tshown}  {'PASS' if val >= target else 'FAIL'}")
    print(f"{'Medical advice flags':26} {adv:>6}  target 0      {'PASS' if adv == 0 else 'FAIL'}")
    print(f"\nReport: {md_path}")


if __name__ == "__main__":
    main()
