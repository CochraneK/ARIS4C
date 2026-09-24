# ARIS4C021 · Research Plan v0.1

## Working question

Which structural, elite-level, conflict, target-vulnerability and international conditions — alone or in combinations — are necessary or sufficient for the onset of genocide/politicide or intrastate mass killing?

The terms “necessary” and “sufficient” are method-specific formal claims, not deterministic universal laws. QCA/CNA, NCA, event-history models and process tracing answer different parts of the causal question and are not interchangeable.

## Claim hierarchy

### C1 · Replication
Can the classic Harff structural-risk findings and the Williams QCA configurations be reproduced under an auditable coding pipeline?

### C2 · Temporal extension
Do the same configurations remain sufficient/necessary when newer cases and newer covariates are added without changing the original outcome definition?

### C3 · Outcome robustness
Do configurations survive when the outcome changes from genocide/politicide to a separately defined intrastate mass-killing onset?

### C4 · Causal asymmetry / resilience
Are configurations associated with the absence of mass atrocity simply the negation of atrocity configurations, or do protective pathways differ?

### C5 · Stability
Which candidate conditions retain necessity/sufficiency status across calibration thresholds, case-universe choices, outcome definitions, leave-one-region-out, and leave-one-case-out analyses?

## Design hierarchy

### Stage A · Exact historical replication

Replicate Harff's case universe and condition definitions as closely as source availability allows.

Core historical candidates:
- prior genocide/politicide;
- magnitude of political upheaval;
- exclusionary ideology of the ruling elite;
- autocracy;
- ethnic-minority / salient ethnic character of the ruling elite;
- low trade openness / international isolation.

The goal is not to improve the model in this stage. Any mismatch is documented before extension.

### Stage B · Williams QCA replication

Reconstruct the 139-case genocide/non-genocide QCA frame and test the published sufficient configuration:

AUTocracy AND ELITE-ETHNIC-SALIENCE AND (EXCLUSIONARY-IDEOLOGY OR POLITICAL-UPHEAVAL)

This is a replication target, not an assumed truth.

### Stage C · Modern extension

Build a theory-constrained extension using modern public sources. Candidate families:

1. Political opportunity / regime — autocracy, abrupt regime transition, armed conflict.
2. Elite motive / ideology — exclusionary ideology, elite ethnic salience, institutionalized political exclusion.
3. Target vulnerability — organized discrimination, prior targeted violence, political exclusion.
4. Coercion / impunity — repression, impunity, coercive capacity without accountability.
5. International constraint — trade openness, international integration, external monitoring.
6. Historical path dependence — prior genocide/politicide, prior mass atrocity, unresolved recurrent conflict.

Do not put every available variable into one truth table. QCA condition count is frozen by theory and sample size before outcome inspection.

### Stage D · Cross-method triangulation

On the same frozen historical and modern frames:

- QCA tests set-theoretic configurations and causal asymmetry;
- CNA searches redundancy-free minimally sufficient/necessary configurational structures;
- NCA tests bottleneck-style necessity, especially for continuous modern indicators;
- event-history models test timing, duration dependence and lagged onset risk;
- rare-events / penalized regression provides a conventional inferential benchmark;
- machine-learning models provide out-of-sample prediction benchmarks;
- process tracing and comparative process tracing test mechanisms and condition sequence in selected typical/deviant cases.

No method is treated as the adjudicator of all others. Disagreement is analyzed explicitly.

### Stage E · Predictive benchmark

Compare set-theoretic configurations with a conventional predictive baseline using lagged country-year covariates.

The predictive model answers “who is at elevated risk?”; QCA answers “which configurations are set-theoretically sufficient/necessary in this sample?” They are complementary and must not be conflated.

## Case universes

### U1 · Historical replication universe
Political-instability/state-failure episodes used by Harff/Williams.

### U2 · Global country-year onset universe
Country-years with no ongoing onset at baseline, using a separately frozen mass-killing definition.

### U3 · Matched high-risk negative cases
Retain severe crises that did not escalate. Easy peaceful controls alone would trivialize the comparison.

## Temporal firewall

All explanatory conditions must be measured before the defined onset.

- default lag: t-1 for annual covariates;
- no post-onset values in calibration;
- retrospectively coded predictors that may depend on knowing the outcome are flagged or excluded;
- outcome and condition coding are versioned separately.

## Configurational workflow

1. descriptive missingness and case-universe audit;
2. calibration freeze;
3. necessity analysis before sufficiency analysis;
4. truth table construction;
5. contradictory-row audit;
6. conservative / intermediate / parsimonious solutions;
7. solution consistency and coverage;
8. PRI / contradiction diagnostics where applicable;
9. leave-one-case-out and leave-one-region-out stability;
10. threshold sensitivity;
11. explicit analysis of outcome absence;
12. deviant-case qualitative review.

### Initial thresholds to preregister

These are starting rules, not results:

- necessity consistency target: >= 0.90;
- sufficiency consistency target: >= 0.80;
- PRI floor for headline sufficient paths: >= 0.65;
- frequency cutoff selected from the frozen N before outcome inspection;
- no “necessary condition” headline if empirical relevance/coverage is trivial.

Threshold grids around these values will be shown rather than using one arbitrary cutpoint.

## Periodic-table-like condition atlas

The final atlas groups conditions by causal role:

| Family | Role |
|---|---|
| O · Opportunity | regime and institutional opportunity structure |
| M · Motive | exclusionary elite ideology and political projects |
| T · Trigger | political upheaval, war escalation, coups, acute crises |
| V · Vulnerability | target exclusion, discrimination, prior victimization |
| C · Coercion | coercive capacity, repression, impunity |
| X · External constraint | trade/international integration and external restraint |
| H · History | prior genocide/politicide and recurrence |

Each cell may eventually receive one of:
- N = robust necessary condition;
- S = component of robust sufficient configuration;
- INUS = insufficient alone but necessary within a sufficient pathway;
- P = protective / non-onset pathway component;
- U = unstable / calibration-sensitive;
- 0 = no reproducible set-theoretic role.

No symbol is assigned before frozen analyses.

## Falsifiers

The central framing is weakened if:
- historical results cannot be reproduced under defensible coding;
- no necessary condition survives threshold sensitivity;
- sufficient configurations have low coverage or collapse under one-case deletion;
- configurations fail across reasonable outcome definitions;
- contradictory rows dominate the truth table;
- negative-outcome pathways are artifacts of calibration.

A null result remains publishable if strong necessary/sufficient claims fail under modern replication.

## Ethics and communication

This is a mass-atrocity prevention and explanation project.

- avoid operational descriptions that would facilitate perpetration;
- do not produce a “recipe” detached from uncertainty and prevention context;
- do not rank living groups as inherently violent;
- avoid essentializing ethnicity, religion or nationality;
- distinguish structural risk from intent;
- frame current-country applications as probabilistic risk assessment requiring expert review, not accusation or prediction of guilt.

## First bounded unit

1. acquire and hash PITF State Failure / GenoPoliticide 2018 materials;
2. reconstruct Harff/Williams case IDs and condition matrix;
3. document coding mismatches;
4. freeze CASE_UNIVERSE_V1.csv;
5. freeze CONDITION_CALIBRATION_V1.md;
6. run the historical replication suite: Harff-style baseline + QCA + CNA, with NCA only where measurement permits;
7. lock the replication comparison before adding V-Dem/EWP modern extensions.
