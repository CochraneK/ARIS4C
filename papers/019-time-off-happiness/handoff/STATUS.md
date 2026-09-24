# ARIS4C019 · Current status

- **Project status:** expanded-modern-module-locked-historical-synthesis-active
- **Activity:** active
- **Portfolio progress:** 75%
- **Current stage:** Modern + historical trend layers LOCKED · century-scale legal spine active · historical reform registry v2 frozen

## Complete / frozen

- Pilot-0 causal-identification sub-study: complete/frozen; interpretation unchanged.
- Expanded modern availability panel: **161 countries / 1,934 country-years**.
- Expanded modern statistical module: TWFE, within-between, FD, macro A1, support subsets, country trends, RCS, lags, influence, joint hours+leave, legal-credibility restriction and legal-time falsification.
- Modern interpretation: locked in `process/EXPANDED_MODERN_INTERPRETATION_LOCK.md`.
- Actual-hours coverage: **130 countries / 5,063 observations / 1870–2023**.
- Prewar hours–WDH bridge: **14/14 earliest hours countries** appear in WDH long-run registry.
- WVS Waves 1–7: **295 country-wave rows / 107 distinct codes**.
- WDH public long-run mean registry: **124 variable series / 61 nation labels / earliest 1946**.
- Eurobarometer life-satisfaction measurement chain: **1973–2026**.

## Main modern finding

The broad modern panel does not produce a stable positive or negative aggregate leave/hours result.

The strongest falsification is timing:
- verified WB leave jumps occur on average **1.22 years after** the actual legal effective year;
- macro-adjusted verified-changer FD is strongly negative when timestamped by WB reporting year;
- the same verified leave steps flip positive when aligned to legal effective year.

Therefore neither sign is promoted as causal, and positive WB lag-2/lag-3 coefficients are not interpreted as delayed well-being benefits.

## Remaining project gate

- acquire/materialize numeric WDH long-run outcome observations;
- acquire/aggregate Eurobarometer and EVS/WVS outcomes;
- complete primary-source C052/C132 rows;
- construct national paid-leave legal chronology;
- run historical source-specific association models;
- synthesize instrument/event estimates;
- rebuild EN/ZH manuscript around the full long-run project.

No current design blocker. Some source acquisition requires a binary-capable or registered-data execution surface.


## 2026-09-24 historical trend milestone

- Full published WDH Table 2: **200 displayed rows / 199 exact unique trend rows**.
- Exact source duplicate retained in verbatim materialization but excluded from analytical weighting: UK ls4 1990–2020.
- Same-window actual-hours bridge: **190 trend rows / 46 countries**.
- One-row-per-country correlation: Pearson **-0.057**, Spearman **-0.045**; full-series Pearson **+0.101**, Spearman **+0.094**.
- Historical trend interpretation is locked: **no stable monotonic hours-trend × well-being-trend relationship**.
- Earlier stronger negative result from the pre-1990-start subset is superseded as sample-selection sensitive.
- Taiwan working-hours join was repaired; A0 hours = **2,015 / 130**, joint = **1,663 / 129**.
- Independent statsmodels validator is committed, but Actions run **35977496016** failed pre-runner with zero executed steps; do not call validation PASS yet.


## New gates closed / advanced

- ILO convention history is now closed at **C052 54/54** and **C132 39/39** exact primary NORMLEX dates.
- C052→C132 overlap = **18 countries**; mean/median ratification gap = **27.8 / 26.4 years**.
- C132 declaration units are explicitly classified without converting weeks/calendar days/months into fake working-day equivalents.
- Official WDH HTML annual reconstruction has a validated extraction contract. USA hl4 and Japan ls4 reproduce published long-run slopes to <0.001/year from displayed HTML values.
- Full WDH HTML batch builder is committed; execution awaits a network-capable runner.


## Century legal spine + 2012 global statistics

- 1934 benchmark from ILO historical review: only **12 countries** had general statutory paid annual leave covering all workers.
- 2000 ILO/NATLEX legal snapshot: **41-country** selected late-20th-century frame.
- 2012 ILO/TRAVAIL snapshot: **155 rows / 147 exact values**.
- 2012 ILO vs WB first-year legal-value crosscheck: **143 exact pairs, r=0.832, MAE=2.17 days**; large gaps are a legal QA queue, not values to average.
- Historical reform registry v2: Bulgaria 2001 and Slovakia 2002 A-tier; Namibia 2008 and GB 2007/2009 B-tier; Nicaragua/Algeria/Mali rejected.
- 2012 legal leave x WHR Life Ladder matched sample: **114 countries**. Adjusted +5-day coefficient = **+0.028 [95% CI -0.103, +0.160]**; nonlinearity/region/influence checks do not reveal a hidden robust effect.
- WHR is not temporally adequate for the early historical reforms; next outcome route is official WDH annual HTML + EVS/WVS/Eurobarometer.
