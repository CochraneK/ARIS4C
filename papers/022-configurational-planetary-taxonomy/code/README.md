# Code plan · ARIS4C022

Planned reproducible pipeline:

1. `build_case_frame` — frozen object list + class labels + source IDs.
2. `ingest_nasa_jpl` — raw physical/orbital fields with provenance.
3. `derive_physics` — density, gravity, escape speed, Hill radius, insolation, published dynamical metrics.
4. `calibrate_sets` — explicit crisp/fuzzy calibration manifest.
5. `run_qca` — necessity, truth tables, complex/intermediate/parsimonious solutions.
6. `sensitivity` — calibration perturbation, alternative condition representatives, leave-one-case-out.
7. `descriptive_geometry` — optional clustering/PCA companion, kept distinct from QCA inference.

Preferred implementation: R package `QCA` for canonical set-theoretic analysis; Python may be used for ingestion/QA/visualization.

No analysis code is considered confirmatory until the case frame and calibration anchors are frozen.
