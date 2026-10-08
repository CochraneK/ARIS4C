# code/sim_benchmark.py
# ARIS4C-004 stage3a T5: synthetic star-loss benchmark.
# Builds 3 synthetic networks (ER / SBM / star+ER background), each embedding
# ONE high-star-degree hub ("star") + background. Same data structure as the
# real pipeline (authors / works / year / concept) and M0/M1/M2 run through the
# SAME simcore_3 code path as the real data (select_deleted / m1_recovery /
# m2_reconnect / compute_metrics). No real graph loaded, no network access.
# Deterministic: seed = SEED = 20260918. Assertions are pre-registered below
# and reported as-is (FAIL is a legitimate outcome, never hidden).
import random, sys, time
import pandas as pd
import networkx as nx
sys.path.insert(0, 'code')
from simcore_3 import (SEED, build_indices, select_deleted, work_coauth_pairs,
                       compute_metrics, m1_recovery, m2_reconnect)

S3 = 'data/stage3'
ALPHAS = (0.25, 0.5, 0.75, 1.0)
T0 = 1980              # star first-work year (debut)
N_SPOKES = 200         # star degree: hub connected to 200 nodes (spec (iii))
LEAVES = 2             # leaves per spoke head -> 3-node island per spoke
CAND_N = 12            # M1 canary sample size per (net, a)
STAR = 'https://openalex.org/AXSTAR00001'
METRICS = ('deg_delta', 'lcc_delta', 'reach_delta')

# top-50 concept pool: real on-disk AC layer (no network)
ac = pd.read_csv('data/network/edges_author_concept.csv')
POOL = sorted(ac['concept_id'].unique().tolist())
assert len(POOL) >= 1, 'empty concept pool'


def _author(i):
    return 'https://openalex.org/AX%07d' % i


def build_network(kind, rng):
    """core background + star + 200 spoke islands. Each island (head p_s +
    LEAVES leaves) links to the rest ONLY through the star edge (post-t0), so
    the star is a true articulation point (meaningful LCC/reach signal)."""
    works = []
    wid = [0]

    def add(authors_, year, concepts):
        wid[0] += 1
        works.append({'id': 'W%06d' % wid[0], 'authors': list(authors_),
                      'year': int(year), 'concepts': list(concepts)})

    def rndc(k):
        return rng.sample(POOL, k)

    def er_core(n):
        core = [_author(i) for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if rng.random() < 10.0 / (n - 1):
                    add([core[i], core[j]], rng.randint(1900, 2020),
                        rndc(rng.choice((1, 2))))
        return core

    if kind == 'er':
        core = er_core(1600)
    elif kind == 'star_er':
        core = er_core(1000)
    elif kind == 'sbm':
        sizes = (1000, 800, 600)
        core = [_author(i) for i in range(sum(sizes))]
        b1, b2 = sizes[0], sizes[0] + sizes[1]
        blk = lambda x: 0 if x < b1 else (1 if x < b2 else 2)
        for i in range(len(core)):
            for j in range(i + 1, len(core)):
                p = 0.01 if blk(i) == blk(j) else 0.001   # p_in > p_out
                if rng.random() < p:
                    add([core[i], core[j]], rng.randint(1900, 2020),
                        rndc(rng.choice((1, 2))))
    else:
        raise ValueError(kind)

    for s in range(N_SPOKES):
        ps = _author(100000 + s)
        leaves = [_author(200000 + s * (LEAVES + 1) + k) for k in range(LEAVES)]
        cs = [rng.choice(POOL)]
        ys = rng.randint(T0 + 1, 2020)
        add([ps] + leaves, ys - 1, cs + rndc(1))      # cluster work, year < ys
        add([STAR, ps], ys, cs + rndc(1))             # star link work, > T0
    for d in range(10):                               # star debut (year == T0)
        add([STAR] + rng.sample(core, 2), T0, rndc(rng.choice((2, 3))))

    G = nx.Graph()
    G.add_node(STAR)
    for w in works:
        for (u, v) in work_coauth_pairs(w):
            G.add_edge(u, v)
    return G, works


def run_network(kind, net_idx, rng):
    G, works = build_network(kind, rng)
    by_author, by_concept = build_indices(works)
    lcc_base = max(len(c) for c in nx.connected_components(G))
    deg_base = G.degree(STAR)
    reach_base = set(nx.single_source_shortest_path_length(G, STAR))
    star_post = sorted((w for w in works
                        if STAR in w['authors'] and w['year'] > T0),
                       key=lambda w: w['id'])
    # per-work M1 verdict (full view), same function as real path
    verdict = {w['id']: m1_recovery(works, by_concept, STAR, [w])[0]
               for w in star_post}
    assert m1_recovery(works, by_concept, STAR, star_post)[0] == sum(
        verdict.values()), 'per-work M1 verdicts inconsistent with list call'

    rows = []
    G0_by_a = {}
    Gf = G.copy()
    prev = 0
    for a in ALPHAS:
        deleted = select_deleted(works, by_author, STAR, T0, a)
        for w in deleted[prev:]:                      # cumulative M0 deletion
            for (u, v) in work_coauth_pairs(w):
                if Gf.has_edge(u, v):
                    Gf.remove_edge(u, v)
        prev = len(deleted)
        G0 = Gf.copy()
        G0_by_a[a] = G0

        m0 = compute_metrics(Gf, STAR, reach_base)
        rows.append({'network': kind, 'model': 'M0', 'a': a, 't0': T0,
                     'n_deleted': len(deleted), 'n_recoverable': 0,
                     'n_replaced': 0, 'deg_delta': m0['deg'] - deg_base,
                     'lcc_delta': m0['lcc'] - lcc_base,
                     'reach_delta': m0['reach'] - len(reach_base),
                     'affected_nodes': m0['affected']})

        G1 = Gf.copy()                                # M1: re-add recovered
        n_rec = 0                                     # deleted works' cliques
        for w in deleted:
            if verdict[w['id']]:
                n_rec += 1
                for (u, v) in work_coauth_pairs(w):
                    G1.add_edge(u, v)
        m1m = compute_metrics(G1, STAR, reach_base)
        rows.append({'network': kind, 'model': 'M1', 'a': a, 't0': T0,
                     'n_deleted': len(deleted), 'n_recoverable': n_rec,
                     'n_replaced': 0, 'deg_delta': m1m['deg'] - deg_base,
                     'lcc_delta': m1m['lcc'] - lcc_base,
                     'reach_delta': m1m['reach'] - len(reach_base),
                     'affected_nodes': m1m['affected']})

        G2 = Gf.copy()                                # M2 reconnection
        n_rep, n_ed, _st = m2_reconnect(G2, works, STAR, T0, deleted)
        m2m = compute_metrics(G2, STAR, reach_base)
        rows.append({'network': kind, 'model': 'M2', 'a': a, 't0': T0,
                     'n_deleted': len(deleted), 'n_recoverable': 0,
                     'n_replaced': n_rep, 'deg_delta': m2m['deg'] - deg_base,
                     'lcc_delta': m2m['lcc'] - lcc_base,
                     'reach_delta': m2m['reach'] - len(reach_base),
                     'affected_nodes': m2m['affected']})

    # ---- canary (d): no-look-ahead view invariance
    works_pre = [w for w in works if w['year'] is not None and w['year'] <= T0]
    can_m2 = []
    for a in ALPHAS:
        deleted = select_deleted(works, by_author, STAR, T0, a)
        Gfull = G0_by_a[a].copy()
        Gpre = G0_by_a[a].copy()
        rf, ef, _ = m2_reconnect(Gfull, works, STAR, T0, deleted)
        rp, ep, _ = m2_reconnect(Gpre, works_pre, STAR, T0, deleted)
        ok = (rf == rp and ef == ep and set(Gfull.edges) == set(Gpre.edges))
        can_m2.append({'network': kind, 'a': a, 'identical': ok,
                       'n_replaced_full': rf, 'n_replaced_pre': rp,
                       'n_edges_full': ef, 'n_edges_pre': ep})
    can_m1 = []
    for a in ALPHAS:
        deleted = select_deleted(works, by_author, STAR, T0, a)
        samp = random.Random(SEED + net_idx * 97 + int(a * 100)).sample(
            deleted, min(CAND_N, len(deleted)))
        for w in samp:
            y = w['year']
            wr = [x for x in works if x['year'] is not None and x['year'] < y]
            _ba, bcr = build_indices(wr)
            v_rest = m1_recovery(wr, bcr, STAR, [w])[0]
            can_m1.append({'network': kind, 'a': a, 'work': w['id'],
                           'verdict_full': verdict[w['id']],
                           'verdict_restricted': v_rest,
                           'agree': verdict[w['id']] == v_rest})
    meta = {'n_nodes': G.number_of_nodes(), 'n_edges': G.number_of_edges(),
            'lcc_base': lcc_base, 'deg_base': deg_base,
            'reach_base': len(reach_base), 'n_star_post': len(star_post),
            'n_recoverable_full': sum(verdict.values())}
    return rows, can_m1, can_m2, meta


def main():
    t_start = time.time()
    nets = ('er', 'sbm', 'star_er')
    all_rows, all_c1, all_c2, metas = [], [], [], {}
    for i, kind in enumerate(nets):
        rng = random.Random(SEED + i)
        rows, c1, c2, meta = run_network(kind, i, rng)
        all_rows += rows
        all_c1 += c1
        all_c2 += c2
        metas[kind] = meta
        print('NET %s nodes=%d edges=%d lcc_base=%d star_deg=%d '
              'n_star_post=%d M1_recoverable_full=%d' % (
                  kind, meta['n_nodes'], meta['n_edges'], meta['lcc_base'],
                  meta['deg_base'], meta['n_star_post'],
                  meta['n_recoverable_full']))
    df = pd.DataFrame(all_rows)
    df.to_csv(S3 + '/benchmark_results.csv', index=False)

    # ---- pre-registered assertions
    a_fail, a_tie = [], 0
    b_fail = []
    for (net, a), g in df.groupby(['network', 'a']):
        g0 = g[g['model'] == 'M0'].iloc[0]
        g1 = g[g['model'] == 'M1'].iloc[0]
        g2 = g[g['model'] == 'M2'].iloc[0]
        for m in METRICS:
            d0, d1, d2 = -g0[m], -g1[m], -g2[m]
            if d0 >= d1 and d0 >= d2:
                if d0 == d1 or d0 == d2:
                    a_tie += 1
            else:
                a_fail.append('%s a=%s %s: M0=%d M1=%d M2=%d' % (net, a, m, d0, d1, d2))
        t0, t1, t2 = (sum(-g0[m] for m in METRICS),
                      sum(-g1[m] for m in METRICS),
                      sum(-g2[m] for m in METRICS))
        if not t1 < t0:
            b_fail.append('%s a=%s M1 total=%d vs M0=%d' % (net, a, t1, t0))
        if not t2 < t0:
            b_fail.append('%s a=%s M2 total=%d vs M0=%d' % (net, a, t2, t0))
    c_fail, c_tot = [], 0
    for (net, model), g in df.groupby(['network', 'model']):
        for m in METRICS:
            seq = [-g[g['a'] == a].iloc[0][m] for a in ALPHAS]
            for x, y in zip(seq, seq[1:]):
                c_tot += 1
                if not x <= y:
                    c_fail.append('%s %s %s seq=%s' % (net, model, m, seq))
    d2_bad = [r for r in all_c2 if not r['identical']]
    d1_bad = [r for r in all_c1 if not r['agree']]
    n_a = len(df.groupby(['network', 'a'])) * len(METRICS)

    v = {}
    v['a'] = 'PASS' if not a_fail else 'FAIL'
    v['b'] = 'PASS' if not b_fail else 'FAIL'
    v['c'] = 'PASS' if not c_fail else 'FAIL'
    v['d'] = 'PASS' if not d2_bad and not d1_bad else 'FAIL'
    overall = 'PASS' if all(x == 'PASS' for x in v.values()) else 'FAIL'

    def mrow(net, a, model):
        return df[(df['network'] == net) & (df['a'] == a) & (df['model'] == model)].iloc[0]

    k = {}
    for net in nets:
        r = mrow(net, 1.0, 'M0')
        k[net] = 'deg=%d lcc=%d reach=%d' % (r['deg_delta'], r['lcc_delta'], r['reach_delta'])
    m1sat = int((df[(df['model'] == 'M1')]['n_recoverable']
                 == df[(df['model'] == 'M1')]['n_deleted']).all())
    m2eq = int((df[(df['model'] == 'M2')].set_index(['network', 'a'])['deg_delta']
                == df[(df['model'] == 'M0')].set_index(['network', 'a'])['deg_delta']).all())

    rep = []
    rep.append('# T5 synthetic star-loss benchmark report (seed=%d)' % SEED)
    rep.append('Construction: star hub (first year t0=%d; %d post-t0 star-link works, '
               '%d spokes x 3-node islands linked to the rest ONLY via the star) + '
               'background: er=ER n=1600 (avg deg~10) | sbm=SBM 1000+800+600 '
               '(p_in=0.01 > p_out=0.001) | star_er=ER n=1000 (avg deg~10). '
               'Years 1900-2020; concepts from the real top-50 pool (N=%d, '
               'edges_author_concept.csv). M0/M1/M2 via simcore_3 (same code path '
               'as real data); M1 graph = M0 graph + coauth cliques of recoverable '
               'deleted works re-added.' % (T0, N_SPOKES, N_SPOKES, len(POOL)))
    rep.append('Sizes: ' + ' | '.join(
        '%s nodes=%d edges=%d lcc_base=%d' % (n, metas[n]['n_nodes'],
                                              metas[n]['n_edges'], metas[n]['lcc_base'])
        for n in nets))
    rep.append('(a) M0 drop largest per metric (ties allowed): %s %d/%d%s' % (
        v['a'], n_a - len(a_fail), n_a,
        ('; FAIL ' + '; '.join(a_fail[:3])) if a_fail else
        '; note: M2 ties M0 on deg in %d checks by design (substitution never '
        'restores focal degree)' % a_tie))
    rep.append('(b) M1 & M2 partial recovery, total drop (deg+lcc+reach) strictly '
               '< M0: %s %d/24%s' % (
                   v['b'], 24 - len(b_fail), ('; FAIL ' + '; '.join(b_fail[:3]))
                   if b_fail else ''))
    rep.append('(c) drop non-decreasing in a (3 nets x 3 models x 3 metrics x 3 '
               'adjacent pairs): %s %d/%d%s' % (
                   v['c'], c_tot - len(c_fail), c_tot,
                   ('; FAIL ' + '; '.join(c_fail[:3])) if c_fail else ''))
    rep.append('(d) no-look-ahead canary: M2 reconnection decisions identical '
               'under works_full vs works_pre_only %d/12; M1 resampled recovered '
               'works re-judged under restricted view (only year<y works visible) '
               '%d/%d agree%s' % (
                   12 - len(d2_bad), len(all_c1) - len(d1_bad), len(all_c1),
                   ('; FAIL ' + str(d2_bad[:2] or d1_bad[:2])) if (d2_bad or d1_bad) else ''))
    rep.append('Key numbers (a=1.0 M0): ' + ' | '.join('%s: %s' % (n, k[n]) for n in nets) +
               ' | M1 n_recoverable==n_deleted in all rows: %s (saturated, consistent '
               'with real data 60/64 rows) | M2 deg_delta==M0 deg_delta in all rows: %s'
               % (m1sat, m2eq))
    rep.append('Verdict: (a)%s (b)%s (c)%s (d)%s => overall %s. Assertions were not '
               'tuned to results; any FAIL above lists observed values.' %
               (v['a'], v['b'], v['c'], v['d'], overall))
    with open(S3 + '/benchmark_report.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(rep) + '\n')
    assert len(rep) <= 15, 'benchmark_report.md exceeds 15 lines'
    print('ASSERT a=%s (%d fail) b=%s (%d) c=%s (%d) d=%s (m2bad=%d m1bad=%d)' % (
        v['a'], len(a_fail), v['b'], len(b_fail), v['c'], len(c_fail), v['d'],
        len(d2_bad), len(d1_bad)))
    print('OVERALL', overall, 'SECS', round(time.time() - t_start, 1))


if __name__ == '__main__':
    main()
