# Decision Log

Records key product decisions, the reasoning behind them, and open questions.

## Decisions
| # | Decision | Reasoning |
|---|---|---|
| 1 | Users: adults attending a non-emergency specialist appointment for the first time | Narrow, specific group with a clear moment of need |
| 2 | Market: United States | Founder lives in New York; complex US referral and paperwork processes; access to interviewees |
| 3 | Platform: web application | Accessible without installing an app |
| 4 | Scope: healthcare administration only | Avoids medical advice risk and stricter regulation |
| 5 | Boundary rule: "organizes and repeats; never advises" | Protects patients from AI errors on medical topics; citations let users verify everything |
| 6 | Primary value: confidence (secondary: organization, time savings) | Unprepared patients focus on paperwork, not their health |
| 7 | Vision: "Every patient walks confidently into their specialist appointment prepared, so their attention goes to their health, not their paperwork." | Describes the user's future state, not features |
| 8 | Metrics: rescheduling (long-term), checklist completeness (primary), self-rated preparedness (secondary) | Completeness is measurable with synthetic data; preparedness confirms trust |
| 9 | Data: synthetic only; no HIPAA or clinical-validation claims | Portfolio prototype; protects privacy |
| 10 | Jira set up in Stage 6 | Backlog needs validated user stories first |
| 11 | Top 3 assumptions to test first: #4 documents are digital, #5 willingness to upload, #3 information arrives in writing | Highest risk scores; testable in Stage 2; can change the MVP (see assumptions.md) |
| 12 | Initial targets: completeness ≥ 90%, citation correctness ≥ 95%, zero generated medical advice, preparedness +1 point | Starting points; to be finalized in the PRD |
| 13 | Proposed: MVP retrieval covers the patient's own documents; external knowledge base is Phase 2 | Fits the 36-hour budget; the most important citations point to the patient's documents |
| 14 | GitHub topics describe a workflow, not agents (`workflow-automation`, not `llm-agents`) | Never claim more than the product does |
| 15 | Stage 2 method: email interviews (5–8 participants) + desk research | Fits the founder's schedule; written answers are weaker than live interviews, so each participant gets one follow-up |
| 16 | Differentiation: per-item citations, flagging missing information, and admin-only safety (vs. ChatGPT Health, clinic portals, record aggregators) | Competitor analysis: no alternative cites sources per item or systematically flags missing information |
| 17 | Interim discovery decision: **Revise (provisional).** Problem = scattered + spoken/forgotten + missing information, not only disorganized documents | Founder experience + desk research; to be confirmed or reversed by email interviews |
| 18 | Proto-personas: Amira (Newcomer, provisional primary) and Daniel (Busy Professional); anti-personas defined | Assumption-based and labeled as such; to be validated by interviews |
| 19 | MVP scope (MoSCoW Must): setup, PDF upload, paste text, extraction + checklist, verified citations, missing-information flags, safety guardrails, review/edit/approve/check-off, privacy controls (~14.5h) | RICE scoring + 14.5h build budget; see prioritization-and-roadmap.md |
| 20 | No vector-database RAG in the MVP: grounded generation with chunk-ID citations verified by code. RAG moves to F12 (curated knowledge base, Could have / stretch) | Patient documents fit in the context window; RAG is used only where the corpus is too large for a prompt |
| 21 | Build the synthetic evaluation set (Week 5) before coding (Week 6) | Evaluation-driven development: define what "good" looks like first |
| 22 | Cut line if behind: PDF upload first, then setup; never cut extraction, citations, missing-information flags, guardrails, or review | Protect the core value and safety |
| 23 | Session-only data: no database storage of documents by default; "Delete everything" button; export instead of accounts | Trust is the biggest adoption risk; less data to secure |
| 24 | The missing-information topic list is a fixed, PM-reviewed configuration file, not AI-generated | Keeps gap detection predictable, testable, and administration-only |
| 25 | The AI never chooses between conflicting instructions; it shows both with citations | Avoids silent errors on safety-relevant details |
| 26 | One-week sprints (Sprint 0–5, Weeks 5–10); 56 story points; Sprint 0 builds the evaluation set first | Matches the roadmap; evaluation-driven development |
| 27 | AI-specific Definition of Done: every AI story re-runs the evaluation and must not lower scores | AI output can get worse without any code error |
| 28 | Three-step flow (Set up → Review draft → Prepare) with a split review screen: checklist + source panel | Citations are the main trust mechanism, so the source must be one click away |
| 29 | Every label pairs an icon with words; Atkinson Hyperlegible typeface; 17px base; ≥44px targets; WCAG 4.5:1 contrast | Low health literacy and accessibility; never rely on color alone |
| 30 | No AI-generated doctor questions; the patient adds their own ("Added by you") | Keeps the product administrative-only while addressing the "forgot my questions" pain |
| 31 | Architecture: single Streamlit app; one LLM call; citations, safety keywords, and missing topics checked in code; session-only storage; no SQLite or vector DB in MVP | Simplest design that meets the PRD; safety never depends on the model alone (ADR-1 to ADR-7) |
| 32 | pypdf instead of PyMuPDF for PDF extraction | PyMuPDF is AGPL-licensed; pypdf is BSD and sufficient for short text PDFs |
| 33 | Model: shortlist small, low-cost models (~$0.002 per checklist); final pick by test-set results and provider data terms in Stage 9; LLM behind a swappable wrapper | Cost isn't the constraint; quality and data terms are |
| 34 | After Round 1 (3 email responses): keep "Revise (provisional)" and the MVP scope; assumptions #3, #4, #5 stay untested; P3 is out of segment (follow-up visit); all new participants get the full 10-question kit | Round 1 used a shorter question set; avoid over-claiming. See findings.md Part B |
| 35 | Evaluation set complete: 10 synthetic sets, 9 specialties, 47 required items; optional items not scored; Set 08 uses a real image-only PDF; Set 09 expects "no instructions found" | Defines "correct" before any code is written (CPA-9) |
| 36 | Evaluation script validated: perfect outputs score 100%, planted mistakes are all caught. Added `forbidden_phrases` because an injected instruction passed the citation check | Citation checks alone can't stop prompt injection; safety needs layered checks (ADR-7) |
| 37 | First model: Anthropic Claude Haiku 5.5 (`claude-haiku-5-5`), called through one forced tool call for structured output; no temperature setting | PM choice to start; Haiku 5.5 rejects temperature/top_p and supports forced tool_choice (Anthropic migration guide). Compared with another model in Stage 9 |
| 38 | Public demo protected by an optional ACCESS_CODE; Evaluation page by EVAL_PASSWORD; API spending limit set at the provider | A public app with our API key could be misused; cost control is a product requirement |
| 39 | Deploy on Streamlit Community Cloud from GitHub; no local Python setup needed | Lowest-effort path for a PM-led prototype |

## Open questions (Stage 2)
- 🚩 **Riskiest strategic question:** is the information disorganized, or missing? See assumptions.md for the full ranked list.
- **Riskiest assumption from discovery so far:** pre-appointment calls confirm logistics but leave out preparation instructions.
- How often do instructions leave out required items?
- Do patients withhold information because they fear rescheduling?
- Is the pain stronger for people new to US healthcare, or for busy working adults?
- Do after-visit tasks (for example, dropping off a sample) cause similar problems?

## Candidate features (evaluate in Stage 4)
- Quick capture of spoken instructions (for example, typing a note right after the clinic's call)
- Question preparation for the doctor (competitors: AHRQ QuestionBuilder, ChatGPT)
- "Flag missing information": moving toward core value (competitor analysis)
- Photo upload for paper documents (desk research: not all patients use portals)
- Data minimization: upload only the instructions page, or paste text (desk research: low trust in health-tech companies)
- Reminders (email/SMS)
- "Ask the clinic" checklist items for information missing from documents
- After-visit task tracking
