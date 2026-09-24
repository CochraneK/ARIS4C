# Numeric acquisition audit · priority-ten readiness anchors

Date: 2026-09-24

## Result

The predeclared priority-ten small/boundary cases now have provenance-complete physical and orbital inputs sufficient for deterministic M2 SCALE / BULK_MATERIAL / SOLAR_ENERGY derivation:

Vesta, Pallas, Hygiea, Interamnia, Eros, Bennu, Ryugu, Itokawa, Quaoar, Orcus.

## Source-tier summary

| Body | Physical path | Orbit path | Primary-mass handling |
|---|---|---|---|
| Vesta | Dawn mission direct | NASA PDS | direct |
| Pallas | peer-reviewed AO + perturbation mass | JPL static element table | solar-mass unit conversion |
| Hygiea | peer-reviewed resolved imaging + density | peer-reviewed orbit table | derived rho × volume |
| Interamnia | peer-reviewed resolved imaging + density | peer-reviewed orbit | derived rho × volume |
| Eros | NEAR / NASA PDS | NASA PDS | direct |
| Bennu | OSIRIS-REx / NASA PDS | NASA PDS | direct |
| Ryugu | Hayabusa2 / NASA PDS | NASA PDS | direct |
| Itokawa | Hayabusa / NASA PDS + Science | NASA PDS | direct |
| Quaoar | 2026 occultation + binary mass-ratio literature | peer-reviewed orbit | system mass explicitly corrected for Weywot |
| Orcus | binary dynamics + ALMA mass ratio + thermal size | peer-reviewed orbit | system mass explicitly corrected for Vanth |

## Derived-radius rules

- Pallas: volume-equivalent radius from triaxial radii.
- Hygiea / Interamnia: published volume-equivalent radius/diameter.
- Eros: equivalent radius derived from direct mass + bulk density because bounding dimensions are not treated as a true ellipsoid.
- Bennu / Ryugu / Itokawa: volume-equivalent radius from mission volume.
- Quaoar / Orcus: published equivalent/thermal diameter halved.

## Frozen-gate effect

Without changing any readiness threshold or M2 condition:
- SCALE 34 → **44/50**
- BULK_MATERIAL 34 → **44/50**
- ATMOSPHERE_RETENTION 40 → **41/50**
- INTERNAL_ORGANIZATION remains **40/50**
- SOLAR_ENERGY 34 → **44/50**
- complete cases 27 → **37/50**
- small/boundary complete 0 → **10/16**

All pre-frozen readiness gates PASS.

The remaining six small/boundary numeric rows are intentionally left missing; they are not needed to open calibration and will remain a later robustness/completeness task.
