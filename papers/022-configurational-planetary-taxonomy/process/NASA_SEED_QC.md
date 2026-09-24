# NASA seed QC · why “diameter” is not automatically “mean radius”

The first 10-body NASA NSSDC seed exposed an important harmonization issue before full ingestion.

The compact NASA fact sheet defines **Diameter** as equatorial diameter, while **Density** is whole-body average density. Its gravity field is equatorial and includes rotation; for gas giants it is reported at the 1-bar level. Therefore a naive spherical calculation from mass + displayed equatorial diameter should not be expected to reproduce every catalogued density/gravity value exactly.

A local diagnostic using the seed values showed:

| Body | Density difference from naive spherical derivation | Gravity difference |
|---|---:|---:|
| Mercury | -0.05% | +0.03% |
| Venus | +0.04% | -0.29% |
| Earth | -0.38% | -0.05% |
| Moon | -0.53% | +0.87% |
| Mars | -0.53% | +0.42% |
| Jupiter | -6.48% | +7.29% |
| Saturn | -9.83% | +15.97% |
| Uranus | -2.28% | +1.93% |
| Neptune | -2.11% | +0.92% |
| Pluto | +0.05% | -12.18% |

The large Jupiter/Saturn discrepancies are exactly the kind of warning this QC stage is meant to expose: **do not infer mean volume from equatorial diameter for substantially oblate bodies**. Pluto's gravity/escape discrepancies also show the effect of strongly rounded display values in the compact fact sheet.

## Frozen consequence

1. Catalogued density/gravity remain source values.
2. Any derived density uses a source that explicitly provides mean volumetric radius (or equivalent axes), not the compact equatorial diameter by default.
3. Derived gravity must state whether it is pure GM/R² or effective equatorial gravity including rotation.
4. Gas-giant “surface” fields require an explicit pressure-level convention.
5. The raw provenance layer must preserve source definitions, not just numbers.

Diagnostic script: code/qc_nasa_seed.py
