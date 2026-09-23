# SIR final blinded document visual QA

**QA date:** 2026-09-23  
**Status:** **PASS**

## Canonical input lock

- Blinded manuscript Git blob: `d15ee7b66b2c994fad33a4d759114aaeaa1d189b`
- Blinded manuscript SHA-256: `e9441bcb7ffa1a1c822f12ea00606be1b5c0e913240d3a6c498acb1f9b5c1b90`
- Figure 1 Git blob: `ed5d4ffe1f7a8f13f837af00a509213a067b702b`
- Figure 2 Git blob: `c6975c1a0c822a82f0d82202a7b1006b062af2cb`
- Figure 3 Git blob: `93136ffc70bc3508eeb7ff5bf57c946e36873dac`
- Figure 4 Git blob: `b84bcf530e74574c62542167c49bb1b580afe656`

The final binaries were rebuilt after the latest Data and Code Availability edit. Scientific results, event admission, outcome definitions, and interpretation were not reopened during packaging.

## Machine QA

- PDF pages: **34**
- Embedded figures: **4/4**
- Figure-caption references: **4/4**
- Estimator equation: **PASS**; no raw LaTeX placeholder/control-string leakage
- Blinded identity scan across DOCX XML and extracted PDF text: **PASS / 0 hits**
- DOCX accessibility audit: **0 high / 0 medium / 0 low findings**
- DOCX-rendered PDF versus reviewer PDF: **34/34 pages pixel-identical at 100 dpi; changed pages = 0**
- Final DOCX SHA-256: `bc8469ac22fd1a5bd8e92e099ba2f94aed25d4568ae13efa14aa95494549b4ed`
- Final reviewer PDF SHA-256: `e074201092e78961aaf8285e2e11cd58e1329b9c53eddaf6b8f2b62e919714ab`

## Page-by-page visual inspection

All **34 pages** of the latest DOCX rendering were inspected after the anonymity-metadata fix.

PASS checks:

- no clipping or off-page text;
- no overlapping paragraphs, figures, captions, or footer page numbers;
- no blank or duplicate pages;
- title, abstract, headings, references, Data and Code Availability, and Online Resource 1 are readable;
- all four figures are legible and paired with the correct caption;
- Fig. 1 Bahrain outlier annotation is visible;
- Fig. 2 legal-isolation funnel is legible;
- Fig. 3 Israel event-time panel and transition band are visible;
- Fig. 4 reference-year sensitivity bars and labels are visible;
- the centered estimator equation renders correctly;
- references fit within page boundaries.

Nonblocking formatting note: Markdown bullet lists render as separated list lines without bullet glyphs in the current Pandoc/Word style. This is consistent, readable, and does not alter content.

## Anonymity fix recorded

The first final-source rebuild exposed a temporary local project path in `pic:cNvPr/@descr` inside DOCX image metadata. The visible manuscript and PDF text were already anonymous, but the hidden DOCX metadata failed the identity scan. The canonical builder now overwrites both `wp:docPr` and `pic:cNvPr` picture metadata with neutral figure names/alt text. The rebuilt package passes the full identity scan.

## Online Resource 1 lock

- Artifact commit: `c0492aab9bcb508a58d9cd745af3f4ef6b2354b9`
- ZIP: `SIR_Online_Resource_1_Anonymous_Replication.zip`
- SHA-256: `8463e216e4c49dea30ee47773a55326e6830ed8a0735295770eeff3239f5ad07`
- Identity scan: **PASS**
- Headline number-lock reproduction: **PASS**

Reviewers should receive the ZIP uploaded through the journal portal, not a repository/branch URL.
