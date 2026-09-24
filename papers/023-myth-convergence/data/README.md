# Data · ARIS4C-023

## Canonical tables

1. `sources.csv` — source witnesses and provenance.
2. `traditions.csv` — bounded tradition-time units.
3. `motifs.csv` — motif ontology and catalogue crosswalks.
4. `coding.csv` — source-supported motif coding.
5. `contacts.csv` — historically supported contact edges.
6. `environment.csv` — preregistered ecological variables.
7. `genealogy.csv` — language/ancestry proxies and uncertainty.
8. derived `dyads.csv/parquet` — pairwise table; never hand-edited.

Pilot source inventory currently lives in `pilot0_source_audit.csv`.
The reliability packet lives under `calibration/`.

## Missingness

Use: present, explicitly assessed absent, uncertain, and not observed.

**Unknown / uncertain / not-observed are never converted to absence.**

## Witness scope

Every coded claim also records:
- `in-window`
- `inherited_or_transmitted`
- `later-comparator`
- `uncertain`

This prevents a late surviving witness from being silently treated as proof of an early origin date.

## Evidence grades

A = primary/critical text or direct scholarly edition; B = specialist secondary work with explicit source trail; C = curated comparative database requiring source audit for confirmatory use; D = tertiary/web discovery only.

Licensed/raw corpora are not committed when redistribution is not permitted. Commit provenance, codebooks, hashes/metadata and derived public-safe outputs.

## Analysis utilities

```bash
python code/validate_coding.py data/coding.csv
python code/build_similarity.py --coding data/coding.csv --out data/dyads.csv --min-comparable 10
```

The similarity script computes Jaccard on explicit present/absent comparisons and never treats missing data as absence.
