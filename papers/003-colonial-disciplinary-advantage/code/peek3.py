import json
j = json.load(open('data/raw/sub_engineering.json', encoding='utf-8'))
print('count=', j['meta']['count'])
for r in j['results']:
    print('  ', r['id'], '|', r['display_name'])
