# Code · ARIS4C022

Implemented reproducible checks/builders:

1. `validate_case_frame.py`
2. `validate_raw_physical.py`
3. `fetch_sbdb_small_bodies.py`
4. `dynamics_metrics.py` + `test_dynamics_metrics.py`
5. `derive_pilot1_physics.py` + `validate_pilot1.py`
6. `validate_source_hardening.py`
7. evidence validators for batches 01–04
8. `validate_evidence_state_v06.py` — Batch 05 / 50-of-50 composition-state closure / 188-cell coverage

Canonical data products:

- `raw_physical_core_v0.1.csv`
- `orbital_geometry_v0.2.csv`
- `derived_physics_v0.2.csv`
- `evidence_state_v0.6.csv`
- `SOURCE_REGISTRY.md`
- `SOURCE_CONFLICT_AUDIT.md`
- `EVIDENCE_CODING_AUDIT_BATCH05.md`
- `process/EVIDENCE_STATE_PROTOCOL.md`

Still gated:

- live 16-case SBDB numeric snapshot;
- five dwarf-planet live orbit replacements;
- primary M2 condition-family freeze;
- only targeted evidence completion needed by those conditions;
- calibration freeze;
- QCA / sensitivity / clustering only afterward.
