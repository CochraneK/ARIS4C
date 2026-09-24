# ARIS4C 000 · Session Log

## 2026-09-19 · Controller handoff created

- Added a dedicated Git-resident 000 command-center entry point.
- Bound 000 to the repository operating model and four-state status model.
- Recorded completion-first scheduling and checkpoint-before-switch as controller rules.
- Established that new agents should read 000 first, then enter the selected paper through its `handoff/` package.


## 2026-09-19 · Pre-delete controller checkpoint

- Re-read live `main`, recent commits, `papers/dashboard.json`, 000 controller files, and representative paper handoffs.
- Verified portfolio now contains **17 papers (001–017)**.
- Verified current primary state snapshot: Finish 001/002; Active 003/015; Wait 006/007/008/009/011/012/014/017; Block 004/005/010/013/016.
- Verified the public Research Command Center split-view behavior is already committed on main:
  - All projects → rolling marquee;
  - Finish/Active/Wait/Block → detailed cards;
  - search → detailed cards;
  - Hero summary → All only;
  - public paper actions → English / 中文 only.
- Verified representative handoff snapshots for 004, 011, 014, 015, 016 and 017 are synchronized to current dashboard state.
- Added `PRE_DELETE_CHECKPOINT_2026-09-19.md` as the deletion-safe recovery point.

## 2026-09-19 · Command-center visibility correction

- User clarified that Finish and no-progress-today projects should be hidden **only from the time progress curve**, not from the rest of the command center.
- Removed the accidental global `0 < progress < 100` filtering from the portfolio generator.
- Restored Finish navigation, Finish legend/overview counts, and complete All-projects showcase/card visibility.
- Changed today's chart payload to include only non-Finish projects with an actual percentage change across today's checkpoints.
- Hardened command-center JS so theme/storage/chart/showcase failures cannot prevent navigation, Reset, search, sorting, or other controls from receiving listeners.
- Added CI audit for complete portfolio visibility, chart-only filtering, control presence, and JavaScript syntax.

## 2026-09-19 · Daily progress idle-gap compression

- Replaced the linear wall-clock x-axis with an adaptive discontinuous axis for the daily progress chart.
- Long inactivity is detected relative to the day's normal checkpoint cadence, not by one fixed arbitrary threshold.
- Compressed gaps retain explicit dashed break markers, `//`, real idle duration, and real-time tooltip provenance.
- Added CI audit tokens so accidental removal of the compression/disclosure mechanism fails the command-center audit.

## 2026-09-19 · Adaptive vertical progress range

- Added an adaptive Y-axis to the daily progress chart so unused percentage ranges no longer flatten meaningful movement.
- Kept at least a 20-point visible range as an anti-exaggeration guard.
- Added Y-axis break marks plus an explicit visible Y-range in the chart summary whenever 0–100% is truncated.
- Extended command-center CI audit to require the adaptive-axis safeguards.

## 2026-09-21 · Fixed stale daily progress date

Root cause:
- Build workflow had no scheduled trigger.
- The command center derived "Today" from the latest dashboard commit date, so an idle day could keep showing yesterday.
- A first progress change after midnight could not be identified with only one same-day checkpoint.

Fix:
- Added a daily GitHub Actions schedule at 16:05 UTC (00:05 Beijing).
- Bound the daily chart to the real current `Asia/Shanghai` date.
- Added a prior-state midnight baseline only when today's first checkpoint exists.
- Added CI freshness/timezone assertions.
- Verified generated public payload now reports `2026-09-21`.

## 2026-09-21 · Deletion-safe chat checkpoint

- Re-read the live 000 controller files, dashboard, output standard, README/Page generators, chart JavaScript/CSS, and 001/002 visual metadata before retiring the chat.
- Verified the canonical dashboard currently contains 19 projects (001–019).
- Verified the approved compact homepage layout is already implemented: hero left = portfolio summary, hero right = today's progress chart, responsive stack on smaller screens.
- Verified Finish-paper README previews now reuse the original one-page WebP at 80 px with `loading="lazy"` and `decoding="async"`.
- Verified the temporary custom SVG mini-thumbnails are no longer present.
- Verified Finish output audit requires the one-page visual but not a separate thumbnail.
- Added `PRE_DELETE_CHECKPOINT_2026-09-21.md` and linked it from 000 README/agent handoff.
- No scientific paper state was rewritten from chat memory; current paper state remains owned by dashboard + per-paper canonical files.

## 2026-09-24 · Portfolio re-audit after 023 registration

- Re-read canonical `papers/dashboard.json`, current manifests, controller snapshot, public Command Center, README and recent GitHub Actions.
- Canonical dashboard contains 23 projects (001–023). All 23 canonical paper folders have the full 8-file handoff package.
- Historical `018-drosophila-open-simulation` is intentionally retained for provenance with `portfolio_visible:false` and `superseded_by`; canonical 018 is `018-drosophila-neural-simulation`.
- Hardened the Command Center generator so only dashboard-member visible manifests are loaded, with missing/duplicate visible IDs treated as errors.
- Hardened the Command Center audit to use the same canonical visible-paper set.
- Refreshed `000/STATUS.md` manually from the current dashboard because automated controller generation is not currently executing.
- Public generated surfaces are stale: `docs/index.html` still shows 22 papers through 022 and Today's date 2026-09-23; README also still reports 22 papers. 023 is present in canonical Git but has not been regenerated onto those surfaces.
- GitHub Actions are currently failing before runner steps begin across multiple independent workflows (paper index, handoff sync, public PDFs and 021 contract). A manual rerun reproduced the same zero-step failure. This localizes the immediate automation fault to runner/account/platform execution rather than a repository test failure, but the exact account-side cause is not exposed by the available connector.
- 019 canonical public PDFs remain absent from `docs/paper/019/en/main.pdf` and `zh/main.pdf`; its scientific work is complete but publication remains engineering-blocked.

## 2026-09-24 · 023 calibration gate closed; portfolio queue refreshed

- 023 completed the dual-AI calibration gate and is no longer blocked on coding independence: `coder_A.csv` (GLM substitute) and `coder_B.csv` (DeepSeek) both frozen at 120/120 judgments, `reliability.json` produced only after both were committed (four-state raw agreement 0.825; binary present/absent subset n = 103, raw 0.951 / kappa 0.894 / AC1 0.911; 21 disagreements).
- Ontology v0.1 freezes with a mandatory six-rule v0.1.1 amendment layer before expansion to 56 motifs; the disagreement taxonomy and reliability decision are committed under `papers/023-myth-convergence/process/`.
- Canonical `papers/dashboard.json` updated: 023 moved **Block 55 → Wait 70**, which returns it to the completion-first Wait pool (its next unit — v0.1.1 amendments, a replacement Sumerian anthropogony witness, the regression check and the first tradition × motif matrix — is fully executable).
- `000/STATUS.md` refreshed manually for the same reason as the previous entry: automated controller generation is still not executing.
- Continuity audit state unchanged for the rest of the portfolio: 020, 022 and 023 fail the `AGENT_HANDOFF.md` "Immediate next action" contract. 023 was repaired in this pass; 020 and 022 still need the heading added.
- Public generated surfaces (README, `docs/index.html`, progress history) remain stale for the same runner reason and were not hand-patched.
