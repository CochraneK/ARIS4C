# Preliminary Descriptive Results · 2026-09-24

These results are frozen from the official Retraction Watch bulk snapshot generated 2026-09-23. They are **descriptive counts among RWDB records**, not comparative retraction-risk estimates.

## Population

- all RWDB rows: **72,606**
- primary `Retraction` rows: **67,197** (92.55%)
- usable original-paper DOI rows: **61,316**
- unique usable original-paper DOI: **61,155**
- unique controlled Reason labels observed: **110**

## Publication → retraction lag

All 67,197 primary Retraction rows have parseable publication and retraction dates in this snapshot.

- P10: 38 days
- P25: 153 days
- median: **490 days (1.34 years)**
- P75: 1,061 days
- P90: 2,194 days
- negative lags: **0**

This is a distribution **conditional on eventual recorded retraction**. It is not a population survival curve; non-retracted works are needed for that.

## Calendar-year signal

Recent recorded Retraction counts:

| Year | Retractions |
|---|---:|
| 2018 | 2,534 |
| 2019 | 2,907 |
| 2020 | 3,080 |
| 2021 | 3,908 |
| 2022 | 5,591 |
| 2023 | **13,227** |
| 2024 | 6,383 |
| 2025 | 5,945 |
| 2026* | 1,757 |

The 2023 count is **2.37×** 2022 and **2.07×** 2024. This is a database/event signal, not evidence that underlying scientific misconduct suddenly doubled. Mass-retraction and paper-mill episodes, publisher cleanup policy, publication volume, detection, and cohort opportunity must be decomposed first.

* 2026 is incomplete in the 2026-09-23 dataset snapshot.

## Reason labels are not mutually exclusive

Mean Reason labels per Retraction record: **3.96**.

Selected high-frequency labels:

| Reason label | n | Share of Retraction rows |
|---|---:|---:|
| Investigation by Journal/Publisher | 30,278 | 45.06% |
| Unreliable Results and/or Conclusions | 21,970 | 32.69% |
| Investigation by Third Party | 17,554 | 26.12% |
| Concerns/Issues about Referencing/Attributions | 15,049 | 22.40% |
| Concerns/Issues about Data | 14,343 | 21.34% |
| Notice - Limited or No Information | 11,985 | 17.84% |
| Paper Mill | 11,712 | 17.43% |
| Concerns/Issues about Peer Review | 11,437 | 17.02% |
| Compromised Peer Review | 11,195 | 16.66% |
| Computer-Aided Content or Computer-Generated Content | 9,317 | 13.87% |

Percentages intentionally do not sum to 100%. The official RWDB guide states that most entries have multiple reasons and that some “Reasons” describe the notice/process rather than an underlying substantive problem.

## Interpretation gate

Do **not** yet interpret:
- country raw counts as country risk;
- publisher raw counts as publisher risk;
- 2023 spike as incidence of misconduct;
- Reason labels as mutually exclusive causes;
- affiliation as responsibility;
- citation as endorsement.

Comparative claims remain locked until denominator, identity, mass-event and censoring gates pass.
