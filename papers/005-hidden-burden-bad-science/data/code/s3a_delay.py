# s3a_delay.py - stage3a T2 correction delay distribution (reads e1_numerators.csv; no imputation; negative delay report-only)
import pandas as pd, json
u = pd.read_csv('data/stage3/e1_numerators.csv')
d = u['delay_years'].dropna()
W = '校正延迟为notice级观测，受检出/公告延迟与日期质量影响，不得用于推断隐藏案例或 misconduct。'
out = {'n_valid': int(len(d)), 'n_na': int(u['delay_years'].isna().sum()),
 'median': float(d.median()), 'p25': float(d.quantile(.25)), 'p75': float(d.quantile(.75)), 'p90': float(d.quantile(.90)),
 'cdf_years': {str(y): float((d <= y).mean()) for y in [1, 3, 5, 10, 20]},
 'negative_delay_count': int((d < 0).sum()), 'negative_delay_note': 'RetractionDate早于OriginalPaperDate，日期质量问题，仅报告不处理',
 'same_year_0to1_share': float(((d >= 0) & (d < 1)).mean()), 'same_year_note': '有效delay中0<=delay<1占比',
 'by_bucket': {}}
for b, s in u.groupby('bucket'):
    dd = s['delay_years'].dropna()
    out['by_bucket'][str(b)] = {'n': int(len(dd)), 'median': (float(dd.median()) if len(dd) else None), 'cdf_5y': (float((dd <= 5).mean()) if len(dd) else None)}
out['detection_bias_warning'] = W
json.dump(out, open('data/stage3/correction_delay.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('OK median', out['median'], '| n', out['n_valid'], 'na', out['n_na'], '| neg', out['negative_delay_count'], '| same_year', round(out['same_year_0to1_share'], 4), '| cdf5y', round(out['cdf_years']['5'], 4))
