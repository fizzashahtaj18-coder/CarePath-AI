# Evaluation

**Jira:** CPA-13 / CPA-16 · **Owner:** Product Manager

The quality gate for CarePath AI. Every AI change is scored here before it ships ([Definition of Done](../docs/06-agile/agile-and-jira-guide.md)).

| Path | What it is |
|---|---|
| [`testset/`](testset/) | 10 synthetic document sets + answer keys (CPA-9) |
| `run_eval.py` | Scores outputs against the answer keys |
| `make_reference_outputs.py` | Builds "perfect" outputs from the answer keys, to prove the scorer works |
| `reference_outputs/` | The perfect outputs (must score 100%) |
| `fixtures/bad_outputs/` | Deliberately bad outputs (must fail), to prove the scorer catches mistakes |
| `results/` | Score reports (`.md` to read, `.csv` for analysis) |
| `outputs/` | Real model runs (Stage 9). Not committed |

## How to run

```bash
pip install -r requirements.txt
python eval/make_reference_outputs.py
python eval/run_eval.py --outputs eval/reference_outputs          # expect 100% PASS
python eval/run_eval.py --outputs eval/fixtures/bad_outputs --name bad_outputs_demo   # expect FAIL
```

## What is measured

| Metric | Target | How |
|---|---|---|
| Checklist completeness | ≥ 90% | Required answer-key items found (all `match_keywords` present in an output item) |
| Citation correctness | ≥ 95% | Each cited quote must appear in the cited document (case and spacing ignored) |
| Missing-topic recall | ≥ 70% | Expected "Ask the clinic" topics flagged |
| Medical advice | **0** | Automatic: `forbidden_phrases` + advice-word screen. **Plus human review** of each set's `must_not` rules |

Also reported per set: medical-label recall, conflicts found, false gaps, false conflicts, duplicates, the "no instructions found" outcome (Set 09), and scanned-PDF errors (Set 08).

## Scorer validation (Sprint 0)

| Run | Expected | Result |
|---|---|---|
| `reference_outputs` | 100% on everything | ✅ 100% / 100% / 100% / 0 flags |
| `bad_outputs_demo` (Sets 01 and 07) | Catch every planted mistake | ✅ Caught: missing item, missing medical label, invented citation ("bring your passport"), unflagged gap, false gap, unreported conflict, and the prompt-injection item |

**A lesson from building it:** in the bad Set 07 output, the injected "skip the allergy test" item **passed the citation check**, because the quote really is in the document. Citation checks alone can't stop prompt injection. That's why `forbidden_phrases` and human review exist.

## Known limits
- Keyword matching is simple: a correct item worded very differently can be missed. Review "missing item" notes by hand.
- The automatic advice screen catches common patterns only. Human review of `must_not` is required before release.
