# ARIS4C021 · Case-universe reconstruction v0.3

## Published target

Williams 2016 analyzes:

- **40 genocide cases**
- **99 non-genocide PITF instability cases**
- **139 total cases**

## Positive cases · PASS

The 40 genocide identities are taken directly from Williams's published case list.

Independent cross-check against IBM's transformed SystemicPeace/PITF annual genocide series finds:
- 40/40 positive cases overlap at least one positive annual death-magnitude observation;
- episode identity is strongly corroborated;
- episode boundaries must not be reconstructed as simple consecutive runs of annual DEATHMAG > 0.

Canonical positive seed:
- data/WILLIAMS_POSITIVE_CASES_SEED.csv

## Negative controls · 102 -> 99 resolved

A reproducible reconstruction from the public PITF-2014 country-year panel initially yields **102** apparent non-genocide consolidated episodes beginning in 1955–1998.

The difference from Williams's published 99 is explained by three **left-truncation artifacts**. Restricting the annual panel to 1955 makes three older consolidated episodes look as though they began in 1955:

| Apparent 1955 candidate | Older consolidated onset |
|---|---:|
| Colombia | 1948 |
| Cuba | 1952 |
| Iran | 1953 |

These are not new post-1955 control onsets and are therefore excluded.

**102 - 3 = 99**, exactly matching Williams.

The exclusion rule is substantive and temporal; it was not chosen to improve condition margins or QCA fit.

Canonical audit artifacts:
- data/WILLIAMS_NEGATIVE_CANDIDATES_V0.csv
- data/LEFT_TRUNCATION_EXCLUSIONS_V1.csv
- data/WILLIAMS_NEGATIVE_CASES_IDENTITY_V1.csv
- code/validate_control_identity.py

## Combined identity lock

data/CASE_UNIVERSE_IDENTITY_V1.csv contains the full **40 + 99 = 139** identity frame.

Identity is now frozen at the case/event level.

## What identity lock does NOT imply

The six-condition matrix is not yet reconstructed.

Later PITF vintages changed some dates/type boundaries relative to the older Williams-era consolidated list. Therefore:
- positive Williams dates are publication-anchored;
- negative identities are stable;
- some exact old-vintage negative dates remain provisional/cross-version;
- retrospective P/W coding cannot silently use later-vintage dates.

## Condition reconstruction boundary

Directly substituting later public elite-characteristics data does not reproduce Williams's published I/S margins. Williams also used qualitative/manual coding.

Therefore:
- R track reconstructs Williams's historical procedure and manual judgments where recoverable;
- M track uses explicitly version-pinned reproducible modern rules;
- published marginal totals and QCA solutions are validation targets, never imputation targets.

See:
- process/WILLIAMS_CODING_PROTOCOL.md
- process/CONDITION_RECOVERY_AUDIT.md
- process/CONDITION_MATRIX_CONTRACT.md
- data/CONDITION_MATRIX_V0.csv

## Next gate

Recover condition evidence case-by-case, quantify unresolved/manual cells, compare reconstructed margins to the published targets without tuning, then freeze CONDITION_MATRIX_V1.
