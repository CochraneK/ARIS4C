# Source Registry · ARIS4C022

Retrieval baseline: 2026-09-24.

## Classification / definitions

1. International Astronomical Union — List of Resolutions; 2006 Resolutions B5 and B6, “Definition of a Planet in the Solar System” / “Pluto”.
   - https://iau.org/Iau/Publications/List-of-Resolutions

## Planet / dwarf-planet physical data

2. JPL Solar System Dynamics — Planetary Physical Parameters.
   - https://ssd.jpl.nasa.gov/planets/phys_par.html
   - Used in `raw_physical_core_v0.1.csv` for 8 planets + 5 IAU dwarf planets.
   - Provides mass, mean radius, bulk density, sidereal rotation, sidereal orbital period, geometric albedo, and references/uncertainties where available.

3. JPL Solar System Dynamics — Approximate Positions of the Planets.
   - https://ssd.jpl.nasa.gov/planets/approx_pos.html
   - Table 1 provides approximate J2000 Keplerian elements for Mercury through Neptune for 1800–2050.
   - `orbital_geometry_v0.2.csv` uses its semimajor axis, eccentricity, and inclination for seven planet-center/system rows.
   - Earth is explicitly recorded as the Earth-Moon barycenter proxy because that is what the JPL table supplies.
   - These are lower-accuracy fitted elements; Horizons remains the route for high-precision ephemerides.

4. NASA NSSDC Planetary Fact Sheet and notes.
   - https://nssdc.gsfc.nasa.gov/planetary/factsheet/
   - https://nssdc.gsfc.nasa.gov/planetary/factsheet/fact_notes.html
   - Secondary cross-check route; values may evolve with ongoing research.

## Satellite physical + orbital data

5. JPL Solar System Dynamics — Planetary Satellite Physical Parameters.
   - https://ssd.jpl.nasa.gov/sats/phys_par/
   - Used in `raw_physical_core_v0.1.csv` for all 21 selected satellites.
   - Primary fields: GM, uncertainty/reference, mean radius, radius uncertainty, density and uncertainty.
   - Satellite mass is deterministically derived from GM with CODATA-2018 G and labeled as derived.

6. JPL Solar System Dynamics — Planetary Satellite Mean Elements.
   - https://ssd.jpl.nasa.gov/sats/elem/
   - Used for all 21 selected satellites.
   - Preserves primary-centric semimajor axis, eccentricity, inclination, orbital period, reference frame, epoch, and ephemeris identifier.
   - These are descriptive mean elements, not high-fidelity ephemerides.

7. JPL Solar System Dynamics — Astrodynamic Parameters.
   - https://ssd.jpl.nasa.gov/astro_par.html
   - Reference route for current planetary-system GM values, Solar GM, AU, and CODATA-2018 G.

## Small-body route

8. JPL Small-Body Database API.
   - Documentation: https://ssd-api.jpl.nasa.gov/doc/sbdb.html
   - Query API: https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html
   - Provides current machine-readable identification, orbital elements and selected physical data. The API documentation requires callers to inspect the payload signature/version.
   - `code/fetch_sbdb_small_bodies.py` remains the canonical raw-JSON snapshot route for the 16 frozen small/boundary cases.
   - Current control-thread network surfaces could not retrieve the live 16-response snapshot on 2026-09-24; those rows remain explicit `NA_NOT_INGESTED`.

9. JPL Solar System Dynamics — Small-Body Element Tables.
   - https://ssd.jpl.nasa.gov/sb/elem_tables.html
   - Confirms the fixed-format asteroid schema and provenance fields: epoch (TDB/MJD), semimajor axis, eccentricity, J2000-ecliptic inclination, angular elements, H/G and orbit-solution reference.
   - The page's sample header includes Ceres and Pallas, but sample rows are not treated as a current replacement for the live SBDB snapshot.

10. JPL Solar System Dynamics — Small-Body Orbits & Ephemerides.
    - https://ssd.jpl.nasa.gov/sb/orbits.html
    - States that JPL SBDB supplies orbits for known small bodies including TNOs and dwarf planets, and that Horizons is the ephemeris route.

## Quantitative planet criteria

11. Margot, J.-L. (2015). A Quantitative Criterion for Defining Planets. *The Astronomical Journal*, 150, 185.
   - DOI: 10.1088/0004-6256/150/6/185
   - https://arxiv.org/abs/1507.06300
   - Implementation uses Eq. 8, Eq. 9 and Eq. 10 directly.

12. Margot, J.-L., Gladman, B., & Yang, T. (2024). Quantitative Criteria for Defining Planets.
   - https://arxiv.org/abs/2407.07590

13. Soter, S. (2006). What Is a Planet?
   - https://arxiv.org/abs/astro-ph/0608359
   - Implementation uses the published planetary discriminant mu = M/m; a current orbital-zone mass census is a separate data requirement.

## QCA method

14. Thiem, A., & Duşa, A. (2013). QCA: A Package for Qualitative Comparative Analysis. *The R Journal*.
   - https://journal.r-project.org/articles/RJ-2013-009/

15. COMPASSS — QCA common-errors / good-practice materials.
   - https://compasss.org/

## Provenance rules

- Prefer IAU / NASA / JPL for labels and physical/orbital baseline.
- Preserve source field + retrieval date + unit + uncertainty for every raw value.
- Snapshot machine-readable API responses before flattening when feasible.
- Keep source values, fitted approximate elements, descriptive satellite mean elements, proxies, and derived physics visibly distinct.
- Derived variables must identify formula version and source variables.
- Model-estimated composition or interior variables must never be presented as directly measured.
- Missing or un-ingested values remain explicit missingness states, never zero-filled.
- A later extrasolar phase must use a separate source registry and a separate definition scope.
