# 一般认知能力还是任务特异性结构？蜜蜂学习中的跨任务协方差与试次级决策分析

**ARIS4C-001 · 已发表数据定量再分析 · 主语言：ZH（EN 镜像：`paper_EN.md`）**

## 摘要

已发表研究记录了蜜蜂（*Apis mellifera*）学习表现与难度敏感决策中的大量个体差异，但通常仅凭跨任务相关的存在就推断出"一般认知能力"（GCA）或"元认知"，而未做形式化模型比较。本文对满足预设标准的全部已发表数据——25 项研究、32 条引用，逐条经 Crossref/DataCite 核实——在两个互补层面进行再分析。（i）**跨任务协方差结构**：相关层元分析，检验五个预设模型（M1 单一一般因子；M2 双相关因子；M3 双独立因子；M4 任务局部零结构；M5 混合），确认性对比为 M1 vs M4。（ii）**试次级决策分析**：基于唯一公开可用的个体-试次数据集（536 个入口事件、213 只跟随蜂、325 个试次；Oxman 等 2026），混合模型检验什么预测 opt-out 型招募努力——客观信息含量、舞者可靠性人格、还是潜在 precision 代理。结果：零结构零假设（M4）被**拒绝**（合并简单辨别-逆转 r = 0.571 [0.369, 0.722]，k = 3；辨别-负 patterning r = 0.277 [0.164, 0.383]，k = 4），但单因子模型（M1）仅**部分支持**：12 个可提取的研究内相关全部为正、3 变量协方差矩阵均正定，但最弱一条边（逆转-负 patterning）在全部四个单实验中均不显著，合并估计（r = 0.185，p = .028）在留一实验检验下处于临界（最大 p = .087）。试次级分析给出**稳健的信息追踪**（每单位 focal 环路 β = 0.0106，p < .001，跨变换与子样本稳定）与**稳健的舞者人格效应**（跟随不可靠"骗子"舞者的蜂跟随时长多约 26%；对数尺度 β = 0.2346，p = 2.5×10⁻⁵）；信息敏感度的个体差异——即我们的潜在 precision 代理——仅有提示性（高敏感组符号检验 p = .023）而非确认性（Welch p = .233；交互 p = .390）。按预注册主张策略，这些数据**不能**确立蜜蜂的 GCA：以简单辨别为强极的层级结构获支持，不确定性监控/元认知主张须有独立证据链。

## 1. 引言

### 1.1 昆虫学习中的个体差异

蜜蜂通过联想条件化和更复杂的配置过程学习 [27][28]。四十余年的工作中反复出现的发现是：个体在学习表现上差异显著——触觉辨别 [5]、逆转学习 [7][17]、带/不带潜伏抑制的辨别 [6]、嗅觉逆转 [10][12][13]。不确定性下觅食决策的个体恒常性是经典结果 [2]；选择实验表明辨别学习表现可遗传且与其他性状相关，暗示跨性状协变的遗传架构 [4][9]。多性状个体水平数据（学习 × 动机 × 觅食经验）进一步表明"学习能力"与动机和生态维度纠缠在一起 [8][14][16]。跨物种看，熊蜂中存在同样模式：个体学习速度与逆转速度正相关，且无速度-灵活性权衡 [20]；同一批个体的学习表现与终身觅食产出共变 [21]。迄今最直接的证据来自 Finke 等 2023：同一批蜂完成三项任务——简单辨别、逆转、负 patterning——跨任务表现在个体水平上相关 [23]。

### 1.2 从跨任务协方差到"一般认知能力"

人类心理计量学中，一般因子（g）的确立依赖形式化模型比较：给定数据，单因子模型必须优于局部备选模型。而昆虫文献中的推断通常被视为直接成立：因为个体在多个任务上以相似方式变化，就被说成拥有"一般认知能力" [23]——当任务包含弃权/opt-out 选项时，则被说成"元认知"或"不确定性监控" [18][24]。这一跳跃欠约束。正的跨任务协变与真正的一般因子、层级（群因子）结构、方法因子、部分任务局部依赖都相容。区分它们需要显式模型与显式对比，而非显著相关的单纯存在。

### 1.3 opt-out 行为：观察决策监控的窗口

Opt-out（弃权）范式让动物把不确定选择的期望价值与安全选项比较；在人和啮齿类中，此类选项的使用索引信心与不确定性监控 [28][29][30]。在蜜蜂中，Perry 等 2013 证明有 opt-out 选项时蜜蜂选择性地回避困难选择 [18]；蜜蜂与熊蜂的觅食选择工作记录了能量平衡与选项价值敏感度 [22]。方法学工作告诫 opt-out 选项的存在本身会移动选择模式 [32]；认知判断偏倚（CJB）工作提供了相邻的、个体水平的蜜蜂不确定性加工测量 [24]。因此，opt-out 型决策的试次级账户至少须区分三个候选驱动：(a)**客观试次难度**、(b)**近期奖惩历史**、(c) 关于信息源的**潜在 precision（可靠性/信心）变量**。

### 1.4 缺口

没有任何已发表的蜜蜂数据分析对 GCA 推断做过形式化模型比较；在 Oxman 等 2026 之前，也没有已发表的试次级数据集公开可用——我们登记表中唯一的 A 级数据集，提供操纵舞蹈可靠性下个体与试次级的招募努力数据 [25]。两个缺口现在都可以仅用已发表数据闭合。

### 1.5 目标与预注册主张策略

我们检验两个 estimand。**Estimand ①（跨任务结构）**：个体水平指标（简单辨别、逆转、负 patterning、opt-out 难度敏感、opt-out 增益、opt-out 迁移）的协方差结构。**Estimand ②（试次级过程）**：什么更好地预测 opt-out 型决策——客观难度、近期强化历史、还是潜在 precision 型变量。五个确认性模型预设且不预设胜者：M1 单一一般因子；M2 双相关因子；M3 双独立因子；M4 任务局部零结构（无一般因子，每任务独立过程）；M5 混合（基线学习/决策效率上有潜在个体因子，而 opt-out 决策由习得的试次级价值生成）。探索性预测-precision 比较仅在 M1–M5 可估处允许，不预注册符号、最优或神经定位。**主张策略（预注册）**："一般学习能力"仅当模型比较明确支持 M1/M2 时可讨论；不确定性监控/元认知/意识主张各需独立证据链，不得从因子存在推断；神经推论标注为假设而非证据。

## 2. 数据与文献登记

### 2.1 检索与核引

五轮 OpenAlex 查询（任务关键词 + 作者检索；去重后 279 条，蜜蜂相关候选 67 条）产出冻结登记表 **25 项研究 / 32 条引用**。每条引用均经 Crossref（31 条）或 DataCite（1 条，Zenodo 数据集）核实；30 条完全匹配，2 条按出版方元数据标记并修正（Perry 等年份 2014 → 2013；"Golański" 变音符号变体）。不虚构任何统计量：摘要或 OA 文本缺数字处，该格标注"不可提取"。完整登记表、检索日志与核实文件见 `lit/REGISTRY.md` 与 `results/crossref_check.txt`。

### 2.2 统计量层级

每条按可获得的公开统计量最细粒度分层：**A 级** = 个体水平原始数据公开可取（1 条：Oxman 等 2026，Zenodo 10.5281/zenodo.17771502）；**B 级** = 报告个体水平分布或相关但无原始数据（16 条，其中 5 条为"可能 A"，待补材料核实）；**C 级** = 仅组水平统计（8 条）。补材料核实（段2）确认 Finke 等 2023 的 SI 仅含组水平 GLMM 表（表 S1–S24，无逐个体数据）→ 维持 B 级；Raine 2012 / Evans 2017 / Pérez Claudio 2018 的个体水平数值在已报告处从 OA 全文提取。

### 2.3 Estimand 可行性判定（段1 闸门）

- **Estimand ①** 在原始数据层不可行（除单任务重复外无多任务个体水平数据集）。重新规定为**相关层元分析**：确认性输入为 Finke 等 2023（同一批个体、三任务、四实验）[23]，辅以 Chandra 等 2000（潜伏抑制 × 逆转；闭源全文不可提取——记录而不填补）[6] 与跨物种熊蜂对 Raine 等 2012 [20]；Evans 等 2017 贡献学习-生态对 [21]。
- **Estimand ②** 对完整难度/奖励/precision 设计不可行。降级到唯一 A 级数据集：Oxman 等 2026（舞蹈可靠性操纵 → 跟随者招募努力，个体 × 试次）[25]，辅以 Perry 等 2013 组/block 级 opt-out 数据 [18]。

### 2.4 M1–M5 操作化

可估指标集为三项任务——简单辨别（RL1）、逆转（RL2）、负 patterning（NP）——来自 Finke 等 2023。恰好三个指标时单因子模型**饱和**，故确认性 M1 vs M4 对比操作化为**相关模式检验**：(a) 全部可提取研究内相关的成对显著性；(b) 每个实验 3 变量相关矩阵的正定性（行列式 1 + 2r₁₂r₁₃r₂₃ − r₁² − r₂² − r₃² > 0）；(c) 跨实验 DerSimonian–Laird 随机效应元分析。M4（零结构）在相当比例边显著为正时被拒绝。**M2/M3 不可估**（登记表无同一批个体 ≥4 任务个体水平数据；原因记录于 `results/stage2_results.json`）。**M5** 两阶段估计：学习侧个体因子（M1 操作化）+ block 级 opt-out 敏感性分析（Perry 等 2013，逐蜂相加 χ² = 25.349，df = 10，P = .005；7/10 蜂在有 opt-out 时适应性回避困难条件）[18]。

**表 1.** 提取的研究内个体水平相关（段2；完整文件 `lit/corr_pairs.csv`，16 行）。

| 来源 | 对 | r | N | 注 |
|---|---|---|---|---|
| Finke 2023 [23]，实验 1 | RL1–RL2 | 0.53 | 27 | |
| Finke 2023 [23]，实验 1 | RL1–NP | 0.42 | 33 | |
| Finke 2023 [23]，实验 1 | RL2–NP | 0.25 | 27 | 单实验不显著 |
| Finke 2023 [23]，实验 2 | RL1–RL2 | 0.60 | 20 | |
| Finke 2023 [23]，实验 2 | RL1–NP | 0.46 | 22 | |
| Finke 2023 [23]，实验 2 | RL2–NP | 0.19 | 20 | 单实验不显著 |
| Finke 2023 [23]，实验 3 | RL1–RL2 | — | — | 不可估（RL1 得分退化） |
| Finke 2023 [23]，实验 3 | RL1–NP | 0.18 | 140 | |
| Finke 2023 [23]，实验 3 | RL2–NP | 0.18 | 61 | 单实验不显著 |
| Finke 2023 [23]，实验 4 | RL1–RL2 | — | — | 不可估（RL1 得分退化） |
| Finke 2023 [23]，实验 4 | RL1–NP | 0.33 | 89 | |
| Finke 2023 [23]，实验 4 | RL2–NP | 0.15 | 42 | 单实验不显著 |
| Raine 2012 [20] | D–R（速度） | 0.60 | 18 | Spearman ρ；剔除异常值稳健变体 |
| Evans 2017 [21] | LPI–试次时长 | 0.62 | 48 | LPI = 学习表现指数 |
| Evans 2017 [21] | LPI–采集天数 | — | 49 | 正文无精确 ρ（图 2a）；Poisson GLMM 0.06 ± 0.02（表 2），方向：学得快者采集天数更少 |
| Chandra 2000 [6] | LI–R | — | — | 不可提取（无 OA 全文） |

## 3. 跨任务协方差结构（段2）

所有元分析统计量：Fisher z 变换、DerSimonian–Laird 随机效应合并、双尾检验。完整数值：`results/s2_precision.json`（段2 主产物；`results/stage2_results.json` 含可行性判定记录）。

### 3.1 M4（任务局部零结构）：被拒绝

| 边 | 合并 r | 95% CI | k | p |
|---|---|---|---|---|
| RL1–RL2（研究内） | 0.56 | [0.316, 0.735] | 2 | .0001 |
| RL1–NP（研究内） | 0.277 | [0.164, 0.383] | 4 | <.001 |
| 简单辨别→逆转（跨研究：Finke 实验 1–2 + Raine 2012） | 0.571 | [0.369, 0.722] | 3 | <.001 |
| RL2–NP（研究内） | 0.185 | [0.020, 0.340] | 4 | .028 |

四条边中三条在合并水平显著为正，最强边（简单辨别-逆转）在 Finke 两个实验与独立的跨物种熊蜂数据集 [20] 中均显著。因此"所有跨任务协方差为零"的模型被**拒绝**。

### 3.2 M1（单一一般因子）：部分支持

- 全部 12 个可提取研究内相关（表 1）方向**为正**。
- 两个数据完整的 3 变量相关矩阵（Finke 实验 1：N = 27/33；实验 2：N = 20/22）均**正定**（行列式 0.5915 与 0.4972），满足公共因子表示的要求。
- 但 RL2–NP 边在**全部四个单实验中不显著**（r = 0.25/0.19/0.18/0.15，各在其 N 下 p > .05），仅在合并水平达显著（p = .028，CI 勉强排除 0）。

在三项任务上大幅且等量负荷的单因子未获确立；数据支持**层级结构：简单辨别（RL1）为强极**，其与负 patterning 的关联较弱但元分析意义上可靠非零。

### 3.3 M2 / M3：不可估

登记表无同一批个体 >3 任务的个体水平数据，双因子模型无法拟合或对比。不可估性（及使各自可估所需的数据条件）记录于 `results/stage2_results.json`；我们对 M2/M3 **不作主张**。

### 3.4 M5（混合，两阶段）

- **学习侧**：同 §3.2（以 RL1 为锚的个体结构）。
- **opt-out 侧（Perry 等 2013 [18]）**：跨 block 难度敏感回避的逐蜂相加分析：χ² = 25.349，df = 10，P = .005，7/10 蜂在有 opt-out 时适应性回避困难条件。组/block 级数据排除蜂内试次模型；原始逐蜂计数不在 OA 文本中，故该数值按报告使用（仅一致性核对；见 §5）。

### 3.5 段2 探索性 precision 分析（Oxman 2026，三层）

| 层 | 检验 | 结果 |
|---|---|---|
| 事件层（n = 536） | Mann–Whitney，诚实 vs 骗子舞者 | p = .0618（rank-biserial 0.093）——边缘 |
| 事件层（n = 536） | OLS 原始努力 ~ is_liar + focal | is_liar β = 0.2272，p < .001；focal β = 0.0104，p < .001；R² = .096 |
| 个体层（两阶段均可见的 56 只跟随者） | 配对 Δ + 符号检验 | Δ = 0.136，t = 0.219，p = .827；29/56 为正，p = .894——**不支持** |
| 阶段层（n = 135） | OLS ~ is_liar + focal | focal β = 0.0894 [0.065, 0.114]，p < .0001，R² = .283；is_liar p = .239 ns |

中间判读（段3 细化）：**信息追踪强**；**个性效应在事件层显著但与阶段混杂**（加入阶段协变量后 ns）；**敏感度的个体差异在该层不支持**。

## 4. 试次级决策分析（段3）

### 4.1 数据与模型设定

试次级分析使用 Oxman（2026；Raw Follower Data，Zenodo 10.5281/zenodo.17771502）随文发布的首次进入事件表：325 个蜂试次共 536 个首次进入事件，由 213 只不同跟随者观测（234 个诚实条件事件、302 个骗子条件事件；305 个学习阶段、231 个测试阶段）。因变量为 log1p（跟随者到达入口前跟随的环数），保留全零单元格。固定效应：骗子条件（is_liar）、试次级线索信息量（focal，段2 计算）、阶段（测试 vs 学习）。含跟随者身份（ID）随机截距；REML 估计，模型收敛（对数似然 = −484.28）。全部检验双尾；未预注册方向性假设（沿用段2 纪律）。

**表 2.** 主试次级混合模型（n = 536 事件；REML，收敛）。

| 项 | β | 95% CI | p |
|---|---|---|---|
| is_liar（骗子 vs 诚实） | 0.2346 | [0.1255, 0.3437] | 2.5e-05 |
| focal（线索信息量） | 0.0106 | [0.0078, 0.0134] | < .001 |
| stage（测试 vs 学习） | 0.0652 | [−0.0360, 0.1664] | .207 |
| Var(ID) | 0.0293 | — | — |
| Var(残差) | 0.3170 | — | — |

R²m = .112，R²c = .130。

两个关注效应均为正且（§5 所示）稳健：骗子条件下的跟随者在 log1p 尺度上持续时长约多 26%（exp(0.2346) − 1 = 0.264）；每单位线索信息量对应约多 1.1% 的环路（exp(0.0106) − 1 = 0.0107）。阶段效应不显著。

### 4.2 Precision 代理：线索加权度的个体差异

冻结设计不支持完整潜在 precision 模型；因此检验两个代理，回答"是否有些蜂比另一些更重视线索？"

**随机斜率。** 允许 focal 斜率跨 ID 变化：斜率方差非可忽略（Var = 0.00087；对截距-only 拟合的似然比检验 p = .080）但不显著；ID×focal 协方差 = −0.0272（p = .110）。斜率分布非奇异；R²c 从 .130 升至 .298。

**高/低分层。** 在两个条件均可见的 47 只跟随者中，按逐蜂 β_focal 中位数（0.0185；24 只高敏感、23 只低敏感）分组：高敏感组的骗子效应更大（β_hi = 0.3904 [0.1711, 0.6097]）vs 低敏感组（β_lo = 0.1835 [−0.0699, 0.4368]）；Welch t = 1.210，df = 43.8，p = .233。符号检验：高组 18/24 为正（p = .023）vs 低组 11/23（p = 1.0）。交互模型（is_liar × high_sens）给出 is_liar × high_sens β = −0.1291 [−0.4236, 0.1654]，p = .390（n = 264 事件；R²m = .132）。

判读：线索加权度个体差异的证据**有提示性但非确认性**——随机斜率方差处于边缘，组对比与交互均不显著，且三者皆为探索性事后检验。我们仅将其报告为代理，不作确认性主张（见 §7）。

### 4.3 近期结果代理

作为进一步的探索性检验，用逐蜂近期结果摘要（该蜂先前事件的平均线索值；剔除试次内首事件，余 n = 211）替换试次级 focal 项。recent_mean β = 0.2176 [0.0563, 0.3788]，p = .008；二值近期正向指标不显著（β = 0.1465，p = .365）。两者同入模型时骗子效应（p = .006）与剩余 focal 项（p < .001）均保持；阶段不显著（p = .452）。此模型为探索性：随机效应塌缩到边界（Var(ID) = 0），交叉结构不支持，近期结果效应仅作事后观察。

## 5. 稳健性

§3–§4 的每个定量主张均在表 3 的扰动下重新估计。全部检验双尾；未预注册多重性校正，故对探索性条目避免族式表述。

**表 3.** 稳健性矩阵。

| # | 扰动 | 结果 | 判定 |
|---|---|---|---|
| 1 | 元分析留一法，RL1–NP（k = 4） | 剔除后 r = .258（p = 4e-05）、.262（p = 2e-05）、.370（p = 1e-05）、.252（p = 4.6e-04） | 稳健 |
| 2 | 元分析留一法，RL1–RL2（k = 2） | r = .600（p = .0043）、.530（p = .0038） | 稳健 |
| 3 | 元分析留一法，RL2–NP（k = 4） | 合并 r = .185（p = .028）；剔除实验 2 p = .040，**剔除实验 3 p = .087（ns）**，剔除实验 4 p = .045 | **临界**——显著性依赖实验 3（n = 61） |
| 4 | 全部 16 个报告相关单元格（corr_pairs.csv）对源表复算 | 16/16 复现 | OK |
| 5 | Perry 等（2013）两阶段分析 | 原始计数不在 OA 版；χ²(10) = 25.349，P = .005，7/10 适应——仅一致性核对 | 与报告一致 |
| 6 | 主模型不做 log1p（原始努力，OLS） | is_liar 1.4417（p = 4e-05）；focal 0.0716（p < .001）；stage p = .103 | 结论不变 |
| 7 | 剔除单次事件跟随者（n = 446 事件） | is_liar 1.5613 [0.7717, 2.3510]（p = 1.1e-04）；focal 0.0782 [0.0579, 0.0984]（p < .001）；stage p = .183 | 结论不变 |

唯一临界情形（第 3 行）在讨论 RL2–NP 的两处（§3.1 与此处）均如实报告：合并关联显著，但显著性由一个研究承载。所有试次级结论（§4）同时通过未变换结果（第 6 行）与单次事件剔除（第 7 行）。

## 6. 讨论

### 6.1 任务特异性结构，而非单一 GCA 因子

跨任务证据拒绝强 M4 主张（跨三个任务家族的单一一般协方差因子）。协方差结构实为**层级且由任务结构驱动**：RL1–RL2 协方差强（合并 r ≈ .56；研究内 .53–.60，表 1），两者与无问题对照中等相关（RL1–NP r ≈ .28），但 RL2–NP 关联弱且临界（r ≈ .19，§3.1、§5 第 3 行）。这是**相关觅食型任务内共享程序/可学习结构 + 一个不跨结构异质任务的一般"投入"成分**的签名——不是跨所有任务预测的单一 GCA 签名。按主张策略，这是 M1 的部分支持（两级结构：家族内强、跨家族弱/临界），不构成 GCA 解释的支持。

### 6.2 试次级数据展示了什么、没展示什么

事件层有两个稳健效应：(i) 线索为骗子时跟随者持续更久（β = 0.2346，p = 2.5e-05，log1p 尺度约 +26%）；(ii) 跟随者追踪线索的信息含量（focal β = 0.0106，p < .001，跨变换与剔除稳定）。阶段效应不显著，意味着学习 vs 测试对这两个效应不构成混杂。这支持狭窄判读：蜜蜂**监控其所跟随对象的信息价值**——信息追踪效应——而骗子效应提示社会信息无奖励时系统性过度持续，与弱"信任先验"相容，而非校准的监控器。

Precision 问题（蜂对线索的加权是否不同？）**非确认性**：随机斜率方差边缘（p = .080），高/低对比（p = .233）与交互（p = .390）均不显著。我们将其报告为提示性代理。同样，近期结果效应（p = .008）为探索性且依赖边界塌缩的随机结构。

### 6.3 主张策略下的边界

三条边界直接推出：

1. **不作 GCA 主张。** M4 被拒、M1 仅部分支持，故不主张蜜蜂具一般认知能力。获支持的最强表述是两级任务协方差结构（家族内强、跨家族弱/临界）。
2. **不确定性监控需独立证据链。** 本文的信息追踪效应是线索价值的*相关物*，不是主观不确定性的直接测量（如信心下注或元认知探针）。任何"蜜蜂监控不确定性"的主张必须立足于直接测量不确定性反应的设计；我们的试次级数据仅支持行为追踪客观线索信息。
3. **神经推论标注为假设。** 任何调用神经基底（如蘑菇体介导的不确定性编码）的账户都是待检验假设，不是本再分析的结论；我们不作此类因果主张。

## 7. 局限

1. **RL2–NP 临界。** 跨家族关联的显著性依赖一个研究（Finke 实验 3，n = 61）；跨家族协方差比合并估计提示的更弱、可能为零。
2. **Precision 代理为探索性。** 随机斜率方差（p = .080）、高/低对比（p = .233）、交互（p = .390）均为事后；对线索加权度的个体差异不作确认性主张。
3. **近期结果代理**依赖边界塌缩的随机结构（Var(ID) = 0），仅作事后观察。
4. **Perry 等（2013）**原始计数不在 OA 版，其两阶段结果（χ²(10) = 25.349，P = .005）按报告使用；仅一致性核对，未重算。
5. **Finke 等（2023）**相关按已发表表/SI 报告（B 级）；补材料的个体水平数据无法从 OA 记录核实，层级未能升 A。
6. **Chandra 等（2000）**无 OA 全文；潜伏抑制 × 逆转的个体水平 r 不可提取，未纳入元分析。
7. **试次级 = 单一已发表设计。** 事件层分析基于单一数据集（Oxman 等，2026；213 只跟随者）；骗子效应反映一种特定可靠性操纵，外推有限。
8. **推断纪律。** 未预注册方向性假设；全部检验双尾；探索性条目未做多重性校正，故需独立重复。
9. **focal 为操作化指数。** 按冻结设计定义索引线索信息量；raw/log1p 不变性（§5 第 6–7 行）说明效应非变换伪迹，但操作化选择约束幅度解释。
10. **随机结构受数据约束。** 约化模型不支持交叉效应（如蜂 × 试次）；所有随机结构陈述限于数据可支撑范围。

## 8. 溯源与可重复性

- **流水线。** ARIS v0.4.26 编排器执行，单一内网 LLM 网关；全部统计代码运行于 Python 3.13 venv。本次运行在 LLM 执行进程 128K 上下文上限死亡后共需 8 次编排器接管（每次按时间戳顺序记录于 `COORDINATION.md`）；每个死亡阶段的确定性剩余由编排器直接补完，从不以相同 prompt 重跑 LLM。
- **代码。** 抽取：`code/fetch_round1–5.py`、`code/verify_crossref.py`。段2：`code/s2_precision*.py`。段3：`code/s3_trial_model.py`、`code/s3_robust.py`。
- **冻结产物。** `results/s2_precision.json`、`results/s3_trial_model.json`、`results/s3_robustness.json`、`lit/corr_pairs.csv`、`results/crossref_check.txt`、`lit/REGISTRY.md`、`lit/LIT_NOTES.md`。本文每个数字均可溯源至上述某一文件；逐数字映射见 `paper_EN_notes.md`（EN 版 notes；ZH 版数字与 EN 完全一致）。
- **引用。** 32 条引用逐条经 Crossref（31）或 DataCite（1）核实；30 条完全匹配，2 条按出版方元数据修正（Perry 等年份 2014 → 2013；Golańska 变音符号）。无未核实引用。
- **数据源。** 试次级：Oxman 等（2026），Zenodo 10.5281/zenodo.17771502（Raw Follower Data）。跨任务相关：Finke 等（2023）已发表表、Raine 等（2012）与 Evans 等（2017）OA 全文、Perry 等（2013）按报告。
- **冻结。** 段3 数值 2026-09-26 冻结；冻结后无重估。本稿件（段4）不产生新统计量。

## 参考文献

以下 32 条引用全部在收录前逐条经 Crossref（31）或 DataCite（1）核实；30 条完全匹配，2 条按出版方元数据修正（见 §8）。书目保留原文。

1. Bermant (1966). Discrimination training and reversal in groups of honey bees. *Psychonomic Science*. 10.3758/bf03328341
2. Wells, M. J., & Haines, D. W. (1986). Optimal diet, minimal uncertainty and individual constancy in the foraging of honey bees. *Journal of Animal Ecology*. 10.2307/4422
3. Gould, J. L. (1986). Pattern learning by honey bees. *Animal Behaviour*. 10.1016/s0003-3472(86)80157-9
4. Benatar, S. T., Cobey, S., & Smith, B. H. (1995). Selection on a haploid genotype for discrimination learning performance: Correlation between drone honey bees (*Apis mellifera*) and their worker progeny (Hymenoptera: Apidae). *Journal of Insect Behavior*, 8, 637–652. 10.1007/bf01997235
5. Scheiner, Wcislo, et al. (1999). Tactile learning and the individual evaluation of the reward in honey bees (*Apis mellifera* L.). *Journal of Comparative Physiology A*. 10.1007/s003590050360
6. Chandra, Srinivasan, Smith & Page (2000). Heritable variation for latent inhibition and its correlation with reversal learning in honeybees. *Journal of Comparative Psychology*. 10.1037/0735-7036.114.1.86
7. Ben-Shahar, et al. (2000). Differences in performance on a reversal learning test and division of labor in honey bee colonies. *Animal Cognition*. 10.1007/s100710000068
8. Scheiner, et al. (2001). The effects of genotype, foraging role, and sucrose responsiveness on the tactile learning performance of honeybees. *Neurobiology of Learning and Memory*. 10.1006/nlme.2000.3996
9. Chandra, et al. (2001). Quantitative trait loci associated with reversal learning and latent inhibition in honeybees (*Apis mellifera*). *Behavior Genetics*. 10.1023/a:1012227308783
10. Komischke, et al. (2002). Successive olfactory reversal learning in honeybees. *Learning & Memory*. 10.1101/lm.44602
11. Chen, D., Dyer, F. C., & Srinivasan, M. V. (2003). Global perception in small brains: Topological pattern recognition in honey bees. *PNAS*. 10.1073/pnas.0732090100
12. Mota, et al. (2010). Multiple reversal olfactory learning in honeybees. *Frontiers in Behavioral Neuroscience*. 10.3389/fnbeh.2010.00048
13. Hadar, et al. (2010). Memory formation in reversal learning of the honeybee. *Frontiers in Behavioral Neuroscience*. 10.3389/fnbeh.2010.00186
14. Carr-Markell, M. K., & Robinson, G. E. (2014). Comparing reversal-learning abilities, sucrose responsiveness, and foraging experience between scout and non-scout honey bee (*Apis mellifera*) foragers. *Journal of Insect Behavior*. 10.1007/s10905-014-9465-1
15. Muszynski, et al. (2015). Relational learning in honeybees (*Apis mellifera*): Oddity and nonoddity discrimination. *Behavioural Processes*. 10.1016/j.beproc.2015.03.001
16. Benaets, et al. (2017). Covert deformed wing virus infections have long-term deleterious effects on honeybee foraging and learning. *Proceedings of the Royal Society B*. 10.1098/rspb.2016.2149
17. Pérez Claudio, et al. (2018). Appetitive reversal learning differences of two honey bee subspecies with different foraging behaviour. *PeerJ*. 10.7717/peerj.5918
18. Perry, et al. (2013). Honey bees selectively avoid difficult choices. *PNAS*. 10.1073/pnas.1314571110
19. Cheeseman, et al. (2014). Way-finding in displaced clock-shifted bees proves bees use a cognitive map. *PNAS*. 10.1073/pnas.1408039111
20. Raine, et al. (2012). No trade-off between learning speed and associative flexibility in bumblebees: A reversal learning study. *PLoS ONE*. 10.1371/journal.pone.0045096
21. Evans, et al. (2017). Fast learning in free-foraging bumble bees is negatively correlated with lifetime resource collection. *Scientific Reports*. 10.1038/s41598-017-00389-0
22. Hendriksma, et al. (2019). Individual and colony level foraging decisions of bumble bees and honey bees in relation to balance of payments. *Frontiers in Ecology and Evolution*. 10.3389/fevo.2019.00177
23. Finke, et al. (2023). Individual consistency in the learning abilities of honey bees: Cognitive specialization within colonies. *Animal Cognition*. 10.1007/s10071-022-01741-2
24. Golańska, et al. (2026). Buzzed but not elated? Effect of ethanol on cognitive judgement bias in honeybees. *Animal Cognition*. 10.1007/s10071-026-02076-y
25. Oxman, et al. (2026). Honey bees increase recruitment effort when dance information is honest. *Behavioral Ecology and Sociobiology*. 10.1007/s00265-026-03744-2
26. Hammer, M., & Menzel, R. (1995). Learning and memory in the honeybee. *Journal of Neuroscience*. 10.1523/jneurosci.15-03-01617.1995
27. Pahl, M., Si, A., & Zhang, S. (2013). Numerical cognition in bees and other insects. *Frontiers in Psychology*. 10.3389/fpsyg.2013.00162
28. Roberts, W., McMillan, N., Musolino, E., & Cole, M. (2012). Information seeking in animals: Metacognition? *Comparative Cognition and Behavior Reviews*. 10.3819/ccbr.2012.70005
29. Fleming, S. M., & Lau, H. C. (2014). How to measure metacognition. *Frontiers in Human Neuroscience*. 10.3389/fnhum.2014.00443
30. Qu, Z., Shi, L., So, B. C. L., Yin, J., & Kwok, S. C. (2023). Uncertainty monitoring and information seeking in non-primate animals: Meta-analysis and systematic review. *Frontiers in Ethology*. 10.3389/fetho.2023.1246370
31. Hills, T. T. (2006). Animal foraging and the evolution of goal-directed cognition. *Cognitive Science*. 10.1207/s15516709cog0000_50
32. Veldwijk, J., Lambooij, M. S., de Bekker-Grob, E. W., Smit, H. A., & de Wit, G. A. (2014). The effect of including an opt-out option in discrete choice experiments. *PLoS ONE*. 10.1371/journal.pone.0111805

数据：Oxman, K., et al. (2025). Raw Follower Data for "Honey bees increase recruitment effort when dance information is honest." Zenodo. 10.5281/zenodo.17771502（DataCite 核实；姊妹记录 10.5281/zenodo.17771503）。
