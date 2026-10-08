# Stage 2a summary - ARIS4C-004 (2nd attempt, D-6) - 2026-09-30

## Queue (target 4x75=300; works-bridge form D-1)
| stratum | first_pub window | selected | shortfall |
|---------|------------------|----------|-----------|
| math | [1840,1940] | 75 | 0 |
| cs | [1890,1940] | 33 | 42 |
| physics | [1840,1940] | 48 | 27 |
| biology | [1840,1940] | 34 | 41 |
Total 190/300; first_pub in [1840,1940]; OpenAlex queries 19 (cap 32), rate floor 503, stop never hit.

## Identity rules (queue 190)
R1 verified_orcid: 32 | R2 verified_triple: 41 | R3 collision_risk: 0 | R4 unresolved: 117
R4 share 62% - unresolved entities enter 2b with per-author works-list disambiguation (works lists out of 2a scope).

## Pilot 32 re-judgement (frozen R1-R4, local, 0 queries)
old {collision_risk 12 unresolved 17 verified 3} -> new {collision_risk 4 unresolved 17 verified_orcid 4 verified_triple 7}; 18 of 32 changed (data/identity_pilot_readjudication.csv).

## D-6
Death proxy switched last_pub<=1965 -> first_pub<=1940: contamination-immune (first_pub unaffected by appended 2022-26 works) + 150y cap dead-certain in 2026; evidence: prev run 14/300.

## Residual limitations
1. cs/physics/biology under cap 75: top-200 works page pool exhausted (no extra pages per frozen design).
2. R4 117 unresolved remain in queue; final identity re-check deferred to 2b (protocol S6).
3. first_pub<=1940 is a death proxy, not proof of death (no verified death date collected).

DONE stage2a 004
