"""Build 'perfect' outputs from the answer keys (CPA-16 sanity check).

If the scoring script is correct, these outputs must score 100% on every metric.
Usage:  python eval/make_reference_outputs.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TESTSET = os.path.join(HERE, "testset")
OUT = os.path.join(HERE, "reference_outputs")
os.makedirs(OUT, exist_ok=True)

for set_id in sorted(d for d in os.listdir(TESTSET) if d.startswith("set")):
    key = json.load(open(os.path.join(TESTSET, set_id, "answer_key.json"), encoding="utf-8"))
    items = []
    for e in key["expected_items"]:
        cits = [e["source"]] + e.get("also_sources", [])
        items.append({"text": e["text"], "category": e["category"],
                      "citations": cits, "medical_instruction": e["medical_instruction"]})
    out = {
        "set_id": set_id,
        "outcome": key.get("expected_outcome", "checklist"),
        "document_errors": key.get("expected_document_errors", []),
        "items": items,
        "conflicts": [{"topic": c["topic"], "citations": c["sources"]} for c in key["expected_conflicts"]],
        "missing_topics": key["expected_missing_topics"],
    }
    with open(os.path.join(OUT, f"{set_id}.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("wrote", set_id)
