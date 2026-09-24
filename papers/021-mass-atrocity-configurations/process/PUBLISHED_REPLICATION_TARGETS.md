# ARIS4C021 · Published Replication Targets v1

Status: frozen before reconstruction of the case-level matrix.

This document separates **published target facts** from any future ARIS4C021 estimates.

## Harff 2003 target

Harff's final structural model uses 35 geno-/politicide problems and 91 controls (126 total). The model reports c = 0.83 and classifies 26/35 genocide cases and 66/91 non-genocide cases correctly at the reported threshold.

Published six-variable direction:
- more prior political upheaval -> higher risk;
- prior genocide -> higher risk;
- exclusionary elite ideology -> higher risk;
- autocracy -> higher risk;
- ethnocultural minority elite -> higher risk;
- trade openness -> lower risk.

The exact published coefficients / odds ratios are stored in data/PUBLISHED_REPLICATION_TARGETS_V1.json.

## Williams 2016 target

Williams uses:
- 40 genocide cases;
- 99 non-genocide political-instability cases;
- 139 total cases.

Published marginal condition counts:

| Condition | Genocide | Non-genocide | Total |
|---|---:|---:|---:|
| A · Autocracy | 38 | 69 | 107 |
| P · Political upheaval | 25 | 31 | 56 |
| W · War | 26 | 54 | 80 |
| I · Exclusionary ideology | 25 | 22 | 47 |
| S · Salient elite ethnicity | 32 | 45 | 77 |
| E · Economic autarky | 18 | 22 | 40 |

Williams's intermediate QCA solution:

A*S*I + A*S*P + A*I*E*P*~W + A*I*E*~P*W + S*~I*E*P*W

Published overall:
- coverage = 0.750;
- consistency = 0.769;
- 39 cases predicted positive;
- 30 true positives;
- 9 false positives.

The project will not call a reconstruction successful merely because it produces a qualitatively similar formula. It must satisfy the machine-readable target contract within prespecified tolerance.

## Important conceptual correction

Williams calls autocracy approximately/quasi-necessary because it appears in 38/40 genocide cases, not because it is literally perfectly necessary. ARIS4C021 will preserve that distinction.

## Provenance

Harff:
DOI 10.1017/S0003055403000522

Williams:
DOI 10.5038/1911-9933.9.3.1306

The machine-readable target file is the canonical replication-test contract.
