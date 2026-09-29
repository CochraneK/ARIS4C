import json, glob
for f in sorted(glob.glob('data/raw/probes/f_*.json')):
    j = json.load(open(f, encoding='utf-8'))
    print(f, 'meta=', j.get('meta'), 'nres=', len(j.get('results', [])))
    for r in j.get('results', [])[:6]:
        p = (r.get('parent') or {})
        print('   ', r.get('id'), '|', r.get('display_name'), '| parent:', p.get('id'), p.get('display_name'))
# also dump the 4xx error bodies fully
for f in sorted(glob.glob('data/raw/probes/*.err4xx')):
    print('===', f)
    print(open(f, encoding='utf-8').read()[:600])
