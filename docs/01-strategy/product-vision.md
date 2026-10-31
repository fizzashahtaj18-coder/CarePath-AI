# CarePath AI: Product Vision Document

**Stage:** 1, Product Vision & Strategy
**Status:** Approved for discovery (to be revised after Stage 2 user research)
**Last updated:** October 30, 2026

---

## 1. Vision
> **Every patient walks confidently into their specialist appointment prepared, so their attention goes to their health, not their paperwork.**

## 2. Mission
CarePath AI turns scattered appointment-related documents and instructions into an organized, editable preparation checklist, supported by source citations, so first-time specialist patients know exactly what to bring and do.

## 3. Why this product exists
CarePath AI started with the founder's own experience of a first specialist appointment in the US: arriving with a stack of papers, being unsure what was needed, never being told about required test preparation, and leaving without asking the questions that mattered. See [Origin Story](origin-story.md).

## 4. Problem statement
First-time specialist patients struggle to know what they need to bring and do before their appointment, because instructions come from different sources, are often given only verbally, and are sometimes incomplete.

Today, clinics usually call to confirm logistics (doctor, location, time), and patients rely on memory, paper documents, and asking front-desk staff. As a result, patients arrive unsure and anxious. They focus on paperwork instead of their health, may hold back information, and forget to ask their own questions. Missing steps lead to wasted trips, rescheduled tests, and delayed care.

Full version: [Problem Statement](problem-statement.md). This is a **hypothesis**, to be validated in Stage 2.

## 5. Target users
| | |
|---|---|
| **Primary user** | Adults in the **United States** attending a **non-emergency specialist appointment for the first time** (for example neurology, cardiology, dermatology, orthopedics) |
| **Not targeted (yet)** | Caregivers, returning patients, emergency care, clinics as users |
| **Segments to explore in Stage 2** | People new to the US healthcare system; busy working adults |

The target audience will not expand without evidence and an explicit decision recorded in the [Decision Log](decision-log.md).

## 6. Value proposition
> **For** first-time specialist patients **who** feel unsure what to bring and do before their appointment, **CarePath AI** is a web app **that** turns their appointment documents into one clear, editable checklist. **Unlike** phone calls, clinic portals, and general AI chatbots, **every checklist item links back to its source**, missing information is flagged, and the patient reviews and approves it. See [Competitor Analysis](../03-research/competitor-analysis.md).

| Value | Role |
|---|---|
| **Confidence:** knowing you're prepared | **Primary** |
| Organization: everything in one place | Secondary |
| Time savings: no searching, fewer wasted trips | Secondary |

## 7. Product objectives & success metrics
| Level | Objective | Metric | Initial target* |
|---|---|---|---|
| Long-term outcome (lagging) | Fewer wasted visits | % of appointments or tests rescheduled because of missing items | Not measurable in the prototype; tracked as the long-term goal |
| **Primary (leading)** | The checklist captures everything the documents require | **Checklist completeness:** % of required items correctly captured, on a synthetic test set | ≥ 90% |
| Secondary | Patients feel more prepared and trust the checklist | **Self-rated preparedness** (1–5), before vs. after, with test users | Average improvement ≥ 1 point |
| Trust guardrail | Every item can be verified | % of checklist items with a correct source citation | ≥ 95% |
| Safety guardrail | No medical advice is generated | Number of test cases where the product creates medical guidance not found in the documents | 0 |

\*Initial targets are starting points. They will be reviewed after Stage 2 and finalized in the PRD (Stage 5).

## 8. Product principles & boundaries
1. **Organizes and repeats; never advises.**
   - ✅ Repeats instructions written in the patient's own documents, always with a citation.
   - ⚠️ When a repeated instruction is medical (for example medication or fasting), it shows the original wording and adds: *"Confirm with your care team if you have questions."*
   - 🚩 When documents conflict, it points out the conflict and does not choose an answer.
   - ❌ Never creates medical guidance that isn't in the documents.
2. **The patient stays in control.** The AI drafts the checklist; the patient reviews, edits, and approves it.
3. **Cite everything.** No checklist item without a visible source.
4. **Say "I don't know."** When evidence is missing, the product says so instead of guessing.
5. **Controlled workflow, not an autonomous agent.** Each step is predictable and testable.
6. **Synthetic data only.** This prototype is not HIPAA compliant and is not clinically validated, and it will not claim to be.

## 9. MVP boundaries
### Candidate MVP features (to be prioritized in Stage 4)
1. Appointment setup
2. PDF and text document upload
3. AI extraction of administrative information
4. Document organization
5. Retrieval with source citations
6. AI-generated preparation checklist
7. Source citations on every item
8. Patient review and editing
9. Checklist progress tracking

> ✅ **Scope update (Stage 4):** This list was prioritized with RICE and MoSCoW. See [Prioritization & Roadmap](../04-prioritization/prioritization-and-roadmap.md) for the final MVP scope.
> **Proposed direction:** for the MVP, retrieval and citations cover the **patient's own uploaded documents**. A separate external knowledge base is a Phase 2 candidate.

### Out of scope
- Medical diagnosis, treatment, or medication recommendations
- Interpretation of test results
- Emergency triage
- Autonomous clinical decisions
- Direct hospital, EHR, or insurance integrations, including insurance verification

### Candidate features (decide in Stage 4, not committed)
- Reminders (email/SMS)
- "Ask the clinic" checklist items for information missing from documents
- After-visit task tracking (for example, dropping off a sample)

## 10. Key assumptions & risks
Full list: [Assumptions & Risk Map](assumptions.md).

**Top 3 to test first in Stage 2:**
1. Patients have their documents in **digital form**.
2. Patients are **willing to upload** health documents to a new website.
3. Required information arrives **in writing** rather than only verbally or not at all.

**Riskiest strategic question:** Is the main problem **disorganized** information or **missing** information? The answer may change what the MVP builds.

## 11. Next steps
- **Stage 2, Discovery:** Interview 5–8 recent first-time specialist patients to test the top assumptions.
- Update this document, the problem statement, and the assumptions map based on what we learn.
