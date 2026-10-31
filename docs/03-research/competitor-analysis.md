# Competitor & Alternatives Analysis

**Stage:** 3, Research
**Date:** October 30, 2026
**Question:** What do first-time specialist patients use today to prepare, and where is the gap CarePath AI could fill?

> Personas will be created after the email interviews, because they must be based on real evidence. This analysis is based on public product information and can be done now.

---

## 1. The competitive landscape

Patients don't only "compete" between apps. They choose between **five types of alternatives**:

| Category | Examples | Who controls it | Main job |
|---|---|---|---|
| **A. Manual methods** | Clinic phone call, paper folder, notes app, asking family | Patient / clinic staff | Remember and carry everything |
| **B. Clinic pre-visit tools** | Epic MyChart eCheck-in, Phreesia | The clinic | Collect forms, insurance, and payments before the visit |
| **C. Health record aggregators** | Apple Health Records, Fasten Health | Patient | Combine clinical records from several providers |
| **D. General AI assistants** | ChatGPT Health (and other AI chatbots) | AI company | Answer health questions using the patient's records |
| **E. Visit-preparation tools** | AHRQ QuestionBuilder | Patient (government tool) | Prepare questions to ask the doctor |

---

## 2. Competitor profiles

### A. Manual methods (the real default)
- **What patients do:** Listen to the confirmation call, keep paper letters, ask the front desk, rely on memory.
- **Strengths:** Free, familiar, no technology or trust barrier.
- **Weaknesses:** Spoken instructions are easily forgotten (see [desk research](../02-discovery/desk-research.md)); nothing combines instructions from different sources; no way to check what's missing.
- **Threat level:** 🔴 **High.** This is what CarePath AI must beat. "Good enough" habits are the strongest competitor.

### B. Clinic pre-visit tools: MyChart eCheck-in, Phreesia
- **What they do:** MyChart eCheck-in lets patients update personal and insurance details, review medications and allergies, complete questionnaires, and sign forms, typically a few days before a scheduled visit. Some clinics also send notifications that list what to bring. Phreesia offers similar digital registration and intake for practices, and can send patients pre-visit instructions by text.
- **Strengths:** Built into the clinic's own systems; trusted; free for patients; connected to the appointment.
- **Weaknesses (from the patient's view):**
  - Designed for the **clinic's needs** (forms, insurance, payment), not the patient's preparation
  - Works for **one clinic at a time**, so the referral letter from the patient's *other* doctor isn't included
  - Depends on what each clinic chooses to set up; availability varies by clinic and appointment type
  - Opens only a few days before the visit
- **Threat level:** 🟠 **Medium-high.** If clinics improved their instructions, the problem would shrink. But clinics improve slowly and unevenly.

### C. Health record aggregators: Apple Health Records, Fasten Health
- **What they do:** Apple Health Records brings records from participating providers into one view on iPhone, covering categories like allergies, conditions, medications, lab results, and procedures. Fasten Health is an open-source, self-hosted personal health record that imports records from multiple providers.
- **Strengths:** Solve the "records spread across portals" problem; Apple's is free and built into the iPhone.
- **Weaknesses:**
  - Focus on **clinical data** (labs, medications), not **administrative instructions** (what to bring, fasting, arrive early)
  - No preparation checklist or task tracking
  - Apple Health Records is iPhone-only; Fasten requires technical setup
- **Threat level:** 🟡 **Low-medium.** A different job, but a possible future partner or data source.

### D. General AI assistants: ChatGPT Health
- **What it does:** OpenAI launched ChatGPT Health in January 2026 and rolled it out to US users 18+ in July 2026. Users can connect medical records from supported US health systems and apps like Apple Health. OpenAI says over 230 million people ask ChatGPT health and wellness questions each week. Preparing for doctor appointments is one of the uses OpenAI promotes.
- **Strengths:** Free or low cost; huge user base; can read records and documents; flexible conversation; strong brand.
- **Weaknesses (for this specific job):**
  - **General-purpose chat**, not a structured, trackable preparation checklist
  - Answers in conversation; **no per-item citation** back to the exact line in the patient's own letter
  - Designed to discuss health broadly, including medical topics, which brings risk. In July 2026, OpenAI was sued by a user who alleged ChatGPT gave dangerous medical recommendations (reported by Northeast Times / The Verge). CarePath AI's admin-only boundary avoids this category entirely.
  - The patient has to know **what to ask**. First-time patients often don't.
- **Threat level:** 🔴 **High.** This is the competitor interviewers will ask about: *"Why wouldn't a patient just use ChatGPT?"*

### E. Visit-preparation tools: AHRQ QuestionBuilder
- **What it does:** A free federal app that helps patients prepare and organize questions by visit type, take photos (for example insurance cards), and send their questions to email or a calendar. Information stays on the user's device.
- **Strengths:** Free, trusted government source, privacy-friendly (no data collected), directly addresses "forgetting to ask questions."
- **Weaknesses:** Doesn't read the patient's documents; no "what to bring" checklist; generic prompts rather than appointment-specific instructions; limited adoption (few App Store ratings).
- **Threat level:** 🟢 **Low.** But it proves the problem is recognized and shows a **privacy-first design** CarePath AI can learn from.

---

## 3. Feature comparison

| Capability | Manual | MyChart / Phreesia | Apple Health Records | ChatGPT Health | QuestionBuilder | **CarePath AI (planned)** |
|---|---|---|---|---|---|---|
| Reads the patient's own appointment documents | ❌ | 🟡 own clinic only | 🟡 clinical data only | ✅ | ❌ | ✅ |
| Works across different clinics and sources | 🟡 manually | ❌ | ✅ (participating providers) | ✅ | ✅ | ✅ |
| "What to bring and do" checklist | ❌ | 🟡 if the clinic sets it up | ❌ | 🟡 if asked | ❌ | ✅ |
| Citation to the exact source for each item | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ **Core differentiator** |
| Flags missing or conflicting information | ❌ | ❌ | ❌ | 🟡 not systematic | ❌ | ✅ (planned) |
| Administration only, never medical advice | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| Patient reviews and approves the output | n/a | n/a | n/a | ❌ | ✅ | ✅ |
| Progress tracking | ❌ | 🟡 eCheck-in tasks | ❌ | ❌ | ❌ | ✅ |
| Helps prepare questions for the doctor | ❌ | ❌ | ❌ | ✅ | ✅ | ❓ candidate |
| Free for patients | ✅ | ✅ | ✅ | ✅ (with paid tiers) | ✅ | ❓ |
| Already trusted by patients | ✅ | ✅ | 🟡 | 🟡 | ✅ | ❌ **Must earn it** |

---

## 4. Gaps & opportunities

1. **No one turns *all* of a patient's appointment instructions into one verified checklist.** Clinic tools cover one clinic; aggregators cover clinical data; AI chatbots answer whatever is asked.
2. **No one cites the source of each instruction.** This is CarePath AI's clearest differentiator, and it directly addresses the trust problem found in desk research.
3. **No one systematically spots what's *missing*.** For example: "Your referral letter doesn't mention test preparation. Ask the clinic." This fits the "missing information" finding.
4. **The "forgot my questions" pain is only partly solved.** QuestionBuilder and ChatGPT help, but neither is connected to a preparation checklist.

---

## 5. Differentiation

> **CarePath AI is the only tool focused entirely on getting first-time specialist patients ready: it turns their appointment documents into a checklist where every item is cited, missing information is flagged, and nothing is medical advice.**

### Answering the hard interview question: "Why not just use ChatGPT?"

| ChatGPT Health | CarePath AI |
|---|---|
| Answers what you ask | Tells you what you didn't know to ask |
| A conversation | A checklist you can track to completion |
| General answers | Every item linked to the exact line in your document |
| Discusses medical topics | Administration only; repeats your documents, never advises |
| A broad health space | One focused job: be ready for this appointment |

**Honest risk:** ChatGPT Health or a similar product could add a "prepare for my appointment" checklist feature. CarePath AI's defense is **focus, citations, and the safety boundary**, not technology. In an interview, acknowledge this threat openly.

---

## 6. Implications for CarePath AI

| # | Implication | Where it goes |
|---|---|---|
| 1 | Citations are the core differentiator, so citation quality must be a top evaluation metric | PRD / Stage 12 |
| 2 | "Flag missing information" moves from nice-to-have toward **core value** | Stage 4 prioritization |
| 3 | Question preparation could address the "forgot my questions" pain | Candidate feature, Stage 4 |
| 4 | Learn from QuestionBuilder's privacy-first design (minimal data, clear controls) | Stage 7 design, Stage 12 |
| 5 | Long-term distribution could be **through clinics**, since patients trust them most | Viability (assumption #8) |
| 6 | Add an interview question: *"Have you ever used an AI chatbot to prepare for an appointment?"* | Email interview follow-ups |

---

## Sources

1. OpenAI. *Introducing ChatGPT Health* (January 7, 2026; updated July 23, 2026). https://openai.com/index/introducing-chatgpt-health/
2. OpenAI. *Launching Health in ChatGPT* (July 23, 2026). https://openai.com/index/health-in-chatgpt/
3. FourWeekMBA. *ChatGPT Health Launches: 230 Million Users Ask Health Questions Weekly.* https://fourweekmba.com/chatgpt-health-launches-230-million-users-ask-health-questions-weekly/
4. Leanware. *ChatGPT Health Launch.* https://leanware.co/insights/chatgpt-health-launch
5. Northeast Times. *OpenAI rolls out ChatGPT Health to all US users* (July 24, 2026). https://northeasttimes.com/?p=159203
6. M Health Fairview. *MyChart eCheck-In tip sheet.* https://mhealthfairview.org/-/media/MHealthFairview/Project/MHealthFairviewOrg/PDFs/Video-Visits/MyChart-eCheck-In.pdf
7. The Oregon Clinic. *eCheck-In Information.* https://www.oregonclinic.com/check-in-form-information
8. Hartford HealthCare. *eCheck-in Virtual Registration.* https://hartfordhealthcare.org/patients-visitors/patients/virtual-registration
9. Phreesia. *Phreesia for health systems.* https://www.phreesia.com/healthsystems/
10. AdvancedMD. *Phreesia partner overview.* https://www.advancedmd.com/?p=162351
11. Apple Health Records overview (IntuitionLabs). https://intuitionlabs.ai/software/patient-engagement-digital-health/patient-portals-and-phr/apple-health-records
12. Fasten Health (self-hosted alternatives listing). https://selfhostyourself.com/alternative-to/apple-health-records
13. AHRQ. *QuestionBuilder App.* https://www.ahrq.gov/patient-safety/question-builder.html
14. Fierce Healthcare. *AHRQ launches app to help patients prepare for medical visits.* https://fiercehealthcare.com/tech/ahrq-launches-app-to-help-patients-prepare-for-medical-visits
15. Apple App Store. *AHRQuestionBuilder.* https://apps.apple.com/us/app/-/id1455119729
