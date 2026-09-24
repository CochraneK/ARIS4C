# SESSION LOG · ARIS4C022

## 2026-09-24
- Registered ARIS4C022.
- Verified current IAU planet-definition summary and NASA/JPL source surfaces.
- Added Margot (2015/2024) and Soter (2006) quantitative-dynamics references.
- Added QCA methodology / calibration guidance.
- Built research-plan, variable/calibration, source-registry, code-plan and continuity scaffolds.

## 2026-09-24 · Pilot-0 case-frame freeze
- Froze 50 cases: 8 planets, 5 dwarf planets, 21 satellites, 16 small/boundary bodies.
- Added large-moon, irregular-moon, candidate-dwarf, rubble-pile and distant-object contrasts.
- Froze raw-variable schema and separate heliocentric vs primary-centric orbit variables.
- Froze M0 definitional benchmark, M1 dynamical audit, M2 non-definitional physical-signature model, M3 satellite boundary analysis, and exploratory M4 geophysical similarity set.
- Limited primary QCA to roughly 4–6 condition families to avoid truth-table explosion.
- Added deterministic frame validator.
- No numerical QCA solutions were inspected before this freeze.

## 2026-09-24 · Physical-core ingestion v0.1
- Materialized `raw_physical_core_v0.1.csv` with all 50 frozen cases.
- Ingested authoritative JPL physical-core values for 34/50 cases.
- Preserved satellite GM, uncertainty and ephemeris reference; derived satellite mass from GM with CODATA-2018 G and labeled it as derived.
- Left all 16 small-body numeric cells explicitly un-ingested.
- Added JPL SBDB snapshotter, Margot/Soter implementations, and raw-matrix QA.
- No fsQCA calibration anchors or solutions were inspected.

## 2026-09-24 · Pilot-1 orbit + derived spine
- Verified JPL's current Planetary Satellite Mean Elements table and its explicit high-fidelity warning.
- Added `orbital_geometry_v0.1.csv` for all 50 frozen rows:
  - 21 selected satellites populated from JPL mean elements with frame, epoch and ephemeris provenance.
  - 13 direct-Sun planet/dwarf semimajor axes explicitly derived from JPL sidereal periods as a temporary Pilot-1 layer.
  - 16 small bodies remain explicit `NA_NOT_INGESTED`.
- Added `derived_physics_v0.1.csv`: 34 gravity, escape-speed, density-diagnostic and stellar-environment rows; Margot Pi for 13 direct-Sun bodies only.
- Added reproducible derivation and Pilot-1 validation scripts.
- Added `MISSINGNESS_AUDIT.md`; evidence-coded composition/atmosphere/geology variables remain gated.
- Firecrawl credits and the current control runtime could not retrieve the live 16-case SBDB JSON snapshot, so no substitute values were fabricated.
- No QCA calibration or solution inspection occurred.
