# ARIS4C021 · Method Landscape v0.1

The scientific question is broader than QCA: **what conditions, combinations, sequences, and timing patterns distinguish mass-atrocity onset from non-onset?**

No single method is allowed to answer every part of that question.

| Method | Main question | Main contribution to 021 | Main limitation |
|---|---|---|---|
| csQCA / fsQCA / mvQCA | Which configurations are sufficient or necessary in set relations? | Reproduce Williams and inspect equifinality/asymmetry | Sensitive to calibration, case universe, limited diversity |
| Coincidence Analysis (CNA) | What minimally necessary/sufficient causal structures fit the data? | Alternative configurational minimization; explicit INUS-style structures | Still configurational and observational; model ambiguity must be reported |
| Necessary Condition Analysis (NCA) | Is a minimum level of X required for Y? | Test bottleneck-type necessity, especially continuous modern indicators | Focuses necessity rather than full causal mechanism |
| Event-history / survival models | When does onset occur, conditional on surviving without onset until t? | Model timing, duration dependence, time-varying covariates and lags | Usually effect-oriented rather than configurational |
| Rare-events logistic / penalized binary models | Which lagged factors change onset risk when events are rare? | Conventional inferential benchmark for country-year onset | Average-effect logic differs from necessity/sufficiency |
| Machine-learning prediction | Can held-out future/high-risk cases be predicted? | Out-of-sample benchmark; nonlinear interactions | Prediction is not causal explanation |
| Process tracing | Did the proposed mechanism operate inside selected cases? | Test typical and deviant QCA/CNA pathways within cases | Small-N and evidence intensive |
| Comparative process tracing / sequence analysis | Does order/timing of conditions matter? | Distinguish, e.g., exclusion→crisis→repression from crisis→exclusion | Requires rich temporal coding |
| Typological theory | What theoretically coherent case types/pathways exist? | Organize configurations into interpretable pathway families | Typology alone does not estimate causal effects |
| Bayesian networks / causal discovery | Which dependency/causal graph structures are compatible with data and assumptions? | Exploratory structure discovery and conditional-dependence checks | Strong assumptions; observational equivalence; not a replacement for design |
| Matched case-control / nested comparison | How do similar high-risk cases diverge? | Compare escalators with non-escalators under stronger comparability | Matching cannot remove unmeasured confounding |

## Recommended architecture for 021

### Layer 1 · Historical replication
- Reproduce Harff's conventional structural-risk model.
- Reproduce Williams with QCA.
- Run CNA on the same frozen matrix as a configurational robustness check.

### Layer 2 · Necessity
- Test single-condition set necessity.
- Where modern variables are continuous, run NCA bottleneck analysis.
- Do not call a condition "necessary" unless the claim is stable across reasonable calibrations.

### Layer 3 · Timing and sequence
- Build onset-time / country-year data.
- Use event-history models with lagged predictors.
- For selected cases, code event sequences and use comparative process tracing.

### Layer 4 · Prediction
- Benchmark rare-events logistic / penalized models against nonlinear machine-learning models.
- Separate explanatory claims from out-of-sample prediction.

### Layer 5 · Within-case mechanism
Select:
- typical pathway cases;
- deviant consistency cases;
- deviant coverage cases;
- high-risk non-onset cases.

Use process tracing to test whether the mechanism implied by a cross-case configuration actually occurred.

## Method-selection rule

021 is not committed to any method winning.

A finding is strongest when different logics converge:

- QCA/CNA: configuration;
- NCA: bottleneck necessity;
- event history: temporal ordering/risk;
- prediction: out-of-sample discrimination/calibration;
- process tracing: within-case mechanism.

Disagreement between methods is itself a result and must be explained rather than averaged away.
