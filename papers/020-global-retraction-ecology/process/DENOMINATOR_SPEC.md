# Denominator Specification · v1

## Core estimand

Raw RWDB counts measure recorded retractions, not retraction probability.

Primary cohort rate:

`unique retracted works / all eligible works in the same publication cohort × 10,000`

## Time axis
Use original publication year for denominators. Recent cohorts are right-censored because they have had less time to be retracted.

- descriptive rates show follow-up age;
- confirmatory cross-cohort comparisons use mature cohorts and/or time-to-event models;
- 2026 is incomplete in the 2026-09-23 snapshot.

## Field denominator
Primary field mapping: OpenAlex `primary_topic.field.id`.

For year × field:
- numerator = DOI-linked unique RWDB Retraction works matched to that field;
- denominator = all eligible OpenAlex works in the same year × field.

RWDB Subject remains a separate descriptive taxonomy and sensitivity mapping.

## Country denominator
Country is an affiliation attribute, not responsibility.

Report:
1. **Full counting** — a multinational work contributes one work to each represented country.
2. **Fractional counting** — k unique represented countries each receive 1/k.

OpenAlex `group_by=authorships.countries` is suitable for fast full-count denominators. Fractional denominators require work-level authorship-country data.

## Journal/source denominator
Estimate source-level rates only after stable source identity and year-specific publication denominators are available. Suppress or shrink unstable small-source league tables.

## Publisher denominator
Publisher comparisons are secondary because acquisitions and publisher hierarchies change. Use versioned source/publisher identifier mappings and run sensitivity at immediate and top-level parent publisher.

## Work-type eligibility
RWDB ArticleType and OpenAlex work type are different systems. Freeze an eligible OpenAlex work-type set before rate estimation; non-scholarly metadata objects are excluded.

## OpenAlex implementation
OpenAlex currently supports:
- filters including `publication_year`;
- up to 100 OR DOI values in one filter;
- `group_by` aggregations;
- cursor paging for grouped results beyond 200 buckets.

Raw enrichment lives in gitignored `data/interim/`; Git stores compact manifests, coverage reports, and denominator tables.

## Headline gate
No comparative risk claim until:
- full DOI match coverage;
- frozen eligible-work-type set;
- year × field denominators;
- right-censoring policy;
- mass-retraction-event sensitivity;
- full vs fractional country comparison.
