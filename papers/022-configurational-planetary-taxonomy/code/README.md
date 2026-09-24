# Code · ARIS4C022

Implemented reproducible checks/builders:

1. `validate_case_frame.py`
2. `validate_raw_physical.py`
3. `fetch_sbdb_small_bodies.py`
4. `dynamics_metrics.py` + `test_dynamics_metrics.py`
5. `derive_pilot1_physics.py` + `validate_pilot1.py`
6. `validate_source_hardening.py`
7. `validate_evidence_state.py` — batch 01
8. `validate_evidence_state_v03.py` — batch 02 / 82-cell coverage / ocean-temporal firewall

Canonical data products:

- `raw_physical_core_v0.1.csv`
- `orbital_geometry_v0.2.csv`
- `derived_physics_v0.2.csv`
- `evidence_state_v0.3.csv`
- `EVIDENCE_CODING_AUDIT.md`
- `EVIDENCE_CODING_AUDIT_BATCH02.md`
- `ORBIT_SOURCE_HARDENING_AUDIT.md`
- `process/EVIDENCE_STATE_PROTOCOL.md`

Still gated:

- live 16-case SBDB snapshot;
- five dwarf-planet live orbit replacements;
- remaining evidence coding + conflict adjudication;
- calibration freeze;
- QCA / sensitivity / clustering only afterward.
