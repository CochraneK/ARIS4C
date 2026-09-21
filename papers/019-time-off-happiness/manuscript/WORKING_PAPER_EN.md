# Statutory Paid Annual Leave and National Life Evaluation

## A Global Legal-Event Audit and Falsification-First Holdout Study

**ARIS4C019 — Working paper v0.1**  
**Date:** 21 September 2026

### Abstract

Whether statutory paid annual leave improves population well-being is plausible but difficult to identify cross-nationally. We combine verified legal reform timing with annual Gallup/World Happiness Report Life Ladder data and explicitly separate statutory annual leave from public holidays, actual working hours and leave utilization. An eight-event reform panel initially yields a positive mean donor-adjusted post-reform gap (+0.110 Life Ladder points) but a negative median (−0.099), with five of eight event means negative. Updating the same frozen design to the World Happiness Report 2024 annual panel through 2023 reduces the mean to +0.088 and leaves six of eight event means negative; omitting the most influential event, Bahrain, changes the mean to −0.117. Modern staggered-adoption diagnostics also fail to support a clean pooled causal interpretation, and legal review shows that most original events are broad labour/time-off packages rather than isolated annual-leave reforms.

We therefore conduct two outcome-blind legal audits. A bounded review of 11 remaining World Bank annual-leave discontinuities admits no new clean holdout. A separate comparison of WORLD 2015/16 and Equal Futures 2026 legal snapshots identifies Israel's 2016 Annual Leave Law amendment as a cleaner leave-specific reform. Before opening Israel's outcome, we freeze a 2015 reference year, a 2016 transition exclusion, 2017–2020 full-post years, and a 115-country contamination-screened donor pool. The frozen donor-adjusted full-post mean is +0.002, with no prespecified pretrend flag. However, post-outcome baseline diagnostics range from approximately −0.34 to zero depending on the pre-period reference, preventing a precise null interpretation.

Across these analyses, statutory annual-leave reforms do not show a robust, directionally stable population Life Ladder response. The findings primarily demonstrate the importance of legal treatment isolation, exposure-outcome alignment and baseline sensitivity in cross-national policy evaluation. They do not imply that actual vacations or paid leave lack worker-level well-being benefits.

**Keywords:** paid annual leave; vacation; life satisfaction; Life Ladder; working time; legal epidemiology; difference-in-differences; event study; policy evaluation

---

## 1. Introduction

Paid annual leave is a core institution of working-time regulation. The International Labour Organization treats paid holidays as an important component of worker protection and Convention No.132 establishes an international reference standard. A growing literature links shorter working time, vacations and recovery from work to job satisfaction, stress and other well-being outcomes. Yet a different question remains difficult: when national law increases statutory paid annual leave, does population life evaluation measurably change?

A simple cross-country correlation is poorly suited to this question. Countries with generous leave also differ in income, social protection, institutions, labour-market composition, culture and many other determinants of well-being. Statutory entitlement also differs from actual leave taken. Moreover, legal changes in annual leave are often enacted inside broad labour-code reforms that simultaneously alter working hours, dismissal rules, public holidays or other worker protections.

This study therefore asks a narrower question:

> Are legally verified changes in statutory paid annual-leave entitlement followed by directionally stable changes in annual national Life Ladder, under designs that explicitly audit legal treatment isolation and pre-treatment comparability?

The study was designed around falsification rather than effect discovery. Event timing, donor eligibility, outcome hierarchy and macro covariate rules were frozen before the first post-reform Life Ladder inspection. After the first analysis revealed substantial fragility, subsequent legal-source expansion was kept outcome-blind. This process eventually produced an independently frozen Israeli holdout that was not part of the original event set.

The contribution is methodological as much as substantive. We show that three issues materially alter the apparent conclusion: legal-policy bundling, influential events and reference-year choice. The resulting evidence does not support a robust positive or negative population effect of statutory annual leave.

## 2. Conceptual framework

### 2.1 Exposure is statutory entitlement, not realized vacation

We distinguish four constructs:

1. statutory paid annual-leave entitlement;
2. statutory public holidays;
3. actual annual or weekly working time;
4. actual leave utilization.

Only the first is the focal exposure in the leave-specific track.

### 2.2 Why aggregate effects may be attenuated

A legal entitlement can have worker-level benefits while producing little movement in national Life Ladder because only part of the population is employed, only part of the workforce is newly treated, take-up can be incomplete, workload can adjust around leave, and broad life evaluation responds to many non-labour shocks.

### 2.3 Why direction is not predetermined

Additional leave could improve recovery and work-life balance. Conversely, legal entitlement may be weakly enforced, offset by workload intensification, or too small relative to macro and social shocks to shift annual national life evaluation.

## 3. Data

### 3.1 Outcome

The primary outcome is the annual Gallup/World Happiness Report **Life Ladder**, measured on a 0–10 scale. We do not use the published World Happiness ranking or a multi-year ranking average as the dependent variable.

The first-look panel used the WHR2023 historical annual file through 2022. A post-unlock robustness update validated a pinned WHR2024 annual mirror through 2023. The two releases share 2,199 country-year Life Ladder observations that are identical at published three-decimal precision; the newer release adds observations in 2022 and 2023.

Positive and negative affect were preregistered as secondary outcomes but remain unopened for this Pilot-0 paper.

### 3.2 Legal exposure sources

Legal timing and entitlement changes were reconstructed from primary or official legal sources. World Bank Employing Workers data were used as a historical screening/corroboration source, not as final legal authority.

A later discovery layer used:

- WORLD Policy Analysis Center's 2015/16 annual-leave snapshot;
- Equal Futures' 2026 Annual Leave and Weekly Rest dataset;
- country-level primary legal sources for exact reform verification.

Snapshot differences generated candidates only; they were never treated as reforms without independent legal verification.

## 4. Design

### 4.1 Frozen eight-event stress-test panel

The original headline pool contained eight Tier-A reforms with verified timing, WHR coverage and World Bank directional corroboration.

Event time is anchored to the legal effective year. The last full untreated year is the reference period. A partial-exposure reform year is excluded and the following calendar year is the first full post year.

Donor eligibility requires:

- at least two observed pre and two observed post Life Ladder years;
- no nearby statutory annual-leave jump;
- no verified leave treatment in the focal event window;
- no interpolated outcome values.

### 4.2 Estimation

The transparent event-specific estimator compares the treated country's change from the frozen reference year with the mean change among contamination-screened donors.

Modern staggered-adoption specifications based on Callaway–Sant'Anna and Sun–Abraham logic are used as robustness diagnostics; conventional TWFE event-study coefficients are not used as the headline causal estimate.

### 4.3 Outcome firewall

Legal timing, outcome availability, donor contamination and macro covariate support were inspected before outcome unlock. Post-treatment Life Ladder values were not inspected until the design freeze was complete.

### 4.4 Independent Israel holdout

After the original analysis, a bounded legal audit and a separate 2015/16→2026 snapshot comparison were conducted without inspecting candidate-specific Life Ladder effects.

Israel's Annual Leave Law Amendment No.15 directly increased annual-leave entitlement for workers in their first four years of tenure. One additional day applied from July 2016 and another from January 2017.

Before opening the outcome we froze:

- event clock: 2016;
- reference: 2015;
- 2016 excluded as transition;
- full post: 2017–2020;
- strict donor pool: 115 countries.

## 5. Results

### 5.1 Original eight-event panel

The first WHR2023 donor-adjusted analysis yields a mean full-post gap of **+0.110** but a median of **−0.099**. Five of eight event-level means are negative. Bahrain is the dominant positive event; removing it reverses the pooled mean.

These properties alone argue against interpreting the positive mean as a stable average annual-leave effect.

### 5.2 WHR2024 source refresh

Using the same frozen event definitions and donors with the WHR2024 annual panel through 2023:

- pooled mean: **+0.088**;
- pooled median: **−0.099**;
- positive event means: **2/8**;
- negative event means: **6/8**.

Luxembourg changes from positive to negative. Leaving Bahrain out gives **−0.117**.

![Figure 1. Refreshed eight-event heterogeneity](../figures/fig1_eight_event_refresh.svg)

*Figure 1. Event-level WHR2024-refreshed donor-adjusted gaps. The large Bahrain estimate makes the pooled mean highly influence-sensitive.*

### 5.3 Legal treatment-isolation audit

Most original reforms alter more than annual leave. A bounded review of all 11 remaining unregistered World Bank annual-leave discontinuities produces **zero** new clean leave-specific holdouts.

This audit prevents database discontinuities or broad labour-code changes from being promoted into treatments merely to increase sample size.

![Figure 4. Legal treatment-isolation funnel](../figures/fig4_legal_isolation_funnel.svg)

*Figure 4. Candidate discovery is deliberately separated from treatment admission. The historical World Bank queue produced no new clean holdout; the modern legal-snapshot screen produced Israel as a current holdout and Mexico as a future one.*

### 5.4 Israel holdout

Under the strict 115-country donor pool, the event-time adjusted gaps are:

| Event time | Calendar year | Adjusted gap |
|---:|---:|---:|
| +1 | 2017 | +0.177 |
| +2 | 2018 | −0.265 |
| +3 | 2019 | +0.114 |
| +4 | 2020 | −0.018 |

The equal-weight full-post mean is **+0.002**.

The frozen pretrend warning thresholds are not triggered. Using the original 120-donor contamination rule gives +0.010; using a donor-median counterfactual gives +0.008. Leave-one-region-out estimates remain close to zero.

![Figure 2. Israel holdout event time](../figures/fig2_israel_event_time.svg)

*Figure 2. Israel donor-adjusted event-time gaps under the pre-frozen strict-115 design.*

### 5.5 Reference-year fragility

The near-zero result depends on the pre-frozen last-pre-year normalization. Post-outcome diagnostics using earlier or multi-year baselines are negative:

- 2013 reference: approximately **−0.306**;
- 2014 reference: approximately **−0.337**;
- 2013–2015 mean baseline: approximately **−0.219**;
- 2012–2015 mean baseline: approximately **−0.175**.

These are not alternative preferred estimates. They show that a modest statutory treatment is difficult to distinguish from year-to-year national Life Ladder variation.

![Figure 3. Israel reference sensitivity](../figures/fig3_israel_reference_sensitivity.svg)

*Figure 3. Reference-year sensitivity is a post-outcome fragility diagnostic. The 2015 specification remains primary because it was frozen before the holdout outcome was opened.*

## 6. Discussion

The evidence does not support the simple proposition that increasing statutory annual leave reliably raises national life evaluation. The original positive pooled mean is fragile to influential-event removal, legal treatment isolation and newer outcome observations. The cleaner Israel holdout is near zero under the frozen last-pre-year specification but does not retain a stable direction under post-outcome baseline diagnostics.

This should not be interpreted as evidence that vacations are ineffective. The study's outcome is population Life Ladder, while much of the vacation literature studies exposed workers, short-term recovery, stress, job satisfaction or mental health. Treatment dilution is therefore substantial.

The study also demonstrates a sequencing principle for cross-national policy evaluation: **legal treatment isolation should precede estimator sophistication**. A modern difference-in-differences estimator cannot solve a treatment-definition problem.

### 6.1 Strengths

- design and outcome firewall frozen before first effect inspection;
- exact legal timing from primary/official sources;
- no interpolation of annual happiness outcomes;
- explicit donor contamination screen;
- source-version robustness;
- bounded legal search rather than significance-driven event expansion;
- independently frozen post-discovery holdout.

### 6.2 Limitations

- small number of clean reforms;
- annual country means rather than exposed-worker microdata;
- statutory entitlement is not actual leave use;
- treatment intensity differs across tenure groups and jurisdictions;
- national shocks can dominate small policy changes;
- donor-adjusted estimators do not guarantee parallel trends;
- the Israel holdout has only four full post years;
- WHR2025/2026 freely downloadable Figure 2.1 files use multi-year averages rather than the required annual outcome series.

## 7. Conclusion

Across the currently reproducible annual Life Ladder evidence, statutory paid annual-leave reforms do not show a robust, directionally stable population-level effect. Apparent positive signals weaken when legal treatment isolation, influential events, source refreshes and reference-year sensitivity are made explicit.

The main contribution is therefore not a positive or negative leave coefficient. It is a transparent demonstration that credible evaluation of annual-leave law requires exact legal-event reconstruction, careful exposure-outcome alignment and prospective robustness rules.

Future work should evaluate newly emerging leave-specific reforms with longer annual follow-up and, where possible, worker-level outcomes matched to the legally treated population.

## References · core working list

- Callaway, B., & Sant'Anna, P. H. C. (2021). Difference-in-Differences with multiple time periods. *Journal of Econometrics*. https://doi.org/10.1016/j.jeconom.2020.12.001
- International Labour Organization. (2026). *Global legislative trends on paid annual leave*.
- Lepinteur, A. (2019). The shorter workweek and worker wellbeing: Evidence from Portugal and France. *Labour Economics*. https://doi.org/10.1016/j.labeco.2018.05.010
- Sun, L., & Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. *Journal of Econometrics*. https://doi.org/10.1016/j.jeconom.2020.09.006
- Voglino, G., et al. (2022). How the reduction of working hours could influence health outcomes: a systematic review. *BMJ Open*. https://doi.org/10.1136/bmjopen-2021-051131
