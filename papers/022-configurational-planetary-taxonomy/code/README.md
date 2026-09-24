# Code · ARIS4C022

Implemented reproducible checks/builders:

1. `validate_case_frame.py` — frozen 50-body frame.
2. `validate_raw_physical.py` — physical-core coverage + no-fabrication rule.
3. `fetch_sbdb_small_bodies.py` — frozen JPL SBDB raw-JSON snapshotter.
4. `dynamics_metrics.py` + `test_dynamics_metrics.py` — Margot/Soter equations and regression checks.
5. `derive_pilot1_physics.py` + `validate_pilot1.py` — Pilot-1 derived layer.
6. `validate_source_hardening.py` — orbit-source hardening checks.
7. `validate_evidence_state.py` — evidence vocabulary, source-key, 10-anchor coverage and QCA-firewall checks.

Canonical data products:

- `raw_physical_core_v0.1.csv`
- `orbital_geometry_v0.2.csv`
- `derived_physics_v0.2.csv`
- `evidence_state_v0.2.csv`
- `EVIDENCE_CODING_AUDIT.md`
- `ORBIT_SOURCE_HARDENING_AUDIT.md`
- `process/EVIDENCE_STATE_PROTOCOL.md`

Still gated:

- live 16-case SBDB snapshot;
- five dwarf-planet live orbit replacements;
- remaining evidence coding + source-conflict adjudication;
- fsQCA calibration freeze;
- QCA, sensitivity, clustering/PCA only after those freezes.
