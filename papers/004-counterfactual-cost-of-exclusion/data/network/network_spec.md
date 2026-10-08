# Network spec — ARIS4C-004 stage2b (frozen at build time)
Scope: science core pilot; local build from frozen T1 data (data/raw/works; 190 authors, 41,549 fetched work records). Zero new queries.
Node classes (3):
 1. authors — active queue authors (queue 190 − excluded_2b). Full CoAuth node set = all author ids appearing in the works union (incl. non-queue co-authors; no stratum label).
 2. works — deduplicated union of fetched works of active authors (by work id).
 3. concepts — top 50 concept ids by frequency across the works union (tie: lexicographic id).
Edge classes (2):
 1. CoAuth(a1,a2,weight,first_year,last_year) — unordered co-occurrence within a work; weight = #shared works; years = min/max work year. Covers ALL authors in the works union.
 2. AuthorConcept(author,concept,weight) — active queue authors x top-50 concepts; weight = # of the author's works carrying the concept.
Time rules: node first/last = min/max publication_year over the node's works; edge year span = min..max over the works generating the edge; missing year -> blank.
ID normalization: author ids in edges/index are short A-form; queue & nodes_authors.csv keep full URLs. Concept ids as returned (C-form).
Gate C (RESEARCH_BRIEF names "science data pilot" without numeric thresholds; stage2b_prompt T5 measurement basis applied): active set size, CoAuth edge count, largest-component fraction, n_works>0 coverage. No additional brief requirements found on inspection.
T4 metrics scope: CoAuth subgraph induced by active queue authors (spec node class); full-graph shape (components/LCC/density) reported alongside in metrics.json.
Decisions: (a) full co-author graph kept in edges for stage-3 M0-M3 simulation; (b) concept layer = sample-summary layer (active authors x top-50); (c) works of excluded authors omitted from the union.
