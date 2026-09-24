# The Global Ecology of Scientific Retractions
## A Full-Database, Field-Normalized Study of Retraction Dynamics, Causes, and Citation Afterlife

**ARIS4C-020 · Working paper · pre-confirmatory draft · 2026-09-24**

### Abstract

Retraction databases are often summarized through raw counts of countries, journals, publishers, or stated reasons. Those counts conflate publication volume, disciplinary composition, detection practices, publisher policy, mass-retraction episodes, and the time available for a publication to be retracted. We develop a reproducible all-discipline framework using the complete Retraction Watch bulk dataset as an event spine and Crossref/OpenAlex as metadata, denominator, and citation layers. In the 2026-09-23 Retraction Watch snapshot, 72,606 records include 67,197 Retractions. The primary Retraction population contains 61,155 unique usable original-paper DOIs. Publication-to-retraction lag has a median of 490 days (1.34 years; P25 153, P75 1,061), and Reason is strongly multi-label, with a mean of 3.96 labels per Retraction. A deterministic OpenAlex matching pilot linked 996/1,000 unique original-paper DOIs (99.6%); the first full-match shard linked 15,146/15,255 unique DOIs (99.29%) without API errors. These preliminary results establish the feasibility of a cohort-normalized, work-level analysis. Confirmatory comparisons remain locked until full DOI matching, publication denominators, right-censoring policy, reason-ontology audit, mass-event sensitivity, and work-type concordance are complete.

### 1. Introduction

Retractions are observable editorial events, not direct measurements of misconduct. A recorded retraction depends on the existence of a problematic or superseded work, detection, investigation, editorial action, notice practices, database capture, and time. Consequently, raw retraction counts cannot by themselves identify comparative research-integrity risk.

Recent large-scale work has described retractions in Web of Science and Scopus, studied paper-mill retractions, estimated denominator-aware rates for particular access models, and modeled post-retraction citation persistence in selected disciplines. ARIS4C-020 targets the intersection that remains underdeveloped: a single work-level pipeline spanning the complete current Retraction Watch Retraction population, publication denominators across the disciplinary space, time-to-retraction, the native multi-label reason structure, concentrated mass-retraction events, and citation afterlife.

### 2. Data

#### 2.1 Retraction Watch

The event spine is the Crossref-distributed Retraction Watch bulk CSV. The frozen snapshot used here was generated 2026-09-23 and retrieved 2026-09-24.

SHA-256: `da61a30cd4b01b681d1b42ad43cae7ae9eca2213a4f33ff7e762b7942c93f663`.

Primary confirmatory event population: `RetractionNature == Retraction`.

Expressions of concern, corrections, and reinstatements are retained for pathway analyses but excluded from the primary retraction-rate numerator because Retraction Watch does not claim population-complete coverage for corrections or expressions of concern.

#### 2.2 OpenAlex and Crossref

OpenAlex supplies DOI-linked work metadata, fields/topics, authorship-country metadata, sources, citation counts/graph structure, and publication-universe denominators. Crossref remains a DOI-metadata and update-relation sensitivity source.

### 3. Identity and unit of analysis

The database is event-oriented. We therefore maintain:

1. an **event table** keyed by RWDB Record ID;
2. a **work table** keyed first by normalized OriginalPaperDOI, then by PMID when DOI is absent.

Multiple Retraction records for the same original DOI collapse to one work for publication-risk numerators. Contributing Record IDs, reason labels, affiliations, subjects, and notice dates remain traceable. The frozen snapshot contains 14 repeated original DOI values among Retraction rows, with maximum multiplicity 145.

### 4. Measures and analysis

#### 4.1 Descriptive counts

Report counts by publication cohort, retraction year, RWDB subject, country, publisher, journal, article type, and Reason. Country and subject use both full and fractional counting.

#### 4.2 Publication-normalized rates

Primary estimand:

[
R_{y,f} = 10,000 \times \frac{\text{unique retracted works in publication year }y\text{ and field }f}{\text{all eligible works in publication year }y\text{ and field }f}
]

Recent publication cohorts require explicit follow-up/censoring treatment.

#### 4.3 Publication-to-retraction time

The current descriptive lag distribution is conditional on eventual retraction. Confirmatory survival/time-to-event analysis requires non-retracted denominator works and right censoring.

#### 4.4 Reason ecology

Official RWDB Reason labels remain atomic and multi-label. Higher-order analysis uses orthogonal facets: affected object, failure mechanism, ethics/compliance, process actor, notice/lifecycle state, and evidence specificity. Procedural labels are not reinterpreted as substantive causes.

#### 4.5 Concentrated episodes

Publisher-year, journal-year, and reason-year concentration screens identify mass-retraction waves. Headline models are repeated with and without high-concentration episodes.

#### 4.6 Citation afterlife

For DOI-linked works, citation trajectories are aligned on the earliest formal retraction date. Outcomes include pre/post citation rates, proportion of lifetime citations after retraction, time to first post-retraction citation, and persistence at fixed horizons. Matched non-retracted controls receive pseudo-event dates at comparable publication age.

### 5. Preliminary results

#### 5.1 Snapshot

The frozen dataset contains **72,606** rows: 67,197 Retractions, 3,719 expressions of concern, 1,530 corrections, and 160 reinstatements. Within Retractions, 61,316 rows have usable original-paper DOI values, corresponding to **61,155 unique DOI**.

#### 5.2 Retraction lag

All 67,197 Retraction rows have parseable publication and retraction dates under the current file format, with no negative lag. Median publication-to-retraction lag is **490 days (1.34 years)**; P25 is 153 days and P75 is 1,061 days.

#### 5.3 Multi-label Reason structure

The snapshot contains **110 unique Reason labels**. Retraction records contain a mean of **3.96 labels**. Only 11,564 Retractions have exactly one Reason label. This structure rules out treating a single assigned “cause” as the native unit of the database.

#### 5.4 Calendar-time concentration

Recorded Retractions increase from 5,591 in 2022 to **13,227 in 2023**, then fall to 6,383 in 2024 and 5,945 in 2025. The 2023 count is 2.37 times the 2022 count. This pattern is treated as an event/detection/publisher-policy signal until mass-event decomposition is complete.

#### 5.5 OpenAlex match feasibility

The deterministic 1,000-DOI pilot matched **996/1,000 (99.6%)**. Full-match shard 0 linked **15,146/15,255 (99.2855%)** unique DOI with no API errors, supporting full-dataset enrichment.

### 6. Discussion

The early audit already changes the appropriate research design. First, retraction counts are too structurally confounded to support league-table interpretations without denominators. Second, a typical Retraction record carries several Reason labels, many of which describe investigations or notice states rather than a single causal failure. Third, publication-to-retraction lag is long enough that naive comparisons of recent and older publication cohorts are intrinsically biased. Fourth, the 2023 volume spike is sufficiently large that mass-retraction episodes must be modeled explicitly rather than absorbed into a smooth temporal trend.

No country, institution, journal, publisher, field, or author is interpreted here as more misconduct-prone on the basis of the preliminary counts.

### 7. Next confirmatory gates

1. Complete OpenAlex DOI matching.
2. Freeze OpenAlex work-type eligibility.
3. Generate publication-year × field denominators.
4. Complete and manually audit the 110-label Reason facet map.
5. Quantify mass-event concentration.
6. Freeze mature-cohort/right-censoring policy.
7. Build matched citation controls.
8. Only then unlock comparative risk estimates and the final Results/Discussion.

### References · working set

- Koo M, Lin S-C. Retracted articles in scientific literature: A bibliometric analysis from 2003 to 2022 using the Web of Science. *Heliyon*. 2024;10:e38620. doi:10.1016/j.heliyon.2024.e38620.
- Cheng MWT, Yang X, Allen RM. Tracking the retracted paper mill articles: a bibliometric study. *Scientometrics*. 2026;131:6341–6361. doi:10.1007/s11192-026-05751-6.
- Mañana-Rodríguez J, Granadino-Goenechea B, Bautista-Puig N. An analysis of the relationship between access models and retractions with peer review issues (2014–2024). *Scientometrics*. 2026;131:4151–4173. doi:10.1007/s11192-026-05668-0.
- García-Romero A, González-Mancebo S, Espallardo-Ortega C, et al. The enduring influence of retracted research: determinants and citation patterns across three disciplines. *Scientometrics*. 2026;131:5685–5712. doi:10.1007/s11192-026-05699-7.
- Lendvai GF, Sasvári P. ‘Wasted’ research and lost citations: A scientometric assessment of retracted documents in Scopus between 2001 and 2024. *Journal of Information Science*. 2026. doi:10.1177/01655515251362383.
