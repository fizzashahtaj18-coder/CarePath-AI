# Agile Plan & Jira Backlog

**Stage:** 6, Agile & Jira
**Source:** [PRD v0.1](../05-prd/prd.md) · [Prioritization & Roadmap](../04-prioritization/prioritization-and-roadmap.md)
**Import file:** [carepath-jira-import.csv](carepath-jira-import.csv) (8 epics, 15 stories, 21 sub-tasks)

---

## 1. How the backlog is structured

```
Epic (a large goal, from the PRD)          e.g. E3: Citations & trust
 └── Story (user value, fits in one sprint)  e.g. US-4: See and verify where each item came from
      └── Sub-task (a piece of work, hours)  e.g. Write deterministic quote-verification function
```

| Level | Who writes it | Contains |
|---|---|---|
| **Epic** | PM | Goal + linked PRD requirements |
| **Story** | PM (with team input) | User story + acceptance criteria + story points |
| **Sub-task** | Engineers (here: you, with AI coding help) | Concrete technical steps |

**Story points** use the Fibonacci scale (1, 2, 3, 5, 8). They measure **relative size and uncertainty**, not hours. US-3 (generate checklist, 8 points) is the biggest and riskiest story because it holds the core AI behavior.

---

## 2. Epics

| Epic | Goal | Stories | Points |
|---|---|---|---|
| **E0** Foundation & evaluation | Test set + evaluation script **before** features | S0-1, S0-2, S5-1 | 13 |
| **E1** Appointment & document input | Get documents in | US-0, US-1, US-2 | 6 |
| **E2** Checklist generation | Core AI value | US-3 | 8 |
| **E3** Citations & trust | Verifiable output | US-4 | 5 |
| **E4** Safety guardrails | Never give medical advice | US-5, US-6, US-11 | 9 |
| **E5** Missing-information flags | Spot gaps | US-7 | 5 |
| **E6** Review, approval & progress | Human in control | US-8, US-9 | 8 |
| **E7** Privacy | Trust by design | US-10 | 2 |
| | | **Total** | **56** |

---

## 3. Sprint plan (1-week sprints, matching the roadmap)

| Sprint | Week | Sprint goal | Stories | Points |
|---|---|---|---|---|
| **Sprint 0** | 5 | *"We can measure quality before we build."* | S0-1 test set, S0-2 setup + evaluation script | 8 |
| **Sprint 1** | 6 | *"A patient can paste instructions and get a draft checklist."* | US-0, US-2, US-3 | 11 |
| **Sprint 2** | 7 | *"Every item is verified, and the product is safe."* | US-4, US-5, US-6, US-11 | 14 ⚠️ |
| **Sprint 3** | 8 | *"The patient is in control of their checklist and data."* | US-8, US-9, US-10 | 10 |
| **Sprint 4** | 9 | *"CarePath AI spots what's missing."* | US-7, US-1 | 8 |
| **Sprint 5** | 10 | *"The MVP meets its release criteria."* | S5-1 full evaluation + fixes | 5 |

⚠️ **Sprint 2 is the heaviest.** If it runs over, move **US-6 (conflicts)** to Sprint 3. Do not move US-11 (safety). Following the [cut line](../04-prioritization/prioritization-and-roadmap.md), **US-1 (PDF upload)** is the first story to drop if the whole plan falls behind.

**Why a sprint goal?** It's one sentence explaining *why* the sprint matters. When you have to choose what to drop mid-sprint, the goal tells you what to protect.

---

## 4. Definition of Ready (DoR)

A story can enter a sprint only when:
- [ ] It's written as a user story (*As a... I want... so that...*)
- [ ] It has clear, testable acceptance criteria (Given / When / Then)
- [ ] It's linked to an epic and a PRD requirement (FR-x.x)
- [ ] It's estimated in story points (8 or less; bigger stories get split)
- [ ] Dependencies are known (for example, US-4 needs US-3's chunking)
- [ ] Test cases exist in the synthetic test set (for AI stories)

## 5. Definition of Done (DoD)

A story is done only when:
- [ ] All acceptance criteria pass
- [ ] Code is committed to GitHub with a clear commit message that includes the Jira key (for example `CPA-12 Add quote verification`)
- [ ] **AI stories:** the evaluation script was run, and scores are recorded and didn't get worse
- [ ] **Safety check:** no new path to medical advice; disclaimers still visible
- [ ] No real patient data, no API keys in the repo
- [ ] The PM (you) has tried it as a user and accepted it

> **AI-specific DoD lines matter.** In normal software, "tests pass" is enough. In AI products, output can get worse without any code error, so every AI story must re-run the evaluation.

---

## 6. Set up Jira (your steps)

> Jira's screens change from time to time. If a button has a slightly different name, look for the closest match, or tell me what you see.

### Step 1: Create a free account and project
1. Go to https://www.atlassian.com/software/jira and sign up for the **free plan** with your email.
2. When asked, choose the **Scrum** template (not Kanban), because we're planning in sprints.
3. Choose a **team-managed** project (simpler for one person).
4. Name it **CarePath AI**. Set the key to **CPA**, so issues will be numbered CPA-1, CPA-2...

### Step 2: Import the backlog
1. Download `carepath-jira-import.csv`.
2. In Jira, open the **⚙️ settings** menu (top right) → **System** → **External system import** → **CSV**. *(If you don't see this, search Jira's help for "import CSV".)*
3. Upload the file and select your **CarePath AI** project.
4. Map the columns:

   | CSV column | Jira field |
   |---|---|
   | Work item ID | Issue ID |
   | Parent | Parent |
   | Issue Type | Issue Type |
   | Summary | Summary |
   | Description | Description |
   | Priority | Priority |
   | Labels | Labels |
   | Story Points | Story point estimate *(skip it if this field isn't offered)* |
   | Sprint (plan) | **Don't map.** You'll create sprints manually |

5. Run the import and check that you see 8 epics with stories under them.

**If the import fails:** create the 8 epics manually (section 2), then create each story and paste its description from the CSV. It takes longer, but it's good practice.

### Step 3: Create sprints
1. Open **Backlog**.
2. Click **Create sprint** six times: Sprint 0 to Sprint 5.
3. Drag stories into sprints following section 3.
4. Click each sprint's **⋯ → Edit sprint** and paste its **sprint goal**.

### Step 4: Connect GitHub (optional but impressive)
Jira can link commits to issues when the commit message includes the issue key (for example `CPA-12`). Search for "GitHub for Jira" in Jira's **Apps** menu to set this up. Then reviewers can trace any feature from requirement → story → code.

### Step 5: Take a screenshot for your portfolio
Once your backlog and sprints are set up, take a screenshot of the **Backlog** view and save it as `docs/06-agile/jira-backlog.png`.

---

## 7. How a PM uses Jira day to day

| Activity | When | What you do in Jira |
|---|---|---|
| **Backlog refinement** | Weekly | Re-order by priority; split big stories; check the DoR |
| **Sprint planning** | Start of each sprint | Set the sprint goal; pull in Ready stories; check total points vs. capacity |
| **Daily progress** | Each work session | Move cards: To Do → In Progress → Done |
| **Sprint review** | End of sprint | Demo what's done; did we meet the sprint goal? |
| **Retrospective** | End of sprint | Write a short note: what went well, what to change |
| **Re-prioritizing** | When evidence changes | For example, if interviews show most patients have paper, create a story for photo upload (F4) and move it up |

---

## 8. How a PM works with the team

In this project, you play every role. In interviews, explain how each role would work in a real team:

| Role | What the PM gives them | What the PM gets from them |
|---|---|---|
| **Designer** | Problem, personas, user journey, requirements | User flows, wireframes, prototype; usability findings |
| **Engineers** | Prioritized stories with acceptance criteria; the "why" | Effort estimates, technical risks, feasibility trade-offs (for example "RAG isn't needed for 5 documents") |
| **ML/AI engineer** | Quality targets, evaluation set, safety rules | Model choice, prompt design, evaluation results, cost per request |
| **QA** | Acceptance criteria, edge cases, safety test cases | Bug reports; confirmation that stories meet the DoD |
| **Stakeholders** (for example clinic partners, legal, leadership) | Roadmap, progress against goals, risks | Constraints (legal, compliance), feedback, approval |

> 💬 **Interview talking point:** *"In AI products, the PM owns the evaluation set and the quality bar, not just the feature list. I defined the test set and the release criteria before any code was written."*

---

## 9. Backlog summary

| Key | Type | Summary | Epic | Points | Sprint |
|---|---|---|---|---|---|
| S0-1 | Story | Create 10 synthetic document sets with known correct checklists | E0 | 5 | 0 |
| S0-2 | Story | Set up the project environment and an evaluation script | E0 | 3 | 0 |
| US-0 | Story | Enter appointment details | E1 | 1 | 1 |
| US-2 | Story | Paste text and phone-call notes as a document | E1 | 2 | 1 |
| US-3 | Story | Generate my draft checklist | E2 | 8 | 1 |
| US-4 | Story | See and verify where each item came from | E3 | 5 | 2 |
| US-5 | Story | Be warned about medical instructions | E4 | 3 | 2 |
| US-6 | Story | Know when documents disagree | E4 | 3 | 2 |
| US-11 | Story | Never receive medical advice | E4 | 3 | 2 |
| US-8 | Story | Edit, remove, add, and approve checklist items | E6 | 5 | 3 |
| US-9 | Story | Track progress and export my checklist | E6 | 3 | 3 |
| US-10 | Story | Delete my data | E7 | 2 | 3 |
| US-7 | Story | Find out what my documents don't mention | E5 | 5 | 4 |
| US-1 | Story | Upload PDF documents | E1 | 3 | 4 |
| S5-1 | Story | Run the full evaluation and fix the top failures | E0 | 5 | 5 |

*Full descriptions, acceptance criteria, and sub-tasks are in the CSV file.*
