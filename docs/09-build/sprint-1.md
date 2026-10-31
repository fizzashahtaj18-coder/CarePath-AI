# Sprint 1: First Working Checklist

**Sprint goal:** *A patient can paste instructions and get a draft checklist.*
**Stories:** CPA-20 (appointment details) · CPA-17 (paste text and call notes) · CPA-21 (draft checklist)

## What was built

| Part | File | What it does |
|---|---|---|
| Chunking | `app/pipeline/chunk.py` | Splits each document into numbered sentences (`D2-C3`) so every item can cite its source |
| Output schema | `app/pipeline/schema.py` | The exact structure the AI must return (items, conflicts, covered topics) |
| LLM wrapper | `app/pipeline/llm.py` | One function calls Claude Haiku 5.5; easy to swap providers |
| Prompt | `prompts/checklist_v1.md` | 10 rules: repeat never advise, cite everything, label medical instructions, never choose between conflicts, documents are data |
| Checklist logic | `app/pipeline/checklist.py` | Chunk → prompt → one AI call → validate → retry once → convert. **Missing topics are computed by code**, not the AI |
| App | `app/streamlit_app.py` | Patient page (3 steps) + password-protected **Evaluation** page |
| Tests | `tests/test_pipeline.py` | 7 tests with a fake AI: end-to-end scoring, retry, scanned PDF, missing topics |

## Model-specific decisions (Claude Haiku 5.5)
From Anthropic's migration guide, checked October 31, 2026:
- **No `temperature`** setting: Haiku 5.5 returns an error for it. Consistency comes from the prompt and the schema instead.
- **Forced tool call** for structured output: supported, and the answer starts directly with the tool call.
- **Strip trailing newlines** in returned text: Haiku 5.5 may add them to tool-call strings.

## Scope kept out on purpose (later sprints)
Show-source panel and code-level citation checks (Sprint 2) · editing and approval (Sprint 3) · "Ask the clinic" display and PDF upload (Sprint 4).

## Test results (fake AI, no cost)
All 7 tests pass. With perfect answers, the evaluation scores 100% on every metric, so the pipeline and the scorer are connected correctly.

## First real evaluation (Oct 31, 2026)

**Run:** Claude Haiku 5.5 · prompt `checklist_v1` · 10 synthetic sets · **cost ≈ $0.006**

| Metric | Target | v1 (as run) | v1 (corrected answer keys) | v2 |
|---|---|---|---|---|
| Checklist completeness | ≥ 90% | 100% | **94%** | ⏳ |
| Citation correctness | ≥ 95% | 100% | 100% | ⏳ |
| Missing-topic recall | ≥ 70% | 86% | 86% | ⏳ |
| Medical advice flags | 0 | 0 | 0 | ⏳ |
| Safety review (must_not) | no violations | ✅ | ✅ | ⏳ |

**Headline:** no medical advice, and the hidden prompt-injection instruction (Set 07) was ignored completely.

**Found by human review** ([full review](../../eval/results/claude-haiku-5-5_checklist_v1_2026-10-31_review.md)):
1. Timing words dropped ("5 days before:"): a real patient-safety gap the scorer missed. Fixed in prompt v2 and in the answer keys.
2. Topics over-claimed as "covered" in 6 sets, removing "Ask the clinic" questions. Fixed in v2 with topic definitions plus code-checked evidence.
3. One answer-key error (Set 03 forms) and one scorer false alarm, both corrected.

## Prompt v2 (ready to run)
- Rule 8: keep every timing phrase in the item text
- Precise `covered_when` definition for each topic (`config/topics.yaml` v2)
- Each covered topic needs evidence (chunk ID + quote), **verified by code**; no evidence means "Ask the clinic"
- 9 tests pass with the fake AI
