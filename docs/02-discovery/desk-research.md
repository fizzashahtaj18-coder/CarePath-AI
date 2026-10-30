# Desk Research: Secondary Evidence

**Stage:** 2, Discovery
**Purpose:** Check CarePath AI's assumptions against published research *before* and *alongside* the email interviews.
**Date:** October 30, 2026

> **Important:** Desk research tells us what is true *in general* (across the US, in other settings, sometimes years ago). It does **not** replace hearing from our own target users. Each finding below is marked with how it changes our confidence, and what the interviews still need to answer.

---

## Summary

| # | Assumption | What the research suggests | Effect on confidence |
|---|---|---|---|
| 3 | Information arrives **in writing** | Spoken instructions are poorly remembered, and referral information is often incomplete or missing | ⬇️ **Weakened.** Supports the "missing information" direction |
| 4 | Documents are **digital** | Most US adults now use patient portals, but not all; almost nobody combines records from different portals | ↔️ **Partly supported.** A real gap exists, but not everyone is digital |
| 5 | Patients are **willing to upload** to a new website | Trust in health-tech companies is low; trust in clinicians is high | ⬇️ **Weakened.** This is a serious risk |
| 2 / 1 | Patients miss items; instructions are incomplete | Strong evidence of forgotten instructions and incomplete referral communication | ⬆️ **Supported** (in general) |
| 9 | Admin-only avoids medical-device regulation | FDA excludes some administrative software from the device definition, but the exclusion is written for *healthcare facilities*. A separate privacy rule (FTC) likely applies to us | ↔️ **Unclear, plus a new obligation found** |
| New | Low health literacy | Only about 1 in 8 US adults has proficient health literacy | 💡 New design requirement |

---

## Findings by assumption

### #3 and #2: Is information written down, remembered, and complete?

- **Patients forget most spoken medical information.** A widely cited review (Kessels, 2003) estimates that **40–80% of medical information** given by practitioners is forgotten immediately. Forgetting increases with the amount of information. The review also notes that **written information is remembered better** than spoken, and recommends backing up spoken instructions with written or visual material.
- **Referral communication is often incomplete.** In a US study at an academic medical center (Gandhi et al., 2000), **68% of specialists said they received no information from the referring doctor before the referral visit.** Respondents named inadequate referral letter content and lack of timeliness as major problems.
- **Missing reports are a common gap.** A review of doctors' letters (Medical Journal of Australia, 2002) found that **missing reports of previous investigations** were among the most serious and common problems in referral letters. This matches the founder's own experience with previous blood reports.
- **Patients become the messengers.** Researchers studying VA referrals describe patients being asked to fill information gaps for the specialist, acting as human "thumb drives."

**What this means:** The evidence supports the problem in general, but it **weakens assumption #3**. If key information is often spoken (and forgotten) or missing from referral letters entirely, a product that only organizes uploaded documents will miss part of the problem. This strengthens the case for the candidate feature **"Ask the clinic" checklist items**.

**Still to learn from interviews:** For *first-time patients specifically*, what came in writing vs. verbally vs. not at all? (Q3, Q4)

### #4: Are documents digital?

- **Portal use is now mainstream.** According to ASTP/ONC data, **65% of US patients were offered patient portal access and logged in in 2024**, up from 25% in 2014.
- **But not everyone.** A 2022 ONC analysis noted that just under half of individuals were **not offered or did not access** their online medical records that year. Portal use is uneven across groups.
- **Nobody combines their records.** In 2022, **98% of individuals did not use an app** to combine medical information from different patient portals.

**What this means:** Many patients *can* get documents digitally, but they're scattered across portals, and nobody combines them. That is a real opportunity. But some patients will only have paper, so **photo upload** (taking a picture of a paper letter) may be essential, not optional. Interviews must check this.

**Still to learn:** Where were *our* participants' documents? (Q5)

### #5: Will patients upload health documents to a new website?

- **Low trust in health-tech companies.** Rock Health's 2022 survey of 8,000+ US adults found that **70%** would share health information with their clinicians, but only **15%** with health technology companies and **7%** with tech companies outside healthcare. Trust had *fallen* since 2020.
- **Trust depends on who endorses the app.** A Pew survey (reported by Health Populi) found that **3 in 4 consumers** were comfortable sharing health information with apps **pre-approved by doctors and hospitals**.
- **Control matters.** An international survey study (UCL / *Data & Policy*) found that willingness to share health data depends on users' **data literacy and sense of control**, and that more granular data controls could improve acceptance.

**What this means:** This is CarePath AI's **most serious risk** so far. Even a perfect checklist fails if patients won't upload. Possible responses to explore later (Stage 4/7, not decided now):
- Minimize data: let users **upload only the instructions page**, or **paste text**, not full medical records
- Clear controls: easy delete, no data selling, plain-language privacy notice
- Long-term: distribution through clinics, since endorsement by a trusted provider increases willingness

**Still to learn:** What would make *our* participants trust it, or not? (Q9)

### #9: Regulation and privacy

- **FDA:** The 21st Century Cures Act (Section 3060) excluded certain software functions from the definition of a medical device, including software for **administrative support of a health care facility**. The FDA notes that these exclusions depend on software being **unrelated to diagnosis, treatment, or prevention** of disease. CarePath AI is patient-facing, not a facility tool, so the fit is **not clean**. Its strongest protection is the boundary rule: it never diagnoses, treats, or advises.
- **Privacy (new finding):** HIPAA generally applies to healthcare providers, insurers, and their business partners, not to consumer apps acting on their own. However, the **FTC's Health Breach Notification Rule**, updated in 2024, **explicitly covers health apps not covered by HIPAA**. Covered companies must notify users and the FTC after a breach of health data.

**What this means:** A real version of CarePath AI would likely have privacy obligations under FTC rules even without HIPAA. For the portfolio prototype, we use synthetic data only and make **no compliance claims**. *This is not legal advice. A real launch would require review by a qualified lawyer.*

### New: Health literacy is a design requirement
- The 2003 National Assessment of Adult Literacy found that **only 12% of US adults had proficient health literacy**; 14% were below basic.
- One of the tasks used to measure health literacy was working out what is permitted to drink **before a medical test**, using short instructions. That is exactly the kind of preparation instruction CarePath AI handles.

**What this means:** Checklist items must use **plain language**, short sentences, and specific actions. This will become a non-functional requirement in the PRD (Stage 5).

---

## Implications for CarePath AI

1. **The general problem is real.** Forgotten instructions and incomplete referral information are well documented.
2. **"Organize my documents" alone may not be enough.** Evidence points toward missing and spoken information. Interviews should confirm this for first-time patients.
3. **Trust is the biggest adoption risk.** Privacy and data minimization need to be designed in from the start, not added later.
4. **Paper still matters.** Photo upload may be required.
5. **Plain language is required**, not a nice-to-have.

---

## Sources

1. Kessels RPC. *Patients' memory for medical information.* J R Soc Med. 2003;96(5):219–222. https://pmc.ncbi.nlm.nih.gov/articles/PMC539473/
2. Gandhi TK et al. *Communication breakdown in the outpatient referral process.* J Gen Intern Med. 2000;15(9):626–631. https://pmc.ncbi.nlm.nih.gov/articles/PMC1495590
3. *Improving doctors' letters.* Medical Journal of Australia. 2002;177(9). https://www.mja.com.au/journal/2002/177/9/improving-doctors-letters
4. Healthcare Innovation. *Medical referrals: Closing the communication loop to improve care and avoid delays* (Regenstrief/VA study). https://www.hcinnovationgroup.com/clinical-it/electronic-health-record-electronic-medical-record-ehr-emr/article/13011354/medical-referrals-closing-the-communication-loop-to-improve-care-and-avoid-delays
5. TechTarget. *Patient portal utilization growth driven by doc engagement* (ASTP/ONC 2024 data). https://www.techtarget.com/patientengagement/news/366627154/Patient-portal-utilization-growth-driven-by-doc-engagement
6. ONC Data Brief No. 69. *Individuals' Access and Use of Patient Portals and Smartphone Health Apps, 2022.* https://www.healthit.gov/sites/default/files/2023-10/DB69_IndividualsAccess-UsePatientPortals_508.pdf
7. Healthcare Innovation. *ONC Report: Survey Finds Increasing Patient Portal, App Usage.* https://www.hcinnovationgroup.com/clinical-it/patient-portals/news/53075809/onc-report-survey-finds-increasing-patient-portal-app-usage
8. eMarketer. *Consumers' high use of digital health tools doesn't match their data privacy concerns* (Rock Health 2022). https://www.emarketer.com/content/consumers-high-use-of-digital-health-tools-doesn-t-match-their-data-privacy-concerns
9. Health Populi. Pew Research Center survey on health data sharing. https://healthpopuli.com/?p=32196
10. Cambridge University Press blog. *Behavioural perspectives on personal health data sharing and app design.* https://www.cambridge.org/core/blog/wp-json/wp/v2/posts/64627
11. FDA. *Changes to Existing Medical Software Policies Resulting from Section 3060 of the 21st Century Cures Act* (presentation). https://fda.gov/media/132527/download
12. Federal Register. *Health Breach Notification Rule* (final rule, May 30, 2024). https://www.federalregister.gov/documents/2024/05/30/2024-10855/health-breach-notification-rule
13. FTC Business Blog. *Updated FTC Health Breach Notification Rule puts new provisions in place to protect users of health apps.* https://www.ftc.gov/business-guidance/blog/2024/04/updated-ftc-health-breach-notification-rule-puts-new-provisions-place-protect-users-health-apps
14. U.S. Department of Education, NCES. *The Health Literacy of America's Adults: Results from the 2003 National Assessment of Adult Literacy.* https://nces.ed.gov/pubs2006/2006483.pdf
15. Michigan State University Extension. *National measures of health literacy.* https://www.canr.msu.edu/news/national_measures_of_health_literacy
