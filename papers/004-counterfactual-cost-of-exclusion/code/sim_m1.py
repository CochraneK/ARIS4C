# code/sim_m1.py
# ARIS4C-004 stage3a T3: M1 observed alternative-path recovery (conservative).
# A deleted work W (year y) is 'recoverable' iff an observed NON-focal work W'
# with W'.year < y shares >= 1 concept with W. Strictly existing works only
# (no fabricated works); W'.year < y => no look-ahead by construction.
import json, sys, time, pickle
import pandas as pd
sys.path.insert(0, 'code')
from simcore_3 import build_indices, select_deleted, m1_recovery, to_full

OUT = 'data/stage3'
t_start = time.time()
cache = pickle.load(open(OUT + '/graph_cache.pkl', 'rb'))
works = cache['works']
by_author, by_concept = build_indices(works)

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
        n_rec, lg = m1_recovery(works, by_concept, focal, deleted)
        frac = (n_rec / len(deleted)) if deleted else 0.0
        rows.append({'focal': focal, 'a': a, 'n_deleted': len(deleted),
                     'n_recoverable': n_rec, 'recovery_frac': round(frac, 6)})
        led['%s|%s' % (focal, a)] = lg
pd.DataFrame(rows).to_csv(OUT + '/m1_results.csv', index=False)
with open(OUT + '/m1_lookahead_log.json', 'w', encoding='utf-8') as f:
    json.dump(led, f, indent=2)

df = pd.DataFrame(rows)
print('M1 focals=%d rows=%d' % (df['focal'].nunique(), len(df)))
for a in (0.25, 0.5, 0.75, 1.0):
    s = df[df['a'] == a]['recovery_frac']
    print('M1 a=%s min=%.4f mean=%.4f max=%.4f' % (a, s.min(), s.mean(), s.max()))
worst = [v['worst_gap'] for v in led.values() if v['worst_gap'] is not None]
print('M1 WORST_GAP_MAX', max(worst) if worst else None,
      '(must be < 0: cited W\' year strictly before deleted W year)')
print('SECS', round(time.time() - t_start, 1))
