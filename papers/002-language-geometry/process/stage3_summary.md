# 002-language-geometry · 段3 摘要（stage3_summary）

- 日期：2026-09-28 ｜ 规格：stage3_prompt.txt（冻结）
- 代码：scripts/m3_comparators.py（M3）、scripts/m4_robust.py（M4+稳健性）——本 run 新写
- 时间线：M3 主跑 09:40–11:17（total_elapsed=5833s）→ M4+稳健性 11:17–11:19 → xcheck r1 11:19–11:30（会话终止）→ xcheck r2 ~11:45–12:36（diffs=0）

## 1. 门控状态

| 门 | 状态 |
|---|---|
| sha256 钉版（8 件 CSV vs MANIFEST） | PASS · ALL_OK=True（§2；xcheck r2 于 11:45 复核并重写 m3_sha256.txt） |
| M3 六表完成度 | 82/82 · 108/108 · 65/65 · 75/75 · 75/75 · 104/104；capped 全 False；WALS 5 skip：basq1248/band1339/sena1264/sout2772/yoku1255 |
| 残标检查 | 0（grep TODO/FIXME/XXX/TBD/placeholder/to-be-filled/to-be-supplied 于 m3_comparators.py、m4_robust.py、m3_results.json、m3_<table>.json×6、m4_aggregation.json、robustness×3、xcheck_m3_compare.txt → 无匹配） |
| xcheck 双跑 | PASS · SUMMARY diffs=0（逐字串全等；folds 表除 elapsed_sec） |
| 稳健性三项 | 完成（leaveout_layer / leakage_sens / m5_priors，11:19 落盘） |
| 交付物落盘 | results/：m3_<table>.json×6、m3_results.json、m4_aggregation.json、robustness×3、m3_{folds,macro,meta}×6(+xcheck)、m3_null×2(+xcheck)、m3_run.log、xcheck_run.log、m3_sha256.txt、xcheck_m3_compare.txt、leak_sens_GBI_stat_{folds.tsv,raw.json} |

## 2. sha256 核验（8 件，exp=act 全一致，ALL_OK=True）

| 文件 | sha256 |
|---|---|
| statisticalTLI_full_densified_small | 2b34b9c23b910604ef4c11fb6f2cde27314159050d287ac30201eb3930492f6f |
| statisticalTLI_full_densified_large | efd1f1c099ead1775c63f0ed7c94fc257e8c87bd43283057e288ba99536c34eb |
| logicalTLI_full_densified_small | a6da5ed4b4580172159c0fb98c5ddf861a90304d0bd412eb1270318c34b84426 |
| statisticalGBI_densified | 17fef9d026e5357a4e8290a85d40095ff35f111ac04b23a16e3524c76264fc6e |
| logicalGBI_densified | e06024c1251729e4d4c68ef556d0dc8ddff864d66427f5db9abc77d7de2def78 |
| wals/values | 2d672f80dbe8cf1839061af0301650bde60c326bbb486835c93ab7304b5b06cd |
| wals/languages | 10e0742f158dadd4ef9484797ef7606a337306ee49a110a58c8e658826d3290e |
| glottolog/languages | 1a50a393bc81568b656f9522be18aa4f80f38e94309ba6c863d583234adfbb89 |

（完整记录：results/m3_sha256.txt；01:30 晨间预检 sha256_check_stage3.txt 同 8 件 ALL_OK=True）

## 3. 各表 M3 关键数字（逐字取自 results/m3_results.json；Δ=ll_circular−ll_comparator，95% CI 族级）

### 3.1 TLI_stat_small（82/82，n_cells 31729，impute_rate 0.05102247809665485）

| 模型 | mean log-loss | top1 acc |
|---|---|---|
| circular | 0.4665523412608537 | 0.6852578290411468 |
| marginal | 0.5401859302363116 | 0.7437321241916925 |
| UPGMA | 0.2944136211646837 | 0.6710163547004158 |
| MDS-2D | 0.40511292118480985 | 0.6757788471825374 |

- H2 (UPGMA)：拒绝 — Δ=0.1721387200961701，95% CI [0.05672952583770871, 0.36745613157407814]，下界 0.0567 > margin 0.02
- H2 (MDS)：未拒绝 — Δ=0.061439420076044006，95% CI [-0.1281043339039451, 0.22765075610962462]，下界未超 margin
- m5a（地理先验残差增益，探索性）：Δ=0.018272345376294116，CI [-0.18901376567390407, 0.27390558765886663]，worse=False
- 随机 2D null：已执行（82 族 × 1000 layouts，§7）
- elapsed 3328.3s；matches_m2=True

### 3.2 TLI_stat_large（108/108，n_cells 59343，impute_rate 0.18896379473479155）

| 模型 | mean log-loss | top1 acc |
|---|---|---|
| circular | 0.48572673315998505 | 0.67955957434057 |
| marginal | 0.5314238716262168 | 0.7508488480159868 |
| UPGMA | 0.22988410893813066 | 0.7133241941873818 |
| MDS-2D | 0.29599738914651547 | 0.7018431062468855 |

- H2 (UPGMA)：拒绝 — Δ=0.25584262422185433，95% CI [0.10079888488359529, 0.4585080232419573]，下界 0.1008 > margin
- H2 (MDS)：拒绝 — Δ=0.18972934401346964，95% CI [0.034734639052493556, 0.45865241296249026]，下界 0.0347 > margin
- m5a：Δ=0.03294187616186463，CI [-0.1158893867699287, 0.27114487296999223]，worse=False
- 随机 2D null：未执行（预算：估计 54324s > 剩余 10702s）
- elapsed 98.1s；matches_m2=True

### 3.3 TLI_log_small（65/65，n_cells 28624，impute_rate 0.039620125540703155）

| 模型 | mean log-loss | top1 acc |
|---|---|---|
| circular | 0.4747657966533464 | 0.687742736383933 |
| marginal | 0.5240766780036488 | 0.7540444506874338 |
| UPGMA | 0.29512375055927675 | 0.6928072147945736 |
| MDS-2D | 0.37486124594818054 | 0.6982402778306452 |

- H2 (UPGMA)：拒绝 — Δ=0.17964204609406967，95% CI [0.0464988785014972, 0.3610425420964417]，下界 0.0465 > margin
- H2 (MDS)：未拒绝 — Δ=0.09990455070516588，95% CI [-0.05196836558137247, 0.2606542385508518]，下界未超 margin
- m5a：Δ=0.02720493072318598，CI [-0.15470326605781654, 0.22812625149569002]，worse=False
- 随机 2D null：已执行（65 族 × 1000 layouts，§7）
- elapsed 2079.5s；matches_m2=True

### 3.4 GBI_stat（75/75，n_cells 86337，impute_rate 0.00026030836529427167）

| 模型 | mean log-loss | top1 acc |
|---|---|---|
| circular | 0.669097174599512 | 0.6617110143505149 |
| marginal | 0.5410274927960423 | 0.72181231412488 |
| UPGMA | 0.4416677115383105 | 0.6670648815470709 |
| MDS-2D | 0.49963725014782756 | 0.672082562044582 |

- H2 (UPGMA)：拒绝 — Δ=0.2274294630612014，95% CI [0.11437239602694357, 0.35188947995575537]，下界 0.1144 > margin
- H2 (MDS)：拒绝 — Δ=0.16945992445168429，95% CI [0.056601518708417724, 0.2809345990146889]，下界 0.0566 > margin
- m5a：Δ=0.15748002865395194，CI [0.021623599986282327, 0.3051912158412761]，worse=TRUE（圆形显著劣于 Macroarea 地理先验 → 圆形几何不可完全由地理先验还原）
- 随机 2D null：未执行（预算：估计 17625s > 剩余 10770s）
- elapsed 29.3s；matches_m2=True

### 3.5 GBI_log（75/75，n_cells 104066，impute_rate 4.416174976881993e-05）

| 模型 | mean log-loss | top1 acc |
|---|---|---|
| circular | 0.6807653926821746 | 0.660196485904223 |
| marginal | 0.5330256672618042 | 0.7265465699509146 |
| UPGMA | 0.4716098846688852 | 0.6665857352153227 |
| MDS-2D | 0.4997426880447014 | 0.6657727205091001 |

- H2 (UPGMA)：拒绝 — Δ=0.20915550801328936，95% CI [0.11184268797037789, 0.29688171588489665]，下界 0.1118 > margin
- H2 (MDS)：拒绝 — Δ=0.1810227046374732，95% CI [0.05932316493210508, 0.2764157475540817]，下界 0.0593 > margin
- m5a：Δ=0.18060472541544145，CI [0.055753246940047706, 0.30615435396064267]，worse=TRUE（同 3.4）
- 随机 2D null：未执行（预算：估计 20625s > 剩余 10766s）
- elapsed 33.8s；matches_m2=True

### 3.6 WALS（109 族，104 done，5 skip，n_cells 4287，impute_rate 0.9982576569372251 —— 高填补率·解释需谨慎）

| 模型（有效 fold n） | mean log-loss | top1 acc |
|---|---|---|
| circular（n=88） | 1.0738384604729019 | 0.40358527661398635 |
| marginal（n=90） | 1.1842131436781866 | 0.5172027398223081 |
| UPGMA（n=84） | 0.5343248133811108 | 0.43115234462035423 |
| MDS-2D（n=81） | 0.9594304886848183 | 0.4007984627685158 |

- wals_note：16 fold logloss 非有限（同段2 剔出均值与检验）
- H2 (UPGMA)：未拒绝 — Δ=0.5154113614035749，95% CI [-0.26760759137578527, 1.8394173098241693]，下界未超 margin
- H2 (MDS)：未拒绝 — Δ=0.06695530145899414，95% CI [-0.7308947384132571, 0.8948399907730591]，下界未超 margin
- m5a（n=88）：Δ=0.051384867101879665，CI [-0.7693391331323989, 1.0440470491608473]，worse=False
- 随机 2D null：未执行（预算：估计 23412s > 剩余 10720s）
- elapsed 79.6s；matches_m2=True

### 3.7 段2 基线速查（M1/M2 冻结件，逐字取自 m1_results.json / m2_results.json，供 §11 分歧裁定引用）

| 表 | M1 R_obs | M1 p（单侧） | M2 sign_test_p | M2 H1 方向 | n_leak_pairs |
|---|---|---|---|---|---|
| TLI_stat_small | 0.053851946851075846 | 0.004 | 5.2573169769006436e-09 | circular_better | 48854 |
| TLI_stat_large | 0.05174877999774007 | 0.734 | 1.8829338019072798e-08 | circular_better | 51634 |
| TLI_log_small | 0.060353030969664885 | 0.03 | 1.1688116132369708e-06 | circular_better | 53203 |
| GBI_stat | 0.04862160710577147 | 0.001 | 5.293955920339377e-23 | marginal_better | 16091 |
| GBI_log | 0.0832751225701077 | 0.0 | 4.0234064994579266e-21 | marginal_better | 17770 |
| WALS | 0.9514340507219855 | 0.234 | 0.0037465093469812305 | circular_better | 15431 |

## 4. H2 判定汇总（族级 95% CI 下界 vs margin 0.02 nats/cell）

| 表 | UPGMA | MDS |
|---|---|---|
| TLI_stat_small | 拒绝（下界 0.0567） | 未拒绝（下界 -0.1281） |
| TLI_stat_large | 拒绝（0.1008） | 拒绝（0.0347） |
| TLI_log_small | 拒绝（0.0465） | 未拒绝（-0.0520） |
| GBI_stat | 拒绝（0.1144） | 拒绝（0.0566） |
| GBI_log | 拒绝（0.1118） | 拒绝（0.0593） |
| WALS | 未拒绝（-0.2676） | 未拒绝（-0.7309） |

## 5. M4 跨层聚合 / H3（results/m4_aggregation.json）

方向规则：方向=族级 Δ 均值符号；层结论=层内各表方向多数（TLI≥2/3、GBI 2/2、WALS 单表）；H3 成立=三层方向一致且无层被非圆形全面占优；H1/H2 线分别聚合。

| 线 | TLI 层 | GBI 层 | WALS 层 | 三层一致 | 非圆形全面占优层 |
|---|---|---|---|---|---|
| H1 (circular vs marginal) | circular_better 3:0 | marginal_better 2:0（dominance） | circular_better 1:0 | FALSE | GBI |
| H2 (UPGMA) | upgma_better 3:0（dominance） | upgma_better 2:0（dominance） | upgma_better 1:0（dominance） | TRUE | TLI, GBI, WALS |
| H2 (MDS) | mds_better 3:0（dominance） | mds_better 2:0（dominance） | mds_better 1:0（dominance） | TRUE | TLI, GBI, WALS |

逐表 Δ（族级均值，逐字；表序 = TLI_small / TLI_large / TLI_log / GBI_stat / GBI_log / WALS）：
- H1：-0.0736335889754578 / -0.04569713846623181 / -0.04931088135030235（circular 优）；0.12806968180346945 / 0.14773972542037034（marginal 优）；-0.07074787439302108（circular 优，88 fold 配对）
- H2_upgma：0.1721387200961701 / 0.25584262422185433 / 0.17964204609406967 / 0.2274294630612014 / 0.20915550801328936 / 0.5154113614035749
- H2_mds：0.061439420076044006 / 0.18972934401346964 / 0.09990455070516588 / 0.16945992445168429 / 0.1810227046374732 / 0.06695530145899414

逐表 fold_pos_share（方向正例占比，同表序）：
- H1：0.18292682926829268 / 0.23148148148148148 / 0.2 / 1.0 / 0.9866666666666667 / 0.3409090909090909
- H2_upgma：1.0 / 1.0 / 0.9846153846153847 / 1.0 / 1.0 / 0.9047619047619048
- H2_mds：0.8292682926829268 / 0.9814814814814815 / 0.9538461538461539 / 1.0 / 0.9866666666666667 / 0.49382716049382713

逐表 95% CI（fold 级配对，同表序）：
- H1：[-0.19797175001981962, 0.10900312175757615] / [-0.17393620922261102, 0.16912213827882652] / [-0.14756825396923245, 0.142755968203197] / [0.02469189043170756, 0.23670931847947088] / [0.049533638220936364, 0.25608157058382613] / [-0.8284979396423761, 0.8620089667643234]（GBI_stat 项与 §6.2 baseline 行全等）
- H2_upgma / H2_mds：与 §3.1–3.6 各表 H2 Δ 置信区间逐字相同（m4 与 m3 逐格一致，inputs.n_cell_mismatches=0）

**H3 verdict（逐字）：「H3 拒绝/降级（逐层依据见 basis；探索性聚合、非新增假设）」**

basis 8 条（逐字）：
1. H1_marginal: 三层方向不一致 TLI=circular_better, GBI=marginal_better, WALS=circular_better
2. H1_marginal × GBI: 层内 2 表全部被非圆形占优（marginal_better）
3. H2_upgma × TLI: 层内 3 表全部被非圆形占优（upgma_better）
4. H2_upgma × GBI: 层内 2 表全部被非圆形占优（upgma_better）
5. H2_upgma × WALS: 层内 1 表全部被非圆形占优（upgma_better）
6. H2_mds × TLI: 层内 3 表全部被非圆形占优（mds_better）
7. H2_mds × GBI: 层内 2 表全部被非圆形占优（mds_better）
8. H2_mds × WALS: 层内 1 表全部被非圆形占优（mds_better）

## 6. 稳健性三项（results/robustness_*.json，11:19 落盘）

### 6.1 leaveout_layer（逐层留一）

| 留一 | H1 剩余层方向 | H1 一致 | H2_upgma 一致 | H2_mds 一致 |
|---|---|---|---|---|
| TLI | GBI=marginal, WALS=circular | FALSE | TRUE | TRUE |
| GBI | TLI=circular, WALS=circular | TRUE | TRUE | TRUE |
| WALS | TLI=circular, GBI=marginal | FALSE | TRUE | TRUE |

→ H1 三层不一致的唯一离群源 = GBI 层。

### 6.2 leakage_sens（GBI_stat，n_folds 75，近义剔除 |r| 0.90→0.95）

| 量 | baseline (r=0.90) | sens (r=0.95) | direction_changed |
|---|---|---|---|
| circular logloss | 0.669097174599512 | 0.6729985610327625 | false |
| H1 Δ (marginal) | 0.12806968180346945 [0.02469189043170756, 0.23670931847947088] | 0.1314653409087065 [0.03087915112910502, 0.2619704225035886] | false |
| H2_upgma Δ | 0.2274294630612014 [0.11437239602694357, 0.35188947995575537] | 0.2323866557290659 [0.11270281130087689, 0.3697877844430633] | false |
| H2_mds Δ | 0.16945992445168429 [0.056601518708417724, 0.2809345990146889] | 0.17226299642613216 [0.06224433713313516, 0.30278184386816687] | false |

note：探索性、非判定项；同 fold 集合；几何同段2（逐 fold rng42）；仅近义剔除阈值放宽。

### 6.3 m5_priors

- m5a（自 m3 转写）：GBI_stat worse=TRUE、GBI_log worse=TRUE，其余 4 表（TLI×3、WALS）worse=False。
- m5b Spearman(n_held_langs, Δ_f)，18 格（6 表 × 3 线），p<.05 者 3 格（探索性、非判定）：
  - TLI_stat_small H2_upgma：ρ=0.2579806028520392, p=0.01928327390355501
  - TLI_stat_small H2_mds：ρ=0.23232345397324344, p=0.03570148362199148
  - TLI_stat_large H2_mds：ρ=-0.19239770366708087, p=0.046057237472302295
- m5b 其余 15 格 ns（逐字，表序同 §3，n 为有效 fold 数）：
  - TLI_stat_small H1_marginal：ρ=0.05315178249715381, p=0.6353171502646331 (n=82)
  - TLI_stat_large H1_marginal：ρ=-0.046000738229894055, p=0.6363977123338062 (n=108)
  - TLI_stat_large H2_upgma：ρ=-0.12225905719864999, p=0.20748775960758017 (n=108)
  - TLI_log_small H1_marginal：ρ=-0.21800578970055204, p=0.08106047675716505 (n=65)
  - TLI_log_small H2_upgma：ρ=-0.15451638427898778, p=0.21908082416809394 (n=65)
  - TLI_log_small H2_mds：ρ=0.07338716961105239, p=0.5612604672157272 (n=65)
  - GBI_stat H1_marginal：ρ=0.18649650072988103, p=0.10914015294784059 (n=75)
  - GBI_stat H2_upgma：ρ=0.01857945782676516, p=0.8742882238685035 (n=75)
  - GBI_stat H2_mds：ρ=0.05904743651651966, p=0.6148121618568227 (n=75)
  - GBI_log H1_marginal：ρ=-0.056853233670295995, p=0.6280410570149099 (n=75)
  - GBI_log H2_upgma：ρ=0.08258755631652318, p=0.48117062788241066 (n=75)
  - GBI_log H2_mds：ρ=-0.1253348869225266, p=0.28397485639020886 (n=75)
  - WALS H1_marginal：ρ=-0.09763872270735678, p=0.3654648394240576 (n=88)
  - WALS H2_upgma：ρ=-0.05504187532594522, p=0.6189877314670071 (n=84)
  - WALS H2_mds：ρ=-0.07497108710477421, p=0.5059293002023771 (n=81)

## 7. 随机 2D null 状态（门控 el<2.4h；未触发者按规格标注「未执行（预算）」）

| 表 | 状态 |
|---|---|
| TLI_stat_small | 已执行：82 族 × 1000 layouts；per-family p 均值 0.5398 / 中位 0.5300，min 0.046，max 0.980；p<0.05 族 1 个、p>0.95 族 9 个 |
| TLI_log_small | 已执行：65 族 × 1000 layouts；均值 0.3096 / 中位 0.2550，min 0.005，max 0.960；p<0.05 族 7 个、p>0.95 族 1 个 |
| TLI_stat_large | 未执行（预算：估计 54324s > 剩余 10702s） |
| GBI_stat | 未执行（预算：估计 17625s > 剩余 10770s） |
| GBI_log | 未执行（预算：估计 20625s > 剩余 10766s） |
| WALS | 未执行（预算：估计 23412s > 剩余 10720s） |

xcheck 复核：TLI_stat_small null 前 3 族（indo1319 0.173 / ural1272 0.134 / utoa1244 0.182）主跑与 xcheck 逐字一致。

## 8. Leakage 对数复核（段2 冻结口径 |r|>0.9，n_leak_pairs）

TLI_stat_small 48854 ｜ TLI_stat_large 51634 ｜ TLI_log_small 53203 ｜ GBI_stat 16091 ｜ GBI_log 17770 ｜ WALS 15431

（逐字取自 results/m2_results.json；源表 leakage_check.tsv 9,093,086B，段2 冻结 mtime 09-27 15:14，段3 未改动；leakage_sens 以 0.95 阈值复核 GBI_stat，方向不变，§6.2）

## 9. 运行时长与逐 fold 完成度

- M3 主跑 total_elapsed=5833s（09:40–11:17）；逐表 elapsed：3328.3 / 98.1 / 2079.5 / 29.3 / 33.8 / 79.6 s（表序同 §3）
- 逐 fold：六表 capped 全 False（无单表 3h 截断）；folds tsv 行数（含表头）83/109/66/76/76/105，与 n_fams done 一致；WALS 5 族 skip（basq1248/band1339/sena1264/sout2772/yoku1255）
- xcheck：r1 11:19–11:30 死于会话终止（fold/macro/meta 11:20 落盘、null 完成 3/82）→ r2 ~11:45 自检查点续跑 → 12:36 完成，SUMMARY diffs=0
- M4+稳健性：11:17–11:19（m4_aggregation.json 与 robustness×3 落盘 11:19）

## 10. 缺口报告

1. **m4 H1_marginal 符号 quirk**：m4_aggregation.json 的 sign_convention 声明「Δ=ll_marginal−ll_circular，族级均值>0→circular_better」，但存储的 delta_mean 实为 (ll_circular−ll_marginal) 的 fold 配对均值（符号相反）：TLI_stat_small 存储 -0.0736335889754578 = 0.4665523412608537−0.5401859302363116；GBI_stat 存储 0.12806968180346945 = 0.669097174599512−0.5410274927960423。direction 字段已用原始逐比较器均值逐表核对：全部正确（TLI 三表 circular 均值 < marginal 均值；GBI 两表 circular 均值 > marginal 均值；WALS circular 1.0738384604729019 < marginal 1.1842131436781866）。WALS 存储 Δ 为 88 fold 配对均值，与两比较器各自均值之差不同，因有效 fold 集不同（circular n=88 vs marginal n=90），属正常。对 H3 verdict 无影响；稿件引用须用原始均值 + direction 字段，不得直接引用 H1 行 delta_mean 数值符号。
2. **m3_results.json WALS 表缺 h2_direction 键**（json.dump 时机 quirk）；per-table m3_WALS.json 的 h2_rejected：upgma=False / mds=False，与 §3.6 Δ/CI 一致。
3. **随机 2D null 4 表未执行**：预算门控触发（§7），按规格标注「未执行（预算）」，非失败。
4. **WALS 高填补率 0.9982576569372251**：按规格双标注（高填补率·解释需谨慎 + 16 fold 非有限剔除 + 5 族 skip）。

## 11. 段4 建议（稿件叙述要点）

1. **M1/M2/M3 分歧裁定**：M1 直接诊断 6 表中 4 表 reject_null（TLI_stat_small p=0.004、TLI_log_small p=0.03、GBI_stat p=0.001、GBI_log p=0.0；TLI_stat_large p=0.734 ns、WALS p=0.234 ns）；M2 留出 H1：TLI 三表 + WALS circular_better、GBI 两表 marginal_better（sign_p 见 §3.7）；M3 H2：UPGMA 主五表全拒绝、MDS 三表拒绝；M4 H3 拒绝/降级。裁定（依 RESEARCH_PLAN §3 证伪条件 1/3）：周期性组织在留出预测侧不成立——「非圆形比较器在全部三层占优」；按 §8.3，M1 的显著周期性表述为「周期性结构不提供留出预测力」，不作机制性结论。
2. **TLI_large 诊断 ns 但 H1/H2 方向**：M1 p=0.734（直接诊断侧拒绝信号）vs M2 H1 支持（sign_p 1.8829338019072798e-08）+ M3 H2 双比较器拒绝 → 诊断与预测背离，按 §8.3 单列讨论，不互相抵消。
3. **WALS 双标注**：高填补率 0.9982576569372251 + 16 fold 非有限剔除（+5 族 skip）→ 仅作辅助层，不作核心证据；其 H1 方向（circular_better）在 leaveout 中随 GBI 变化（§6.1），不改变 H3 结论。
4. **Claims 纪律（RESEARCH_PLAN §8，5 条逐字入稿）**：
   1. 不从「非圆形更优」推出「存在单一 universal 语言树」。
   2. 不「挽救」圆形假设：圆形模型若胜出，强版本如实报告（含全部局限）。
   3. M1 诊断显著 ≠ 预测有用：布局有显著周期性但 M2/M3 无预测增益时，结论表述为「周期性结构不提供留出预测力」。
   4. 所有留出判定以 LOFO 主 split 为准；次 split 结果仅作方差参考。
   5. provenance：数据全部公开源重取（MANIFEST 钉版）、代码全部本 run 新写、不复用旧仓库 code/data/results；旧 run 阴性结论仅作背景事实引用。
5. **稿件结构建议**：M1（诊断）→ M2（H1 留出）→ M3（H2 非劣性，逐表×比较器）→ M4（H3 跨层）→ 稳健性（leaveout/leakage_sens/m5）→ 局限（null 预算缺口、WALS、§10 两条 quirk）→ claims 纪律。
