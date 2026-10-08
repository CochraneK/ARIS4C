"""Gate E T1: variance & dependency estimation (focal-level CPE, strata, graph dependency, missingness, benchmark matching).

Reads: data/stage3/{cpe_results,pilot_focals,m3_results,benchmark_results}.csv, graph_cache.pkl (read-only).
Writes: data/stage4/gateE_variance.json. stdout <= 15 lines.
No network. Fixed interpreter.
"""
import json
import os
import sys
import time
import pickle

import numpy as np
import pandas as pd
import networkx as nx
from scipy import stats

sys.path.insert(0, 'code')
from simcore_3 import to_full, to_short

T0 = time.time()
S3 = 'data/stage3'
os.makedirs('data/stage4', exist_ok=True)

cdf = pd.read_csv(S3 + '/cpe_results.csv')
pilot = pd.read_csv(S3 + '/pilot_focals.csv')
m3 = pd.read_csv(S3 + '/m3_results.csv')
bm = pd.read_csv(S3 + '/benchmark_results.csv')

pilot['fid'] = pilot['author_id'].map(to_short)
stratum = dict(zip(pilot['fid'], pilot['stratum']))
fids = pilot['fid'].tolist()
assert len(fids) == 16
METRICS = ('deg', 'lcc', 'reach')
MODELS = ('M0', 'M1', 'M1s', 'M2')

out = {'meta': {
    'generated_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    'files': ['cpe_results.csv', 'pilot_focals.csv', 'm3_results.csv',
              'benchmark_results.csv', 'graph_cache.pkl'],
    'n_focals': 16,
}}

# ---- (a) focal-level CPE mean/SD/median per model x metric, a=0.75 & 1.0 ----
vectors_a075 = {}
part_a = {}
for a in (0.75, 1.0):
    key = 'a%.2f' % a
    part_a[key] = {}
    for model in MODELS:
        part_a[key][model] = {}
        for m in METRICS:
            g = cdf[(cdf.model == model) & (cdf.metric == m) & (cdf.a == a)]
            x = g.set_index(g.focal.map(to_short))['cpe'].reindex(fids)
            assert x.notna().all(), (a, model, m)
            part_a[key][model][m] = {
                'n': 16, 'mean': round(float(x.mean()), 4),
                'sd': round(float(x.std(ddof=1)), 4),
                'median': round(float(x.median()), 4),
                'min': round(float(x.min()), 4), 'max': round(float(x.max()), 4),
            }
            if a == 0.75:
                vectors_a075[model + '|' + m] = {
                    fid: round(float(v), 6) for fid, v in x.items()}
out['a_focal_cpe'] = part_a
out['focal_vectors_a075'] = vectors_a075

# ---- (b) stratum one-way ANOVA + ICC per model x metric (a=0.75 primary) ----
k_groups = 4  # groups (strata), n=4 per stratum
part_b = {}
for a in (0.75, 1.0):
    key = 'a%.2f' % a
    part_b[key] = {}
    for model in MODELS:
        part_b[key][model] = {}
        for m in METRICS:
            g = cdf[(cdf.model == model) & (cdf.metric == m) & (cdf.a == a)]
            x = g.set_index(g.focal.map(to_short))['cpe'].reindex(fids)
            groups = [x[[stratum[f] == s for f in fids]].tolist()
                      for s in ('math', 'cs', 'physics', 'biology')]
            allv = x.values
            grand = allv.mean()
            ssb = sum(len(gi) * (np.mean(gi) - grand) ** 2 for gi in groups)
            ssw = sum(((np.array(gi) - np.mean(gi)) ** 2).sum() for gi in groups)
            msb = ssb / (k_groups - 1)
            msw = ssw / (16 - k_groups)
            F, p = stats.f_oneway(*groups)
            icc = (msb - msw) / (msb + (4 - 1) * msw) if (msb + (4 - 1) * msw) > 0 else 0.0
            part_b[key][model][m] = {
                'ssb': round(float(ssb), 4), 'ssw': round(float(ssw), 4),
                'msb': round(float(msb), 4), 'msw': round(float(msw), 4),
                'F': round(float(F), 4), 'p': round(float(p), 5),
                'icc1': round(float(max(0.0, icc)), 4),
                'var_between': round(float(max(0.0, (msb - msw) / 4)), 4),
                'var_within': round(float(msw), 4),
            }
out['b_strata_anova'] = part_b

# ---- (c) focal subnetwork dependency from graph_cache.pkl ----
t_g = time.time()
cache = pickle.load(open(S3 + '/graph_cache.pkl', 'rb'))
G = cache['G']
works = cache['works']
aw = {}
for w in works:
    for a in w['authors']:
        aw.setdefault(a, set()).add(w['id'])
full_focals = [to_full(f) for f in fids]
wsets = {f: aw.get(f, set()) for f in full_focals}
nsets = {f: set(G.neighbors(f)) for f in full_focals}
sw, sc, jac = [], [], []
jac_within, jac_between = [], []
n_pairs = 0
for i in range(16):
    for j in range(i + 1, 16):
        a1, a2 = full_focals[i], full_focals[j]
        n_pairs += 1
        sw.append(len(wsets[a1] & wsets[a2]))
        inter = len(nsets[a1] & nsets[a2])
        union = len(nsets[a1] | nsets[a2])
        sc.append(inter)
        jv = inter / union if union else 0.0
        jac.append(jv)
        if stratum[fids[i]] == stratum[fids[j]]:
            jac_within.append(jv)
        else:
            jac_between.append(jv)
mean_jac = float(np.mean(jac))
deff_16 = 1.0 + (16 - 1) * mean_jac
out['c_dependency'] = {
    'n_pairs': n_pairs,
    'shared_works': {'mean': round(float(np.mean(sw)), 3),
                     'max': int(max(sw)), 'frac_nonzero': round(float(np.mean(np.array(sw) > 0)), 4)},
    'shared_coauth': {'mean': round(float(np.mean(sc)), 3),
                      'max': int(max(sc)), 'frac_nonzero': round(float(np.mean(np.array(sc) > 0)), 4)},
    'jaccard_coauth': {'mean': round(mean_jac, 4), 'min': round(float(min(jac)), 4),
                       'max': round(float(max(jac)), 4),
                       'within_stratum_mean': round(float(np.mean(jac_within)), 4),
                       'between_stratum_mean': round(float(np.mean(jac_between)), 4)},
    'deff_16': round(deff_16, 4), 'ess_pilot': round(16.0 / deff_16, 3),
    'note': ('deff(n)=1+(n-1)*mean pairwise Jaccard of focal coauth neighborhoods; '
             'ESS(n)=n/deff(n). Jaccard used as ICC proxy for design effect (T4).'),
    'graph_load_secs': round(time.time() - t_g, 1),
}
del cache, G, works, aw, wsets, nsets

# ---- (d) M3 missingness per focal and overall ----
def m3_agg(df):
    tot = int(df['n_pairs'].sum())
    miss = int((df['frac_missing'] * df['n_pairs']).round().sum())
    return tot, miss

tot_all, miss_all = m3_agg(m3)
m3a1 = m3[m3.a == 1.0].copy()
m3a1['fid'] = m3a1.focal.map(to_short)
tot1, miss1 = m3_agg(m3a1)
pf = m3a1.set_index('fid')['frac_missing'].reindex(fids)
out['d_missing'] = {
    'overall_all_rows': {'n_pairs': tot_all, 'missing_pairs': miss_all,
                         'frac': round(miss_all / tot_all, 4)},
    'a1.0': {'n_pairs': tot1, 'missing_pairs': miss1, 'frac': round(miss1 / tot1, 4),
             'per_focal_min': round(float(pf.min()), 4),
             'per_focal_median': round(float(pf.median()), 4),
             'per_focal_max': round(float(pf.max()), 4)},
    'a1.0_focal_frac_missing': {fid: round(float(v), 4) for fid, v in pf.items()},
}

# ---- (e) benchmark matching quality ----
out['e_benchmark'] = {
    'n_rows': int(len(bm)), 'networks': int(bm.network.nunique()),
    'models': int(bm.model.nunique()), 'n_a': int(bm.a.nunique()),
    'rows_per_focal': int(len(bm)), 'min_rows_per_focal': int(len(bm)),
    'median_rows_per_focal': int(len(bm)),
    'note': ('benchmark_results.csv is a synthetic star-loss benchmark (3 networks x 3 '
             'models x 4 a, single seed 20260918) with NO focal dimension: every focal '
             'has access to the same 36 contrast rows, so per-focal min=median=36 by '
             'construction. It validates model-contrast direction (M0 largest drop, '
             'see benchmark_report.md) but cannot supply focal-level contrast '
             'variance; focal median effect/SD for T3 power must come from the real '
             'pilot focal data (cpe_results.csv).'),
}

with open('data/stage4/gateE_variance.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2)

print('T1_OK focal_cpe=strata_anova=dep+missing+benchmark written')
print('a=0.75 M0 deg mean=%.2f sd=%.2f | M2 deg mean=%.2f | M1s deg mean=%.2f' % (
    part_a['a0.75']['M0']['deg']['mean'], part_a['a0.75']['M0']['deg']['sd'],
    part_a['a0.75']['M2']['deg']['mean'], part_a['a0.75']['M1s']['deg']['mean']))
for m in METRICS:
    r = part_b['a0.75']['M0'][m]
    print('ANOVA a=.75 M0/%s F=%.2f p=%.4f icc=%.3f' % (m, r['F'], r['p'], r['icc1']))
c = out['c_dependency']
print('dep pairs=%d shared_works mean=%.1f max=%d | shared_coauth mean=%.1f max=%d fracNZ=%.2f' % (
    c['n_pairs'], c['shared_works']['mean'], c['shared_works']['max'],
    c['shared_coauth']['mean'], c['shared_coauth']['max'], c['shared_coauth']['frac_nonzero']))
print('jaccard mean=%.3f (within=%.3f between=%.3f) deff16=%.2f ESS=%.1f' % (
    c['jaccard_coauth']['mean'], c['jaccard_coauth']['within_stratum_mean'],
    c['jaccard_coauth']['between_stratum_mean'], c['deff_16'], c['ess_pilot']))
print('M3 missing all-rows %d/%d=%.3f | a=1.0 %d/%d=%.3f focal med=%.3f' % (
    miss_all, tot_all, miss_all / tot_all, miss1, tot1, miss1 / tot1,
    out['d_missing']['a1.0']['per_focal_median']))
print('SECS %d' % int(time.time() - T0))
