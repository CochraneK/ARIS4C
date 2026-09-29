import json
fl = json.load(open('data/raw/fields.json', encoding='utf-8'))
print('n_fields', len(fl))
for f in fl:
    print(f['id'].split('/')[-1], '|', f['display_name'])
