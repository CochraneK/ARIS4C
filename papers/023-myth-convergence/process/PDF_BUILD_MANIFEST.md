# PDF Build + QA Manifest · ARIS4C-023

## Durable repository PDFs

| Artifact | Repository path | Pages | Bytes | Git blob SHA | Verification |
|---|---|---:|---:|---|---|
| English PDF | `dist/ARIS4C-023_EN.pdf` | 6 | 59,060 | `37b85671190a160e1fea7d93848bf20a7d33c36a` | GitHub re-read: PDF 1.4 header + page objects + xref + trailer + EOF |
| 中文 PDF | `dist/ARIS4C-023_ZH.pdf` | 5 | 53,718 | `b59f0dfc7271b4833f3332c9d611cc8aca515874` | GitHub re-read: PDF 1.4 header + page objects + xref + trailer + EOF |

The durable repository editions are compact text/vector PDFs generated directly from the frozen Markdown manuscripts. English text uses a standard PDF Latin font; Chinese uses a standard CJK CID font mapping. Scientific diagrams are drawn as PDF vector primitives rather than screenshots.

## High-layout local QA build

Before the durable Git editions were generated, a separate Pandoc → DOCX → LibreOffice publication build was fully rendered and visually inspected page by page:

- EN: 12 pages, SHA-256 `aa0d39b5fa2c9c854f9013b43b3e1edfd5734bbe9b22f33a7b8b74c495afd0c2`
- ZH: 10 pages, SHA-256 `1fca428a9a8200637171eee82928c90c98e41d8fc54f5039b84f05a5c0b31139`

That local build established manuscript/figure/table layout correctness. The compact repository PDFs were separately structurally verified after being re-read from GitHub. These are different renderings of the same frozen manuscript, so the manifest does not falsely claim pixel identity between them.

## Why the repository PDFs use a direct PDF writer

The available GitHub connector could write UTF-8/text blobs but could not ingest a generated local binary file reference directly. A temporary GitHub Actions publisher was attempted, but this repository's Actions jobs were failing before any workflow steps executed, including unrelated existing workflows. The temporary workflow was therefore removed.

The final route writes standards-compliant ASCII PDF 1.4 syntax directly as repository blobs. This avoids an external binary-upload dependency while preserving searchable text, vector graphics and durable Git history.

## Canonical sources
- `manuscript/working_paper_en.md`
- `manuscript/working_paper_zh.md`
- `figures/fig1_pipeline.svg`
- `figures/fig2_bundle_jaccard.svg`
- `figures/fig3_mechanism_map.svg`

Do not hand-edit the PDFs to change scientific claims; update a future versioned manuscript instead.
