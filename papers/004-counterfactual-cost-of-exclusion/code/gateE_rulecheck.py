"""T2 pre-check: verify frozen rule JSON is complete/valid; print key values. Read-only."""
import json

d = json.load(open('data/stage4/gateE_decision_rule.json', encoding='utf-8'))
print('keys:', list(d))
print('frozen_utc:', d['meta']['frozen_utc'])
print('grid:', d['grid']['N'], d['grid']['r'], 'pool', d['grid']['available_pool'])
print('D_alt:', d['criteria']['i_ci_width']['D_alt_median_focal'])
print('D_med:', d['criteria']['i_ci_width']['D_med'], 'threshold:', d['criteria']['i_ci_width']['threshold'])
print('vobs_max_deg:', d['standardization']['vobs_max_deg'])
for k, v in d['criteria']['ii_power']['effect_scales'].items():
    print('scale', k, v)
print('consistency:', d['consistency_checks']['median_of_median_missing_all_a'])
print('JSON_OK')
