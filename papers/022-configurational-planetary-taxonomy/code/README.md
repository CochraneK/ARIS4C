# Code · ARIS4C022

Implemented reproducible checks/builders:

1. `validate_case_frame.py`
2. `validate_raw_physical.py`
3. `fetch_sbdb_small_bodies.py`
4. `dynamics_metrics.py` + `test_dynamics_metrics.py`
5. `derive_pilot1_physics.py` + `validate_pilot1.py`
6. `validate_source_hardening.py`
7. evidence validators through v0.6
8. `validate_m2_freeze.py` — frozen five-condition anti-circularity manifest
9. `validate_m2_readiness_v02.py` — evidence v0.7 + current condition coverage + stratum readiness

Canonical analytical control:

- `process/M2_CONDITION_FREEZE.md/.json`
- `data/M2_READINESS_GAP_MAP_v0.2.csv`
- `data/M2_READINESS_AUDIT_v0.2.md`
- `process/VARIABLES_AND_CALIBRATION.md`

Current readiness:
- complete 25/50
- planets 8/8 PASS
- dwarfs 4/5 PASS
- satellites 13/21 PASS
- small/boundary 0/16 FAIL
- calibration CLOSED_NOT_READY

Still gated:
- live 16-case SBDB numeric snapshot;
- small-body atmosphere/internal-organization evidence as needed;
- >=35 complete cases and per-condition >=40;
- calibration freeze;
- QCA / sensitivity / clustering only afterward.
