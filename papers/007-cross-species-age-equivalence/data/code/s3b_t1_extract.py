import pandas as pd, json, os
os.makedirs('data/raw', exist_ok=True)
t = pd.read_csv('data/tableE.csv')
t['species'] = t['species'].astype(str).str.strip()
print('cols:', t.columns.tolist())
print('methods:', t['method'].value_counts().to_dict())
print('species:', sorted(t['species'].unique()))
q = t[t['method'].isin(['A0','A1','A2','A3','A4'])].drop_duplicates(['species','q'])[['species','q','a_years']].sort_values(['species','q'])
q.to_csv('data/s3b_quantiles.csv', index=False)
an = pd.read_csv('data/suppl/anage_lu2023_snapshot.csv', header=1)
mc = [c for c in an.columns if 'maxanAge' in str(c)][0]
sl = [c for c in an.columns if 'SpeciesLatinName' in str(c)][0]
M = {'Human':'Homo sapiens','Mouse':'Mus musculus','Wild mouse':'Mus musculus','Cat':'Felis catus','Domestic cat':'Felis catus','European rabbit':'Oryctolagus cuniculus','Dog':'Canis lupus familiaris','Horse':'Equus caballus','Domestic pig':'Sus scrofa domesticus','Chimpanzee':'Pan troglodytes','Meerkat':'Suricata suricatta'}
out = {}
for sp in sorted(t['species'].unique()):
    lat = M.get(sp, sp); rr = an[an[sl].astype(str).str.strip() == lat]
    out[sp] = {'latin': lat, 'maxanAge': (float(rr[mc].iloc[0]) if len(rr) else None)}
json.dump(out, open('data/raw/s3b_anchors.json','w'), indent=1)
print({k: v['maxanAge'] for k, v in out.items()})
print('human a_years:', sorted(t[t['species']=='Human']['a_years'].unique()))
