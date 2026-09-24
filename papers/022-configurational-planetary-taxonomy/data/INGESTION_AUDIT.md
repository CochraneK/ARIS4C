# Ingestion audit · physical core v0.1

Date: 2026-09-24

This audit is deliberately conservative: a cell is populated only when the current source route is explicit and auditable.

## Coverage

- Frozen case frame: **50/50 rows materialized**
- Core physical fields ingested: **34/50 cases**
  - 8 planets
  - 5 IAU dwarf planets
  - 21 selected satellites
- Pending JPL SBDB ingestion: **16/50 small/boundary bodies**
- Mean radius + density: **34/50**
- Mass: **13 direct table values + 21 values derived from JPL GM**
- Rotation period + heliocentric orbital period + geometric albedo: **13/50** (planet/dwarf table only)
- Satellite GM + GM uncertainty + ephemeris reference: **21/21 selected satellites**
- Heliocentric semimajor axis / satellite-primary semimajor axis: **not yet ingested in this tranche**

## Source routes

- `JPL_PLANET_PHYS`: JPL Solar System Dynamics, Planetary Physical Parameters.
- `JPL_SAT_PHYS`: JPL Solar System Dynamics, Planetary Satellite Physical Parameters.
- `JPL_SBDB_API_PLANNED`: JPL Small-Body Database API; values remain blank until the machine-readable response is captured.

## Transformations already permitted

1. Planet/dwarf rotation: days → hours using exactly 24 h/day.
2. Planet/dwarf orbital period: years → days using 365.25 d/year.
3. Satellite mass: `M = GM / G`, with `G = 6.67430e-20 km^3 kg^-1 s^-2` (CODATA 2018).

These transformations are deterministic and are labeled in `mass_value_type` / notes. They are not silently treated as direct observations.

## Missingness discipline

The 16 small bodies are currently `NA_NOT_INGESTED`, not zero and not "unknown forever". Subsequent extraction should distinguish:

- `NA_NOT_MEASURED`
- `NA_UNCERTAIN`
- `NA_SOURCE_CONFLICT`
- `NA_NOT_APPLICABLE`

## Next ingestion gate

1. Run the SBDB snapshot script for the 16 small/boundary bodies.
2. Add orbital geometry from JPL/Horizons or another pinned JPL machine-readable route.
3. Recompute field-level coverage and conflicts.
4. Only after that, freeze fsQCA calibration anchors.
