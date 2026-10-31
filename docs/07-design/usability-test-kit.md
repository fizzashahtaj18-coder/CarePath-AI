# Usability Test Kit: Wireframes v0.1

**Stage:** 7, UX · **Goal:** Find out whether people can use the three wireframe screens without help, and whether they'd trust the checklist.
**Sessions:** 3–5 people · about 15 minutes each · in person or on a video call with screen sharing
**Prototype:** the [interactive design canvas](https://claude.ai/artifact/FEvitTPi9QAPwfRSywkc5m). Open it, click **Play** on screen 1, and share your screen.

> All data in the wireframes is synthetic. Never ask participants to use their own documents.

---

## Who to test with
- Adults who have been to a specialist (first-time ideal, but anyone who has been a patient is fine for usability)
- **Not** people who have seen the project before
- Friends and family are OK for a portfolio usability test. Note it as a limitation

## Before the session (2 minutes)
- [ ] Prototype open in **Play** mode on screen 1 ("Set up & add documents")
- [ ] This sheet open to take notes
- [ ] Ask: "Is it OK if I take notes? I won't record your name."

---

## Script: read this out loud

> "Thanks for helping! I'm testing an early design for a website that helps people prepare for a first specialist appointment. **I'm testing the design, not you.** There are no wrong answers. If something is confusing, that's the design's fault, and it's exactly what I need to know.
>
> Please **think out loud** as you go: say what you're looking at, what you expect, and what surprises you. I'll mostly stay quiet so I don't influence you."

**Rule for you:** don't help, don't explain, don't defend the design. If they're stuck for 30 seconds, say: *"What would you try next?"* If still stuck, move to the next task and mark it **failed**.

---

## The 5 tasks

Read each task exactly as written.

| # | Say this | Success looks like | Tests |
|---|---|---|---|
| 1 | "The clinic just called you. Show me how you'd add what they told you." | Finds **Paste text**, adds a label | Paste text is discoverable |
| 2 | *(Click Create my checklist first.)* "You're not sure 'Photo ID' is right. How would you check where it came from?" | Clicks **Show source**, finds the highlighted sentence | Citation design |
| 3 | "What should you do about the arrival time?" | Says they'd **ask the clinic** which time is correct | Conflict design |
| 4 | "Is there anything you should ask the clinic before your visit? Why are those there?" | Finds both questions; understands they're **not in the documents** | Missing-information design |
| 5 | *(Click Approve checklist.)* "You've packed your photo ID and insurance card. Show me." | Checks both items; reads the progress | Progress tracking |

## Two questions at the end
1. "How much would you **trust** this checklist, from 1 (not at all) to 5 (completely)? Why that number?"
2. "Would you upload **your real** appointment documents to a site like this? What would make you more or less comfortable?"

Thank them. Done.

---

## Note sheet (copy once per person)

```
Participant: T1 (no names)     Date:            Has seen a specialist? Y / N

Task 1 – Paste text:        Success / Partial / Failed     Time stuck:
  Notes:
Task 2 – Show source:       Success / Partial / Failed
  Notes:
Task 3 – Conflict:          Success / Partial / Failed
  Notes:
Task 4 – Ask the clinic:    Success / Partial / Failed
  Notes:
Task 5 – Progress:          Success / Partial / Failed
  Notes:

Trust (1–5):      Why:
Upload real documents? Y / N / Maybe     Why:

Most surprising thing they said:
```

---

## Results (fill in after 3–5 sessions)

| Task | T1 | T2 | T3 | T4 | T5 | Success rate | Pass? (≥ 4 of 5, or 3 of 3) |
|---|---|---|---|---|---|---|---|
| 1 Paste text | | | | | | | |
| 2 Show source | | | | | | | |
| 3 Conflict | | | | | | | |
| 4 Ask the clinic | | | | | | | |
| 5 Progress | | | | | | | |
| Trust (avg 1–5) | | | | | | | |
| Would upload (Y/N/Maybe) | | | | | | | |

**Top 3 problems found** (most severe first):
1.
2.
3.

**Design changes decided:**

**Limitations:** friends and family; small sample; wireframes, not a working product.

> 💬 **Interview talking point:** *"Before writing code, I ran a 15-minute usability test with five tasks. It showed [top problem], so I changed [design change] before building."*
