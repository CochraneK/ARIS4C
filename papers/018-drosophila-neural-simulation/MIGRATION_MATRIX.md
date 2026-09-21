# ARIS4C018 · Legacy → Current Migration Matrix

Snapshot: 2026-09-21

| Layer | Legacy reproduced | Current migrated | Gate |
|---|---|---|---|
| body / physics | FlyGym 1.3.2 | FlyGym 2.x | PASS |
| eye rendering | legacy vision API | `Simulation.get_ommatidia_readouts()` | PASS |
| retinal order | legacy RetinaMapper | `FlyGym2RetinaMapper` | PASS |
| visual neural model | flyvis 1.1.2 | current pinned flyvis | PASS |
| neural shape | 2 × 45,669 | 2 × 45,669 | PASS |
| stepwise neural interface | legacy `RealTimeVisionNetwork` | ARIS `StepwiseFlyvisNetwork` adapter | PASS |
| decoder math | legacy inline implementation | frozen `official_legacy_decoder.py` | PASS + unit CI |
| target detection | moving fly | static migration sphere | PASS within own condition |
| descending signal | 2-value engineered drive | same frozen equations | PASS |
| locomotor controller | legacy hybrid turning | current `HybridTurningController` | PASS |
| body motion under neural-derived drive | yes | yes | PASS |
| synchronized trace | Pilot 2C | Pilot 3C | RUNNING |
| shared replay UI | legacy trace | current trace | UI ready; waits for current trace |
| matched cross-version experiment | not applicable | not yet built | NOT STARTED |

## Important non-equivalences

Current migration success does **not** mean legacy and current outputs are numerically equivalent.

Known non-matched factors include:

- FlyGym version;
- MuJoCo / rendering implementation;
- target type;
- experiment duration;
- flyvis version;
- baseline duration;
- body/controller implementation details.

## Migration closure rule

Migration engineering closes only when:

1. Pilot 3C current synchronized trace PASS;
2. semantic parity CI PASS;
3. one replay implementation loads both trace provenances;
4. current trace provenance and condition difference are explicit.

Matched numerical comparison belongs to a separate cross-version regression stage.
