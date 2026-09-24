# Source Registry · ARIS4C022

Retrieval baseline: 2026-09-24.

## Core classification / physical / orbital sources

1. IAU 2006 Resolutions B5/B6 — https://iau.org/Iau/Publications/List-of-Resolutions
2. JPL Planetary Physical Parameters — https://ssd.jpl.nasa.gov/planets/phys_par.html
3. JPL Approximate Positions of the Planets — https://ssd.jpl.nasa.gov/planets/approx_pos.html
4. JPL Planetary Satellite Physical Parameters — https://ssd.jpl.nasa.gov/sats/phys_par/
5. JPL Planetary Satellite Mean Elements — https://ssd.jpl.nasa.gov/sats/elem/
6. JPL Astrodynamic Parameters — https://ssd.jpl.nasa.gov/astro_par.html
7. JPL SBDB API — https://ssd-api.jpl.nasa.gov/doc/sbdb.html
8. JPL SBDB query docs — https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html

## Evidence batches 01–03

Existing NASA/JPL/peer-reviewed sources remain frozen as listed in prior revisions for:
- 8 planets + Ceres + Pluto
- Moon / Io / Europa / Ganymede / Callisto / Enceladus / Titan / Triton / Charon
- remaining selected satellites + Haumea / Makemake / Eris
- Mimas 2024 ocean update / source-conflict adjudication

## Evidence batch 04 · mission/sample-return small bodies

- `NASA_VESTA_FACTS` — https://science.nasa.gov/solar-system/asteroids/4-vesta/
- `NASA_DAWN_VESTA` — https://science.nasa.gov/mission/dawn/science/vesta/
- `NASA_EROS_NEAR` — https://science.nasa.gov/mission/near-shoemaker/
- `NASA_EROS_SOLID_UNIFORM` — https://science.nasa.gov/image-article/apod-2009-june-7-asteroid-eros-reconstructed/
- `NASA_BENNU_FACTS` — https://science.nasa.gov/solar-system/asteroids/101955-bennu/facts/
- `NASA_BENNU_RUBBLE` — https://www.nasa.gov/solar-system/cosmic-detective-work-why-we-care-about-space-rocks/
- `NASA_BENNU_SAMPLE` — https://science.nasa.gov/missions/osiris-rex/nasas-bennu-samples-reveal-complex-origins-dramatic-transformation/
- `NASA_RYUGU_SAMPLE` — https://www.nasa.gov/centers-and-facilities/goddard/first-look-at-ryugu-asteroid-sample-reveals-it-is-organic-rich/
- `NASA_RYUGU_RUBBLE` — https://science.nasa.gov/blogs/osiris-rex/2023/06/28/long-history-and-bright-future-of-space-sample-deliveries/
- `NASA_ITOKAWA_FACTS` — https://science.nasa.gov/solar-system/asteroids/25143-itokawa/

Returned-sample interpretation may describe aqueous alteration on a destroyed parent body. That evidence is not converted into a present-day ocean state for Bennu or Ryugu.

## Quantitative planet criteria

- Margot (2015) — https://arxiv.org/abs/1507.06300
- Margot, Gladman & Yang (2024) — https://arxiv.org/abs/2407.07590
- Soter (2006) — https://arxiv.org/abs/astro-ph/0608359

## QCA method

- Thiem & Duşa (2013) — https://journal.r-project.org/articles/RJ-2013-009/
- COMPASSS — https://compasss.org/

## Provenance rules

- Raw, approximate, proxy, derived and evidence-coded values remain distinct.
- Every non-pending evidence state requires a source key.
- Scientific missingness is never zero-filled.
- Temporal supersession is distinct from unresolved conflict.
- Parent-body alteration is distinct from current-object state.
- No QCA result may be consulted while evidence-state coding is active.
