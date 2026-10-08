# code/sim_m1s.py
# ARIS4C-004 stage3b T1: M1-strict sensitivity variant (original M1 untouched).
# Pre-registered criterion decision (T1 step 1, verified on 2 sample works of
# data/network/works_index.jsonl): concepts are FLAT canonical concept IDs
# (https://openalex.org/C...) with NO level/depth field. Therefore the main
# criterion (deepest concept level) is inapplicable and the FALLBACK criterion
# is used:
#   deleted work W (year y) is 'strict-recoverable' iff an observed NON-focal
#   work W' with W'.year < y shares >= 1 concept c with W AND c is RARE, i.e.
#   the share of the graph's works (n_works) carrying c is <= 30%
#   (avoids trivial recovery via super-broad concepts).
# Same code path as simcore_3 (build_indices/select_deleted) and the same
# m1_recovery loop structure, with the rarity gate added. seed=20260918.
import bisect
import json
import sys
import time
import pickle
import pandas as pd

sys.path.insert(0, 'code')
from simcore_3 import SEED, build_indices, select_deleted, to_full

OUT = 'data/stage3'
RARITY_MAX = 0.30  # pre-registered fallback threshold (share of graph works)

t_start = time.time()
cache = pickle.load(open(OUT + '/graph_cache.pkl', 'rb'))
works = cache['works']
by_author, by_concept = build_indices(works)
n_works = len(works)
rare_max_count = RARITY_MAX * n_works
rare = {c for c, idxs in by_concept.items() if len(idxs) <= rare_max_count}
print('M1S n_works=%d rare_concepts=%d (in <= %.0f works each, <=30%%)' % (
    n_works, len(rare), rare_max_count))


def m1s_recovery(works, by_concept, rare, focal, deleted):
    # Mirror of simcore_3.m1_recovery (same per-concept (year, is_focal) index,
    # same bisect walk, same ledger) restricted to RARE concepts only.
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
    max_cited = None
    worst_gap = None
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
                cy = lst[j][0]
                if max_cited is None or cy > max_cited:
                    max_cited = cy
                gap = cy - y
                if worst_gap is None or gap > worst_gap:
                    worst_gap = gap
                break
    return n_rec, {'max_cited_year': max_cited, 'worst_gap': worst_gap,
                   'criterion': 'fallback_rarity<=0.30', 'seed': SEED}


nodes = pd.read_csv('data/network/nodes_authors.csv')
nodes['author_id'] = nodes['author_id'].map(to_full)
fyear = dict(zip(nodes['author_id'], nodes['first_work_year']))
pilot = pd.read_csv(OUT + '/pilot_focals.csv')
pilot['author_id'] = pilot['author_id'].map(to_full)

rows = []
led = {}
for focal in pilot['author_id']:
    t0 = int(fyear[focal])
    for a in (0.25, 0.5, 0.75, 1.0):
        deleted = select_deleted(works, by_author, focal, t0, a)
        n_rec, lg = m1s_recovery(works, by_concept, rare, focal, deleted)
        frac = (n_rec / len(deleted)) if deleted else 0.0
        rows.append({'focal': focal, 'a': a, 'n_deleted': len(deleted),
                     'n_recoverable': n_rec, 'recovery_frac': round(frac, 6)})
        led['%s|%s' % (focal, a)] = lg
pd.DataFrame(rows).to_csv(OUT + '/m1s_results.csv', index=False)
with open(OUT + '/m1s_lookahead_log.json', 'w', encoding='utf-8') as f:
    json.dump(led, f, indent=2)

df = pd.DataFrame(rows)
print('M1S focals=%d rows=%d' % (df['focal'].nunique(), len(df)))
for a in (0.25, 0.5, 0.75, 1.0):
    s = df[df['a'] == a]['recovery_frac']
    print('M1S a=%s min=%.4f mean=%.4f max=%.4f' % (a, s.min(), s.mean(), s.max()))
sat = int((df['recovery_frac'] >= 0.999).sum())
print('M1S SATURATED_ROWS (frac>=0.999)=%d/64 (M1 original was 60/64)' % sat)
worst = [v['worst_gap'] for v in led.values() if v['worst_gap'] is not None]
n_none = sum(1 for v in led.values() if v['worst_gap'] is None)
print('M1S WORST_GAP_MAX', max(worst) if worst else None,
      '(must be < 0) | worst_gap=None rows=%d' % n_none)
print('SECS', round(time.time() - t_start, 1))
