# 段2 接管：汇整 data/raw/probes/ 全部探针结果（编排器用，输出 <=40 行）
import json, glob, os, re

d = 'data/raw/probes'
rows = []
for f in sorted(glob.glob(os.path.join(d, '*'))):
    name = os.path.basename(f)
    if name.endswith('.json'):
        try:
            j = json.load(open(f, encoding='utf-8'))
            cnt = (j.get('meta') or {}).get('count')
            n_res = len(j.get('results') or [])
            rows.append((name, f'count={cnt} results={n_res}'))
        except Exception as e:
            rows.append((name, f'PARSE_ERR {type(e).__name__}'))
    elif name.endswith('.err4xx'):
        sz = os.path.getsize(f)
        head = open(f, encoding='utf-8', errors='replace').read(120).replace('\n', ' ')
        rows.append((name, f'ERR4xx size={sz} head={head!r}'))
    else:
        rows.append((name, f'other size={os.path.getsize(f)}'))

for name, info in rows:
    print(f'{name:32s} {info}')
print(f'TOTAL files={len(rows)}')
