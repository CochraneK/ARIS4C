import json, re, ssl, time, urllib.request, csv
M = 'mailto=aris4c005@example.org'
B = 'https://api.openalex.org/works?per-page=1&' + M
res = []
def get(url, tag, ctx=None):
    last = {}
    for w in (0, 30, 60, 120, 240):
        if w: time.sleep(w)
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'aris4c005/0.1'}), timeout=60, context=ctx)
            last = {'tag': tag, 'url': url, 'status': r.status, 'count': json.loads(r.read().decode()).get('meta', {}).get('count')}
            break
        except Exception as e:
            last = {'tag': tag, 'url': url, 'status': 'ERR ' + str(e)[:140], 'count': None}
    res.append(last)
dn = dm = ''
for row in csv.DictReader(open('data/raw/rw_official/retraction_watch.csv', encoding='utf-8', errors='replace')):
    m2 = re.match(r'^(\d{1,2})/(\d{1,2})/(\d{2,4})', (row.get('RetractionDate') or '').strip())
    if m2:
        s = ('20' if m2.group(3) < '70' else '19') + m2.group(3) if len(m2.group(3)) == 2 else m2.group(3)
        s = '%s-%02d-%02d' % (s, int(m2.group(1)), int(m2.group(2)))
        dn = s if (not dn or s < dn) else dn
        dm = s if (not dm or s > dm) else dm
man = json.load(open('data/manifests/rw_csv_manifest.json'))
man['date_min'], man['date_max'] = dn, dm; man['date_format_note'] = 'RetractionDate raw = MM/DD/YYYY H:MM (US); ISO-normalized here; 2-digit year <70 -> 20xx else 19xx'
json.dump(man, open('data/manifests/rw_csv_manifest.json', 'w'), indent=1, ensure_ascii=False); print('date_range', dn, dm)
get(B + 'filter=publication_year:2015-2015', 'P1')
get(B + 'filter=publication_year:2020-2020', 'P2')
get(B + 'filter=from_publication_date:2015-01-01,to_publication_date:2015-12-31', 'P3')
c1 = [x for x in res if x['tag'] == 'P1'][0]['count']; c3 = [x for x in res if x['tag'] == 'P3'][0]['count']; ok = bool(c1 and c3 and c1 < 50000000 and abs(c1 - c3) <= 0.1 * c1)
get(B + ('filter=from_publication_date:2000-01-01,to_publication_date:2025-12-31' if ok else 'filter=publication_year:2000-2025'), 'P4')
U = 'https://api.reporter.nih.gov/v2/awards?per_page=1'
c = ssl.create_default_context(); c.check_hostname = False; c.verify_mode = ssl.CERT_NONE
try:
    r = urllib.request.urlopen(urllib.request.Request(U, headers={'User-Agent': 'aris4c005/0.1'}), timeout=45, context=c)
    rep = {'tag': 'T4_reporter', 'url': U, 'verify': False, 'tls_deviation': 'CERT_NONE (stage1: self-signed in chain)', 'status': r.status, 'snip': r.read(500).decode('utf-8', 'replace')[:300]}
except Exception as e:
    rep = {'tag': 'T4_reporter', 'url': U, 'verify': False, 'tls_deviation': 'CERT_NONE (stage1: self-signed in chain)', 'status': 'ERR ' + str(e)[:160]}
res.append(rep); print('T4', rep['status'], str(rep.get('snip'))[:120]); print('P1-P4=', [(x['tag'], x['status'], x['count']) for x in res]); json.dump(res, open('data/_raw/denominator_probe.json', 'w'), indent=1, ensure_ascii=False); print('wrote probe json; done')
