# ARIS4C019 · Expanded modern module QA

**Date:** 2026-09-24  
**Status:** repository readback PASS; CI execution pending repository-wide Actions recovery

## Canonical readback

- `code/expanded_modern_panel_analysis.py`: present; public WHR/hours transport pinned to commit `a5aa864fd27a044b8ffc0a4432e6e18ab1532247`; WDI macro transport pinned to `c6c27edc5f1359cc51def03e8d3514359f1c7d40`.
- `data/expanded_modern_panel_first_statistics.csv`: present.
- `data/expanded_modern_panel_A1_macro.csv`: present.
- `data/legal_time_aligned_panel_falsification.csv`: present.
- `data/macro_attenuation_decomposition.csv`: present.
- `data/wdh_trends_mean_variable_registry.csv`: **124 rows**.
- `data/working_hours_country_coverage_summary.csv`: **130 rows**.
- `paper.json`: valid JSON; status `expanded-modern-module-locked-historical-synthesis-active`; version `v0.10.0`.
- `papers/dashboard.json`: valid JSON; project 019 = **75% / active**.

## Scientific cross-checks

- statutory-leave availability contract: **161 countries / 1,934 country-years**;
- A1 complete-case leave contract: **1,885 rows / 157 countries**;
- actual-hours source contract: **5,063 rows / 130 countries / 1870–2023**;
- verified legal-vs-WB timing audit: **9 events**, mean offset **+1.22 years**;
- modern interpretation lock records the sign-flip falsification and prohibits causal interpretation of either WB-year or legal-year broad-panel FD signs.

## Known execution limitation

The reusable Python pipeline has been code-reviewed and its source/data contracts are pinned, but an independent repository CI execution cannot be counted as PASS while the repository-wide GitHub Actions pre-runner startup failure persists.

This does **not** invalidate the committed result tables generated in the active analysis surface. It means a second execution surface remains an engineering reproducibility gate.

## Gate

Do not reopen modern specifications merely to chase significance. Continue to historical numeric outcome materialization and cross-instrument synthesis.
