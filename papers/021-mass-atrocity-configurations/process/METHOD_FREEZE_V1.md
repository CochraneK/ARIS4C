# ARIS4C021 · Method Freeze v1

Date: 2026-09-24
Status: frozen before empirical outcome inspection

## Scientific target

Identify which conditions, configurations, sequences, and timing patterns distinguish mass-atrocity onset from non-onset, while separating:
- set-theoretic necessity/sufficiency;
- bottleneck necessity;
- onset timing;
- predictive discrimination;
- within-case mechanism.

No single method is treated as the project's identity or final adjudicator.

## Phase 1 · Historical replication frame

Use the same frozen historical case universe and condition matrix for three parallel analyses:

### A. Harff-style conventional baseline
Purpose:
- reproduce the classic structural-risk result as closely as possible;
- establish a conventional statistical reference point.

### B. QCA replication
Purpose:
- reproduce the published Williams configurational result;
- estimate necessity, sufficiency, consistency, coverage, equifinality and causal asymmetry.

### C. Coincidence Analysis (CNA)
Purpose:
- search for minimally sufficient/necessary redundancy-free configurational structures;
- test whether the QCA solution is method-dependent;
- allow causal-chain structures only if the historical data support a defensible ordering.

The three outputs are compared but not averaged into one score.

## Phase 2 · Modern necessity extension

Necessary Condition Analysis (NCA) is introduced only when continuous or meaningfully ordinal modern indicators are available.

Primary use:
- bottleneck-style necessity;
- effect size and ceiling-line diagnostics;
- bottleneck tables across outcome severity where defensible.

NCA will not be mechanically applied to every binary replication condition.

## Phase 3 · Temporal onset models

Use country-year data with pre-onset covariates:
- event-history / survival models;
- rare-events or penalized logistic models;
- explicit lag and duration dependence.

Purpose:
- ask when onset occurs;
- test whether configurational conditions precede rather than follow onset.

## Phase 4 · Predictive benchmark

Use strictly held-out evaluation:
- penalized regression baseline;
- nonlinear tree/boosting models where sample size permits;
- calibration + discrimination metrics;
- temporal or geographically grouped validation rather than random leakage-prone splits.

Prediction does not establish causal necessity or sufficiency.

## Phase 5 · Within-case mechanism

Select cases from cross-case results:
- typical configuration cases;
- deviant-consistency cases;
- deviant-coverage cases;
- high-risk non-onset cases.

Use comparative process tracing / sequence reconstruction to test whether the proposed mechanism and ordering actually occurred.

## Convergence rule

A condition receives a strong atlas role only when its evidence is transparent across the relevant methods.

Examples:
- QCA/CNA agree on a pathway -> stronger configurational support.
- NCA supports a bottleneck but QCA does not show set necessity -> report both, not a synthetic "necessary" label.
- Prediction importance without configurational/mechanistic support -> predictive marker only.
- Process tracing contradicts the proposed mechanism -> downgrade causal interpretation even if cross-case fit is high.

## Anti-overfitting rules

- freeze condition families before outcome inspection;
- keep the historical replication condition set fixed;
- no threshold tuning solely to recover a preferred historical formula;
- report all equally fitting CNA models;
- report contradictory QCA rows and limited diversity;
- perform leave-one-case / leave-one-region sensitivity;
- keep outcome definitions separate.

## Phase-1 deliverables

1. source manifest + SHA-256 records;
2. CASE_UNIVERSE_V1.csv;
3. CONDITION_MATRIX_V1.csv;
4. CODING_CROSSWALK_V1.md;
5. Harff baseline output;
6. QCA replication output;
7. CNA replication output;
8. CROSS_METHOD_REPLICATION_LOCK.md.

No modern extension begins before item 8 is frozen.
