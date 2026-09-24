# ARIS4C021 · Phase-1 Analytic Matrix Contract v0.1

The historical replication matrix must preserve both raw/source values and calibrated analytic values.

## Case identity

Required:
- case_id
- country
- instability_episode_start
- instability_episode_end
- outcome_gp
- outcome_onset_date
- outcome_source_ref

## Harff six-condition core

Each condition has:
- *_raw: source-scale value;
- *_set: frozen binary/fuzzy membership used by QCA/CNA;
- *_source_ref: provenance;
- *_coding_note: any judgment/crosswalk.

### H_PRIOR
Prior genocide/politicide history.

### T_UPH
Magnitude of political upheaval before the focal outcome window.

### M_IDEO
Exclusionary ideological orientation of ruling elite.

### O_AUT
Autocratic regime status.

### M_ETH
Ethnic character/salience/minority position of ruling elite.

### X_TRADE
Trade openness; any inversion to "low trade" must be explicit rather than silently changing the sign.

## Timing

All explanatory values must be temporally eligible:
- no post-onset values;
- preserve the original Harff timing when reproducing the 126-case frame;
- modern extension defaults to lagged t-1 covariates unless separately frozen.

## Missingness

Allowed values:
- observed;
- missing_source;
- ambiguous_coding;
- not_applicable.

Never impute a historical replication condition solely to make a QCA/CNA configuration complete.

## Calibration metadata

A separate calibration file must record:
- source variable;
- transformation;
- threshold/anchor;
- direction;
- theoretical justification;
- whether inherited from Williams or newly chosen;
- sensitivity grid.

## Output separation

The same frozen matrix feeds:
1. Harff-style statistical baseline;
2. QCA;
3. CNA.

Method-specific derived variables may be created downstream, but no method gets a privately recoded version of the cases without an explicit crosswalk.


## Dual timing representation

For Williams-derived conditions with retrospective coding risk, preserve two versions:

- *_R: exact-replication coding following the published Williams procedure;
- *_T: time-safe coding using only information observable at the frozen prediction date.

At minimum:
- P_R / P_T;
- W_R / W_T.

The canonical historical QCA replication uses *_R.
The leakage-safe sensitivity uses *_T.
Neither may overwrite the other.
