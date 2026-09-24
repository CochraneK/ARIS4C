# Event and Work Identity Contract · v1

RWDB is event-oriented; ARIS4C-020 therefore keeps both an **event table** and a **work table**.

## Event table
Primary key: `Record ID`. Every RWDB row is retained.

## Primary event population
Confirmatory event analyses use `RetractionNature == "Retraction"`. EOC / Correction / Reinstatement stay outside the primary retraction-rate numerator.

## Work identity tiers
1. **Tier A — DOI:** normalized OriginalPaperDOI.
2. **Tier B — PMID:** OriginalPaperPubMedID when DOI is absent.
3. **Tier C — unresolved candidate:** exact normalized Title + Journal + OriginalPaperDate for sensitivity/manual QA only.

For DOI-linked work-level analyses, multiple Retraction rows for one original DOI collapse to one work:
- date = earliest valid RetractionDate;
- reasons = union of all Retraction reason labels;
- countries/subjects = union with row provenance;
- contributing Record IDs remain linked.

The 2026-09-23 snapshot contains **14 original DOI values repeated across Retraction rows**, with a maximum multiplicity of **145**. Therefore row counts and unique-retracted-work counts are not interchangeable.

Primary normalized risk analyses start with DOI-linked unique works. No fuzzy author/title deduplication enters the confirmatory numerator before a separate identity-validation gate.
