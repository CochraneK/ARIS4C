# Disagreement Taxonomy · ARIS4C-023 calibration v0.1

## Scope and inputs

- Coder A: `data/calibration/coder_A.csv` (GLM substitute for Qoder/Qwen) — 36 present / 72 absent / 5 uncertain / 7 not_observed.
- Coder B: `data/calibration/coder_B.csv` (DeepSeek-V4.1-Flash) — 40 present / 74 absent / 6 uncertain / 0 not_observed.
- Scorer: `code/score_calibration.py` → `data/calibration/reliability.json`.
- Frozen taxonomy categories (from `../process/CALIBRATION_PLAN.md`): **definition**, **translation**, **incomplete witness**, **chronology**, **ontology overlap**.

## Headline reliability

| statistic | value |
|---|---|
| four-state raw agreement (n = 120) | **0.825** (99/120) |
| four-state Cohen kappa | 0.669 |
| four-state Gwet AC1 | 0.788 |
| binary present/absent subset (n = 103) | raw **0.951**, kappa **0.894**, AC1 **0.911** |
| four-state raw agreement excluding the exposure-contaminated cell | 0.824 (98/119) |
| agreement pairs | 99 — 34 present/present, 64 absent/absent, 1 uncertain/uncertain |
| disagreements | **21** |

## The 21 disagreements, classified

### 1. Missingness-vocabulary boundary — *incomplete witness* (7 cells)

| cell | A | B | note |
|---|---|---|---|
| P_ANTH_SUM × ANTH_EARTH_DUST | not_observed | absent | locator is one surviving sentence inside a heavily lacunose Segment A |
| P_ANTH_SUM × ANTH_CLAY_MUD | not_observed | absent | as above |
| P_ANTH_SUM × ANTH_POTTER_FORMING | not_observed | absent | as above |
| P_ANTH_SUM × ANTH_DIVINE_BLOOD_FLESH | not_observed | absent | as above |
| P_ANTH_SUM × ANTH_BREATH_ANIMATION | not_observed | absent | as above |
| P_ANTH_SUM × ANTH_BODY_SACRIFICE | not_observed | absent | as above |
| P_DIV_ULLI × DIV_COUNCIL | not_observed | absent | locator tablet/column attribution is itself philologically uncertain |

This is a single, consistent boundary rather than six independent errors: Coder A treats a bare mention inside a fragmentary witness as *no usable evidence*, Coder B treats an engaged motif family as scorable and therefore *absent*. It accounts for 7/21 disagreements but only 7/120 = **5.8 % of packets**.

### 2. Ontology overlap between sibling motifs — *ontology overlap* (3 cells)

| cell | A | B | overlapping pair |
|---|---|---|---|
| P_ANTH_ATRA × ANTH_BODY_SACRIFICE | uncertain | absent | ANTH_BODY_SACRIFICE ↔ ANTH_DIVINE_BLOOD_FLESH |
| P_ANTH_ATRA × ANTH_EARTH_DUST | absent | present | ANTH_EARTH_DUST ↔ ANTH_CLAY_MUD |
| P_ANTH_ATRA × ANTH_BREATH_ANIMATION | absent | uncertain | ANTH_BREATH_ANIMATION ↔ the divine-spirit component of ANTH_DIVINE_BLOOD_FLESH |

All three sit on the Atrahasis creation passage, where clay, divine flesh-and-blood and a residual divine spirit co-occur in one short sequence — exactly the configuration the sibling rules do not disjoin.

### 3. Inclusion-rule precision — *definition* (10 cells)

| cell | A | B | unresolved question |
|---|---|---|---|
| P_ANTH_GEN × ANTH_POTTER_FORMING | uncertain | present | does the potter's forming verb alone instantiate "molding/shaping", without a wheel or implement? |
| P_ANTH_ATRA × ANTH_POTTER_FORMING | absent | uncertain | does "mix clay … do the making" satisfy craft-forming? |
| P_DIV_HES_SUCC × DIV_COUNCIL | absent | present | is a three-deity private counsel a "divine council"? |
| P_DIV_HES_SUCC × DIV_SUCCESSION_YOUNGER_OLDER | uncertain | present | does a *foretold* displacement count, or must it be narrated? |
| P_DIV_HES_SUCC × DIV_KINGSHIP_TRANSFER | absent | present | same question for kingship transfer: foretold or effected? |
| P_DIV_HES_SUCC × DIV_PRIMORDIAL_REBELLION | absent | uncertain | does a retrospective reference inside the locator count when the rebellion itself is narrated elsewhere? |
| P_DIV_HES_TYPH × DIV_PRIMORDIAL_REBELLION | present | absent | does a monster attack carried out by Earth's own child carry a rebellion frame? |
| P_DIV_BAAL × DIV_PRIMORDIAL_REBELLION | present | uncertain | is resistance to El's grant of kingship a rebellion frame, and does it live inside the locator? |
| P_DIV_ULLI × DIV_FATHER_SON | absent | uncertain | do the *combatants* have to be father and son, or does a paternal plot frame suffice? |
| P_DIV_ULLI × DIV_SUCCESSION_YOUNGER_OLDER | uncertain | absent | the rule names one direction (younger displaces older); the Ullikummi battle runs the other way |

### 4. Language/term mapping — *translation* (1 cell)

| cell | A | B | note |
|---|---|---|---|
| P_ANTH_NUWA × ANTH_EARTH_DUST | absent | present | 黄土 ("yellow earth") and 摶 (knead) do not map one-to-one onto the earth/dust versus clay/mud distinction; the same cell is simultaneously the overlap case of §2 |

### 5. Chronology — *chronology* (0 cells)

No disagreement was caused by tradition dating, witness strata or the Egypt Middle/New Kingdom split. The packet's chronology cautions were not a source of unreliability in this round.

## Structure of the disagreements

- **By pair type:** not_observed→absent 7; absent→uncertain 4; absent→present 4; uncertain→absent 2; uncertain→present 2; present→uncertain 1; present→absent 1.
- **Asymmetry:** Coder B is the softer coder in both directions — B alone used `uncertain` 4 times where A said `absent`, and B said `present` 4 times where A said `absent`. Only one cell runs the other way for presence (P_DIV_HES_TYPH × DIV_PRIMORDIAL_REBELLION, A present / B absent). This is a *coder-level*, not a passage-level, difference, and it must be named as such when the numbers are reported.
- **By passage:** P_ANTH_SUM 6, P_ANTH_ATRA 4, P_DIV_HES_SUCC 4, P_DIV_ULLI 3, P_ANTH_GEN 1, P_ANTH_NUWA 1, P_DIV_BAAL 1, P_DIV_HES_TYPH 1. Three of fifteen passages carry 14/21 = 67 % of all disagreement.
- **By motif (agreement out of 5):** ANTH_EARTH_DUST 2, ANTH_POTTER_FORMING 2, DIV_PRIMORDIAL_REBELLION 2, ANTH_BODY_SACRIFICE 3, ANTH_BREATH_ANIMATION 3, DIV_COUNCIL 3, DIV_SUCCESSION_YOUNGER_OLDER 3; the remaining 17 motifs agree on 4/5 or 5/5.
- **No disagreement at all** on: FLOOD_* (all 8 motifs, 40 cells), DIV_STORM_SERPENT, DIV_STORM_SEA, DIV_BODY_TO_COSMOS, DIV_FATHER_SON (4/5), ANTH_CREATED_FOR_SERVICE, ANTH_FIRST_PAIR, DIV_KINGSHIP_TRANSFER (4/5). The transmission-sensitive flood family and the storm-serpent/storm-sea separation — the distinctions the plan cared most about — reproduced perfectly across model families.

## Boundary statements implied by this taxonomy

These are the rulings that have to be written into the ontology before it is expanded beyond the calibration set (see `RELIABILITY_DECISION.md`):

1. `not_observed` is reserved for evidence that is missing from the witness (a marked lacuna swallowing the relevant content) or outside the passage's scope. A passage that engages the motif or its family but does not contain the element is `absent`, even if the surrounding text is fragmentary.
2. Every sibling pair must be made mutually exclusive in the rule text: ANTH_EARTH_DUST ⊥ ANTH_CLAY_MUD; ANTH_BODY_SACRIFICE ⊥ ANTH_DIVINE_BLOOD_FLESH; ANTH_BREATH_ANIMATION ⊥ the divine-spirit component of ANTH_DIVINE_BLOOD_FLESH.
3. "Foretold" and "effected" must be separated explicitly for DIV_SUCCESSION_YOUNGER_OLDER and DIV_KINGSHIP_TRANSFER.
4. Direction must be stated for DIV_SUCCESSION_YOUNGER_OLDER (younger displaces older) and scope for DIV_PRIMORDIAL_REBELLION (who rebels against whom, and inside which locator).
5. For DIV_COUNCIL, a collective body acting as such is required; a private counsel among related deities is not a council.
6. The P_ANTH_SUM locator (ETCSL 1.7.4 Segment A 10-14) is too thin to carry six motif judgments and needs a replacement or widened witness before the Sumerian anthropogony cell enters any confirmatory analysis.
