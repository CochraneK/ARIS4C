# code/gateE_grid.py
# Gate E T4: precision grid per FROZEN data/stage4/gateE_decision_rule.json
# (frozen_utc 2026-10-08T06:15:36Z, written before any grid computation).
# Host-completed after executor 128K death (10-08 14:19); implementation is a
# literal transcription of the frozen spec, no design decisions here.
#
# Spec highlights (from the frozen JSON):
#  - stdCPE = cpe / max_focal(V_obs) per metric; vobs_max_deg=6797.0; a=0.75, deg
#  - M3 standardized cost := per-focal frac_missing at a=0.75 (0-1 scale)
#  - grid: N in {20,30,50,75,100,150} x r in {0.1,0.2,0.4}; pool=73;
#    n_exposed = min(N, round(r*73)); feasible iff N <= 73
#  - models: M0, M2, M3, M1s (M1 excluded: saturated, weak discrimination)
#  - bootstrap: B=2000, resample n_exposed WHOLE focals w.r. from 16;
#    statistic = mean and median of stdCPE
#  - deff(n) = 1 + (n-1)*rho, rho = jaccard_coauth.mean (gateE_variance.json)
#  - ci_width_mean = 3.92 * sd(boot means) * sqrt(deff(n)); median analog
#  - power: ncp = sqrt(n)*median(d)/sd(d) from frozen effect_scales;
#    two-sided alpha=0.05 via scipy.stats.nct, df=n-1
#  - sign_agreement: median over B of fraction of (focal,family) pairs
#    with stdCPE>0 across the 4 families
#
# Reads (read-only): cpe_results.csv, m3_results.csv, gateE_decision_rule.json,
# gateE_variance.json. Writes: data/stage4/gateE_grid.csv. stdout <= 15 lines.
import json
import time

import numpy as np
import pandas as pd
from scipy import stats

T0 = time.time()
S3 = 'data/stage3'
S4 = 'data/stage4'

rule = json.load(open(S4 + '/gateE_decision_rule.json'))
var = json.load(open(S4 + '/gateE_variance.json'))
assert rule['meta']['status'].startswith('FROZEN')
rho = var['c_dependency']['jaccard_coauth']['mean']

# ---- per-focal stdCPE vectors (a=0.75, primary metric deg)
cdf = pd.read_csv(S3 + '/cpe_results.csv')
m3 = pd.read_csv(S3 + '/m3_results.csv')
A = rule['standardization']['a_primary']
MET = rule['standardization']['metric_primary']
vmax = rule['standardization']['vobs_max_deg']
MODELS = rule['grid']['model_families']  # ['M0','M2','M3','M1s']

sub = cdf[(cdf.a == A) & (cdf.metric == MET)].copy()
vobs_max_by_model = sub.groupby('model')['V_obs'].max()
assert abs(vobs_max_by_model['M0'] - vmax) < 1e-9, \
    'frozen vobs_max_deg mismatch: %s' % vobs_max_by_model['M0']

pilot = sorted(sub[sub.model == 'M0']['focal'].unique())
n_foc = len(pilot)
assert n_foc == 16, n_foc
idx = {f: i for i, f in enumerate(pilot)}

X = np.zeros((n_foc, len(MODELS)))
for j, m in enumerate(MODELS):
    if m == 'M3':
        s = m3[m3.a == A].set_index('focal')['frac_missing']
        for i, f in enumerate(pilot):
            X[i, j] = float(s[f])
    else:
        s = sub[sub.model == m].set_index('focal')['cpe']
        for i, f in enumerate(pilot):
            X[i, j] = float(s[f]) / vmax

# ---- grid
Ns = rule['grid']['N']
rs = rule['grid']['r']
pool = rule['grid']['available_pool']
B = 2000
rng = np.random.default_rng(20261008)

es = rule['criteria']['ii_power']['effect_scales']
TEST_BY_MODEL = {'M0': 'cpe_vs_null_M0', 'M2': 'contrast_M0_vs_M2',
                 'M3': 'contrast_M0_vs_M3', 'M1s': 'contrast_M0_vs_M1s'}


def power_test(name, n):
    sc = es[name]
    if sc['focal_sd'] == 0:
        return None  # structural null: power = alpha by design
    ncp = np.sqrt(n) * abs(sc['focal_median']) / sc['focal_sd']
    df = n - 1
    tc = stats.t.ppf(0.975, df)
    return float(stats.nct.sf(tc, df, ncp) + stats.nct.cdf(-tc, df, ncp))


rows = []
for N in Ns:
    for r in rs:
        n = min(N, int(round(r * pool)))
        feasible = N <= pool
        deff = 1.0 + (n - 1) * rho
        sd = np.sqrt(deff)
        # vectorized bootstrap: B x n draws of focal indices
        draws = rng.integers(0, n_foc, size=(B, n))
        samp = X[draws]                      # B x n x 16->j
        means = samp.mean(axis=1)            # B x J
        medians = np.median(samp, axis=1)    # B x J
        w_mean = 3.92 * means.std(axis=0, ddof=1) * sd
        w_med = 3.92 * medians.std(axis=0, ddof=1) * sd
        pos_frac = (samp > 0).mean(axis=(1, 2))   # B: frac (focal,family)>0
        sign_agr = float(np.median(pos_frac))
        for j, m in enumerate(MODELS):
            pw = power_test(TEST_BY_MODEL[m], n)
            note = ''
            if pw is None:
                note = 'structural_null_power=alpha_by_design'
            if not feasible:
                note = ('target_exceeds_pool73_stats_at_achievable_n; ' + note
                        ).strip('; ')
            rows.append({'N': N, 'r': r, 'n_exposed': n,
                         'feasible': feasible, 'model': m,
                         'ci_width_mean': round(float(w_mean[j]), 6),
                         'ci_width_median': round(float(w_med[j]), 6),
                         'contrast_power': (round(pw, 6) if pw is not None
                                            else np.nan),
                         'sign_agreement': round(sign_agr, 6),
                         'note': note})

gdf = pd.DataFrame(rows)
gdf.to_csv(S4 + '/gateE_grid.csv', index=False)

# ---- stdout (<=15 lines)
print('GRID rows=%d (N=%s x r=%s x models=%s) rho=%.4f B=%d' % (
    len(gdf), Ns, rs, MODELS, rho, B))
for N in Ns:
    sel = gdf[(gdf.N == N) & (gdf.model == 'M0')].sort_values('r')
    if N > pool:
        print('N=%d INFEASIBLE (pool %d); best feasible-equivalent n=%d '
              'w_mean(M0)=%.5f' % (N, pool, int(sel.n_exposed.max()),
                                   sel.ci_width_mean.max()))
        continue
    best = sel[sel.ci_width_mean == sel.ci_width_mean.min()].iloc[0]
    pw = gdf[(gdf.N == N) & (gdf.model.isin(['M0', 'M3', 'M1s']))]
    min_pw = pw.contrast_power.min()
    print('N=%d: min w_mean(M0)=%.5f @r=%s(n=%d) | min operative power=%.4f '
          '(null/M3/M1s @n=%d)' % (
              N, best.ci_width_mean, best.r, int(best.n_exposed),
              min_pw, int(pw.loc[pw.contrast_power.idxmin(), 'n_exposed'])))
print('criterion i threshold = 0.5*D_med = %s (D_med=%s): ci_width>0 always '
      '-> structurally INFEASIBLE' % (
          rule['criteria']['i_ci_width']['threshold'],
          rule['criteria']['i_ci_width']['D_med']))
print('SECS %d' % int(time.time() - T0))
