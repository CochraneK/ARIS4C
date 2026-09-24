# M2 readiness audit · pre-calibration

Date: 2026-09-24  
Condition freeze: `process/M2_CONDITION_FREEZE.md`

## Current coverage

| Primary condition | substantive values / 50 |
|---|---:|
| escape velocity / SCALE | 34 |
| density / BULK_MATERIAL | 34 |
| atmosphere value / ATMOSPHERE_RETENTION | 25 |
| differentiation value / INTERNAL_ORGANIZATION | 32 |
| relative insolation / SOLAR_ENERGY | 34 |
| complete on all five | **19** |

Complete-case strata:
- planets 8/8
- dwarf planets 2/5
- satellites 9/21
- small/boundary bodies 0/16

## Decision

**FAIL — not calibration-ready.**

This is an expected gate failure, not a negative scientific result.

### Main deficits

1. The 16 small/boundary bodies still lack the canonical JPL SBDB numeric snapshot, directly limiting SCALE, BULK_MATERIAL and SOLAR_ENERGY.
2. Atmosphere substantive evidence is only 25/50.
3. Differentiation substantive evidence is 32/50.
4. Current complete cases contain no small/boundary body, so running M2 now would structurally bias the comparison.

## Next evidence work is targeted

Do **not** fill all remaining evidence cells.

Priority order:
1. obtain SBDB physical/orbital values for the 16 small/boundary bodies;
2. add atmosphere evidence/upper limits where mission or occultation data provide real constraints;
3. add differentiation evidence only where interior modeling or measurements are defensible;
4. recompute readiness;
5. freeze calibration anchors only after the readiness gates pass.

No QCA outcome-fit statistic is needed to decide any of these steps.
