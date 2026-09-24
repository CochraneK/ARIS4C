# Model Ladder · ARIS4C022

Updated: 2026-09-24

The central design risk is circularity: entering the official definition and then claiming QCA rediscovered it. Models therefore remain separated.

## M0 · Definitional benchmark

Outcome: PLANET.

Conditions:
- DIRECT_SUN_ORBIT
- ROUND
- DYN_DOM

Expected benchmark: `DIRECT_SUN_ORBIT * ROUND * DYN_DOM -> PLANET`.

This is an implementation sanity check, not discovery and not a causal model.

## M1 · Quantitative dynamical audit

Run Margot-family and Soter-family discriminants in separate specifications. Do not count algebraically related dominance metrics as independent conditions.

## M2 · Anti-circularity physical-signature model

Outcome: current official PLANET label, used **only as the outcome**.

Primary five condition families are now frozen in `M2_CONDITION_FREEZE.md/.json`:

1. **SCALE** → escape velocity
2. **BULK_MATERIAL** → density as a quantitative material proxy, not literal composition
3. **ATMOSPHERE_RETENTION** → staged evidence-coded atmosphere state
4. **INTERNAL_ORGANIZATION** → differentiation evidence
5. **SOLAR_ENERGY** → relative insolation

Pilot-0's provisional INTERNAL_ACTIVITY family was moved to sensitivity before any result inspection because geology does not have stable measurement semantics across gas giants and solid bodies.

Explicitly excluded from M2 conditions:
- direct-Sun-orbit / satellite status / primary body
- official classification recodings
- cleared-neighborhood labels
- Margot Pi / Soter mu
- ROUND / hydrostatic-equilibrium labels
- boundary tags
- any outcome-derived variable

Current readiness audit: **FAIL**. Only 19/50 cases are complete on all five conditions; calibration remains closed.

## M3 · Satellite boundary analysis

Outcome: SATELLITE. Orbital hierarchy is the benchmark; planet-like satellites are described separately. Key cases include Ganymede, Titan, Charon and Triton.

## M4 · Geophysical similarity set

Exploratory only, never an official class. Candidate dimensions include internal organization, atmosphere retention, current activity, ocean evidence and tidal heating. Never call this “true planetness”.

## Why compact QCA matters

With 50 cases:
- 4 binary conditions → 16 possible rows
- 5 → 32
- 6 → 64
- 10 → 1024

Primary M2 therefore remains exactly five condition families. Alternatives are one-family-at-a-time sensitivity substitutions.

## Companion analyses

- unsupervised clustering
- PCA / low-dimensional geometry
- cross-validated decision tree as a predictive sanity check

## Reporting gate

Before necessary/sufficient language appears in an abstract, report calibration anchors, frequency threshold, consistency, PRI, complex/intermediate/parsimonious solutions, raw/unique coverage, contradictions, deviant cases, calibration perturbation and leave-one-case-out sensitivity.
