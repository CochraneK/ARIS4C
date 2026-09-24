# Source Registry · ARIS4C022

Retrieval baseline: 2026-09-24.

## Core classification / physical / orbital sources

1. IAU 2006 Resolutions B5/B6.
   - https://iau.org/Iau/Publications/List-of-Resolutions
2. JPL Planetary Physical Parameters.
   - https://ssd.jpl.nasa.gov/planets/phys_par.html
3. JPL Approximate Positions of the Planets.
   - https://ssd.jpl.nasa.gov/planets/approx_pos.html
4. JPL Planetary Satellite Physical Parameters.
   - https://ssd.jpl.nasa.gov/sats/phys_par/
5. JPL Planetary Satellite Mean Elements.
   - https://ssd.jpl.nasa.gov/sats/elem/
6. JPL Astrodynamic Parameters.
   - https://ssd.jpl.nasa.gov/astro_par.html
7. JPL Small-Body Database API.
   - https://ssd-api.jpl.nasa.gov/doc/sbdb.html
   - https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html
8. JPL Small-Body Element Tables / Orbits.
   - https://ssd.jpl.nasa.gov/sb/elem_tables.html
   - https://ssd.jpl.nasa.gov/sb/orbits.html

## Evidence-state coding · Anchor batch 01

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

## Evidence-state coding · Moon/boundary batch 02

- `NASA_MOON_FACTS` — https://science.nasa.gov/moon/facts/
- `NASA_IO_FACTS` — https://science.nasa.gov/jupiter/jupiter-moons/io/facts/
- `NASA_EUROPA_FACTS` — https://science.nasa.gov/jupiter/jupiter-moons/europa/europa-facts/
- `NASA_GANYMEDE_FACTS` — https://science.nasa.gov/jupiter/jupiter-moons/ganymede/facts/
- `NASA_CALLISTO_FACTS` — https://science.nasa.gov/jupiter/jupiter-moons/callisto/facts/
- `NASA_ENCELADUS_OVERVIEW` — https://science.nasa.gov/saturn/moons/enceladus/
- `NASA_TITAN_FACTS` — https://science.nasa.gov/saturn/moons/titan/facts/
- `NASA_TRITON_OVERVIEW` — https://science.nasa.gov/neptune/moons/triton/
- `NASA_NH_PLUTO_CHARON_BLOG` — https://science.nasa.gov/blogs/new-horizons/2016/01/15/studying-pluto-from-3-billion-miles-away/
- `NASA_NTRS_PLUTO_CHARON_GEOLOGY` — https://ntrs.nasa.gov/citations/20170000011

Batch-02 coding uses only claims directly supported by these agency/mission sources. Charon's paleo-ocean evidence is retained in notes rather than coded as a present-day ocean.

## Quantitative planet criteria

9. Margot, J.-L. (2015). *A Quantitative Criterion for Defining Planets*. AJ 150:185.
   - https://arxiv.org/abs/1507.06300
10. Margot, Gladman & Yang (2024). *Quantitative Criteria for Defining Planets*.
   - https://arxiv.org/abs/2407.07590
11. Soter, S. (2006). *What Is a Planet?*
   - https://arxiv.org/abs/astro-ph/0608359

## QCA method

12. Thiem & Duşa (2013), R Journal QCA package.
   - https://journal.r-project.org/articles/RJ-2013-009/
13. COMPASSS.
   - https://compasss.org/

## Provenance rules

- Prefer IAU / NASA / JPL for labels and physical/orbital baseline.
- Preserve source + retrieval date + unit + uncertainty for raw numeric values.
- Keep raw, approximate, proxy, derived and evidence-coded values visibly distinct.
- A coded evidence value requires a source key.
- `PENDING_REVIEW` has no scientific value and never enters analysis.
- Missing/un-ingested values are never zero-filled.
- No QCA result may be consulted while evidence-state coding remains active.
