# ARIS4C019 · Manuscript Number / Claim QA

**Run:** 2026-09-21  
**Status:** **PASS**

This QA compares the bilingual working-paper drafts against committed machine-readable result files. It does not recompute estimators; it verifies that manuscript-facing rounded numbers and figure links agree with canonical CSV outputs.

## Number checks

| Check | Expected | EN | ZH |
|---|---:|---:|---:|
| WHR2024 mean | +0.088 | PASS | PASS |
| WHR2024 median | −0.099 | PASS | PASS |
| exclude Bahrain | −0.117 | PASS | PASS |
| Israel primary | +0.002 | PASS | PASS |
| Israel 120 donor | +0.010 | PASS | PASS |
| Israel donor median | +0.008 | PASS | PASS |
| Israel 2013 ref | −0.306 | PASS | PASS |
| Israel 2014 ref | −0.337 | PASS | PASS |
| Israel mean1315 | −0.219 | PASS | PASS |
| Israel mean1215 | −0.175 | PASS | PASS |

## Figure-link checks

| Figure | EN | ZH |
|---|---:|---:|
| fig1_eight_event_refresh.svg | PASS | PASS |
| fig2_israel_event_time.svg | PASS | PASS |
| fig3_israel_reference_sensitivity.svg | PASS | PASS |
| fig4_legal_isolation_funnel.svg | PASS | PASS |

## Claim-language guard

Flagged strong-causal phrases searched:

- `statistically significant`
- `proves that`
- `proves annual leave`
- `annual leave has no effect`
- `causes happiness`

Hits: **none**

## Canonical machine-readable inputs

- `data/whr2024_refresh_pooled.csv`
- `data/whr2024_refresh_sensitivities.csv`
- `data/israel_holdout_summary.csv`
- `data/israel_reference_sensitivity.csv`
- `data/israel_holdout_event_time.csv`

The exact source blob SHAs and unrounded locked values are stored in `data/manuscript_number_lock.json`.

## Boundary

A PASS here means manuscript numbers match committed data. It does **not** upgrade identification strength or validate causal assumptions.
