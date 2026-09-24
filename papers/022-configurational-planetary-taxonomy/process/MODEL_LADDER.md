# Model Ladder · ARIS4C022

Pilot-0 · 2026-09-24

The main design risk is circularity: entering the exact IAU definition and then claiming QCA discovered the IAU classes. The following models are frozen separately.

## M0 · Definitional benchmark

Outcome: PLANET.

Conditions:
- DIRECT_SUN_ORBIT
- ROUND
- DYN_DOM

Expected benchmark relation: DIRECT_SUN_ORBIT * ROUND * DYN_DOM -> PLANET.

This is an implementation sanity check, not discovery and not a causal model.

## M1 · Quantitative dynamical audit

Run Margot-family and Soter-family discriminants in separate specifications. Do not count algebraically related dominance metrics as independent conditions.

## M2 · Anti-circularity physical-signature model

Ask whether non-definitional physical traits alone reproduce official taxonomy. Keep at most about five core condition families in the primary Pilot-0 specification:

1. SCALE
2. COMPOSITION
3. ATMOSPHERE_RETENTION
4. INTERNAL_ACTIVITY
5. SOLAR_ENERGY

Exclude direct-Sun-orbit status, official cleared-neighborhood labels, and any direct recoding of PLANET. A weak M2 result is informative because it shows intuitive geophysical similarity does not substitute for orbital taxonomy.

## M3 · Satellite boundary analysis

Outcome: SATELLITE. Use orbital hierarchy as the benchmark and separately describe planet-like satellites. Key cases include Ganymede, Titan, Charon, and Triton.

## M4 · Geophysical similarity set

Exploratory only and not an official class. Candidate dimensions are roundness/self-gravity, differentiation, atmosphere retention, internal activity, and volatile/ocean evidence. Never call this “true planetness”.

## Why compact QCA matters

With 50 cases:
- 4 binary conditions create 16 possible rows
- 5 create 32
- 6 create 64
- 10 create 1024

Primary QCA therefore stays around 4–6 core conditions. Larger ontologies are handled through condition-family substitution and sensitivity analyses.

## Companion analyses

- unsupervised clustering
- PCA / low-dimensional geometry
- cross-validated decision tree as a predictive sanity check

## Reporting gate

Report calibration anchors, frequency threshold, consistency, PRI, complex/intermediate/parsimonious solutions, raw and unique coverage, contradictions, deviant cases, calibration perturbation, and leave-one-case-out sensitivity before using necessary/sufficient language in the abstract.
