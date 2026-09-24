# ARIS4C019 · Process status

- Stage: **Expanded modern statistics LOCKED · historical outcome/legal reconstruction active**
- Activity: **active**
- Progress: **75%**
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
- ILO: C052 current official count **54 ratifications**; C132 **39 ratifications**; C132 complete 39-country seed is materialized and primary-date verification is partial.

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
