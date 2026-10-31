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
