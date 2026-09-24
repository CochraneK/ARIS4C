# Source Registry · ARIS4C022

Retrieval baseline: 2026-09-24.

## Classification / definitions

1. International Astronomical Union — List of Resolutions; 2006 Resolutions B5 and B6, “Definition of a Planet in the Solar System” / “Pluto”.
   - https://iau.org/Iau/Publications/List-of-Resolutions

## Planet / dwarf-planet physical data

2. JPL Solar System Dynamics — Planetary Physical Parameters.
   - https://ssd.jpl.nasa.gov/planets/phys_par.html
   - Used in `raw_physical_core_v0.1.csv` for 8 planets + 5 IAU dwarf planets.
   - Source table provides mass, mean radius, bulk density, sidereal rotation, sidereal orbital period, geometric albedo and references/uncertainties where available.

3. NASA NSSDC Planetary Fact Sheet and notes.
   - https://nssdc.gsfc.nasa.gov/planetary/factsheet/
   - https://nssdc.gsfc.nasa.gov/planetary/factsheet/fact_notes.html
   - Secondary cross-check route; the notes explicitly state that values evolve with ongoing research.

## Satellite physical data

4. JPL Solar System Dynamics — Planetary Satellite Physical Parameters.
   - https://ssd.jpl.nasa.gov/sats/phys_par/
   - Used in `raw_physical_core_v0.1.csv` for all 21 selected satellites.
   - Primary recorded fields in this tranche: GM, GM uncertainty/reference, mean radius, radius uncertainty, derived density and uncertainty.
   - Satellite mass is deterministically derived from GM with CODATA-2018 G and labeled as derived.

## Small-body route

5. JPL Small-Body Database API.
   - Documentation: https://ssd-api.jpl.nasa.gov/doc/sbdb.html
   - Query API: https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html
   - The API exposes orbital elements plus physical fields including effective diameter, GM, density, rotation period and geometric albedo.
   - `code/fetch_sbdb_small_bodies.py` is frozen to snapshot the 16 selected small/boundary cases before flattening them.

## Quantitative planet criteria

6. Margot, J.-L. (2015). A Quantitative Criterion for Defining Planets. *The Astronomical Journal*, 150, 185.
   - DOI: 10.1088/0004-6256/150/6/185
   - https://arxiv.org/abs/1507.06300
   - Implementation uses Eq. 8, Eq. 9 and Eq. 10 directly.

7. Margot, J.-L., Gladman, B., & Yang, T. (2024). Quantitative Criteria for Defining Planets.
   - https://arxiv.org/abs/2407.07590

8. Soter, S. (2006). What Is a Planet?
   - https://arxiv.org/abs/astro-ph/0608359
   - Implementation uses the published planetary discriminant mu = M/m; a current orbital-zone mass census is a separate data requirement.

## QCA method

9. Thiem, A., & Duşa, A. (2013). QCA: A Package for Qualitative Comparative Analysis. *The R Journal*.
   - https://journal.r-project.org/articles/RJ-2013-009/

10. COMPASSS — QCA common-errors / good-practice materials.
    - https://compasss.org/

## Provenance rules

- Prefer IAU / NASA / JPL for labels and physical/orbital baseline.
- Preserve source field + retrieval date + unit + uncertainty for every raw value.
- Snapshot machine-readable API responses before flattening when feasible.
- Derived variables must identify formula version and source variables.
- Model-estimated composition or interior variables must never be presented as directly measured.
- Missing or un-ingested values remain explicit missingness states, never zero-filled.
- A later extrasolar phase must use a separate source registry and a separate definition scope.
