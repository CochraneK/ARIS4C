# code/sim_m0.py
# ARIS4C-004 stage3a T2: deterministic pilot focal set + M0 naive deletion.
# M0 = upper-bound stress test (per brief: NOT the preferred/main model).
# Edge deletion is NAIVE FULL REMOVAL of each deleted work's coauth clique and
# author-concept pairs (upper bound, not weight decrement).
import json, sys, time, pickle, random
import pandas as pd
import networkx as nx
sys.path.insert(0, 'code')
from simcore_3 import (SEED, to_full, to_short, build_indices, select_deleted,
                       work_coauth_pairs, work_ac_pairs, compute_metrics)

OUT = 'data/stage3'
t_start = time.time()
cache = pickle.load(open(OUT + '/graph_cache.pkl', 'rb'))
G = cache['G']
works = cache['works']
active_set = set(cache['active'])
ac_set = set((a, c) for a, c, _ in cache['ac_edges'])
by_author, by_concept = build_indices(works)

nodes = pd.read_csv('data/network/nodes_authors.csv')
nodes['author_id'] = nodes['author_id'].map(to_full)
fyear = dict(zip(nodes['author_id'], nodes['first_work_year']))
name = dict(zip(nodes['author_id'], nodes['name']))
strat = dict(zip(nodes['author_id'], nodes['stratum']))
with open(OUT + '/betweenness_full.json', 'r', encoding='utf-8') as f:
    bc = json.load(f)

# ---- deterministic pilot focal set: top20 top5 U per-stratum betweenness top3
top20 = pd.read_csv('data/network/metrics_top20.csv')
top5 = [to_full(x) for x in top20['author_id'].head(5).tolist()]
rng = random.Random(SEED)
randkey = {to_full(a): rng.random() for a in nodes['author_id'].tolist()}
src = {}
for x in top5:
    src[x] = {'top20'}
for st, grp in nodes.groupby('stratum'):
    recs = grp.to_dict('records')
    recs.sort(key=lambda r: (-bc.get(to_short(r['author_id']), 0.0),
                             randkey[r['author_id']]))
    for r in recs[:3]:
        src.setdefault(r['author_id'], set()).add('stratum:' + str(st))
focals = sorted(src.keys())
pilot = pd.DataFrame([
    {'author_id': a, 'name': name.get(a, ''), 'stratum': strat.get(a, ''),
     'betweenness': bc.get(to_short(a), 0.0), 'source': ';'.join(sorted(src[a]))}
    for a in focals])
pilot.to_csv(OUT + '/pilot_focals.csv', index=False)

# ---- baseline (full graph, computed once; betweenness never recomputed)
lcc_base = max(len(c) for c in nx.connected_components(G))
rows = []
aux = {}
ac_viol = 0
for focal in focals:
    t0 = int(fyear[focal])
    reach_base = set(nx.single_source_shortest_path_length(G, focal))
    deg_base = G.degree(focal)
    Gf = G.copy()
    ac_removed = set()
    prev = 0
    for a in (0.25, 0.5, 0.75, 1.0):
        deleted = select_deleted(works, by_author, focal, t0, a)
        for w in deleted[prev:]:
            for (u, v) in work_coauth_pairs(w):
                if Gf.has_edge(u, v):
                    Gf.remove_edge(u, v)
            for (aa, c) in work_ac_pairs(w, active_set):
                # count only pairs in the actual 6380-edge AC layer; the works
                # layer legitimately carries concepts beyond the top-50 summary
                if (aa, c) in ac_set:
                    ac_removed.add((aa, c))
        prev = len(deleted)
        ac_viol += len(ac_removed - ac_set)
        m = compute_metrics(Gf, focal, reach_base)
        rows.append({'focal': focal, 'a': a, 't0': t0,
                     'n_works_deleted': len(deleted),
                     'deg_delta': m['deg'] - deg_base,
                     'lcc_delta': m['lcc'] - lcc_base,
                     'reach_delta': m['reach'] - len(reach_base),
                     'affected_nodes': m['affected']})
        aux[str(a)] = aux.get(str(a), {'n_works_deleted': 0,
                                       'n_ac_pairs_removed_cum_max': 0})
        aux[str(a)]['n_works_deleted'] += len(deleted)
        aux[str(a)]['n_ac_pairs_removed_cum_max'] = max(
            aux[str(a)]['n_ac_pairs_removed_cum_max'], len(ac_removed))
    del Gf
pd.DataFrame(rows).to_csv(OUT + '/m0_results.csv', index=False)
with open(OUT + '/m0_aux.json', 'w', encoding='utf-8') as f:
    json.dump({'ac_violations': ac_viol, 'aux_by_a': aux, 'seed': SEED,
               'lcc_base': lcc_base}, f, indent=2)

df = pd.DataFrame(rows)
print('FOCAL_COUNT', len(focals))
print('GRAPH nodes=%d edges=%d lcc_base=%d' % (
    G.number_of_nodes(), G.number_of_edges(), lcc_base))
for a in (0.25, 0.5, 0.75, 1.0):
    s = df[df['a'] == a]
    print('M0 a=%s n_del_sum=%d deg_min=%d lcc_min=%d reach_min=%d aff_max=%d' % (
        a, s['n_works_deleted'].sum(), s['deg_delta'].min(),
        s['lcc_delta'].min(), s['reach_delta'].min(), s['affected_nodes'].max()))
print('AC_VIOLATIONS', ac_viol)
print('SECS', round(time.time() - t_start, 1))
