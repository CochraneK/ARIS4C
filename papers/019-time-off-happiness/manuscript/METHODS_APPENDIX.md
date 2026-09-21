# ARIS4C019 · Methods and Reproducibility Appendix v0.1

## A1. Study principle

The project uses a falsification-first workflow. Legal event definition, event timing, donor eligibility, outcome hierarchy and core covariate rules are frozen before the corresponding primary outcome is inspected.

The design intentionally separates:

- candidate discovery;
- legal treatment admission;
- outcome availability;
- donor/support checks;
- effect estimation;
- post-outcome fragility diagnostics.

A favorable effect estimate can never promote an event into the treatment set.

## A2. Outcome

Primary outcome: annual Gallup / World Happiness Report **Life Ladder** country mean.

The study does not use the World Happiness ranking itself and does not use rolling multi-year ranking averages as annual event-study outcomes.

Outcome releases:

1. WHR2023 annual historical workbook through 2022 for the first outcome look;
2. validated WHR2024 annual source through 2023 for post-unlock source-refresh robustness.

The WHR2023 and WHR2024 releases share 2,199 published country-year Life Ladder values that agree at three-decimal precision.

No missing Life Ladder value is interpolated.

## A3. Secondary outcome firewall

Positive and negative affect were specified as secondary outcomes but remain unopened for the current Pilot-0 manuscript.

They require a separate unlock decision because:

- they answer a different psychological outcome question;
- their annual coverage differs;
- opening them after a fragile primary result could create outcome-selection degrees of freedom.

## A4. Legal-source hierarchy

Preferred event evidence, in order:

1. enacted statute / official legal repository;
2. official government or parliamentary implementation notice;
3. ILO NATLEX / NORMLEX or equivalent authoritative legal repository;
4. World Bank legal-regulation panel as corroboration;
5. secondary summaries only for discovery, never final timing.

The World Bank Employing Workers panel is not allowed to veto a legally verified reform and is not allowed to create a treatment without legal verification.

## A5. Exposure construct

Focal treatment: change in **statutory paid annual-leave entitlement**.

Kept separate:

- public holidays;
- standard weekly hours;
- actual annual hours;
- actual leave taken / utilization;
- sick leave, parental leave or other leave types.

## A6. Event clock

Event time is anchored to the verified legal effective year.

- pre window: T−4…T−1;
- reference: T−1, last full untreated year;
- January 1 reform: T can enter post at k=0;
- after-January-1 reform: T is excluded as partial-exposure transition year and full post begins T+1;
- post window ends at T+4;
- missing annual outcomes remain missing.

## A7. Original eight-event donor rule

A donor must:

1. not be the focal treated country;
2. have >=2 observed pre and >=2 observed post Life Ladder years;
3. have no World Bank annual-leave jump in an expanded nearby window;
4. have no verified leave treatment in the focal event window;
5. require no interpolated outcome.

Not-yet-treated countries can serve as donors outside their treatment window.

## A8. Original event-specific estimator

For event i and event time k:

`gap_ik = (Y_i,t − Y_i,ref) − mean_d(Y_d,t − Y_d,ref)`.

Event full-post summary is the equal-weight mean of available post-event gaps.

The pooled eight-event mean is descriptive/diagnostic because treatment isolation is poor and event heterogeneity is substantial.

## A9. Modern staggered-adoption diagnostics

Callaway–Sant'Anna-style group-time ATT and Sun–Abraham-style heterogeneous event-study logic are used to test whether the apparent pooled signal survives modern staggered-treatment diagnostics.

Conventional TWFE event-study estimates are not permitted as the headline causal result.

Pretrend failures or contaminated leads weaken the strong interpretation rather than being optimized away.

## A10. WHR2024 source-refresh freeze

Before rerunning effects on WHR2024 annual data, the project froze an A/B/C decomposition:

- A-proxy: newer release restricted to original WHR2023 country-year keys;
- B: newer release through 2022, adding newly available 2022 observations;
- C: newer release through 2023.

This separates precision/source changes, backfilled coverage and genuinely later follow-up.

## A11. Bounded legal-event expansion

The 11 unregistered World Bank leave discontinuities with usable WHR coverage were reviewed under a bounded search rule.

Result: 0 new clean leave-specific holdouts.

The search stopped rather than lowering legal-isolation criteria.

## A12. Modern snapshot discovery

WORLD's 2015/16 annual-leave snapshot and Equal Futures' January-2026 annual-leave dataset use a closely aligned minimum-entitlement construct.

Snapshot category differences are only candidate generators. A candidate must still pass:

- exact legal verification;
- national/scope review;
- reform-bundle review;
- sufficient pre/post annual outcome coverage;
- donor-support review.

Equal Futures raw public-use data are not redistributed in this repository. The repository stores only derived audit results, provenance and non-restricted summaries.

## A13. Israel holdout

Israel Annual Leave Law Amendment No.15 was identified after the original analysis and admitted before its candidate-specific outcome was inspected.

Frozen design:

- T = 2016;
- reference = 2015;
- 2016 excluded as staged partial exposure;
- post = 2017–2020;
- strict donor pool = 115 countries.

The strict pool additionally excludes every country whose annual-leave category changes between the legacy WORLD and 2026 Equal Futures snapshots, making the donor contamination screen more conservative.

## A14. Israel prespecified diagnostics

Before outcome opening:

- mean-donor counterfactual;
- original-rule donor pool sensitivity;
- donor-median counterfactual;
- leave-one-region-out diagnostic;
- pretrend warning thresholds:
  - mean absolute pre gap >0.30;
  - any absolute pre gap >0.50.

No p-value is used as the headline criterion.

## A15. Post-outcome reference sensitivity

Alternative Israel baselines were inspected only after the pre-frozen 2015-reference result was opened.

They are labeled fragility diagnostics and can never become the preferred specification.

This distinction is essential because selecting a different pre year after observing the result would introduce researcher degrees of freedom.

## A16. Macro and concurrent shocks

Pre-treatment macro variables were frozen before first outcome inspection:

- log GDP per capita;
- unemployment;
- CPI inflation.

Contemporaneous post-treatment macro controls are not inserted into the headline regression because they can be mediators.

Country-specific security/macro events are documented as interpretation risks rather than used for post-hoc event exclusion unless the sensitivity was prespecified.

## A17. Reproducibility hierarchy

Canonical numerical files include:

- `data/whr2024_refresh_event_summary.csv`
- `data/whr2024_refresh_pooled.csv`
- `data/whr2024_refresh_sensitivities.csv`
- `data/israel_holdout_event_time.csv`
- `data/israel_holdout_summary.csv`
- `data/israel_holdout_region_loo.csv`
- `data/israel_reference_sensitivity.csv`
- `data/manuscript_number_lock.json`

Canonical interpretation files include:

- `process/PILOT0_INTERPRETATION_LOCK.md`
- `process/ISRAEL_HOLDOUT_FREEZE.md`
- `process/ISRAEL_HOLDOUT_RESULTS.md`
- `process/ISRAEL_REFERENCE_SHOCK_AUDIT.md`
- `process/MANUSCRIPT_QA.md`

## A18. Claim rule

The present evidence supports neither:

- a robust positive population effect of statutory annual leave, nor
- a precise causal zero.

The defensible conclusion is directional instability and limited aggregate identifiability under the available legal events and annual national Life Ladder data.
