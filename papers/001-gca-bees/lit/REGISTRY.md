# REGISTRY.md — 文献登记表（ARIS4C-001 段1 · 冻结）

> 冻结时间：2026-09-26（段1 结束）· run: ARIS4C-001 重跑
> 方法：OpenAlex API 多轮检索（code/fetch_round1–5.py）→ 去重 279 条 → 蜜蜂相关候选 67 条（results/bees_cand.txt）→ 逐条 Crossref 核（code/verify_crossref.py → results/crossref_check.txt）；Zenodo 数据集经 DataCite 核。
> 统计量层级：**A**=个体水平原始数据公开可取；**B**=报告个体水平分布参数/相关（均值±SD、r、N，无原始数据；"可能A"=OA 全文/附录待段2核实是否含逐个体数据）；**C**=仅组水平统计。
> 任务代码：D=简单辨别；R=逆转；P=负patterning/配置；O1=opt-out难度敏感；O2=opt-out增益；O3=opt-out迁移/泛化。多任务=同一批个体完成≥2任务。
> 核实状态：VERIFIED=Crossref（或 DataCite）确认 DOI 存在且标题/第一作者/年份对齐；OpenAlex 摘要缺失处标注"无摘要"，统计量以原文为准（段2 提取），本表不虚构数字。

## 条目（25 条）

**[1] Bermant (1966). Discrimination training and reversal in groups of honey bees. *Psychonomic Science*. DOI 10.3758/bf03328341。** 任务 D+R。N：组水平（无个体数据）。层级 C。关键统计量：OpenAlex 无摘要；组水平辨别+逆转表现（全文付费，未核）。相关性：最早的"辨别+逆转"双任务组水平报告之一（历史锚点）。核实：VERIFIED（Crossref 1966/Bermant/标题匹配）。

**[2] Wells & Haines (1986). Optimal Diet, Minimal Uncertainty and Individual Constancy in the Foraging of Honey Bees. *Journal of Animal Ecology*. DOI 10.2307/4422。** 任务 O1 相关（不确定性下的觅食决策+个体恒常性）。N：个体恒常性得分（全文核）。层级 B。关键统计量：无摘要（pre-DOI 年代，JSTOR）；个体恒常性数据见原文。相关性：个体水平觅食恒常性/不确定性回避的经典证据。核实：VERIFIED（Crossref 1986/Wells/标题匹配）。

**[3] Gould (1986). Pattern learning by honey bees. *Animal Behaviour*. DOI 10.1016/s0003-3472(86)80157-9。** 任务 P（模式/配置学习）。N：组。层级 C。关键统计量：无摘要（付费）。相关性：配置学习的经典报告。核实：VERIFIED（Crossref 1986/Gould/标题匹配）。

**[4] Benatar & Papaj (1995). Selection on a haploid genotype for discrimination learning performance: Correlation between discrimination learning and [第二性状，全文核]. *Journal of Insect Behavior*. DOI 10.1007/bf01997235。** 任务 D（+标题所示第二性状）。N：个体（选系内，全文核）。层级 B。关键统计量：无摘要；个体学习得分的系间差异见原文。相关性：辨别学习的遗传改良+跨性状相关（个体差异的遗传架构）。多任务：是（D+第二性状，待核）。核实：VERIFIED（Crossref 1995/Benatar/标题匹配）。

**[5] Scheiner, Wcislo et al. (1999). Tactile learning and the individual evaluation of the reward in honey bees (*Apis mellifera* L.). *J. Comparative Physiology A*. DOI 10.1007/s003590050360。** 任务 D（触觉辨别）。N：个体（全文核）。层级 B。关键统计量：无摘要。相关性：个体水平触觉辨别学习+奖励评估差异。核实：VERIFIED（Crossref 1999/Scheiner/标题匹配）。

**[6] Chandra, Srinivasan, Smith & Page (2000). Heritable variation for latent inhibition and its correlation with reversal learning in honeybees. *Journal of Comparative Psychology*. DOI 10.1037/0735-7036.114.1.86。**（OpenAlex 显示双斜杠 DOI 10.1037//…，规范形已核。）任务 R+LI（两个学习任务）。N：个体（全文核）。层级 B（报告个体水平 r）。关键统计量：无摘要（APA 付费）；LI 与逆转的个体水平相关 r 见原文。相关性：**estimand ① 核心输入**——同一个体两任务个体水平相关。多任务：是。核实：VERIFIED（Crossref 2000/Chandra/标题匹配）。

**[7] Ben-Shahar et al. (2000). Differences in performance on a reversal learning test and division of labor in honey bee colonies. *Animal Cognition*. DOI 10.1007/s100710000068。** 任务 R+分工（行为）。N：个体（全文核）。层级 B。关键统计量：无摘要。相关性：个体逆转表现×分工（学习个体差异与行为分工关联）。多任务：是（R+任务表现）。核实：VERIFIED（Crossref 2000/Ben-Shahar/标题匹配）。

**[8] Scheiner et al. (2001). The Effects of Genotype, Foraging Role, and Sucrose Responsiveness on the Tactile Learning Performance of Honeybees. *Neurobiology of Learning and Memory*. DOI 10.1006/nlme.2000.3996。** 任务 D（触觉）+蔗糖反应性+觅食角色。N：个体（全文核）。层级 B。关键统计量：无摘要。相关性：多性状个体水平数据（学习×动机×行为），可作"动机/努力"维度输入。多任务：是。核实：VERIFIED（Crossref 2001/Scheiner/标题匹配）。

**[9] Chandra et al. (2001). Quantitative Trait Loci Associated with Reversal Learning and Latent Inhibition in Honeybees (*Apis mellifera*). *Behavior Genetics*. DOI 10.1023/a:1012227308783。** 任务 R+LI。N：家系内个体（全文核）。层级 B。关键统计量：无摘要。相关性：跨任务相关的遗传基础（QTL）——支持 GCA 假说的遗传架构证据。多任务：是。核实：VERIFIED（Crossref 2001/Chandra/标题匹配）。

**[10] Komischke et al. (2002). Successive Olfactory Reversal Learning in Honeybees. *Learning & Memory*. DOI 10.1101/lm.44602。** 任务 R（连续逆转）。N：组（全文核）。层级 C（OA；组学习曲线）。关键统计量：摘要无数值（OA 全文：3/2/1/0 次前序逆转条件下的组水平表现）。相关性：任务内经验（successive reversal、"learn to learn"）对照。核实：VERIFIED（Crossref 2002/Komischke/标题匹配）。

**[11] Chen, Dyer & Srinivasan (2003). Global perception in small brains: Topological pattern recognition in honey bees. *PNAS*. DOI 10.1073/pnas.0732090100。** 任务 P（拓扑模式辨别）。N：组（OA 全文核）。层级 C（OA；组正确率）。关键统计量：摘要无数值（OA 全文：拓扑不同模式辨别更快更好，拓扑等价模式慢且差）。相关性：自由飞行蜜蜂的配置学习。核实：VERIFIED（Crossref 2003/Chen/标题匹配）。

**[12] Mota et al. (2010). Multiple reversal olfactory learning in honeybees. *Frontiers in Behavioral Neuroscience*. DOI 10.3389/fnbeh.2010.00048。** 任务 R（多次逆转）。N：组（OA 全文核）。层级 C（OA）。关键统计量：摘要无数值。相关性：重复逆转的"learn to learn"对照。核实：VERIFIED（Crossref 2010/Mota/标题匹配）。

**[13] Hadar et al. (2010). Memory Formation in Reversal Learning of the Honeybee. *Frontiers in Behavioral Neuroscience*. DOI 10.3389/fnbeh.2010.00186。** 任务 R。N：组（OA 全文核）。层级 C（OA）。关键统计量：摘要无数值。相关性：逆转记忆的神经/认知机制（背景）。核实：VERIFIED（Crossref 2010/Hadar/标题匹配）。

**[14] Carr-Markell et al. (2014). Comparing Reversal-Learning Abilities, Sucrose Responsiveness, and Foraging Experience Between [两种亚种，全文核]. *Journal of Insect Behavior*. DOI 10.1007/s10905-014-9465-1。** 任务 R+蔗糖反应性+觅食经验。N：个体（全文核）。层级 B。关键统计量：无摘要。相关性：多性状个体水平比较（学习×动机×经验），跨任务结构候选输入。多任务：是。核实：VERIFIED（Crossref 2014/Carr-Markell/标题匹配）。

**[15] Muszynski et al. (2015). Relational learning in honeybees (*Apis mellifera*): Oddity and nonoddity discrimination. *Behavioural Processes*. DOI 10.1016/j.beproc.2015.03.001。** 任务 P（关系/奇异性辨别）。N：个体（全文核）。层级 B。关键统计量：无摘要。相关性：关系/配置辨别个体水平表现。多任务：是（oddity+nonoddity 两规则）。核实：VERIFIED（Crossref 2015/Muszynski/标题匹配）。

**[16] Benaets et al. (2017). Covert deformed wing virus infections have long-term deleterious effects on honeybee foraging and learning. *Proc. R. Soc. B*. DOI 10.1098/rspb.2016.2149。** 任务 D（学习）+觅食（行为）。N：RFID 标记个体（OA 全文核）。层级 B（OA；逐个体觅食/学习；原始数据待核）。关键统计量：摘要无数值（OA：DWV 隐性感染→死亡↑、早龄觅食、觅食活动期缩短）。相关性：个体水平学习+觅食（隐性感染作为个体差异来源）。多任务：是。核实：VERIFIED（Crossref 2017/Benaets/标题匹配）。

**[17] Pérez Claudio et al. (2018). Appetitive reversal learning differences of two honey bee subspecies with different foraging behaviour. *PeerJ*. DOI 10.7717/peerj.5918。** 任务 R。N：亚种×个体（OA 全文核）。层级 B（OA；个体学习曲线；SI 原始数据待核）。关键统计量：摘要无数值（OA：common-garden 下 A.m. caucasica vs A.m. syriaca 食欲性逆转学习比较）。相关性：个体水平逆转学习曲线（试次级），亚种间差异。多任务：单任务（R）但试次级重复测量。核实：VERIFIED（Crossref 2018/Pérez Claudio/标题匹配）。

**[18] Perry et al. (2013). Honey bees selectively avoid difficult choices. *PNAS*. DOI 10.1073/pnas.1314571110。** 任务 O1（难度敏感 opt-out）+D。N：组/block 水平（OA 全文核个体/block 比例）。层级 C（可能 B——OA 全文段2核）。关键统计量：摘要无数值（OA 全文：有 opt-out 选项时蜜蜂回避更难的辨别）。相关性：**蜜蜂 opt-out/难度敏感核心论文**——estimand ② 的主要来源。多任务：是（强迫辨别 vs 有 opt-out 的辨别）。核实：VERIFIED（Crossref 2013/Perry/标题匹配；本 run 初估年份 2014，经核为 2013，已更正）。

**[19] Cheeseman et al. (2014). Way-finding in displaced clock-shifted bees proves bees use a cognitive map. *PNAS*. DOI 10.1073/pnas.1408039111。** 任务：导航（非 6 类核心任务，背景）。N：OA 全文核。层级 C（OA）。关键统计量：摘要无数值。相关性：扰动下个体导航表现（GCA 背景证据）。核实：VERIFIED（Crossref 2014/Cheeseman/标题匹配）。

**[20] Raıne et al. (2012). No Trade-Off between Learning Speed and Associative Flexibility in Bumblebees: A Reversal Learning Study. *PLoS ONE*. DOI 10.1371/journal.pone.0045096。** 任务 D+R（同一批个体）。N：个体（OA 全文核）。层级 B（OA；个体水平学习速度×逆转相关；SI 原始数据待核）。关键统计量：摘要无数值（OA：学得快者逆转也快，无权衡；过夜保留测试）。相关性：Bombus 跨物种对照——两个任务间个体水平正相关（GCA 样结构的跨物种支持）。多任务：是。核实：VERIFIED（Crossref 2012/Raine/标题匹配）。

**[21] Evans et al. (2017). Fast learning in free-foraging bumble bees is negatively correlated with lifetime resource collection. *Scientific Reports*. DOI 10.1038/s41598-017-00389-0。** 任务 D+觅食（同一批个体，实验室→野外）。N：85 工蜂（摘要明示）。层级 B（OA；个体水平学习×觅食相关；SI 待核）。关键统计量：摘要明示 N=85，学习与觅食表现存在可观个体差异且未被预测。相关性：Bombus——学习表现与生态表现（同一批个体、两个测量）的个体水平关联。多任务：是。核实：VERIFIED（Crossref 2017/Evans/标题匹配）。

**[22] Hendriksma et al. (2019). Individual and Colony Level Foraging Decisions of Bumble Bees and Honey Bees in Relation to Balance of Payments. *Frontiers in Ecology and Evolution*. DOI 10.3389/fevo.2019.00177。** 任务：觅食决策（O3 邻近：能量平衡下的选择/回避）。N：个体+蜂群（OA 全文核）。层级 B（OA）。关键统计量：摘要无数值。相关性：个体 vs 群体水平觅食决策（两物种），觅食层"选择/回避"证据。多任务：是（个体+群体水平）。核实：VERIFIED（Crossref 2019/Hendriksma/标题匹配）。

**[23] Finke et al. (2023). Individual consistency in the learning abilities of honey bees: cognitive specialization within colonies. *Animal Cognition*. DOI 10.1007/s10071-022-01741-2。** 任务 D+R+P（4 个实验：视觉/嗅觉 × Pavlovian/操作，简单辨别、逆转、负 patterning）。N：个体（OA 全文核）。层级 B（OA；个体水平跨任务相关；**SI 是否含逐个体数据待段2核实，若有则升 A**）。关键统计量：摘要无数值（OA 全文：考察简单辨别与逆转/负 patterning 表现是否个体水平相关——段2 提取 r/N）。相关性：**estimand ① 核心研究**——学习能力的个体一致性（同一批个体 ≥3 任务）。多任务：是。核实：VERIFIED（Crossref 2023/Finke/标题匹配）。

**[24] Golańska et al. (2026). Buzzed but not elated? Effect of ethanol on cognitive judgement bias in honeybees. *Animal Cognition*. DOI 10.1007/s10071-026-02076-y。** 任务：不确定性代理（认知判断偏倚 CJB；非 opt-out）。N：个体（OA 全文核）。层级 B（OA）。关键统计量：摘要无数值（OA：1% 乙醇对 CJB 的效应；经典嗅觉条件化后 CJB 测试）。相关性：个体水平判断偏倚（不确定性/情感加工代理）——支持不确定性监控证据链的辅助证据。多任务：否（单一 CJB 范式）。核实：VERIFIED（Crossref 2026/Golański/标题匹配；核对时"Golan"字符差异系变音符号，非不匹配）。

**[25] Oxman et al. (2026). Honey bees increase recruitment effort when dance information is honest. *Behavioral Ecology and Sociobiology*. DOI 10.1007/s00265-026-03744-2。** 任务：precision/信心（舞蹈可靠性→招募努力；O1/O3 代理）。N：焦点蜂个体+试次（OA 全文+数据核）。层级 **A**（Zenodo 原始数据 10.5281/zenodo.17771502 经 DataCite 核实存在；姊妹记录 10.5281/zenodo.17771503）。关键统计量：摘要无数值（OA 全文：可靠性操纵下焦点蜂舞蹈被追随/招募努力的个体-试次模式）。相关性：**唯一公开的个体+试次级原始数据集**——precision 型潜变量（可靠性/信心评估）→ estimand ② 降级方案核心。多任务：是（可靠性处理×试次）。核实：VERIFIED（论文 Crossref 2026/Oxman/标题匹配；数据 DataCite OK，Zenodo 2025）。

## 检索日志（2026-09-26，OpenAlex/Crossref）
| 轮 | 查询 | 返回/总数 |
|---|---|---|
| r1 | "Apis mellifera discrimination learning" | 20/3628 |
| r1 | "Apis mellifera reversal learning" | 20/1120 |
| r1 | "Apis mellifera negative patterning" | 20/22394（噪声多） |
| r1 | "Apis mellifera opt-out foraging" | 20/895（噪声多） |
| r1 | "Apis mellifera metacognition confidence" | 19/19 |
| r2 | title:"opt-out"；title:reversal+honey；title:patterning+honey；title:confidence+bee；title:metacognition | 20/3135；20/36；20/304；6/6；20/10128（5 条多词查询因 URL 空格失败，r3 修复） |
| r3 | author "Avila d'Avila Leal"；title:"opt out"+bee；title:"general cognitive ability"；"honey bee uncertainty decision"；"Dyer cognitive abilities of bees"；"Oxman bees confidence recruitment"；title:confidence+honey；"honey bee opt-out difficulty" | 25/699；0/0；20/358；20/8827；15/2629；10/226；1/1；20/2292 |
| r4 | Crossref 书目检索："Apis mellifera opt-out"、"Avila d'Avila Leal honey bee learning"、"Dyer honey bee cognitive abilities review"、"honey bee negative patterning"；OpenAlex author "Avila d'Avila Leal" | 12/15/10/10 条（0 条核心相关）；作者 0 匹配 |
| r5 | author "Avila Leal"（8 匹配，0 相关）；"honey bee abstention"；"bee opt out confidence"；"Apis mellifera uncertainty" | 8/155（0 相关）；8/1606 → **命中 Perry 2013**；8/4801 → 命中 Wells 1986 |

## 备注
- 合计 OpenAlex 去重 279 条，蜜蜂相关候选 67 条；登记表 25 条，引用 32 条逐条核（Crossref 31 + DataCite 1），30 条完全 OK，2 条标记（Perry 2013 年份预期 2014→实为 2013；Golański 变音符号）均已按 Crossref/DataCite 元数据修正，无编造。
- OpenAlex 特性：Chandra 2000 DOI 在 OpenAlex 显示为双斜杠 "10.1037//0735-7036.114.1.86"，规范形（已核）"10.1037/0735-7036.114.1.86"。
- 未纳入：Menzel (1969) "On the honey bee's memory of spectral colors: reversal learning and learning…"（*J. Comp. Physiol.*，pre-DOI，无 DOI/Crossref 记录）——历史锚点仅口头提及，不入表。
- G. Avila d'Avila Leal 在 OpenAlex 无作者记录，其第一作者论文未出现在任何轮次检索结果中；Perry 2013 等关键论文以 Crossref 元数据为准。此缺口不构成编造风险，但段2 写稿引用作者列表时以 Crossref 返回为准。
- **冻结**：2026-09-26 段1 结束，本表冻结（25 条目 / 32 引用）。段2 只可引用本表条目；新增引用须补 Crossref 核并追加"段2 增补"小节，不得改动已冻结条目。
