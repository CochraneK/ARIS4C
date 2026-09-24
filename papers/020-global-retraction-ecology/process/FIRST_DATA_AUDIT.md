# First Full-Database Audit · RWDB 2026-09-23

## Snapshot

- Official Crossref / Retraction Watch bulk CSV
- Generated: **2026-09-23**
- Retrieved/audited: **2026-09-24**
- Size: **66,881,479 bytes**
- SHA-256: `da61a30cd4b01b681d1b42ad43cae7ae9eca2213a4f33ff7e762b7942c93f663`
- Rows: **72,606**
- Unique Record IDs: **72,606**

The primary population is **67,197 Retraction records** (92.55% of all rows). Expressions of concern (3,719), corrections (1,530), and reinstatements (160) are retained outside the primary confirmatory population.

## Identifier coverage

Within Retraction records:

- original-paper DOI available: **61,316 / 67,197 = 91.25%**
- unique usable original-paper DOIs: **61,155**
- 14 DOI values occur more than once; the maximum multiplicity is 145
- notice DOI available: **62,651** rows, **57,609** unique

Repeated DOI rows are not automatically duplicates: one original work can have multiple notices/records. Deduplication must be event-aware.

## Retraction lag

All 67,197 Retraction rows have parseable publication and retraction dates under the current file format. No negative lag was found.

Publication → retraction lag:

| Quantile | Days |
|---|---:|
| P10 | 38 |
| P25 | 153 |
| Median | **490** |
| P75 | 1,061 |
| P90 | 2,194 |

Median lag is approximately **1.34 years**.

This immediately motivates cohort-aware / survival-style analysis; recent publication cohorts have much less opportunity to be retracted.

## Multi-label structure

RWDB reasons are strongly multi-label. Across Retraction records the mean is **3.96 reason labels per record**; records range from 1 to 17 reason labels. Only 11,564 / 67,197 records have exactly one reason.

Country and Subject are also multi-valued:
- 56,705 records contain one country label; the rest can contain multiple countries.
- only 9,015 records contain one subject label; most records have 2–4 subject labels.

Therefore no headline country/field analysis may silently use naive duplicated full counting. Full and fractional counting must be shown side-by-side.

## High-frequency reason labels

The most frequent labels include:

1. Investigation by Journal/Publisher — 30,278
2. Unreliable Results and/or Conclusions — 21,970
3. Investigation by Third Party — 17,554
4. Concerns/Issues about Referencing/Attributions — 15,049
5. Concerns/Issues about Data — 14,343
6. Notice - Limited or No Information — 11,985
7. **Paper Mill — 11,712**
8. Concerns/Issues about Peer Review — 11,437
9. Compromised Peer Review — 11,195
10. **Computer-Aided Content or Computer-Generated Content — 9,317**

These are labels, not mutually exclusive cases.

## Time signal

Recorded Retraction counts by notice year rose sharply in 2023 (13,227), versus 5,591 in 2022 and 6,383 in 2024. This is not interpretable as a change in underlying misconduct incidence without decomposing mass-retraction events, publication denominators, detection effort, publisher policy, and cohort exposure time.

## Immediate methodological consequences

1. Freeze **Retraction-only** as the confirmatory event population.
2. Use Crossref/OpenAlex publication cohorts as denominators before country/field/publisher risk claims.
3. Preserve the original 110-label reason vocabulary, then create a versioned higher-order ontology.
4. Model time-to-retraction rather than comparing raw contemporary cohorts.
5. Detect and isolate mass-retraction/paper-mill waves.
6. Treat author/institution analysis as entity-resolution work, not string counting.
7. Run post-retraction citation analysis only on DOI-matched works, with matched non-retracted controls.

Machine-readable counterpart: `data/derived/rwdb_audit_2026-09-23.json`.
