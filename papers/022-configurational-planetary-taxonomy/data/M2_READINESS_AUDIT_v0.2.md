# M2 readiness gap map · v0.2

Date: 2026-09-24

This audit is computed **without opening calibration or QCA results**.

## After readiness-targeted evidence batch 06

Primary substantive coverage:
- SCALE: 34/50
- BULK_MATERIAL: 34/50
- ATMOSPHERE_RETENTION: 28/50
- INTERNAL_ORGANIZATION: 36/50
- SOLAR_ENERGY: 34/50
- complete on all five: **25/50**

Complete strata:
- planets 8/8
- dwarf planets 4/5
- satellites 13/21
- small/boundary 0/16

## Gate interpretation

- Planet gate: PASS.
- Dwarf gate (>=4): **PASS** after Haumea/Eris internal-structure updates and Haumea occultation atmosphere constraint.
- Satellite gate (>=12): **PASS** after Mimas/Enceladus atmosphere and Tethys/Charon internal-structure updates.
- Small-body gate (>=10): **FAIL**, currently 0 because the 16 cases still lack canonical numeric SCALE/BULK_MATERIAL/SOLAR_ENERGY.
- Complete-case gate (>=35): **FAIL**, currently 25.
- Per-condition >=40 gate: atmosphere 28/40 and internal organization 36/40 still fail; three numeric conditions remain 34/40.

## Highest-value next work

1. **SBDB numeric snapshot is dominant**: adding mass/radius/orbit for the 16 small/boundary cases can simultaneously unlock SCALE, BULK_MATERIAL and SOLAR_ENERGY.
2. **Small-body atmosphere evidence** is the next cross-cutting bottleneck: after numerics arrive, at least 10 small bodies must also have atmosphere + differentiation values to satisfy the small-body complete-stratum gate.
3. INTERNAL_ORGANIZATION now needs only 4 additional substantive cases to meet the per-condition gate.
4. ATMOSPHERE_RETENTION needs 12 additional substantive cases.

No condition is deleted or replaced in response to this gap pattern.
