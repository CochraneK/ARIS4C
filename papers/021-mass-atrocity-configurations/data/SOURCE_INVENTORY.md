# ARIS4C021 · Source Inventory v0.1

## Tier A · Historical outcome / replication

### PITF State Failure Problem Set 2018

Provider: Center for Systemic Peace / Political Instability Task Force archive.

The 2018 codebook describes separate event files for ethnic war, revolutionary war, adverse regime change, and genocide/politicide. The genocide/politicide file contains 45 episodes / 289 case-years.

Landing page:
https://www.systemicpeace.org/inscrdata.html

Codebook:
https://www.systemicpeace.org/inscr/PITFProbSetCodebook2018.pdf

Use:
- reproduce historical case universe;
- identify geno-/politicide onset;
- reconstruct political-instability conditioning frame.

Status: verified public source; raw snapshot not yet vendored.

## Tier A · Modern institutional covariates

### V-Dem v16

Provider: Varieties of Democracy.

Current release checked at project creation: v16, published March 2026. Country-year data provide democracy, executive constraints, political exclusion, repression and related institutional indicators.

Landing page:
https://www.v-dem.net/data/the-v-dem-dataset/

Use:
- modern extension only;
- version-pin exact v16 files;
- never compare absolute scores across V-Dem versions without an explicit harmonization design.

Status: verified current public release; acquisition may require website form.

## Tier A/B · Modern mass-killing benchmark

### Early Warning Project

Provider: US Holocaust Memorial Museum Simon-Skjodt Center.

Use:
- secondary intrastate mass-killing onset definition;
- predictive benchmark and source-variable inventory;
- do not merge its outcome definition with PITF geno-/politicide.

Reference:
https://www.ushmm.org/genocide-prevention/blog/how-to-use-the-early-warning-projects-statistical-risk-assessment-2024

Status: methodology verified; exact machine-readable historical onset/source bundle must be pinned before analysis.

## Tier B · Atrocity-event sensitivity

### PITF Worldwide Atrocities Dataset

Public archive describes coded deliberate lethal violence against noncombatant civilians, with archived files spanning 1995–2020.

Landing page:
https://parusanalytics.com/eventdata/data.dir/atrocities.html

Use:
- sensitivity / escalation analysis;
- not a substitute for genocide/politicide onset.

Status: verified archived source; updating suspended.

## Source rules

1. Raw files are hash-pinned before transformation.
2. Outcome datasets and explanatory-condition datasets are versioned separately.
3. Retrospectively coded predictors that may depend on knowing the outcome are flagged.
4. No current-country “genocide prediction” is published from a single QCA solution.
5. Source licenses and redistribution permissions are checked before raw data are committed.


## 2026-09-24 · Phase-1 verification note

Official Systemic Peace index confirms the 1955–2018 PITF Problem Set and directly exposes the 2018 consolidated case list, genocide/politicide spreadsheet and 2018 codebook.

Historical-replication warning: the codebook documents that the genocide/politicide event list is not a continuously updated modern outcome series. Treat PITF GP as historical replication only.

See process/PHASE1_SOURCE_FREEZE.md and code/acquire_pitf.py.
