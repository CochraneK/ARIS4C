# s3a_rates.py - stage3a T3 detection rate (denominator=222,714,158 stage2 P4 frozen; per 100k; + on-disk verify)
import pandas as pd, json, os
u = pd.read_csv('data/stage3/e1_numerators.csv')
DEN = 222714158
r = lambda n: round(100000.0 * n / DEN, 4)
e1 = u[u['bucket'] == 'E1_CANDIDATE']
W = 'notice级检出率非患病率：检出≠患病，E1_CANDIDATE为筛查候选（终裁模块B人工审计）；notice级reason≠裁定原因；RW覆盖随时空异质（检测偏倚）；不含国家misconduct排名与隐藏案例数。'
yy = e1.groupby('orig_year').size().reindex(range(2000, 2026), fill_value=0)
out = {'denominator': DEN, 'denominator_source': 'stage2 P4实测（2000-2025 publication_year口径）冻结值；秒级漂移只注记，重钉为段3b工作（1次）',
 'n_universe': int(len(u)), 'n_E1_CANDIDATE': int(len(e1)),
 'per_100k_all_retractions': r(len(u)), 'per_100k_E1_CANDIDATE': r(len(e1)),
 'by_orig_year_E1_CANDIDATE': {str(y): r(int(yy[y])) for y in range(2000, 2026)},
 'by_subject_E1_CANDIDATE': {str(k): r(int(n)) for k, n in e1.groupby('subject').size().sort_values(ascending=False).items()},
 'detection_bias_warning': W}
json.dump(out, open('data/stage3/detection_rates.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('OK per100k all', out['per_100k_all_retractions'], '| E1', out['per_100k_E1_CANDIDATE'], '| n_universe', out['n_universe'], '| n_E1', out['n_E1'])
c = json.load(open('data/stage3/e1_counts.json', encoding='utf-8'))
print('COUNTS with_doi', c['with_doi'], 'no_doi', c['no_doi'], 'pre_dedup', c['pre_dedup'], 'na_rate', c['na_rate'])
print('VERIFY ls data/stage3:', sorted(f for f in os.listdir('data/stage3') if os.path.getsize('data/stage3/' + f) > 0))
print('VERIFY wc -l e1_numerators.csv:', sum(1 for _ in open('data/stage3/e1_numerators.csv', encoding='utf-8')))
