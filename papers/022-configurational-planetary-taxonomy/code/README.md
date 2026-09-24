# Code · ARIS4C022

Current reproducible pipeline state:

1. `validate_case_frame.py` — validates the frozen 50-body frame and class counts.
2. `validate_raw_physical.py` — validates physical-core coverage and prevents fabricated numeric values in pending rows.
3. `fetch_sbdb_small_bodies.py` — snapshots raw JPL SBDB JSON for the 16 small/boundary cases, then flattens selected physical/orbital fields.
4. `dynamics_metrics.py` — implements published Margot (2015) Eq. 8/9/10 and Soter (2006) mu.
5. `test_dynamics_metrics.py` — regression checks against Margot's published Earth and Mars discriminants plus Soter's mass-ratio definition.
6. `derive_pilot1_physics.py` — rebuilds the Pilot-1 gravity / escape-speed / spherical-density diagnostic / stellar-distance / insolation / Margot-Pi layer from frozen raw tables.
7. `validate_pilot1.py` — validates 50-row orbit/derived layers, exact 13+21+16 orbit-state counts, 34 derived rows, 13 Margot-Pi rows, and the no-fabrication rule for pending small bodies.

Current data products:

- `raw_physical_core_v0.1.csv`
- `orbital_geometry_v0.1.csv`
- `derived_physics_v0.1.csv`
- `MISSINGNESS_AUDIT.md`

Still to implement:

8. Replace/validate the 13 Kepler-derived heliocentric semimajor axes with pinned catalog/Horizons/SBDB orbit elements.
9. Execute the frozen 16-case SBDB snapshot.
10. Add Hill-radius / primary-mass derivatives after the primary-GM provenance layer is pinned.
11. Build evidence-state coding for composition, atmosphere, differentiation, ocean and current activity.
12. `calibrate_sets` — explicit crisp/fuzzy calibration manifest frozen before solution inspection.
13. `run_qca` — necessity, truth tables, complex/intermediate/parsimonious solutions.
14. `sensitivity` — calibration perturbation, alternative condition representatives, leave-one-case-out.
15. `descriptive_geometry` — optional clustering/PCA companion kept distinct from QCA inference.

Preferred implementation: R package `QCA` for canonical set-theoretic analysis; Python for ingestion, QA, published metric replication, and visualization.

No confirmatory QCA solution is to be inspected until the raw matrix, evidence-state missingness audit, and calibration anchors are frozen.
