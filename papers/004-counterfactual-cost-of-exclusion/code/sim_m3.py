# code/sim_m3.py
# ARIS4C-004 stage3b T2: M3 substitution-prerequisite / discovery-delay
# exploration (bounded, observable implementation).
# For each deleted focal work w (year y, concept set C_w) and each c in C_w:
#   first observed NON-focal work w' with year >= y covering c in the observed
#   graph; delay = year(w') - y; missing if no such w' exists.
# EXPLICIT LABEL (also in m3_lookahead_log.json): OBSERVED-ALTERNATIVE — the
# delay is a proxy measured on the actually-occurring non-focal history, NOT an
# oracle. Limitation: the focal's presence may have accelerated or altered
# these non-focal alternatives, so delay estimates are biased (direction not
# assumed).
import bisect
import json
import statistics
import sys
import time
import pickle
import pandas as pd

sys.path.insert(0, 'code')
from simcore_3 import SEED, build_indices, select_deleted, to_full

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


def build_cl(by_concept, works, focal):
    # per concept: sorted list of (year, is_focal) + parallel year array.
    cl = {}
    for c, idxs in by_concept.items():
        lst = []
        for i in idxs:
            w = works[i]
            yr = w.get('year')
            if yr is not None:
                lst.append((yr, focal in w['authors']))
        lst.sort()
        cl[c] = (lst, [t[0] for t in lst])
    return cl


def first_alt_year(cl, c, y):
    # first NON-focal work covering c with year >= y (observed history only).
    ent = cl.get(c)
    if not ent:
        return None
    lst, yrs = ent
    j = bisect.bisect_left(yrs, y)
    while j < len(lst) and lst[j][1]:
        j += 1
    return lst[j][0] if j < len(lst) else None


rows = []
led = {}
for focal in pilot['author_id']:
    t0 = int(fyear[focal])
    cl = build_cl(by_concept, works, focal)
    by_a_led = {}
    for a in (0.25, 0.5, 0.75, 1.0):
        deleted = select_deleted(works, by_author, focal, t0, a)
        n_pairs = 0
        n_missing = 0
        delays = []
        a_min = None
        a_max = None
        a_used = 0
        for w in deleted:
            y = w.get('year')
            if y is None:
                continue
            for c in w.get('concepts') or []:
                n_pairs += 1
                ya = first_alt_year(cl, c, y)
                if ya is None:
                    n_missing += 1
                else:
                    d = ya - y
                    delays.append(d)
                    a_used += 1
                    if a_min is None or ya < a_min:
                        a_min = ya
                    if a_max is None or ya > a_max:
                        a_max = ya
        med = round(statistics.median(delays), 2) if delays else None
        frac5 = (sum(1 for d in delays if d <= 5) / n_pairs) if n_pairs else 0.0
        frac10 = (sum(1 for d in delays if d <= 10) / n_pairs) if n_pairs else 0.0
        frac20 = (sum(1 for d in delays if d <= 20) / n_pairs) if n_pairs else 0.0
        fracmiss = (n_missing / n_pairs) if n_pairs else 0.0
        rows.append({'focal': focal, 'a': a, 'n_deleted': len(deleted),
                     'n_pairs': n_pairs,
                     'median_delay_years': med,
                     'frac_alt_within_5': round(frac5, 6),
                     'frac_alt_within_10': round(frac10, 6),
                     'frac_alt_within_20': round(frac20, 6),
                     'frac_missing': round(fracmiss, 6)})
        by_a_led[str(a)] = {'year_min': a_min, 'year_max': a_max, 'n_used': a_used}
    led[focal] = {
        'year_min': min((v['year_min'] for v in by_a_led.values()
                         if v['year_min'] is not None), default=None),
        'year_max': max((v['year_max'] for v in by_a_led.values()
                         if v['year_max'] is not None), default=None),
        'n_used': sum(v['n_used'] for v in by_a_led.values()),
        'observed_alternative': True,
        'note': ('delay proxy measured on realized non-focal history, not '
                 'oracle; focal presence may bias delays; seed=%d' % SEED),
        'by_a': by_a_led,
    }
pd.DataFrame(rows).to_csv(OUT + '/m3_results.csv', index=False)
with open(OUT + '/m3_lookahead_log.json', 'w', encoding='utf-8') as f:
    json.dump(led, f, indent=2)

df = pd.DataFrame(rows)
print('M3 focals=%d rows=%d (observed-alternative, NOT oracle)' %
      (df['focal'].nunique(), len(df)))
for a in (0.25, 0.5, 0.75, 1.0):
    s = df[df['a'] == a]
    print('M3 a=%s median_of_median=%.2f frac5=%.3f frac10=%.3f '
          'frac20=%.3f missing=%.3f' % (
              a, s['median_delay_years'].median(),
              s['frac_alt_within_5'].mean(), s['frac_alt_within_10'].mean(),
              s['frac_alt_within_20'].mean(), s['frac_missing'].mean()))
tot_pairs = int(df['n_pairs'].sum())
tot_miss = int(df['frac_missing'].mul(df['n_pairs']).round().sum())
print('M3 TOTAL pairs=%d missing_pairs=%d (%.3f)' %
      (tot_pairs, tot_miss, tot_miss / tot_pairs if tot_pairs else 0.0))
print('M3 used-alt years: min=%s max=%s (across all focals)' % (
    min(v['year_min'] for v in led.values() if v['year_min'] is not None),
    max(v['year_max'] for v in led.values() if v['year_max'] is not None)))
print('SECS', round(time.time() - t_start, 1))
