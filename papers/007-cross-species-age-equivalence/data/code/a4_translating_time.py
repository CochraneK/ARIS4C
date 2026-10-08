"""A4: TT rank-OLS fit -> human_eq_years; tableE_partial + tt_fit + tt_events + tableA -> tableE.csv."""
import csv
Y = 365.25
M = {'Human': 'Human', 'Mouse / Mouse  / Wild mouse': 'Mouse',
     'European rabbit': 'Rabbit', 'Cat / Domestic cat': 'Cat'}
fit = {r['species']: (float(r['onset']), float(r['slope']),
                      float(r['pc_min_l']), float(r['pc_max_u']),
                      r['pc_min_l'].strip(), r['pc_max_u'].strip())
       for r in csv.DictReader(open('data/tt_fit.csv', encoding='utf-8-sig'))}
ev = {}
for r in csv.DictReader(open('data/tt_events.csv', encoding='utf-8-sig')):
    ev.setdefault(r['species'], []).append((float(r['pc_median']),
                                            float(r['lower95']), float(r['upper95'])))
for sp in ev:
    ev[sp].sort()
gest = {r['species_id']: float(r['gestation_days'])
        for r in csv.DictReader(open('data/tableA_species.csv', encoding='utf-8-sig'))}
assert len(fit) == 18 and len(ev) == 18 and all(len(v) == 10 for v in ev.values())

def interp(x, p):
    if x <= p[0][0]:
        x1, y1, x2, y2 = p[0][0], p[0][1], p[1][0], p[1][1]
    elif x >= p[-1][0]:
        x1, y1, x2, y2 = p[-2][0], p[-2][1], p[-1][0], p[-1][1]
    else:
        for i in range(len(p) - 1):
            if p[i][0] <= x <= p[i + 1][0]:
                x1, y1, x2, y2 = p[i][0], p[i][1], p[i + 1][0], p[i + 1][1]; break
    if abs(x2 - x1) < 1e-12:
        return 0.5 * (y1 + y2)
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
oh, sh = fit['Human'][0], fit['Human'][1]
rows = list(csv.reader(open('data/tableE_partial.csv', encoding='utf-8-sig')))
hdr, data = rows[0], rows[1:]
assert len(data) == 216
a4, st, ex, seen = [], {}, None, set()
for r in data:
    sp, sid, q, ay = r[0], r[1], r[2], r[3]
    if (sp, q) in seen:
        continue
    seen.add((sp, q))
    tt = M.get(sp)
    if tt is None:
        a4.append([sp, sid, q, ay, 'A4', '', '', '', 'human_eq_years', 'species not in Translating Time 11-event subset'])
        continue
    on, sl, lo_f, hi_f, lo_s, hi_s = fit[tt]
    t = float(ay) * Y + gest[sid]
    th = lambda x: oh + sh * (x - on) / sl
    m = th(t) / Y
    l, h = th(interp(t, [(x, a) for x, a, b in ev[tt]])) / Y, th(interp(t, [(x, b) for x, a, b in ev[tt]])) / Y
    in_ = lo_f <= t <= hi_f
    note = 'in_domain' if in_ else f'out_of_domain=true; TT 11-event domain [{lo_s},{hi_s}] d PC'
    a4.append([sp, sid, q, ay, 'A4', f'{l:.4f}', f'{h:.4f}', f'{m:.4f}', 'human_eq_years', note])
    s = st.setdefault(tt, [0, 0, 1e18, 0.0]); s[0] += in_; s[1] += not in_; s[2] = min(s[2], t); s[3] = max(s[3], t)
    if sp == 'Human' and q == '0.9' and ex is None:
        ex = (q, ay, t, m, l, h)
with open('data/tableE.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(hdr); w.writerows(data); w.writerows(a4)
nc = sum(1 for a in a4 if a[5])
for tt in ('Human', 'Mouse', 'Cat', 'Rabbit'):
    print(f'{tt}: in={st[tt][0]} out={st[tt][1]}  t_pc {st[tt][2]:.0f}-{st[tt][3]:.0f} d PC')
print(f'example Human q={ex[0]} a={ex[1]}y t_pc={ex[2]:.1f}d out_mid={ex[3]:.4f} [out_low={ex[4]:.4f}, out_high={ex[5]:.4f}]')
print(f'A4: {nc} computed, {54-nc} empty; tableE.csv {216+len(a4)} data rows')
