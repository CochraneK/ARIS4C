# ARIS4C019 · WHR2024-Refresh Robustness Diagnostics

> Same frozen 8-event donor-adjusted design, using the validated WHR2024 annual mirror through 2023. This is a post-unlock source-refresh robustness layer, not a new causal specification.

- Full C-panel mean post gap: **0.088**.
- Full C-panel median post gap: **-0.099**.
- Positive / negative event means: **2 / 6**.
- Most influential event remains **Bahrain**.
- Leaving Bahrain out gives mean **-0.117** and median **-0.147**.
- The covariate-complete subset remains **6/8 events**, as frozen before the first outcome look.
- Excluding Bahrain plus all GFC/COVID-overlap events leaves **3** events with mean **-0.263**.

## Prespecified / diagnostic subsets

| Subset | n | Mean | Median | Positive | Negative |
|---|---:|---:|---:|---:|---:|
| full_primary_8 | 8 | 0.088 | -0.099 | 2 | 6 |
| exclude_gfc_overlap | 6 | 0.081 | -0.180 | 1 | 5 |
| exclude_covid_overlap | 6 | 0.158 | -0.099 | 2 | 4 |
| exclude_jurisdiction_limited | 7 | 0.133 | -0.051 | 2 | 5 |
| exclude_gfc_and_covid | 4 | 0.183 | -0.180 | 1 | 3 |
| covariate_complete_only | 6 | 0.213 | -0.035 | 2 | 4 |
| exclude_bahrain | 7 | -0.117 | -0.147 | 1 | 6 |
| exclude_bahrain_gfc_covid | 3 | -0.263 | -0.214 | 0 | 3 |

## Leave-one-event-out

| Left out | Remaining n | Remaining mean | Remaining median |
|---|---:|---:|---:|
| Bahrain | 7 | -0.117 | -0.147 |
| Croatia | 7 | 0.062 | -0.147 |
| Luxembourg | 7 | 0.103 | -0.147 |
| China | 7 | 0.108 | -0.147 |
| Taiwan, China | 7 | 0.121 | -0.051 |
| Kuwait | 7 | 0.131 | -0.051 |
| Canada | 7 | 0.133 | -0.051 |
| Kosovo | 7 | 0.162 | -0.051 |

## Interpretation

- The extra 2023 follow-up does not stabilize a positive pooled result. It reduces the full mean and changes Luxembourg from positive to negative.
- Bahrain remains sufficiently influential that omitting it reverses the pooled mean.
- The subset excluding Bahrain and crisis-overlap events is entirely negative in the surviving events; because this subset is post-unlock and very small, it is a fragility diagnostic, **not** a preferred causal estimate.
- The 6-event covariate-complete sensitivity remains positive in its mean but is still Bahrain-sensitive; covariate completeness therefore does not resolve treatment isolation or pretrend failures.
- These diagnostics reinforce the treatment-isolation audit: the current eight events do not support a robust annual-leave-specific causal claim.
- Positive and negative affect remain locked.
