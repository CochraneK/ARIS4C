# code/sim_m2.py
# ARIS4C-004 stage3a T4: M2 bounded dynamic reconnection.
# Per deleted work W (year y): substitute = pre-t0 author with (1) CoAuth
# distance <= 2 from focal on the PRE-T0 coauth graph, (2) pre-t0 concept
# overlap with W, (3) pre-t0 output > 0. If found, K=1 substitute work
# (year=y, delay 0) by substitute + W's surviving non-focal co-authors; its
# coauth clique is added. Decision uses ONLY pre-t0 information (no look-ahead).
import json, sys, time, pickle
import pandas as pd
import networkx as nx
sys.path.insert(0, 'code')
from simcore_3 import (build_indices, select_deleted, compute_metrics,
                       m2_reconnect, work_coauth_pairs, to_full)

OUT = 'data/stage3'
t_start = time.time()
cache = pickle.load(open(OUT + '/graph_cache.pkl', 'rb'))
G = cache['G']
works = cache['works']
by_author, by_concept = build_indices(works)

nodes = pd.read_csv('data/network/nodes_authors.csv')
nodes['author_id'] = nodes['author_id'].map(to_full)
fyear = dict(zip(nodes['author_id'], nodes['first_work_year']))
pilot = pd.read_csv(OUT + '/pilot_focals.csv')
pilot['author_id'] = pilot['author_id'].map(to_full)

lcc_base = max(len(c) for c in nx.connected_components(G))
rows = []
led = {}
for focal in pilot['author_id']:
    t0 = int(fyear[focal])
    reach_base = set(nx.single_source_shortest_path_length(G, focal))
    deg_base = G.degree(focal)
    Gf = G.copy()
    prev = 0
    for a in (0.25, 0.5, 0.75, 1.0):
        deleted = select_deleted(works, by_author, focal, t0, a)
        # M0-style naive deletion of newly deleted works first ...
        for w in deleted[prev:]:
            for (u, v) in work_coauth_pairs(w):
                if Gf.has_edge(u, v):
                    Gf.remove_edge(u, v)
        prev = len(deleted)
        # ... then M2 reconnection (idempotent across a: earlier substitute
        # edges already present, earlier works re-processed as no-ops)
        n_rep, n_ed, st = m2_reconnect(Gf, works, focal, t0, deleted)
        m = compute_metrics(Gf, focal, reach_base)
        rows.append({'focal': focal, 'a': a, 'n_deleted': len(deleted),
                     'n_replaced': n_rep,
                     'deg_delta': m['deg'] - deg_base,
                     'lcc_delta': m['lcc'] - lcc_base,
                     'reach_delta': m['reach'] - len(reach_base)})
        led['%s|%s' % (focal, a)] = dict(st, t0=t0)
    del Gf
pd.DataFrame(rows).to_csv(OUT + '/m2_results.csv', index=False)
with open(OUT + '/m2_lookahead_log.json', 'w', encoding='utf-8') as f:
    json.dump(led, f, indent=2)

df = pd.DataFrame(rows)
print('M2 focals=%d rows=%d' % (df['focal'].nunique(), len(df)))
for a in (0.25, 0.5, 0.75, 1.0):
    s = df[df['a'] == a]
    print('M2 a=%s n_del=%d n_rep=%d lcc_min=%d reach_min=%d (vs M0 baseline lcc=%d)' % (
        a, s['n_deleted'].sum(), s['n_replaced'].sum(), s['lcc_delta'].min(),
        s['reach_delta'].min(), lcc_base))
bad = [(k, v['t0'], v['max_year_used']) for k, v in led.items()
       if v['max_year_used'] is not None and v['max_year_used'] > v['t0']]
print('M2 NO_LOOKAHEAD_RUNTIME', 'OK' if not bad else ('FAIL ' + str(bad[:3])))
print('M2 candidates per focal (a=1.0):',
      sorted({v['n_candidates'] for k, v in led.items() if k.endswith('|1.0')}))
print('SECS', round(time.time() - t_start, 1))
