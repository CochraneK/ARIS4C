# ARIS4C019 · Pilot-0 Estimator Freeze v0.1

**Frozen:** 2026-09-21  
**Stage:** pre-outcome / no-effect-look

> This file fixes the first executable Life Ladder estimator before outcome inspection. It is a transparent Pilot-0 screening estimator, not the final causal specification. The previously frozen Callaway–Sant'Anna / Sun–Abraham robustness stage remains required before strong causal claims.

## 1. Event clock and reference

For each frozen event with verified legal effective year `T`:

- event time is `k = year - T`;
- reference year is always `T-1` (`k=-1`);
- January-1 reforms may use `k=0` as a full post year;
- reforms effective after January 1 exclude `k=0` as a partial-exposure transition year;
- missing Life Ladder years remain missing and are never interpolated.

## 2. Event-specific contrast

For event `e` and event time `k`:

1. treated change:
   `ΔY_e,k = Y_treated,T+k - Y_treated,T-1`;
2. for every frozen clean donor with both calendar years observed:
   `ΔY_d,k = Y_d,T+k - Y_d,T-1`;
3. equal-weight donor counterfactual change:
   `mean_d(ΔY_d,k)`;
4. Pilot-0 event-time contrast:
   `ATT_e,k = ΔY_e,k - mean_d(ΔY_d,k)`.

No donor is added or removed based on Life Ladder values.

## 3. Event-level post summary

For each event, the post summary is the equal-weight mean of its available full-exposure event-time contrasts:

- January-1 reform: available `k = 0...+4`;
- mid-year / unknown-day reform: available `k = +1...+4`.

At least two full-post contrasts are required for an event-level post summary.

## 4. Pooled summary

- headline pool = the 8 frozen Tier-A primary events;
- pooled event-time estimate = equal-weight mean of `ATT_e,k` across eligible headline events at that `k`;
- pooled post estimate = equal-weight mean of event-level post summaries, so countries/events receive equal weight regardless of survey density;
- report the number of contributing events at every event time.

The pooled result is a compact summary, not a substitute for event-specific inspection.

## 5. Uncertainty

Pilot-0 reports:

- across-event standard deviation;
- descriptive 95% interval `mean ± 1.96 × SD/sqrt(n_events)` when at least 2 events contribute;
- no headline p-value.

With only eight primary events, uncertainty is necessarily coarse. Later inference must use the prespecified modern staggered-adoption specifications and small-cluster-aware interpretation.

## 6. Pretrend / falsification screen

Before interpreting post estimates, report `k=-4,-3,-2` contrasts relative to `k=-1`.

Flag an event for pretrend review when either:

- the mean absolute available pre-period contrast exceeds **0.30 Life Ladder points**, or
- any available pre-period contrast exceeds **0.50 points** in absolute value.

These thresholds are diagnostic, not exclusion rules. Events are not deleted based on this screen.

## 7. Prespecified sensitivity summaries

Produce pooled post summaries for:

- full Tier-A primary pool;
- excluding global-financial-crisis-window events;
- excluding COVID-overlap events;
- excluding jurisdiction-limited events;
- excluding all currently flagged crisis/scope events;
- Tier-A + Tier-B as a separate sensitivity, never merged into the headline silently.

Taiwan and Kosovo remain in the headline unadjusted analysis despite incomplete frozen WDI covariates. They enter a prespecified **covariate-complete sensitivity subset** only when all three macro baselines are available.

## 8. Leave-one-event-out

Recompute the pooled post summary eight times, each time omitting one headline event. Report the range and every omitted-event estimate.

## 9. Interpretation boundary

This first estimator is designed to reveal:

- direction and rough magnitude;
- event heterogeneity;
- pretrend problems;
- dependence on a single event;
- crisis/scope sensitivity.

It does **not** by itself establish causality. Strong causal wording remains locked until the Callaway–Sant'Anna / Sun–Abraham stage, legal-scope review, and robustness checks are complete.
