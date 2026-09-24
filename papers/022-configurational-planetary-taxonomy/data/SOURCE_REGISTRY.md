# Source Registry · ARIS4C022

Retrieval baseline: 2026-09-24.

## Classification / definitions

1. International Astronomical Union — List of Resolutions; 2006 Resolutions B5 and B6, “Definition of a Planet in the Solar System” / “Pluto”.
   - https://www.iau.org/Iau/Iau/Publications/List-of-Resolutions.aspx
2. IAU Astronomy FAQs — current summary of the adopted Solar-System planet definition.
   - https://www.iau.org/IAU/IAU/Astronomy-FAQs/FAQs.aspx

## Planetary physical/orbital data

3. NASA NSSDC Planetary Fact Sheet.
   - https://nssdc.gsfc.nasa.gov/planetary/factsheet/
4. NASA NSSDC Mars Fact Sheet.
   - https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html
5. NASA Science — Solar System / planets / dwarf planets.
   - https://science.nasa.gov/solar-system/
6. JPL Solar System Dynamics — orbits, physical characteristics, small-body tools.
   - https://ssd.jpl.nasa.gov/

## Quantitative planet criteria

7. Margot, J.-L. (2015). A Quantitative Criterion for Defining Planets. *The Astronomical Journal*, 150, 185.
   - DOI: 10.1088/0004-6256/150/6/185
   - https://arxiv.org/abs/1507.06300
8. Margot, J.-L., Gladman, B., & Yang, T. (2024). Quantitative Criteria for Defining Planets.
   - https://arxiv.org/abs/2407.07590
9. Soter, S. (2006). What Is a Planet?
   - https://arxiv.org/abs/astro-ph/0608359

## QCA method

10. Thiem, A., & Duşa, A. (2013). QCA: A Package for Qualitative Comparative Analysis. *The R Journal*.
    - https://journal.r-project.org/articles/RJ-2013-009/
11. COMPASSS — QCA common-errors / good-practice materials.
    - https://compasss.org/

## Provenance rules

- Prefer IAU / NASA / JPL for labels and physical/orbital baseline.
- Preserve source field + retrieval date + unit + uncertainty for every raw value.
- Derived variables must identify formula version and source variables.
- Model-estimated composition or interior variables must never be presented as directly measured.
- A later extrasolar phase must use a separate source registry and a separate definition scope.

## Machine-readable acquisition endpoints

12. NASA/JPL SBDB API documentation — machine-readable identity, orbit and selected physical parameters for known asteroids/comets.
    - https://ssd-api.jpl.nasa.gov/doc/sbdb.html
    - API version documented: 1.3 (2021 September)
    - Project fetcher: `code/fetch_jpl_sbdb.py`

13. NASA/JPL Horizons API documentation — ephemeris/state-vector fallback for bodies that need Horizons rather than SBDB.
    - https://ssd-api.jpl.nasa.gov/doc/horizons.html

## Frozen source-definition notes

- NASA NSSDC Planetary Fact Sheet was last updated 2025-03-18 at project retrieval and is used for the first 10-body seed.
- The table's “Diameter” is equatorial diameter, not mean volumetric diameter.
- Its gravity values are equatorial and include rotation; gas-giant gravity is reported at the 1-bar pressure level.
- Moon distance/orbit fields in the compact comparison table are Earth-relative, not Sun-relative.
- See `process/NASA_SEED_QC.md` before deriving density/gravity from compact fact-sheet fields.
