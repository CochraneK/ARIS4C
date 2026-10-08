#!/usr/bin/env python
"""T2: F2 re-verify + R4 disambiguation. Local only (zero OpenAlex queries).

Inputs (frozen): data/exposure_queue.csv, data/raw/works/*.json, data/_raw/fetch_progress_2b.txt
Outputs: data/network/f2_reverify.csv, data/network/excluded_2b.csv, data/network/r4_disambiguation.csv
Rules (stage2b_prompt T2):
  F2: n_works==0 -> EXCLUDE noworks; first_pub_works>1940 & n>=5 -> EXCLUDE post1940;
      >1940 & n<5 -> keep + DIGIT_GAP; works w/o years -> OK_noyear (keep).
  R4: rows with identity_status unresolved / rule_fired R4; top-5 cited work titles vs
      display_name simple token check (case-folded alphabetic tokens len>=2);
      max shared-token fraction over the 5 titles < 0.5 -> NAME_MISMATCH (flag only).
"""
import csv, json, os, re

RAW = 'data/raw/works'
QUEUE = 'data/exposure_queue.csv'
PROG = 'data/_raw/fetch_progress_2b.txt'
OUT = 'data/network'
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
        raise SystemExit('UNKNOWN_CONTAINER ' + p + ' keys=' + repr(sorted(d.keys())[:15]))
    raise SystemExit('UNKNOWN_TOP_TYPE ' + p)

# per-author truncated flag from T1 progress log (fallback: n>=1000)
trunc = {}
if os.path.exists(PROG):
    for line in open(PROG, encoding='utf-8'):
        parts = line.strip().split(',')
        if len(parts) >= 5:
            trunc[short_id(parts[0])] = (parts[3].strip() == '1')

queue = list(csv.DictReader(open(QUEUE, encoding='utf-8')))

def tokens(s):
    return set(t for t in re.findall(r'[a-z]+', (s or '').lower()) if len(t) >= 2)

rows_f2, rows_excl, rows_r4 = [], [], []
stat = {}
r4_flag = 0
no_year = 0
for r in queue:
    aid = r['author_id']
    short = short_id(aid)
    works = load_works(short)
    n = len(works)
    years = [w.get('publication_year') for w in works
             if isinstance(w.get('publication_year'), int)]
    fp = min(years) if years else None
    t = trunc.get(short, n >= 1000)
    if n == 0:
        st = 'EXCLUDE_noworks'
    elif fp is None:
        st = 'OK_noyear'
    elif fp > 1940 and n >= 5:
        st = 'EXCLUDE_post1940'
    elif fp > 1940:
        st = 'DIGIT_GAP'
    else:
        st = 'OK'
    stat[st] = stat.get(st, 0) + 1
    if fp is None and n > 0:
        no_year += 1
    rows_f2.append({
        'author_id': aid, 'name': r['display_name'], 'stratum': r['stratum'],
        'first_pub_queue': r['first_pub'], 'first_pub_works': fp if fp is not None else '',
        'n_works': n, 'truncated': '1' if t else '0', 'f2_status': st,
    })
    if st.startswith('EXCLUDE'):
        rows_excl.append({'author_id': aid, 'reason': st.split('_', 1)[1]})
    if 'r4' in (r.get('rule_fired') or '').lower() or \
       'unresolved' in (r.get('identity_status') or '').lower():
        top5 = sorted(works, key=lambda w: w.get('cited_by_count') or 0, reverse=True)[:5]
        nt = tokens(r['display_name'])
        best = 0.0
        if nt:
            for w in top5:
                tt = tokens(w.get('title') or '')
                best = max(best, len(nt & tt) / len(nt))
        flag = 'NAME_MISMATCH' if (nt and best < 0.5) else 'OK'
        if flag == 'NAME_MISMATCH':
            r4_flag += 1
        titles = ' || '.join((w.get('title') or '')[:200] for w in top5)
        rows_r4.append({'author_id': aid, 'top5_titles': titles, 'mismatch_flag': flag})

with open(os.path.join(OUT, 'f2_reverify.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['author_id', 'name', 'stratum', 'first_pub_queue',
                                      'first_pub_works', 'n_works', 'truncated', 'f2_status'])
    w.writeheader(); w.writerows(rows_f2)
with open(os.path.join(OUT, 'excluded_2b.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['author_id', 'reason'])
    w.writeheader(); w.writerows(rows_excl)
with open(os.path.join(OUT, 'r4_disambiguation.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['author_id', 'top5_titles', 'mismatch_flag'])
    w.writeheader(); w.writerows(rows_r4)

print('queue', len(queue))
print('f2', stat)
print('excluded', len(rows_excl))
print('r4_rows', len(rows_r4), 'r4_flagged', r4_flag)
print('no_year_kept', no_year)
print('DONE_T2')
