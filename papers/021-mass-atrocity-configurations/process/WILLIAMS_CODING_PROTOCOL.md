# ARIS4C021 · Williams 2016 Coding Protocol v0.1

Date: 2026-09-24
Status: source-locked transcription of the published coding rules; unresolved details are explicitly marked.

## Purpose

This file defines the historical replication track R. It records what Williams actually reports doing, rather than silently replacing his coding with newer machine-readable proxies.

A second modern/reproducible track M will be constructed separately.

## A · Autocratic regime

Published rule:
- binary: autocratic = 1, non-autocratic = 0;
- source: Polity IV POLITY;
- Williams reports reassessing the classification using Freedom House Freedom in the World;
- published total: 107/139 autocratic = 38/40 genocide + 69/99 non-genocide.

Important unresolved detail:
- the article does not state a single numeric POLITY cutoff or a deterministic rule for how Freedom House overrides/reassesses ambiguous cases.

Replication rule:
- do not invent a cutoff and label it exact Williams coding;
- reconstruct A_R only where the published source procedure or case-level evidence supports the classification;
- construct A_M separately from a fully specified modern rule.

## P · Political upheaval

Published rule:
- P=1 if the range between the highest and lowest democracy/autocracy values over the whole conflict is >=10; OR
- the maximum Harff political-upheaval value during the conflict is >=30.
- Harff political upheaval is based on the sum of maximum magnitudes of revolutionary war, ethnic war, and regime-crisis events in the prior 15 years.
- Harff value <15 -> P=0.
- intermediate Harff values 15–30 -> Williams qualitatively assessed the individual case.
- published total: 56/139 = 25/40 genocide + 31/99 non-genocide.

Temporal-warning:
- whole-conflict range and maximum-during-conflict can use information after the prediction/onset date.

Track split:
- P_R reproduces Williams's retrospective rule where possible.
- P_T/M uses only information observable by the frozen pre-onset prediction date.

## W · War

Published rule:
- source: UCDP/PRIO Armed Conflict Dataset v4-2012, 1946–2011;
- a case is W=1 if it is labelled as war in the armed-conflict dataset during any year of the case;
- underlying armed-conflict definition includes a government/territory incompatibility, armed force between two parties with at least one state government, and at least 25 battle-related deaths;
- published total: 80/139 = 26/40 genocide + 54/99 non-genocide.

Temporal-warning:
- any-year-of-case coding can use post-onset information.

Track split:
- W_R = published any-year case coding.
- W_T/M = war status observable by the frozen pre-onset date.

## I · Exclusionary ideology

Published rule:
- builds on Harff's coding of governing-elite belief systems that justify restricting, persecuting, or eliminating categories defined as opposed to an overriding purpose/principle;
- where Harff coding was unavailable, Williams manually coded the case from in-depth accounts;
- I=1 = exclusionary ideology present among governing elites;
- published total: 47/139 = 25/40 genocide + 22/99 non-genocide.

Replication consequence:
- I_R is partly qualitative/manual by design;
- later ELC values cannot simply be substituted for Williams's manual coding;
- every reconstructed manual cell must carry a source and coding note.

## S · Salience of elite ethnicity

Published rule:
- S=0 when elite ethnicity is not politically salient;
- S=1 when political leadership represents a majority or minority communal group or coalition;
- Williams collapses Harff's majority/minority distinction because the distinction is not theoretically required for his QCA;
- published total: 77/139 = 32/40 genocide + 45/99 non-genocide.

Known contentious case:
- Philippines 1972–76 was coded S=0 in the analysis; Williams later notes this may understate the Christian-vs-Moro cleavage.

Replication consequence:
- preserve Williams's case-level interpretation for S_R where recoverable;
- use a separately specified machine-readable rule for S_M.

## E · Economic autarky

Published rule:
- source: World Bank import and export data;
- imports + exports as percentages of GDP are summed to form trade openness;
- E=1 when the case's trade percentage is below the world average over the relevant 1960–1998 frame;
- published cutoff: 33%;
- E=0 otherwise.

Published-count inconsistency:
- prose says 41 autarkic and 98 interdependent;
- Table 1 cells are 18 genocide + 22 non-genocide = 40, not 41.

Replication rule:
- retain both numbers as a source discrepancy;
- do not modify a case simply to make the total equal either 40 or 41;
- resolve against any recoverable case-level matrix / underlying World Bank series.

## Outcome / case frame

Published Williams analysis:
- 40 genocide cases;
- 99 non-genocide PITF instability controls;
- 139 cases total.

The ARIS4C021 identity reconstruction now reproduces these counts without arbitrary case deletion:
- 40 positive identities from Williams's published case list;
- 99 negative identities after correcting three pre-1955 left-truncation artifacts in the 2014 country-year panel.

## Published marginal validation targets

| Condition | Genocide | Non-genocide | Total |
|---|---:|---:|---:|
| A | 38 | 69 | 107 |
| P | 25 | 31 | 56 |
| W | 26 | 54 | 80 |
| I | 25 | 22 | 47 |
| S | 32 | 45 | 77 |
| E | 18 | 22 | Table=40 / prose=41 |

## Evidence-status vocabulary for CONDITION_MATRIX_V0

Each R/M condition cell must have a status:

- SOURCE_EXACT — directly recoverable from the named source under the frozen rule;
- SOURCE_DERIVED — deterministic transform of source data;
- AUTHOR_RECONSTRUCTED — qualitative reconstruction following Williams's published rule;
- PUBLISHED_CASE_CLUE — inferable from Williams's reported solution/case discussion;
- UNRESOLVED — insufficient evidence;
- NOT_APPLICABLE — condition cannot be defined for that case/rule.

No UNRESOLVED R cell may be silently imputed merely to reproduce published marginal totals.

## Primary source

Williams, Timothy (2016), More Lessons Learned from the Holocaust — Towards a Complexity-Embracing Approach to Why Genocide Occurs, Genocide Studies and Prevention 9(3):137–153, DOI 10.5038/1911-9933.9.3.1306.

Source details recorded in the article:
- PITF/Harff genocide list accessed 2012-11-12;
- Harff Genocide and Politicide Model Data accessed 2013-01-11;
- Polity IV accessed 2013-05-15;
- Freedom House accessed 2013-05-15;
- UCDP/PRIO Armed Conflict Dataset v4-2012;
- World Bank trade data.
