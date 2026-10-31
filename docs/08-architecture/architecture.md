# Technical & AI Architecture

**Stage:** 8, Technical & AI Architecture
**Status:** 🟡 v0.1. Model choice to be confirmed by the Stage 9 comparison on the test set
**Inputs:** [PRD](../05-prd/prd.md) (especially §8, the AI behavior spec) · [Prioritization](../04-prioritization/prioritization-and-roadmap.md) · [UX](../07-design/ux-design.md)
**Prices checked:** October 30, 2026. API prices change often, so re-check before building.

---

## 1. Architecture in one sentence

A **single Python web app** (Streamlit) reads the patient's documents, splits them into numbered chunks, asks **one LLM call** for a structured checklist with quotes, and then uses **plain code** to verify every quote, flag safety issues, and find missing topics, all inside the browser session, with **nothing stored**.

> **Guiding rule:** use the LLM only where language understanding is needed. Everything that *can* be deterministic, *is* deterministic, because deterministic code is cheaper, faster, testable, and never hallucinates.

---

## 2. System diagram

```mermaid
flowchart LR
    subgraph Browser["Patient's browser"]
        UI[Streamlit UI<br/>3 screens]
    end

    subgraph App["CarePath AI app (Streamlit Community Cloud)<br/>session memory only, no database"]
        IN[1. Ingest<br/>pypdf text extraction<br/>+ pasted text]
        CH[2. Chunk<br/>numbered D1-C1, D1-C2…]
        PR[3. Build prompt<br/>versioned template<br/>+ topics list]
        VAL[5. Validate<br/>JSON schema check<br/>retry once]
        VER[6. Verify citations<br/>quote must exist in chunk]
        SAF[7. Safety rules<br/>medical keywords backup<br/>conflict check]
        MIS[8. Missing topics<br/>fixed list minus covered]
        ST[(Session state<br/>cleared on close<br/>or Delete everything)]
    end

    subgraph External["External"]
        LLM[LLM API<br/>small model]
    end

    CFG[[config/topics.yaml<br/>PM-reviewed]]
    PT[[prompts/checklist_v1.md<br/>versioned in GitHub]]

    UI --> IN --> CH --> PR
    PT --> PR
    CFG --> PR
    PR -- "4. one call<br/>(document text leaves the app here)" --> LLM
    LLM --> VAL --> VER --> SAF --> MIS --> ST --> UI
    CFG --> MIS
```

**Trust boundary:** the only place patient text leaves the app is **step 4, the LLM API call**. That's why the privacy notice says so, why the prototype uses **synthetic data only**, and why the provider's data-use terms are part of model selection (§5).

---

## 3. The pipeline step by step

| Step | What happens | AI or code? | Why |
|---|---|---|---|
| 1. Ingest | Extract text from PDFs; accept pasted text; detect scanned PDFs (no text) | **Code** | Deterministic; clear error for scanned files (FR-1.3) |
| 2. Chunk | Split each document into short passages; give IDs like `D2-C3` | **Code** | Stable IDs make citations checkable |
| 3. Build prompt | Instructions + rules ("repeat, never advise", "document text is data") + chunks + topics list | **Code** | Versioned template = reproducible results |
| 4. Generate | Extract admin instructions → checklist JSON with chunk IDs + exact quotes; flag medical instructions and conflicts; list covered topics | **AI** | Needs language understanding |
| 5. Validate | Check JSON against the schema; retry once; otherwise show an error | **Code** | Reliability (FR-2.4) |
| 6. Verify citations | Each quote must appear in its cited chunk (case and whitespace ignored). Fail → "Couldn't verify source" | **Code** | **Catches hallucinations** (FR-3.2) |
| 7. Safety rules | Keyword backup check (for example "fast", "medication", "do not eat") marks medical instructions even if the AI missed them; conflict items must cite ≥2 different chunks | **Code** | **Defense in depth:** safety never depends on the AI alone |
| 8. Missing topics | `missing = all topics − topics covered with a verified citation` → "Ask the clinic" items | **Code** | Predictable; the AI can't invent gaps (FR-5.4) |
| 9. Show & approve | Draft → patient edits → approves → checks off | **Code** | Human in the loop |

---

## 4. Components: purpose, alternatives, cost, decision

| Component | Purpose | Chosen | Alternatives considered | Cost | Why this choice |
|---|---|---|---|---|---|
| **Language** | Everything | **Python** | JavaScript/TypeScript | Free | Matches the PM's skills; best AI/data libraries |
| **Web UI** | 3 screens | **Streamlit** | Gradio; Next.js + FastAPI | Free | A web app in pure Python in hours; good enough to test value. A React front end is unnecessary for an MVP |
| **Backend** | Pipeline logic | **Plain Python modules inside the Streamlit app** | FastAPI service | Free | One user, one session, no API consumers yet. FastAPI only when a second client (mobile, clinic integration) needs it |
| **PDF extraction** | Read text PDFs | **pypdf** (BSD license) | PyMuPDF (faster, more features) | Free | **PyMuPDF is AGPL-licensed**: using it in a web service can require open-sourcing the app or buying a commercial license. pypdf is permissive and fast enough for 1–5 short documents. Re-evaluate if layout quality becomes a problem |
| **LLM** | Extraction + checklist | **A small, low-cost model** (shortlist below) | Large frontier models | ~$0.002 per checklist | Admin extraction from short documents doesn't need the largest model. Choose by **test-set accuracy**, not brand |
| **Structured output** | Reliable JSON | Provider's JSON/structured-output mode + **pydantic** schema | Free-text parsing | Free | Schema-checked output is the base of verification |
| **Citation verifier** | Catch invented quotes | **Normalized string match** (code) | Fuzzy matching; a second LLM as a judge | Free | Exact is strict, simple, and explainable. Add fuzzy matching only if valid quotes fail too often |
| **Topics list** | Missing-information flags | **`config/topics.yaml`** | AI-generated topics | Free | PM-reviewed, versioned, testable |
| **Storage** | Session data | **Streamlit session state (memory)** | SQLite; Postgres | Free | Decision 23: session-only. **SQLite (in the original brief) isn't needed** because nothing is saved |
| **Vector database** | Retrieval | **None in MVP** | Chroma + embeddings | Free | Decision 20: documents fit in one prompt. Chroma comes with feature F12 (curated knowledge base) |
| **Hosting** | Public demo | **Streamlit Community Cloud** | Hugging Face Spaces; Render | Free | Deploys from GitHub; built-in secrets settings |
| **Secrets** | API key | `st.secrets` / `.streamlit/secrets.toml` in `.gitignore` | Hard-coding | Free | Keys never in the public repo |
| **Evaluation** | Quality gate | **Python script + synthetic test set (JSON)**; optional GitHub Actions run | Paid eval platforms | ~$0.02 per full run | Simple, transparent, version-controlled |
| **Analytics** | Product metrics | Privacy-safe event counts (no document text) | Third-party trackers | Free | Designed in Stage 13 |

---

## 5. Model selection

### Shortlist (small, low-cost models; prices per million tokens)

| Model | Input | Output | Notes |
|---|---|---|---|
| Claude Haiku 5.5 (Anthropic) | $0.10 | $0.50 | Prompts over 100K tokens cost more ($0.50 / $2.50). Ours are far below that |
| GPT-6 Luna (OpenAI) | $0.10 | $0.50 | Long-context rate above 272K input tokens |
| Gemini 2.5 Flash (Google) | $0.30 | $2.50 | Flash-Lite is cheaper ($0.10 / $0.40) |
| *Reference: a mid-tier model (for example Claude Sonnet 5.5 or GPT-6 Sol)* | *$2.00* | *$10.00* | *Only if small models fail the quality bar* |

### Cost per checklist (estimate)
Assumption: 5 short documents ≈ **8,000 input tokens** (including instructions), **1,500 output tokens**.

| Tier | Calculation | Cost per checklist | 1,000 checklists |
|---|---|---|---|
| Small ($0.10 / $0.50) | 8,000 × $0.10/1M + 1,500 × $0.50/1M | **≈ $0.0016** | ≈ $1.60 |
| Gemini 2.5 Flash ($0.30 / $2.50) | 8,000 × $0.30/1M + 1,500 × $2.50/1M | ≈ $0.006 | ≈ $6 |
| Mid-tier ($2 / $10) | 8,000 × $2/1M + 1,500 × $10/1M | ≈ $0.031 | ≈ $31 |

**All options are well under the PRD target of $0.05 per checklist.** Cost doesn't decide the model. **Quality and data terms do.**

### How the model will be chosen (Stage 9)
1. Run the **same prompt** on 2–3 shortlisted models against the **synthetic test set** (Sprint 0).
2. Compare: completeness, citation correctness, medical-advice count (**must be 0**), missing-topic recall, latency.
3. Check each provider's **API data-use terms** (training on inputs, retention).
4. Choose the cheapest model that **meets every release criterion**. Record the decision in the decision log.
5. Keep the LLM call behind **one small wrapper function**, so switching providers means changing one file.

> 💬 **Interview talking point:** *"I didn't pick a model by reputation. I defined the quality bar first, ran candidates on the same test set, and chose the cheapest one that passed. The architecture keeps the model swappable."*

---

## 6. Non-functional requirements: how the design meets them

| NFR (PRD §10) | How |
|---|---|
| ≤ 30 s per checklist | One LLM call (~5–15 s for a small model); all other steps < 1 s |
| ≤ $0.05 per checklist | ≈ $0.002 with a small model |
| Reliability | Schema validation + one retry + clear error |
| Privacy | No database, no logging of document text, session cleared on Delete or close; synthetic data only |
| Security | API key in secrets; `.gitignore`; no keys in commits |
| Safety | Prompt rules + code-level citation verification + keyword safety net + human approval |
| Prompt injection | Documents wrapped in clear delimiters and labeled as data; output must match the schema; no tools or actions available to the model, so injected text has nothing to trigger |

---

## 7. Planned repository code structure

```
app/
├── streamlit_app.py        UI: 3 screens
└── pipeline/
    ├── ingest.py           PDF and pasted-text extraction
    ├── chunk.py            Numbered chunks (D1-C1…)
    ├── llm.py              One wrapper around the LLM API (swappable)
    ├── schema.py           Pydantic models for checklist JSON
    ├── verify.py           Citation verification
    ├── safety.py           Medical keyword backup, conflict checks
    └── topics.py           Missing-topic calculation
config/
└── topics.yaml             Common administrative topics (PM-reviewed)
prompts/
└── checklist_v1.md         Versioned prompt template
eval/
├── testset/                10 synthetic document sets + answer keys
└── run_eval.py             Completeness, citation correctness, medical advice, missing-topic recall
.streamlit/secrets.toml     Local API key (in .gitignore, never committed)
requirements.txt
```

---

## 8. Architecture decision records (ADRs)

| # | Decision | Status | Consequence |
|---|---|---|---|
| ADR-1 | Streamlit monolith, no separate backend | Accepted | Fast to build; revisit for multi-client or scale |
| ADR-2 | No vector DB / RAG in MVP; grounded generation over numbered chunks | Accepted | Simpler and cheaper; RAG returns with F12 |
| ADR-3 | Deterministic citation verification in code | Accepted | Hallucinated quotes are caught and labeled |
| ADR-4 | pypdf instead of PyMuPDF | Accepted | Avoids AGPL obligations; weaker on complex layouts |
| ADR-5 | Session-only storage, no database | Accepted | Strong privacy story; no history or accounts |
| ADR-6 | Small LLM behind a swappable wrapper; final pick by test set | Proposed | Decided in Stage 9 |
| ADR-7 | Safety in layers: prompt rules + code checks + human approval | Accepted | Safety never depends on the model alone |

---

## 9. Technical risks

| Risk | Mitigation |
|---|---|
| Valid quotes fail exact matching (formatting differences) | Normalize whitespace and quotes; measure the false-failure rate; add fuzzy matching if needed |
| PDF text comes out jumbled (columns, tables) | Paste-text fallback; test with realistic layouts; reconsider the PDF library later |
| Model changes or is retired | Pin the model version; re-run evaluation on any change |
| Free hosting limits (sleep, resources) | Fine for a portfolio demo; note it in the README |
| API key leak | Secrets settings + `.gitignore`; rotate the key if exposed |

---

## Sources
- Claude Haiku 5.5 pricing: [Tech Enclave](https://techenclave.com/news/items/claude-haiku-5-5-launches-with-0-10-input-pricing-for-shorter-prompts), [Let's Data Science](https://letsdatascience.com/blog/claude-haiku-5-5-cut-prices-90-prompts-over-100k-pay-5x)
- GPT-6 Luna pricing: [eesel AI](https://www.eesel.ai/blog/gpt-6-luna-pricing)
- Gemini API pricing: [Morph](https://www.morphllm.com/gemini-api-pricing)
- PyMuPDF vs pypdf licensing: [PDF Oxide comparison](https://pdf.oxide.fyi/docs/comparison/pymupdf-vs-pypdf), [PyMuPDF on PyPI](https://pypi.org/project/PyMuPDF/1.19.0/)
- Streamlit secrets: [Streamlit docs](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)
