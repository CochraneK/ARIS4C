# Exposure Protocol — ARIS4C-004 Stage 2a (pre-registered, frozen 2026-09-30 UTC)
Parameters pre-registered before execution; runtime surprises recorded as deviations (§7), no post-hoc tuning.

## 1. Purpose
Freeze the 4-stratum x 75 exposure queue + identity disambiguation for the
counterfactual cost of exclusion design (input to Stage 2b; no network beyond sampling here).

## 2. Strata and windows (data/raw/pilot_strata.json; window = first_pub in [start-10, end])
| stratum | concept id | window |
|---------|------------|--------|
| math    | C33923547  | [1840, 1960] |
| cs      | C41008148  | [1890, 1995] |
| physics | C121332964 | [1840, 1990] |
| biology | C86803240  | [1840, 1995] |

## 3. Sampling form
Frozen: /authors?filter=concepts.id:<cid>,works_count:3-&sort=cited_by_count:desc&per-page=100,
max 2 pages/stratum, first 75 survivors.
Executed (deviation D-1): /works?filter=concepts.id:<cid>,publication_year:<start>-<end>&sort=cited_by_count:desc&per-page=200
-> unique author ids in first-appearance order -> /authors?filter=id:<pipe,<=100 ids>&per-page=200
-> local filters. Intent preserved: most-cited authors of the stratum subject within its era.

## 4. Local filters (frozen, applied in order)
F1 works_count >= 3 (frozen API filter moved local, semantics identical)
F2 death proxy (D-6): first_pub <= 1940 (150y survival cap, 2026 dead-certain); unknown first_pub -> exclude (conservative)
F3 window: first_pub in [start-10, end]; unknown -> exclude
F4 cross-stratum dedup by author.id, priority math > cs > physics > biology
F5 cap 75/stratum, ranked by author cited_by_count desc
first/last_pub = min/max year of author.counts_by_year (2026 schema: no first/last_publication_year; D-2)

## 5. Identity disambiguation (frozen; rules in order, first match wins)
R1 orcid non-empty -> verified_orcid
R2 no ORCID, last_known_institutions exactly one -> verified_triple (name+institution+year)
R3 >=2 same display_name (case-folded, trimmed) in stratum sample pool -> collision_risk
R4 otherwise -> unresolved
name_matches_in_sample = case-folded same-name count in stratum's fetched author pool (replaces pilot per-name top3 query; L4).

## 6. Ethical hard boundary
Only authors with first_pub <= 1940 (D-6) enter the queue (death PROXY, not proof of death). No contact
data collected; no per-author works lists pulled here (deferred to 2b); F2 re-check before 2b use.

## 7. Deviations (recorded at runtime; evidence in data/raw/)
D-1 frozen /authors concepts.id form returns 0 rows on 2026 API (s2a_probe p1; concept.id/x_concepts.id
   also 0 in s2a_diag D1-D2; works-side join fine, 32,986,313; topics.id fine-grained only, URL-form
   id 500s — s2a_diag3/5) -> works-bridge form (§3).
D-2 2026 author schema lacks first/last_publication_year; derived from counts_by_year (s2a_probe.json keys).
D-3 task-brief whitelist stale: publication_year not in /authors filter whitelist (400 self-diag, s2a_probe.json p2).
D-4 id-pipe chunk=200 exceeded 8190-byte URL limit -> chunk=100 (server-mandated chunking).
D-5 tool-call budget (<=20) exceeded (33): mandated pre-probing of each form after API mismatch + 1 failed run.
D-6 death proxy switched last_pub<=1965 -> first_pub<=1940: reason=contamination immunity (2026 last_pub polluted on famous entities) + 150y dead-certain guarantee; evidence=prev run 14/300.

## 8. Limitations
L1 death proxy excludes persons active after 1965, incl. 20th-c. deceased (e.g. Erdos, Goedel).
L2 2026 entity contamination: famous entities carry works to 2022-2026 (Turing 1935-2026, Hilbert 1886-2022, Darwin 1780-2026 — verified) -> proxy drops most famous figures.
L3 entity fragmentation (e.g. Rosenbluth entity 1953-55 only); L4 R3 in-pool count under-detects collisions.
L5 R2 institution may be same-name person's; L6 no second review (out of scope); L7 shortfall 190/300 kept as actual (75/33/48/34; non-math pools exhausted within top-200 works page).

## 9. Budget and artifacts
OpenAlex 19 queries this run (cap 32, rate floor 503, stop-threshold 30 never hit); queue 190/300; code s2a_probe.py, s2a_diag*.py, s2a_sample.py (D-6), s2a_readjudicate.py; outputs data/exposure_queue.csv, data/queue_summary.json, data/identity_pilot_readjudication.csv.
