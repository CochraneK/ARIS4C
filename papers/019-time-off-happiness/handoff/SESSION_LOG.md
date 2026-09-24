# ARIS4C019 · Session log

## 2026-09-21

- Registered ARIS4C019.
- Performed an initial source and literature feasibility scan.
- Separated four time-off constructs and defined a longitudinal/policy-reform identification hierarchy.
- Added a data-source audit and continuity package.

- Corrected and verified the legal-year event clock so partially exposed reform years are excluded rather than counted as pre-treatment.
- Froze pre-treatment macro covariates and ran the outcome-blind WDI/WHR coverage gate; 6/8 headline events have >=2 pre observations for all three frozen covariates.
- Formally unlocked Life Ladder only; positive/negative affect remain locked.
- Ran and CI-published the first 8-event clean-donor Life Ladder diagnostic plus leave-one-event-out and prespecified crisis/scope sensitivities.
- Recorded identification fragility: pooled mean +0.110, median -0.099, 5/8 negative; excluding Bahrain flips the pooled mean negative and Bahrain has a large pre-placebo gap.
- Added the modern staggered-DiD execution path; estimator verification is the next gate.
- Completed a post-unlock treatment-isolation audit across all 8 headline events and added machine-readable isolation flags.
- Found that China is the cleanest leave-specific legal reform currently in the pool, while Croatia/Kosovo/Kuwait/Bahrain are broad labour codes, Taiwan is a bundled working-time reform, Luxembourg combines annual leave with a new public holiday, and Canada is a broad federal labour-standards package.
- Added a specific Bahrain identification warning: 2011 domestic unrest and the subsequent 2012 macro rebound make the frozen T-1 reference especially vulnerable to rebound bias.
- Reframed the next gate toward legally verified stand-alone annual-leave reforms rather than adding more estimators or opening secondary affect outcomes.
- Validated a pinned WHR2024 annual mirror against official published summary statistics and an independent WHR2023 CSV transcription; all 2,199 overlapping Life Ladder values match at three decimals, with 26 additional 2022 observations and 138 observations in 2023.
- Ran the pre-frozen A/B/C source-refresh decomposition. The refreshed 2023 panel mean is +0.088, median -0.099, with 2 positive and 6 negative event means; Luxembourg flips negative and Bahrain remains the dominant positive event.
- Recomputed refreshed leave-one-out and sensitivity diagnostics; excluding Bahrain gives mean -0.117 with 6/7 negative event means.
- Confirmed that current WHR2025/WHR2026 Figure 2.1 public files are three-year averages, not annual country-year Life Ladder; annual 2024/2025 values will not be reconstructed from rolling averages.
- Completed the bounded 11-row World Bank legal-jump audit and admitted 0 new clean annual-leave holdouts. Added machine-readable and narrative legal isolation audit files.
- Scientific direction now shifts from searching for a positive leave effect to documenting the identification-feasibility boundary and preserving Mexico 2023 as a future holdout pending >=2 verifiable annual post years.
- Added a modern legal discovery route using the WORLD 2015/16 and Equal Futures 2026 annual-leave snapshots without treating snapshot differences as treatments.
- Identified Israel Annual Leave Law Amendment No.15 as a cleaner leave-specific national reform; legally verified staged implementation (2016-07-01, 2017-01-01).
- Froze Israel's outcome-blind design before viewing Life Ladder: T=2016, reference=2015, transition year excluded, full post 2017–2020, 115-country strict donor pool.
- Opened only Life Ladder after the freeze. Strict-115 full-post mean = +0.002; 120-donor sensitivity +0.010; donor-median sensitivity +0.008; frozen pretrend warning thresholds not triggered.
- Completed standardized leave-one-region-out robustness after resolving all donor-region aliases; post means remain near zero across omitted regions.
- Added post-outcome reference-year fragility audit. Earlier/multi-year baselines produce negative estimates, demonstrating baseline sensitivity; none is promoted over the pre-frozen 2015 reference.
- Verified official Knesset staged implementation and Bank of Israel documentation of 2014/late-2015 security disturbances relevant to reference-year interpretation.
- Updated literature position with ILO 2026 global annual-leave brief and Equal Futures 2026 193-country legal data.
- Created and locked Pilot-0 interpretation: no robust positive or negative population Life Ladder effect is established.
- Started bilingual English/Chinese working-paper drafts and reframed the manuscript around legal-event identification, source robustness and independent holdout logic.

- 2026-09-24 final public-delivery audit: canonical EN/ZH Markdown and four SVG figures were independently rebuilt into public PDFs and passed machine/text plus render-first visual QA (EN 12 pages, ZH 7 pages; CJK and figure pages visually clean).
- A watched builder revision (`dc857f638517a25b7cb5b3b70284dd4aa6955682`) was committed to trigger the canonical GitHub PDF workflow, but no bot PDF commit appeared and `docs/paper/019/en/main.pdf` / `zh/main.pdf` remain absent.
- Project state was therefore corrected to 98% / BLOCK: scientific and submission work is complete; the sole remaining gate is canonical Git binary publication and verification. Do not reopen outcomes or legal-event discovery to fill this engineering gap.
