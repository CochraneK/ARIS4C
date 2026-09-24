# ARIS4C021 · 99-control identity lock v0.1

## Result

The Williams non-genocide control count is now reproduced without arbitrary deletion.

Starting from the public PITF-2014 country-year panel:
- reconstruct consolidated instability episodes using the official <=5-year consolidation rule;
- retain apparent starts in 1955–1998;
- exclude consolidated episodes containing genocide/politicide.

This initially yields **102** controls.

Three are artifacts of left truncating the annual panel at 1955:

| Panel artifact | Historical consolidated onset |
|---|---|
| Colombia 1955–1960 | Colombia began 1948 |
| Cuba 1955–1961 | Cuba began 1952 |
| Iran 1955 | Iran began 1953 |

The older GMU consolidated-event archive explicitly records those pre-1955 onsets.

Therefore:

**102 - 3 left-truncated pre-1955 events = 99 controls**

which exactly matches Williams 2016.

## What is locked

WILLIAMS_NEGATIVE_CASES_IDENTITY_V1.csv freezes the 99 control identities at the country/event level.

## What is not yet locked

The full historical timing/coding matrix is not frozen because later PITF versions changed some dates. Therefore:
- case identity: sufficiently reconstructed for the next stage;
- exact old-version month/year boundaries: still under audit;
- six condition values: still under reconstruction;
- CONDITION_MATRIX_V1.csv: not yet frozen.

No condition result may be interpreted until the timing/coding crosswalk is complete.
