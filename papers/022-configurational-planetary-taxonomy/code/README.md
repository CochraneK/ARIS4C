# Code · ARIS4C022

Implemented reproducible checks/builders:

1. `validate_case_frame.py`
2. `validate_raw_physical.py`
3. `fetch_sbdb_small_bodies.py`
4. `dynamics_metrics.py` + `test_dynamics_metrics.py`
5. `derive_pilot1_physics.py` + `validate_pilot1.py`
6. `validate_source_hardening.py`
7. evidence validators for batches 01–05
8. `validate_evidence_state_v06.py` — 50/50 composition evidence-state closure
9. `validate_m2_freeze.py` — validates the five-condition anti-circularity manifest and keeps calibration closed

Canonical analytical control files:

- `process/M2_CONDITION_FREEZE.md`
- `process/M2_CONDITION_FREEZE.json`
- `data/M2_READINESS_AUDIT.md`
- `process/VARIABLES_AND_CALIBRATION.md`

Current readiness is deliberately **FAIL**: 19/50 cases complete on all five M2 primary conditions.

Still gated:

- live 16-case SBDB numeric snapshot;
- five dwarf-planet live orbit replacements;
- targeted atmosphere/differentiation completion;
- readiness re-audit;
- calibration freeze;
- QCA / sensitivity / clustering only afterward.
