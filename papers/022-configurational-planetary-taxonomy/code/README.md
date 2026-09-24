# Code · ARIS4C022

Reproducible control now includes:

1. case-frame / raw-physical / source-hardening validators
2. JPL SBDB fetch scaffold
3. Margot/Soter dynamics functions + regression tests
4. evidence-state validators through v0.8
5. `validate_m2_freeze.py`
6. `validate_m2_readiness_v02.py`
7. `validate_m2_readiness_v03.py` — Batch 07 and INTERNAL_ORGANIZATION gate pass

Current readiness:
- 34 / 34 / 31 / **40** / 34 substantive primary-condition coverage
- complete 25/50
- planet/dwarf/satellite strata PASS
- small/boundary 0/16 FAIL
- calibration CLOSED_NOT_READY

Next code/data gate is the 16-case JPL SBDB numeric snapshot plus targeted small-body atmosphere evidence.
