# S2: A-layer count panel. 1 request per (country x discipline), single page, idempotent.
# filter = authorships.countries:<ISO>,<disc filter verbatim>,from_publication_date:1990-01-01
# group_by=publication_year + per-page=1  (meta.count + year distribution in one page)
import json, csv, os, time, urllib.request, urllib.parse, urllib.error
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def p(*a): return os.path.join(R, *a)
UA = {'User-Agent': 'aris4c-003-stage3a/0.1 (local research)'}
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
    for wait in (0, 3, 6, 12, 24):  # backoff policy
        if wait: time.sleep(wait)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            last = e
            if e.code not in (429, 500, 502, 503, 504):
                raise
        except Exception as e:
            last = e
    raise RuntimeError('retries exhausted: %r' % last)
countries = list(csv.DictReader(open(p('data/manifests/country_panel.csv'), encoding='utf-8')))
rawdir, outdir = p('data/raw/panel_a'), p('data/panel')
os.makedirs(rawdir, exist_ok=True); os.makedirs(outdir, exist_ok=True)
total = len(countries) * len(DISC)
t0 = time.time(); done = 0; fails = []
print('start: countries=%d discs=%d total_requests=%d est_eta_min=%.0f' %
      (len(countries), len(DISC), total, total * 2.7 / 60), flush=True)
try:
    for c in countries:
        for dname, dkey, dfilter in DISC:
            fn = '%s__%s.json' % (c['iso'], dkey)
            fp = os.path.join(rawdir, fn)
            if os.path.exists(fp) and os.path.getsize(fp) > 0:
                done += 1
                continue
            flt = 'authorships.countries:%s,%s,from_publication_date:1990-01-01' % (c['iso'], dfilter)
            url = BASE + '?' + urllib.parse.urlencode(
                {'filter': flt, 'group_by': 'publication_year', 'per-page': '1'})
            try:
                open(fp, 'w', encoding='utf-8').write(fetch(url))
            except Exception as e:
                fails.append(fn)
                print('FAIL %s: %r' % (fn, e), flush=True)
            done += 1
            time.sleep(2.0)
            if done % 25 == 0:
                el = time.time() - t0
                print('progress %d/%d elapsed=%.0fmin eta=%.0fmin fails=%d' %
                      (done, total, el / 60, el / done * (total - done) / 60, len(fails)), flush=True)
finally:
    rows = []
    for c in countries:
        for dname, dkey, dfilter in DISC:
            fp = os.path.join(rawdir, '%s__%s.json' % (c['iso'], dkey))
            if not (os.path.exists(fp) and os.path.getsize(fp) > 0):
                continue
            j = json.load(open(fp, encoding='utf-8'))
            groups = {g['key']: g['count'] for g in j.get('group_by', []) if g.get('key')}
            rows.append([c['iso'], c['country_name'], dname, dfilter, '1990',
                         j.get('meta', {}).get('count'), json.dumps(groups)])
    with open(p('data/panel/a_layer_count.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['iso','country','discipline','filter_path','from_year','count','years_json'])
        w.writerows(rows)
    print('DONE rows_written=%d/%d fails=%d %s' %
          (len(rows), total, len(fails), fails[:10]), flush=True)
