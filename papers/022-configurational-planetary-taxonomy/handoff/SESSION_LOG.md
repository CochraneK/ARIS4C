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
- Re-checked latest main before writing because ARIS4C papers are advancing concurrently.
- Materialized `raw_physical_core_v0.1.csv` with all 50 frozen cases.
- Ingested authoritative JPL physical-core values for 34/50 cases:
  - 8 planets + 5 dwarf planets from JPL Planetary Physical Parameters.
  - 21 satellites from JPL Planetary Satellite Physical Parameters.
- Preserved satellite GM, uncertainty and ephemeris reference; derived satellite mass from GM with CODATA-2018 G and labeled the result as derived.
- Left all 16 small-body numeric cells explicitly un-ingested instead of guessing values.
- Added a standard-library JPL SBDB snapshotter for those 16 small bodies.
- Implemented Margot (2015) Eq. 8/9/10 and Soter (2006) mu directly from the source papers.
- Added Earth/Mars regression checks against Margot's published discriminants and deterministic raw-matrix QA.
- No fsQCA calibration anchors or numerical QCA solutions were inspected.
