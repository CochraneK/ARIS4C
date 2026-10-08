# code/audit_lookahead.py
# ARIS4C-004 stage3a T6: no-look-ahead audit.
# 1) Static scan of code/simcore_3.py, code/sim_m1.py, code/sim_m2.py:
#    confirm M1 recovery candidates are filtered by year < y and M2
#    reconnection candidates use only pre-t0 (year <= t0) information;
#    cite evidence line numbers.
# 2) Runtime log verification:
#    m1_lookahead_log.json  -> every entry worst_gap < 0
#                              (worst_gap = max_cited_year - y; None = no
#                              cited work, vacuously OK)
#    m2_lookahead_log.json  -> every entry max_year_used <= t0
# Outputs data/stage3/lookahead_audit.json. No network access.
import json
import re

S3 = 'data/stage3'

# required evidence per file: label -> regex (first match wins per line)
PATTERNS = {
    'code/simcore_3.py': {
        'M1_CONTRACT_year_lt_y': r'judged ONLY by works with year < y',
        'M1_BISECT_FIRST_GE_y': r'pos = bisect\.bisect_left\(yrs, y\)',
        'M1_SCAN_STARTS_BEFOR_y': r'j = pos - 1',
        'M1_SKIP_FOCAL_WORKS': r'while j >= 0 and lst\[j\]\[1\]:',
        'M2_CONTRACT_pre_t0': r'uses ONLY works with year <= t0',
        'M2_PRE_T0_FILTER': r'if yr is None or yr > t0:',
        'M2_MAX_YEAR_LEDGER': r'max_year_used = yr',
    },
    'code/sim_m1.py': {
        'M1_DOC_no_lookahead': r'no look-ahead by construction',
        'M1_CALL_same_path': r'm1_recovery\(works, by_concept, focal, deleted\)',
        'M1_LEDGER_WRITTEN': r"led\['%s\|%s' % \(focal, a\)\] = lg",
        'M1_RUNTIME_CHECK': r'M1 WORST_GAP_MAX',
    },
    'code/sim_m2.py': {
        'M2_DOC_pre_t0_only': r'uses ONLY pre-t0 information',
        'M2_CALL_same_path': r'm2_reconnect\(Gf, works, focal, t0, deleted\)',
        'M2_RUNTIME_GUARD': r"v\['max_year_used'\] > v\['t0'\]",
    },
}

static_scan = {}
static_ok = True
for path, pats in PATTERNS.items():
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    found = {}
    for label, pat in pats.items():
        rx = re.compile(pat)
        hits = [i + 1 for i, ln in enumerate(lines) if rx.search(ln)]
        found[label] = hits
        if not hits:
            static_ok = False
    static_scan[path] = found
    print('STATIC %s %s' % (path, 'OK' if all(found[p] for p in pats) else 'MISSING-EVIDENCE'))
    for label, hits in found.items():
        print('  %-28s lines=%s' % (label, hits[:6]))

with open(S3 + '/m1_lookahead_log.json', 'r', encoding='utf-8') as f:
    lg1 = json.load(f)
gaps = [v.get('worst_gap') for v in lg1.values()]
n_none1 = sum(1 for g in gaps if g is None)
nonnone1 = [g for g in gaps if g is not None]
m1_bad = [g for g in nonnone1 if not g < 0]
m1_ok = not m1_bad
m1_msg = ('OK: %d/%d entries worst_gap<0 (min=%s max=%s, none=%d)' % (
    len(lg1), len(lg1), min(nonnone1) if nonnone1 else None,
    max(nonnone1) if nonnone1 else None, n_none1)) if m1_ok else \
    ('VIOLATION: %d entries worst_gap>=0, e.g. %s' % (len(m1_bad), m1_bad[:3]))

with open(S3 + '/m2_lookahead_log.json', 'r', encoding='utf-8') as f:
    lg2 = json.load(f)
my = [v.get('max_year_used') for v in lg2.values()]
n_none2 = sum(1 for m in my if m is None)
nonnone2 = [m for m in my if m is not None]
m2_bad = [k for k, v in lg2.items()
          if v.get('max_year_used') is not None and v['max_year_used'] > v.get('t0')]
m2_ok = not m2_bad
m2_msg = ('OK: %d/%d entries max_year_used<=t0 (min=%s max=%s, none=%d)' % (
    len(lg2), len(lg2), min(nonnone2) if nonnone2 else None,
    max(nonnone2) if nonnone2 else None, n_none2)) if m2_ok else \
    ('VIOLATION: %d entries max_year_used>t0, e.g. %s' % (len(m2_bad), m2_bad[:3]))

verdict = 'PASS' if (static_ok and m1_ok and m2_ok) else 'FAIL'
out = {'static_scan': static_scan,
       'runtime_logs': {'m1': m1_msg, 'm2': m2_msg},
       'verdict': verdict}
with open(S3 + '/lookahead_audit.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2)
print('RUNTIME m1:', m1_msg)
print('RUNTIME m2:', m2_msg)
print('AUDIT_VERDICT', verdict)
