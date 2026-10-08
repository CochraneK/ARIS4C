# s3a_numerators.py - ARIS4C-005 stage3a module A: E1 numerator (Retraction only/universe 2000-2025/unit=unique original paper/no-doi separate)
import pandas as pd, json, hashlib, sys; PW, MAPF, MP = 'data/raw/rw_official/retraction_watch.csv', 'data/rw_e1_mapping.csv', 'data/manifests/rw_csv_manifest.json'
def pt(s):
    try:
        d = str(s).strip().split(' ')[0].split('/')
        yi = int(d[2]); return pd.Timestamp(yi if yi >= 100 else 2000 + yi if yi < 70 else 1900 + yi, int(d[0]), int(d[1]))
    except Exception:
        return pd.NaT
m = pd.read_csv(MAPF, skiprows=3)
bki = next((i for i in range(m.shape[1]) if set(m.iloc[:, i].astype(str).str.strip().str.upper()) <= {'E1_CANDIDATE', 'NON_E1', 'UNDECIDED'}), 2)
mp = {str(a).strip().lower(): str(b).strip().upper() for a, b in zip(m.iloc[:, 0], m.iloc[:, bki])}
h = hashlib.sha256(open(PW, 'rb').read()).hexdigest()
mm = json.load(open(MP, encoding='utf-8'))
sha_m = str(mm.get('sha256', '')).lower()
if h != sha_m: print('T0 FAIL sha256 mismatch', h[:16], sha_m[:16]); sys.exit(1)
df = pd.read_csv(PW, dtype=str, keep_default_na=False, encoding='utf-8-sig')
df = df[[c for c in df.columns if str(c).strip()]]
df['odt'] = df['OriginalPaperDate'].map(pt); df['rdt'] = df['RetractionDate'].map(pt); df['oy'] = df['odt'].dt.year; df['doi'] = df['OriginalPaperDOI'].str.strip()
r = df[df['RetractionNature'].str.strip().str.lower() == 'retraction'].copy(); hd = r['doi'] != ''
g = r[hd].sort_values('rdt', na_position='first').groupby('doi', sort=False); multi = int((g.size() > 1).sum())
u = pd.concat([g.tail(1), r[~hd]], ignore_index=True)
ex = {'pre2000': int(((u['oy'] < 2000) & u['oy'].notna()).sum()), 'post2025': int((u['oy'] > 2025).sum()), 'na_year': int(u['oy'].isna().sum())}
u = u[u['oy'].between(2000, 2025)].copy(); u['oy'] = u['oy'].astype(int)
def bk(x):
    bs = [mp.get(p, 'UNDECIDED') for p in str(x).lower().split(';') if p.strip()]
    return 'E1_CANDIDATE' if 'E1_CANDIDATE' in bs else 'NON_E1' if 'NON_E1' in bs else 'UNDECIDED'
u['bucket'] = u['Reason'].map(bk); u['n_reasons'] = u['Reason'].map(lambda x: len([p for p in str(x).split(';') if p.strip()]))
u['delay_years'] = (u['rdt'] - u['odt']) / pd.Timedelta(days=365.25)
unm = sorted({p.strip().lower() for x in r['Reason'] for p in str(x).split(';') if p.strip() and p.strip().lower() not in mp})
u = u.rename(columns={'oy': 'orig_year', 'Subject': 'subject', 'Country': 'country'}); u['retraction_year'] = u['rdt'].dt.year.astype('Int64')
u[['doi', 'orig_year', 'subject', 'country', 'bucket', 'n_reasons', 'retraction_year', 'delay_years']].to_csv('data/stage3/e1_numerators.csv', index=False)
byy, bys = {}, {}
for y, s in u.groupby('orig_year'): byy[int(y)] = {'total': int(len(s)), **{str(k): int(v) for k, v in s['bucket'].value_counts().items()}}
for s, g2 in u.groupby('subject', dropna=False): bys[str(s)] = {'total': int(len(g2)), **{str(k): int(v) for k, v in g2['bucket'].value_counts().items()}}
cnt = {'total': int(len(u)), 'by_bucket': {str(k): int(v) for k, v in u['bucket'].value_counts().items()}, 'by_orig_year': byy, 'by_subject': bys,
 'country_top20': {str(k): int(v) for k, v in u['country'].value_counts().head(20).items()}, 'with_doi': int((u['doi'] != '').sum()), 'no_doi': int((u['doi'] == '').sum()),
 'na_rate': {'orig_date': float(u['odt'].isna().mean()), 'retraction_date': float(u['rdt'].isna().mean())}, 'unmapped_reasons': unm, 'unmapped_count': len(unm),
 'pre_dedup': {'retraction_notices': int(len(r)), 'unique_papers_with_doi': int(hd.sum()), 'multi_notice_dois': multi, 'no_doi_notices': int((~hd).sum())}, 'map_bucket_col': int(bki),
 'excluded_universe': ex, 'input_sha256': h, 'manifest_sha256': sha_m, 'sha256_match': True, 'script_lines': sum(1 for _ in open(__file__, encoding='utf-8')),
 'detection_bias_warning': 'notice级检出率非患病率：检出≠患病，E1_CANDIDATE为筛查候选（终裁模块B）；notice级reason≠裁定；RW覆盖随时空异质。'}
json.dump(cnt, open('data/stage3/e1_counts.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False); print('OK total', len(u), dict(u['bucket'].value_counts()), ex, multi, bki, h[:8], len(unm))
