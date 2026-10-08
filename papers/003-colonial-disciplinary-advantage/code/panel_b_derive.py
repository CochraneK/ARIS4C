# stage3b derive: data/raw/panel_b/*.json -> b_layer_cell.csv + b_layer_dyd_year.csv
# deterministic, no network, per-cell streaming (peak memory = 1 cell), cross-checks manifest meta_count
import json, csv, os, glob, re
from collections import defaultdict
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def p(*a): return os.path.join(R, *a)
def wkey(w): return w.get('id') or (w.get('doi') or '')
def akey(a):
    a = a or {}
    return a.get('id') or a.get('orcid') or ('an|%s' % (a.get('display_name') or ''))
def ikey(i):
    i = i or {}
    return i.get('id') or i.get('ror') or ('in|%s' % (i.get('display_name') or ''))
PAT = re.compile(r'^([^_]+)__([^_]+)__(.+)__p(\d+)$')
# enumerate cells from raw filenames (4-part names only; 3-part smoke files ignored)
cellfiles = defaultdict(list)
for fp in glob.glob(p('data/raw/panel_b/*.json')):
    m = PAT.match(os.path.basename(fp))
    if not m: continue
    cellfiles[(m.group(1), m.group(2), m.group(3))].append((int(m.group(4)), fp))
# manifest cross-check (optional; written by panel_b_full.py at end)
man = {}
mf = p('data/panel/b_fetch_manifest.csv')
if os.path.exists(mf):
    for r in csv.DictReader(open(mf, encoding='utf-8')):
        man[(r['mp_iso'], r['col_iso'], r['discipline'])] = int(r['meta_count'])
os.makedirs(p('data/panel'), exist_ok=True)
out_c, out_y = [], []
tot_works = drift = badjson = 0
for key in sorted(cellfiles):
    mp, col, disc = key
    works = []
    for pg, fp in sorted(cellfiles[key]):
        try:
            j = json.load(open(fp, encoding='utf-8'))
        except Exception as e:
            badjson += 1; print('BADJSON %s: %r' % (fp, e)); continue
        works.extend(j.get('results', []))
    seen, au_cell, ins_cell = set(), set(), set()
    years = defaultdict(lambda: {'w': 0, 'au': set(), 'ins': set()})
    n_doi = n_ret = 0
    for w in works:
        k = wkey(w)
        if k in seen: continue
        seen.add(k)
        if w.get('doi'): n_doi += 1
        if w.get('is_retracted'): n_ret += 1
        y = w.get('publication_year')
        ys = years[y]; ys['w'] += 1
        for au in (w.get('authorships') or []):
            ak = akey(au.get('author'))
            au_cell.add(ak); ys['au'].add(ak)
            for inst in (au.get('institutions') or []):
                ik = ikey(inst)
                ins_cell.add(ik); ys['ins'].add(ik)
    n_works = len(seen)
    tot_works += n_works
    if key in man and man[key] != n_works:
        drift += 1
        print('DRIFT %s-%s %s fetched=%d manifest=%d' % (mp, col, disc, n_works, man[key]))
    yj = {str(k): v['w'] for k, v in sorted(years.items(), key=lambda x: (x[0] is None, x[0]))}
    out_c.append([mp, col, disc, n_works, len(au_cell), len(ins_cell), n_doi, n_ret, json.dumps(yj, ensure_ascii=False)])
    for y, v in years.items():
        out_y.append([mp, col, disc, y if y is not None else '', v['w'], len(v['au']), len(v['ins'])])
out_y.sort(key=lambda r: (r[0], r[1], r[2], (r[3] == '', r[3])))
with open(p('data/panel/b_layer_cell.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['mp_iso', 'col_iso', 'discipline', 'n_works', 'n_authors', 'n_institutions', 'n_with_doi', 'n_retracted', 'years_json'])
    w.writerows(out_c)
with open(p('data/panel/b_layer_dyd_year.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['mp_iso', 'col_iso', 'discipline', 'year', 'n_works', 'n_authors', 'n_institutions'])
    w.writerows(out_y)
nz = sorted([r for r in out_c if r[3] > 0], key=lambda r: -r[3])
print('DONE cells=%d manifest_cells=%d nonzero_cells=%d total_works=%d drift_cells=%d badjson=%d' %
      (len(out_c), len(man), len(nz), tot_works, drift, badjson))
print('top10 cells by n_works:')
for r in nz[:10]:
    print('  %s-%s %s works=%d authors=%d insts=%d doi=%d' % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
