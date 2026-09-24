# Reliability Decision · ARIS4C-023 calibration v0.1

## What was run

```
python code/score_calibration.py \
  --a data/calibration/coder_A.csv \
  --b data/calibration/coder_B.csv \
  --out data/calibration/reliability.json
```

Run only after both packets were frozen in Git (`afa03bdc`, coder B packet; coder A packet frozen earlier at `38a07ae4`). No reliability output existed at any point while either coder was coding.

## Frozen freeze criteria (from `CALIBRATION_PLAN.md`) and their outcome

| criterion | required | observed | verdict |
|---|---|---|---|
| raw agreement on scorable items | ≥ 0.80 | **0.825** (99/120) | **pass** |
| recurring disagreement from the same undefined boundary | not > 10 % of packets | 7/120 = **5.8 %** (the missingness boundary) | **pass** |
| every motif has explicit inclusion and exclusion rules | required | 24/24 present in `motifs_v0.1.csv` | **pass** |
| uncertain / not-observed handling understood by both coders | required | same vocabulary used, different threshold | **conditional pass** — see §3 |

Supporting evidence, not gate criteria: four-state Cohen kappa 0.669 and Gwet AC1 0.788; on the binary present/absent subset (n = 103) raw agreement 0.951, kappa 0.894, AC1 0.911. The four-state kappa is depressed by the 7 not_observed→absent cells and by extreme prevalence (64 of 120 cells are absent/absent), which the plan anticipated: "if prevalence makes kappa unstable, report that rather than lowering standards."

## 1. Decision

**Ontology v0.1 freezes as the ARIS4C-023 calibration ontology, with a mandatory rule-amendment layer v0.1.1 applied before the ontology is expanded beyond the 24 calibration motifs.**

- The motif list and the 24 labels of v0.1 are unchanged. No labels were massaged, and neither coder's file was edited after coding.
- v0.1.1 is a *text* amendment to the inclusion/exclusion rules and to the missingness convention only (six rulings, §4). It creates no new motifs and deletes none.
- A full v0.2 recalibration is **not** triggered now. It is triggered automatically if, after applying v0.1.1, any motif falls below 0.70 per-motif agreement on the expanded (56-motif) packet — i.e. if the amended rules do not in fact fix the boundaries identified here.

## 2. Adjudication of the exposure-contaminated cell

One cell — **P_DIV_BAAL × DIV_KINGSHIP_TRANSFER** — was visible in the coder's own project memory before coding (see `../handoff/DECISIONS.md`).

- Both coders recorded `present`; the cell belongs to the 34 present/present agreements.
- Excluding it: four-state raw agreement 0.824 (98/119), kappa 0.664, AC1 0.786; binary subset unchanged in substance (0.951, kappa 0.892, AC1 0.910).
- **Ruling:** the leak is real and is disclosed, but it **cannot have manufactured the gate result** — the result survives its removal, and removing a *concordant* cell can only lower agreement. The cell is nevertheless excluded from any confirmatory use, and the headline statistic is reported both with and without it.
- **Standing disclosure for the manuscript:** the two coding streams used different model families (GLM and DeepSeek-V4.1-Flash) but the same orchestration harness, and one cell-level Coder A answer plus A's aggregate counts reached Coder B's session through project memory. Methods must state this, report the with/without numbers, and note that a clean external re-code of the affected cell (or the packet) was not performed.

## 3. Conditional item — the missingness boundary

The only recurring boundary is `not_observed` vs `absent` (7 cells, 5.8 % of packets). Both coders used the same four-state vocabulary and neither converted missingness into absence in the other direction, but their *threshold* differs: Coder A treats a bare mention inside a fragmentary witness as no usable evidence; Coder B treats an engaged motif family as scorable. The condition is discharged by ruling 1 in §4, which the plan requires to be explicit; it does not block the freeze because the recurrence stays under the 10 % criterion and does not touch the binary subset that carries the substantive claims.

## 4. v0.1.1 rule amendments (mandatory before expansion)

1. **Missingness threshold.** `not_observed` is reserved for evidence missing from the witness (a marked lacuna swallowing the relevant content) or outside the passage's scope. A passage that engages the motif or its family but lacks the element is `absent`.
2. **Sibling disjunction — earth material.** ANTH_EARTH_DUST requires a generic loose-earth term (earth, soil, dust, ground) *without* explicit plastic/wet quality; ANTH_CLAY_MUD requires explicit plastic or wet earth (clay, mud). Material named as clay no longer also satisfies ANTH_EARTH_DUST.
3. **Sibling disjunction — body material.** ANTH_DIVINE_BLOOD_FLESH requires the *material of human formation* to incorporate divine body substance; ANTH_BODY_SACRIFICE requires human groups or social categories to arise from the *division* of a primordial being. The two never both fire on one passage.
4. **Sibling disjunction — animation.** ANTH_BREATH_ANIMATION requires an animating principle given to a formed body. A divine spirit-component mixed into the material is not by itself animation.
5. **Foretold vs effected.** DIV_SUCCESSION_YOUNGER_OLDER and DIV_KINGSHIP_TRANSFER count only when the displacement/transfer is narrated or acclaimed as occurring (or as an accomplished divine decree), not when merely foretold or feared. Direction is fixed: the *younger* generation displaces the older.
6. **Council and rebellion scope.** DIV_COUNCIL requires a plurality of gods acting as a collective body, not a private counsel among related deities. DIV_PRIMORDIAL_REBELLION requires the rebellious act against established divine authority to be inside the frozen locator and framed as insubordination; retrospective references and monster attacks do not qualify.

## 5. Locator defect — P_ANTH_SUM

`ETCSL 1.7.4 Segment A 10-14` is a single surviving sentence inside a text with ~36 lines missing before and ~32 after it. It carries six of the eight Sumerian anthropogony judgments and produced 6 of the 21 disagreements (75 % of that passage's cells). It is **withdrawn as a confirmatory witness**. Before the Sumerian anthropogony cell enters the tradition × motif matrix it needs either a widened locator or a replacement witness with explicit creation material (a clay-explicit Sumerian anthropogony text).

## 6. What this decision unlocks

- The source-backed **tradition × motif matrix** may now be coded.
- Historical **contact edges**, **genealogy/language structure** and **preregistered environmental variables** may be populated.
- **QCA remains OFF** — its trigger conditions are unchanged and were not met by Pilot-0.
- Similarity still does not prove borrowing: the four mechanism families (vertical inheritance, horizontal diffusion, ecological convergence, cognitive/social convergence) remain unselected by this exercise.
