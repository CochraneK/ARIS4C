# ARIS4C019 · Israel Leave-Specific Holdout Results v0.1

**Outcome opened:** 2026-09-21, only after `ISRAEL_HOLDOUT_FREEZE.md` and the strict donor list were committed.

## Headline holdout result

Under the frozen **115-country strict donor pool**:

- full-post mean donor-adjusted Life Ladder gap: **0.002**
- full-post median event-time gap: **0.048**
- Israel's mean raw change from 2015 across 2017–2020: **0.117**
- donors' mean change over the same event times: **0.115**
- pre-period mean absolute gap: **0.221**
- pre-period maximum absolute gap: **0.342**
- frozen pretrend flags: **PASS / PASS**
- minimum donor count at any event time: **90**

The holdout estimate is therefore **approximately zero**, not a stable positive or negative population Life Ladder response.

## Event time

| k | Year | Israel | Israel Δ from 2015 | Donor Δ | Adjusted gap | n donors |
|---:|---:|---:|---:|---:|---:|---:|
| -4 | 2012 | 7.111 | +0.032 | +0.005 | +0.027 | 108 |
| -3 | 2013 | 7.321 | +0.242 | -0.052 | +0.294 | 108 |
| -2 | 2014 | 7.401 | +0.322 | -0.020 | +0.342 | 108 |
| -1 | 2015 | 7.079 | +0.000 | +0.000 | +0.000 | 112 |
| 1 | 2017 | 7.331 | +0.252 | +0.075 | +0.177 | 111 |
| 2 | 2018 | 6.927 | -0.152 | +0.113 | -0.265 | 110 |
| 3 | 2019 | 7.332 | +0.253 | +0.139 | +0.114 | 110 |
| 4 | 2020 | 7.195 | +0.116 | +0.134 | -0.018 | 90 |

## Frozen robustness specifications

| Specification | Post mean | Post median | Pre mean |pre gap| | Pre max |gap| |
|---|---:|---:|---:|---:|
| strict115_mean | 0.002 | 0.048 | 0.221 | 0.342 |
| strict115_median | 0.008 | 0.036 | 0.220 | 0.327 |
| original120_mean | 0.010 | 0.064 | 0.214 | 0.331 |

The 120-donor original-rule and donor-median counterfactual specifications remain near zero.

## Leave-one-region-out

| Donor region omitted | Donors omitted | Remaining | Post mean gap | Pre mean |gap| |
|---|---:|---:|---:|---:|
| East Asia & Pacific | 15 | 100 | -0.006 | 0.222 |
| Europe & Central Asia | 40 | 75 | +0.072 | 0.211 |
| Latin America & Caribbean | 18 | 97 | -0.032 | 0.254 |
| Middle East & North Africa | 11 | 104 | -0.034 | 0.230 |
| North America | 1 | 114 | +0.002 | 0.224 |
| South Asia | 4 | 111 | -0.007 | 0.213 |
| Sub-Saharan Africa | 26 | 89 | +0.046 | 0.189 |

Across these diagnostics the post mean remains close to zero; no single broad donor region creates the headline null.

## Interpretation boundary

This is a cleaner legal holdout than the original eight-event labour/time-off package panel, but it is still a country-level, population-outcome design with substantial treatment dilution:

- the statutory increase applies to workers in the relevant tenure group, not the entire population;
- legal entitlement is not the same as leave actually taken;
- four post years cannot establish a long-run effect;
- annual national Life Ladder is a coarse outcome for a modest leave-entitlement change.

The result is therefore best described as:

> **No detectable aggregate Life Ladder shift in this transparent donor-adjusted holdout.**

It must not be translated into “annual leave has no well-being benefit.” Individual-worker effects, affective outcomes, leave use, job satisfaction and subgroup responses are different estimands.

Positive/negative affect remain locked.
