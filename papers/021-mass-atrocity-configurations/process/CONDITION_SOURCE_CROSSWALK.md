# ARIS4C021 · Williams Condition Source Crosswalk v0.1

Date: 2026-09-24
Status: frozen acquisition/coding plan before condition-value inspection

## Goal

Recover the six Williams crisp-set conditions A/P/W/I/S/E for the candidate 139-case frame while separating:
- exact historical replication inputs;
- independently reconstructed inputs;
- time-safe sensitivity inputs;
- modern sensitivity inputs.

## A · Autocracy

### Published Williams rule
Primary source: Polity IV annual time series 1800–2011, with Freedom House 1973–2013 used for cases where Polity coding does not permit a clear democratic/autocratic classification.

### Historical replication target
Recover a Polity IV vintage contemporary to Williams (2011/2012), not a current revised series.

### Validation
Published Williams margins:
- genocide A=1: 38/40
- controls A=1: 69/99
- total A=1: 107/139

### Sensitivity
A modern/revised Polity or V-Dem-derived autocracy variable may be analyzed separately but may not overwrite A_R.

## P · Political upheaval

### Published Williams rule
High if:
- Polity range over the conflict >= 10, OR
- Harff upheaval maximum >= 30.

Low if Harff upheaval < 15.
Intermediate Harff values 15–30 were qualitatively assessed by Williams.

### Replication risk
This can use values observed after genocide onset.

### Required dual coding
- P_R: published retrospective replication procedure.
- P_T: time-safe version using only information observable before/on frozen prediction date.

Published margin:
- 25/40 positives
- 31/99 controls
- 56/139 total

## W · War

### Published Williams rule
Source: UCDP/PRIO Armed Conflict Dataset v4-2012, 1946–2011.
W=1 if the case is classified as war in any year of the case.

Official historical download endpoint verified:
https://ucdp.uu.se/downloads/replication_data/2012_c_666956-l_1-k_ucdp_prio_armedconflict-dataset_v4_2012.xls

### Required dual coding
- W_R: any-year-in-case replication rule.
- W_T: only war status observable before/on prediction date.

Published margin:
- 26/40 positives
- 54/99 controls
- 80/139 total

## I · Exclusionary ideology

### Published Williams rule
Primarily inherited from Harff model data, supplemented by Williams qualitative coding when unavailable.

Published margin:
- 25/40 positives
- 22/99 controls
- 47/139 total

### Recovery rule
Do not infer I automatically from regime type, ethnicity, or conflict.
Recover Harff/Williams coding or perform blinded source-based recoding with explicit provenance and reliability review.

## S · Elite ethnicity salient

### Published Williams rule
Based on Harff's ethnocultural-character information, modified by Williams into a dichotomy:
- ethnicity salient in politics = 1
- ethnicity not salient = 0

It does not preserve Harff's majority/minority distinction.

Published margin:
- 32/40 positives
- 45/99 controls
- 77/139 total

### Recovery rule
Do not infer salience from national ethnic diversity alone.
Prefer original Harff coding; otherwise use an explicit historical elite-ethnicity coding protocol.

## E · Economic autarky

### Published Williams rule
Source: World Bank national-accounts trade data.
Operationalization: trade (imports + exports) as percentage of GDP.
Threshold: below the published world average of approximately 33% for the 1960–1998 frame = economically autarkic.

Current World Bank indicator corresponding to the construct:
NE.TRD.GNFS.ZS · Trade (% of GDP)

### Vintage issue
Current WDI historical values can be revised relative to the values available to Williams.

Therefore:
- E_R: recover Williams-era data/vintage where possible.
- E_C: current WDI reconstruction as sensitivity.

Published table margins:
- 18/40 positives
- 22/99 controls
- table-implied total 40
Published prose says total 41; this discrepancy is already frozen in PUBLISHED_REPLICATION_TARGETS_V1.json.

## Priority order

1. W_R / W_T — exact historical UCDP version is publicly archived.
2. A_R — recover Polity IV 2011/2012 vintage and Freedom House supplement.
3. E_R/E_C — recover historical WDI vintage if possible; current WDI sensitivity is straightforward.
4. P_R/P_T — requires Polity plus Harff upheaval data.
5. I_R and S_R — highest dependence on Harff/Williams original coding; do not manufacture from proxies.

## Acceptance rule

A reconstructed condition is promoted to the canonical CONDITION_MATRIX_V1 only when:
- source/version is pinned;
- case-to-country mapping is auditable;
- coding procedure is deterministic or adjudicated;
- published marginal counts are compared;
- mismatch is documented rather than tuned away.
