# Code · ARIS4C022

Current reproducible pipeline state:

1. `validate_case_frame.py` — validates the frozen 50-body frame and class counts.
2. `validate_raw_physical.py` — validates physical-core coverage and prevents fabricated numeric values in pending rows.
3. `fetch_sbdb_small_bodies.py` — snapshots raw JPL SBDB JSON for the 16 small/boundary cases, then flattens selected physical/orbital fields.
4. `dynamics_metrics.py` — implements published Margot (2015) Eq. 8/9/10 and Soter (2006) mu.
5. `test_dynamics_metrics.py` — regression checks against Margot's published Earth and Mars discriminants plus Soter's mass-ratio definition.

Still to implement:

6. `ingest_orbits` — authoritative heliocentric vs primary-centric orbital geometry with explicit frame/epoch.
7. `derive_physics` — gravity, escape speed, Hill radius, insolation and normalized units.
8. `calibrate_sets` — explicit crisp/fuzzy calibration manifest frozen before solution inspection.
9. `run_qca` — necessity, truth tables, complex/intermediate/parsimonious solutions.
10. `sensitivity` — calibration perturbation, alternative condition representatives, leave-one-case-out.
11. `descriptive_geometry` — optional clustering/PCA companion kept distinct from QCA inference.

Preferred implementation: R package `QCA` for canonical set-theoretic analysis; Python for ingestion, QA, published metric replication, and visualization.

No confirmatory QCA solution is to be inspected until the raw matrix, missingness audit, and calibration anchors are frozen.
