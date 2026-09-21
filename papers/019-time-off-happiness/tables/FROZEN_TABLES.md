# ARIS4C019 · Frozen Manuscript Tables v0.1

**Frozen:** 2026-09-21  
**Rule:** manuscript tables are rendered from committed machine-readable CSVs. Rounded display values below are not a second source of truth.

## Table 1. Evidence architecture

| Layer | Candidate/event count | Role | Outcome status | Interpretation |
|---|---:|---|---|---|
| Frozen original panel | 8 | broader labour/time-off reform stress test | opened after pre-outcome freeze | not a clean annual-leave-specific causal panel |
| Unregistered World Bank jump queue | 11 | bounded legal verification | candidate outcomes not used for admission | 0 new clean leave-specific holdouts |
| WORLD 2015/16 → Equal Futures 2026 cross-category screen | 13 | modern candidate discovery | outcome-blind during legal triage | Israel admitted; Mexico future holdout |
| Israel 2016 holdout | 1 | independent leave-specific test | opened only after donor/timing freeze | no directionally stable aggregate shift |

## Table 2. WHR2024-refreshed eight-event donor-adjusted results

Source: `data/whr2024_refresh_event_summary.csv`  
Blob SHA: `c7e3b9155696a6b6c757d379d27383dff3c14fd9`

| Event | Full-post mean gap | Pre RMS gap | Post points | Sign |
|---|---:|---:|---:|---|
| Bahrain | +1.521 | 1.023 | 4 | positive |
| Canada | -0.225 | 0.300 | 4 | negative |
| China | -0.051 | 0.149 | 5 | negative |
| Croatia | +0.266 | 0.432 | 5 | positive |
| Kosovo | -0.429 | 0.565 | 4 | negative |
| Kuwait | -0.214 | 0.292 | 4 | negative |
| Luxembourg | -0.019 | 0.253 | 3 | negative |
| Taiwan, China | -0.147 | 0.125 | 5 | negative |

Pooled refreshed mean = **+0.088**; median = **−0.099**; 2 positive / 6 negative. Bahrain is the dominant positive event.

## Table 3. Israel strict-115 frozen event time

Source: `data/israel_holdout_event_time.csv`  
Blob SHA: `7104de3e93c06bd39614bc722667e9ca14aabf26`

| k | Year | Israel Life Ladder | Israel Δ from 2015 | Donor Δ | Adjusted gap | Donor n |
|---:|---:|---:|---:|---:|---:|---:|
| -4 | 2012 | 7.111 | +0.032 | +0.005 | +0.027 | 108 |
| -3 | 2013 | 7.321 | +0.242 | -0.052 | +0.294 | 108 |
| -2 | 2014 | 7.401 | +0.322 | -0.020 | +0.342 | 108 |
| -1 | 2015 | 7.079 | +0.000 | +0.000 | +0.000 | 112 |
| 1 | 2017 | 7.331 | +0.252 | +0.075 | +0.177 | 111 |
| 2 | 2018 | 6.927 | -0.152 | +0.113 | -0.265 | 110 |
| 3 | 2019 | 7.332 | +0.253 | +0.139 | +0.114 | 110 |
| 4 | 2020 | 7.195 | +0.116 | +0.134 | -0.018 | 90 |

Primary full-post mean = **+0.002**.

## Table 4. Israel reference sensitivity

Source: `data/israel_reference_sensitivity.csv`  
Blob SHA: `f2398550d7a90e9a209153d7cd6f2baa325c7cd2`

| Baseline | Type | Post mean gap | Post median gap | Min donor n |
|---|---|---:|---:|---:|
| 2012 | single_year | -0.027 | +0.013 | 91 |
| 2013 | single_year | -0.306 | -0.271 | 89 |
| 2014 | single_year | -0.337 | -0.302 | 90 |
| 2015 | single_year | +0.002 | +0.048 | 90 |
| mean_2013_2015 | multi_year_mean | -0.219 | -0.185 | 85 |
| mean_2012_2015 | multi_year_mean | -0.175 | -0.141 | 84 |

Only the 2015 baseline is pre-frozen. All other rows are post-outcome fragility diagnostics.

## Table-use rule

If a manuscript number conflicts with a table above, resolve against the source CSV and `data/manuscript_number_lock.json`, then rerun `process/MANUSCRIPT_QA.md` checks.
