# ARIS4C021 · Williams Positive-Case Cross-check v0.1

Date: 2026-09-24

## Result

The 40 Williams 2016 genocide-positive analysis cases were compared against IBM's public transformed SystemicPeace/PITF annual genocide series (derived from PITF GenoPoliticide 2017).

Cross-check result:
- 40 / 40 included Williams positive cases have at least one overlapping country-year with IBM `SP.GE.MAG.DEATH > 0`;
- 33 / 40 have positive death-magnitude values across every year of the Williams-labeled episode;
- 7 / 40 contain one or more zero-death-magnitude years inside the broader labeled episode.

The seven partial-coverage cases are:
- Burundi 1965–1973: missing 1966, 1968;
- DR Congo 1964–1965: missing 1965;
- El Salvador 1980–1989: missing 1989;
- Indonesia 1975–1992: missing 1988, 1991;
- Iran 1981–1992: missing 1987;
- Iraq 1963–1975: missing 1967, 1970, 1971;
- Rwanda 1963–1964: missing 1964.

## Interpretation

This strongly supports the identity/year integrity of the 40-case positive seed.

It also demonstrates that **episode boundaries are not equivalent to a simple run of annual DEATHMAG>0 values**. Therefore:
- do not reconstruct genocide episodes merely by grouping consecutive positive annual death-magnitude years;
- preserve published case/episode boundaries from the source literature;
- use annual SystemicPeace values as a cross-check, not as the sole episode-construction rule.

## Provenance boundary

IBM's transformed dataset is a third-party processed representation of PITF data, pinned at IBM commit:
`5047c748b60b3f7c3621e0174200007865cc2933`.

It is not a replacement for the official PITF workbook or the Williams case-level condition matrix.
