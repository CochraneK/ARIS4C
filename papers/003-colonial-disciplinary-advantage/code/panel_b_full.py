# stage3b: B-layer full works fetch. Cross-border colonial dyads x 17 disciplines.
# filter = authorships.countries:<mp>,authorships.countries:<col>,<disc>,from_publication_date:1990-01-01
# (two separate authorships.countries keys = AND: works with authors in BOTH countries; verified in b_smoke)
# per-page=200, paginated to meta.count. Idempotent: raw at data/raw/panel_b/<mp>__<col>__<disc>__p<N>.json.
# self_dyad=1 rows (11) excluded: domestic pairs are not dyad outcomes (layer A territory, multi-10^6 scale).
# 2026-10-08 host edits (quota-aware): backoff (0,30,60,120,240); 10-consecutive-fail circuit breaker -> sleep 1800s;
#   429 detail log (Retry-After + body). Quota facts: X-RateLimit-Limit=1000 queries/day ($0.10, $0.0001/query,
#   Beijing 08:00 reset); soft grace observed ~3k/day (09-30). Breaker rides out daily exhaustion with ~10 probes/30min.
import json, csv, os, time, math, urllib.request, urllib.parse, urllib.error
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def p(*a): return os.path.join(R, *a)
UA = {'User-Agent': 'aris4c-003-stage3b/0.1 (local research)'}
BASE = 'https://api.openalex.org/works'
DISC = [
 ('History','history','topics.subfield.id:https://openalex.org/subfields/1202'),
 ('Political Science','polsci','topics.subfield.id:https://openalex.org/subfields/3320'),
 ('Law','law','topics.subfield.id:https://openalex.org/subfields/3308'),
 ('Philosophy','philosophy','topics.subfield.id:https://openalex.org/subfields/1211'),
 ('Linguistics','linguistics','topics.subfield.id:https://openalex.org/subfields/1203|https://openalex.org/subfields/3310'),
 ('Anthropology','anthropology','topics.subfield.id:https://openalex.org/subfields/3314'),
 ('Archaeology','archaeology','concepts.id:https://openalex.org/C166957645'),
 ('Evolutionary Biology','evolbio','topics.subfield.id:https://openalex.org/subfields/1105'),
 ('Botany','botany','concepts.id:https://openalex.org/C59822182'),
 ('Tropical','tropical','concepts.id:https://openalex.org/C185032368'),
 ('Mining','mining','concepts.id:https://openalex.org/C16674752'),
 ('Materials Science','materials','topics.field.id:https://openalex.org/fields/25'),
 ('Computer Science','compsci','topics.field.id:https://openalex.org/fields/17'),
 ('Physics and Astronomy','physics','topics.field.id:https://openalex.org/fields/31'),
 ('Mathematics','math','topics.field.id:https://openalex.org/fields/26'),
 ('Chemistry','chemistry','topics.field.id:https://openalex.org/fields/16'),
 ('Engineering','engineering','topics.field.id:https://openalex.org/fields/22'),
]
def fetch(url):
    last = None
    for wait in (0, 30, 60, 120, 240):
        if wait: time.sleep(wait)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
                return r.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 429:
                try:
                    _d = e.read().decode('utf-8', 'replace')[:150]
                except Exception:
                    _d = ''
                print('429 retry-after=%r body=%r' % (e.headers.get('Retry-After'), _d), flush=True)
            if e.code not in (429, 500, 502, 503, 504):
                raise
        except Exception as e:
            last = e
    raise RuntimeError('retries exhausted: %r' % last)
def getpage(flt, page, fp):
    if os.path.exists(fp) and os.path.getsize(fp) > 0:
        return json.load(open(fp, encoding='utf-8'))
    url = BASE + '?' + urllib.parse.urlencode(
        {'filter': flt, 'per-page': '200', 'page': str(page)})
    body = fetch(url)
    open(fp, 'w', encoding='utf-8').write(body)
    return json.loads(body)
dyads = [r for r in csv.DictReader(open(p('data/manifests/dyad_set.csv'), encoding='utf-8'))
         if r['self_dyad'] != '1']
rawdir = p('data/raw/panel_b'); outdir = p('data/panel')
os.makedirs(rawdir, exist_ok=True); os.makedirs(outdir, exist_ok=True)
total = len(dyads) * len(DISC)
t0 = time.time(); done = 0; fails = []; manrows = []; consec_fail = 0
print('start: dyads=%d discs=%d total_cells=%d est_base_h=%.1f (extra pages not counted)' %
      (len(dyads), len(DISC), total, total * 3.5 / 3600), flush=True)
try:
    for d in dyads:
        for dname, dkey, dfilter in DISC:
            mp, col = d['mp_iso'], d['col_iso']
            flt = ('authorships.countries:%s,authorships.countries:%s,%s,from_publication_date:1990-01-01'
                   % (mp, col, dfilter))
            p1fp = os.path.join(rawdir, '%s__%s__%s__p1.json' % (mp, col, dkey))
            try:
                j1 = getpage(flt, 1, p1fp)
                count = j1.get('meta', {}).get('count') or 0
                pages = math.ceil(count / 200) if count else 1
                for pg in range(2, pages + 1):
                    time.sleep(1.0)  # polite gap between pages of the same cell
                    getpage(flt, pg, os.path.join(rawdir, '%s__%s__%s__p%d.json' % (mp, col, dkey, pg)))
                manrows.append([mp, col, dname, count, pages])
                consec_fail = 0
            except Exception as e:
                fails.append('%s__%s__%s' % (mp, col, dkey))
                print('FAIL %s %s %s: %r' % (mp, col, dkey, e), flush=True)
                consec_fail += 1
                if consec_fail >= 10:
                    print('CIRCUIT_BREAK 10 consecutive fails -> sleep 1800s (quota window?)', flush=True)
                    time.sleep(1800)
                    consec_fail = 0
            done += 1
            time.sleep(2.0)
            if done % 50 == 0:
                el = time.time() - t0
                print('progress %d/%d elapsed=%.0fmin eta=%.0fmin fails=%d' %
                      (done, total, el / 60, el / done * (total - done) / 60, len(fails)), flush=True)
finally:
    with open(p('data/panel/b_fetch_manifest.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['mp_iso','col_iso','discipline','meta_count','pages'])
        w.writerows(manrows)
    nworks = sum(r[3] for r in manrows)
    print('DONE cells_written=%d/%d total_works=%d fails=%d %s' %
          (len(manrows), total, nworks, len(fails), fails[:10]), flush=True)
