# ARIS4C019 · Final Public-Delivery Audit

**Audit date:** 2026-09-24  
**Scientific package:** PASS  
**Submission package:** PASS  
**Public manuscript sources:** PASS  
**Canonical public PDF publish:** PENDING

## Canonical source checks

- English source exists: `manuscript/WORKING_PAPER_EN.md`.
- Chinese source exists: `manuscript/WORKING_PAPER_ZH.md`.
- Four manuscript SVG masters exist and are linked from both public manuscripts.
- `tools/build_public_pdfs.py` includes ARIS4C019 EN/ZH builds.
- `.github/workflows/build-public-pdfs.yml` watches ARIS4C019 manuscript/figure changes and validates generated PDFs.

## Independent local build reproduction

A local reproduction of the repository public-PDF contract was run using the canonical Markdown, publication CSS and four committed SVG figure masters.

Machine checks:

- English: **12 pages**, >80 KB after PDF optimization, extractable text on the first two pages.
- Chinese: **7 pages**, >180 KB after PDF optimization, extractable text on the first two pages.
- Both exceed the repository workflow's minimum-page and minimum-text sanity checks.

Render-first visual QA:

- English title page: PASS.
- Chinese title page: PASS; no broken CJK glyphs / tofu blocks.
- English figure page: PASS; no clipping or overlap.
- Chinese figure page: PASS; no clipping or overlap.
- Page footers and pagination render correctly.

## Canonical repository check

As of this audit, the required main-branch files are still absent:

- `docs/paper/019/en/main.pdf`
- `docs/paper/019/zh/main.pdf`

A watched no-op builder revision was committed to trigger the canonical workflow:

- commit: `dc857f638517a25b7cb5b3b70284dd4aa6955682`
- message: `ci: trigger canonical public PDF build for 019 final gate`

No GitHub Actions bot PDF commit has appeared yet.

## Decision

Do **not** promote ARIS4C019 to Finish / 100% until the two canonical PDF paths exist on `main` and are re-read from GitHub.

This is an engineering/public-delivery blocker only. It does not reopen:

- event selection;
- Life Ladder outcomes;
- Israel holdout interpretation;
- legal audits;
- manuscript scientific claims;
- SIR submission package.

## Finish condition

When both canonical PDFs exist:

1. verify each file is readable and nontrivial;
2. record Git blob SHA(s);
3. update `paper.json` PDF status to complete;
4. update `process/STATUS.md` to repository output gate PASS;
5. set dashboard progress to **100**, activity to **finish**;
6. sync handoff/session log and regenerate the portfolio index if needed.
