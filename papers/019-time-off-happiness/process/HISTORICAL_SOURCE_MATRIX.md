# ARIS4C019 · Historical source matrix v1.0

## Exposure / institutional sources

| source | time depth | geography | construct | use | caveat |
|---|---|---|---|---|---|
| ILO NORMLEX C052 | 1936 convention; ratifications thereafter | ILO members | holidays with pay standard / ratification dates | institutional diffusion anchor and candidate reform discovery | ratification date is not automatically national entitlement adoption |
| ILO NORMLEX C132 | 1970 convention; in force 1973; ratifications thereafter | ILO members | revised paid annual leave standard, sometimes declared leave length | institutional diffusion + legal cross-check | adoption/implementation law still requires country verification |
| ILO/NATLEX national legislation | historical | global where indexed | labor-law text / effective dates | primary legal reconstruction | heterogeneous digitization and language |
| WORLD Policy Analysis Center | 2015/16 snapshot | 193 UN members | annual leave + weekly rest | modern global cross-section / candidate comparison | snapshot, not long-run panel |
| Equal Futures | 2026 snapshot | 193-country framework | annual leave / right to rest | modern refresh / candidate discovery | snapshot differences are not automatically reforms |
| World Bank Employing Workers / Doing Business legacy | modern historical years | broad global | leave-days screening fields | discontinuity screening / corroboration | not final legal authority |
| OECD historical working-time series | selected countries, in some tables back to 1870 | mainly OECD / historical industrial countries | actual annual / weekly work hours | long-run realized-time history | limited country coverage and sector comparability |

## Subjective-well-being sources

| source | time depth | geography | construct | use | caveat |
|---|---|---|---|---|---|
| World Database of Happiness | observations from 1945 onward; coverage through 2019 in documented archive | up to 173 nations in archive | happiness/life satisfaction distributions with wording metadata | historical outcome backbone / comparable-question subsets | heterogeneous questions and irregular timing |
| Cantril Pattern of Human Concerns | 1957–1963 | ICPSR data for 10 of original 14 nations | early comparative subjective evaluation / concerns | early cross-national bridge | not an annual panel; some sampling limitations |
| Eurobarometer | first life-satisfaction study 1973; repeated thereafter | European Community/EU, expanding membership | life satisfaction | repeated European long-run panel | changing country membership; Europe only |
| WVS / EVS | 1981 onward | expanding global country waves | happiness + life satisfaction | global country-wave panel | wave spacing and question/scaling differences |
| Gallup World Poll / WHR | mid-2000s onward; current WHR public products vary by release | >140 countries in typical recent years | Cantril Life Ladder and affect | modern annual/global backbone | distinguish genuine annual values from rolling multi-year WHR display averages |

## Verified scope facts motivating expansion

- WORLD annual-leave / weekly-rest dataset covers all 193 UN countries at the 2015 snapshot.
- ILO C052 (1936) has 54 ratifications in the current NORMLEX table; C132 (1970) has 39.
- Eurobarometer traces life-satisfaction measurement to 1973.
- WVS reports long-term happiness evidence beginning in 1981.
- World Database of Happiness documents roughly 12,705 happiness distributions in 173 nations for 1945–2019 in its 2020 coverage statement, while long comparable time series are much smaller.
- ICPSR 7023 preserves Pattern of Human Concerns data for ten countries from 1957–1963.
- OECD historical working-time material contains selected-country annual-hours series extending to 1870.

## Design implication

Coverage is large but uneven. ARIS4C019 must use a **tiered panel** rather than pretend every country has yearly observations from 1900 onward. The correct unit changes from legal milestone / decade to survey wave to annual country-year as source density improves.
