# Research Plan · ARIS4C-020

## 0. Source and scope freeze

Primary population: records whose `RetractionNature` is Retraction in the complete Retraction Watch bulk dataset.

Retraction Watch explicitly describes its retraction coverage as the intended comprehensive component; expressions of concern and corrections are retained only for exploratory pathway analyses because their collection is not population-complete.

Official bulk source:
- https://gitlab.com/crossref/retraction-watch-data
- Crossref documentation: https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/

Freeze every analytical snapshot by SHA-256 and retrieval timestamp.

## 1. Data audit before results

Report:
- total records and unique Record IDs;
- RetractionNature distribution;
- duplicate original DOI / notice DOI patterns;
- DOI / PMID missingness;
- date validity and impossible negative lags;
- multi-valued field parsing;
- missingness by year / field / publisher / country;
- controlled-vocabulary reason cardinality;
- changes in reason vocabulary over time.

No substantive ranking before this audit is frozen.

## 2. Descriptive layer

Describe counts by:
- original publication year;
- retraction year;
- field / topic;
- country and collaboration type;
- journal and publisher;
- article type;
- reason;
- retraction lag.

Use both fractional and full counting for multi-country / multi-institution records.

## 3. Denominator layer

Join each retracted DOI to Crossref/OpenAlex. Build denominators from the publication universe by year × field and, where coverage allows, country × field, journal, institution and publisher.

Primary normalized quantity:
`retractions in publication cohort / eligible publications in the same cohort × 10,000`.

Do not interpret absolute counts as comparative risk.

## 4. Time-to-retraction layer

Treat original publication date as time origin and retraction date as event time.

Analyses:
- Kaplan–Meier-style descriptive survival;
- median / quantile lag by field and reason;
- accelerated-failure-time or Cox-type models only after proportionality / distributional checks;
- calendar-period sensitivity because detection practices change over time.

## 5. Reason ontology

Keep Retraction Watch reasons multi-label.

Build:
- atomic reason frequencies;
- reason co-occurrence matrix / network;
- transparent higher-order families with a frozen mapping table;
- temporal drift of reason mix;
- field / publisher / country heterogeneity.

Do not infer intentional misconduct from neutral RW labels.

## 6. Event / cluster structure

Detect concentrated episodes:
- journal-level mass retractions;
- publisher cleanup waves;
- paper-mill-linked waves;
- repeated author/institution clusters.

Run headline models with and without high-volume episodes to distinguish systemic trends from single cleanup events.

Author analyses require disambiguation confidence tiers; names alone are insufficient.

## 7. Citation afterlife

For DOI-linked records, use OpenAlex/Crossref/OpenCitations to reconstruct yearly citation trajectories.

Key quantities:
- citations before retraction;
- citations after retraction;
- time from retraction to first subsequent citation;
- fraction of citations occurring post-retraction;
- citation decay / persistence by field, reason and notice age.

A citation is exposure/attention, not evidence that the citing paper endorses the retracted claim.

## 8. Falsification and sensitivity

At minimum:
- DOI-only vs all-record analyses;
- full vs fractional country counting;
- RW subject vs OpenAlex field/topic mapping;
- excluding very recent publication cohorts with incomplete opportunity for retraction;
- excluding top mass-retraction episodes;
- alternate denominator definitions;
- pre/post Crossref-RW integration period;
- matched citation controls for retracted vs non-retracted works.

## 9. Candidate paper structure

1. Data completeness and global descriptive map.
2. Normalized field/country/publisher risk.
3. Retraction-lag dynamics.
4. Reason ecology and event clustering.
5. Citation afterlife.
6. Detection/coverage limitations and policy implications.

The project may split into multiple papers if the combined inferential package becomes too broad; the canonical dataset and ontology should remain shared.
