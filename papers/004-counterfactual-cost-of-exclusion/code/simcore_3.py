# code/simcore_3.py
# ARIS4C-004 stage3a: shared deterministic core for M0/M1/M2 (real + benchmark).
# NO-LOOK-AHEAD CONTRACT:
#   - M1 (m1_recovery): deleted work W (year y) judged ONLY by works with year < y.
#   - M2 (m2_reconnect): substitute decision uses ONLY works with year <= t0
#     (pre-t0 coauth graph + pre-t0 concept sets); post-t0 works/edges never read.
import bisect
from collections import defaultdict
import networkx as nx

SEED = 20260918
PRE = 'https://openalex.org/'

def to_full(a):
    a = str(a)
    return a if a.startswith('http') else PRE + a

def to_short(a):
    return a[len(PRE):] if a.startswith(PRE) else a

def build_indices(works):
    by_author = defaultdict(list)
    by_concept = defaultdict(list)
    for i, w in enumerate(works):
        for a in w['authors']:
            by_author[a].append(i)
        for c in w.get('concepts') or []:
            by_concept[c].append(i)
    return by_author, by_concept

def select_deleted(works, by_author, focal, t0, a):
    # M0 deletion gate: focal works with year > t0 (early-career gate), sorted by
    # work id (deterministic order); take first n = int(a * len). SEED recorded
    # in outputs for provenance.
    post = [works[i] for i in by_author.get(focal, [])
            if works[i].get('year') is not None and works[i]['year'] > t0]
    post.sort(key=lambda w: w['id'])
    return post[:int(a * len(post))]

def work_coauth_pairs(w):
    au = w['authors']
    return [(au[i], au[j]) for i in range(len(au)) for j in range(i + 1, len(au))]

def work_ac_pairs(w, active_set):
    out = []
    for a in w['authors']:
        if a in active_set:
            for c in w.get('concepts') or []:
                out.append((a, c))
    return out

def compute_metrics(G, focal, reach_base):
    # deg / LCC / focal reachability / affected nodes (lost connectivity to focal).
    lcc = max((len(c) for c in nx.connected_components(G)), default=0)
    if focal in G:
        reach = set(nx.single_source_shortest_path_length(G, focal))
        deg = G.degree(focal)
    else:
        reach = set()
        deg = 0
    affected = len(reach_base) - len(reach)
    assert affected >= 0, 'reachability grew beyond baseline (implausible)'
    return {'deg': deg, 'lcc': lcc, 'reach': len(reach), 'affected': affected}

def m1_recovery(works, by_concept, focal, deleted):
    # M1 observed alternative-path recovery (conservative, observed graph only):
    # deleted W (year y) is 'recoverable' iff an observed NON-focal work W' with
    # W'.year < y shares >= 1 concept with W. Only existing works; W'.year < y =>
    # no look-ahead. Returns (n_recoverable, ledger) for the no-look-ahead audit.
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
    return n_rec, {'max_cited_year': max_cited, 'worst_gap': worst_gap}

def m2_pre_t0_state(works, focal, t0):
    # PRE-T0 ONLY: coauth graph + per-author pre-t0 concept set / work count from
    # works with year <= t0. max_year_used ledger for the no-look-ahead audit.
    H = nx.Graph()
    H.add_node(focal)
    pre_concepts = defaultdict(set)
    pre_count = defaultdict(int)
    max_year_used = None
    for w in works:
        yr = w.get('year')
        if yr is None or yr > t0:
            continue
        if max_year_used is None or yr > max_year_used:
            max_year_used = yr
        for a in w['authors']:
            pre_count[a] += 1
            for c in w.get('concepts') or []:
                pre_concepts[a].add(c)
        au = w['authors']
        for i in range(len(au)):
            for j in range(i + 1, len(au)):
                H.add_edge(au[i], au[j])
    return H, pre_concepts, pre_count, max_year_used

def m2_reconnect(G, works, focal, t0, deleted):
    # M2 bounded dynamic reconnection (K=1 substitute work per deleted work).
    # Substitute = pre-t0 author with (1) CoAuth distance <= 2 from focal on the
    # PRE-T0 graph, (2) pre-t0 concept overlap with W, (3) pre-t0 output > 0.
    # Substitute work (year = y, delay 0) = substitute + W's surviving non-focal
    # co-authors; its coauth clique is added to G (in place). Decision uses only
    # pre-t0 information (no look-ahead).
    H, pre_concepts, pre_count, max_year_used = m2_pre_t0_state(works, focal, t0)
    cands = {}
    if focal in H:
        d = nx.single_source_shortest_path_length(H, focal, cutoff=2)
        d.pop(focal, None)
        cands = d
    cand_by_concept = defaultdict(set)
    for A in cands:
        if pre_count.get(A, 0) > 0:
            for c in pre_concepts.get(A, set()):
                cand_by_concept[c].add(A)
    n_replaced = 0
    n_edges_added = 0
    for w in deleted:
        ws = set(w.get('concepts') or [])
        pool = set()
        for c in ws:
            pool |= cand_by_concept.get(c, set())
        if not pool:
            continue
        A = min(pool)  # deterministic substitute (min canonical id)
        n_replaced += 1
        au = list(dict.fromkeys([A] + [x for x in w['authors'] if x != focal]))
        for i in range(len(au)):
            for j in range(i + 1, len(au)):
                if not G.has_edge(au[i], au[j]):
                    G.add_edge(au[i], au[j])
                    n_edges_added += 1
    stats = {'n_candidates': len(cands), 'max_year_used': max_year_used,
             'n_replaced': n_replaced, 'n_edges_added': n_edges_added}
    return n_replaced, n_edges_added, stats
