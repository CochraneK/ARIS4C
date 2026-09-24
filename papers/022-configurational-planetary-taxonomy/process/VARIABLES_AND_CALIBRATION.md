# Variables & Calibration · ARIS4C022

Updated: 2026-09-24

Calibration is **CLOSED_NOT_READY**. The primary M2 condition families are frozen, but no fuzzy-set anchor may be tuned or inspected until the pre-calibration readiness gates pass.

## Outcomes

| Outcome | Type | Role |
|---|---|---|
| PLANET | crisp benchmark | M0/M2 outcome |
| DWARF_PLANET | crisp benchmark | separate outcome analysis |
| SATELLITE | crisp | M3 outcome |
| DYN_DOM | fuzzy/quantitative | M1 only |
| ROUND | fuzzy/crisp sensitivity | M0/M4 only |

## Frozen M2 primary conditions

| Family | Primary representative | Current substantive coverage | Status |
|---|---|---:|---|
| SCALE | escape_velocity_m_s | 34/50 | incomplete |
| BULK_MATERIAL | density_from_mass_radius_g_cm3 | 34/50 | incomplete |
| ATMOSPHERE_RETENTION | atmosphere_value | 25/50 | incomplete |
| INTERNAL_ORGANIZATION | differentiation_value | 32/50 | incomplete |
| SOLAR_ENERGY | insolation_rel_earth | 34/50 | incomplete |

Complete on all five: **19/50**.

The composition ontology is not forced into an ordinal fuzzy scale. It remains available for mvQCA / class-contrast sensitivity.

## Readiness gates before calibration

All must pass:

1. every primary condition has >=40/50 substantive values;
2. complete-case set >=35/50;
3. all 8 major planets complete;
4. complete non-planets include at least:
   - 4/5 dwarf planets,
   - 12/21 satellites,
   - 10/16 small/boundary bodies;
5. remaining missingness has scientific provenance;
6. calibration anchors are theory/physics/evidence based and frozen before any solution inspection.

Current complete strata: 8 planets, 2 dwarf planets, 9 satellites, 0 small bodies. **FAIL.**

## Redundancy map

Do not enter tightly coupled variables simultaneously:
- mass + radius → density;
- mass + radius → surface gravity;
- mass + radius → escape velocity;
- stellar distance → insolation;
- mass + host + orbit → dynamical-dominance metrics.

Primary M2 selects one representative per family. Alternatives are sensitivity substitutions only.

## Calibration principles once the gate passes

- theory/natural-break/published thresholds preferred to sample quantiles;
- outcome labels cannot determine anchors;
- explicit full-out / crossover / full-in values;
- uncertainty and scientific missingness stay visible;
- threshold perturbation is mandatory.

## Frozen sensitivity families

- SCALE: mass or radius instead of escape velocity
- BULK_MATERIAL: composition classes via mvQCA instead of density
- ATMOSPHERE_RETENTION: comparable pressure where defensible
- INTERNAL_ORGANIZATION: geology, ocean, or tidal heating in separate sensitivity models
- SOLAR_ENERGY: distance or equilibrium-temperature proxy instead of insolation

## Anti-circularity state

- calibration anchors inspected/tuned: 0
- truth-table rows inspected: 0
- consistency/PRI/coverage inspected: 0
- QCA solutions inspected: 0
