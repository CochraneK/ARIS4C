# ARIS4C019 · Pilot-0 Robustness Diagnostics

> Prespecified post-unlock robustness checks on the first equal-weight donor-adjusted Life Ladder diagnostic. These are still not the final causal estimator.

- Full 8-event mean full-post gap: **0.110**.
- Full 8-event median full-post gap: **-0.099**.
- Most influential leave-one-out case: **Bahrain**; remaining-event mean = **-0.091**.
- Bahrain pre-placebo RMS gap: **1.023**; Bahrain full-post mean gap: **1.521**.

## Prespecified sensitivity subsets

| Subset | n | Mean post gap | Median post gap | Positive | Negative |
|---|---:|---:|---:|---:|---:|
| full_primary_8 | 8 | 0.110 | -0.099 | 3 | 5 |
| exclude_gfc_overlap | 6 | 0.111 | -0.160 | 2 | 4 |
| exclude_covid_overlap | 6 | 0.158 | -0.099 | 2 | 4 |
| exclude_jurisdiction_limited | 7 | 0.151 | -0.051 | 3 | 4 |
| exclude_gfc_and_covid | 4 | 0.183 | -0.181 | 1 | 3 |
| covariate_complete_only | 6 | 0.243 | 0.029 | 3 | 3 |

## Leave-one-event-out

| Left out | Remaining n | Remaining mean | Remaining median |
|---|---:|---:|---:|
| Bahrain | 7 | -0.091 | -0.146 |
| Croatia | 7 | 0.088 | -0.146 |
| Luxembourg | 7 | 0.110 | -0.146 |
| China | 7 | 0.133 | -0.146 |
| Taiwan, China | 7 | 0.147 | -0.051 |
| Canada | 7 | 0.151 | -0.051 |
| Kuwait | 7 | 0.157 | -0.051 |
| Kosovo | 7 | 0.187 | -0.051 |

## Interpretation boundary

- A sign change under leave-one-event-out is evidence of event-level fragility, not evidence that the omitted event should be deleted.
- Large pre-placebo gaps weaken a causal interpretation of that event-specific post gap.
- Crisis/scope/covariate subsets were defined before these robustness summaries; they are not selected for significance.
- Positive/negative affect remain locked.
