# code/cpe_pilot.py
# ARIS4C-004 stage3b T3: CPE pilot table (no re-simulation; reuses on-disk
# m0/m1/m2_results.csv + m1s_results.csv).
# CPE_i(a,t0) = V_obs - E[V_cf] (sign-neutral): >0 participation raised V,
# =0 full substitution, <0 counterfactual adaptation raised V.
# M0/M2 rows: direct graph measurements, V_cf = V_obs + delta (delta from the
#   3a results CSVs; delta <= 0 by construction of deletion/reconnection).
# M1/M1s rows: the 3a CSVs store work-level recovery_frac, NOT graph-level
#   deltas. CPE is therefore derived by the LINEAR-RECOVERY decomposition
#   (explicit assumption, flagged in stage3b_summary.md):
#       cpe = (1 - recovery_frac) * cpe_M0
#   i.e. recovered works keep their M0-era contribution and unrecovered works
#   carry damage proportional to the M0 full-deletion damage.
# 2026-10-08 host fix: 'sign' was previously threshold-based (|cpe|<=5% of
# V_obs -> 'zero'), conflating practical significance with the CPE sign
# (383/768 rows disagreed with the true sign of cpe; acceptance found it).
# Now 'sign' = strict sign of cpe; the 5% band moved to a separate
# 'significant' column (yes/no).
import json
import sys
import time
import pickle
import pandas as pd
import networkx as nx

sys.path.insert(0, 'code')
from simcore_3 import to_full

OUT = 'data/stage3'
t_start = time.time()
cache = pickle.load(open(OUT + '/graph_cache.pkl', 'rb'))
G = cache['G']
lcc_obs = max(len(c) for c in nx.connected_components(G))

pilot = pd.read_csv(OUT + '/pilot_focals.csv')
pilot['author_id'] = pilot['author_id'].map(to_full)
base = {}
for focal in pilot['author_id']:
    base[focal] = {'deg': G.degree(focal), 'lcc': lcc_obs,
                   'reach': len(nx.single_source_shortest_path_length(G, focal))}

m0 = pd.read_csv(OUT + '/m0_results.csv')
m1 = pd.read_csv(OUT + '/m1_results.csv')
m2 = pd.read_csv(OUT + '/m2_results.csv')
m1s = pd.read_csv(OUT + '/m1s_results.csv')
METRICS = ('deg', 'lcc', 'reach')
AS = (0.25, 0.5, 0.75, 1.0)


def true_sign(cpe):
    # strict CPE sign (RESEARCH_BRIEF 8: sign-neutral >0/=0/<0)
    return 'pos' if cpe > 0 else ('zero' if cpe == 0 else 'neg')


def is_significant(cpe, vobs):
    # practical-significance band (5% of metric scale) - NOT the sign
    return 'yes' if abs(cpe) > 0.05 * vobs else 'no'


rows = []
# M0 and M2: direct deltas.
for model, df in (('M0', m0), ('M2', m2)):
    for _, r in df.iterrows():
        f = r['focal']
        for m in METRICS:
            d = r['%s_delta' % m]
            vobs = base[f][m]
            cpe = -d
            rows.append({'focal': f, 'a': r['a'], 'model': model, 'metric': m,
                         'V_obs': vobs, 'V_cf': vobs + d, 'cpe': cpe,
                         'sign': true_sign(cpe),
                         'significant': is_significant(cpe, vobs)})
# M1 and M1s: linear-recovery decomposition of M0 damage.
m0_cpe = {(r['focal'], r['a']): {m: -r['%s_delta' % m] for m in METRICS}
          for _, r in m0.iterrows()}
for model, df in (('M1', m1), ('M1s', m1s)):
    for _, r in df.iterrows():
        f = r['focal']
        rrec = r['recovery_frac']
        for m in METRICS:
            cpe = (1.0 - rrec) * m0_cpe[(f, r['a'])][m]
            vobs = base[f][m]
            rows.append({'focal': f, 'a': r['a'], 'model': model, 'metric': m,
                         'V_obs': vobs, 'V_cf': vobs - cpe, 'cpe': cpe,
                         'sign': true_sign(cpe),
                         'significant': is_significant(cpe, vobs)})
cdf = pd.DataFrame(rows)
cdf.to_csv(OUT + '/cpe_results.csv', index=False)
print('CPE rows=%d (4 models x 16 focals x 4 a x 3 metrics)' % len(cdf))

# sign distribution per model x metric
for model in ('M0', 'M1', 'M1s', 'M2'):
    for m in METRICS:
        s = cdf[(cdf['model'] == model) & (cdf['metric'] == m)]['sign']
        print('CPE %s/%s pos=%d zero=%d neg=%d' % (
            model, m, int((s == 'pos').sum()), int((s == 'zero').sum()),
            int((s == 'neg').sum())))

# monotonicity: within focal, cpe non-decreasing in a (adjacent pairs, strict
# decrease = violation); reported per model x metric.
viol = {}
for model in ('M0', 'M1', 'M1s', 'M2'):
    for m in METRICS:
        v = 0
        for f, g in cdf[(cdf['model'] == model) & (cdf['metric'] == m)].groupby('focal'):
            g = g.sort_values('a')
            cs = g['cpe'].tolist()
            v += sum(1 for i in range(len(cs) - 1) if cs[i + 1] < cs[i])
        viol[(model, m)] = v
print('CPE MONOTONICITY VIOLATIONS (cpe decreases as a increases):')
for k, v in viol.items():
    print('  %s/%s: %d' % (k[0], k[1], v))
print('CPE TOTAL violations=%d' % sum(viol.values()))

# cpe range per model (anomaly screen: any negative cpe = counterfactual raised V)
for model in ('M0', 'M1', 'M1s', 'M2'):
    s = cdf[cdf['model'] == model]['cpe']
    print('CPE %s cpe min=%.4f max=%.4f (neg_rows=%d)' % (
        model, s.min(), s.max(), int((s < 0).sum())))
# M0 scale at a=1.0 per metric
s1 = cdf[(cdf['model'] == 'M0') & (cdf['a'] == 1.0)]
for m in METRICS:
    t = s1[s1['metric'] == m]['cpe']
    print('CPE M0 a=1.0 %s mean=%.1f min=%.1f max=%.1f' % (
        m, t.mean(), t.min(), t.max()))
print('SECS', round(time.time() - t_start, 1))
