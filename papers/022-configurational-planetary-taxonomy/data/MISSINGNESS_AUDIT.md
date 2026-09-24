# Pilot-1 missingness & provenance audit

Date: 2026-09-24

## Current coverage

| Layer | Complete / 50 | State |
|---|---:|---|
| Identity / official class | 50 | frozen |
| Raw physical core | 34 | authoritative JPL values |
| Orbit descriptor layer | 34 | 13 direct-Sun bodies + 21 satellites |
| Surface gravity / escape velocity / density diagnostic | 34 | deterministic derived |
| Stellar-distance / relative-insolation proxy | 34 | direct body or host-planet distance |
| Margot Pi | 13 | direct-Sun bodies only |
| Small-body physical + osculating orbit | 0 / 16 | pending JPL SBDB snapshot |
| Composition evidence state | 0 | not yet coded |
| Atmosphere evidence state | 0 | not yet coded |
| Internal/geologic activity evidence state | 0 | not yet coded |
| Soter mu | 0 | blocked on explicit orbital-zone mass census |

## Provenance distinctions now enforced

- **JPL source value**: copied from an identified JPL table.
- **Derived from JPL source value**: formula and dependencies are explicit.
- **Mean orbital element**: descriptive satellite orbit parameter; JPL explicitly warns that mean elements are not high-fidelity ephemerides.
- **Not ingested**: blank numeric cells plus a machine-readable state, never zero.
- **Not applicable**: e.g. Margot Pi is not assigned to satellites.

## Important caveat

The heliocentric semimajor axes for the 13 planet/dwarf rows in `orbital_geometry_v0.1.csv` are currently **derived from JPL sidereal periods via Kepler's third law**, not copied as catalog osculating elements. They are sufficient for a reproducible Pilot-1 physics layer and Margot smoke test, but the final raw-data freeze should replace/validate them with a pinned JPL/Horizons or SBDB orbital source.

## What is still structurally missing

The next scientific missingness problem is no longer just "some cells are blank." Composition, atmosphere, differentiation, ocean evidence and current geological activity are evidence-coded variables with heterogeneous observability. Their missingness must distinguish:

- directly measured / strongly constrained,
- model-inferred,
- evidence for absence,
- not measured,
- genuinely uncertain,
- source conflict,
- not applicable.

This evidence-state layer must be frozen before these variables can enter M2 fsQCA.
