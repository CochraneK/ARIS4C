# S1: mechanical export of main dyad set (stage3a). Zero subjective filtering.
# exposure_pair_merged.csv x countries_oa.json, aliases from data/manifests/country_alias_map.tsv
import json, csv, os, sys, unicodedata
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def p(*a): return os.path.join(R, *a)

def norm(s):
    s = unicodedata.normalize('NFKD', s or '')
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace('&', ' and ')
    return ' '.join(s.split())

oa = json.load(open(p('data/raw/countries_oa.json'), encoding='utf-8'))
exact = {}
iso2 = {}
for c in oa:
    exact[norm(c['display_name'])] = c
    iso2[c['country_code']] = c
aliases = {}
for r in csv.DictReader(open(p('data/manifests/country_alias_map.tsv'), encoding='utf-8-sig'), delimiter='\t'):
    aliases[(r['role'], r['cow_code'])] = (r['iso'], r['note'])
rows = list(csv.DictReader(open(p('data/raw/exposure/exposure_pair_merged.csv'), encoding='utf-8-sig')))

def resolve(role, code, name):
    if name in ('?', ''):
        return None, 'unresolved name "?"'
    if norm(name) in exact:
        c = exact[norm(name)]
        return c['country_code'], 'exact'
    if (role, code) in aliases:
        iso, note = aliases[(role, code)]
        if iso == 'NA':
            return None, note
        if iso not in iso2:
            return None, 'alias ISO %s not in OA table' % iso
        return iso, 'alias: ' + note
    return None, 'NO RULE: not exact and not in alias map'

kept, excl, miss = [], [], []
for i, r in enumerate(rows, start=2):
    m_iso, m_how = resolve('mp', r['mp_code'], r['mp_name'])
    c_iso, c_how = resolve('col', r['col_code'], r['col_name'])
    for side, how in (('mp', m_how), ('col', c_how)):
        if how.startswith('NO RULE'):
            miss.append((i, side, r['mp_code'], r['mp_name'], r['col_code'], r['col_name'], how))
    if m_iso is None or c_iso is None:
        why = []
        if m_iso is None: why.append('mp: ' + m_how)
        if c_iso is None: why.append('col: ' + c_how)
        excl.append((i, r, '; '.join(why)))
        continue
    kept.append((r, m_iso, c_iso, m_how, c_how))

os.makedirs(p('data/manifests'), exist_ok=True)
w = csv.writer(open(p('data/manifests/dyad_set.csv'), 'w', newline='', encoding='utf-8'))
w.writerow(['mp_code','mp_name','mp_iso','mp_oa_id','col_code','col_name','col_iso','col_oa_id',
            'first','last','dur','src','occ_dur','mp_match','col_match','self_dyad'])
for r, mi, ci, mh, ch in kept:
    w.writerow([r['mp_code'], r['mp_name'], mi, iso2[mi]['id'], r['col_code'], r['col_name'],
                ci, iso2[ci]['id'], r['first'], r['last'], r['dur'], r['src'], r['occ_dur'],
                mh, ch, int(mi == ci)])
with open(p('data/manifests/dyad_exclusions.md'), 'w', encoding='utf-8') as f:
    f.write('# dyad_exclusions (stage3a S1, mechanical)\n\n'
            'total rows=339, excluded=%d, kept=%d. Mapping rules: exact OA display_name match > country_alias_map.tsv (241 entries, all recorded) > exclude.\n\n'
            '| csv_line | mp_code | mp_name | col_code | col_name | first-last | src | reason |\n'
            '|---|---|---|---|---|---|---|---|\n')
    for i, r, why in excl:
        f.write('| %d | %s | %s | %s | %s | %s-%s | %s | %s |\n' %
                (i, r['mp_code'], r['mp_name'], r['col_code'], r['col_name'], r['first'], r['last'], r['src'], why))
cpanel = {}
for r, mi, ci, mh, ch in kept:
    for role, iso in (('mp', mi), ('col', ci)):
        d = cpanel.setdefault(iso, {'mp': 0, 'col': 0, 'n': 0})
        d[role] += 1
for r, mi, ci, mh, ch in kept:
    for iso in {mi, ci}:
        cpanel[iso]['n'] += 1
w = csv.writer(open(p('data/manifests/country_panel.csv'), 'w', newline='', encoding='utf-8'))
w.writerow(['country_name','iso','oa_id','role','n_dyad'])
for iso in sorted(cpanel):
    d = cpanel[iso]
    role = 'both' if (d['mp'] and d['col']) else ('mp' if d['mp'] else 'col')
    w.writerow([iso2[iso]['display_name'], iso, iso2[iso]['id'], role, d['n']])
print('total=339 kept=%d excluded=%d countries=%d' % (len(kept), len(excl), len(cpanel)))
print('mp_roles=%d col_roles=%d both_roles=%d' % (
    sum(1 for d in cpanel.values() if d['mp'] and not d['col']),
    sum(1 for d in cpanel.values() if d['col'] and not d['mp']),
    sum(1 for d in cpanel.values() if d['mp'] and d['col'])))
print('self_dyads=%d' % sum(1 for r, mi, ci, mh, ch in kept if mi == ci))
if miss:
    print('!!! UNMAPPED ENTITIES (need alias entries):')
    for m in miss: print(m)
    sys.exit(1)
print('OK no unmapped entities')
