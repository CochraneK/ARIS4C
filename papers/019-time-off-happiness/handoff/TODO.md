# ARIS4C019 · TODO

## P0H · Historical expansion / coverage rebuild

- [x] Reopen ARIS4C019 beyond the narrow leave-specific Pilot-0 after scope audit.
- [x] Freeze multi-resolution historical design: legal/institutional history -> country-wave well-being -> annual Gallup-era panel.
- [x] Add historical source matrix spanning ILO C052/C132, national laws, WORLD/Equal Futures, OECD historical hours, WDH, Cantril, Eurobarometer, WVS/EVS and Gallup/WHR.
- [~] Build country × source × year/wave coverage inventory for 1900–2026 exposures and 1945–2026 subjective well-being. Modern WB×WHR 161-country/1,934-year overlap, WVS 295 country-wave rows/107 codes, Cantril seed, Eurobarometer registry summary and WDH acquisition gate are complete; full historical country-year reconstruction remains.
- [x] Ingest ILO C052/C132 ratification/denunciation histories as institutional anchors. C052 is now 54/54 exact primary rows; C132 is 39/39 exact primary rows; succession history and declaration-unit guardrail are materialized. Ratification remains distinct from domestic legal adoption.
- [ ] Build national paid-leave legal chronology with primary-law effective dates and entitlement levels, prioritizing earliest adoption and major upgrades.
- [~] Build historical actual-working-hours panel, retaining source/sector comparability flags. Current transport-pinned source has 5,063 observations / 130 countries / 1870–2023; 14-country 1870–1938 seed and coverage/WDH bridge are materialized. Further source-version/comparability work remains.
- [~] Build World Database of Happiness historical outcome table with question-family metadata and comparable-subset flags. Public registry + full 200-row published trend table are materialized. Official HTML year-level reconstruction is now validated on USA hl4 and Japan ls4 to <0.001/year slope error; batch builder is committed. Full annual HTML batch remains pending a network-capable runner.
- [~] Add Cantril 1957–1963, Eurobarometer 1973+, WVS/EVS 1981+ and Gallup-era outcome coverage manifests. Cantril/WVS/Eurobarometer/Gallup coverage scaffolds are materialized; WDH XLSX and full EVS country-wave expansion remain.
- [x] Freeze no-effect-inspection coverage gates and expanded statistical plan before running new expanded association/causal models.

## P1G · Century-scale legal reconstruction

- [x] Close full C052 54/54 and C132 39/39 primary ratification registers.
- [x] Recover late-20th-century ILO/NATLEX 2000 41-country annual-leave snapshot.
- [x] Recover ILO/TRAVAIL 2012 155-country standardized annual-leave cross-section.
- [x] Crosscheck ILO 2012 against WB 2012 and preserve 22 >=5-day discrepancies as QA cases.
- [x] Freeze historical reform registry v2: BGR 2001, SVK 2002, NAM 2008, GBR 2007/2009; reject NIC/DZA/MLI artifacts.
- [~] Execute outcome-blind historical reform registry v2 against pre-WHR outcome sources. WHR feasibility gate says BGR/SVK unavailable and NAM/GBR too sparse for primary event inference; route to WDH HTML / EVS-WVS / Eurobarometer.
- [~] Push national-law snapshots further back toward 1960s/1970s using ILO 1964/1969 revision reports and Legislative Series where recoverable.

## P1H · Expanded statistics

- [~] Independently validate key modern FE/FD coefficients with the committed statsmodels implementation. Validator/workflow are ready; GitHub Actions run 35977496016 fails before any step due the repository-wide pre-runner issue.

- [x] Execute and freeze the expanded modern WHR association module (TWFE / within-between / FD / A1 / support / trends / spline / lags / influence / joint hours+leave).
- [x] Quantify legal-vs-WB timing error: verified WB jump timing averages +1.22 years relative to law.
- [x] Run legal-time falsification; same verified-changer FD flips sign when re-timestamped from WB report year to legal effective year.
- [x] Freeze modern interpretation in `process/EXPANDED_MODERN_INTERPRETATION_LOCK.md`.
- [x] Add same-sample macro attenuation decomposition to separate complete-case selection from control adjustment.

- [ ] Descriptive atlas: decade diffusion, regional trajectories, country timelines, exposure distributions, happiness trajectories and happiness inequality where available.
- [~] Country/time fixed-effects and within-between models for comparable panels. Modern WHR leave/hours module executed and interpretation-locked; published WDH historical trend×hours bridge executed and locked; raw-year WDH/Eurobarometer/WVS-EVS instrument-specific panels remain.
- [~] Nonlinear dose-response and lag/distributed-lag models with explicit association-only interpretation unless stronger identification is met. Modern RCS + lag stack executed; WB report-year lag interpretation is timing-falsified and historical instruments remain.
- [ ] Instrument-specific outcome models plus overlap-country bridge diagnostics; do not pool raw happiness scales blindly.
- [ ] Random-effects / multilevel synthesis across survey families.
- [ ] Expand verified reform inventory beyond the original eight-event cap.
- [ ] Run modern staggered DiD / stacked event study / synthetic-control family where assumptions permit.
- [ ] Event-level meta-analysis and influence diagnostics.
- [ ] Prespecified heterogeneity by reform size, baseline entitlement, region, income, hours, informality, labor-force exposure and welfare/labor institutions. Do only after historical instrument materialization / sufficient event count.

## P0 · Measurement and legal-event gate

- [x] Freeze statutory annual-leave definition.
- [x] Keep annual leave, public holidays, actual hours and leave utilization separate.
- [x] Build source × country × year coverage artifacts.
- [x] Verify World Bank historical leave fields and country-year availability.
- [x] Audit annual WHR Life Ladder coverage and transport provenance.
- [x] Create and legally verify the frozen Pilot-0 reform inventory.
- [x] Close bounded verification of all 11 high-value unregistered World Bank leave jumps.
- [x] Build WORLD 2015/16 → Equal Futures 2026 legal-snapshot candidate screen.
- [x] Verify and freeze Israel 2016 as an independent leave-specific holdout before outcome inspection.

## P1 · Primary Life Ladder analysis

- [x] Freeze annual Life Ladder as primary outcome.
- [x] Freeze legal-year event clock and transition-year exclusion.
- [x] Freeze macro covariates and pre-treatment-only handling.
- [x] Freeze estimator hierarchy before outcome inspection.
- [x] Run outcome-blind donor/support diagnostics.
- [x] Create outcome-unlock manifest.
- [x] Run transparent eight-event donor-adjusted analysis.
- [x] Run leave-one-event-out and crisis/scope/covariate sensitivities.
- [x] Run modern staggered-adoption / heterogeneous-treatment diagnostics and document failed/fragile pretrend support.
- [x] Validate WHR2024 annual source refresh through 2023 and rerun the frozen stack.
- [x] Run Israel strict-115 holdout, original-rule donor sensitivity and donor-median sensitivity.
- [x] Run standardized Israel leave-one-region-out robustness.
- [x] Run post-outcome Israel reference-year/concurrent-shock fragility audit.
- [x] Freeze Pilot-0 interpretation.

## P2 · Manuscript and SIR submission package

- [x] Update literature position with ILO 2026 and Equal Futures 2026 legal sources.
- [x] Draft English working paper.
- [x] Draft Chinese working paper.
- [x] Build four-figure manuscript package.
- [x] Freeze manuscript result tables from machine-readable CSVs.
- [x] Run bilingual number / claim / figure-link QA.
- [x] Add methods and reproducibility appendix.
- [x] Freeze Social Indicators Research as primary target.
- [x] Build double-anonymous SIR Markdown submission draft.
- [x] Verify SIR Markdown gate: ~8.15k words, 218-word abstract, 6 keywords, ordered figures, no author/repository identity leakage.
- [x] Document substantive OpenAI/LLM assistance in Methods and keep AI out of authorship/evidence roles.
- [x] Remove duplicate partial legal-audit artifacts; retain the complete 11-row legal audit as the sole canonical audit.
- [x] Build and QA editable SIR DOCX source from the blinded manuscript.
- [x] Build reviewer PDF from the same frozen source and visually inspect pagination, equations, references and figure rendering.
- [x] Establish a genuinely anonymous reviewer data/code access path; do not expose the identifying repository in the blinded file.
- [ ] Fill author-side submission metadata separately: affiliation, corresponding email, ORCID if applicable, funding, competing interests, and any institution-specific ethics/exemption determination.
- [x] Freeze final submission manifest linking manuscript, figures, tables, number lock, QA results and anonymous review package.

## P2.5 · Portfolio public delivery

- [x] Diagnose canonical PDF workflow startup failure: run `35965678753` fails before build steps and a failed-job re-run reproduces the same zero-step condition; local fallback render/QA passes.
- [x] Add one-page visual explainer for Finish-state portfolio display.
- [x] Wire ARIS4C019 into the canonical bilingual public-PDF builder and CI workflow.
- [ ] Verify generated English and Chinese public PDFs are committed under `docs/paper/019/` and pass extractability/page-count checks.
- [ ] Run final repository output audit and only then promote dashboard activity to `finish` / 100%.

## P3 · Deferred / future confirmation

- [ ] Keep Mexico 2023 behind firewall until >=2 verifiable annual full-post Life Ladder observations exist.
- [ ] Seek true annual WHR/Gallup data through 2024/2025; do not reconstruct annual values from rolling three-year averages.
- [ ] Add actual-hours / leave-utilization triangulation only as a separate exposure/mechanism study.
- [ ] Prefer worker-level or subgroup outcomes for future leave-specific causal work.
- [ ] Positive/negative affect remain locked for the current Pilot-0 manuscript; opening them requires a separately frozen secondary-outcome plan.
