# ARIS4C021 · Source Gap and Cross-check Policy

## Current gap

The official Systemic Peace landing page, codebook, consolidated case list, and legacy GenoPoliticide XLS endpoint are verified. The current execution runtime cannot retrieve the legacy XLS binary, so its bytes and SHA-256 are not yet frozen locally.

This is an acquisition limitation, not permission to invent or silently replace the source.

## Third-party transformed cross-check

IBM's public mixed-migration-forecasting repository contains:
- a transformer that reads PITF GenoPoliticide 2017.xls;
- a processed long-format SystemicPeace CSV;
- genocide indicators SP.GE.YR.LENGTH and SP.GE.MAG.DEATH.

Use:
- check country-year episode presence and death-magnitude patterns;
- detect obvious transcription mismatches once the official source is acquired.

Do not use:
- as the canonical original PITF workbook;
- as Williams's 139-row condition matrix;
- to infer I/S/E/P/A/W values not present in the transformed file.

The exact IBM commit is pinned in the cross-check script.

## Resolution gate

The source gap is closed only when:
1. the official PITF source is downloaded;
2. byte size + SHA-256 are frozen;
3. the transformed IBM cross-check is compared against the overlapping official annual fields;
4. discrepancies are documented rather than silently reconciled.
