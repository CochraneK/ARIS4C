# Code · ARIS4C022

Current reproducible pipeline state:

1. `validate_case_frame.py` — frozen 50-body frame.
2. `validate_raw_physical.py` — physical-core coverage + no-fabrication rule.
3. `fetch_sbdb_small_bodies.py` — frozen raw-JSON snapshotter for 16 JPL SBDB small/boundary bodies.
4. `dynamics_metrics.py` — Margot (2015) Eq. 8/9/10 + Soter (2006) mu.
5. `test_dynamics_metrics.py` — published-value regression checks.
6. `derive_pilot1_physics.py` — v0.1 derived layer builder.
7. `validate_pilot1.py` — v0.1 orbit/derived validation.
8. `validate_source_hardening.py` — v0.2 validation: 8 JPL planet-element rows, 5 derived dwarf rows, 21 satellite rows, 16 pending small bodies, 34 derived rows, 13 Margot-Pi rows, and a fully unexposed evidence matrix.

Current canonical data products:

- `raw_physical_core_v0.1.csv`
- `orbital_geometry_v0.2.csv`
- `derived_physics_v0.2.csv`
- `evidence_state_v0.1.csv`
- `ORBIT_SOURCE_HARDENING_AUDIT.md`
- `MISSINGNESS_AUDIT.md`
- `process/EVIDENCE_STATE_PROTOCOL.md`

Still gated:

9. Execute live 16-case SBDB snapshot.
10. Replace five dwarf-planet derived heliocentric a values with live/pinned SBDB/Horizons elements.
11. Code geophysical evidence states under the frozen protocol.
12. Add Hill-radius / primary-mass derivatives after primary-GM provenance is pinned.
13. Freeze fuzzy-set calibration anchors.
14. Run QCA only after the above freeze.
15. Sensitivity + clustering/PCA companion analyses.

Preferred implementation: R package `QCA` for canonical set-theoretic analysis; Python for ingestion, QA, metric replication, and visualization.

No confirmatory QCA solution is to be inspected until raw/evidence provenance and calibration anchors are frozen.
