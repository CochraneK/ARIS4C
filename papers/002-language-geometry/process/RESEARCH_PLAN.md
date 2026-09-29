# RESEARCH_PLAN — ARIS4C-002 · 语言几何「元素周期表」假设的预测压力测试（LING-01 重跑）

> 冻结件 1（段1 门控）· 2026-09-26 21:4x 驱动器接管直写补完（第 10 次接管，未重跑 LLM）。
> 来源纪律：全部设计点从 `RESEARCH_BRIEF.md`（唯一 idea 输入）+ `COORDINATION.md` 关键设定推导并预注册；无编造假设。数据版本已按 `data/raw/MANIFEST.tsv` 实际下载回填。
> 红线：禁读/复用旧仓库 code/data/results；数据仅公开源（钉版）；不合并数据集凑覆盖；不「挽救」圆形假设；不预设圆形错。

## 0. 问题与立场
- 受检主张：人类语言类型学特征空间存在**全局圆形/周期性组织**（「语言元素周期表」）。
- 立场：结论必须是模型比较的产物——若圆形模型在留出预测上不输甚至优于非圆形基准，强版本应被保留并如实报告；反之才拒绝。
- 两条线：**L1 = circularity 直接诊断**；**L2 = family-held-out 预测**。
- 数据层：TLI / GBI / WALS 三个公开源，共 6 张分析表（§4），**分表分析、不合并**，最后协调综合。

## 1. 假设编号表（每条给可计算操作化：指标 + 判据）
主指标（全模型统一）：**留出平均 log-loss（nats/cell，对非缺失留出 cell）**；次指标 = top-1 正确率。
判定检验：family 级配对比较（每族一个配对差）+ 符号检验/置换检验（≥1000 次）。

| # | 假设 | 操作化 | 判据（预注册） |
|---|---|---|---|
| H1 | 全局圆形组织具有超出边际基线的留出预测力 | M2：LOFO 下圆形模型 vs 特征边际·独立基线（§2.4） | 圆形 mean log-loss < 边际基线，且 family 级配对差符号检验 p<.05（双侧） |
| H2 | 圆形组织不劣于非圆形基准（层次/树感知/潜因子） | M3：LOFO 下圆形 vs 各非圆形比较器（§2.2/2.3） | 非劣性：Δ=logloss_circular − logloss_comparator，margin=0.02 nats/cell（≈典型 log-loss 量级的 2–3%，实践可忽略）；Δ 的 family 级 95% CI 下界 > margin 才拒绝该比较器下的 H2 |
| H3 | 预测结论跨 TLI/GBI/WALS 稳健 | M4：M2/M3 分 6 表独立运行，按层聚合 | 层结论=层内各表方向多数（TLI ≥2/3、GBI 2/2、WALS 其单表）；H3 成立 = 三层结论方向一致且无一层被非圆形全面占优；任一层方向分裂（GBI 1:1）或某层非圆形全面占优 → H3 拒绝/降级 |
| H4 | 特征空间布局本身具显著周期性（L1 直接诊断，brief 推导增补） | M1：MDS 布局首谐波周期性统计 vs 随机布局置换 null | 置换 p<.05（单侧，≥1000 次置换）拒绝 null；ns → 圆形假设收到直接诊断侧拒绝信号 |

注：H1–H3 为 L2 线（对应 M2/M3/M4），H4 为 L1 线（M1）。阈值（p<.05、margin=0.02、置换≥1000）此处一次性预注册，段2/3 不得中途调整。

## 2. 比较器模型族（全部纯 Python：numpy/scipy/pandas 可实现，无 GPU）
1. **圆形序贯（circular，待检模型）**：Gower–Rossman circular seriation；目标 = Robinson loss L(π)=Σ d̂(i,j)·|π(i)−π(j)|_circle（d̂ = 二值特征不匹配距离）。n 最大 3573 → O(n³) DP 不可行，**预注册用局部搜索**：2-opt 换位 + 随机重启（seed=42，3 次重启取最优 Robinson loss）。留出预测操作化：留出语言按其特征向量在训练语言圆形顺序上的最近邻投影定位，预测 = 弧距加权近邻多数投票（k=10，权重=1/弧距）。
2. **层次/树感知**：(a) 训练集 Robinson（或 Gower）距离上 UPGMA 建树；(b) 预测 = cophenetic 距离加权 kNN（k=10）；树结构用于距离与加权，不假设「单棵 universal 树」（claims 纪律 §8.1）。
3. **潜因子/低维**：classical MDS（scipy，2 维，metric）+ 潜空间 Euclidean kNN（k=10）。不跑完整 factor analysis（纯 Python 成本/稳定性差）；若段2 需要更强低维比较器，单独预注册后追加。
4. **特征边际·独立基线（marginal，H1 基准）**：每个特征的训练集 base rate；预测取众数类（log-loss 用 p̂=base rate）；不含任何语言间结构信息。
5. **随机空间布局 null（可选/用于显著性）**：M1 的置换 null = 随机圆形排列；M3 增益显著性 = 随机 2-D 布局 null（≥1000 次）。

## 3. 证伪条件（brief Gaps.3 四条逐条落）
1. **留出下圆形增益消失** → M2：圆形 vs 边际基线增益不显著（family 级 p≥.05 或方向为负）→ H1 拒绝。
2. **circularity 诊断不显著** → M1：置换 p≥.05 → H4 拒绝（L1 直接信号，与 L2 独立报告）。
3. **任一数据层非圆形全面占优** → 任一层表 M3 中所有非圆形比较器在所有指标上占优 → 该层 H2 拒绝，H3 相应降级。
4. **增益可被语系/地理先验完全解释** → M5（探索性）：控制语系规模/地理先验后圆形残余增益≈0 → H1/H2 降级为「先验可解释」。注：语系是留出单位，本条实际检验跨族结构（地理/距离先验）；探索性、非确认性。

## 4. 数据版本冻结计划（段1 实际下载后回填；全部钉版见 `data/raw/MANIFEST.tsv`：sha256+URL+commit+获取日期）
| 层 | 公开来源 | 版本钉死 | 落盘文件 |
|---|---|---|---|
| TLI（statistical/logical × small/large） | GitHub `annagraff/crossling-curated` | commit `255632bc62ce05674f1af195b88efea5aef7afce` | statisticalTLI_full_densified_small/large.csv、logicalTLI_full_densified_small.csv + cldf StructureDataset-metadata |
| GBI（statistical/logical） | 同上 | 同上 | statisticalGBI_densified.csv、logicalGBI_densified.csv + cldf StructureDataset-metadata |
| WALS | GitHub `cldf-datasets/wals` | commit `f97440d6edbaed0097d1bd307a5a20ea3f09e271` | values.csv + languages/parameters/codes.csv + cldf metadata |
| 语系标签 + 系统发育 | GitHub `glottolog/glottolog-cldf` | commit `072ca0d0410039fb8b779be8fc165bac575d2cda` | languages.csv + classification.nex（NEXUS 树）+ cldf metadata |

- 获取日期统一 **2026-09-26**（executor 段1 下载，MANIFEST 逐件 sha256 核验）。
- **6 张分析表（分表分析、不合并、不跨表共享 cell）**：TLI_stat_small / TLI_stat_large / TLI_log_small / GBI_stat / GBI_log / WALS。
- **target leakage 检查规则**（段2 执行，此处预注册）：(a) 逐特征预测设定下，目标特征列（及其近义/派生编码列）不得进入预测变量集；(b) 近义编码操作化 = 特征两两相关 |r|>0.9 的对，报告并剔除目标侧列，清单落 `results/leakage_check.tsv`；(c) M1 布局诊断无目标列（全特征为输入），leakage N/A，仅要求版本同钉。
- 语系标签：Glottolog **顶级语系**（glottocode，如 `indo1319`）；无族标签语言（WALS 约 26%）记「isolate/unknown」，永不作为留出单位。

## 5. family-held-out split 方案（预注册）
- **留出单位 = Glottolog 顶级语系**；**最小语系规模规则：≥3 语言**（规模依据 stage1_prompt 默认值；更小语系 cell 数不足以稳定估计留出误差，其信息仍全部留在训练集）。各层可留出语系清单见 `data/DATA_PROFILE.md`。
- **主 split = LOFO（leave-one-family-out）**：每个可留出语系依次整体留出（该系全部语言同时移出训练集），跨语系聚合；确定性、全覆盖、无随机性。
- **次 split（方差估计，仅用于 CI 与参考）**：随机 3-way 语系划分（seeds 1/2/3）；主判定一律以 LOFO 为准。
- **留出 cell** = 留出语系内全部（语言 × 特征）cell；缺失 cell 不计入指标（各层缺失率见 DATA_PROFILE），有效 cell 数逐族记录。
- **isolate/unknown 语系**：恒在训练集（贡献边际基线 base rate），不参与留出。
- 每张表独立 split 与评估；同一语言在不同表中的 cell 不跨表共享。

## 6. M-estimand 清单（可估性预判，段1 画像支持见 DATA_PROFILE）
| # | estimand | 线 | 范围 | 可估性预判 |
|---|---|---|---|---|
| M1 | circularity 直接诊断（MDS 首谐波 vs 置换 null） | L1 | 6 表 | A（6 表二值特征 ≥12 全过；WALS 仅 17 个二值，边缘通过，须标注） |
| M2 | family-held-out 圆形 vs 边际基线 | L2 | 6 表 | A（可留出族数 82/108/65/75/75/109，cell 充足） |
| M3 | family-held-out 圆形 vs 非圆形族（层次/树感知、潜因子） | L2 | 6 表 | A（成本注：n 最大 3573，局部搜索启发式，单表运行时间预注册上限见段2） |
| M4 | 跨层一致性聚合 | L1+L2 | 跨 6 表 | A（方向性聚合，M2/M3 产物即可算） |
| M5 | 语系/地理先验解释检查（探索性） | L2 | 6 表 | B（依赖 Glottolog 地理字段可得性；缺失则降级为仅族规模解释检查，标注探索性） |

## 7. 分段与门控
- 段2（本门控通过后）：M1 直接诊断 + 边际基线 + M2 family-held-out 主实验（LOFO 主判定，冻结数值）。
- 段3：M3 模型族比较 + M4 跨层聚合 + 稳健性（留一数据层、leakage 敏感性、M5 先验解释）。
- 段4：双语稿件（编排器直写，不跑 LLM）；段5：收官（paper.json stage5_final + final_FROZEN.txt + git 同步，排除 .log/.npz/>5MB/草稿）。
- 门控（段1→段2）：本文件 + `lit/REGISTRY.md` + `data/DATA_PROFILE.md` 三件冻结且 `stage1_summary.md` 落盘（残标=0、关键数字双跑一致）。

## 8. Claims 纪律（逐字入终稿）
1. 不从「非圆形更优」推出「存在单一 universal 语言树」。
2. 不「挽救」圆形假设：圆形模型若胜出，强版本如实报告（含全部局限）。
3. M1 诊断显著 ≠ 预测有用：布局有显著周期性但 M2/M3 无预测增益时，结论表述为「周期性结构不提供留出预测力」。
4. 所有留出判定以 LOFO 主 split 为准；次 split 结果仅作方差参考。
5. provenance：数据全部公开源重取（MANIFEST 钉版）、代码全部本 run 新写、不复用旧仓库 code/data/results；旧 run 阴性结论仅作背景事实引用。

## 9. 缺口/停报检查
- 关键设计点（指标定义、split 方案、阈值、比较器估计器）均可从 brief 问题定义 + stage1_prompt 规范推导并已在此预注册：**无停报缺口**。
- 唯一裁量点记录：M3 潜因子代表取 MDS 而非完整 factor analysis（理由：纯 Python 成本/稳定性）；若段2 需更强低维比较器，单独预注册后追加，不影响本文件冻结。
