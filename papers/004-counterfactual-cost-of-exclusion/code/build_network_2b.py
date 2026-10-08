#!/usr/bin/env python
"""T3: build science-core network from frozen T1 works data. Local only.

Outputs (data/network/): nodes_authors.csv, edges_coauthor.csv,
edges_author_concept.csv, works_index.jsonl, network_manifest.json, network_spec.md
"""
import csv, json, os, collections, datetime

QUEUE = 'data/exposure_queue.csv'
EXCL = 'data/network/excluded_2b.csv'
RAW = 'data/raw/works'
OUT = 'data/network'
MAN = 'data/_raw/fetch_manifest_2b.json'
PROG = 'data/_raw/fetch_progress_2b.txt'
os.makedirs(OUT, exist_ok=True)

def short_id(aid):
    s = (aid or '').strip()
    return s.rsplit('/', 1)[-1] if '/' in s else s

def load_works(short):
    p = os.path.join(RAW, short + '.json')
    if not os.path.exists(p):
        return []
    with open(p, encoding='utf-8') as f:
        d = json.load(f)
    if isinstance(d, list):
        return d
    if isinstance(d, dict):
        for k in ('results', 'works', 'items', 'data'):
            v = d.get(k)
            if isinstance(v, list):
                return v
        lists = [v for v in d.values()
                 if isinstance(v, list) and v and isinstance(v[0], dict) and 'id' in v[0]]
        if len(lists) == 1:
            return lists[0]
    raise SystemExit('UNKNOWN_CONTAINER ' + p)

queue = list(csv.DictReader(open(QUEUE, encoding='utf-8')))
excluded = {r['author_id'] for r in csv.DictReader(open(EXCL, encoding='utf-8'))}
active = [r for r in queue if r['author_id'] not in excluded]

per_author = {}   # short id -> list of raw work dicts (active authors only)
works_union = {}  # work id -> normalized record
for r in active:
    short = short_id(r['author_id'])
    ws = load_works(short)
    per_author[short] = ws
    for w in ws:
        wid = w.get('id')
        if not wid or wid in works_union:
            continue
        authors = []
        for a in (w.get('authorships') or []):
            au = a.get('author')
            if isinstance(au, dict) and au.get('id'):
                sid = short_id(au['id'])
                if sid not in authors:
                    authors.append(sid)
        concepts = []
        for c in (w.get('concepts') or []):
            if c.get('id') and c['id'] not in concepts:
                concepts.append(c['id'])
        works_union[wid] = {
            'id': wid, 'doi': w.get('doi'), 'year': w.get('publication_year'),
            'cited': w.get('cited_by_count'), 'authors': authors, 'concepts': concepts,
        }

# concept top-50 by frequency over the union
cc = collections.Counter()
for w in works_union.values():
    cc.update(w['concepts'])
top50 = [cid for cid, _ in sorted(cc.items(), key=lambda kv: (-kv[1], kv[0]))[:50]]
top50set = set(top50)

# CoAuth edges over ALL authors in the union
pair = collections.defaultdict(lambda: [0, None, None])
for w in works_union.values():
    A = w['authors']
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            u, v = sorted((A[i], A[j]))
            p = pair[(u, v)]
            p[0] += 1
            y = w['year']
            if isinstance(y, int):
                p[1] = y if p[1] is None else min(p[1], y)
                p[2] = y if p[2] is None else max(p[2], y)

# AuthorConcept edges: active authors x top-50
ac = collections.Counter()
for short, ws in per_author.items():
    local = collections.Counter()
    for w in ws:
        rec = works_union.get(w.get('id'))
        if rec is None:
            continue
        for c in rec['concepts']:
            if c in top50set:
                local[c] += 1
    for c, k in local.items():
        ac[(short, c)] = k

# nodes_authors.csv (active authors, queue full URL)
all_author_ids = set()
for w in works_union.values():
    all_author_ids.update(w['authors'])
with open(os.path.join(OUT, 'nodes_authors.csv'), 'w', encoding='utf-8', newline='') as f:
    wtr = csv.writer(f)
    wtr.writerow(['author_id', 'name', 'stratum', 'n_works', 'first_work_year', 'last_work_year'])
    for r in active:
        short = short_id(r['author_id'])
        ws = per_author[short]
        years = [w['year'] for w in works_union.values() if isinstance(w['year'], int)]  # placeholder
        ys = []
        for w in ws:
            if isinstance(w.get('publication_year'), int):
                ys.append(w['publication_year'])
        wtr.writerow([r['author_id'], r['display_name'], r['stratum'], len(ws),
                      min(ys) if ys else '', max(ys) if ys else ''])

with open(os.path.join(OUT, 'edges_coauthor.csv'), 'w', encoding='utf-8', newline='') as f:
    wtr = csv.writer(f)
    wtr.writerow(['a1', 'a2', 'weight', 'first_year', 'last_year'])
    for (u, v), (k, fy, ly) in sorted(pair.items()):
        wtr.writerow([u, v, k, fy if fy is not None else '', ly if ly is not None else ''])

with open(os.path.join(OUT, 'edges_author_concept.csv'), 'w', encoding='utf-8', newline='') as f:
    wtr = csv.writer(f)
    wtr.writerow(['author_id', 'concept_id', 'weight'])
    for (a, c), k in sorted(ac.items()):
        wtr.writerow([a, c, k])

with open(os.path.join(OUT, 'works_index.jsonl'), 'w', encoding='utf-8') as f:
    for wid in sorted(works_union):
        f.write(json.dumps(works_union[wid], ensure_ascii=False) + '\n')

# manifest
trunc_count = 0
if os.path.exists(PROG):
    for line in open(PROG, encoding='utf-8'):
        parts = line.strip().split(',')
        if len(parts) >= 5 and parts[3].strip() == '1':
            trunc_count += 1
fm = json.load(open(MAN, encoding='utf-8'))
manifest = {
    'queries_total': fm.get('queries_total'),
    'works_total': len(works_union),
    'truncated_count': fm.get('truncated') if isinstance(fm.get('truncated'), int) else trunc_count,
    'http429': fm.get('http429', 0),
    'stop_reason': fm.get('stop_reason'),
    'queue_authors': len(queue),
    'active_authors': len(active),
    'excluded_authors': len(excluded),
    'author_nodes_full': len(all_author_ids),
    'works_nodes': len(works_union),
    'concept_nodes': len(top50),
    'coauth_edges': len(pair),
    'author_concept_edges': len(ac),
    'ts': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
}
active_short = {short_id(r['author_id']) for r in active}
pair_active = sum(1 for (u, v) in pair if u in active_short and v in active_short)
manifest['coauth_edges_active_only'] = pair_active
with open(os.path.join(OUT, 'network_manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

# frozen network spec (<=30 lines)
spec = [
    '# Network spec — ARIS4C-004 stage2b (frozen at build time)',
    'Scope: science core pilot; local build from frozen T1 data (data/raw/works; 190 authors, 41,549 fetched work records). Zero new queries.',
    'Node classes (3):',
    ' 1. authors — active queue authors (queue 190 − excluded_2b). Full CoAuth node set = all author ids appearing in the works union (incl. non-queue co-authors; no stratum label).',
    ' 2. works — deduplicated union of fetched works of active authors (by work id).',
    ' 3. concepts — top 50 concept ids by frequency across the works union (tie: lexicographic id).',
    'Edge classes (2):',
    ' 1. CoAuth(a1,a2,weight,first_year,last_year) — unordered co-occurrence within a work; weight = #shared works; years = min/max work year. Covers ALL authors in the works union.',
    ' 2. AuthorConcept(author,concept,weight) — active queue authors x top-50 concepts; weight = # of the author\'s works carrying the concept.',
    'Time rules: node first/last = min/max publication_year over the node\'s works; edge year span = min..max over the works generating the edge; missing year -> blank.',
    'ID normalization: author ids in edges/index are short A-form; queue & nodes_authors.csv keep full URLs. Concept ids as returned (C-form).',
    'Gate C (RESEARCH_BRIEF names "science data pilot" without numeric thresholds; stage2b_prompt T5 measurement basis applied): active set size, CoAuth edge count, largest-component fraction, n_works>0 coverage. No additional brief requirements found on inspection.',
    'T4 metrics scope: CoAuth subgraph induced by active queue authors (spec node class); full-graph shape (components/LCC/density) reported alongside in metrics.json.',
    'Decisions: (a) full co-author graph kept in edges for stage-3 M0-M3 simulation; (b) concept layer = sample-summary layer (active authors x top-50); (c) works of excluded authors omitted from the union.',
]
with open(os.path.join(OUT, 'network_spec.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(spec) + '\n')

print('active', len(active), 'excluded', len(excluded))
print('works_union', len(works_union))
print('author_nodes_full', len(all_author_ids))
print('coauth_edges', len(pair), 'active_only', pair_active)
print('ac_edges', len(ac), 'top50', len(top50))
print('DONE_T3')
