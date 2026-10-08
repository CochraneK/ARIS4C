import csv, json, hashlib, os, re, datetime
P = 'data/raw/rw_official/retraction_watch.csv'
raw = open(P, 'rb').read()
sha = hashlib.sha256(raw).hexdigest(); size = len(raw)
assert not raw.lstrip()[:9].lower().startswith(b'<!doctype'), 'NOT_CSV:' + raw[:80].decode('utf-8', 'replace')
R = csv.DictReader(open(P, 'r', encoding='utf-8', errors='replace'))
cols = R.fieldnames; low = {c.lower(): c for c in cols}
doi_c = low.get('originalpaperdoi')
rea_c = next((c for k, c in low.items() if 'reason' in k), None)
pd = 'RetractionDate'
rows = doi_ok = 0; dmin = dmax = ''; rs = {}; dsamp = []
for row in R:
    rows += 1
    if (row.get(doi_c) or '').strip(): doi_ok += 1
    v = (row.get(pd) or '').strip()
    if v and len(dsamp) < 3: dsamp = dsamp + [v]
    m = re.search(r'(19|20)\d{2}[-/.]\d{1,2}[-/.]\d{1,2}', v) or re.search(r'\d{1,2}[-/.](19|20)\d{2}', v)
    if m:
        s = m.group(0)
        dmin = s if (not dmin or s < dmin) else dmin
        dmax = s if (not dmax or s > dmax) else dmax
    for x in (row.get(rea_c) or '').split(';'):
        x = x.strip().lower()
        if x: rs[x] = rs.get(x, 0) + 1
E1K = ['fabricat', 'falsif', 'plagiaris', 'tamper', 'fraud', 'misconduct', 'manipulation', 'duplication', 'forgery', 'splicing', 'doctored']
N1K = ['error', 'mistake', 'duplicate', 'clerical', 'typo', 'administrative', 'editorial', 'copyright', 'permission', 'withdraw']
def cls(v):
    if any(k in v for k in E1K): return 'E1_CANDIDATE'
    if any(k in v for k in N1K): return 'NON_E1'
    return 'UNDECIDED'
items = sorted(rs.items(), key=lambda t: -t[1])
with open('data/rw_e1_mapping.csv', 'w', encoding='utf-8', newline='') as f:
    f.write('# T2 E1 mapping (stage2): official RW CSV, reason split on ";" then lowercased; mapping only, NO rates; row_count = rows containing that value\n')
    f.write('# E1_CANDIDATE contains fabricat|falsif|plagiaris|tamper|fraud|misconduct|manipulation|duplication|forgery|splicing|doctored; NON_E1 = editorial/administrative/errors (error|mistake|duplicate|clerical|typo|administrative|editorial|copyright|permission|withdraw); else UNDECIDED\n')
    f.write('# notice-level reason != adjudicated conclusion (ban1: retraction != fabrication); E1_CANDIDATE is a screening candidate only, final ruling deferred to module B manual audit\n')
    f.write('reason_value,row_count,category\n')
    for v, n in items: f.write(v + ',' + str(n) + ',' + cls(v) + '\n')
tot = {c: sum(n for v, n in items if cls(v) == c) for c in ('E1_CANDIDATE', 'NON_E1', 'UNDECIDED')}
try: cj = json.load(open('data/_raw/gitlab_commits.json'))
except Exception: cj = []
c0 = cj[0] if isinstance(cj, list) and cj else {}
rdl = [l.strip() for l in open('data/raw/rw_official/README.md', encoding='utf-8', errors='replace').read().splitlines() if re.search(r'20\d\d-\d\d-\d\d|updated|generated|weekday', l, re.I)][:6]
man = {'dataset': 'crossref/retraction-watch-data (official RW CSV)',
 'url_csv': 'https://gitlab.com/crossref/retraction-watch-data/-/raw/main/retraction_watch.csv',
 'url_readme': 'https://gitlab.com/crossref/retraction-watch-data/-/raw/main/README.md', 'url_commits_api': 'https://gitlab.com/api/v4/projects/crossref%2Fretraction-watch-data/repository/commits?per_page=1',
 'fetched_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'bytes': size, 'sha256': sha,
 'header_check': 'first line is CSV header, no <!DOCTYPE>', 'rows': rows, 'columns': cols, 'doi_column': doi_c,
 'doi_nonempty_pct': round(100.0 * doi_ok / rows, 2), 'date_column_used': pd, 'date_min': dmin, 'date_max': dmax,
 'distinct_reason_values': len(rs), 'reason_list_split': ';', 'mapping_file': 'data/rw_e1_mapping.csv',
 'provenance': {'commit': c0.get('id'), 'committed_date': c0.get('committed_date'), 'author_name': c0.get('author_name'), 'readme_keylines': rdl}}
json.dump(man, open('data/manifests/rw_csv_manifest.json', 'w'), indent=1, ensure_ascii=False)
print('rows=', rows, 'doi_pct=', man['doi_nonempty_pct'], 'sha256=', sha, 'date_col=', pd, dmin, dmax, 'distinct_reasons=', len(rs), 'dsamp=', dsamp)
print('cols=', cols)
print('top15=', items[:15])
print('cat_totals=', tot)
print('commit=', c0.get('id'), c0.get('committed_date'), 'readme=', rdl)
print('done')
