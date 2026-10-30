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

## Open questions (Stage 2)
- 🚩 **Riskiest strategic question:** is the information disorganized, or missing? See assumptions.md for the full ranked list.
- **Riskiest assumption from discovery so far:** pre-appointment calls confirm logistics but leave out preparation instructions.
- How often do instructions leave out required items?
- Do patients withhold information because they fear rescheduling?
- Is the pain stronger for people new to US healthcare, or for busy working adults?
- Do after-visit tasks (for example, dropping off a sample) cause similar problems?

## Candidate features (evaluate in Stage 4)
- Reminders (email/SMS)
- "Ask the clinic" checklist items for information missing from documents
- After-visit task tracking
