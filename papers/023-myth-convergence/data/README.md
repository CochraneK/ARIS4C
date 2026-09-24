# Data · ARIS4C-023

## Canonical tables

1. `sources.csv` — source witnesses and provenance.
2. `traditions.csv` — bounded tradition-time units.
3. `motifs.csv` — motif ontology and catalogue crosswalks.
4. `coding.csv` — source-supported motif coding.
5. `contacts.csv` — historically supported contact edges.
6. `environment.csv` — preregistered ecological variables.
7. `genealogy.csv` — language/ancestry proxies and uncertainty.
8. derived `dyads.parquet` — pairwise table; never hand-edited.

## Missingness
Use: present, explicitly assessed absent, uncertain, and not observed. **Do not convert unknown/not-observed to absence.**

## Evidence grades
A = primary/critical text or direct scholarly edition; B = specialist secondary work with explicit source trail; C = curated comparative database requiring source audit for confirmatory use; D = tertiary/web discovery only.

Licensed/raw corpora are not committed when redistribution is not permitted. Commit provenance, codebooks, hashes/metadata and derived public-safe outputs.
