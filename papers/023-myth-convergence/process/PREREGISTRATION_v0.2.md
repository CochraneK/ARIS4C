# PREREGISTRATION · v0.2 Analysis Contract

This is an internal preregistration-style freeze before expanded-result inspection. It is not claimed to be a time-stamped external registry.

## Primary observational unit

The primary inferential object is **tradition-time × motif-family source bundle**. Pairwise analyses operate on dyads of eligible bundles within the same motif family.

## Eligibility

A bundle enters primary similarity analysis only if:
- provenance is auditable;
- chronology is bounded;
- motif-family coding uses the frozen v0.2 ontology;
- at least 75% of family motifs are mutually scorable for a dyad;
- the positive union contains at least 2 motifs;
- neither member is a later-comparator-only bundle.

## Primary similarity

Presence-Jaccard.

Simple matching is diagnostic only.

Sensitivity metrics:
- Sørensen-Dice;
- overlap coefficient;
- simple matching;
- weighted Jaccard if evidence-quality weighting is preregistered before inspection.

## Primary mechanism predictors

Kept independent:
1. **ancestry** — categorical/topological relatedness globally; dated phylogenetic distance only inside families with defensible published trees;
2. **historical contact** — independently sourced edge/path measures, never inferred from motif similarity;
3. **temporal separation** — bundle midpoint / interval separation;
4. **geographic separation** — historical location estimates with uncertainty;
5. **environment** — palaeoenvironmental variables only when temporally defensible.

## Model gate

Inferential modeling is activated only when:
- >=15 eligible tradition-time units overall;
- >=50 analyzable dyads in at least one motif family;
- no single case contributes >20% of all analyzable dyads after exclusions.

If the gate fails, v0.2 remains a Methods + descriptive/process-tracing paper.

## Primary model family

Preferred:
- Bayesian dyadic/multi-membership model with random effects for both nodes;
- family-stratified or family interaction effects;
- uncertainty propagated where source dates / tree estimates permit.

Network/permutation robustness:
- MRQAP or equivalent matrix-permutation analysis.

Cross-family pseudo-distances are prohibited.

## Outcome formulation

Do not treat each motif as an independent Bernoulli trial without testing overdispersion/dependence.

Primary continuous outcome: Jaccard with an appropriate bounded model.
Sensitivity: shared-positive count conditional on positive union, using overdispersed count/binomial formulation if diagnostics support it.

## Multiple testing

Primary claims are C1–C4. Motif-level or family-level exploratory coefficients are explicitly secondary and corrected or hierarchically regularized.

## Stopping / interpretation

No post-hoc threshold converts a similarity coefficient into “borrowed.”
No model coefficient is called causal without a separately justified identification strategy.
