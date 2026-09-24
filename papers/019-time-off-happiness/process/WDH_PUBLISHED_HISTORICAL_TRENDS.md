# ARIS4C019 · Published WDH historical trend layer (1940s–1980s)

**Materialized:** 2026-09-24  
**Source:** Veenhoven & Kegel, *Did Average Happiness in Nations Change over the Years?*, Table 2.  
**Unit:** OLS slope in points on the transformed 0–10 happiness scale per calendar year.  
**Raw-data status:** published trend coefficients materialized; the downloadable `TrendsInNations-2023e.xlsx` raw yearly workbook remains transport-blocked in the current runtime.

## Coverage

- published trend rows materialized: **95**
- distinct countries/labels: **28**
- cohorts: 1940s, 1950s, 1960s, 1970s, 1980s
- earliest start: **1946**
- prewar-hours 14-country bridge represented here: **12/14**

Missing from this particular pre-1990 published-trend subset:
- Australia
- Germany

## Cohort summaries

| cohort | trend rows | countries | mean slope | median | positive | negative | zero |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1940s | 3 | 2 | 0.0163 | 0.0020 | 3 | 0 | 0 |
| 1950s | 6 | 3 | 0.0033 | 0.0025 | 4 | 2 | 0 |
| 1960s | 12 | 10 | 0.0077 | 0.0095 | 10 | 2 | 0 |
| 1970s | 35 | 16 | 0.0050 | 0.0070 | 25 | 9 | 1 |
| 1980s | 39 | 18 | 0.0050 | 0.0030 | 25 | 13 | 1 |

These cohort summaries are descriptive only. Rows are not independent: a nation can appear with multiple happiness measures and in nested start-period windows. They must not be treated as 1:1 country observations or pooled as if independent.

## Measurement guardrail

Measure codes retain concept/instrument identity:
- `hl3/hl4/hl5`: happiness questions;
- `ls4/ls5/ls10/ls11/ls10+11`: life-satisfaction questions;
- `bw11`: best-worst possible life / ladder-type evaluation.

The WDH source transforms scores to a comparable 0–10 range, but that does not make the instruments identical. Any 019 historical synthesis must model or stratify by measure family before pooling.

## Use in 019

This layer is suitable for:
1. documenting long-run well-being direction by country/instrument;
2. linking historical work-time trajectories to later well-being trend histories;
3. screening eras/countries for deeper legal-history work.

It is **not** a substitute for the unavailable yearly WDH observations and cannot identify the effect of a particular annual-leave reform on its own.
