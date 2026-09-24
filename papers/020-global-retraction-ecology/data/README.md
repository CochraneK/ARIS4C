# Data

## Canonical raw source

Retraction Watch bulk data distributed by Crossref:
https://gitlab.com/crossref/retraction-watch-data

The repository is updated on working days. Raw files are downloaded into `data/raw/`, which is gitignored in ARIS4C.

## Expected Retraction Watch fields

Record ID, Title, Subject, Institution, Journal, Publisher, Country, Author, URLS, ArticleType, RetractionDate, RetractionDOI, RetractionPubMedID, OriginalPaperDate, OriginalPaperDOI, OriginalPaperPubMedID, RetractionNature, Reason, Paywalled, Notes.

Semicolon-delimited lists inside cells must be parsed as multi-valued fields where specified by Retraction Watch; do not naïvely split free-text Notes.

## Tracked artifacts

- `data/manifests/rwdb_source.json` — retrieval provenance, hash, row count, columns.
- `data/derived/` — compact analysis-ready tables only.
- large raw snapshots and caches stay local / artifact storage and are not committed.
