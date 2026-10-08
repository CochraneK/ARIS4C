"""Gate E T2: Monte-Carlo variance of M1s CPE at a=0.75 (16 focals).

Part A (frozen pipeline, K=10 seed labels): re-run the EXACT sim_m1s logic
(select_deleted deterministic gate + m1s_recovery verbatim below) with 10 new
provenance seed labels. The 3a/3b pipeline is DETERMINISTIC (SEED is a provenance
constant, no RNG anywhere in simcore_3.select_deleted / m1s_recovery) -> all K
runs must be bit-identical to the single 3b run (seed=20260918). MC noise of the
frozen pipeline is therefore exactly 0; this part proves it on disk.

Part B (randomized-deletion sensitivity, K=10 new seeds, LABELED EXTENSION):
because the frozen pipeline has no RNG, the meaningful MC question is how much
recovery_frac / M1s CPE varies across same-size deletion sets. For each seed,
rng = numpy default_rng(seed) draws n = int(0.75*len(post_t0)) works without
replacement from the focal's post-t0 works; the SAME m1s_recovery logic is
applied. cpe_k = (1 - frac_k) * cpe_M0_3b (M0 3b CPE held fixed at its
deterministic value; linear-recovery decomposition per cpe_pilot.py).

Reads: graph_cache.pkl, works indices, m1s_results.csv, cpe_results.csv,
pilot_focals.csv, nodes_authors.csv (all on disk, read-only).
Writes: data/stage4/gateE_mcv.csv. stdout <= 15 lines.
"""
import json
import os
import sys
import time
import pickle

import bisect

import numpy as np
import pandas as pd

sys.path.insert(0, 'code')
from simcore_3 import SEED, build_indices, select_deleted, to_full

T0 = time.time()
S3 = 'data/stage3'
S4 = 'data/stage4'
os.makedirs(S4, exist_ok=True)
A = 0.75
K = 10
MC_SEEDS = [20261008 + i for i in range(1, K + 1)]  # new seeds, != 20260918
RARITY_MAX = 0.30  # same as sim_m1s.py


# ---- VERBATIM copy of code/sim_m1s.py::m1s_recovery (logic reuse; original
# ---- file untouched). Do not import sim_m1s (module-level code would rewrite
# ---- frozen 3b outputs).
def m1s_recovery(works, by_concept, rare, focal, deleted):
    cl = {}
    for c, idxs in by_concept.items():
        if c not in rare:
            continue
        lst = []
        for i in idxs:
            w = works[i]
            yr = w.get('year')
            if yr is not None:
                lst.append((yr, focal in w['authors']))
        lst.sort()
        cl[c] = (lst, [t[0] for t in lst])
    n_rec = 0
    for w in deleted:
        y = w.get('year')
        if y is None:
            continue
        for c in w.get('concepts') or []:
            ent = cl.get(c)
            if not ent:
                continue
            lst, yrs = ent
            pos = bisect.bisect_left(yrs, y)
            j = pos - 1
            while j >= 0 and lst[j][1]:
                j -= 1
            if j >= 0:
                n_rec += 1
                break
    return n_rec


cache = pickle.load(open(S3 + '/graph_cache.pkl', 'rb'))
works = cache['works']
by_author, by_concept = build_indices(works)
n_works = len(works)
rare = {c for c, idxs in by_concept.items()
        if len(idxs) <= RARITY_MAX * n_works}

nodes = pd.read_csv('data/network/nodes_authors.csv')
nodes['author_id'] = nodes['author_id'].map(to_full)
fyear = dict(zip(nodes['author_id'], nodes['first_work_year']))
pilot = pd.read_csv(S3 + '/pilot_focals.csv')
pilot['author_id'] = pilot['author_id'].map(to_full)

m1s3b = pd.read_csv(S3 + '/m1s_results.csv')
m1s3b = m1s3b[m1s3b.a == A].copy()
m1s3b['key'] = m1s3b.focal + '|' + str(A)
cdf = pd.read_csv(S3 + '/cpe_results.csv')
m0_3b = cdf[(cdf.model == 'M0') & (cdf.a == A)]
m1s_cpe_3b = cdf[(cdf.model == 'M1s') & (cdf.a == A)]
METRICS = ('deg', 'lcc', 'reach')
cpe_m0 = {}
for r in m0_3b.itertuples():
    cpe_m0.setdefault(r.focal, {})[r.metric] = r.cpe
cpe_m1s_3b = {(r.focal, r.metric): r.cpe for r in m1s_cpe_3b.itertuples()}

rows = []
check = []
for focal in pilot['author_id']:
    t0 = int(fyear[focal])
    post = [works[i] for i in by_author.get(focal, [])
            if works[i].get('year') is not None and works[i]['year'] > t0]
    post.sort(key=lambda w: w['id'])
    n = int(A * len(post))
    r3b = m1s3b[m1s3b.focal == focal].iloc[0]
    # ---- Part A: frozen pipeline with K new provenance seed labels
    for k in MC_SEEDS:
        deleted = select_deleted(works, by_author, focal, t0, A)
        n_rec = m1s_recovery(works, by_concept, rare, focal, deleted)
        frac = n_rec / len(deleted) if deleted else 0.0
        rows.append({'part': 'A_frozen_pipeline', 'focal': focal, 'seed': k,
                     'n_deleted': len(deleted), 'n_recoverable': n_rec,
                     'recovery_frac': round(frac, 6),
                     'cpe_deg': round((1.0 - frac) * cpe_m0[focal]['deg'], 6),
                     'cpe_lcc': round((1.0 - frac) * cpe_m0[focal]['lcc'], 6),
                     'cpe_reach': round((1.0 - frac) * cpe_m0[focal]['reach'], 6),
                     'cpe3b_deg': cpe_m1s_3b[(focal, 'deg')]})
        check.append((focal, k, len(deleted), n_rec, frac,
                      int(r3b.n_deleted), int(r3b.n_recoverable), float(r3b.recovery_frac)))
    # ---- Part B: randomized same-size deletion (LABELED extension)
    for k in MC_SEEDS:
        rng = np.random.default_rng(k)
        idx = np.sort(rng.choice(len(post), size=n, replace=False))
        deleted = [post[i] for i in idx]
        n_rec = m1s_recovery(works, by_concept, rare, focal, deleted)
        frac = n_rec / len(deleted) if deleted else 0.0
        rows.append({'part': 'B_random_deletion', 'focal': focal, 'seed': k,
                     'n_deleted': len(deleted), 'n_recoverable': n_rec,
                     'recovery_frac': round(frac, 6),
                     'cpe_deg': round((1.0 - frac) * cpe_m0[focal]['deg'], 6),
                     'cpe_lcc': round((1.0 - frac) * cpe_m0[focal]['lcc'], 6),
                     'cpe_reach': round((1.0 - frac) * cpe_m0[focal]['reach'], 6),
                     'cpe3b_deg': cpe_m1s_3b[(focal, 'deg')]})

df = pd.DataFrame(rows)
df.to_csv(S4 + '/gateE_mcv.csv', index=False)

# Part A integrity: every run must equal the 3b single-seed row
# Note: 3b stored recovery_frac rounded to 6 decimals (round(frac, 6)); the
# unrounded float cannot be compared with tolerance 1e-9 (rounding error up to
# 5e-7). Compare round(fr, 6) against fr3; integer nd/nr equality is exact.
mismatch = 0
for (f, k, nd, nr, fr, nd3, nr3, fr3) in check:
    if not (nd == nd3 and nr == nr3 and abs(round(fr, 6) - fr3) < 1e-9):
        mismatch += 1
# Part B summary (deg, primary metric)
b = df[df.part == 'B_random_deletion']
per_focal = b.groupby('focal')['cpe_deg'].agg(['mean', 'std', 'min', 'max', 'count'])
rel_dev = (b[['cpe_deg', 'cpe3b_deg']].apply(
    lambda r: abs(r.cpe_deg - r.cpe3b_deg) / r.cpe3b_deg if r.cpe3b_deg != 0 else np.nan,
    axis=1)).dropna()
pooled_mean_b = b.groupby('focal')['cpe_deg'].mean().mean()
pooled_mean_3b = b.groupby('focal')['cpe3b_deg'].mean().mean()
ci_lo = float(b.cpe_deg.quantile(0.025))
ci_hi = float(b.cpe_deg.quantile(0.975))

print('MCV rows=%d (A=%d B=%d) K=%d seeds=%d..%d' % (
    len(df), len(df[df.part == 'A_frozen_pipeline']), len(b), K, MC_SEEDS[0], MC_SEEDS[-1]))
print('PART A mismatch vs 3b single-seed: %d/%d -> frozen pipeline MC noise = %s' % (
    mismatch, len(check), 'EXACTLY 0 (deterministic pipeline)' if mismatch == 0 else 'NONZERO'))
print('PART B (random deletion, deg): pooled MC mean=%.5f vs 3b mean=%.5f' % (pooled_mean_b, pooled_mean_3b))
print('PART B per-focal cpe_deg MC: min=%.5f max=%.5f (mean of focal means)' % (
    float(per_focal['mean'].min()), float(per_focal['mean'].max())))
print('PART B rel dev |cpe_k-cpe3b|/cpe3b: mean=%.4f p95=%.4f max=%.4f (n=%d)' % (
    float(rel_dev.mean()), float(rel_dev.quantile(0.95)), float(rel_dev.max()), len(rel_dev)))
print('PART B pooled 95%% CI of cpe_deg (pctile, K x 16): [%.5f, %.5f]' % (ci_lo, ci_hi))
worst = per_focal.sort_values('std', ascending=False).head(2)
for f, r in worst.iterrows():
    print('  most variable focal %s: mc_mean=%.4f mc_sd=%.4f n=%d' % (f[-12:], r['mean'], r['std'], int(r['count'])))
print('SECS %d' % int(time.time() - T0))
