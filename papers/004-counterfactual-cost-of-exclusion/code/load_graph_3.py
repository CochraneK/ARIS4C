# code/load_graph_3.py
# ARIS4C-004 stage3a T1: graph loader + integrity gate (local only, zero OpenAlex queries).
# Canonical key = full URL (short A-form gets https://openalex.org/ prefix).
import time, json, sys, os, gc, pickle
T_START = time.time()
import pandas as pd
import networkx as nx

PRE = 'https://openalex.org/'

def to_full(a):
    a = str(a)
    return a if a.startswith('http') else PRE + a

def to_short(a):
    return a[len(PRE):] if a.startswith(PRE) else a

BASE = 'data/network'
OUT = 'data/stage3'
os.makedirs(OUT, exist_ok=True)

with open(BASE + '/network_manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# active authors (canonical full URLs)
nodes = pd.read_csv(BASE + '/nodes_authors.csv')
active = [to_full(x) for x in nodes['author_id'].tolist()]
active_set = set(active)

# CoAuth edges (31MB -> pandas only, never raw-read)
t_e = time.time()
e = pd.read_csv(BASE + '/edges_coauthor.csv')
n_rows = len(e)
e['a1'] = e['a1'].map(to_full)
e['a2'] = e['a2'].map(to_full)
agg = e.groupby(['a1', 'a2'], sort=False).agg(
    weight=('weight', 'sum'),
    first_year=('first_year', 'min'),
    last_year=('last_year', 'max')).reset_index()
del e
gc.collect()
G = nx.Graph()
G.add_nodes_from(active_set)
for r in agg.itertuples(index=False):
    fy = None if pd.isna(r.first_year) else int(r.first_year)
    ly = None if pd.isna(r.last_year) else int(r.last_year)
    G.add_edge(r.a1, r.a2, weight=float(r.weight), first_year=fy, last_year=ly)
del agg
gc.collect()
n_edges = G.number_of_edges()
secs_edges = time.time() - t_e

# works index (19MB jsonl -> python only)
t_w = time.time()
works = []
with open(BASE + '/works_index.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            d = json.loads(line)
            d['authors'] = [to_full(a) for a in d.get('authors') or []]
            works.append(d)
n_works = len(works)
secs_works = time.time() - t_w

# author-concept edges
ac = pd.read_csv(BASE + '/edges_author_concept.csv')
ac_edges = [(to_full(a), c, int(w)) for a, c, w in
            zip(ac['author_id'].tolist(), ac['concept_id'].tolist(),
                ac['weight'].tolist())]
n_ac = len(ac_edges)
n_concepts = len(set(c for _, c, _ in ac_edges))
del ac
gc.collect()

# integrity gate (FAIL -> exit, no downstream)
g_nodes = set(G.nodes)
res = {
    'coauth_edges': [n_edges, manifest['coauth_edges']],
    'coauth_rows_raw': n_rows,
    'works': [n_works, manifest['works_total']],
    'active_subset': [len(active_set & g_nodes), len(active_set)],
}
ok = (n_edges == manifest['coauth_edges']
      and n_works == manifest['works_total']
      and active_set <= g_nodes)
if not ok:
    print('INTEGRITY_FAIL ' + json.dumps(res))
    sys.exit(1)

# betweenness: ONE approximate pass (k=200), never exact O(VE)
t_b = time.time()
bc = nx.betweenness_centrality(G, k=200, seed=42)
secs_bt = time.time() - t_b
with open(OUT + '/betweenness_full.json', 'w', encoding='utf-8') as f:
    json.dump({to_short(k): round(v, 8) for k, v in bc.items()}, f)

# cache for stage3a sims (single source of truth)
with open(OUT + '/graph_cache.pkl', 'wb') as f:
    pickle.dump({'G': G, 'works': works, 'ac_edges': ac_edges,
                 'active': sorted(active_set), 'manifest': manifest}, f)

def mem_mb():
    try:
        import psutil
        return round(psutil.Process().memory_info().rss / 1e6, 1)
    except Exception:
        import ctypes
        class PMC(ctypes.Structure):
            _fields_ = [('cb', ctypes.c_uint32), ('pf', ctypes.c_uint32),
                        ('ws', ctypes.c_size_t), ('qpp', ctypes.c_size_t),
                        ('qp', ctypes.c_size_t), ('qnpp', ctypes.c_size_t),
                        ('qnp', ctypes.c_size_t), ('pf2', ctypes.c_size_t),
                        ('pws', ctypes.c_size_t)]
        m = PMC()
        m.cb = ctypes.sizeof(m)
        r = ctypes.windll.psapi.GetProcessMemoryInfo(
            ctypes.windll.kernel32.GetCurrentProcess(),
            ctypes.byref(m), ctypes.sizeof(m))
        return round(m.ws / 1e6, 1) if r else None

out = {
    'n_authors': G.number_of_nodes(),
    'n_active': len(active_set),
    'n_coauth_edges': n_edges,
    'n_works': n_works,
    'n_concepts': n_concepts,
    'n_ac_edges': n_ac,
    'coauth_rows_raw': n_rows,
    'betweenness_k': 200,
    'betweenness_seed': 42,
    'mem_mb': mem_mb(),
    'load_secs': round(time.time() - T_START, 1),
    'edges_secs': round(secs_edges, 1),
    'works_secs': round(secs_works, 1),
    'betweenness_secs': round(secs_bt, 1),
    'integrity': 'OK',
}
with open(OUT + '/graph_manifest.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2)
print('LOADER_OK ' + json.dumps(out))
print('INTEGRITY ' + json.dumps(res))
