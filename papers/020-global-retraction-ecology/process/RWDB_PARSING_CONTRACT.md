# RWDB Parsing Contract · v1

Source documentation states that the CSV is comma-separated and that lists within cells are semicolon-separated.

## Never split as lists
Record ID, Title, Journal, Publisher, RetractionDate, RetractionDOI, RetractionPubMedID, OriginalPaperDate, OriginalPaperDOI, OriginalPaperPubMedID, RetractionNature, Paywalled, Notes.

A semicolon in free text, especially Title or Notes, is content rather than a list delimiter.

## Semicolon-list fields
Treat these as ordered multi-valued cells where semicolons occur:
- Subject
- Institution
- Country
- Author
- URLS
- ArticleType
- Reason

Trim surrounding whitespace, preserve the original string, and create normalized exploded representations separately.

## Counting rules
- **Reason:** multi-label by definition; never infer a single main reason.
- **Country:** show full and fractional counting. If k distinct countries are present, full counting contributes 1 to each; fractional counting contributes 1/k.
- **Subject:** same dual full/fractional strategy for RWDB descriptive analyses.
- **Institution / Author:** raw strings are not resolved entities; identity confidence tiers are required before risk models.
- **URLS:** provenance only.

## DOI normalization
Lowercase; trim; remove `doi:`, `https://doi.org/`, or `http://doi.org/`. Blank / 0 / unavailable / n/a are missing.

Raw names, affiliations, country labels and reasons are retained alongside any normalized mapping; raw values are never overwritten.
