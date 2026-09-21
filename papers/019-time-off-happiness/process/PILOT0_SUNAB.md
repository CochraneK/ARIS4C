# ARIS4C019 · Pilot-0 Sun–Abraham robustness

> Fully interacted saturated event study on the same frozen eight-event Life Ladder design. This is a robustness specification, not a new sample-selection step.

- PyFixest version: **0.40.1**.
- Frozen treated countries: **8**.
- Common clean never-treated control universe: **66 countries**.
- Treated outcome window: **legal T-4 through T+4**.
- Legal effective year is the treatment cohort.
- Mid-year transition outcome at legal T is masked; it anchors event time but is not used as an outcome observation.
- Reference period: legal T-1 (the last full untreated year).
- Country and calendar-year fixed effects; standard errors clustered by country.
- Treatment-heterogeneity diagnostic: **{'available': True, 'pvalue': 1.0}**.

## Aggregated event-time output

~~~text
 period  Estimate Std. Error   t value  Pr(>|t|)      2.5%     97.5%
   -4.0 -0.123543     0.1518 -0.813851   0.41573 -0.421065   0.17398
   -3.0  0.044684    0.12931   0.34556  0.729674 -0.208759  0.298128
   -2.0  0.182517   0.062171  2.935739  0.003328  0.060665  0.304369
    0.0 -0.030376   0.056652 -0.536179  0.591835 -0.141411   0.08066
    1.0 -0.025312   0.114308 -0.221434  0.824755  -0.24935  0.198727
    2.0  0.121981   0.114556  1.064812  0.286961 -0.102545  0.346506
    3.0  0.259069    0.06857  3.778143  0.000158  0.124673  0.393465
    4.0   0.01494   0.111048  0.134537  0.892978 -0.202711  0.232591
~~~

## Interpretation boundary

- Only eight treated countries are available; cluster-robust asymptotics are weak for treatment-side inference even with many controls.
- A non-zero pre-treatment lead weakens parallel-trends credibility and cannot be repaired by a positive post coefficient.
- The transition-year mask is part of the pre-outcome timing freeze, not a result-driven exclusion.
- Positive/negative affect remain locked.
