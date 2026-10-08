#!/usr/bin/env python
"""T4 structure metrics (networkx on CoAuth graphs) + T5 Gate C verdict & stage2b_summary.md.
Local only. Verdict rule PRE-REGISTERED below (brief defines Gate C by name only;
measurement basis per stage2b_prompt T5):
  FAIL        if active < 100 or coverage < 0.5
  PASS        if active >= 150 and active-internal CoAuth edges >= 50
              and full-graph LCC fraction >= 0.5 and coverage >= 0.9
  CONDITIONAL otherwise
"""
import csv, json, os, statistics, datetime, sys

try:
    import networkx as nx
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', 'networkx'])
    import networkx as nx

OUT = 'data/network'

def short_id(aid):
    s = (aid or '').strip()
    return s.rsplit('/', 1)[-1] if '/' in s else s

nodes = list(csv.DictReader(open(os.path.join(OUT, 'nodes_authors.csv'), encoding='utf-8')))
name = {short_id(r['author_id']): r['name'] for r in nodes}
strat = {short_id(r['author_id']): r['stratum'] for r in nodes}
active = set(name)

G = nx.Graph()
with open(os.path.join(OUT, 'edges_coauthor.csv'), encoding='utf-8') as f:
    for r in csv.DictReader(f):
        G.add_edge(r['a1'], r['a2'])
Ga = G.subgraph([a for a in active if a in G.nodes]).copy()

def degstats(H):
    d = [x for _, x in H.degree()]
    if not d:
        return {'min': 0, 'median': 0.0, 'max': 0}
    return {'min': min(d), 'median': statistics.median(d), 'max': max(d)}

def shape(H):
    n = H.number_of_nodes()
    m = H.number_of_edges()
    comps = sorted((len(c) for c in nx.connected_components(H)), reverse=True) if n else []
    dens = (2.0 * m / (n * (n - 1))) if n > 1 else 0.0
    lcc = comps[0] if comps else 0
    return {'n_nodes': n, 'n_edges': m, 'n_components': len(comps),
            'lcc_size': lcc, 'lcc_fraction': round(lcc / n, 6) if n else 0.0,
            'density': round(dens, 8), 'top_component_sizes': comps[:10],
            'degree': degstats(H), 'avg_clustering': round(nx.average_clustering(H), 6)}

S_a = shape(Ga)
S_f = shape(G)

bt = nx.betweenness_centrality(Ga)
top20 = sorted(bt.items(), key=lambda kv: (-kv[1], kv[0]))[:20]
with open(os.path.join(OUT, 'metrics_top20.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['author_id', 'name', 'stratum', 'betweenness'])
    for a, v in top20:
        w.writerow([a, name.get(a, ''), strat.get(a, ''), round(v, 6)])

lcc_nodes = max(nx.connected_components(Ga), key=len) if Ga.number_of_nodes() else set()
bystrat = {}
for s in sorted(set(strat.values())):
    ids = [a for a in active if strat[a] == s]
    ds = [Ga.degree(a) for a in ids if a in Ga.nodes]
    bystrat[s] = {'n_active': len(ids),
                  'mean_degree_in_active_graph': round(sum(ds) / len(ds), 3) if ds else 0.0,
                  'in_lcc': sum(1 for a in ids if a in lcc_nodes)}

f2 = list(csv.DictReader(open(os.path.join(OUT, 'f2_reverify.csv'), encoding='utf-8')))
q_n = len(f2)
cov = sum(1 for r in f2 if int(r['n_works'] or 0) > 0) / q_n
excl_n = sum(1 for _ in csv.DictReader(open(os.path.join(OUT, 'excluded_2b.csv'), encoding='utf-8')))
r4 = list(csv.DictReader(open(os.path.join(OUT, 'r4_disambiguation.csv'), encoding='utf-8')))
r4f = sum(1 for r in r4 if r['mismatch_flag'] == 'NAME_MISMATCH')
f2stat = {}
for r in f2:
    f2stat[r['f2_status']] = f2stat.get(r['f2_status'], 0) + 1
man = json.load(open(os.path.join(OUT, 'network_manifest.json'), encoding='utf-8'))

gate = {'active_set_size': len(active), 'queue_size': q_n,
        'coauth_edges_active': S_a['n_edges'], 'coauth_edges_full': S_f['n_edges'],
        'lcc_fraction_active': S_a['lcc_fraction'], 'lcc_fraction_full': S_f['lcc_fraction'],
        'n_works_gt0_coverage': round(cov, 4)}

if len(active) < 100 or cov < 0.5:
    verdict = 'FAIL'
    reason = 'active set (%d) or works coverage (%.2f) too small for a science-core pilot' % (len(active), cov)
elif len(active) >= 150 and S_a['n_edges'] >= 50 and S_f['lcc_fraction'] >= 0.5 and cov >= 0.9:
    verdict = 'PASS'
    reason = ('active=%d/%d, active-internal CoAuth edges=%d, full-graph LCC fraction=%.3f, '
              'works coverage=%.3f — pilot network sufficient for stage-3 M0-M3'
              % (len(active), q_n, S_a['n_edges'], S_f['lcc_fraction'], cov))
else:
    verdict = 'CONDITIONAL'
    reason = ('active=%d/%d, active-internal CoAuth edges=%d, full-graph LCC fraction=%.3f, '
              'works coverage=%.3f — proceed to stage 3 only after validating R4 identity '
              'flags and entity-fragmentation limits (protocol L2/L3)'
              % (len(active), q_n, S_a['n_edges'], S_f['lcc_fraction'], cov))

metrics = {'scope': 'CoAuth graphs; active subgraph = induced on queue-active authors; full graph = all authors in works union',
           'active_graph': S_a, 'full_graph': S_f,
           'betweenness_top20': [{'author_id': a, 'name': name.get(a, ''), 'stratum': strat.get(a, ''),
                                  'betweenness': round(v, 6)} for a, v in top20],
           'by_stratum': bystrat, 'gate_c': gate, 'verdict': verdict, 'reason': reason,
           'ts': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')}
with open(os.path.join(OUT, 'metrics.json'), 'w', encoding='utf-8') as f:
    json.dump(metrics, f, indent=2, ensure_ascii=False)

bs = '; '.join('%s n=%d deg=%.2f lcc=%d' % (s, bystrat[s]['n_active'],
                  bystrat[s]['mean_degree_in_active_graph'], bystrat[s]['in_lcc'])
               for s in sorted(bystrat))
lines = [
    '# stage2b summary — ARIS4C-004 science core network pilot (2026-10-08)',
    'Local run on frozen T1 data; zero OpenAlex queries this run; T1 accepted, not re-verified.',
    '## Fetch (T1)',
    '- 190 authors; queries_total=%s; http429=%s; stop_reason=%s; %d authors truncated at 5-page/1000-work cap'
    % (man.get('queries_total'), man.get('http429'), man.get('stop_reason'), man.get('truncated_count', 0)),
    '- 41,549 fetched work records; deduplicated union over active authors = %d works' % man.get('works_total', 0),
    '## F2 re-verify (death proxy re-check)',
    '- %s' % ' '.join('%s=%d' % (k, v) for k, v in sorted(f2stat.items())),
    '- active = %d/%d; DIGIT_GAP kept (not a hard fail)' % (len(active), q_n),
    '## R4 disambiguation',
    '- %d unresolved rows; simple token check (top-5 cited titles vs display_name): NAME_MISMATCH=%d; flags only, no exclusions' % (len(r4), r4f),
    '## Exclusions',
    '- %d total (all post1940) -> data/network/excluded_2b.csv' % excl_n,
    '## Network shape',
    '- nodes: %d active authors (%d in full CoAuth set incl. co-authors), %d works, top-50 concepts'
    % (len(active), man.get('author_nodes_full', 0), man.get('works_total', 0)),
    '- edges: CoAuth %d (active-internal %d), AuthorConcept %d'
    % (S_f['n_edges'], S_a['n_edges'], man.get('author_concept_edges', 0)),
    '- full graph: %d components; LCC %d nodes = %.1f%% of %d; density %.2e; avg clustering %.4f'
    % (S_f['n_components'], S_f['lcc_size'], 100 * S_f['lcc_fraction'], S_f['n_nodes'], S_f['density'], S_f['avg_clustering']),
    '- active subgraph: %d nodes (>=1 edge), %d edges, %d components, LCC %d (%.1f%%), degree min/med/max = %s/%s/%s'
    % (S_a['n_nodes'], S_a['n_edges'], S_a['n_components'], S_a['lcc_size'], 100 * S_a['lcc_fraction'],
       S_a['degree']['min'], S_a['degree']['median'], S_a['degree']['max']),
    '- by stratum (active): %s' % bs,
    '## Gate C (science data pilot)',
    '- measurements: active set=%d/%d; CoAuth edges active/full=%d/%d; LCC fraction full=%.4f; n_works>0 coverage=%.4f'
    % (len(active), q_n, S_a['n_edges'], S_f['n_edges'], S_f['lcc_fraction'], cov),
    '- verdict: %s — %s' % (verdict, reason),
    '- rule (pre-registered in code/metrics_2b.py): FAIL if active<100 or coverage<0.5; PASS if active>=150 and active-internal edges>=50 and full LCC fraction>=0.5 and coverage>=0.9; else CONDITIONAL',
    '## Deviations',
    '- D-2b-1: edges/works_index use short A-form author ids (queue & nodes_authors.csv keep full URLs); normalization only.',
    '- D-2b-2: brief defines Gate C by name only; measurement basis per stage2b_prompt T5; pilot thresholds pre-registered above.',
    '- D-2b-3: works union covers active authors only; excluded authors\' works omitted from the network.',
    '## Limitations',
    '- R4 token check weak (%d/%d flagged): flags are not evidence of misidentity; independent second review infeasible — limitation recorded per brief.' % (r4f, len(r4)),
    '- OpenAlex entity contamination/fragmentation (protocol L2/L3) persists inside works; death proxy excludes persons active after 1965 (L1).',
    '- 2 authors truncated at 1000 works; 26 post1940 exclusions (13.7%%) shift the sample earlier.',
    '- full-graph co-authors include living persons (network context only, outside the quantitative sample).',
    '- stage 3 must use the full graph: the active-internal subgraph is sparse by sampling design.',
    'DONE stage2b 004',
]
with open('stage2b_summary.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')

print('gate_c', json.dumps(gate))
print('verdict', verdict)
print('active_graph', S_a['n_nodes'], S_a['n_edges'], S_a['n_components'], S_a['lcc_size'], round(S_a['lcc_fraction'], 4))
print('full_graph', S_f['n_nodes'], S_f['n_edges'], S_f['n_components'], S_f['lcc_size'], round(S_f['lcc_fraction'], 4))
print('coverage', round(cov, 4))
print('summary_lines', len(lines))
print('DONE_T4_T5')
