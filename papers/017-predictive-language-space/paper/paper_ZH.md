# 预测未见之物：类型学特征空间中的留出配置预测与对缺席组合的校准支持度

> **Provenance（来源追踪）.** ARIS4C-017 · Predictive Language Space (LING-02)，本地确定性重跑（ARIS v0.4.26；无 GPU）。数据：Grambank v1.0，repo commit 37f73da55cf8b426c82383f46a972bc59ce6cf76，获取于 2026-09-25T11:50:05Z，values sha256 b5ad64804fb092496c4447938a1a5143f502c95e0799833db97b064c13d22363。冻结阶段：Pilot-0 2026-09-25T15:42:09Z，P2 2026-09-25T16:46:44Z，P3 2026-09-25T21:41:36Z。本稿中所有数字均逐字抄录自冻结阶段产物（results/pilot0_results.json、results/p2_results.json、results/p3_results.json 及其冻结摘要/笔记）；为本文档未重跑任何分析、未重新生成任何图、未重新获取任何数据。

## 摘要

类型学数据库记录了世界各语言中哪些语法特征共现，但这一空间的经验约束结构很少被当作未见配置的预测器来检验。我们提出一个可证伪的问题：观测到的类型学空间能否预测留出语言实际呈现的特征？在 Grambank v1.0（2467 种语言、195 个参数；481065 个单元格的 75.25% 被观测）上，我们执行了一个预注册的三步阶梯，设六个竞争约束模型与六个证伪条件。(i) 留出语言基线：在随机划分下，语系先验优于全局边际（logloss 0.4275 对 0.5106），但当整个南岛语系（536 种语言）或 Papunesia 地理大区（728 种语言）被留出时，先验坍缩回边际——这是一个跨组迁移缺口。(ii) 掩蔽特征预测：潜因子模型（C4）在 logloss（0.5396 对 0.7011，随机单特征任务）与校准（ECE 0.0158 对 0.1866）上均优于树感知邻居模型（C3），且两者都将真实留出特征束排在 1000 个伪配置之上（池化 rank-AUC：C3 0.57–0.79，C4 0.73–0.78，全部 > 0.5）。(iii) 空格支持度：在一个包含 32 个真正缺席组合的 17053 个双特征组合全集上，≥4/6 模型共识由 1428 个低支持度单元格构成，且包含全部 32 个空格；而流形密度模型与能量模型未能通过跨种子稳定性（mean Spearman 0.103 < 0.5，触发条件 ④）与稀有组合校准（Spearman 0.065 与 0.034 < 0.5，触发条件 ⑤）。判定：配置可预测性获支持（H1、H3）；谱系稳健性被证伪（H2，触发条件 ①：C3 语系 logloss 0.7820 ≥ 边际 0.5252）；校准弃权仅部分获支持（H4）。针对历史与灭绝语言的外部留出（P4）未在本轮执行，留作未来工作。

## 1. 引言

大规模类型学数据库——WALS 以及 2023 年以来的 Grambank——如今以统一的、机器可读的跨语言格式覆盖数千种语言与数百个结构参数（Forkel et al., 2018; Skirgård et al., 2023）。它们的使用正从描述转向建模：类型学特征成为 NLP 系统的输入信号（Kornilov & Shavrina, 2024），综述文章描绘了类型学数据库在 NLP 中的现状与展望（Baylor et al., 2023），基于语料库的梯度资源补充了词序的矩阵式图景（Baylor et al., 2024; Ring, 2025）。概念上，这一路线立足于可能性空间观：世界语言占据语法可能性的逻辑空间中一个受强烈约束的子集，而非无约束的全体（Evans & Levinson, 2009）。

围绕这些矩阵的大部分工作仍是描述性或相关性分析：分布、地图、共现网络，以及对类型学假设的下游检验（Shcherbakova, Gast & Blasi, 2022; Shcherbakova, Michaelis & Haynie, 2023; Shcherbakova, Blasi & Gast, 2024）。一个更尖锐、可证伪的检验一直缺失：类型学空间的经验约束结构能否预测留出语言——或留出特征槽位——实际呈现的配置？本稿把类型学空间从描述对象转变为预测目标，并在预注册的留出条件下评估一族竞争约束模型。

该设计遵循 LING-02 脚手架——一个预测阶梯。P1（在本实现中为 Pilot-0）留出整语言并预测其完整特征向量，设三个层级——random（随机）、language-family-held-out（语系留出）与 macroarea-held-out（地理大区留出）——以建立基线并暴露结构无法迁移之处。P2 在留出语言内掩蔽单个特征或预设的三特征束，从剩余结构中预测，并加入不确定性校准与配置排序检验。P3 仅在 P1/P2 之后进入，用六个支持度模型为特征对空间的未观测区域打分，并询问低支持度"空格"能否以校准、稳定的方式被识别——作为分级支持度，而非不可能性声明。P4 是针对历史与灭绝语言的外部留出，不在本轮范围内（第 6 节）。比较器之间不预设赢家：特征边际、语系/地理先验、树感知邻居、潜因子、一个图模型、一个非线性流形模型与一个约束/能量模型全部参与竞争（谱系比较动机：Atkinson & Gray, 2005）。

四个假设、六个证伪条件构成本评估的骨架。H1（预测约束）：多元结构预测留出特征优于特征频率基线。H2（谱系稳健）：至少部分预测增益在语系留出下存活。H3（配置预测）：已验证的模型能把真实留出特征束排在匹配的伪配置之上。H4（校准的空缺）：低支持度缺席组合可由校准不确定性识别，而非裸缺失。六个条件为：① 语系留出下增益消失；② 性能可被地理/语系先验完全解释；③ 预设束打不过边际基线；④ 空格评分跨划分/模型族不稳定；⑤ 校准差；⑥ 独立外部留出失败。

我们的贡献是：(i) 在 Grambank v1.0 上冻结的三层留出协议，暴露了一个跨组迁移缺口——朴素组先验在其自身组被留出时无法迁移；(ii) 掩蔽特征结果：极简潜因子模型在准确率与校准上均优于树感知邻居模型，支持 H1 与 H3，并证伪 H2（触发条件 ①）；(iii) 由六个支持度模型打分的 17053 个双特征组合空格全集、捕获全部 32 个真正缺席组合的 1428 单元格共识，以及两个被触发、定位于流形与能量比较器的失败模式（④、⑤）；(iv) 对六个证伪条件的完整裁定，并将 P4 明确定位为未来工作。

## 2. 数据

我们使用 Grambank v1.0（Glottobank），一个 CLDF 格式（Forkel et al., 2018）的数据库，包含 195 个结构语法参数，为 2467 个语言条目编码。Grambank 的主描述文档记录了谱系约束强烈塑造其特征分布这一事实（Skirgård et al., 2023）——这是我们语系留出层级与树感知比较器的经验基础。Stage 1 对 WALS（192 个参数、2694 种语言、14.98% 网格覆盖、整行缺失型缺失）做了画像，作为辅助层；按设计，不合并任何数据集，全部分析仅运行于 Grambank 本身。

来源追踪（Provenance）。来源：https://grambank.clld.org；repo commit 37f73da55cf8b426c82383f46a972bc59ce6cf76；获取于 2026-09-25T11:50:05Z；values 表 sha256 b5ad64804fb092496c4447938a1a5143f502c95e0799833db97b064c13d22363。矩阵构建所用的表：values（441663 行）、languages（2467 行）、parameters（195）、codes（398）；lineage 列提供树感知模型所用的谱系前缀结构，215 棵语系树在 stage 1 中完成画像。

矩阵。语言 × 参数矩阵（results/p1_matrix.csv）为 2467 × 195 = 481065 个单元格。level 列将行划分为 2393 种语言、70 个方言与 4 个语系级节点。全部 195 个参数各带 3–5 个代码（上限 5；以二元 0/1 编码为主）。原始值分布为：0（absent）54.96%，1（present）25.43%，"?" 18.03%（79638 行），2：1.22%，3：0.34%。

缺失约定。"?" 是显式未知；它与缺失的参数行一起映射为 NaN，使 481065 个单元格中 119040 个为 NaN（0.247451），观测率为 75.25%。协变量：2463 种语言（0.16% 缺失）带有坐标；101 种语言（4.1%）缺失 Family_name；同样这 101 种语言没有谱系路径，在树感知模型中按空路径处理。冻结矩阵中不填充任何缺失单元格；模型内缺失处理遵循各比较器自身的定义（第 3 节）。

可复现性。矩阵与留出划分（results/p1_matrix.csv、results/pilot0_split_config.json）在任何 P2/P3 代码编写之前冻结（P2 的 frozen_before_code = true）；P2 与 P3 复用它们，无重新下载、重建或重采样。阶段冻结时间戳：Pilot-0 2026-09-25T15:42:09Z；P2 2026-09-25T16:46:44Z；P3 2026-09-25T21:41:36Z。

## 3. 方法

### 3.1 留出阶梯与指标

三个层级定义评估。random：5 个独立划分（种子 42–46），每个留出 493 种语言。family：整个南岛语系（aust1307；536 种语言，占矩阵 21.7%——最大语系，按规模降序取 ≥20% 前缀选出）。macroarea：整个 Papunesia 地理大区（728 种语言，29.5%）。所有比较器仅用训练行拟合；测试语言绝不进入拟合。指标各阶段一致，且仅在观测（非 NaN）单元格上计算：logloss、Brier score、macro 特征准确率、10 分箱期望校准误差（ECE）与加权可靠性斜率（校准方法论：Nguyen & O'Connor, 2015）。

### 3.2 Pilot-0 比较器

C1_marginal：全局代码频率分布，Laplace add-1 平滑，对每种语言与参数均相同。C2a_phylo：测试语言所属语系的逐语系边际（Laplace add-1）。C2b_geo：逐地理大区边际。回退规则：若组缺失/NA、在训练中缺席、或对该参数无观测值，则预测回退到 C1。因此语系层级将 C2a 与其自身回退对照，地理大区层级将 C2b 与其自身回退对照。

### 3.3 P2 任务

两类任务。single：对每种留出语言，按冻结 rng 行序掩蔽 k = min(5, n_observed) 个观测单元格（掩蔽种子：random 用划分子种子，family 用 1042，macroarea 用 1043）；每个掩蔽单元格是独立的预测目标。bundle：三个预设参数的全部观测单元格一起掩蔽。束是确定性的：B1 = GB068、GB074、GB075（按字典序前三个名称匹配 word-order/modifier/position 的参数——谓语核心形容词行为、前置词、后置词）；B2 = GB079、GB080、GB081（紧随 B1 的三参数块——动词前缀、后缀、中缀化）；B3 = GB262、GB041、GB306（从剩余 189 个参数中用 rng(42) 抽取——句首是非疑问粒子、补偿式数词、非二值相互代词）。

### 3.4 P2 模型

C3_tree（树感知邻居）：对测试语言 t 与参数 p，每个训练语言 i 按 glottocode 路径分量计算谱系前缀距离 d = 1 − 2L/(len_t + len_i)（对 101 种无谱系的语言取空路径）、权重 w_i = exp(−3d)·(1 + 2·[same family])·(1 + 0.5·[same macroarea])，预测为 P(c | t, p) = (Σ_i w_i·1[x_i = c] + 1) / (Σ_i w_i + K_p)，其中 K_p 是 p 的合法代码数。若 Σw = 0，或语系与地理大区均为 NA，则单元格回退到 C1。前缀距离是文献中比较的若干类型学距离选项之一（Guzmán Naranjo & Jäger, 2024）；它是 C3 使用的唯一结构。

C4_ldm（潜因子）：Bjerva et al. (2019) 潜变量 + 特征读出结构的极简非神经重实现——不是完整模型（无 RNN、无概念词典）。(parameter, code) one-hot 矩阵有 398 个槽位（4 个非零基参数 GB024/GB025/GB065/GB130 使用其实际代码位置）。训练用 soft-impute，30 次迭代，秩 3，缺失单元格初始化为 C1 概率，得到 X ≈ F·Aᵀ。对测试语言，潜向量 f_t 由其观测槽位（排除任务掩蔽单元格）经最小二乘读出，P(c | t, p) ∝ max(0, A_{p,c}·f_t)；若所有代码得分 ≤ 0，或无任何槽位被观测，则单元格回退到 C1。

### 3.5 H3 配置排序

对每个三个单元格均被观测的束，真实配置的得分为三个逐单元格预测概率之积（特征独立近似，设计中有注明），并以从每个参数合法代码集中均匀采样每个单元格的方式抽取 1000 个伪配置。单一全局 rng(42) 按固定顺序 layer × 语言行 × B1→B3 生成伪配置，且 C3 与 C4 共享同一伪配置集，因此行内模型对比是公平的。我们报告平均秩（1 = 最佳；≈501 = 随机）与 1001 个配置上的 rank AUC（并列计 0.5）。

### 3.6 P3 支持度模型

对 P3，每个模型为冻结参数对每个合法 (code_i, code_j) 组合赋予一个非负支持度；支持度越高表示越合理。C1_indep：两个全局 Laplace 边际之积。C3_tree：跨语言的谱系加权经验共现均值（与 §3.4 相同权重，leave-self-out，Laplace +1）。C4_ldm：跨语言、§3.4 中两个潜因子读出概率之积的均值（条件独立近似，设计中有注明）。C5_graph：逐对秩 1 对数线性模型——log P̂(ci,cj) ≈ α_i + β_j + u_i·v_j，以 100 轮 ALS（种子 42）拟合 Laplace 平滑的对频数，支持度 = 对参数对网格做 softmax(α+β+uᵀv)。C6_manifold：对 one-hot (language, slot) 矩阵（缺失槽位置 0）做 t-SNE 嵌入（perplexity 30，PCA 初始化，种子 42）；某组合的支持度为以两个代码质心之和为高斯密度中心、跨语言的均值，带宽 σ = 最近邻距离中位数（全局 0.5555）。C7_energy：率比能量——E = clip(−ln(rate/rate_indep), ±ln 50)，使用 Laplace 平滑的对率，且 rate_indep = C1 之积；支持度 = 在网格上归一化的 exp(−E)。

## 4. 结果

下文所有数字均可追溯至冻结产物（pilot0_results.json、p2_results.json、p3_results.json 及其逐阶段摘要）；random 层数值为 5 种子（42–46）均值 ± 标准差。

### 4.1 Pilot-0：组先验可迁移，随后消失

随机留出下，两个组先验均优于全局边际：C2a_phylo 达到 logloss 0.4275±0.0015（相对 C1 的 0.5106±0.0018，Δ = −0.0831），macro 准确率 0.8061 对 0.7466；C2b_geo 达到 0.4721±0.0027（Δ = −0.0386）；C2a 的 ece 温和上升（0.0174 对 0.0047）（figures/pilot0_comparison.png, pilot0_calibration_marginal.png）。当定义先验的组被整体留出时，先验消失：语系留出（aust1307，536 种语言，语料的 21.7%）下 C2a 恰好回退到 C1（0.5252 = 0.5252，设计使然），而 C2b 退化至 0.5833；地理大区留出（Papunesia，728 种语言，29.5%）下 C2b 恰好回退（0.5323 = 0.5323），而 C2a 保留部分增益（0.5087，相对 C1 的 0.5323，Δ = −0.0236）（figures/pilot0_calibration_phylo.png）。这种不对称性是 Pilot-0 的核心发现：谱系先验部分地存活于地理大区留出，但没有先验能存活于其自身定义组的留出。这个跨组迁移缺口正是 P2 与 P3 的目标。

### 4.2 P2：掩蔽特征预测

在掩蔽单元格上，潜因子模型 C4 在层级表几乎每一行都压倒树感知模型 C3（figures/p2_comparison.png, p2_calibration.png）。Random single：C4 logloss 0.5396±0.0271 对 C3 的 0.7011±0.0048（Δ = −0.1615）；macro 准确率近乎持平（0.7828 对 0.7855，n = 2464），而 C4 的 ece 坍缩（0.0158 对 0.1866）。束使对比更尖锐：C4 赢 B1（0.6926 对 0.7215）与 B3（0.3952 对 0.7415），但输 B2（0.5749 对 0.5588）——B2 是唯一有利于树结构的相邻动词词缀块行。语系留出下树模型的信号坍缩——C3 single logloss 0.7820，差于 Pilot-0 的 C1 背景（0.5252），也差于其自身 random 层（0.7011）——而 C4 保持在 0.5331，与 C1 背景持平。跨组迁移缺口因此在模型层面复现，H2 的证伪条件 ① 触发。

H3 配置排序（figures/p2_h3_ranking.png, p2_h3_rank_auc.png）：在每一层，两个模型给出的真实配置排名都远高于 1000 个伪配置（随机秩 ≈ 501，随机 AUC = 0.5）。跨束池化后，random 上 C3 平均秩 147.1 / AUC 0.7914，C4 151.5 / 0.7841（n = 4745）；family 上 369.7 / 0.5685 对 203.3 / 0.7348；macroarea 上 228.5 / 0.7099 对 174.0 / 0.7643。B3（补偿式数词、非二值相互代词、句首是非疑问粒子）是最容易的任务（秩 51–105，AUC 0.83–0.89）。有一个单元格是病态的：C3 的 family B1，AUC 0.2113 低于随机（准确率 0.1702）——树模型在被留出语系内部的词序配置上是系统性反信息的。
假设裁决（由冻结设计锁定）：H1（预测约束）获支持——所有 h3_all AUC 均 > 0.5；H2（谱系稳健）被 ① 证伪；H3（配置预测）获支持；H4（校准缺口）被部分证伪——C4 的校准远优于 C3（random ece 0.0158 对 0.1866），但 C3 的 ece 在每一行都偏高，且 C4 的 family/macroarea 束 ece（0.08–0.13）仍超过 0.05 阈值，故条件 ⑤ 触发，稀有单元格的完整校准推迟到 P3。

### 4.3 P3：空格全集与六个支持度模型

全集（universe）：观测 ≥200 且代码 ≥2 的 195 个参数；在 ≥300 种语言中共现的配对共 18915 对，按字典序截断取前 4000（自 GB020–GB021 至 GB047–GB316）；其 17053 个合法代码组合由 32 个真空格（从未被观测）、484 个稀有组合（1–10 次观测）与 14726 个高频单元格（≥50）构成。每个模型的最底十分位含 1705 个单元格。全集（全局拟合）上的支持度中位数对五个模型处于概率尺度——C1 0.1643、C3 0.1078、C4 0.1643、C5 0.1609、C7 0.2425——而 C6_manifold 处于密度尺度（中位数 1.54e-04），因为它输出的是均值高斯密度而非概率（figures/p3_comparison.png）。
一致性（item 1）。在 17053 全集上，四个计数/结构模型 C1、C3、C4、C5 几乎完全一致——两两 Spearman 0.972–0.996——而凡涉及 C6 或 C7 的配对均 ≤ 0.120（figures/p3_agreement.png）。在 32-空格集上局面反转：只有 C1|C4 仍高（+0.900），C1|C7 转为强负（−0.946），C3|C6 为负（−0.424）。共识低支持度集（落在 ≥4/6 个模型最底十分位内）大小为 1428 且包含全部 32 个真空格；C4 将共识单元格排在全集的 1 至 3611 之间（中位 719.5）。

种子稳定性（item 2；五个随机划分，每个模型在训练划分上重拟合）。C1 0.9997、C3 0.9993、C4 0.9996、C5 0.9993 与 C7 0.9634 均远高于 0.5 阈值，但 C6_manifold 坍缩到 0.1028（最小 −0.0425），触发证伪条件 ④。C6 的带宽在各划分间漂移（σ 0.603–0.649，对比全局 0.5555），与 t-SNE 已知的逐次运行敏感性一致。
稀有校准（item 3；484 个稀有单元格，软标签取自 Laplace 率；figures/p3_calibration.png）。C3（对 log 计数的 Spearman 0.927）与 C5（0.932）对最稀有单元格的排序最佳；C1（0.599）与 C4（0.636）中等；C6（0.065）与 C7（0.034）处于随机水平，且 C7 还伴随最差的 logloss（0.2700，其余模型均 ≤0.039）与 brier（0.0603，其余模型均 ≤1.9e-05）。触发条件 ⑤（false_low_rate > 0.10 或 Spearman < 0.5）对 C6（Spearman 0.065；false_low_rate 0.0987，略低于 0.10）与 C7（Spearman 0.034；false_low_rate 0.0799）触发。C6 的 logloss/brier 是代理值——其支持度是密度，截断已在设计中注明。C5 在 4000 对中的 3999 对上收敛。

弃权（item 4）。C1–C5 的最底十分位弃权集与共识集的 Jaccard 重叠为 0.800–0.829，且每个都包含全部 32 个真空格；C6 的弃权集仅重叠 0.063（3/32 空格），C7 为 0.129（13/32）。校准失败的两个模型，恰好是弃权集与共识集不重叠的两个模型。
## 5. 讨论

三个阶段干净利落地分解了迁移问题。朴素组先验在随机留出下有增益（Pilot-0），但在其自身定义组被留出时消失——这就是跨组迁移缺口。在掩蔽预测上，极简非神经潜因子模型在每一层与校准上都击败树感知模型，且树模型的谱系信号在语系留出下坍缩（H2 被证伪，条件 ①）；潜因子模型保持在背景水平（0.5331 对比 C1 的 0.5252），因此它收窄而非闭合了这一缺口。在空格全集上，四个结构各异的计数模型（独立、谱系加权共现、潜因子、逐对对数线性）对 17053 个合法组合中哪些不可信几乎完全一致（两两 Spearman ≥ 0.97），其联合最底十分位包含全部 32 个真空格，且共识在五次重拟合下稳定、对稀有单元格校准良好（C3/C5 Spearman ≈ 0.93）。

六个支持度模型中的两个以互补的方式失败。C6_manifold 不稳定（种子稳定性 0.103，④）且校准失准（Spearman 0.065，⑤）：嵌入步骤的随机几何主导了下游平均——这是对将随机嵌入用作可信度骨干的一个警示性结果。C7_energy 稳定（0.963）但校准失准（0.034）且在空格集上反信息（对比 C1 为 −0.946）；其固定的 ±ln 50 截断把支持度的动态范围压在上限 50 倍之内，全局独立基线也与漏掉单个配对的局部稀疏性相一致。有一个 P2 单元格值得注意：C3 的 family B1（秩 AUC 0.2113，准确率 0.1702）系统性低于随机——谱系加权对被留出语系内部的词序配置可能变得反信息；本文不诊断其成因。H4 裁决（部分证伪）在 P3 之后依然成立：计数模型对稀有单元格校准良好，但分布偏移下的束 ece（C4 0.08–0.13）表明偏移下的校准仍是开放问题。

局限性。(i) 配对全集是 18915 个合格配对按字典序截断到 4000 的结果；结论在该子集上成立，未必迁移到更稀有的配对。(ii) H3 配置得分使用了 §3.5 注明的特征独立近似。(iii) C6 的 logloss/brier 是带截断的密度代理值。(iv) Grambank v1.0 覆盖 2467 种语言，其中 101 种无谱系代码，C3 的距离对它们回退到语系/地理大区标志位。(v) "支持度"是可信度得分而非后验概率；本文未推导任何决策程序（例如田野调查应优先哪个空格）。
## 6. 结论与未来工作

从原始 Grambank v1.0 数据与从零开始编写的代码出发，我们确立了：(1) 组先验在随机留出下可迁移，但在其定义组被留出时消失；(2) 极简非神经潜因子模型在掩蔽预测上优于树感知模型，且该差距在组留出下仍然存在——只是被收窄；(3) 四个计数模型对 17053 个合法代码组合的共识包含全部 32 个真空格，且在重拟合下稳定、对稀有单元格校准良好。未来工作（P4）：以覆盖率感知的配对选择取代字典序截断；用一个小联合模型取代配置打分中的特征独立近似；并把共识转化为可执行的优先级——一份供数据采集的空格组合排名表，使成本与覆盖率的权衡显式化。

## 参考文献

以下所有条目均在正文中被引用，取自冻结的文献笔记（lit/LIT_NOTES.md）。核实状态：Baylor 2023/2024、Kornilov & Shavrina 2024 与 Ring 2025 于 2026-09-25 对照其 arXiv 摘要页核实；Skirgård et al. 2023、Atkinson & Gray 2005、Evans & Levinson 2009 与 Forkel et al. 2018 于 2026-09-26 按 DOI 经 Crossref 复核（完整题名与作者列表以 Crossref 登记为准）；其余条目沿用 stage-1 扫描所得 OpenAlex 元数据。
Atkinson, Q. D., & Gray, R. D. (2005). Curious parallels and curious connections—phylogenetic thinking in biology and historical linguistics. *Systematic Biology*. doi:10.1080/10635150590950317

Baylor, K., Ploeger, D., & Bjerva, Y. (2023). The past, present, and future of typological databases in NLP. *arXiv preprint* arXiv:2310.13440.

Baylor, K., Ploeger, D., & Bjerva, Y. (2024). Multilingual gradient word-order typology from Universal Dependencies. *Proceedings of EACL 2024*. arXiv:2402.01513.

Bjerva, Y., Kementchedjhieva, T., & Cotterell, R. (2019). A probabilistic generative model of linguistic typology. *Proceedings of NAACL-HLT 2019*. doi:10.18653/v1/n19-1156

Evans, N., & Levinson, S. C. (2009). The myth of language universals: Language diversity and its importance for cognitive science. *Behavioral and Brain Sciences*. doi:10.1017/s0140525x0999094x

Forkel, R., List, J.-M., Greenhill, S. J., Rzymski, C., & Bank, S. (2018). Cross-linguistic data formats, advancing data sharing and re-use in comparative linguistics. *Scientific Data*. doi:10.1038/sdata.2018.205

Guzmán Naranjo, L., & Jäger, G. (2024). Euclide, the crow, the wolf and the pedestrian: distance metrics for linguistic typology. *Open Research Europe*. doi:10.12688/openreseurope.16141.2

Kornilov, A., & Shavrina, M. (2024). From MTEB to MTOB: Retrieval-augmented classification for descriptive grammars. *arXiv preprint* arXiv:2411.15577.

Nguyen, D., & O'Connor, B. (2015). Posterior calibration and exploratory analysis for NLP models. *Proceedings of EMNLP 2015*. doi:10.18653/v1/d15-1182

Ring, H. (2025). Extending dependencies to the taggedPBC: Word order in transitive clauses. *arXiv preprint* arXiv:2506.06785.

Shcherbakova, O., Gast, C., & Blasi, D. E. (2022). A quantitative global test of the complexity trade-off hypothesis. *Linguistics Vanguard*. doi:10.1515/lingvan-2021-0011

Shcherbakova, O., Michaelis, A., & Haynie, H. J. (2023). Societies of strangers do not speak less complex languages. *Science Advances*. doi:10.1126/sciadv.adf7704

Shcherbakova, O., Blasi, D. E., & Gast, C. (2024). The evolutionary dynamics of how languages signal who does what to whom. *Scientific Reports*. doi:10.1038/s41598-024-51542-5

Skirgård, H., Haynie, H. J., Blasi, D. E., Hammarström, H., & Collins, J. (2023). Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss. *Science Advances*. doi:10.1126/sciadv.adg6175
