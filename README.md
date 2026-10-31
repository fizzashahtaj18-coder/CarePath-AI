# CarePath AI

**Helping first-time specialist patients walk into their appointment prepared and confident.**

CarePath AI is an AI Product Management portfolio project. It is a web application concept that turns scattered appointment documents and instructions into one editable preparation checklist, with a source citation for every item.

🚧 **Project status:** Sprint 0 in progress: synthetic evaluation set ✅ (10 sets) · Next: evaluation script (CPA-13) · email interviews continuing.

---

## The problem
First-time specialist patients often don't know exactly what to bring or do before their appointment. Instructions come from different sources, are often given only verbally, and are sometimes incomplete. Patients arrive anxious and focused on paperwork instead of their health. Missing items can mean wasted trips, rescheduled tests, and delayed care.

→ [Problem Statement](docs/01-strategy/problem-statement.md) · [Origin Story](docs/01-strategy/origin-story.md)

## Vision
> *Every patient walks confidently into their specialist appointment prepared, so their attention goes to their health, not their paperwork.*

→ [Product Vision Document](docs/01-strategy/product-vision.md)

## How it will work (MVP scope)
1. The patient sets up their appointment and uploads a PDF or pastes text, including notes from the clinic's phone call.
2. AI extracts the administrative instructions: what to bring, what to do, deadlines.
3. CarePath AI drafts a preparation checklist. **Every item links to its source**, and citations are verified by code.
4. It flags medical instructions, conflicting documents, and **likely missing information** ("Ask the clinic...").
5. The patient reviews, edits, and approves the checklist, then checks items off.

→ [Prioritization & Roadmap](docs/04-prioritization/prioritization-and-roadmap.md) · [PRD](docs/05-prd/prd.md)

## Product principles
- **Organizes and repeats; never advises.** CarePath AI is a healthcare-administration tool, not a medical advice chatbot.
- **Cite everything.** Every checklist item can be verified against its source.
- **The patient stays in control.** The AI drafts; the patient approves.
- **Controlled workflow, not an autonomous agent.**

## How success is measured
| Metric | Type |
|---|---|
| Checklist completeness (% of required items captured) | Primary |
| Self-rated preparedness, before vs. after | Secondary |
| Fewer appointments rescheduled for missing items | Long-term outcome |

## Project roadmap
| Stage | Focus | Status |
|---|---|---|
| 1 | Product vision & strategy | ✅ Complete |
| 2 | Discovery & user interviews | 🔄 Interim findings done; interviews pending |
| 3 | Personas & competitor analysis | 🔄 Competitors done; proto-personas pending validation |
| 4 | Prioritization & MVP scope | ✅ Complete |
| 5 | Product Requirements Document | 🟡 v0.1 draft |
| 6 | Agile backlog (Jira) | ✅ Backlog ready |
| 7 | UX & prototype | 🟡 Wireframes v0.1; usability tests pending |
| 8 | Technical & AI architecture | ✅ v0.1 |
| 9–11 | LLM, RAG & workflow build | |
| 12 | AI evaluation & responsible AI | |
| 13 | Product analytics | |
| 14 | Case study | |

## Repository structure
```
docs/
├── 01-strategy/
│   ├── product-vision.md     Product Vision Document
│   ├── problem-statement.md  Problem and success metrics
│   ├── assumptions.md        Assumptions & risk map
│   ├── decision-log.md       Key decisions and open questions
│   └── origin-story.md       Why this product exists
├── 02-discovery/
│   ├── desk-research.md       Published evidence on our assumptions
│   ├── email-interview-kit.md Interview emails and question plan
│   └── findings.md            Interim findings + interview results
├── 03-research/
│   ├── competitor-analysis.md Alternatives, gaps, and differentiation
│   └── proto-personas.md      Assumption-based personas (to validate)
├── 04-prioritization/
│   └── prioritization-and-roadmap.md  RICE, MoSCoW, MVP scope, roadmap
├── 05-prd/
│   └── prd.md                 Product Requirements Document (v0.1)
├── 06-agile/
│   ├── agile-and-jira-guide.md   Epics, sprints, DoR/DoD, team workflow
│   └── carepath-jira-import.csv  Jira import file (8 epics, 15 stories)
├── 07-design/
│   └── ux-design.md           User flow, information architecture, screens, test plan
└── 08-architecture/
    └── architecture.md        System diagram, components, model choice, cost, ADRs
```
```
config/
└── topics.yaml                Common administrative topics (PM-reviewed)
eval/
└── testset/                   10 synthetic document sets + answer keys (see its README)
```
More folders will be added as each stage begins.

## ⚠️ Data & safety
This project uses **only synthetic data**. No real patient documents or health information will ever be uploaded. CarePath AI is a portfolio prototype: it is **not HIPAA compliant, not clinically validated, and does not provide medical advice.**

## License
[MIT](LICENSE)
