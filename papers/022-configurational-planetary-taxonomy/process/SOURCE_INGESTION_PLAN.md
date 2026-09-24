# Source Ingestion Plan · ARIS4C022

## Source hierarchy

1. IAU: official Solar-System classification / definition.
2. NASA NSSDC fact sheets: bulk baseline for major planets, Moon and Pluto.
3. JPL SBDB API: machine-readable orbital + selected physical data for asteroids/comets/small bodies.
4. JPL Horizons API: orbit/state-vector fallback and satellite/planetary ephemerides where appropriate.
5. Peer-reviewed planetary literature: composition, interior, hydrostatic-equilibrium disputes, geological activity, atmosphere/ocean evidence.

## Current empirical seed

A 10-body NASA NSSDC seed table is committed in:
- data/raw/nasa_nssdc_planetary_fact_sheet_seed.csv
- data/manifests/nasa_nssdc_planetary_fact_sheet_2025-03-18.json

It includes the eight planets plus Moon and Pluto.

## Important hierarchy rule

NASA's compact comparison table reports the Moon's distance and period relative to Earth, whereas the planet rows are Sun-relative. The raw seed therefore records the orbit reference explicitly. These values must not be put into one heliocentric-distance QCA condition without transformation.

## JPL small-body route

code/fetch_jpl_sbdb.py requests:
- object identity;
- orbit elements;
- selected physical parameters;
- full precision.

The cache is JSONL so the original API payload is retained. Harmonization happens in a separate derived step.

## Planned acquisition batches

Batch A — large/benchmark asteroids:
Vesta, Pallas, Hygiea, Interamnia, Eros.

Batch B — sample-return/rubble-pile:
Bennu, Ryugu, Itokawa.

Batch C — trans-Neptunian / candidate dwarf:
Quaoar, Orcus, Sedna, Gonggong, Salacia, Varda, Ixion, Varuna.

Dwarf planets and natural satellites require mixed IAU/NASA/JPL/peer-reviewed sources; they must not be forced through SBDB if the database is not the authoritative representation for that body.

## Provenance contract

For every harmonized cell preserve:
- source_id
- source_url
- retrieval date
- raw field name
- raw value
- raw unit
- transformed value/unit
- uncertainty or evidence state
- derivation formula/version when derived
