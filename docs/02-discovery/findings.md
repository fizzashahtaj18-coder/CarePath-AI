# Discovery Findings

**Stage:** 2, Discovery
**Status:** 🟡 **Interim findings.** Based on the founder's experience, published research, and **3 early email responses** (Part B). More qualifying interviews and follow-up answers are pending.

> **Why interim findings?** PMs often have to make early decisions before research is complete. This document separates what we know from **secondary evidence** (published research) and **founder experience** (one person) from what we will learn from **primary evidence** (our own interviews). Each finding is labeled with its evidence type and strength.

---

## Evidence sources

| Source | Type | Strength | Details |
|---|---|---|---|
| Founder's experience | Autoethnography (n = 1) | Weak alone; useful for generating hypotheses | [Origin story](../01-strategy/origin-story.md) |
| Published research | Secondary | Medium: large samples, but general (not specific to first-time specialist patients; some studies are older or from outside the US) | [Desk research](desk-research.md), 15 sources |
| Competitor analysis | Secondary | Medium | [Competitor analysis](../03-research/competitor-analysis.md) |
| Email interviews | Primary (n = 3 early responses; 0 fully screened yet) | Early; limited by a shorter question set and unconfirmed screening | Part B |

---

# Part A: Interim findings

## Findings by assumption

| # | Assumption | Founder experience | Secondary research | Interim verdict |
|---|---|---|---|---|
| 1 | Calls cover logistics, not preparation | ✅ The call covered doctor, location, and time only | No direct data found | 🟡 **Plausible.** Needs interviews |
| 2 | Patients often miss items | ✅ Missed fasting; previous reports not shared | ✅ 40–80% of spoken medical information is forgotten immediately (Kessels, 2003) | 🟡 **Likely.** Supported in general |
| 3 | Information arrives in writing | ❌ Key instructions were spoken or never given | ❌ Spoken information is poorly remembered; 68% of specialists received no information from the referring doctor before the visit (Gandhi et al., 2000) | 🟠 **Probably false, or only partly true** |
| 4 | Documents are digital | ❓ Mostly paper | 🟡 65% of patients were offered a portal and logged in (2024); 98% don't combine records across portals (2022) | 🟡 **Mixed.** Many digital, many not |
| 5 | Willing to upload documents | ❓ Not tested | ❌ Only 15% would share health data with health-tech companies, vs. 70% with clinicians (Rock Health, 2022) | 🔴 **Serious risk** |

## Pain points (interim)

| Pain point | Evidence | Strength |
|---|---|---|
| Spoken instructions are forgotten | Founder (fasting, sample drop-off); Kessels review | Medium |
| Required items are never communicated | Founder (previous reports); referral communication studies | Medium |
| Records are scattered across portals and paper | Founder; ONC data | Medium |
| Anxiety about rescheduling changes behavior (withholding information) | Founder only | **Weak.** A key interview question |
| Preparation stress crowds out health questions | Founder only; AHRQ built QuestionBuilder because patients arrive with unprepared questions | Weak-medium |
| Low health literacy makes instructions hard to follow | NAAL: only 12% of US adults have proficient health literacy | Medium (general population) |

## Key question: disorganized or missing information?

**Interim answer: both, and *missing* may matter more than we first assumed.**

| Type | Evidence |
|---|---|
| Information exists but is scattered | ONC: patients rarely combine records across portals |
| Information was spoken and forgotten | Kessels review; founder's fasting and sample examples |
| Information was never given | Referral studies; founder's previous-reports example |

## Interim decision: **Revise (provisional)**

The general problem is well supported, but the original hypothesis ("patients struggle to *organize* documents") is too narrow.

**Revised problem direction (provisional):**
> First-time specialist patients don't reliably know what to bring and do, because some instructions are **scattered**, some are **spoken and forgotten**, and some are **never given**.

**Product implications (to confirm in Stage 4):**
1. **Organize and cite** what *is* in the documents (the original MVP core)
2. **Flag what's likely missing** and suggest "Ask the clinic" questions (moves toward core value)
3. **Allow quick capture of spoken instructions**, for example typing a note right after the confirmation call (new idea)
4. **Design for trust from day one**: upload only what's needed, paste text instead of full records, easy delete
5. **Support photos of paper documents**

**What would change this decision:** If interviews show that most participants received complete written instructions and simply needed them organized, we return to the original hypothesis.

## Limitations
- Only 3 early interview responses, none fully screened yet (see Part B). **Part A must not be presented as validated user research.**
- The founder's experience is one person and may not represent others.
- Secondary sources are general, not specific to first-time specialist patients; some are older or from outside the US.

---

# Part B: Email interview results

**Status:** 🟡 3 early responses received (Round 1). Follow-ups, screening checks, and consent are pending.

> **Privacy:** participants are identified only as P1–P3. Names are kept privately, outside GitHub. Health details are generalized. **No direct quotes are included until each participant agrees to be quoted.** Answers below are paraphrased.

## ⚠️ Method note: Round 1 used a shorter question set

Round 1 was sent with **7 general questions**, not the 10-question [interview kit](email-interview-kit.md):

1. Tell me about your last specialist appointment. 2. How did you prepare for it? 3. What documents did you need? 4. What was difficult or confusing? 5. Did you forget anything? 6. How did you prepare questions? 7. What tools did you use?

**What this means:** Round 1 gives useful evidence on preparation, forgetting, documents, confusion, and tools. It gives **no direct evidence** on the three riskiest assumptions: written vs. spoken instructions (#3), digital vs. paper documents (#4), and willingness to upload (#5). It also didn't screen for **first visit with that specialist** or **US-based**. The follow-up emails ask these questions. Future participants receive the full 10-question kit.

> 💬 **Interview talking point:** *"My first round used a looser question set, so it couldn't test my riskiest assumptions. I noticed this, kept those assumptions marked 'untested' instead of over-claiming, and fixed it in the follow-ups."*

## Participants

| ID | Specialist type | Appointment timing | First visit with this specialist? | US-based? | Consent to quote | Counts toward target? |
|---|---|---|---|---|---|---|
| P1 | ENT | Not stated | ❓ Not asked | ❓ Not asked | ⏳ Pending | ⏳ After screening |
| P2 | Not stated | A few weeks before replying | ❓ Not asked | ❓ Not asked | ⏳ Pending | ⏳ After screening |
| P3 | Dermatology | October 2026 | ❌ Described as a follow-up visit | ❓ Not asked | ⏳ Pending | ❌ **Out of segment** (kept as comparison) |

**Qualifying responses so far: 0 confirmed** (target: 5–8).

## Individual summaries (paraphrased)

### P1 (ENT)
- **Preparation:** had specific instructions before the visit: avoid certain foods and exposures, and use a prescribed spray beforehand
- **Documents needed:** insurance card, ID, previous test reports from their physician
- **Confusing:** the testing process itself; unsure what to expect
- **Forgot:** a previous medication prescribed by their physician
- **Questions:** wrote questions down in advance
- **Tools:** none in particular
- **Open questions:** How were the preparation instructions given (written or spoken)? Did forgetting the medication cause a problem? Were the reports paper or digital?

### P2 (specialist not stated)
- **Preparation:** confirmed the date and time, collected previous medical reports, thought about what to discuss
- **Documents needed:** ID, insurance card, previous medical reports, a medication list
- **Confusing:** **knowing which documents to bring**; also nervous about what the doctor would ask
- **Forgot:** to ask one question about symptoms, remembered only after leaving
- **Questions:** wrote questions in phone notes as they came up
- **Tools:** phone calendar, map app, phone notes, email (appointment details)
- **Open questions:** Were the reports paper or digital? Were instructions written or spoken? What happened after the forgotten question?

### P3 (dermatology, follow-up visit: out of segment)
- **Preparation:** checked date, time, and location; noted their usual routine and concerns; arrived early
- **Documents needed:** photo ID only
- **Confusing:** knowing what information to provide; medical terminology in the recommendations
- **Forgot:** nothing. **Said a follow-up visit needs less preparation than a first visit would**
- **Questions:** a mental list
- **Tools:** phone reminders; the clinic's patient portal for appointment information and confirming attendance

## Results by assumption (Round 1)

| # | Assumption | Supports | Contradicts | Unclear | Verdict after Round 1 |
|---|---|---|---|---|---|
| 1 | Calls cover logistics, not preparation | — | — | P1 had prep instructions, but the channel is unknown | ⚪ **Untested** |
| 2 | Patients often miss items | P1 forgot a medication | P3 forgot nothing (but out of segment) | Whether forgetting had consequences | 🟡 **Weak early support** (1 of 2 in-segment) |
| 3 | Information arrives in writing | — | — | Not asked in Round 1 | ⚪ **Untested** |
| 4 | Documents are digital | — | — | P2 and P3 used email or a portal for **appointment details**, which isn't the same as their **documents** being digital | ⚪ **Untested** |
| 5 | Willing to upload documents | — | — | Not asked in Round 1 | ⚪ **Untested** |

## Additional insights (not tied to one assumption)

| Insight | Evidence | Product implication |
|---|---|---|
| **Knowing which documents to bring is confusing** | P2 named it as the most confusing part | Direct support for the core problem; strongest Round 1 signal |
| **Required documents are consistent** | P1 and P2 both needed ID, insurance card, and previous reports; P2 also a medication list | Matches the fixed **common-topics list** (FR-5.1). Early support for the "Ask the clinic" design |
| **Preparation often includes medical instructions** | P1 had to avoid certain things and use a prescribed spray | Confirms the need for **medical-instruction labeling** (FR-4.2) |
| **Forgetting covers items *and* questions** | P1 forgot an item; P2 forgot a question | Supports the "Added by you" question item; **not** a reason to generate questions with AI |
| **Patients already prepare questions themselves** | All 3 prepared questions (paper, phone notes, mental list) | Keep question support light (a user-added item). F13 stays "Should have" |
| **Preparation is spread across everyday tools** | Calendar, maps, notes, email, portal | CarePath AI must fit alongside these (export/print), not replace them |
| **First visits need more preparation than follow-ups** | P3, from outside the segment | Early support for the **first-time patient** focus |
| **Medical terminology is confusing** | P3; P1 (testing process) | Supports the plain-language requirement. Confusion *during* the visit is out of scope |

## Does Part B confirm or change the interim decision?

**Decision: keep "Revise (provisional)." No change to the MVP scope.**

- Round 1 **supports the core problem**: uncertainty about what to bring (P2), and forgotten items and questions (P1, P2).
- It **supports two design decisions**: the fixed common-topics list and medical-instruction labeling.
- It **doesn't yet answer the key question**: is the information disorganized, spoken, or missing? Assumptions #3, #4, and #5 remain **untested**.

## Next research steps
1. Send the follow-ups, including: first visit with this specialist? US-based? written or spoken instructions? paper or digital documents? comfortable uploading? consent to quote?
2. Move P1 and P2 to "qualifying" only if screening confirms it. Keep P3 as an out-of-segment comparison.
3. Recruit 3–6 more people with the **full 10-question kit**, and screen first.
4. Update this table and [assumptions.md](../01-strategy/assumptions.md) after Round 2.

## Round 1 limitations
- Small, convenience sample from the founder's network
- Shorter question set: the three riskiest assumptions weren't asked about
- Screening (first visit, US-based) not yet confirmed
- Consent to quote pending, so answers are paraphrased only
