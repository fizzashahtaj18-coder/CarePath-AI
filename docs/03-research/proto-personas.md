# Proto-Personas

**Stage:** 3, Research
**Status:** 🟡 **Assumption-based, partly informed by Round 1 interviews** (3 early responses, none screened yet). Not yet validated.

> **What is a proto-persona?** A persona built from the team's current knowledge (founder experience and published research) **before** user interviews are complete. It makes assumptions visible so they can be tested. Proto-personas are standard PM practice, as long as they are clearly labeled. These personas are **fictional composites**, not real people, and will be revised or replaced once email interview results are in ([findings.md](../02-discovery/findings.md), Part B).

Both personas are in the confirmed target audience (adults in the US attending a first, non-emergency specialist appointment). They explore the two segments flagged for discovery: **people new to US healthcare** and **busy working adults**.

---

## Persona 1: Amira, "The Newcomer"

| | |
|---|---|
| **Snapshot** | 30s, moved to the US two years ago, first referral to a US specialist |
| **Situation** | Received a referral from a primary care doctor; doesn't yet know how US referrals, insurance, and patient portals work |
| **Documents** | A paper referral letter, an insurance card, test results from a previous doctor (some from abroad), a text confirming the appointment |
| **Tech** | Comfortable with a smartphone; has a portal account but rarely uses it |

**Goals**
- Arrive with everything the clinic needs, so the appointment isn't rescheduled
- Understand what will happen at the visit
- Have time to ask the doctor her real health questions

**Frustrations**
- Doesn't know what US clinics usually expect ("Are these all the documents you need?")
- Instructions came by phone, quickly, in professional language
- Afraid that admitting something is missing will cost her the appointment

**Behaviors today**
- Carries every document she has "just in case"
- Asks the front desk for help when she arrives

**What CarePath AI must do for her**
- Turn her papers into one clear checklist in plain language
- Show *where* each instruction came from, so she can trust it
- Point out what might be missing, and what to ask the clinic, **before** the visit

**Evidence behind this persona**
- Founder's experience ([origin story](../01-strategy/origin-story.md))
- Adults who did not speak English before starting school make up 39% of adults with below basic health literacy (NAAL 2003, via MSU Extension)
- Spoken instructions are poorly remembered (Kessels, 2003)

**Early interview evidence (Round 1, not yet screened)**
- ✅ Supports: P2 said the most confusing part was **knowing which documents to bring**, and felt nervous about the doctor's questions
- ✅ Supports: P3 found **medical terminology** confusing → plain language matters
- ❓ Not yet tested: whether participants were new to US healthcare (not asked)

**Assumptions to validate**
- Do newcomers feel the pain more strongly than people familiar with US healthcare?
- Does fear of rescheduling lead others, not just the founder, to hold back information?
- Would she trust a website with her documents? What would build that trust?

---

## Persona 2: Daniel, "The Busy Professional"

| | |
|---|---|
| **Snapshot** | 40s, full-time job with long hours, first referral to a specialist |
| **Situation** | Booked the appointment weeks ago and squeezes preparation in between meetings |
| **Documents** | Spread across two patient portals, email, and a voicemail from the clinic |
| **Tech** | Heavy smartphone user; uses portals but finds them annoying |

**Goals**
- Prepare quickly, with minimal effort
- Avoid wasted trips and taking another day off work
- Know he's ready without double-checking everything

**Frustrations**
- Missed the clinic's call; the voicemail was rushed
- Instructions are split across portals and messages
- Realizes too late that a test required preparation

**Behaviors today**
- Skims messages, relies on memory, checks details the night before

**What CarePath AI must do for him**
- Bring everything together fast: upload or paste, then get a checklist
- Show clear progress ("4 of 6 done")
- Possibly remind him at the right time (reminders are a candidate feature)

**Evidence behind this persona**
- Most patients now use portals, and almost nobody combines records from different portals (ONC data)
- Spoken instructions are poorly remembered (Kessels, 2003)
- Founder's observation about working patients ([decision log](../01-strategy/decision-log.md), open questions)

**Early interview evidence (Round 1, not yet screened)**
- ✅ Supports: P2 managed preparation across **several everyday tools** (phone calendar, map app, phone notes, email)
- ✅ Supports: P2 still **forgot a question**, remembering it only after leaving
- ⚠️ Challenges: all three participants **already prepare questions themselves**, so question support should stay light
- ❓ Not yet tested: whether participants were working adults or felt time pressure (not asked)

**Assumptions to validate**
- Is time pressure, rather than lack of knowledge, the main problem for working adults?
- Would he spend 5 minutes setting up a checklist, or is that too much effort?
- Do reminders matter more to him than citations?

---

## Anti-persona: who CarePath AI is *not* for

| Anti-persona | Why not |
|---|---|
| **Someone looking for medical answers** ("What does my test result mean?") | CarePath AI is administration only. It never advises. These users should talk to their care team. |
| **An experienced patient with a chronic condition** who sees specialists often | They already know the routine; the pain is lower. Possibly a later segment. |
| **A caregiver managing someone else's appointments** | Out of scope for now (different permissions and privacy needs). Possibly a later segment. |
| **Someone with an urgent or emergency need** | Out of scope. They need immediate care, not a checklist. |

---

## How these personas guide decisions now

| Decision area | Amira (Newcomer) needs | Daniel (Busy Professional) needs |
|---|---|---|
| Core value | Understanding and confidence | Speed and certainty |
| Most important feature | Missing-information flags; plain language | Fast setup; progress tracking |
| Biggest risk | Trust and upload hesitation | Effort ("too much setup") |

**Provisional primary persona: Amira.** She matches the origin story and the primary value (confidence), and her needs (plain language, citations, missing-information flags) also help Daniel. Round 1's strongest signal ("which documents to bring" was confusing) fits Amira best. This will be confirmed or changed after screened interviews.

## Sources
- Founder experience: [origin-story.md](../01-strategy/origin-story.md)
- Desk research and sources: [desk-research.md](../02-discovery/desk-research.md)
- Competitor analysis: [competitor-analysis.md](competitor-analysis.md)
