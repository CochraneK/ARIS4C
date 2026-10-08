# T5 synthetic star-loss benchmark report (seed=20260918)
Construction: star hub (first year t0=1980; 200 post-t0 star-link works, 200 spokes x 3-node islands linked to the rest ONLY via the star) + background: er=ER n=1600 (avg deg~10) | sbm=SBM 1000+800+600 (p_in=0.01 > p_out=0.001) | star_er=ER n=1000 (avg deg~10). Years 1900-2020; concepts from the real top-50 pool (N=50, edges_author_concept.csv). M0/M1/M2 via simcore_3 (same code path as real data); M1 graph = M0 graph + coauth cliques of recoverable deleted works re-added.
Sizes: er nodes=2201 edges=8816 lcc_base=2201 | sbm nodes=3001 edges=12656 lcc_base=3001 | star_er nodes=1601 edges=5849 lcc_base=1601
(a) M0 drop largest per metric (ties allowed): PASS 36/36; note: M2 ties M0 on deg in 12 checks by design (substitution never restores focal degree)
(b) M1 & M2 partial recovery, total drop (deg+lcc+reach) strictly < M0: PASS 24/24
(c) drop non-decreasing in a (3 nets x 3 models x 3 metrics x 3 adjacent pairs): PASS 81/81
(d) no-look-ahead canary: M2 reconnection decisions identical under works_full vs works_pre_only 12/12; M1 resampled recovered works re-judged under restricted view (only year<y works visible) 144/144 agree
Key numbers (a=1.0 M0): er: deg=-200 lcc=-600 reach=-600 | sbm: deg=-200 lcc=-600 reach=-600 | star_er: deg=-200 lcc=-600 reach=-600 | M1 n_recoverable==n_deleted in all rows: 1 (saturated, consistent with real data 60/64 rows) | M2 deg_delta==M0 deg_delta in all rows: 1
Verdict: (a)PASS (b)PASS (c)PASS (d)PASS => overall PASS. Assertions were not tuned to results; any FAIL above lists observed values.
