# SIR submission requirements audit

**Checked:** 2026-09-23  
**Target:** Social Indicators Research  
**Official journal guidance:** https://link.springer.com/journal/11205/submission-guidelines

## Current gate

| Requirement | Current state | Decision |
|---|---|---|
| Double-anonymous manuscript and associated reviewer files | PASS at Markdown / Online Resource layer | Keep author identity and declarations out of reviewer-visible files |
| Editable manuscript source | PENDING REBUILD | Submit the freshly rebuilt blinded DOCX, not the older pre-edit binary |
| Reviewer PDF | PENDING REBUILD / VISUAL QA | Regenerate from the same current blinded Markdown and inspect every page |
| Article length 5,000-10,000 words including references | PASS | Current blinded Markdown ~8.15k words |
| Abstract 150-250 words | PASS | 218 words |
| Keywords 4-6 | PASS | 6 keywords |
| LLM substantive use documented in Methods | PASS | Human accountability and verification boundary are stated |
| Supplementary material referenced in manuscript | PASS | Data/Code Availability cites Online Resource 1 |
| Multi-file supplementary delivery | PASS | Online Resource 1 is a ZIP |
| Anonymous data/code delivery | PASS | Exact artifact pinned in `SIR_ONLINE_RESOURCE_1_POINTER.md` |
| Reproducibility number check | PASS | Headline values independently recomputed against `manuscript_number_lock.json` |
| Author contribution / competing-interest interface fields | AUTHOR INPUT REQUIRED | Complete in the submission interface |
| Affiliation, corresponding email, ORCID if used | AUTHOR INPUT REQUIRED | Complete author-side only |
| Funding declaration | AUTHOR INPUT REQUIRED | Complete author-side only |
| Institution-specific ethics/exemption determination | AUTHOR INPUT REQUIRED | Do not invent an exemption; confirm the applicable institutional requirement |

## Double-anonymous precedence rule

The current SIR page explicitly says the journal recently moved submission systems and is revising its instructions. Its current double-anonymous section requires names, affiliations and potentially identifying information to be removed from the manuscript and accompanying files.

A later legacy Supplementary Information template on the same page still instructs authors to include author names/affiliations inside SI files. These instructions conflict. For peer-review delivery, this project follows the newer and more specific **double-anonymous requirement** and keeps Online Resource 1 de-identified.

Author identity, acknowledgements, disclosures, funding and other author-side fields are supplied through the submission system / author-side materials as requested by the portal, never through the reviewer ZIP.

## Source-file rules captured

- Provide editable source files at submission/revision.
- Manuscript text should be supplied in a common editable format such as DOCX.
- Figures are cited consecutively and normally placed in the body of the text.
- Supplementary multi-file collections may be supplied as ZIP/GZ.
- Supplementary files must be explicitly cited as Online Resource(s).
- The submitted supplementary archive is published essentially as received, so the exact ZIP is treated as a frozen deliverable and checksum-pinned.

## Current exact reviewer artifact

See `submission/SIR_ONLINE_RESOURCE_1_POINTER.md`.

- artifact branch: `artifact-019-sir-online-resource-1`
- artifact commit: `c0492aab9bcb508a58d9cd745af3f4ef6b2354b9`
- ZIP SHA-256: `8463e216e4c49dea30ee47773a55326e6830ed8a0735295770eeff3239f5ad07`
- identity scan: PASS
- number-lock reproduction: PASS

## Remaining executable gate

Regenerate the blinded DOCX and reviewer PDF from the **current** Markdown (which now cites Online Resource 1 and no longer exposes author-side declarations), then repeat full visual QA. Only after that rebuild should the final submission manifest be frozen.

## Remaining author-only gate

Complete `submission/SIR_AUTHOR_SIDE_METADATA_TEMPLATE.md` using real author/institution information and the applicable ethics/exemption determination. These fields cannot be guessed from the research repository.
