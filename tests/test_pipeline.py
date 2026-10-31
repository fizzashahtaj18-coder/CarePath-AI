"""Pipeline tests with a fake LLM (no API key, no cost).

Run:  python tests/test_pipeline.py     (or: pytest tests/)

The fake LLM answers exactly what the answer key expects, using the real chunk IDs.
If everything is wired correctly, the evaluation script must score 100%.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path[:0] = [os.path.join(ROOT, "app"), os.path.join(ROOT, "eval")]

from pipeline.chunk import chunk_document, chunk_documents  # noqa: E402
from pipeline.checklist import generate_checklist  # noqa: E402
from pipeline.ingest import read_file  # noqa: E402
from pipeline.llm import FakeClient  # noqa: E402
import run_eval  # noqa: E402

TESTSET = os.path.join(ROOT, "eval", "testset")


def load_set(set_id):
    key = json.load(open(os.path.join(TESTSET, set_id, "answer_key.json"), encoding="utf-8"))
    docs = []
    for d in key["documents"]:
        text, err = read_file(os.path.join(TESTSET, set_id, d["file"]))
        docs.append({"id": d["id"], "title": d["title"], "text": text, "error": err})
    return key, docs


def find_chunk(chunks_by_doc, doc, quote):
    for c in chunks_by_doc[doc]:
        if quote in c.text:
            return c.chunk_id
    raise AssertionError(f"Quote not inside a single chunk of {doc}: {quote}")


def perfect_fake_answer(key, docs):
    readable = [d for d in docs if d["text"].strip() and not d["error"]]
    cbd = chunk_documents(readable)
    cite = lambda s: {"chunk_id": find_chunk(cbd, s["doc"], s["quote"]), "quote": s["quote"]}
    return {
        "no_instructions_found": key.get("expected_outcome") == "no_instructions_found",
        "items": [{"text": e["text"], "category": e["category"], "due_date": e.get("due_date"),
                   "citations": [cite(e["source"])] + [cite(a) for a in e.get("also_sources", [])],
                   "medical_instruction": e["medical_instruction"]} for e in key["expected_items"]],
        "conflicts": [{"topic": c["topic"], "citations": [cite(s) for s in c["sources"]]} for c in key["expected_conflicts"]],
        "covered_topics": key["covered_topics"],
    }


def test_every_quote_fits_in_one_chunk():
    for set_id in sorted(os.listdir(TESTSET)):
        if set_id.startswith("set"):
            key, docs = load_set(set_id)
            perfect_fake_answer(key, docs)  # raises if a quote is split across chunks


def test_chunk_ids_and_banner():
    chunks = chunk_document("D1", "SYNTHETIC TEST DOCUMENT. NOT A REAL PATIENT.\nFirst sentence. Second one.\n\nthird line")
    assert [c.chunk_id for c in chunks] == ["D1-C1", "D1-C2", "D1-C3"]
    assert chunks[0].text == "First sentence."


def test_end_to_end_scores_100_percent():
    outputs = {}
    for set_id in sorted(os.listdir(TESTSET)):
        if set_id.startswith("set"):
            key, docs = load_set(set_id)
            client = FakeClient([perfect_fake_answer(key, docs)])
            outputs[set_id] = generate_checklist(client, docs, {"specialty": key["specialty"]})
    summary, rows, md = run_eval.evaluate(outputs, "pipeline_fake_llm")
    assert summary["overall_pass"], md
    for name, m in summary.items():
        if name != "overall_pass" and name != "Medical advice flags":
            assert m["value"] == 1.0, (name, m)


def test_retry_once_on_invalid_output():
    key, docs = load_set("set02")
    good = perfect_fake_answer(key, docs)
    client = FakeClient([{"items": "not a list"}, good])
    out = generate_checklist(client, docs)
    assert out["attempts"] == 2 and client.calls == 2 and len(out["items"]) == len(key["expected_items"])


def test_gives_up_after_two_invalid_outputs():
    _, docs = load_set("set02")
    client = FakeClient([{"bad": 1}, {"bad": 2}])
    try:
        generate_checklist(client, docs)
    except ValueError:
        return
    raise AssertionError("Expected a ValueError after two invalid answers")


def test_scanned_pdf_reported_and_not_sent():
    key, docs = load_set("set08")
    client = FakeClient([perfect_fake_answer(key, docs)])
    out = generate_checklist(client, docs)
    assert {"doc": "D1", "error": "no_extractable_text"} in out["document_errors"]


def test_missing_topics_computed_by_code_not_ai():
    key, docs = load_set("set01")
    answer = perfect_fake_answer(key, docs)
    out = generate_checklist(FakeClient([answer]), docs)
    assert sorted(out["missing_topics"]) == sorted(key["expected_missing_topics"])


if __name__ == "__main__":
    tests = [v for k, v in dict(globals()).items() if k.startswith("test_")]
    for t in tests:
        t()
        print(f"PASS  {t.__name__}")
    print(f"\nAll {len(tests)} tests passed.")
