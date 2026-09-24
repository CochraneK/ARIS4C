# Code · ARIS4C022

Reproducible control includes:

1. case-frame / raw-physical / source-hardening validators
2. JPL SBDB fetch scaffold
3. Margot/Soter dynamics functions + regression tests
4. evidence-state validators through v0.9
5. `validate_m2_freeze.py`
6. readiness validators v0.2–v0.4

Current readiness:
- SCALE 34/50
- BULK_MATERIAL 34/50
- ATMOSPHERE_RETENTION 40/50 PASS
- INTERNAL_ORGANIZATION 40/50 PASS
- SOLAR_ENERGY 34/50
- complete 27/50
- small/boundary complete 0/16
- calibration CLOSED_NOT_READY

The remaining code/data gate is now singular: obtain and validate the 16-case JPL SBDB numeric snapshot, then rebuild derived physics and readiness.
