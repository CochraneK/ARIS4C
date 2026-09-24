# Orbit source-hardening audit · v0.2

Date: 2026-09-24

## Change from v0.1

The eight planet rows no longer use semimajor axes reconstructed from sidereal periods.

- Mercury, Venus, Mars, Jupiter, Saturn, Uranus and Neptune now use JPL's published J2000 approximate Keplerian elements.
- Earth uses the JPL Earth-Moon barycenter approximate element as an **explicit proxy**, not as an Earth-center ephemeris.
- The five dwarf planets remain on the explicitly derived period→a path until a live SBDB/Horizons snapshot is captured.
- The 21 satellite rows remain JPL mean elements.
- The 16 small/boundary bodies remain un-ingested.

## Difference against previous period-derived values

| body | v0.1 derived a (au) | v0.2 JPL a/proxy (au) | relative change |
|---|---:|---:|---:|
| Mercury | 0.387103531 | 0.387099270 | -0.0011% |
| Venus | 0.723340744 | 0.723335660 | -0.0007% |
| Earth | 1.000011600 | 1.000002610 | -0.0009% |
| Mars | 1.523710305 | 1.523710340 | 0.0000% |
| Jupiter | 5.201400444 | 5.202887000 | 0.0286% |
| Saturn | 9.535985906 | 9.536675940 | 0.0072% |
| Uranus | 19.182752170 | 19.189164640 | 0.0334% |
| Neptune | 30.057732950 | 30.069922760 | 0.0406% |

These differences are small enough that the earlier Margot smoke tests were not qualitatively dependent on the period-derived approximation, but v0.2 has better provenance.

## Current orbit provenance counts

- 7 planet rows: `JPL_APPROX_PLANET_ELEMENTS`
- 1 Earth row: `JPL_APPROX_PLANET_ELEMENTS_EMB_PROXY`
- 5 dwarf-planet rows: `JPL_PLANET_PHYS_PERIOD` derived a
- 21 satellite rows: `JPL_SAT_MEAN_ELEMENTS`
- 16 small-body rows: `JPL_SBDB_API_PLANNED`

High-precision orbital work still belongs in Horizons; this comparative taxonomy only needs a clearly sourced stable descriptor layer.
