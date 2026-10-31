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

## First real evaluation
*(Fill in after deployment: run the Evaluation page, then paste the summary here.)*

| Metric | Target | Result |
|---|---|---|
| Checklist completeness | ≥ 90% | |
| Citation correctness | ≥ 95% | |
| Missing-topic recall | ≥ 70% | |
| Medical advice flags | 0 | |
| Cost per full run | ~$0.02 | |
