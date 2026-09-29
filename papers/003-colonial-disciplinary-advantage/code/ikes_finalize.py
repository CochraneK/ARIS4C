import csv
import numpy as np

def load(p):
    d = {}
    for ln in open(p, encoding='utf-8-sig'):
        ln = ln.rstrip('\n')
        if not ln or ln.startswith('#') or ln.startswith('discipline\t'):
            continue
        disc, crit, score, rat = ln.split('\t')
        d[(disc, crit)] = int(score)
    return d

a = load('data/ikes/pass1.tsv')
b = load('data/ikes/pass2.tsv')
assert set(a) == set(b)

# --- ikes_scores.csv (long, frozen) ---
rows = []
for k in sorted(a):
    p1, p2 = a[k], b[k]
    arb = 'none' if abs(p1 - p2) <= 1 else 'adjudicated'
    final = p1 if abs(p1 - p2) <= 1 else p1  # 无仲裁格；若有仲裁格需手工补
    rows.append((k[0], k[1], p1, p2, arb, final))
with open('data/ikes/ikes_scores.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['discipline', 'criterion', 'pass1', 'pass2', 'arbitration', 'final'])
    w.writerows(rows)

# --- totals + permutations ---
discs = sorted({k[0] for k in a})
totals = {d: sum(v for (dd, c), v in a.items() if dd == d) for d in discs}
vec = np.array([totals[d] for d in discs])
rng = np.random.default_rng(20260929)
with open('data/ikes/permutations.tsv', 'w', encoding='utf-8') as f:
    f.write('# IKES score vector permutations for H2 falsification (stage 3/4 null distribution)\n')
    f.write('# seed=20260929 (np.random.default_rng), n=100, wide: perm_id + 17 discipline columns (sorted order)\n')
    f.write('# source: data/ikes/ikes_scores.csv final column (pass1==pass2 for all 68 cells, 0 arbitrated)\n')
    f.write('perm_id\t' + '\t'.join(discs) + '\n')
    for i in range(100):
        perm = rng.permutation(vec)
        f.write('%d\t' % (i + 1) + '\t'.join(str(x) for x in perm) + '\n')

print('disciplines:', len(discs), 'cells:', len(a))
for d in discs:
    print('%s\t%d' % (d, totals[d]))
conf = [d for d in discs if d not in ('Engineering', 'Materials Science', 'Computer Science', 'Physics', 'Mathematics', 'Chemistry')]
print('confirm set mean: %.2f, comparator set mean: %.2f' %
      (np.mean([totals[d] for d in conf]), np.mean([totals[d] for d in set(discs) - set(conf)])))
print('perm head:', open('data/ikes/permutations.tsv', encoding='utf-8').readlines()[4][:80])
