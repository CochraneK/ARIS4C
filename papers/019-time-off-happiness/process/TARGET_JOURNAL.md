# ARIS4C019 · Target Journal and Submission Adaptation v0.1

**Frozen for current working-paper cycle:** 2026-09-21  
**Primary target:** **Social Indicators Research**  
**Backup 1:** Applied Research in Quality of Life  
**Backup 2:** Journal of Happiness Studies

This is a journal-fit decision, not an acceptance prediction.

## 1. Primary target · Social Indicators Research

### Why it fits

The journal defines itself as an international/interdisciplinary journal for quality-of-life measurement and explicitly welcomes:

- measurement of well-being and quality of life;
- novel applications of existing indicators;
- work identifying factors or processes associated with higher/lower quality of life;
- domain-specific well-being;
- methodological work on analysis and measurement of social phenomena.

ARIS4C019 is now primarily a **social-indicator / identification-quality paper** rather than a claim that one labour policy reliably raises happiness. That framing matches the journal more closely than a purely psychological happiness outlet.

### Current submission requirements audited 2026-09-21

Official journal instructions currently state:

- double-anonymous peer review;
- manuscript and associated files must be anonymized;
- editable source files are required;
- Word is the preferred manuscript format (LaTeX also accepted for mathematical content);
- article length: **5,000–10,000 words including references**, average about 7,500;
- abstract: **150–250 words**;
- keywords: **4–6**;
- original research requires a **Data Availability Statement**;
- figures should be cited in order and captions belong in the manuscript;
- vector graphics are preferred as EPS for production, though current SVG masters can remain canonical during drafting;
- author details/declarations are partly entered through the current submission interface because the journal recently changed submission systems.

Official source:
- https://link.springer.com/journal/11205/aims-and-scope
- https://link.springer.com/journal/11205/submission-guidelines

## 2. Backup · Applied Research in Quality of Life

ARQOL is the official journal of ISQOLS and welcomes rigorous conceptual, methodological and empirical work on quality of life and well-being, especially work with practical relevance.

Its current format requirements are closely aligned with SIR:

- double-anonymous review;
- 5,000–10,000 words including references;
- abstract 150–250 words;
- 4–6 keywords;
- Data Availability Statement required for original research.

This makes ARQOL a low-friction backup if the SIR framing is judged too methods-heavy or the editors prefer a more explicitly applied QoL presentation.

Official source:
- https://link.springer.com/journal/11482/aims-and-scope
- https://link.springer.com/journal/11482/submission-guidelines

## 3. Backup · Journal of Happiness Studies

JHS is highly topical because it explicitly covers life satisfaction, affect and well-being in work and other life domains.

Current caveat: the journal announced that it becomes fully open access on 2027-01-01, and submissions received from **2026-06-16 onward** are subject to an APC if accepted/published unless a waiver applies.

It also currently requires:

- double-anonymous review;
- 5,000–10,000 words;
- abstract 150–250 words;
- 4–6 keywords;
- Data Availability Statement.

The combination of APC transition and the manuscript's methodological/legal-event emphasis makes it the third target rather than the first.

Official source:
- https://link.springer.com/journal/10902/aims-and-scope
- https://link.springer.com/journal/10902/submission-guidelines

## 4. Required changes from current working paper

Current English working paper before adaptation:

- ~2,200 words;
- ~324-word abstract;
- 9 keywords.

Therefore it is **not submission-ready** for SIR.

Required adaptation:

1. create a separate anonymized SIR submission draft rather than overwriting the scientific working paper;
2. compress abstract to <=250 words;
3. reduce keywords to 4–6;
4. expand manuscript to >=5,000 words using already-frozen methods, legal audits, robustness logic and literature—not new outcome fishing;
5. add Data Availability / Code Availability language that respects third-party data licences;
6. add an AI-use disclosure consistent with Springer Nature policy because AI assistance in this project has gone beyond copy editing;
7. keep author identity, affiliation, email, acknowledgements and funding metadata out of the blinded manuscript;
8. create a separate submission metadata/title-page template with unresolved author-only fields left explicitly blank rather than invented;
9. convert to DOCX only after the Markdown submission draft passes word-count, number-lock and claim QA;
10. retain SVG as canonical figure masters; convert to production format only when the submission package is otherwise frozen.

## 5. Submission claim strategy

Lead with:

> exact legal-event reconstruction and falsification-first evaluation materially change the apparent association between statutory annual-leave reforms and national Life Ladder.

Do not lead with:

- a positive pooled coefficient;
- a “null effect of vacation” statement;
- significance testing;
- a policy recommendation.

The results section should make the evidence hierarchy explicit:

1. frozen eight-event stress-test panel;
2. WHR2024 source refresh;
3. bounded legal-isolation failure of legacy candidates;
4. independently frozen Israel leave-specific holdout;
5. post-outcome reference sensitivity clearly labeled diagnostic.

## 6. Gate to DOCX/PDF

Do **not** build the journal DOCX/PDF until all of these pass:

- 5,000–10,000 words;
- abstract 150–250;
- 4–6 keywords;
- all manuscript numbers match `data/manuscript_number_lock.json`;
- all figures/tables are cited in numerical order;
- blinded manuscript contains no identifying repository links or author information;
- data/code availability language is licence-safe;
- AI-use disclosure draft is present;
- no causal claim exceeds `process/PILOT0_INTERPRETATION_LOCK.md`.
