# ARIS4C 000 · Pre-delete checkpoint · 2026-09-21

**Purpose:** deletion-safe recovery point for the saturated controller chat **`000ARIS4C001`**.  
**Canonical rule:** Git is the source of truth. This file is an index of decisions and entry points, not a duplicate scientific truth store.

## 1. Portfolio controller / continuity

- Human-facing controller: **000**.
- Git-resident controller: **`000/`**.
- A new agent/account/computer should start at `000/README.md`, then enter the selected paper via its own `handoff/README.md`.
- Primary activity states: **Finish / Active / Wait / Block**.
- Scheduling policy: **completion-first**.
  - Continue genuine Active work first.
  - When additional real execution capacity is available, choose the highest-progress Wait paper.
  - Block is excluded until its dependency can be cleared.
  - Finish is skipped unless explicitly reopened.
- Active WIP is **adaptive**: default 1, 3 is only a soft reference, no fixed hard maximum.
- Inside 000, keep one conceptual `CURRENT PAPER` at a time to avoid scientific-context mixing.
- **Checkpoint before switch:** a substantive bounded unit is not complete until canonical files + handoff are updated and committed.
- Visible author name: **Cochrane Kang**.

Canonical files:
- `ARIS4C_OPERATING_MODEL.md`
- `ARIS4C_STATUS_MODEL.md`
- `papers/dashboard.json`
- per-paper `paper.json`, `process/`, scientific artifacts, and `handoff/`

## 2. Current portfolio snapshot

At this checkpoint the canonical dashboard contains **19 projects: 001–019**.

Current counts at checkpoint creation:
- Finish: 2
- Active: 6
- Wait: 4
- Block: 7

Do not treat the counts in this checkpoint as live truth after future changes. Re-read `papers/dashboard.json`.

## 3. Language-series numbering

The global ARIS4C ID and the thematic language-series ID are separate:

- **ARIS4C-002 · LING-01** — completed predecessor testing the simple global-circle / periodic-language geometry hypothesis.
- **ARIS4C-017 · LING-02** — conceptual successor testing predictive structure over held-out, missing, extinct-proxy, and unrealized typological configurations.

Rules:
- Never renumber stable global IDs.
- Do not rewrite 002 into 2.1.
- Domain-series lineage is canonical in `papers/series.json`.
- 017 must preserve 002's negative result; it does not assume a global circle.
- For 017: held-out observed languages/configurations are primary; empty-space claims are downstream; extinct-language claims require independent historical evidence.

## 4. Public Research Command Center · current approved behavior

### Hero layout

The homepage hero is a **two-column desktop component**:

- **Left:** ARIS4C portfolio identity, summary, state metrics, portfolio progress.
- **Right:** today's progress curve.
- On narrower screens the columns stack responsively.

This layout is preferred over a full-width progress chart because the full-width chart looked too stretched.

### Today's progress curve

The curve is a management visualization, not a scientific result.

Current rules:
- calendar day follows **Asia/Shanghai**;
- show the current day only;
- multiple visible paper series share the same chart;
- **Finish is hidden from the curve only**, not from the rest of the public portfolio;
- unchanged-today projects are hidden from the curve to reduce visual noise;
- long idle gaps are compressed with explicit break/disclosure markers;
- unused Y-percentage ranges may be omitted with disclosed axis-break marks and anti-exaggeration minimum span;
- public portfolio navigation/cards remain complete;
- generated HTML contains a static checkpoint summary, so it must never remain stuck at “Loading today's history…”;
- `command-center.js` and `command-center.css` use content-hash cache busting to prevent stale HTML/JS mismatches.

Canonical implementation:
- `tools/sync_progress_history.py`
- `tools/build_papers_index.py`
- `docs/command-center.js`
- `docs/command-center.css`
- generated `papers/progress_history.json`
- generated `docs/index.html`

### Public project cards

- All projects → rolling research showcase.
- Finish / Active / Wait / Block → detailed cards.
- Search → detailed cards.
- Public card paper actions remain **English / 中文** only.
- Figures/tables/pipeline/source remain backend metadata and are not deleted merely because public cards hide them.

## 5. Finish paper “one-page visual” rule

Every project that reaches **Finish** must expose one visual that explains the whole paper at a glance.

Current implementation:
- declared in `paper.json -> outputs.one_page_visual`;
- full asset lives under `docs/assets/paper-at-a-glance/`;
- README table adds a rightmost **一图读懂 / At a glance** column;
- preview reuses the **same original one-page visual**, not a separately redesigned mini-thumbnail;
- README preview height is **80 px**, uses `loading="lazy"` and `decoding="async"`, and clicking opens the full image;
- current 001/002 WebP assets are small enough that this has negligible page-load cost;
- the old custom SVG mini-previews were removed.

Finish output gate requires the one-page visual itself; it does **not** require a separately designed thumbnail.

Canonical implementation:
- `ARIS4C_OUTPUT_STANDARD.md`
- `tools/build_readme.py`
- `tools/audit_paper_outputs.py`
- `papers/001-gca-bees/paper.json`
- `papers/002-language-geometry/paper.json`

## 6. README / Page continuity

- `README.md` is the Chinese-default landing page.
- `README.en.md` is the English mirror.
- README/Page are generated surfaces; edit generators/canonical metadata first.
- The portfolio can grow beyond a hard-coded paper count; audits should derive the paper set from manifests/dashboard rather than assume 16/17 papers.
- Git-resident 000 is explicitly exposed as the takeover entry for other agents.

## 7. Safe deletion of the chat

Retiring chat: **`000ARIS4C001`**.\n\nThis chat is not required for project recovery once this checkpoint and the associated canonical files are on `main`.

A new executor should:

1. read `000/README.md`;
2. read `000/AGENT_HANDOFF.md`;
3. read `papers/dashboard.json`;
4. consult this checkpoint for the UI/continuity decisions from the retiring chat;
5. select the next paper according to the current dashboard + operating model;
6. enter that paper through its `handoff/README.md`.

Do not reconstruct current scientific state from this checkpoint when a newer per-paper canonical file exists.
