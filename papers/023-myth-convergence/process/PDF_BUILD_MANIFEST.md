# PDF Build + QA Manifest · ARIS4C-023

## Local publication artifacts

The scientific core has been compiled locally and visually QA'd in the current execution environment.

| Artifact | Pages | SHA-256 | QA |
|---|---:|---|---|
| ARIS4C-023_EN.pdf | 12 | aa0d39b5fa2c9c854f9013b43b3e1edfd5734bbe9b22f33a7b8b74c495afd0c2 | PASS |
| ARIS4C-023_ZH.pdf | 10 | 1fca428a9a8200637171eee82928c90c98e41d8fc54f5039b84f05a5c0b31139 | PASS |
| one-page visual (local WEBP) | 1 image | f61b4241b62fb640a4549bde7f2d076efe75762298b37437fad4756d98b35b7f | PASS |

PDF preflight: both PDFs open successfully in PyMuPDF, are unencrypted, and are text PDFs rather than scanned-image PDFs. Every DOCX-rendered page was visually inspected; final PDF renders were separately checked on figure/table-heavy pages.

## Repository publication state

- The one-page visual is committed as SVG: `docs/assets/paper-at-a-glance/023.svg`.
- The manuscripts are committed with inline figure/table references.
- **The PDF binary blobs are not yet in GitHub.** The current GitHub connector write surface accepts UTF-8 text or a complete in-memory base64 blob, but cannot consume the generated container file reference directly. This is an execution-surface limitation, not a scientific or PDF-generation failure.
- Therefore PDF-first public links are intentionally **not fabricated**, and the project is not marked Finish.

## Reproducibility

Canonical source inputs:
- `manuscript/working_paper_en.md`
- `manuscript/working_paper_zh.md`
- `figures/fig1_pipeline.svg`
- `figures/fig2_bundle_jaccard.svg`
- `figures/fig3_mechanism_map.svg`

The verified local build used Pandoc -> DOCX -> LibreOffice PDF, with Noto CJK fonts and render-first QA. A future binary-capable execution surface should rebuild or upload the two PDFs, verify the hashes/render, wire PDF-first links, and only then close the Finish gate.
