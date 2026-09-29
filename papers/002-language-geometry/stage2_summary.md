# 段2 摘要 — 002-language-geometry（语言几何：元素周期表假设的预测检验）
## M1 circularity 直接诊断 + leakage 检查 + M2 family-held-out LOFO 主实验（圆形 vs 边际基线）

> 冻结日期：2026-09-27（驱动器接力 14 直写收官；全部关键数字逐字转录自在盘冻结 JSON，未重算）。
> Provenance：段2 executor 03:18:12 死于 128K 溢出（第 8 例，末次动作=common.py chunk 3 edit 成功）→ 驱动器接管第 11 次·接力 5–14 完成 M1 修复（_encode 三 bug）/M1 重跑/M1X 确定性双跑/M2 双 bug 修复（族级码口径 + 混合高级索引）/M2 重启/验收（均未重跑 LLM；M1/M2 数值产自冻结计划任务通道，脚本零改动验收）。

## 门控状态（验收通过，2026-09-27 18:20，results/accept_m2_check.txt）
- 交付物全落盘：`results/leakage_check.tsv`（数据行 202983）/ `scripts/m1_circularity.py` + `results/m1_<table>.json`×6 + `results/m1_results.json` / `scripts/m2_lofo.py` + `results/m2_folds_<table>.tsv`×6 + `results/m2_<table>.json`×6 + `results/m2_results.json` / 本文件。
- 残标扫描 = 0（6 张 m2_folds tsv + m2_results.json + leakage_check.tsv；脚本=`.sandbox-tmp/accept_m2_verify.py`）。
- 数据红线：`sha256 ALL_OK=True`（M2 run.log 首行；7 件 CSV 按 `data/raw/MANIFEST.tsv` 钉版核验；M1 通道同款 ALL_OK）。
- 交叉验证三链：
  1. **M1 确定性双跑**：M1X 全量重跑（10:46:30，748s）vs 首跑（735s）7 件 JSON 除 elapsed* 逐字节 IDENTICAL → `xcheck_m1x_compare.txt` SUMMARY diffs=0 PASS（原件备份 `xcheck_m1_rerun_backup/`）。
  2. **M2 逐 fold 交叉核对**：`race_1510_backup/`（15:10 首跑被误杀前产物）vs 现产：TLI_stat_small 82 folds 全量 + TLI_stat_large 前 24 folds 逐 fold 逐列一致（除 elapsed_sec）。
  3. **汇总独立重算**：自 fold tsv 重算 mean_logloss×2 / top1×2 / sign_p（双侧精确符号检验复刻）/ perm_p（default_rng(42) 1000× 符号翻转精确复刻）/ n_cells_valid / n_families_valid，6 表全部逐字对汇总。

## M1：circularity 直接诊断（H4，L1）— classical MDS 2D + 首谐波 R；null=1000× 特征列内置换（保边际），seed=42，单侧 p
| 表 | n_langs | n_binary | impute_rate | R_obs | p_one_sided | verdict |
|---|---|---|---|---|---|---|
| TLI_stat_small | 644 | 261 | 0.05102247809665485 | 0.053851946851075846 | 0.004 | reject_null（支持圆形组织） |
| TLI_stat_large | 1696 | 266 | 0.18896379473479155 | 0.05174877999774007 | 0.734 | ns（直接诊断侧拒绝信号） |
| TLI_log_small | 555 | 274 | 0.039620125540703155 | 0.060353030969664885 | 0.03 | reject_null（支持圆形组织） |
| GBI_stat | 1140 | 178 | 0.00026030836529427167 | 0.04862160710577147 | 0.001 | reject_null（支持圆形组织） |
| GBI_log | 1223 | 190 | 4.416174976881993e-05 | 0.0832751225701077 | 0.0 | reject_null（支持圆形组织） |
| WALS | 2501 | 18 | 0.9982576569372251 | 0.9514340507219855 | 0.234 | ns [高填补率·解释需谨慎] |

- 6 表 n_null_done=1000、capped=false。WALS 为边缘/ns 信号：R_obs=0.951 系 99.83% 对填补的退化距离伪迹，按预注册口径仅标注、不改判定（段1 DATA_PROFILE §5 裁定已照抄）。

## M2：family-held-out LOFO 主实验（H1，L2）— 圆形（每 fold Robinson 2-opt 圆序几何 + 弧距加权 kNN）vs 边际基线（训练集类 base rate）
| 表 | folds done/valid/skip | mean logloss circular | marginal | top1 circular/marginal | sign_p（双侧） | perm_p | impute_rate | H1 verdict |
|---|---|---|---|---|---|---|---|---|
| TLI_stat_small | 82/82/0 | 0.4665523412608537 | 0.5401859302363116 | 0.6852578290411468 / 0.7437321241916925 | 5.2573169769006436e-09 | 0.0 | 0.05102247809665485 | H1 支持（circular_better） |
| TLI_stat_large | 108/108/0 | 0.48572673315998505 | 0.5314238716262168 | 0.67955957434057 / 0.7508488480159868 | 1.8829338019072798e-08 | 0.0 | 0.18896379473479155 | H1 支持（circular_better） |
| TLI_log_small | 65/65/0 | 0.4747657966533464 | 0.5240766780036488 | 0.687742736383933 / 0.7540444506874338 | 1.1688116132369708e-06 | 0.0 | 0.039620125540703155 | H1 支持（circular_better） |
| GBI_stat | 75/75/0 | 0.669097174599512 | 0.5410274927960423 | 0.6617110143505149 / 0.72181231412488 | 5.293955920339377e-23 | 0.0 | 0.00026030836529427167 | H1 拒绝（marginal_better） |
| GBI_log | 75/75/0 | 0.6807653926821746 | 0.5330256672618042 | 0.660196485904223 / 0.7265465699509146 | 4.0234064994579266e-21 | 0.0 | 4.416174976881993e-05 | H1 拒绝（marginal_better） |
| WALS | 104/88/5 | 1.0738384604729019 | 1.1842131436781866 | 0.40358527661398635 / 0.5172027398223081 | 0.0037465093469812305 | null | 0.9982576569372251 | H1 支持 [高填补率·解释需谨慎] |

- H1 支持 ×3（TLI 三表，圆形 mean log-loss < 边际）；H1 拒绝 ×2（GBI 两表，边际占优）；WALS H1 支持但 impute_rate=0.9983 → 解释受限。
- WALS 口径：109 顶级语系 → 5 族 n_held<3 触发守卫 SKIPPED（basq1248 / band1339 / sena1264 / sout2772 / yoku1255，与段1 r10_verify 预告一致）→ 104 执行 → 88 有效（16 fold logloss 非有限，剔出均值与符号检验 n=88）。perm_test_p=null = 脚本守卫（Δ 含非有限值 → 跳过置换；预注册将置换检验定位为稳健性报告，非判定项，非缺陷）。
- leakage 对数汇总（|r|>0.9，pairwise complete，全清单见 `leakage_check.tsv` 202983 数据行）：TLI_stat_small=48854 / TLI_stat_large=51634 / TLI_log_small=53203 / GBI_stat=16091 / GBI_log=17770 / WALS=15431。预测目标 f 时 f 列 + 近义列禁入留出语言投影向量集（预注册 §4 已执行）。

## 运行时长统计 + 逐 fold 完成度
- M1 单表 elapsed_sec：37.0 / 192.9 / 25.3 / 81.8 / 94.5 / 315.2（首跑 total 735s；M1X 重跑 748s）。
- M2 单表 elapsed_sec：55.0 / 594.2 / 34.7 / 143.4 / 169.0 / 1914.5（total 2915s，< 单表 3h 上限）。
- 逐 fold 完成度：6/6 表 100%（82/82、108/108、65/65、75/75、75/75、104/104，WALS 另有 5 族守卫跳过）；capped=False 全表；逐 fold 检查点 `m2_folds_<table>.tsv` 完整（83/109/66/76/76/105 行含表头）。

## 缺口报告（如实记录，4 条）
1. `m2_<table>.json`×6 脚本从未写（`m2_lofo.py` 仅写 folds tsv + 汇总——脚本-规格 gap，D3 要求按表 JSON）→ 接力 14 自 `m2_results.json` 确定性转写补齐（转录非重算，roundtrip 验证通过）。
2. 本文件（D4 `stage2_summary.md`）executor 未写（03:18 死后 M2 由驱动器接管执行）→ 接力 14 直写收官（收官与产物同周期纪律）。
3. `launch_*.bat` 通道 err.log 尾 `EXIT_CODE=` 空值 quirk（M1/M2 同款；不影响 run.log/JSON 产物与任务自清理）。
4. M2 err.log 3 条 numpy divide-by-zero warning（`np.where(a0.any(), …, 1.0/ad)`，良性）。

## Claims 纪律（入稿前核对，brief 红线）
- 不从「非圆形更优」推出「存在单一 universal 树」（GBI marginal_better ≠ 树的证据）；不「挽救」圆形假设。
- 三数据层分源分析、不合并；WALS（M1 R_obs=0.951 高填补伪迹 + M2 impute=0.998）在综合中仅列探索性参照。
- 结论必须是模型比较的产物：H2（圆形不劣于非圆形基准）与 H3（跨层稳健）待段3 判定；本段 M1/M2 为 H1（留出预测力）与 H4（直接诊断）证据。

## 段3 建议（M3 模型族比较）
- 比较器（RESEARCH_PLAN 预注册）：UPGMA + cophenetic kNN / MDS-2D + Euclidean kNN；圆形比较器复用段2 每 fold 几何，边际基线复用段2 产物（不重算）。
- 沿用段2 模式：每 fold 几何一次不依赖目标特征 / leakage 清单剔近义列 / 逐 fold tsv 检查点幂等续跑；M3 单表上限 ≤3h（含全部比较器，预注册）；超限停表保 fold。
- H2：逐表 圆形 vs 非圆形（层次/树感知/潜因子/边际）；H3：留一数据层稳健 + 语系/地理先验解释核查（证伪条件：留出下圆形增益消失 / 诊断不显著 / 非圆形全面占优 / 增益可被先验完全解释）。
- 注意 M1/M2 分歧模式：TLI_stat_large M1 p=0.734（ns，直接诊断侧拒绝信号）但 M2 H1 支持（p=1.88e-08）；GBI 两表 M1 全 sig 但 M2 边际占优 → M3 须以比较器正面对决裁定，勿以 M1 信号替代。
