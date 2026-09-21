# ARIS4C019 · Agent takeover brief

## What this project is

**Statutory Paid Annual Leave and National Life Evaluation: A Global Legal-Event Audit and Falsification-First Holdout Study**

A cross-national longitudinal study of whether legally verified statutory paid annual-leave changes are followed by stable annual population Life Ladder changes. The project is explicitly falsification-first and separates statutory entitlement from public holidays, actual work hours and leave utilization.

## Current state

- Activity: **active**
- Progress: **68%**
- Stage: **Phase 1 bilingual working paper · interpretation lock + Israel holdout**
- English draft: `manuscript/WORKING_PAPER_EN.md`
- Chinese draft: `manuscript/WORKING_PAPER_ZH.md`

## Evidence that is already locked

1. Original eight-event panel is a broader labour/time-off stress test, not a clean annual-leave causal panel.
2. WHR2024 refresh: mean +0.088, median -0.099, 6/8 event means negative.
3. Removing Bahrain gives -0.117; Bahrain is highly influential.
4. Bounded audit of 11 additional World Bank leave jumps admits 0 clean holdouts.
5. Israel 2016 was discovered independently through outcome-blind modern legal screening and frozen before outcome inspection.
6. Israel strict-115 frozen 2015-reference mean = +0.002; pretrend warning thresholds not triggered.
7. Israel alternative post-outcome baselines are materially negative; therefore do not call the result a precise null.
8. Positive/negative affect remain locked.

## Immediate next action

**Build the publication-quality figure/table package from committed machine-readable results, then run manuscript number/claim reproducibility QA.**

Do not spend the next cycle searching for a more favorable outcome or replacing the frozen Israel reference year.

## Current blocker / gate

No engineering blocker. The scientific ceiling is identification strength: bundled historical events, population-level treatment dilution, annual outcome noise, and baseline sensitivity.

## Canonical files / entry points

- `paper.json`
- `process/PILOT0_INTERPRETATION_LOCK.md`
- `process/ISRAEL_HOLDOUT_FREEZE.md`
- `process/ISRAEL_HOLDOUT_RESULTS.md`
- `process/ISRAEL_REFERENCE_SHOCK_AUDIT.md`
- `process/MODERN_SNAPSHOT_CANDIDATE_AUDIT.md`
- `process/STATUS.md`
- `handoff/TODO.md`

## Before changing anything

1. Preserve pre-outcome and pre-holdout freezes.
2. Treat post-outcome sensitivity analyses as diagnostics, never as a new preferred specification.
3. Do not open positive/negative affect without a separately frozen secondary-outcome plan.
4. Do not use WHR2025/2026 rolling three-year ranking values as annual Life Ladder.
5. Use **Cochrane Kang** for visible author naming.
6. Do not commit secrets, credentials, hidden chain-of-thought, or unnecessary sensitive personal data.
7. After any substantive change, update canonical research files first, then continuity files.

## Handoff completion rule

Before ending a substantial session:
- update `TODO.md`;
- append material research decisions to `DECISIONS.md`;
- append a public-safe summary to `CHATLOG.md`;
- append executed/validated work to `SESSION_LOG.md`;
- verify `paper.json` and `papers/dashboard.json` agree on stage/progress.
