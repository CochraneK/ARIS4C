# ARIS4C019 · Israel Leave-Specific Holdout Freeze v0.1

**Frozen:** 2026-09-21  
**Outcome status at freeze:** Israel holdout effect not inspected

## Question

Did the leave-specific 2016 Israeli Annual Leave Law amendment coincide with a change in annual population Life Ladder relative to a pre-frozen, contamination-screened donor pool?

## Treatment

Annual Leave Law (Amendment No.15 and Temporary Provision), 2016.

- first extra leave day: 2016-07-01;
- second extra leave day: 2017-01-01;
- affected group: workers in their first four years with the employer/workplace;
- legal vehicle: leave-specific amendment, not a broad labour code.

## Event time

- legal event clock T = 2016;
- T−1 = 2015 reference;
- T=2016 excluded as partial/staged transition exposure;
- full-post years = 2017–2020;
- pre-placebo years = 2012–2014;
- no outcome interpolation.

## Donors

Primary holdout donor pool is the **strict 115-country pool** frozen in `data/israel_holdout_donors.csv`.

A donor must:

1. have >=2 observed WHR years in 2012–2015;
2. have >=2 observed WHR years in 2017–2020;
3. have no World Bank annual-leave jump in 2011–2021;
4. have no already verified leave treatment in the focal 2012–2020 window;
5. not be a country whose WORLD 2015/16 → Equal Futures 2026 annual-leave category changed.

Rule 5 is deliberately conservative and was added **before inspecting Israel's outcome**.

## Primary transparent estimator

Use the same donor-adjusted change estimator as frozen Pilot-0:

`gap_k = (Y_ISR,2016+k − Y_ISR,2015) − mean_d(Y_d,2016+k − Y_d,2015)`.

Report every available k in −4…+4 except k=0. The event-level full-post summary is the equal-weight mean of k=+1…+4.

## Pretrend diagnostic

Use k=-4,-3,-2 relative to 2015.

Retain the existing diagnostic thresholds:

- flag if mean absolute pre gap >0.30;
- flag if any absolute pre gap >0.50.

A pretrend flag is not an exclusion rule; it weakens interpretation.

## Robustness frozen before outcome

1. repeat with the 120-donor pool under the original Pilot-0 contamination rule;
2. leave-one-donor-region-out using World Bank regions where available, only as a fragility diagnostic;
3. donor-median counterfactual alongside donor mean;
4. report treated raw change and donor change separately;
5. no p-value as headline;
6. no secondary Positive/Negative Affect analysis.

A synthetic-control specification may be explored only as a **secondary** diagnostic because four fixed pre years are too short to support a strong synthetic-control claim without overfitting.

## Claim rule

- Israel result is reported separately from the original eight-event panel.
- A positive Israel gap does not establish a global annual-leave effect.
- A negative/null Israel gap does not prove annual leave has no effect.
- The strongest permissible interpretation concerns one national leave-specific phased reform with a population-level outcome and substantial treatment dilution.
