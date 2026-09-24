# Code · ARIS4C022

Reproducible control now includes:

1. case-frame / raw-physical / source-hardening validators
2. JPL SBDB fetch scaffold
3. Margot/Soter dynamics functions + regression tests
4. evidence-state validators through v1.0
5. `validate_m2_freeze.py`
6. readiness validators through v1.0
7. `derive_readiness_numeric_v03.py` — deterministic rebuild from raw physical v0.2 + orbit v0.3
8. `validate_m2_readiness_v10.py` — asserts every frozen readiness gate

Current frozen readiness:
- SCALE 44/50 PASS
- BULK_MATERIAL 44/50 PASS
- ATMOSPHERE_RETENTION 41/50 PASS
- INTERNAL_ORGANIZATION 40/50 PASS
- SOLAR_ENERGY 44/50 PASS
- complete 37/50 PASS
- small/boundary complete 10/16 PASS

Calibration is now **eligible to freeze**, but has not yet been opened. Truth tables and QCA outputs remain uninspected.
