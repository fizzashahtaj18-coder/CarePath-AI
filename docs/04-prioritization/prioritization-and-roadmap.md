# Prioritization, MVP Scope & Roadmap

**Stage:** 4, Product Strategy & Prioritization
**Status:** 🟡 Approved for planning. Will be revisited when email interview results arrive.
**Inputs:** [Product vision](../01-strategy/product-vision.md) · [Interim findings](../02-discovery/findings.md) · [Competitor analysis](../03-research/competitor-analysis.md) · [Proto-personas](../03-research/proto-personas.md)

---

## 1. The constraint: time

| | Hours |
|---|---|
| Total budget (12 weeks × ~3 hours) | ~36 |
| Used in Week 1 (Stages 1–3) | ~3.5 |
| **Remaining** | **~33** |
| Non-build work (PRD 3, Jira 2, UX 3, architecture 1.5, evaluation 4, analytics 2, case study 3) | ~18.5 |
| **Available for building the MVP** | **~14.5** |

> Every feature costs hours from a fixed budget. **Prioritization means deciding what *not* to build.**

---

## 2. Product objectives (what prioritization serves)

1. **Completeness:** the checklist captures every required item in the documents (primary metric, target ≥ 90%)
2. **Trust:** every item is cited and verifiable (target ≥ 95% correct citations)
3. **Safety:** zero generated medical advice
4. **Confidence:** patients feel more prepared (secondary metric, target +1 point)

---

## 3. RICE scoring

**RICE = (Reach × Impact × Confidence) ÷ Effort**

| Factor | Scale used |
|---|---|
| **Reach** | How many of 10 target users would benefit (1–10) |
| **Impact** | How much it moves our objectives: 3 = massive, 2 = high, 1 = medium, 0.5 = low |
| **Confidence** | How sure we are about reach and impact: 100% / 80% / 50% / 30%. **Lowered where evidence is weak** (for example, waiting for interviews) |
| **Effort** | Estimated build hours for a beginner using AI coding help |

| Rank | ID | Feature | Reach | Impact | Conf. | Effort (h) | **RICE** |
|---|---|---|---|---|---|---|---|
| 1 | F3 | Paste text (including notes from a phone call) | 9 | 2 | 80% | 0.5 | **28.8** |
| 2 | F10 | Privacy controls: no storage by default, delete | 10 | 2 | 50% | 0.5 | **20.0** |
| 3 | F6 | Per-item source citations, verified | 10 | 3 | 80% | 2 | **12.0** |
| 4 | F8 | Safety guardrails: medical-instruction handling, conflicts, abstention | 10 | 2 | 80% | 1.5 | **10.7** |
| 5 | F1 | Appointment setup (specialty, date, clinic) | 10 | 0.5 | 100% | 0.5 | **10.0** |
| 6 | F9 | Patient review, edit, approve, and check off items | 10 | 2 | 100% | 2 | **10.0** |
| 7 | F2 | PDF upload + text extraction | 8 | 2 | 80% | 1.5 | **8.5** |
| 8 | F5 | AI extraction + checklist generation (structured output) | 10 | 3 | 80% | 4 | **6.0** |
| 9 | F7 | Missing-information flags + "Ask the clinic" items | 7 | 3 | 50% | 2 | **5.2** |
| 10 | F13 | Question preparation for the doctor | 6 | 1 | 50% | 1.5 | 2.0 |
| 11 | F4 | Photo upload of paper documents (OCR) | 5 | 2 | 50% | 3 | 1.7 |
| 12 | F11 | Document organization view | 6 | 0.5 | 50% | 1.5 | 1.0 |
| 13 | F12 | RAG over a curated "what to bring" knowledge base | 6 | 1 | 50% | 4 | 0.8 |
| 14 | F14 | Reminders (email/SMS) | 5 | 1 | 50% | 3 | 0.8 |
| 15 | F15 | After-visit task tracking | 4 | 1 | 30% | 2 | 0.6 |

**Notes on the scores**
- **F3 (paste text) ranks first** because it is almost free to build and serves three needs at once: digital text, typed-up paper letters, and notes from a phone call (the "spoken and forgotten" problem from discovery).
- **F7 (missing-information flags)** has low confidence (50%) because the "missing information" finding is still interim. Its impact is the highest possible, because it is a core differentiator against competitors.
- **F10 (privacy)** has low confidence because we don't yet know how much privacy controls change willingness to upload. But it is cheap, and trust is our biggest risk.

---

## 4. MoSCoW: the MVP decision

RICE ranks features. **MoSCoW decides.** Some features are **Must** regardless of score because the product is unsafe or meaningless without them.

### ✅ Must have (MVP): ~14.5 hours
| ID | Feature | Why it's a Must |
|---|---|---|
| F1 | Appointment setup | Gives the checklist its context (minimal: specialty, date, clinic name) |
| F2 | PDF upload | Most portal documents are PDFs |
| F3 | Paste text | Highest RICE; covers phone-call notes |
| F5 | AI extraction + checklist | The core value |
| F6 | Verified citations | The core differentiator and trust mechanism |
| F7 | Missing-information flags | Addresses the biggest interim finding; differentiator |
| F8 | Safety guardrails | **Non-negotiable** in healthcare, whatever the score |
| F9 | Review, edit, approve, check off | Keeps the human in control; covers progress tracking |
| F10 | Privacy controls | Our biggest adoption risk is trust |

### 🟦 Should have (if time allows, Week 11)
| ID | Feature | Why not Must |
|---|---|---|
| F13 | Question preparation | Valuable for the "forgot my questions" pain, but competitors (QuestionBuilder, ChatGPT) already cover it |
| F4 | Photo upload (OCR) | Important for paper documents, but costly (3h). **Paste text is the MVP workaround** |

### 🟨 Could have (later)
| ID | Feature | Why not now |
|---|---|---|
| F11 | Document organization view | Low impact: the checklist *is* the organization |
| F12 | RAG over a curated knowledge base | See the RAG decision below |
| F14 | Reminders | Needs email/SMS infrastructure (3h); test demand in interviews first |

### ⛔ Won't have (this version)
| ID | Feature | Why |
|---|---|---|
| F15 | After-visit tasks | Different use case; low evidence |
| n/a | Medical advice, diagnosis, test interpretation, triage | Out of scope by product principle |
| n/a | EHR, hospital, or insurance integrations | Too costly; not needed to prove value |
| n/a | Native mobile app | A web app is enough for the MVP |

### ✂️ Cut line (if the build falls behind)
Cut in this order, protecting the core value:
1. **F2 PDF upload.** Paste text still works.
2. **F1 appointment setup.** Reduce it to a single text field.
3. **Never cut:** F5, F6, F7, F8, F9.

---

## 5. Key decision: Is RAG needed for the MVP?

The project brief says: *"Do not add AI simply for the sake of using AI."* So we tested the RAG decision honestly.

| Question | Answer |
|---|---|
| How much text does one patient have? | Usually 2–5 short documents (referral letter, instructions, notes), which fits easily in one LLM prompt |
| Is retrieval needed to find the right passage? | **No.** The whole set fits in context. Retrieval adds complexity without improving answers |
| How do we still get precise citations? | Split documents into **numbered chunks**, ask the LLM to cite chunk IDs and quote the exact text, then **verify the quote exists in the source with simple code** (deterministic, not AI) |
| When *does* RAG make sense? | When the knowledge source is **too large for a prompt**, for example a curated library of trusted "what to bring" guidance from many clinics and specialties (F12) |

**Decision:** The MVP uses **grounded generation with verified citations** over the patient's own documents, without vector-database RAG. **Full RAG (embeddings + Chroma) moves to F12, a "Could have"**, where it genuinely adds value. If time allows in Week 11, F12 is the preferred stretch goal because it also demonstrates RAG for the portfolio.

> 💬 **Interview talking point:** *"I planned to use RAG, then realized the patient's documents fit in the context window. Retrieval would add cost and complexity without improving answers. I kept the citation benefit through chunk IDs plus deterministic verification, and saved RAG for the knowledge-base feature, where the corpus is actually too large."*

---

## 6. MVP user flow (what we're building)

```
1. Set up appointment      → specialty, date, clinic
2. Add documents           → upload a PDF and/or paste text (including call notes)
3. CarePath AI processes   → extracts admin instructions → builds checklist
                             → cites each item → verifies citations
                             → flags medical instructions, conflicts, and likely gaps
4. Patient reviews         → edits, removes, adds, approves
5. Patient prepares        → checks items off ("4 of 6 done")
6. Patient deletes data    → one click (nothing stored by default)
```

---

## 7. Roadmap

### Now / Next / Later
| Horizon | Focus | Features |
|---|---|---|
| **Now (MVP, Weeks 2–10)** | Prove that a cited, safe checklist builds confidence | F1, F2, F3, F5, F6, F7, F8, F9, F10 |
| **Next (Week 11, if time)** | Close gaps for paper users and question prep; demonstrate RAG | F12, F13, F4 |
| **Later (beyond the portfolio)** | Scale and distribution | Reminders, clinic partnerships, caregiver accounts, after-visit tasks, more languages |

### 12-week plan
| Week | Stage | Deliverable |
|---|---|---|
| 1 ✅ | 1–3 | Vision, desk research, competitor analysis, proto-personas |
| 2 | 4 → 5 | This prioritization; **email interviews return**; start the PRD |
| 3 | 5 → 6 | PRD complete; Jira backlog |
| 4 | 7 | User flows + wireframes + Figma prototype |
| 5 | 8 + 12 (prep) | Architecture; **build the synthetic test set and evaluation plan *before* coding** |
| 6 | 9 | Extraction + checklist generation (F5), paste text (F3), setup (F1) |
| 7 | 9 | Citations + verification (F6), safety guardrails (F8) |
| 8 | 11 | Review, edit, approve, check off (F9); privacy (F10) |
| 9 | 9–11 | Missing-information flags (F7), PDF upload (F2) |
| 10 | 12 | Run the evaluation; fix the biggest failures |
| 11 | 13 (+ Should) | Analytics plan + dashboard; stretch: F12 RAG or F13 |
| 12 | 14 | Case study, README polish, interview presentation |

**Why build the test set (Week 5) before the code (Week 6)?** Writing synthetic documents with known correct checklists first defines what "good" looks like. Then every build step can be measured. This is called **evaluation-driven development**, and it is a strong signal of AI PM maturity.

---

## 8. Trade-offs we accepted

| We chose... | Over... | Because... |
|---|---|---|
| Paste text | Photo OCR | 0.5h vs. 3h; covers call notes too |
| Grounded generation with verified citations | Vector RAG in the MVP | Documents fit in context; less complexity |
| Missing-information flags | Document organization view | Higher impact; differentiates from competitors |
| No storage by default | User accounts and history | Trust is the biggest risk; less to secure |
| A web app | A mobile app | Faster to build; enough to test value |
| Safety guardrails as Must | More features | Healthcare product; non-negotiable |

## 9. What could change these priorities
- **Interviews show most information *is* in writing** → F7's confidence drops; F11 may rise
- **Interviewees mostly have paper** → F4 (photo upload) moves to Must
- **Interviewees won't upload at all** → F3 (paste) and F10 (privacy) become even more central; consider a "type your instructions" mode
- **Interviewees ask for reminders** → F14 moves up
