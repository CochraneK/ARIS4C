# ARIS4C021 · Control-Frame Reconstruction Gate v0.1

Date: 2026-09-24
Status: frozen before exact 99-control reconstruction

## Published Williams target

Williams 2016 reports:
- 40 genocide cases;
- 99 non-genocide political-instability cases;
- 139 total cases;
- case frame: PITF political-instability events, 1955–1998.

The 99 controls are not a generic sample of peaceful country-years. They are severe political-instability episodes that did not receive the genocide/politicide outcome.

## Later PITF 2018 mechanical frame

A deterministic parse of the official PITF Consolidated Problem Set 2018 PDF produced:
- 170 parsed consolidated rows;
- 139 rows with a Begin year <= 1998;
- 36 rows whose brief description contains a GEN episode marker;
- 103 rows without a GEN marker.

Therefore the later 2018 consolidated list does **not** mechanically reproduce the Williams 99-control universe.

Observed discrepancy:
- Williams controls: 99
- PITF2018 mechanical non-GEN candidates: 103
- difference: +4

## Interpretation

Treat the +4 as a **source-version / case-definition drift problem**, not as an invitation to drop four inconvenient cases.

Potential explanations include:
- historical cases added after the PITF snapshot Williams used;
- revised event boundaries or consolidated-case merging/splitting;
- a case that later acquired a GEN subepisode;
- differences between the historical source files and the later 2018 consolidated narrative table;
- start/end-window conventions.

No candidate control may be removed solely because its condition pattern worsens replication fit.

## Hard reconstruction rule

CASE_UNIVERSE_V1.csv may be labelled an **exact Williams reconstruction** only when all of the following hold:

1. 40 positive cases match the literature-derived Williams positive seed;
2. exactly 99 non-genocide controls are present;
3. each difference between the candidate historical source frame and the 99-control target has a source/version/case-definition explanation;
4. exclusions are decided without inspecting QCA/CNA fit;
5. a machine-readable crosswalk records:
   - case identity;
   - source version;
   - inclusion/exclusion;
   - reason;
   - evidence reference.

If the four-case drift cannot be resolved, the project must label the frame **approximate reconstruction** and keep exact-replication claims off.

## Current next action

Search for the PITF/Harff/Williams-era source snapshot (approximately 2012–2013), especially:
- the consolidated PITF event list used by Williams;
- “Genocide and Politicide Model Data (Phase III: 1955-1999)”;
- archived GPANET / PITF downloadable tables.

Then compare pre-1999 non-GEN case identities against PITF2018.
