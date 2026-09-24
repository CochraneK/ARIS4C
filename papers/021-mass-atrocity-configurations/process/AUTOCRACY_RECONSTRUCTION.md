# ARIS4C021 · Autocracy A reconstruction · Polity precursor v0

## Frozen source

A historical Polity IV 2012 CSV was recovered from a public replication repository:

- repository: `CommonEconomist/replications`
- pinned commit: `1ad6a9cf5086a29dc2ef84d6ad468fe969570813`
- path: `historical-conflict/raw_data/p4v2012.csv`
- Git blob SHA: `66acf371aa695b458e5a5a07464b200bf71a8743`

This mirror is a historical-vintage source cross-check, not a claim that the mirror is the canonical Polity distributor.

## Target-blind precursor rule

For every frozen Williams case:
1. use the case start year only;
2. read raw `POLITY`;
3. if POLITY is a substantive -10..10 score, set `A_polity_only=1` for -10..0 and 0 otherwise, following the Harff-autocracy code independently reproduced in Jay Ulfelder's 2014 USHMM risk-model scripts;
4. if POLITY is -66, -77, or -88, leave A unresolved;
5. do not replace special values with the nearest convenient year;
6. do not use Williams's published A margins to fill cases.

## Result

The precursor contains:
- 139/139 case identities resolved to the Polity vintage;
- 115 direct substantive start-year Polity scores;
- 24 special start-year Polity codes requiring reassessment;
- 87 directly observed A=1 cases: 26 genocide + 61 controls.

Williams reports 107 A=1 cases: 38 genocide + 69 controls. The gap is **not** filled here.

This is expected because Williams explicitly says the Polity classification was reassessed with Freedom House, rather than being a raw POLITY threshold alone.

## Important inference constraint

The published pathways independently imply that some cases with a non-autocratic raw start-year Polity score were ultimately coded A=1 in Williams. For example, Sudan 1956 and Uganda 1980 appear in the published `A*S*P` path, while their raw p4v2012 start-year POLITY scores are positive.

Therefore:
- `A_polity_only` is a precursor, not `A_R`;
- Freedom House reassessment must be recovered explicitly;
- no row is to be flipped merely to hit 107/38/69.

Canonical machine-readable artifacts:
- `data/A_POLITY2012_PRELIM_V0.csv`
- `data/A_POLITY2012_PRELIM_V0.json`
