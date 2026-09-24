# Agent Handoff · ARIS4C-023

## One-line state

**99% complete. Scientific core and the full bilingual publication package are frozen and QA'd. The only remaining Finish gate is durable/public upload of two already-generated PDF binaries. Do not reopen the science.**

## Read first
1. STATUS.md
2. TODO.md
3. ../process/PUBLIC_DELIVERY_AUDIT.md
4. ../process/PDF_BUILD_MANIFEST.md
5. ../process/CORE_FREEZE_AUDIT.md
6. ../manuscript/working_paper_en.md
7. ../manuscript/working_paper_zh.md

## Frozen core
- 24 motifs + v0.1.1 rules
- frozen A/B coding and reliability
- source-bundle comparison layer
- audited similarity pilot
- PT01–PT04 mechanism synthesis
- ancestry/contact/environment registries
- Egypt exploratory/excluded
- QCA OFF

## Publication state
- One-page visual: repository asset complete.
- EN PDF: built + QA PASS locally, 12 pages, SHA-256 aa0d39b5fa2c9c854f9013b43b3e1edfd5734bbe9b22f33a7b8b74c495afd0c2.
- ZH PDF: built + QA PASS locally, 10 pages, SHA-256 1fca428a9a8200637171eee82928c90c98e41d8fc54f5039b84f05a5c0b31139.
- PDF repository/public binary upload: pending because the current connector cannot consume a container file reference directly.

## Exact next action
Use a binary-capable surface to upload/rebuild the two PDFs, verify their renders/hashes, then:
1. add `paper_en_pdf` and `paper_zh_pdf` links in paper.json;
2. expose PDF-first links on portfolio surfaces;
3. change dashboard/STATUS to Finish 100%;
4. log the final commit and continuity audit.

Do not claim Finish or invent PDF URLs before those links actually resolve.
