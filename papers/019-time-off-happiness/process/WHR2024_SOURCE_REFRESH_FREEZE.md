# ARIS4C019 · WHR 2024 Source-Refresh Analysis Freeze v0.1

**Frozen:** 2026-09-21  
**Stage:** post-unlock, pre-source-refresh effect comparison

> The original WHR2023 Life Ladder analysis has already been inspected. This freeze governs only the *new source-refresh comparison* and is written before any WHR2024-mirror treatment estimate is run.

## 1. Purpose

If the pinned WHR2024 annual mirror passes `WHR2024_MIRROR_VALIDATION.md`, quantify separately:

1. **release-revision effect** — whether the WHR2024 release revises historical 2005–2022 Life Ladder values relative to the frozen WHR2023 workbook;
2. **follow-up extension effect** — what changes when 2023 observations are added on top of the WHR2024 historical release.

Do not combine these two mechanisms into one unexplained “new result”.

## 2. Frozen event set

Use exactly the original 8 Tier-A headline events:

- Bahrain 2012
- Canada 2019
- China 2008
- Croatia 2010
- Kosovo 2010
- Kuwait 2010
- Luxembourg 2019
- Taiwan 2017

No event may be added, removed, promoted or demoted based on WHR2024 outcomes.

The new stand-alone holdout registry is **not** opened by this source-refresh analysis.

## 3. Frozen donor set

For the strict comparability analysis, use the exact clean-donor lists already frozen in `data/pilot0_donor_diagnostics.csv`.

Do not re-select donors using WHR2024 Life Ladder values.

A separate availability-only donor refresh may be reported later, but it must be labelled as such and cannot replace the strict comparison.

## 4. Three analysis panels

Run the same transparent donor-adjusted estimator on three panels:

### A. Frozen benchmark

- WHR2023 annual panel, 2005–2022.
- This is the already-published Pilot-0 benchmark.

### B. WHR2024 release, common horizon

- WHR2024 validated annual mirror.
- Restrict outcomes to <=2022.
- Same event set, event clock, transition-year exclusions and donor lists as A.

**B − A** estimates the effect of historical source-version revisions / rounding / updated release construction.

### C. WHR2024 release, extended horizon

- Same validated WHR2024 mirror.
- Permit 2023.
- Same event set, event clock, transition-year exclusions and donor lists.

**C − B** isolates the effect of adding 2023 follow-up observations.

Because the frozen event window is T-4…T+4, the new year is relevant principally to later reforms such as Canada/Luxembourg 2019; it must not create post-window evidence for older events.

## 5. Required outputs

Report:

- event-specific full-post summaries for A, B, C;
- pooled mean and median for A, B, C;
- event-level `B-A` and `C-B`;
- whether sign changes occur;
- leave-one-event-out comparison under C;
- pre-placebo diagnostics under B/C using the same frozen thresholds;
- counts of contributing post years for every event.

## 6. Interpretation

A source-refresh result may be described as:

- stable to release revision;
- sensitive to release revision;
- sensitive to added 2023 follow-up;
- or both.

It must **not** be described as an independent replication, because B/C use the same underlying Gallup/WHR measurement system.

## 7. Holdout firewall

Do not print, plot, rank or estimate treatment effects for Mexico 2023, New Zealand 2007, Malta stages, or any other post-unlock stand-alone reform candidate as part of this source refresh.

Candidate admission still requires the rules in `STANDALONE_LEAVE_HOLDOUT_REGISTRY.md`, including >=2 pre and >=2 full-post observations and legal-isolation review.

## 8. Secondary outcomes

Positive affect and Negative affect remain locked.
