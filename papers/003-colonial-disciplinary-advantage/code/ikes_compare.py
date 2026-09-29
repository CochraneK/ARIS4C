import sys
def load(p):
    d = {}
    for ln in open(p, encoding='utf-8-sig'):
        ln = ln.rstrip('\n')
        if not ln or ln.startswith('#') or ln.startswith('discipline\t'):
            continue
        disc, crit, score, rat = ln.split('\t')
        d[(disc, crit)] = (int(score), rat)
    return d
a = load(sys.argv[1]); b = load(sys.argv[2])
assert set(a) == set(b), (set(a) - set(b), set(b) - set(a))
print('cells:', len(a))
diffs = 0
for k in sorted(a):
    da, db = a[k][0], b[k][0]
    d = abs(da - db)
    if d > 1:
        diffs += 1
        print('ARBITRATE\t%s\t%s\tp1=%d(%s)\tp2=%d(%s)' % (k[0], k[1], da, a[k][1][:24], db, b[k][1][:24]))
    elif d == 1:
        print('ok-diff1\t%s\t%s\t%d->%d' % (k[0], k[1], da, db))
tot = {}
for name, x in (('pass1', a), ('pass2', b)):
    for (disc, crit), (s, r) in x.items():
        tot.setdefault(name, {}).setdefault(disc, 0)
        tot[name][disc] += s
print('== totals ==')
for disc in sorted(set(list(tot['pass1']) + list(tot['pass2']))):
    t1, t2 = tot['pass1'][disc], tot['pass2'][disc]
    print('%s\tp1=%d\tp2=%d\tdiff=%d%s' % (disc, t1, t2, abs(t1 - t2), '  <--ARBITRATE' if abs(t1 - t2) > 1 else ''))
print('arbitrate cells:', diffs)
