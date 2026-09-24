# OpenAlex API Contract · frozen 2026-09-24

This file freezes the external API assumptions used by ARIS4C-020. It should be re-checked before a future rerun because OpenAlex is a live service.

## Authentication

Supported production mode:

```http
Authorization: Bearer $OPENALEX_API_KEY
```

The API key is optional for casual requests and recommended for real-scale execution. ARIS4C-020 never writes the key into URLs, output files, manifests, or Git.

Official reference:
https://help.openalex.org/api/authentication/

## Corpus

All Work queries explicitly send:

```text
corpus=core
```

OpenAlex currently defines:
- `core`: curated catalog and current default;
- `expansion`: additional expansion layer;
- `all`: core + expansion.

Pinning `core` prevents an implicit corpus-default change from silently changing the denominator.

Official reference:
https://help.openalex.org/data/works/corpus/

## DOI batching

OpenAlex supports OR filters using `|` and documents batch retrieval of up to 100 IDs in a request. ARIS4C-020 therefore batches at most 100 DOI values per enrichment call.

Official reference:
https://help.openalex.org/how-to/api-recipes/

## Grouped denominators

`group_by` returns `key`, `key_display_name`, and `count`.

Grouped responses return at most 200 groups per page. For more groups, ARIS4C-020 uses cursor paging from `cursor=*` through `meta.next_cursor`.

Official reference:
https://help.openalex.org/api/grouping/

## Incoming citations

OpenAlex defines:

```text
filter=cites:W...
```

as works that cite the target Work. A citing Work's `referenced_works` list is used to map a response back to all batched targets it cites.

Official references:
https://help.openalex.org/how-to/api-recipes/
https://github.com/ourresearch/openalex-docs/blob/main/api-entities/works/filter-works.md

## Retraction metadata

OpenAlex `is_retracted` is treated as a metadata/concordance field, never as ARIS4C-020's case-defining authority.

Primary case membership remains:
`RWDB RetractionNature == "Retraction"`.

## Change-control rule

If any of the following external contracts change, bump this file and the 020 pipeline version before rerunning:
- corpus semantics/default;
- filter syntax or OR limit;
- grouped-result schema/paging;
- `cites` semantics;
- authentication method;
- Work field names consumed by the pipeline.

A changed API contract invalidates direct comparison to a prior API-derived snapshot unless the difference is explicitly reconciled.
