# Source Registry · ARIS4C022

Retrieval baseline: 2026-09-24.

## Classification / definitions

1. International Astronomical Union — List of Resolutions; 2006 Resolutions B5 and B6, “Definition of a Planet in the Solar System” / “Pluto”.
   - https://iau.org/Iau/Publications/List-of-Resolutions

## Planet / dwarf-planet physical and orbital data

2. JPL Solar System Dynamics — Planetary Physical Parameters.
   - https://ssd.jpl.nasa.gov/planets/phys_par.html
3. JPL Solar System Dynamics — Approximate Positions of the Planets.
   - https://ssd.jpl.nasa.gov/planets/approx_pos.html
   - Used in `orbital_geometry_v0.2.csv`; Earth remains an explicit Earth-Moon-barycenter proxy.
4. NASA NSSDC Planetary Fact Sheet and notes.
   - https://nssdc.gsfc.nasa.gov/planetary/factsheet/
   - https://nssdc.gsfc.nasa.gov/planetary/factsheet/fact_notes.html

## Satellite physical + orbital data

5. JPL Solar System Dynamics — Planetary Satellite Physical Parameters.
   - https://ssd.jpl.nasa.gov/sats/phys_par/
6. JPL Solar System Dynamics — Planetary Satellite Mean Elements.
   - https://ssd.jpl.nasa.gov/sats/elem/
7. JPL Solar System Dynamics — Astrodynamic Parameters.
   - https://ssd.jpl.nasa.gov/astro_par.html

## Small-body route

8. JPL Small-Body Database API.
   - https://ssd-api.jpl.nasa.gov/doc/sbdb.html
   - https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html
   - Canonical live route for the 16 frozen small/boundary cases; current control-thread network still cannot retrieve object payloads.
9. JPL Solar System Dynamics — Small-Body Element Tables.
   - https://ssd.jpl.nasa.gov/sb/elem_tables.html
10. JPL Solar System Dynamics — Small-Body Orbits & Ephemerides.
    - https://ssd.jpl.nasa.gov/sb/orbits.html

## Evidence-state coding · Anchor batch 01

Agency facts pages used for the first blinded coding batch in `evidence_state_v0.2.csv`:

- `NASA_MERCURY_FACTS` — https://science.nasa.gov/mercury/facts/
- `NASA_VENUS_FACTS` — https://science.nasa.gov/venus/venus-facts/
- `NASA_EARTH_FACTS` — https://science.nasa.gov/earth/facts/
- `NASA_MARS_FACTS` — https://science.nasa.gov/mars/facts/
- `NASA_JUPITER_FACTS` — https://science.nasa.gov/jupiter/jupiter-facts/
- `NASA_SATURN_FACTS` — https://science.nasa.gov/saturn/facts/
- `NASA_URANUS_FACTS` — https://science.nasa.gov/uranus/facts/
- `NASA_NEPTUNE_FACTS` — https://science.nasa.gov/neptune/neptune-facts/
- `NASA_CERES_FACTS` — https://science.nasa.gov/dwarf-planets/ceres/facts/
- `NASA_PLUTO_FACTS` — https://science.nasa.gov/dwarf-planets/pluto/facts/

These sources support only the cells actually coded. Unresolved dimensions remain `PENDING_REVIEW`.

## Quantitative planet criteria

11. Margot, J.-L. (2015). A Quantitative Criterion for Defining Planets. *The Astronomical Journal*, 150, 185.
   - DOI: 10.1088/0004-6256/150/6/185
   - https://arxiv.org/abs/1507.06300
12. Margot, J.-L., Gladman, B., & Yang, T. (2024). Quantitative Criteria for Defining Planets.
   - https://arxiv.org/abs/2407.07590
13. Soter, S. (2006). What Is a Planet?
   - https://arxiv.org/abs/astro-ph/0608359

## QCA method

14. Thiem, A., & Duşa, A. (2013). QCA: A Package for Qualitative Comparative Analysis. *The R Journal*.
   - https://journal.r-project.org/articles/RJ-2013-009/
15. COMPASSS — QCA common-errors / good-practice materials.
   - https://compasss.org/

## Provenance rules

- Prefer IAU / NASA / JPL for labels and physical/orbital baseline.
- Preserve source + retrieval date + unit + uncertainty for raw numeric values.
- Keep source values, fitted approximate elements, descriptive satellite mean elements, proxies, derived physics, and evidence-coded qualitative states visibly distinct.
- A coded evidence value requires a source key; `PENDING_REVIEW` carries no scientific value and never enters analysis.
- Missing/un-ingested values are never zero-filled.
- No QCA result may be consulted while evidence-state coding is active.
