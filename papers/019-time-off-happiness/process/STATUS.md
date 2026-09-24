# ARIS4C019 · Process status

- Stage: **Modern + published historical trends LOCKED · ILO convention history CLOSED · raw annual WDH/national-law reconstruction active**
- Activity: **active**
- Progress: **80%**
- Scope correction remains in force: the former 98% state described only the narrow Pilot-0 publication package, not the full original research question.

## Frozen sub-study

- Pilot-0: **PASS / frozen**. Eight-event WHR2024 refresh + independent Israel holdout + legal isolation audit + bilingual/SIR package remain preserved and must not be retroactively rewritten.
- Pilot-0 conclusion remains unchanged: no robust positive or negative population Life Ladder effect of statutory annual leave is established.

## Historical / coverage layer

- Canonical historical availability master: **8,579 coverage-only rows / 11 materialized source IDs** in `data/historical_country_source_coverage_v1.csv`; all rows record `value_inspected=no`.
- Working-hours source: **5,063 observations / 130 countries / 1870–2023**.
- Prewar hours seed: **14 countries / 98 observations / 1870–1938**; all 14 occur in the WDH long-run registry.
- WDH direct public long-run mean-variable registry: **124 series / 61 nation labels / earliest 1946**. The separate historical coverage master retains its stricter comparable-series normalization subset.
- Eurobarometer: general life-satisfaction measurement chain **1973–2026**; Mannheim trend file = **86 waves / >1,000,000 respondent cases** through 2002, numeric acquisition pending.
- WVS: Waves 1–7 registry = **295 country-wave rows / 107 distinct country-or-territory codes**; Waves 3–6 keep reported-count vs visible-table QA flags.
- WHR2024: annual Life Ladder source through 2023.
- ILO convention history: C052 **54/54 exact primary dates**, C132 **39/39 exact primary dates**; C052→C132 succession table and C132 declaration-unit guardrail are complete.

## Expanded modern annual analysis

- WB statutory leave × WHR: **161 countries / 1,934 country-years**; median support 14 years; 127 countries >=10 years; 57 >=15.
- Modern statistical stack executed: TWFE, within-between, first difference, support subsets, A1 macro adjustment, country trends, frozen RCS, report-year lags, influence diagnostics, legal-credibility restriction, joint hours+leave, and legal-time falsification.
- A1 leave TWFE (+5 days): **+0.045**, 95% CI **[-0.068, +0.159]**.
- A1 leave FD (+5 days): **-0.081**, 95% CI **[-0.184, +0.022]**.
- A1 hours TWFE (+100 annual hours): **+0.013**, 95% CI **[-0.038, +0.064]**.
- RCS nonlinearity is weak/imprecise; country-trend A1 estimates for both leave and hours cross zero.
- Same-sample macro decomposition shows the leave FD attenuation occurs mainly after adding unemployment, not merely from complete-case row loss.

## Timing falsification

- Across 9 verified legal changes with WB panel jumps, WB timing is on average **+1.22 years late** (median +1; range 0–2).
- Verified-changer A1 FD using WB report-year timing: about **-0.240 per +5 days**.
- Re-aligning the same verified steps to the **legal effective year**: about **+0.093**, with opposite sign.
- First-full-year alignment is positive but very imprecise.
- Therefore WB report-year FD and lag coefficients are timing-sensitive and cannot support a simple substantive causal claim.

## Modern interpretation lock

Canonical file: `process/EXPANDED_MODERN_INTERPRETATION_LOCK.md`.

Locked modern-layer conclusion:

> Large-sample modern panel evidence does not establish a stable positive or negative aggregate Life Ladder response to statutory paid annual leave or annual working hours. Statutory-leave coefficients are highly sensitive to how legal change is timestamped, while the negative between-country working-hours association does not reproduce as a stable within-country annual relationship.

This is **not** the final whole-project conclusion.

## Immediate gate

1. materialize numeric WDH long-run observations;
2. acquire/aggregate Eurobarometer + EVS/WVS outcomes;
3. finish C052/C132 primary rows and national paid-leave legal chronology;
4. run historical source-specific hours × well-being models;
5. synthesize instrument-specific coefficients / event effects;
6. rewrite EN/ZH manuscripts for the expanded project.

Existing Pilot-0 PDF Actions pre-runner failure remains an engineering issue only and is not the project-level scientific blocker.


## Full WDH published-trend layer

- IntechOpen/WDH Table 2 is now materialized at **200 displayed rows** spanning the 1940s–2000s start cohorts.
- A source-side exact duplicate (UK ls4 1990–2020) is preserved in the verbatim table but removed deterministically for analysis, leaving **199 unique trend rows**.
- Same-calendar-window actual-hours slopes are estimable under the >=10 observations / >=10-year gate for **190 unique trend rows / 46 countries**.
- Full-frame all-series correlation: Pearson **+0.101**, Spearman **+0.094**.
- One-longest-series-per-country: Pearson **-0.057**, Spearman **-0.045**.
- The earlier pre-1990-start negative Pearson pattern is therefore subset-sensitive and superseded for overall historical inference.
- Canonical historical interpretation is locked in `process/HISTORICAL_TREND_INTERPRETATION_LOCK.md`.
- The raw yearly `TrendsInNations-2023e.xlsx` workbook is still identified but not transferable in the current runtime.

## Reproducibility / QA update

- Working-hours join audit found and fixed `Taiwan` -> `Taiwan Province of China`; corrected A0 hours coverage is **2,015 country-years / 130 countries**, joint A0 **1,663 / 129**.
- A0→A1 decomposition shows hours attenuation is driven by macro adjustment rather than complete-case selection; leave-FD complete-case selection makes the negative A0 coefficient more negative, while macro adjustment moves it back across zero.
- Independent statsmodels validation code is committed in `code/validate_expanded_modern_panel_statsmodels.py`.
- GitHub Actions run **35977496016**, job **107561331580**, failed before any step executed (`steps=null`), matching the repository-wide pre-runner failure. Validator execution is therefore **pending**, not PASS.


## Raw WDH HTML reconstruction

- The transport-blocked XLSX is no longer the only raw-year route.
- Official WDH country/equivalent-measure HTML exposes year-level distributional findings and transformed 0–10 means.
- Reconstruction rule was validated independently on:
  - USA 111C / hl4 (1946–2017): reconstructed slope +0.001732 vs published +0.001;
  - Japan 121C / ls4 (1958–2013): reconstructed +0.004793 vs published +0.004.
- Differences are <0.001/year and consistent with displayed-value rounding.
- Canonical builder: `code/rebuild_wdh_html_annual_panel.py`.
- Full batch output is pending a network-capable runner; this is now an execution dependency, not an unresolved source-design problem.

## ILO institutional history closed

- C052 exact primary register: **54/54**; 37 currently in force, 17 not in force.
- C132 exact primary register: **39/39**; all currently in force.
- **18 countries** appear in both registers.
- Mean C052→C132 ratification gap among overlaps: **27.8 years**; median **26.4 years**.
- C132 declaration units are preserved without unsafe conversion.
