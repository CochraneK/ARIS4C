"""Gate E T3 (pre-freeze step): compute frozen constants for the decision rule
(D_med inter-model median contrast, effect scales) and WRITE
data/stage4/gateE_decision_rule.json. Must run BEFORE gateE_grid.py.

All inputs on-disk only. stdout <= 15 lines.
"""
import json
import time

import numpy as np
import pandas as pd

sys_path_ok = True
S3 = 'data/stage3'
S4 = 'data/stage4'

cdf = pd.read_csv(S3 + '/cpe_results.csv')
pilot = pd.read_csv(S3 + '/pilot_focals.csv')
m3 = pd.read_csv(S3 + '/m3_results.csv')

PRE = 'https://openalex.org/'
to_short = lambda a: a[len(PRE):] if str(a).startswith('http') else str(a)

fids = [to_short(f) for f in pilot['author_id'].tolist()]
A = 0.75          # primary a (pre-registered)
MET = 'deg'       # primary metric (pre-registered)
g = cdf[(cdf.a == A) & (cdf.metric == MET)]
g0 = g[g.model == 'M0']
vobs_max = float(g0.set_index(g0.focal.map(to_short))['V_obs'].reindex(fids).max())

def fam_vec(model):
    gg = g[g.model == model]
    s = gg.set_index(gg.focal.map(to_short))['cpe'].reindex(fids)
    assert s.notna().all(), model
    return (s / vobs_max).values.astype(float)

m3a = m3[m3.a == A].copy()
m3a['fid'] = m3a.focal.map(to_short)
vec_M3 = m3a.set_index('fid')['frac_missing'].reindex(fids).values.astype(float)
FAMS = {'M0': fam_vec('M0'), 'M2': fam_vec('M2'), 'M1s': fam_vec('M1s'),
        'M3': vec_M3}

# D_med: median over alt in {M2,M3,M1s} of median_focal(M0 - alt)
alts = ('M2', 'M3', 'M1s')
d_alt = {alt: float(np.median(FAMS['M0'] - FAMS[alt])) for alt in alts}
D_med = float(np.median([d_alt[a] for a in alts]))
threshold = 0.5 * D_med

# effect scales (focal median effect / focal SD) per pre-registered test
def eff(x):
    med, sd = float(np.median(x)), float(np.std(x, ddof=1))
    return {'focal_median': round(med, 5), 'focal_sd': round(sd, 5),
            'd_ratio': round(med / sd, 5) if sd > 0 else None}

tests = {'cpe_vs_null_M0': eff(FAMS['M0'])}
for alt in alts:
    tests['contrast_M0_vs_' + alt] = eff(FAMS['M0'] - FAMS[alt])

# consistency check vs frozen stage3 number (median-of-median missing across a)
m3f = m3.copy()
m3f['fid'] = m3f.focal.map(to_short)
mom = m3f.groupby('fid')['frac_missing'].median()
mom_med = float(mom.median())

rule = {
    'meta': {
        'frozen_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'status': 'FROZEN - written before any grid computation; do not modify',
        'inputs': ['cpe_results.csv', 'm3_results.csv', 'pilot_focals.csv',
                   'gateE_variance.json (rho for design effect)'],
        'script': 'code/gateE_predecision.py',
    },
    'standardization': {
        'formula': 'stdCPE = cpe / max_focal(V_obs) per metric (max over 16 pilot focals)',
        'vobs_max_deg': round(vobs_max, 2),
        'a_primary': A, 'metric_primary': MET,
        'm3_mapping': ('M3 has no graph-metric CPE; its standardized cost := '
                       'frac_missing at a=0.75 (fraction of work-concept pairs with '
                       'no observed non-focal alternative; 0-1 scale, commensurable '
                       'with fractional standardized deg CPE).'),
    },
    'grid': {
        'N': [20, 30, 50, 75, 100, 150],
        'r': [0.10, 0.20, 0.40],
        'available_pool': 73,
        'available_pool_def': ('identity-verified candidates in exposure_queue.csv '
                               '(verified_triple=41 + verified_orcid=32)'),
        'n_exposed_formula': 'n_exposed = min(N, round(r * 73))',
        'feasible_rule': 'feasible iff N <= 73 (else infeasible: target exceeds pool)',
        'interpretation': ('N = target number of exposed focals; r = realized exposed '
                           'yield from MH evidence encoding (not yet executed); the '
                           'verified pool of 73 caps both. Achieving target N requires '
                           'yield >= N/73 (N=20: >=0.27; N=30: >=0.41; N=50: >=0.69).'),
        'model_families': ['M0', 'M2', 'M3', 'M1s'],
        'm1_note': 'M1 excluded from grid (saturated 60/64 rows, weak discrimination per stage3b); retained only as documented limitation.',
    },
    'ci_method': {
        'bootstrap': ('nonparametric, B=2000, resample n_exposed WHOLE focals with '
                      'replacement from the 16 pilot focals; statistic = focal-level '
                      'mean (and median) of stdCPE'),
        'design_effect': ('deff(n) = 1 + (n-1)*rho, rho = mean pairwise Jaccard of '
                          'focal coauth neighborhoods (gateE_variance.json '
                          'c_dependency.jaccard_coauth.mean); se_adj = se_boot*sqrt(deff(n)); '
                          'ci_width = 3.92 * se_adj'),
        'ci_width_mean': '3.92 * sd(bootstrap means) * sqrt(deff(n))',
        'ci_width_median': '3.92 * sd(bootstrap medians) * sqrt(deff(n)) (robust to right tail)',
        'skew_caveat': ('M0 deg stdCPE is right-skewed (one or two hub focals); '
                        'normal-approx width is a lower bound vs percentile width; '
                        'reported as frozen, both estimators (mean/median) shown.'),
    },
    'criteria': {
        'i_ci_width': {
            'rule': 'ci_width_mean(M0; n) <= 0.5 * D_med',
            'D_med_def': 'median over alt in {M2,M3,M1s} of median_focal(stdCPE_M0 - stdCPE_alt) at a=0.75, deg',
            'D_alt_median_focal': {k: round(v, 5) for k, v in d_alt.items()},
            'D_med': round(D_med, 5),
            'threshold': round(threshold, 5),
        },
        'ii_power': {
            'rule': 'power >= 0.80 for all pre-registered tests (two-sided alpha=0.05)',
            'tests': list(tests.keys()),
            'effect_scale_source': ('focal median effect / focal SD from REAL pilot focal '
                                    'data (a=0.75, deg). benchmark_results.csv is synthetic '
                                    'with no focal dimension (gateE_variance.json e_benchmark): '
                                    'it validates contrast direction, not focal variance.'),
            'power_formula': ('paired focal difference d_f; ncp = sqrt(n)*mean(d)/sd(d); '
                              'power = P(reject H0 | ncp) via scipy.stats.nct, df=n-1'),
            'effect_scales': tests,
            'structural_null_note': ('M0 vs M2 on deg is a structural null (M2 deg_delta '
                                     '== M0 deg_delta by construction, frozen stage3b): its '
                                     'power is alpha by design and is flagged, not counted '
                                     'as a failure of criterion ii; the operative contrasts '
                                     'are M0 vs M1s and M0 vs M3 plus cpe_vs_null.'),
        },
    },
    'sign_agreement_def': ('per (N,r): median over B bootstrap replicates of the '
                           'fraction of (focal, family) pairs with stdCPE > 0 across the '
                           '4 families at a=0.75, deg'),
    'consistency_checks': {
        'frozen_m3_overall_missing': '28629/219142=0.1306 (stage3b)',
        'median_of_median_missing_all_a': round(mom_med, 4),
        'note': 'frozen 0.091 = median over focals of per-focal median frac_missing across a (this script reports it); a=1.0-only per-focal median is 0.105 (gateE_variance.json d_missing) - definitions differ, both on disk.',
    },
}

with open(S4 + '/gateE_decision_rule.json', 'w', encoding='utf-8') as f:
    json.dump(rule, f, indent=2)

print('RULE_FROZEN written before grid')
print('vobs_max_deg=%.1f' % vobs_max)
for k in ('M0', 'M2', 'M1s', 'M3'):
    v = FAMS[k]
    print('stdCPE %-4s mean=%.4f median=%.4f sd=%.4f' % (k, v.mean(), np.median(v), v.std(ddof=1)))
print('D_alt %s' % {k: round(v, 5) for k, v in d_alt.items()})
print('D_med=%.5f threshold(0.5*D_med)=%.5f' % (D_med, threshold))
for k, e in tests.items():
    print('test %-20s med=%.4f sd=%.4f d=%.3f' % (k, e['focal_median'], e['focal_sd'], e['d_ratio']))
print('median_of_median_missing_all_a=%.4f (frozen 0.091)' % mom_med)
