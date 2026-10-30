# Assumptions & Risk Map

Every product is built on beliefs that might be wrong. This document lists CarePath AI's key assumptions, rates them by risk, and identifies which to test first.

## How assumptions are scored

- **Importance:** If this is wrong, does the product fail? High = 3, Medium = 2, Low = 1
- **Evidence gap:** How much proof do we have today? None = 3, Weak = 2, Strong = 1
- **Risk score = Importance × Evidence gap.** Higher scores are tested first.
- **Tie-breakers:** (1) Can it be tested in Stage 2 interviews? (2) If wrong, does the MVP change?

Risk types follow the four product risks: **Value** (do people want it?), **Usability** (can they use it?), **Feasibility** (can we build it?), **Viability** (does it work as a business, legally and financially?).

## Assumption map

| # | We believe that... | Risk type | Importance | Evidence | Score | How we'll test it |
|---|---|---|---|---|---|---|
| 1 | Pre-appointment calls confirm logistics but leave out preparation instructions | Value | High | Weak (founder's experience) | 6 | Interviews: what did the last call cover, and what did you learn later? |
| 2 | First-time specialist patients often miss a required item or preparation step | Value | High | Weak | 6 | Interviews: "Last time, was there anything you forgot or weren't told?" |
| 3 | Patients receive most required information **in writing**, so organizing it solves most of the problem | Value | High | Weak, and founder's examples point the other way | 6 | Interviews: what came in writing vs. verbally vs. not at all? |
| 4 | Patients have their documents in **digital form** (PDF, portal download, or photo) | Usability | High | None | **9** | Interviews: "Where were your documents: paper, email, or patient portal?" |
| 5 | Patients are **willing to upload** documents containing health information to a new website | Usability (trust) | High | None | **9** | Interviews: ask directly; note hesitation and conditions for trust |
| 6 | Patients will review and edit the AI checklist rather than trust it blindly | Usability | Medium | None | 6 | Prototype usability test (Stage 7) |
| 7 | An LLM can extract administrative instructions accurately, with correct citations | Feasibility | High | Weak (general LLM ability, untested on these documents) | 6 | Synthetic documents with a known correct checklist; measure completeness (Stage 9/12) |
| 8 | Someone will pay: patients, clinics, or employers/insurers | Viability | Medium (portfolio) / High (real business) | None | 6 | Interviews on perceived value; desk research on similar tools (Stage 3) |
| 9 | Staying administration-only keeps CarePath AI outside medical-device regulation | Viability (legal) | High | Weak | 6 | Desk research (Stage 12). No legal or compliance claims will be made. |

## Top 3 riskiest assumptions: test first in Stage 2

1. **#4: Documents are digital (score 9).** If patients mostly have paper, or have nothing at all, upload-based features cannot work.
2. **#5: Patients are willing to upload health documents (score 9).** Even a perfect AI fails if patients don't trust a new website with their information.
3. **#3: Information arrives in writing (score 6, wins the tie-break).** It is testable in interviews, and it decides the shape of the MVP. If most instructions are verbal or missing, a document organizer alone will not solve the problem, and the product should also help patients find out what to **ask the clinic**.

**Close fourth: #2 (patients often miss items).** It is foundational and will be covered by the same interviews.

### Why not the others first?
- **#7 (LLM accuracy)** is important but cheap to test without users, using synthetic documents. Value risks come first: a perfect AI that solves an unimportant problem is still a failure.
- **#8 (who pays)** can't be reliably validated in 5–8 interviews. People say "I'd pay" easily. It's a lower priority for a portfolio prototype.
- **#9 (regulation)** is handled by desk research and by the product's strict administration-only boundary.

## Status after desk research (October 30, 2026)
Desk research gives *general* evidence only. Interview results will be added after the email interviews. See [desk-research.md](../02-discovery/desk-research.md).

| # | Desk research signal | Status |
|---|---|---|
| 1, 2 | ⬆️ Supported in general: spoken instructions are widely forgotten; referral information is often incomplete | ⏳ Interviews pending |
| 3 | ⬇️ Weakened: much key information is spoken or missing, not written | ⏳ Interviews pending |
| 4 | ↔️ Partly supported: most adults use portals, not all; records are scattered | ⏳ Interviews pending |
| 5 | ⬇️ Weakened: low trust in health-tech companies; endorsement and user control help | ⏳ Interviews pending |
| 6, 7, 8 | No desk research yet | ⏳ Later stages |
| 9 | ↔️ Unclear: FDA admin exclusion targets facilities; FTC Health Breach Notification Rule likely applies | ⏳ Stage 12 |
