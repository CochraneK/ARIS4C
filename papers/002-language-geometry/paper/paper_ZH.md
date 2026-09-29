# 语言的元素周期表？——类型学特征空间中全局圆形组织的预测性压力测试

**作者：** Cochrane Kang
**运行：** local-ARIS-rerun · 段 4 —— 按冻结 `RESEARCH_PLAN.md` §7 由编排器直写（不经 LLM 起草）；全部数字逐字转录自冻结落盘 JSON，未做任何重算
**日期：** 2026-09-30 · **姊妹篇：** `paper_EN.md`（英文母版）、`paper_EN_notes.md`（数字→来源映射与运行 provenance）

## 摘要

语言类型学中反复出现一种直觉：世界上的语言或许可以像"元素周期表"那样组织——一种低维的、全局结构化的排列，其中类型学特征以规律性的顺序重复出现。本文对这一主张做**预测性**（而非描述性）的压力测试。我们从三个独立策展的公开特征层——TLI（统计与逻辑）与 GBI，外加辅助层 WALS——组装出 6 张"语言 × 特征"表（555–2,501 种语言；每表 18–335 个特征），并检验：特征空间的**圆形组织**（一个全局圆环，相邻语系共享特征剖面）能否产生非圆形几何所不具备的**留出预测力**。设计采用留一族系法（LOFO）：在 509 个实际执行的 fold 中，每次留出整个顶级语系（≥3 种语言），并要求仅用其余语系拟合的几何体去预测被留出语系的特征值。在预注册 margin = 0.02 nats/cell 下，四个比较器家族同台竞争：带弧距加权 kNN 的圆形序贯；带共表距加权 kNN 的 UPGMA；带欧氏 kNN 的 2-D MDS；以及边际（基率）基线。基于置换的周期性诊断（1,000 次保边际特征列置换）先行筛查每张表。结果：(i) 直接诊断在 6 表中 4 表发现显著一阶谐波周期性（单侧 p ≤ 0.03；R ≈ 0.049–0.083），TLI_stat_large（p = 0.734）与 WALS（p = 0.234；99.83% 填补）不显著；(ii) 相对边际基线，圆形模型在全部 3 张 TLI 表胜出（留出 log-loss 0.4666–0.4857 vs 0.5241–0.5402 nats/cell；双侧符号检验 p ≤ 1.17×10⁻⁶），但在两张 GBI 表落败（0.6691 / 0.6808 vs 0.5410 / 0.5330；p ≤ 4.02×10⁻²¹）；(iii) 相对非圆形几何比较器，圆形模型被决定性超越——UPGMA 在全部 5 张主表胜出（族级 95% CI 下界高出 margin 0.0465–0.2558 nats/cell），MDS 在 3 张主表胜出；(iv) 三层聚合判定 H3 被**拒绝**：三层方向不一致（GBI 层是唯一离群源，留一层检验确认），且每一层都被非圆形比较器全面占优。裁定：周期性组织在留出预测侧不成立——按预注册措辞纪律表述为"**周期性结构不提供留出预测力**"。稳健性：泄漏守卫收紧（|r| 0.90→0.95）不翻转任何判定；GBI 层上圆形模型甚至显著差于纯 Macroarea 地理先验（worse = TRUE），即"改用地理"也救不活圆形主张；已执行的随机 2-D 布局 null（2 表）显示 MDS 的优势对随机低维布局不特殊（per-family p ≈ 0.31–0.54），即圆形模型的失败是"输给任意合理低维布局"而非"仅输给 MDS"。

## 1. 引言

### 1.1 受检主张

主张：人类语言类型学特征空间存在**全局圆形 / 周期性组织**（"语言的元素周期表"）——语言可以排成一个圆环，使得类型学特征剖面以规律的、可重复的顺序复现，如同元素性质在化学周期表中的复现。两条预注册证据线用于裁决：**L1** 特征空间布局圆形性的直接诊断；**L2** 族系留出预测——几何体必须比无结构与非圆形替代方案更好地*预测*整个被留出语系的特征。

*主张来源（如实登记，不回避）：* 周期表主张**没有域内索引来源**。OpenAlex 7 轮检索中 'periodic' 命中 4 条，全为跨域（计算力学、化学教育、生物信息学、病毒学）；域内最近邻位于全局结构/对称性方向（Kemp 2026；Evans & Levinson 2009；Piantadosi & Gibson 2014；Levinson & Meira 2003）。受检主张因此经由 `RESEARCH_BRIEF`（受检主张登记表）进入本研究，不为其编造文献来源（冻结 `lit/REGISTRY.md` §0）。

### 1.2 为何是预测性压力测试

描述性拟合是容易的：任意维度的 MDS 布局、任意距离下的序贯，看起来都"有结构"。有鉴别力的问题是：圆形排列能否*预测*。若特征空间全局圆形，则 (a) 布局相对置换 null 显示显著周期性（H4，线 L1）；(b) 在不含被留出语系的情况下拟合的圆形几何，在预测该语系特征时胜过无结构的边际基线（H1）；(c) 圆形几何不被非圆形（层次/潜因子）几何占优（H2）；(d) 结论在独立策展的特征层之间方向一致（H3）。预注册了四条证伪条件：留出后圆形增益消失；直接诊断不显著；任一层被非圆形比较器全面占优；或增益可被语系/地理先验完全解释。

### 1.3 数据：三个独立特征层

- **TLI**（统计与逻辑，densified）：Graff 等（2025）自 5 个已发表库策展，最小化特征间的逻辑与强统计依赖。
- **GBI**：同一策展体系；特征体系源自 Grambank（Skirgård 等 2023）。
- **WALS**（Dryer & Haspelmath 2013）：仅作辅助层——分析矩阵 18 个二值特征，99.83% 填补率；所有 WALS 结果强制携带告诫标注。
- **语系标签、系统发育、地理：** Glottolog 5.2.1（Hammarström 等 2025）。

6 张表**分开分析、绝不合并**（冻结裁定）。所有数据于 2026-09-26 自公开源重新获取，按 commit + sha256 钉版（`data/raw/MANIFEST.tsv`）；所有代码为本次运行新写。不重用任何旧运行的代码/数据/结果（claims 纪律第 5 条，§10）。

### 1.4 预注册设计（H1–H4）

主指标（所有模型）：**留出 mean log-loss（nats/cell，对非缺失留出 cell 计）**；次指标：top-1 准确率。判定检验：族级配对差 + 符号检验/置换检验（≥1,000 次）。阈值（p < .05，margin = 0.02 nats/cell，≥1,000 置换）一次注册、从不调整。

| # | 假设 | 操作化 | 预注册判据 |
|---|---|---|---|
| H1 | 全局圆形组织在边际基线之外具有留出预测力 | M2：LOFO 下圆形模型 vs 特征边际独立基线 | 圆形 mean log-loss < 边际，且族级配对差符号检验 p < .05（双侧） |
| H2 | 圆形组织不劣于非圆形基准（层次/树感知/潜因子） | M3：LOFO 下圆形 vs 每个非圆形比较器 | 非劣性：Δ = logloss_circular − logloss_comparator，margin = 0.02 nats/cell；仅当 Δ 的族级 95% CI 下界超过 margin 才对该比较器拒绝 H2 |
| H3 | 预测结论在 TLI / GBI / WALS 间稳健 | M4：M2/M3 逐表独立执行，按层聚合 | 层结论 = 层内方向多数（TLI ≥2/3，GBI 2/2，WALS 单表）；仅当三层方向一致且无层被非圆形比较器全面占优时 H3 成立 |
| H4 | 特征空间布局本身显示显著周期性（L1 直接诊断） | M1：MDS 布局的一阶谐波周期性 vs 置换 null | 置换 p < .05（单侧，≥1,000 置换）拒绝 null；ns = 对圆形性的直接诊断拒绝信号 |

比较器模型家族（全部纯 Python，无 GPU）：

1. **圆形（受检模型）：** Gower–Rossman 圆形序贯；二元不匹配距离 d̂ 上的 Robinson loss L(π) = Σ d̂(i,j)·|π(i)−π(j)|_circle。精确 O(n³) 解不可行（n 至 3,573）→ 预注册局部搜索：2-opt 交换 + 3 次随机重启（seed = 42，保留最佳 Robinson loss）。留出操作化：被留出语言的特征向量投影到训练圆形序的最近邻上；预测 = k = 10 弧距加权多数投票（权重 = 1/弧距）。
2. **层次 / 树感知：** 训练集 Robinson（或 Gower）距离上的 UPGMA 树；预测 = 共表距加权 kNN（k = 10）。树是距离/加权装置，不是"单一 universal 树"主张（claims 第 1 条，§10）。
3. **潜因子 / 低维：** 经典 2-D metric MDS + 潜空间欧氏 kNN（k = 10）。（完整因子分析预注册为可选升级，最终不需要。）
4. **边际基线（H1 参照）：** 逐特征训练集基率；众数类预测（log-loss 用 p̂ = 基率）；不含任何语言间结构。
5. **随机布局 null：** M1 的 null = 保边际特征列置换（1,000×，见 §3）；M3 增益显著性 = 随机 2-D 布局（每 fold 1,000×，见 §7.4）。冻结计划文本对 M1 写的是"随机圆形排列"；实际执行（冻结、双跑验证）用的是列置换 null——这是该统计量的标准 null，偏差在 `paper_EN_notes.md` 披露。

### 1.5 Claims 政策（预注册；冻结 `RESEARCH_PLAN.md` §8 的忠实转录）

1. 不从"非圆形更优"推断存在*单一 universal 语言树*。
2. 不"挽救"圆形假设：若圆形模型赢了，强版本将如实报告，连同所有限制。
3. M1 诊断显著 ≠ 预测有用：当布局显示显著周期性但 M2/M3 无预测增益时，结论措辞为"周期性结构不提供留出预测力"。
4. 所有留出判定以 LOFO 主 split 为准；次 split 结果仅作方差参考。
5. Provenance：全部数据自公开源重取（MANIFEST 钉版），全部代码本 run 新写，不重用旧 run 代码/数据/结果；旧 run 阴性结论仅作背景事实引用。

## 2. 数据与文献登记

### 2.1 特征层与版本钉死

| 表 | 来源（钉死） | n_langs（分析） | 真特征 | 原始缺失率 | 二值特征（M1） | 分析填补率 |
|---|---|---|---|---|---|---|
| TLI_stat_small | `annagraff/crossling-curated` @ `255632bc…` | 644 | 321 | 0.691 | 261 | 0.0510 |
| TLI_stat_large | 同上 | 1,696 | 328 | 0.780 | 266 | 0.1890 |
| TLI_log_small | 同上 | 555 | 335 | 0.664 | 274 | 0.0396 |
| GBI_stat | 同上 | 1,140 | 181 | 0.294 | 178 | 0.00026 |
| GBI_log | 同上 | 1,223 | 190 | 0.262 | 190 | 0.00004 |
| WALS | `cldf-datasets/wals` @ `f97440d6…` | 2,501（/2,660 唯一） | 192 | 0.850 | 18 | 0.9983 |

语系标签 / 系统发育 / 地理：`glottolog/glottolog-cldf` @ `072ca0d0…`（Glottolog 5.2.1）。所有层获取日期：2026-09-26。全部 8 个分析 CSV 在每个分析阶段对照 `data/raw/MANIFEST.tsv` sha256 核验（段 3：8/8 `ALL_OK=True`；完整哈希表见 `paper_EN_notes.md`）。

### 2.2 留一族系法（LOFO）设计

- 留出单位：**Glottolog 顶级语系**；最小规模守卫 **≥3 语言**（更小的语系留在训练集——其 cell 对基率仍有信息量，但永不被留出）。
- 每表可留出语系数：**82 / 108 / 65 / 75 / 75 / 109**；留出语言数：399 / 1,421 / 289 / 845 / 928 / 2,352；非缺失留出 cell（设计容量）：44,145 / 106,277 / 37,288 / 114,332 / 137,039 / 65,109（最小表 TLI_log_small = 37,288——足以稳定估计 log-loss）。
- 无语系标签的语言（WALS 约 26%：isolate/unknown）**永不**被留出。
- 逐表 split；同一语言的 cell 绝不在表间共享。
- WALS 细节：109 个可留出语系 → 5 个被 ≥3 语言守卫跳过（`basq1248`、`band1339`、`sena1264`、`sout2772`、`yoku1255`）→ 104 执行 → **88 有效**（16 个 fold 因 log-loss 非有限被剔除出均值与符号检验）。
- 实际计入分数的有效非缺失留出 cell（fold 有效性 + 泄漏守卫后，M3 所用口径）：31,729 / 59,343 / 28,624 / 86,337 / 104,066 / 4,287。

### 2.3 目标泄漏守卫

预测特征 *f* 时，*f* 的列及其近义列**排除**出留出投影集。近义操作化：特征两两相关 |r| > 0.9（pairwise complete）；完整对清单落盘（`results/leakage_check.tsv`，202,983 数据行）。每表对数：TLI_stat_small 48,854 · TLI_stat_large 51,634 · TLI_log_small 53,203 · GBI_stat 16,091 · GBI_log 17,770 · WALS 15,431。M1 布局诊断无目标列（所有特征均为输入）——泄漏 N/A；仅版本钉死。

### 2.4 文献登记表与 provenance

冻结登记表（`lit/REGISTRY.md`）含 **29 条**——A8 圆形序贯方法、B8 全局结构/对称、C5 层次/潜因子比较器、D3 WALS 特征预测任务、E5 数据层文档——其中 **26/29 经 Crossref 核验 OK**；3 条无 DOI（A8 补核未命中后按二手引文登记；E3/E4 取自本地数据层元数据）。**引用纪律：** 只可引用登记表条目（与钉死本地元数据）；未经核验的文献不得入稿。

登记的阴性发现（逐字带入 provenance）："语言的元素周期表"假设在 OpenAlex **无域内索引来源**（7 轮检索；4 条 'periodic' 命中全跨域）。主张入口 = `RESEARCH_BRIEF`；域内最近邻 = Kemp（2026）、Evans & Levinson（2009）、Piantadosi & Gibson（2014）、Levinson & Meira（2003）。

执行 provenance（完整细节见 `paper_EN_notes.md`）：本地 ARIS 重跑。段 1 与段 2 的 executor 进程死于 128K 上下文上限（16:50:38 / 03:18:12），由**编排器直写**补完（从冻结落盘 JSON 确定性转录，双跑验证，无 LLM 重算）；段 3 executor 正常完成（独立重跑 xcheck：diffs = 0）；段 4（本稿件）按冻结计划 §7 由编排器直写。

## 3. M1 —— 直接周期性诊断（H4）

**方法。** 每表：语言在二元特征矩阵上的经典 2-D MDS 布局（与 M2/M3 同一距离口径：pairwise complete + min_shared = 10 + 行均值填补）；提取布局质心周围的一阶谐波幅值 R；null 分布 = **1,000 次保边际特征列置换**（列边际保留，语言层结构破坏），seed = 42，单侧 p。全部 6 表：n_null_done = 1,000，无一被截断。确定性双跑（M1X 全量重跑，748 s）与首跑**逐字节一致**（diffs = 0）。

| 表 | n_langs | n_binary | 填补率 | R_obs | p（单侧） | 判定 |
|---|---|---|---|---|---|---|
| TLI_stat_small | 644 | 261 | 0.0510 | 0.053851946851075846 | 0.004 | reject_null |
| TLI_stat_large | 1,696 | 266 | 0.1890 | 0.05174877999774007 | 0.734 | ns |
| TLI_log_small | 555 | 274 | 0.0396 | 0.060353030969664885 | 0.03 | reject_null |
| GBI_stat | 1,140 | 178 | 0.00026 | 0.04862160710577147 | 0.001 | reject_null |
| GBI_log | 1,223 | 190 | 0.00004 | 0.0832751225701077 | 0.0 | reject_null |
| WALS | 2,501 | 18 | 0.9983 | 0.9514340507219855 | 0.234 | ns [高填补 · 告诫] |

**解读。** 6 表中 4 表拒绝 null，但效应很小：R ≈ 0.049–0.083（R² ≈ 0.002–0.007）——一阶谐波是布局中真实而薄片状的一部分。最大表（TLI_stat_large）**ns**（p = 0.734）：在样本最大处出现对圆形性的直接诊断拒绝信号。WALS 的 R_obs = 0.951 是 99.83% 填补率下的退化距离伪迹（段 1 裁定：WALS 边缘通过必须标注）；其 p = 0.234 在预注册读法下为 ns。按 claims 第 3 条（§1.5），诊断显著不确立预测有用性——那是 §4–5 的职责。

## 4. M2 —— H1：圆形 vs 边际基线（留出）

**方法。** 每 fold：圆形几何（训练语系的 Robinson 2-opt 序贯 + 弧距加权 kNN，k = 10）拟合一次，独立于目标特征；对被留出语系的 cell 计分。基线：逐特征训练基率（众数类；log-loss 用 p̂ = 基率）。判定：族级配对 log-loss 差，双侧符号检验（置换符号翻转，≥1,000，作为稳健性报告）。

| 表 | folds done/valid/skip | 圆形 log-loss | 边际 log-loss | top-1 圆形/边际 | sign_p（双侧） | perm_p | H1 判定 |
|---|---|---|---|---|---|---|---|
| TLI_stat_small | 82/82/0 | 0.4665523412608537 | 0.5401859302363116 | 0.6853 / 0.7437 | 5.2573169769006436e-09 | 0.0 | **circular_better** |
| TLI_stat_large | 108/108/0 | 0.48572673315998505 | 0.5314238716262168 | 0.6796 / 0.7508 | 1.8829338019072798e-08 | 0.0 | **circular_better** |
| TLI_log_small | 65/65/0 | 0.4747657966533464 | 0.5240766780036488 | 0.6877 / 0.7540 | 1.1688116132369708e-06 | 0.0 | **circular_better** |
| GBI_stat | 75/75/0 | 0.669097174599512 | 0.5410274927960423 | 0.6617 / 0.7218 | 5.293955920339377e-23 | 0.0 | **marginal_better** |
| GBI_log | 75/75/0 | 0.6807653926821746 | 0.5330256672618042 | 0.6602 / 0.7265 | 4.0234064994579266e-21 | 0.0 | **marginal_better** |
| WALS | 104/88/5 | 1.0738384604729019 | 1.1842131436781866 | 0.4036 / 0.5172 | 0.0037465093469812305 | null | **circular_better** [高填补 · 告诫] |

（top-1 保留 4 位小数；全精度见 `paper_EN_notes.md` 与冻结 JSON。）

**解读。**
- **H1 支持 ×3（全部 TLI 表）：** 圆形模型比无结构基线好 0.0457–0.0736 nats/cell——TLI 层上基率之外真实且高度显著的预测信号。
- **H1 拒绝 ×2（GBI 表）：** 边际基线比圆形模型好 0.1281 / 0.1477 nats/cell——GBI 层上圆形几何 actively 有害。
- **WALS（辅助）：** 名义上圆形有利（1.0738 vs 1.1842；sign_p = 0.0037，n = 88），但 perm_p = null——置换守卫跳过（Δ 含非有限值；置换检验预注册定位为稳健性报告而非判定项）——且 99.83% 填补封顶了可解释性。
- **诚实的次级观察（top-1）：** 边际基线在*全部 6 表*的 top-1 准确率上胜出（如 TLI_stat_small 0.7437 vs 0.6853）。预注册主指标是 log-loss（校准化的期望意外度）：弧距加权 kNN 投票是平滑插值器，在 TLI 上改善了校准概率，而朴素的众数基率赢在硬指派。无任何预注册判定（全部基于 log-loss + 符号检验）受影响。

## 5. M3 —— H2：圆形 vs 非圆形几何（留出）

**方法。** 每表 × 每 fold：在 §4 的配对上加两个新比较器——(i) 训练集 Robinson 距离上的 **UPGMA**，共表距加权 kNN（k = 10）；(ii) **经典 2-D MDS + 欧氏 kNN**（k = 10）。几何每 fold 只算一次，独立于目标（同一距离口径；确定性——主体无随机性）。Δ = ll_circular − ll_comparator（正 = 圆形更差）；判定：仅当 Δ 的族级 95% CI 下界超过 margin 0.02 nats/cell 时对该比较器拒绝 H2。

### 5.1 留出 mean log-loss（nats/cell）与 top-1 准确率

| 表（n_cells） | 圆形 | 边际 | UPGMA | MDS-2D | top-1：圆形/边际/UPGMA/MDS |
|---|---|---|---|---|---|
| TLI_stat_small (31,729) | 0.4665523412608537 | 0.5401859302363116 | 0.2944136211646837 | 0.40511292118480985 | 0.6853 / 0.7437 / 0.6710 / 0.6758 |
| TLI_stat_large (59,343) | 0.48572673315998505 | 0.5314238716262168 | 0.22988410893813066 | 0.29599738914651547 | 0.6796 / 0.7508 / 0.7133 / 0.7018 |
| TLI_log_small (28,624) | 0.4747657966533464 | 0.5240766780036488 | 0.29512375055927675 | 0.37486124594818054 | 0.6877 / 0.7540 / 0.6928 / 0.6982 |
| GBI_stat (86,337) | 0.669097174599512 | 0.5410274927960423 | 0.4416677115383105 | 0.49963725014782756 | 0.6617 / 0.7218 / 0.6671 / 0.6721 |
| GBI_log (104,066) | 0.6807653926821746 | 0.5330256672618042 | 0.4716098846688852 | 0.4997426880447014 | 0.6602 / 0.7265 / 0.6666 / 0.6658 |
| WALS (4,287；n = 88/90/84/81) | 1.0738384604729019 | 1.1842131436781866 | 0.5343248133811108 | 0.9594304886848183 | 0.4036 / 0.5172 / 0.4312 / 0.4008 |

### 5.2 H2 判定（Δ 的族级 95% CI 下界 vs margin 0.02）

| 表 | UPGMA：Δ（CI 下界） | 判定 | MDS：Δ（CI 下界） | 判定 |
|---|---|---|---|---|
| TLI_stat_small | 0.1721387200961701（0.05672952583770871） | **拒绝** | 0.061439420076044006（−0.1281043339039451） | 未拒绝 |
| TLI_stat_large | 0.25584262422185433（0.10079888488359529） | **拒绝** | 0.18972934401346964（0.034734639052493556） | **拒绝** |
| TLI_log_small | 0.17964204609406967（0.0464988785014972） | **拒绝** | 0.09990455070516588（−0.05196836558137247） | 未拒绝 |
| GBI_stat | 0.2274294630612014（0.11437239602694357） | **拒绝** | 0.16945992445168429（0.056601518708417724） | **拒绝** |
| GBI_log | 0.20915550801328936（0.11184268797037789） | **拒绝** | 0.1810227046374732（0.05932316493210508） | **拒绝** |
| WALS | 0.5154113614035749（−0.26760759137578527） | 未拒绝 | 0.06695530145899414（−0.7308947384132571） | 未拒绝 |

**解读。**
- **UPGMA（层次/树感知）在全部 5 张主表胜出**，且 95% CI 下界每表都超过 0.02 margin（0.0465–0.1144；TLI_stat_large 最强 0.1008，GBI_stat 0.1144）。
- **2-D MDS 在 5 张主表中 3 张胜出**（TLI_stat_large、GBI_stat、GBI_log）；两张较小的 TLI 表未拒绝（下界为负）。
- **WALS：** 两个比较器均未拒绝（CI 宽；高填补）——辅助层，无核心证据。
- **解读（预注册证伪条件 3 触发）：** 圆形模型在 TLI 上相对朴素基线的 §4 优势被系统发育/层次几何**完全吸收**——圆形排列捕获的是族系层结构，UPGMA 共表距捕获同一结构但更便宜、更精确。非圆形比较器在每一个主层都占优。
- **符号 quirk 披露：** 冻结 `m4_aggregation.json` 的 H1 行存储的 `delta_mean` 符号与其自身 `sign_convention` 字段相反（记录在冻结段 3 缺口报告第 1 条）。因此本文所有 H1 数字引用**原始逐比较器均值 + direction 字段**（已对照逐表 JSON 核验），从不引用存储的 H1 `delta_mean` 符号。

## 6. M4 —— H3：三层聚合（探索性）

**聚合规则（预注册，RESEARCH_PLAN §1）。** 每表方向 = 族级配对 Δ 均值的符号。层结论 = 层内多数（TLI：≥2/3 表；GBI：2/2；WALS：单表）。H3 成立当且仅当三层方向一致**且**无层被非圆形比较器全面占优。H3 是 H1/H2 的探索性聚合，不是新假设。

### 6.1 三线聚合

| 线 | TLI（3 表） | GBI（2 表） | WALS（1 表） | 三层一致 | 非圆形占优层 |
|---|---|---|---|---|---|
| H1（vs 边际） | circular 3:0 | **marginal 2:0（占优）** | circular 1:0 | **FALSE** | GBI |
| H2 vs UPGMA | upgma 3:0（占优） | upgma 2:0（占优） | upgma 1:0（占优） | TRUE | 全部三层 |
| H2 vs MDS | mds 3:0（占优） | mds 2:0（占优） | mds 1:0（占优） | TRUE | 全部三层 |

### 6.2 逐表族级 Δ（表序：TLI_small / TLI_large / TLI_log / GBI_stat / GBI_log / WALS）

| 线 | 逐表 Δ | 逐表 fold_pos_share |
|---|---|---|
| H1（存储符号，见 §5 quirk） | −0.0736335889754578 / −0.04569713846623181 / −0.04931088135030235 / 0.12806968180346945 / 0.14773972542037034 / −0.07074787439302108（n = 88 配对 fold） | 0.1829 / 0.2315 / 0.2000 / 1.0000 / 0.9867 / 0.3409 |
| H2 vs UPGMA | 0.1721387200961701 / 0.25584262422185433 / 0.17964204609406967 / 0.2274294630612014 / 0.20915550801328936 / 0.5154113614035749 | 1.0000 / 1.0000 / 0.9846 / 1.0000 / 1.0000 / 0.9048 |
| H2 vs MDS | 0.061439420076044006 / 0.18972934401346964 / 0.09990455070516588 / 0.16945992445168429 / 0.1810227046374732 / 0.06695530145899414 | 0.8293 / 0.9815 / 0.9538 / 1.0000 / 0.9867 / 0.4938 |

**判定（冻结 JSON，逐字）：** 「H3 拒绝/降级（逐层依据见 basis；探索性聚合、非新增假设）」——**H3 被拒绝/降级**。

**依据（8 条，逐字摘自 `m4_aggregation.json`）：**
1. H1_marginal：三层方向不一致 TLI=circular_better, GBI=marginal_better, WALS=circular_better
2. H1_marginal × GBI：层内 2 表全部被非圆形占优（marginal_better）
3. H2_upgma × TLI：层内 3 表全部被非圆形占优（upgma_better）
4. H2_upgma × GBI：层内 2 表全部被非圆形占优（upgma_better）
5. H2_upgma × WALS：层内 1 表全部被非圆形占优（upgma_better）
6. H2_mds × TLI：层内 3 表全部被非圆形占优（mds_better）
7. H2_mds × GBI：层内 2 表全部被非圆形占优（mds_better）
8. H2_mds × WALS：层内 1 表全部被非圆形占优（mds_better）

## 7. 稳健性

### 7.1 留一层检验（H3 稳健性）

| 留出的层 | H1：剩余层方向，一致性 | H2 vs UPGMA | H2 vs MDS |
|---|---|---|---|
| 留 TLI | GBI = marginal，WALS = circular → **FALSE** | TRUE | TRUE |
| 留 GBI | TLI = circular，WALS = circular → **TRUE** | TRUE | TRUE |
| 留 WALS | TLI = circular，GBI = marginal → **FALSE** | TRUE | TRUE |

**解读：** H1 三层不一致的**唯一离群源是 GBI 层**——留出 GBI 后 H1 变为三层一致（circular）。全部 9 个 H2 格保持 TRUE：非圆形占优对"留哪一层"稳健。

### 7.2 泄漏敏感性（GBI_stat，75 folds；|r| 0.90 → 0.95 重跑）

| 量 | |r| = 0.90 | |r| = 0.95 | 方向翻转 |
|---|---|---|---|
| 圆形 logloss | 0.669097174599512 | 0.6729985610327625 | 否 |
| H1 Δ（95% CI） | 0.12806968180346945 [0.02469189043170756, 0.23670931847947088] | 0.1314653409087065 [0.03087915112910502, 0.2619704225035886] | 否 |
| H2 vs UPGMA Δ | 0.2274294630612014 | 0.2323866557290659 | 否 |
| H2 vs MDS Δ | 0.16945992445168429 | 0.17226299642613216 | 否 |

更严的泄漏守卫下无任何判定翻转。

### 7.3 Macroarea 地理先验（M5a）+ 小留出样本量探针（M5b）

**M5a**（圆形 vs 留出语言所在 Glottolog macroarea 内训练语言的逐特征基率；无 Macroarea 或该 macroarea 内无 f 非缺失的 cell 对该比较器无效）：**圆形模型在两张 GBI 表上显著差于纯地理先验**——GBI_stat Δ = 0.15748002865395194，95% CI [0.021623599986282327, 0.3051912158412761]（worse = TRUE）；GBI_log Δ = 0.18060472541544145，95% CI [0.055753246940047706, 0.30615435396064267]（worse = TRUE）。其余 4 表 worse = FALSE（CI 均含 0）。**解读：** 圆形模型在 GBI 层的失败不可还原为地理——它甚至*严格差于*地理先验，所以"干脆用地理"救不活圆形主张。

**M5b**（n_held_langs 与 Δ_f 的 Spearman ρ，逐特征；18 格 = 6 表 × 3 线；探索性）：3 格 p < .05——TLI_stat_small × H2_upgma ρ = 0.2579806028520392（p = 0.01928327390355501）；TLI_stat_small × H2_mds ρ = 0.23232345397324344（p = 0.03570148362199148）；TLI_stat_large × H2_mds ρ = −0.19239770366708087（p = 0.046057237472302295）。其余 15 格不显著。不影响任何预注册判定；仅作探索性观察报告。

### 7.4 随机 2-D 布局 null（H4 配套，MDS 专项）

**定义（冻结，`m3_comparators.py` 头注释）：** 每 fold，rng = `default_rng(42)`；1000 个随机 2-D 布局，在 MDS 坐标包围盒内均匀采样、同一坐标尺度、仅替换 MDS 比较器布局；p_f = P(Δ_null ≥ Δ_obs)，fold 级（非有限 Δ 不计入分母）。

| 表 | 状态 | 细节 |
|---|---|---|
| TLI_stat_small | **已执行**（82 族 × 1000） | 逐族 p 均值 0.5398、中位 0.5300，min 0.046、max 0.980；1 族 p < .05，9 族 p > .95 |
| TLI_log_small | **已执行**（65 族 × 1000） | 逐族 p 均值 0.3096、中位 0.2550，min 0.005、max 0.960；7 族 p < .05，1 族 p > .95 |
| TLI_stat_large | 未执行（预算） | 估计 54,324 s > 剩余 10,702 s |
| GBI_stat | 未执行（预算） | 估计 17,625 s > 剩余 10,770 s |
| GBI_log | 未执行（预算） | 估计 20,625 s > 剩余 10,766 s |
| WALS | 未执行（预算） | 估计 23,412 s > 剩余 10,720 s |

交叉核验：TLI_stat_small null 前 3 族（indo1319 0.173 / ural1272 0.134 / utoa1244 0.182）与独立重跑逐字一致（diffs = 0）。

**解读：** 已执行格显示逐族 p ≈ 0.31–0.54——即 MDS 比较器相对圆形的优势**对 MDS 结构并不特殊**：同一坐标尺度上的随机 2-D 布局能达到类似的 Δ。MDS 的胜出是*一般低维欧氏几何*的性质，而非经典标度解特有的性质。这强化了 H2 判定：圆形模型在它失败的层面上输给*任意*合理低维布局。

## 8. 讨论

**裁定。** "语言的元素周期表"主张——类型学特征存在单一全局圆形组织且其几何**预测性**地有用——**没有通过留出压力测试**。三层聚合（H3）被拒绝：非圆形比较器在每一层都占优，且 H1 三层不一致的离群源是 GBI 层（留一层检验在两个方向上都确认它是唯一不一致来源）。按预注册 claims 政策，精确表述是：**周期性结构不提供留出预测力**——更简单的几何（UPGMA 共表距，或同一尺度上的任意 2-D 欧氏布局）就能达到同等或更好；且在 GBI 层上圆形结构严格差于无结构的边际基线。

**M1 显著 ≠ 预测有用。** 6 表中 4 表在训练数据层面显示显著圆形性信号（M1，特征列置换 null），但 M2/M3 在 M1 显著处无留出增益（GBI），在 M2 有增益处（TLI）非圆形几何更便宜地捕获了该增益（H2 被拒绝）。样本内全局形状统计量显著，不等于该形状是可用的预测器。这是本研究的核心方法论教训。

**TLI_stat_large 诊断–预测背离（独立报告，不互相抵消）。** M1 置换 null 在 TLI_stat_large 上不显著（R = 0.05174877999774007，p = 0.734），而留出符号检验在圆形有利方向上高度显著（p = 1.8829338019072798e-08），H2 对两个非圆形比较器均被拒绝。这两个结果逻辑独立——一个是训练集形状检验，一个是留出预测检验——并排报告、不作抵消：大表的特征矩阵在样本内无可检出的*全局*圆形签名，但圆形排列仍比边际基线更好地预测留出特征、比树感知几何更差。

**WALS 仍是辅助层。** 99.83% 填补（率 0.9982576569372251）、16/104 fold 因非有限 Δ 被剔除出 WALS H2 比较（n = 88）、5 个语系被跳过（basq1248、band1339、sena1264、sout2772、yoku1255）、冻结 m3 记录缺 `h2_direction` 键（逐表 `h2_rejected` upgma = False / mds = False 与"两个比较器均未拒绝"一致）——WALS 在两个方向上都不提供核心证据。本文所有 WALS 陈述均携带这一双重告诫。

**非圆形占优的解读。** 圆形排列捕获的是族系层结构（故在 TLI 上胜过边际基线）；UPGMA 共表距从*同一*距离矩阵捕获同样的族系层结构，其确定性、层次感知的加权是弧距 kNN 投票比不上的。随机布局 null（§7.4）显示该优势是一般低维欧氏几何的性质。与 claims 第 1 条一致的最干净读法：**证据支持"族系/系统发育结构对类型学有预测力"——既不支持"单一 universal 树"，也不支持"圆形组织特别地"**。我们不挽救圆形假设，也不主张 universal 树。

## 9. 局限

1. **随机 2-D null 不完整（预算所限，非失败）：** 仅在 TLI_stat_small 与 TLI_log_small 执行；TLI_stat_large、GBI_stat、GBI_log、WALS 因每表时间估计超出阶段剩余预算（54,324 / 17,625 / 20,625 / 23,412 s vs 剩余 10,702 / 10,770 / 10,766 / 10,720 s）未执行。两个已执行格支持"一般低维几何"解读；推广到全部表之前需以更大预算重跑。
2. **WALS 双重告诫：** 填补率 0.9982576569372251；104 fold 中 16 个因非有限 Δ 被剔除出 H2 比较；5 个语系跳过（basq1248、band1339、sena1264、sout2772、yoku1255）；`m3_WALS.json` 缺 `h2_direction` 键（冻结段 3 报告缺口第 2 条）。WALS 为 2,660 唯一语言中的 2,501 分析样本。仅作辅助层。
3. **m4 H1 符号 quirk（缺口第 1 条）：** 存储的 H1 `delta_mean` 符号与 `sign_convention` 字段相反；direction 字段已对照 6 表的原始逐比较器均值逐一复核。本文所有 H1 数字引用原始均值 + direction，从不引用存储符号。
4. **top-1 次指标：** 边际基线在全部 6 表 top-1 准确率上胜出（如 TLI_stat_small 0.7437 vs 0.6853）。主指标是预注册 log-loss；top-1 模式是诚实的次级观察，不影响任何预注册判定。
5. **圆形序贯是局部搜索：** Robinson-loss 序贯用 2-opt + 3 次随机重启（seed = 42）求解，非精确解；n ≈ 600–2,600 下 O(n³) 精确法不可行。局部最优可能低估圆形几何的最好可达性能，即圆形模型可能因求解器质量被压低。这是圆形家族性能*下界*的局限，不是对使用已解布局的判定的局限。
6. **M1 null 计划–实现偏差（已披露，§1.4）：** 计划文本写"随机圆形排列"null；实际执行的是 1,000 次保边际特征列置换（冻结、双跑逐字节一致）。结果按实际执行报告。
7. **LOFO 是唯一判定 split。** 预注册的次 3-way splits（seeds 1/2/3）仅作方差参考；全部判定使用 LOFO。

## 10. Claims 纪律（预注册；与 §1.5 相同）

1. 不从"非圆形更优"推断存在*单一 universal 语言树*。
2. 不"挽救"圆形假设：若圆形模型赢了，强版本将如实报告，连同所有限制。
3. M1 诊断显著 ≠ 预测有用：当布局显示显著周期性但 M2/M3 无预测增益时，结论措辞为"周期性结构不提供留出预测力"。
4. 所有留出判定以 LOFO 主 split 为准；次 split 结果仅作方差参考。
5. Provenance：全部数据自公开源重取（MANIFEST 钉版），全部代码本 run 新写，不重用旧 run 代码/数据/结果；旧 run 阴性结论仅作背景事实引用。

**本次运行 adherence 核对：** 第 1 条——§8 明确拒绝 universal-tree 推断；第 2 条——圆形模型输了，未做任何挽救；第 3 条——头条裁定使用注册的精确措辞；第 4 条——所有判定引用 LOFO 结果；第 5 条——§2.4 provenance 记录。

## 参考文献（冻结登记表：29 条；26/29 经 Crossref 核验；引用纪律见 `lit/REGISTRY.md`）

**A. 圆形序贯方法（8）**

1. Armstrong, C., Guzmán, E., & Sing Long, D. (2021). An optimal algorithm for strict circular seriation. *SIAM J. Math. Data Sci., 3*(4), 1223–1250. https://doi.org/10.1137/21M139356X
2. Carmona, Y., Chepoi, B., Naves, B., & Préat, J. (2023). A simple and optimal algorithm for strict circular seriation. *SIAM J. Math. Data Sci., 5*(1), 201–221. https://doi.org/10.1137/22m1495342
3. Laporte, G. (1978). The seriation problem and the travelling salesman problem. *J. Comput. Appl. Math., 4*(4), 259–268. https://doi.org/10.1016/0771-050x(78)90024-4
4. Concas, S., Fenu, C., Rodriguez, J. P. M., & Vandebril, R. (2023). The seriation problem in the presence of a double Fiedler value. *Numer. Algorithms, 92*(1), 407–435. https://doi.org/10.1007/s11075-022-01461-1
5. Hubert, L. (1974). Some applications of graph theory and related non-metric techniques to problems of approximation. *Br. J. Math. Stat. Psychol.* https://doi.org/10.1111/j.2044-8317.1974.tb00534.x [题名在冻结记录内截断]
6. Hubert, L., & Schultz, K. (1976). Quadratic assignment as a general data analysis strategy. *Br. J. Math. Stat. Psychol.* https://doi.org/10.1111/j.2044-8317.1976.tb00714.x
7. Weber, R. L. (1978). A seriation of the late prehistoric Santa Maria culture of northwestern Argentina. Field Museum of Natural History. https://doi.org/10.5962/bhl.title.5189
8. Gower, J. C., & Rossman, A. H. (1969). 循环/圆形序贯——`RESEARCH_PLAN.md` §2.1 引用的方法出处。[无 DOI。按二手引文登记：Crossref 补核（冻结 `results/lit_takeover2_check.txt`，"gower-rossman-1969" 组）未返回 1969 对应条目。题名与载体不做补造。]

**B. 全局结构 / 几何 / 对称性（8）**

9. Kemp, J. (2026). Symmetry in category systems across languages. *Nat. Commun.* https://doi.org/10.1038/s41467-025-67463-4
10. Evans, N., & Levinson, S. C. (2009). The myth of language universals: Language diversity and its importance for cognitive science. *BBS, 32*(5), 429–448. https://doi.org/10.1017/s0140525x0999094x
11. Piantadosi, S. C., & Gibson, E. (2014). Quantitative standards for absolute linguistic universals. *Cogn. Sci., 38*(4), 736–756. https://doi.org/10.1111/cogs.12088
12. Levinson, S. C., & Meira, M. (2003). "Natural concepts" in the spatial topological domain — adpositional meanings in crosslinguistic… *Language*. https://doi.org/10.1353/lan.2003.0174 [题名在冻结记录内截断]
13. Amalric, M., Wang, D., Pica, P., Figueira, C., Sigman, M., & Dehaene, S. (2017). The language of geometry: Fast comprehension of geometrical primitives and rules in human adults. *PLOS Comput. Biol.* https://doi.org/10.1371/journal.pcbi.1005273
14. Port, J. G., Gheorghita, M., Guth, S., Clark, A., Liang, P., & Dasu, S. (2018). Persistent topology of syntax. *Math. Comput. Sci.* https://doi.org/10.1007/s11786-017-0329-x
15. Port, J. G., Karidi, R., & Marcolli, M. (2022). Topological analysis of syntactic structures. *Math. Comput. Sci.* https://doi.org/10.1007/s11786-021-00520-5
16. Evangelopoulos, G. M., Brockmeier, S., Mu, T., & Goulermas, J. (2020). Circular object arrangement using spherical embeddings. *Pattern Recognition, 103*, 107192. https://doi.org/10.1016/j.patcog.2019.107192

**C. 层次 / 树感知 / 潜因子比较器（5）**

17. Jäger, G., & Wahle, J. (2021). Phylogenetic typology. *Front. Psychol., 12*. https://doi.org/10.3389/fpsyg.2021.682132
18. Murawaki, H. (2015). Continuous space representations of linguistic typology and their application to phylogene… *NAACL-HLT 2015*. https://doi.org/10.3115/v1/n15-1036 [题名在冻结记录内截断]
19. Neureiter, A., Ranacher, J., Efrat-Kowalsky, S., Kaiping, J., Weibel, M., & Widmer, R. (2022). Detecting contact in language trees: A Bayesian phylogenetic model with horizontal transfe… *Research Square 预印本*（Crossref 载体字段为空）. https://doi.org/10.21203/rs.3.rs-1262191/v1 [题名在冻结记录内截断]
20. Verkerk, M., Shcherbakova, A., Haynie, T., Skirgård, Ø., Rzymski, C., & Atkinson, Q. D. (2025). Enduring constraints on grammar revealed by Bayesian spatiophylogenetic analyses. *Nat. Hum. Behav., 10*(1), 126–136. https://doi.org/10.1038/s41562-025-02325-z
21. Bjerva, Y., Kementchedjhieva, T., Cotterell, R., & Augenstein, I. (2019). A probabilistic generative model of linguistic typology. *NAACL-HLT 2019*. https://doi.org/10.18653/v1/N19-1156

**D. WALS 特征预测任务（3）**

22. Bjerva, Y., Salesky, M., Mielke, S. J., Chaudhary, V., Celano, M., & Ponti, E. (2020). SIGTYP 2020 shared task: Prediction of typological features. *Proc. SIGTYP 2020*. https://doi.org/10.18653/v1/2020.sigtyp-1.1
23. Vastl, M., Zeman, D., & Rosa, R. (2020). Predicting typological features in WALS using language embeddings and conditional probabil… *Proc. SIGTYP 2020*. https://doi.org/10.18653/v1/2020.sigtyp-1.4 [题名在冻结记录内截断]
24. Gutkin, E., & Sproat, R. (2020). NEMO: Frequentist inference approach to constrained linguistic typology feature prediction. *Proc. SIGTYP 2020*. https://doi.org/10.18653/v1/2020.sigtyp-1.3

**E. 数据层文档（5）**

25. Graff, A., Chousou-Polydouri, E., Inman, D., Skirgård, Ø., Lischka, S., & Zakharko, N. (2025). Curating global datasets of structural linguistic features for independence. *Sci. Data, 12*. https://doi.org/10.1038/s41597-024-04319-4
26. Skirgård, Ø., Haynie, T., Blasi, D. G., Hammarström, K., Collins, J., & Latarche, S. (2023). Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss. *Sci. Adv., 9*(16). https://doi.org/10.1126/sciadv.adg6175
27. Dryer, M. S. A., & Haspelmath, M. (Eds.). (2013). *The World Atlas of Language Structures Online*. Leipzig: Max Planck Institute for Evolutionary Anthropology. wals.info. CC-BY-4.0. [本地数据层元数据（`data/raw/wals/metadata.json`）；无 DOI——补核的 3 条 Crossref 命中均为书评，非本书本身。]
28. Hammarström, K., Forkel, R., Haspelmath, M., & Bank, S. (2025). *Glottolog 5.2.1*. Leipzig: Max Planck Institute for Evolutionary Anthropology. glottolog.org. CC-BY-4.0. [本地数据层元数据（`data/raw/glottolog/cldf-metadata.json` bibliographicCitation）；无 DOI。]
29. Forkel, R., List, M., Greenhill, S. J., et al. (2018). Cross-linguistic data formats: Advancing data sharing and re-use in comparative linguistics. *Sci. Data, 5*, 180058. https://doi.org/10.1038/sdata.2018.205 [经冻结 `results/lit_takeover2_check.txt` 核验]

**引用纪律：** 本文只引用上述 29 条登记表条目（加钉死的本地数据层元数据）；未经核验的文献不入稿。冻结登记表的 §F 跨域误命中记录于该表内，*不属于*引用宇宙。
