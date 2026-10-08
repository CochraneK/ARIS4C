# S3 (stage3a): B-layer works fetch. stage3a runs SMOKE only (1 dyad x 1 disc x 3 pages).
# dyad filter = authorships.countries:MP,authorships.countries:COL (comma = AND => co-authorship pair)
# full B-layer run is stage3b. per-page=200, idempotent, backoff, UA.
import json, os, sys, time, csv, urllib.request, urllib.parse, urllib.error
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def p(*a): return os.path.join(R, *a)
UA = {'User-Agent': 'aris4c-003-stage3a/0.1 (local research)'}
BASE = 'https://api.openalex.org/works'
MINING = 'concepts.id:https://openalex.org/C16674752'  # subject_freeze verbatim
def fetch(url):
    last = None
    for wait in (0, 3, 6, 12, 24):
        if wait: time.sleep(wait)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return r.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            last = e
            if e.code not in (429, 500, 502, 503, 504):
                raise
        except Exception as e:
            last = e
    raise RuntimeError('retries exhausted: %r' % last)
def main():
    mp, col, pages, per_page = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]) if len(sys.argv) > 4 else 200
    rawdir = p('data/raw/panel_b'); os.makedirs(rawdir, exist_ok=True)
    flt = 'authorships.countries:%s,authorships.countries:%s,%s,from_publication_date:1990-01-01' % (mp, col, MINING)
    works = []
    meta_count = None
    for n in range(1, pages + 1):
        fn = '%s__%s__mining__p%d.json' % (mp, col, n)
        fp = os.path.join(rawdir, fn)
        if os.path.exists(fp) and os.path.getsize(fp) > 0:
            j = json.load(open(fp, encoding='utf-8'))
        else:
            url = BASE + '?' + urllib.parse.urlencode(
                {'filter': flt, 'per-page': str(per_page), 'page': str(n)})
            j = json.loads(fetch(url))
            open(fp, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False))
            time.sleep(2.0)
        if meta_count is None:
            meta_count = j.get('meta', {}).get('count')
        page = j.get('results', [])
        works.extend(page)
        if not page:
            break
    keys = {}
    for w in works:
        for k in w:
            keys[k] = keys.get(k, 0) + 1
    n = len(works)
    cover = {k: round(100.0 * v / n, 1) if n else 0 for k, v in sorted(keys.items(), key=lambda x: -x[1])}
    has_authorships = sum(1 for w in works if w.get('authorships'))
    auth_country_n = sum(1 for w in works if any(a.get('author', {}).get('last_authorship', {}).get('institution', {}).get('country_code') for a in w.get('authorships', [])))
    topics_n = sum(1 for w in works if w.get('topics'))
    doi_n = sum(1 for w in works if w.get('doi'))
    year_n = sum(1 for w in works if w.get('publication_year'))
    example = works[0]['id'] if works else None
    example_topics = works[0].get('topics', [{}])[0].get('display_name') if works and works[0].get('topics') else None
    out = p('data/panel/b_smoke.md')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('# B-layer works fetch SMOKE (stage3a S3)\n\n')
        f.write('scope: dyad %s-%s x Mining (concepts.id C16674752) x 3 pages @per-page=200, window >=1990\n' % (mp, col))
        f.write('filter: %s\n\n' % flt)
        f.write('meta.count=%s; fetched works=%d (pages=%d)\n\n' % (meta_count, n, min(pages, (n + per_page - 1) // per_page or 1)))
        f.write('## top-level field coverage over fetched works\n\n| field | coverage%% |\n|---|---|\n')
        for k, v in cover.items():
            f.write('| %s | %s |\n' % (k, v))
        f.write('\nrequired check: authorships=%d/%d, topics=%d/%d, publication_year=%d/%d, doi=%d/%d (doi absence = no DOI, normal)\n\n' %
                (has_authorships, n, topics_n, n, year_n, n, doi_n, n))
        f.write('example work id: %s (first topic: %s)\n\n' % (example, example_topics))
        f.write('raw: data/raw/panel_b/%s__%s__mining__p1..%d.json\n' % (mp, col, min(pages, 3)))
    print('smoke done: meta.count=%s works=%d example=%s' % (meta_count, n, example))
    print('cover: ' + json.dumps(cover))
if __name__ == '__main__':
    main()
