# stage2b summary — ARIS4C-004 science core network pilot (2026-10-08)
Local run on frozen T1 data; zero OpenAlex queries this run; T1 accepted, not re-verified.
## Fetch (T1)
- 190 authors; queries_total=312; http429=0; stop_reason=None; 2 authors truncated at 5-page/1000-work cap
- 41,549 fetched work records; deduplicated union over active authors = 37636 works
## F2 re-verify (death proxy re-check)
- DIGIT_GAP=1 EXCLUDE_post1940=26 OK=163
- active = 164/190; DIGIT_GAP kept (not a hard fail)
## R4 disambiguation
- 117 unresolved rows; simple token check (top-5 cited titles vs display_name): NAME_MISMATCH=114; flags only, no exclusions
## Exclusions
- 26 total (all post1940) -> data/network/excluded_2b.csv
## Network shape
- nodes: 164 active authors (31733 in full CoAuth set incl. co-authors), 37636 works, top-50 concepts
- edges: CoAuth 848052 (active-internal 121), AuthorConcept 6380
- full graph: 18 components; LCC 30718 nodes = 96.8% of 31732; density 1.68e-03; avg clustering 0.7902
- active subgraph: 163 nodes (>=1 edge), 121 edges, 79 components, LCC 69 (42.3%), degree min/med/max = 0/1/11
- by stratum (active): biology n=23 deg=0.39 lcc=1; cs n=28 deg=0.43 lcc=5; math n=74 deg=2.42 lcc=50; physics n=39 deg=1.10 lcc=13
## Gate C (science data pilot)
- measurements: active set=164/190; CoAuth edges active/full=121/848052; LCC fraction full=0.9680; n_works>0 coverage=1.0000
- verdict: PASS — active=164/190, active-internal CoAuth edges=121, full-graph LCC fraction=0.968, works coverage=1.000 — pilot network sufficient for stage-3 M0-M3
- rule (pre-registered in code/metrics_2b.py): FAIL if active<100 or coverage<0.5; PASS if active>=150 and active-internal edges>=50 and full LCC fraction>=0.5 and coverage>=0.9; else CONDITIONAL
## Deviations
- D-2b-1: edges/works_index use short A-form author ids (queue & nodes_authors.csv keep full URLs); normalization only.
- D-2b-2: brief defines Gate C by name only; measurement basis per stage2b_prompt T5; pilot thresholds pre-registered above.
- D-2b-3: works union covers active authors only; excluded authors' works omitted from the network.
## Limitations
- R4 token check weak (114/117 flagged): flags are not evidence of misidentity; independent second review infeasible — limitation recorded per brief.
- OpenAlex entity contamination/fragmentation (protocol L2/L3) persists inside works; death proxy excludes persons active after 1965 (L1).
- 2 authors truncated at 1000 works; 26 post1940 exclusions (13.7%%) shift the sample earlier.
- full-graph co-authors include living persons (network context only, outside the quantitative sample).
- stage 3 must use the full graph: the active-internal subgraph is sparse by sampling design.
DONE stage2b 004
