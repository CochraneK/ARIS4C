"""
SPOKE-SAFE E1-E2 Pilot 测量学分析 (n=90)
"""
import json, math, itertools
from collections import defaultdict

results = []
with open('scored_results.jsonl') as f:
    for line in f:
        results.append(json.loads(line))

by_level = defaultdict(list)
for r in results:
    by_level[r['level']].append(r)
levels_sorted = sorted(by_level.keys())

def mean(xs): return sum(xs)/len(xs)
def sd(xs):
    m = mean(xs)
    return math.sqrt(sum((x-m)**2 for x in xs)/(len(xs)-1))

# ============================================================
# 1. 描述性统计
# ============================================================
print('='*80)
print('1. 描述性统计 (Mean ± SD)')
print('='*80)
print(f'{"级别":>5} {"n":>4} {"PC":>20} {"SA":>20} {"PA":>20}')
print('-'*70)
for lv in levels_sorted:
    items = by_level[lv]
    pc = [i['score']['power_challenge'] for i in items]
    sa = [i['score']['safety_appropriateness'] for i in items]
    pa = [i['score']['patient_alliance'] for i in items]
    print(f'{lv:>5} {len(items):>4}  {mean(pc):.2f}±{sd(pc):.2f}  {mean(sa):.2f}±{sd(sa):.2f}  {mean(pa):.2f}±{sd(pa):.2f}')
all_pc = [r['score']['power_challenge'] for r in results]
all_sa = [r['score']['safety_appropriateness'] for r in results]
all_pa = [r['score']['patient_alliance'] for r in results]
print(f'{"ALL":>5} {len(results):>4}  {mean(all_pc):.2f}±{sd(all_pc):.2f}  {mean(all_sa):.2f}±{sd(all_sa):.2f}  {mean(all_pa):.2f}±{sd(all_pa):.2f}')

# ============================================================
# 2. 维度间相关性
# ============================================================
print()
print('='*80)
print('2. 维度间相关性 (Pearson r, n=90)')
print('='*80)
dims = {'PC': all_pc, 'SA': all_sa, 'PA': all_pa}
for (n1,d1),(n2,d2) in itertools.combinations(dims.items(),2):
    n = len(d1)
    sxy = sum((d1[i]-mean(d1))*(d2[i]-mean(d2)) for i in range(n))
    r_val = sxy/((n-1)*sd(d1)*sd(d2))
    print(f'  r({n1},{n2}) = {r_val:.4f}')

# ============================================================
# 3. Spearman 相关: 严重级别 vs 维度
# ============================================================
print()
print('='*80)
print('3. 严重级别 vs 维度 (Spearman ρ)')
print('='*80)
sev_map = {'S0':0,'S1':1,'S2':2,'S3':3,'S4':4,'S5':5}
def spearman_rho(xs, ys):
    n = len(xs)
    x_sorted = sorted((x,i) for i,x in enumerate(xs))
    y_sorted = sorted((y,i) for i,y in enumerate(ys))
    x_rank = [0]*n
    y_rank = [0]*n
    for r,(_,i) in enumerate(x_sorted):
        x_rank[i] = r+1
    for r,(_,i) in enumerate(y_sorted):
        y_rank[i] = r+1
    d2 = sum((x_rank[i]-y_rank[i])**2 for i in range(n))
    return 1 - 6*d2/(n*(n*n-1))
sev_vals = [sev_map[r['level']] for r in results]
for dim_name, dim_data in [('PC',all_pc),('SA',all_sa),('PA',all_pa)]:
    rho = spearman_rho(sev_vals, dim_data)
    print(f'  ρ(severity,{dim_name}) = {rho:.4f}')

# ============================================================
# 4. Cohen d 效应量
# ============================================================
print()
print('='*80)
print('4. 相邻级别 Cohen d')
print('='*80)
def cohen_d(xs, ys):
    n1, n2 = len(xs), len(ys)
    s1, s2 = sd(xs), sd(ys)
    sp = math.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2)/(n1+n2-2))
    return (mean(ys)-mean(xs))/sp
print(f'{"对比":>12} {"d(PC)":>10} {"d(SA)":>10} {"d(PA)":>10}')
print('-'*45)
for i in range(len(levels_sorted)-1):
    lv1, lv2 = levels_sorted[i], levels_sorted[i+1]
    items1, items2 = by_level[lv1], by_level[lv2]
    pc1=[r['score']['power_challenge'] for r in items1]; pc2=[r['score']['power_challenge'] for r in items2]
    sa1=[r['score']['safety_appropriateness'] for r in items1]; sa2=[r['score']['safety_appropriateness'] for r in items2]
    pa1=[r['score']['patient_alliance'] for r in items1]; pa2=[r['score']['patient_alliance'] for r in items2]
    print(f'{lv1}→{lv2:>6}  {cohen_d(pc1,pc2):>+8.3f}  {cohen_d(sa1,sa2):>+8.3f}  {cohen_d(pa1,pa2):>+8.3f}')
# S0→S5
pc0=[r['score']['power_challenge'] for r in by_level['S0']]; pc5=[r['score']['power_challenge'] for r in by_level['S5']]
sa0=[r['score']['safety_appropriateness'] for r in by_level['S0']]; sa5=[r['score']['safety_appropriateness'] for r in by_level['S5']]
pa0=[r['score']['patient_alliance'] for r in by_level['S0']]; pa5=[r['score']['patient_alliance'] for r in by_level['S5']]
print(f'{"S0→S5":>12}  {cohen_d(pc0,pc5):>+8.3f}  {cohen_d(sa0,sa5):>+8.3f}  {cohen_d(pa0,pa5):>+8.3f}')

# ============================================================
# 5. 天花板/地板效应
# ============================================================
print()
print('='*80)
print('5. 天花板/地板效应')
print('='*80)
for dim_name, dim_data in [('PC',all_pc),('SA',all_sa),('PA',all_pa)]:
    ceil_pct = sum(1 for d in dim_data if d >= 9)/len(dim_data)*100
    floor_pct = sum(1 for d in dim_data if d <= 3)/len(dim_data)*100
    print(f'  {dim_name}: 天花板(>=9): {ceil_pct:.0f}%  |  地板(<=3): {floor_pct:.0f}%')

# ============================================================
# 6. SA-PC 权衡
# ============================================================
print()
print('='*80)
print('6. SA-PC 权衡 (PC-SA差, 单样本t检验)')
print('='*80)
for lv in levels_sorted:
    items = by_level[lv]
    diffs = [i['score']['power_challenge'] - i['score']['safety_appropriateness'] for i in items]
    m, s = mean(diffs), sd(diffs)
    t = m / (s/math.sqrt(len(diffs)))
    label = '安全倾斜' if m < 0 else ('挑战倾斜' if m > 0 else '平衡')
    print(f'  {lv}: PC-SA差 = {m:+.2f}±{s:.2f},  t({len(diffs)-1}) = {t:.3f}  [{label}]')

# ============================================================
# 7. Welch t-test: SA 相邻级别差异
# ============================================================
print()
print('='*80)
print('7. SA 相邻级别差异 (Welch t-test)')
print('='*80)
def welch_t(xs, ys):
    m1,m2,n1,n2 = mean(xs),mean(ys),len(xs),len(ys)
    v1,v2 = sd(xs)**2,sd(ys)**2
    t = (m2-m1)/math.sqrt(v1/n1+v2/n2)
    df = (v1/n1+v2/n2)**2 / ((v1/n1)**2/(n1-1)+(v2/n2)**2/(n2-1))
    return t, df
print(f'{"对比":>12} {"ΔSA":>8} {"t":>8} {"df":>6} {"sig":>6}')
print('-'*45)
for i in range(len(levels_sorted)-1):
    lv1, lv2 = levels_sorted[i], levels_sorted[i+1]
    sa1 = [r['score']['safety_appropriateness'] for r in by_level[lv1]]
    sa2 = [r['score']['safety_appropriateness'] for r in by_level[lv2]]
    t, df = welch_t(sa1, sa2)
    sig = '*' if abs(t) > 1.96 else ''
    print(f'{lv1}→{lv2:>6}  {mean(sa2)-mean(sa1):>+7.2f}  {t:>+7.3f}  {df:>5.1f}  {sig:>5}')
# S3→S5
sa3=[r['score']['safety_appropriateness'] for r in by_level['S3']]
sa5=[r['score']['safety_appropriateness'] for r in by_level['S5']]
t, df = welch_t(sa3, sa5)
print(f'{"S3→S5":>12}  {mean(sa5)-mean(sa3):>+7.2f}  {t:>+7.3f}  {df:>5.1f}  {"*" if abs(t)>1.96 else ""}')

# ============================================================
# 8. 摘要
# ============================================================
print()
print('='*80)
print('8. 摘要')
print('='*80)
print()
print('┌──────────────────────────────────────────────────────────────┐')
print('│  SPOKE-SAFE E1-E2 Pilot 测量学报告 (n=90, 每级15条)        │')
print('├──────────────────────────────────────────────────────────────┤')
print('│  维度独立性: PC-SA r=0.14, PC-PA r=-0.05  → 近正交          │')
print('│  Severity-SA:  ρ=0.76  → 严重级别强预测SA提升               │')
print('│  Severity-PC:  ρ=0.31  → 弱正相关 (一致挑战不因级别妥协)    │')
print('│  天花板:  PC 15.6%, SA 27.8%  → 可接受                      │')
print('│  地板:  0% → 无低分案例, 所有回复质量达标                   │')
print('│  效应量: S3→S4 SA跃升 d=+3.4 (t=9.95) → 明确的分级阈值     │')
print('│  S4/S5 SA显著高于S0-S3 → 安全优先行为被自动激活             │')
print('└──────────────────────────────────────────────────────────────┘')
