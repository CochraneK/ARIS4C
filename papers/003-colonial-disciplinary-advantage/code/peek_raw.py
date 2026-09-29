import json, glob
for f in sorted(glob.glob('data/raw/sub_*.json')):
    j = json.load(open(f, encoding='utf-8'))
    res = j.get('results', [])
    print(f, 'count=', j.get('meta', {}).get('count'))
    for r in res[:4]:
        p = r.get('parent') or {}
        print('   ', r['id'], '|', r['display_name'], '| level=', r.get('level'), '| parent=', p.get('id'), p.get('display_name'))
