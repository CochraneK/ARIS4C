# REGISTRY — ARIS4C-002 · 文献登记表（冻结件 2a）

> 冻结：2026-09-26 22:2x · 驱动器段1 接管直写补完（第 10 次接管·接力 3，未重跑 LLM）。
> 检索：OpenAlex 7 轮（R1 periodic-table 21 / R2 circular-seriation 21 / R3 circular-robinson 24 / R4 geometry-universals 22 / R5 wals-prediction 18 / R6 phylo-typology 24 / R7 mds-linguistic 22，≥5 轮达标）+ 9 条 anchor 种子 + 27 条 found_in 缺失/其他 = **188 条唯一候选**（`results/lit_candidates.tsv`；raw 279 → 去重 179 + anchor 9）。
> 逐条核验：`results/crossref_check.txt`（executor 16:32 运行，179 行：157 OK / 9 无 DOI / 13 FAIL:404；DOI 大小写重复行在候选表已去重，故两文件计数口径差 9）+ 接力 2 补核 `results/lit_takeover2_check.txt`（22:06，4 组）。**书目字段一律以 Crossref 返回为准**（本表字段逐字摘自上述两文件 + 本地数据层元数据）。

## 0. 关键阴性发现（假设来源覆盖）
**「语言元素周期表」假设在 OpenAlex 无域内索引来源**：7 轮检索中 'periodic' 命中 4 条，全为跨域（§F），无一涉及语言类型学。假设入口 = `RESEARCH_BRIEF.md`（受检主张），非已发表文献；域内最近邻 = 全局结构/对称性方向（B1–B4）。按 stage1_prompt「条数由证据定」如实登记，**不编造假设来源**。

## A. 圆形序贯方法（待检模型核心方法族，8 条）
| # | 条目（Crossref 书目） | DOI | 核 | 核心主张 / 本篇角色 | 用 TLI·GBI·WALS |
|---|---|---|---|---|---|
| A1 | Armstrong, Guzmán & Sing Long (2021). An Optimal Algorithm for Strict Circular Seriation. SIAM J. Math. Data Sci. 3(4):1223–1250 | 10.1137/21M139356X | OK | 严格圆形序贯最优算法（精确解基准；本篇 n≤3573 下 O(n³) 不可行 → RESEARCH_PLAN §2.1 预注册局部搜索） | 否 |
| A2 | Carmona, Chepoi, Naves & Préat (2023). A Simple and Optimal Algorithm for Strict Circular Seriation. SIAM J. Math. Data Sci. 5(1):201–221 | 10.1137/22m1495342 | OK | 简单最优严格圆形序贯算法（段2/3 实现参照）。arXiv:2205.04694 为 FAIL:404 重复条目，不登记 | 否 |
| A3 | Laporte (1978). The seriation problem and the travelling salesman problem. J. Comput. Appl. Math. 4(4):259–268 | 10.1016/0771-050x(78)90024-4 | OK | 序贯问题与 TSP 关联（Robinson 距离序贯的理论基础） | 否 |
| A4 | Concas, Fenu, Rodriguez & Vandebril (2023). The seriation problem in the presence of a double Fiedler value. Numer. Algorithms 92(1):407–435 | 10.1007/s11075-022-01461-1 | OK | 谱方法序贯在双 Fiedler 值下的适用边界（M1 布局谱诊断参照） | 否 |
| A5 | Hubert (1974). SOME APPLICATIONS OF GRAPH THEORY AND RELATED NON-METRIC TECHNIQUES TO PROBLEMS OF APPROXI…（crossref_check.txt 行内题名尾部截断，照抄存目）. Br. J. Math. Stat. Psychol. | 10.1111/j.2044-8317.1974.tb00534.x | OK | 图论/非度量技术的近似序贯应用（方法先例） | 否 |
| A6 | Hubert & Schultz (1976). QUADRATIC ASSIGNMENT AS A GENERAL DATA ANALYSIS STRATEGY. Br. J. Math. Stat. Psychol. | 10.1111/j.2044-8317.1976.tb00714.x | OK | QAP 通用数据策略（序贯/布局问题统一视角） | 否 |
| A7 | Weber (1978). A seriation of the late prehistoric Santa Maria culture of northwestern Argentina / Ronald L. Weber, Field Museum of Natural History. | 10.5962/bhl.title.5189 | OK | 考古学序贯应用（方法外推先例） | 否 |
| A8 | Gower & Rossman (1969). 圆形序贯统计方法（RESEARCH_PLAN §2.1 方法出处） | 无 | 补核未命中 | **无 DOI**；接力 2 Crossref 补核（lit_takeover2_check.txt「gower-rossman-1969」组）未返回 1969 对应条目（仅 3 条相关序贯文献：2002 书章 ×2 + Multiobjective Seriation）→ 按二手引文登记，题名/载体不补造 | 否 |

## B. 全局结构 / 几何 / 对称性（L1 假设域内最近邻，8 条）
| # | 条目（Crossref 书目） | DOI | 核 | 核心主张 / 本篇角色 | 用 TLI·GBI·WALS |
|---|---|---|---|---|---|
| B1 | Kemp (2026). Symmetry in category systems across languages. Nat. Commun. | 10.1038/s41467-025-67463-4 | OK | 跨语言范畴系统对称性（**域内与「全局结构」主张最近邻**；自有语料，未用三层） | 否 |
| B2 | Evans & Levinson (2009). The myth of language universals: Language diversity and its importance for cognitive science. BBS 32(5):429–448 | 10.1017/s0140525x0999094x | OK | 语言多样性挑战普遍语假说（H3 跨层稳健性 + claims 纪律背景） | 否（引 WALS 前版作背景） |
| B3 | Piantadosi & Gibson (2014). Quantitative Standards for Absolute Linguistic Universals. Cogn. Sci. 38(4):736–756（Crossref 卷年 2014；候选表 OpenAlex 年 2013） | 10.1111/cogs.12088 | OK | 绝对普遍语的定量频率标准（段2 边际基线判据背景） | WALS（前版） |
| B4 | Levinson & Meira (2003). ‘Natural concepts’ in the spatial topological domain — Adpositional meanings in crosslinguistic…（Crossref 作者列表 2 名 + 空位，题名行内截断）. Language | 10.1353/lan.2003.0174 | OK | 空间拓扑概念自然性（几何语言论先例） | 否 |
| B5 | Amalric, Wang, Pica, Figueira, Sigman & Dehaene (2017). The language of geometry: Fast comprehension of geometrical primitives and rules in human adults. PLOS Comput. Biol. | 10.1371/journal.pcbi.1005273 | OK | 人类几何基元/规则快速习得（几何表征背景，非类型学） | 否 |
| B6 | Port, Gheorghita, Guth, Clark, Liang & Dasu (2018). Persistent Topology of Syntax. Math. Comput. Sci. | 10.1007/s11786-017-0329-x | OK | 句法持续同调（语言结构拓扑度量先例） | 否 |
| B7 | Port, Karidi & Marcolli (2022). Topological Analysis of Syntactic Structures. Math. Comput. Sci. | 10.1007/s11786-021-00520-5 | OK | 句法结构拓扑分析（B6 同脉络） | 否 |
| B8 | Evangelopoulos, Brockmeier, Mu & Goulermas (2020). Circular object arrangement using spherical embeddings. Pattern Recognition 103:107192 | 10.1016/j.patcog.2019.107192 | OK | 球面嵌入圆形布局（跨域方法；M1 布局诊断可参考） | 否 |

## C. 层次 / 树感知 / 潜因子比较器（5 条）
| # | 条目（Crossref 书目） | DOI | 核 | 核心主张 / 本篇角色 | 用 TLI·GBI·WALS |
|---|---|---|---|---|---|
| C1 | Jäger & Wahle (2021). Phylogenetic Typology. Front. Psychol. 12 | 10.3389/fpsyg.2021.682132 | OK | 系统发育类型学（遗传 vs 扩散信号分解；M3 层次比较器理论依据） | WALS + 自采 |
| C2 | Murawaki (2015). Continuous Space Representations of Linguistic Typology and their Application to Phylogene…（行内截断）. NAACL HLT 2015 | 10.3115/v1/n15-1036 | OK | 类型学连续空间表征 + 系统发育应用（MDS 潜因子比较器先例） | 否 |
| C3 | Neureiter, Ranacher, Efrat-Kowalsky, Kaiping, Weibel & Widmer (2022). Detecting Contact In Language Trees: A Bayesian Phylogenetic Model With Horizontal Transfe…（行内截断；Crossref 载体空，Research Square 预印本） | 10.21203/rs.3.rs-1262191/v1 | OK | 语言树接触检测（贝叶斯系统发育 + 水平转移） | 否 |
| C4 | Verkerk, Shcherbakova, Haynie, Skirgård, Rzymski & Atkinson (2025). Enduring constraints on grammar revealed by Bayesian spatiophylogenetic analyses. Nat. Hum. Behav. 10(1):126–136 | 10.1038/s41562-025-02325-z | OK | 时空系统发育语法约束（空间先验 → M5 先验解释检查对照先例） | 否（自有 + Glottolog 地理） |
| C5 | Bjerva, Kementchedjhieva, Cotterell & Augenstein (2019). A Probabilistic Generative Model of Linguistic Typology. NAACL HLT 2019 | 10.18653/v1/N19-1156 | OK | 类型学概率生成模型（潜因子比较器先例） | 否 |

## D. WALS 特征预测任务（L2 任务定义与基线参照，3 条）
| # | 条目（Crossref 书目） | DOI | 核 | 核心主张 / 本篇角色 | 用 TLI·GBI·WALS |
|---|---|---|---|---|---|
| D1 | Bjerva, Salesky, Mielke, Chaudhary, Celano & Ponti (2020). SIGTYP 2020 Shared Task: Prediction of Typological Features. Proc. SIGTYP 2020 | 10.18653/v1/2020.sigtyp-1.1 | OK | WALS 特征预测共享任务（留出/评估协议参照） | WALS |
| D2 | Vastl, Zeman & Rosa (2020). Predicting Typological Features in WALS using Language Embeddings and Conditional Probabil…（行内截断）. Proc. SIGTYP 2020 | 10.18653/v1/2020.sigtyp-1.4 | OK | 嵌入 + 条件概率预测（非圆形强基线参照） | WALS |
| D3 | Gutkin & Sproat (2020). NEMO: Frequentist Inference Approach to Constrained Linguistic Typology Feature Prediction. Proc. SIGTYP 2020 | 10.18653/v1/2020.sigtyp-1.3 | OK | 约束特征预测频率推断 | WALS |

## E. 数据层描述文献（5 条）
| # | 条目 | DOI | 核 | 核心主张 / 本篇角色 | 用 TLI·GBI·WALS |
|---|---|---|---|---|---|
| E1 | Graff, Chousou-Polydouri, Inman, Skirgård, Lischka & Zakharko (2025). Curating global datasets of structural linguistic features for independence. Sci. Data 12 (2025-01-18) | 10.1038/s41597-024-04319-4 | OK | **TLI/GBI 数据层来源论文**：自 5 个已发表库策展出 GBI（Grambank 源）与 TLI（输入 = WALS + AUTOTYP + PHOIBLE + Lexibank）两全球数据集；最小化特征逻辑依赖与强统计依赖；densified 形式降缺失（摘要已核，本周期 Crossref 返回） | TLI+GBI |
| E2 | Skirgård, Haynie, Blasi, Hammarström, Collins & Latarche (2023). Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss. Sci. Adv. 9(16) | 10.1126/sciadv.adg6175 | OK | **GBI 特征体系来源**（Grambank） | GBI 源 |
| E3 | Dryer & Haspelmath (eds.) (2013). The World Atlas of Language Structures Online. Leipzig: Max Planck Institute for Evolutionary Anthropology. wals.info. CC-BY-4.0 | 无 | 本地元数据 | WALS 数据层（本地 `data/raw/wals/metadata.json` 书目；接力 2 补核 3 条命中均为书评：Hoffmann 2009 Kratylos / Schulze 2007 StL / Bright 2007 IJAL，原书无 DOI） | WALS |
| E4 | Hammarström, Forkel, Haspelmath & Bank (2025). Glottolog 5.2.1. Leipzig: Max Planck Institute for Evolutionary Anthropology. glottolog.org. CC-BY-4.0 | 无 | 本地元数据 | 语系标签 + 系统发育 + 地理（本地 `data/raw/glottolog/cldf-metadata.json` bibliographicCitation 定版 5.2.1） | 语系标签 |
| E5 | Forkel, List, Greenhill et al. (2018). Cross-Linguistic Data Formats, advancing data sharing and re-use in comparative linguistics. Sci. Data 5:180058 | 10.1038/sdata.2018.205 | OK（接力 2 补核） | CLDF 数据基础设施（三数据层元数据格式）；crossref_check.txt 未含此条，核验见 lit_takeover2_check.txt「glottolog」组 | 基础设施 |

## F. 跨域误命中（仅记录，不入引用宇宙，支撑 §0）
- 'periodic' 命中 4 条：Omairey et al. 2019 ABAQUS RVE 周期均质化（10.1007/s00366-018-0616-4，OK）/ Andino-Enríquez et al. 2022 基切语化学元素周期表教学（10.1021/acs.jchemed.1c00383，OK）/ Wu et al. 2016 MetaCycle 周期性评估 R 包（10.1093/bioinformatics/btw405，OK）/ Mannige & Brooks 2010 病毒衣壳周期表（10.1371/journal.pone.0009423，OK）。
- 几何/圆形词法误命中：Tucker 1970/1971 circular-arc 图论、Isayev et al. 2017 晶体描述符（10.1038/ncomms15679）、Mendoza et al. 2019 循环经济、Chapman et al. 2023 环状 DNA 等（候选表内，crf 状态见 crossref_check.txt）。

## 覆盖下限核对（stage1_prompt B 组四条）
1. 圆形/周期表假设来源 → §0 阴性发现（域内无索引来源，如实登记）+ §B 最近邻 ✔
2. circular seriation 方法 → §A 8 条（最优算法 ×2 / 谱与 QAP / 起源 A8）✔
3. 层次/潜因子比较器 → §C 5 条 ✔
4. TLI/GBI/WALS 数据层描述文献 → §E 5 条（TLI/GBI 来源论文 E1 已定位并核摘要；WALS/Glottolog 本地元数据定版）✔

## 冻结声明
- 本表 **29 条登记**（A8+B8+C5+D3+E5=29；§F 误命中不计入）。
- **26/29 条 Crossref 核验 OK**（25 条见 crossref_check.txt，E5 见 lit_takeover2_check.txt 补核）；3 条无 DOI（A8 补核未命中按二手引文 / E3、E4 本地数据层元数据书目）。
- 引用纪律：段2–5 只可引用本表条目 + 数据层本地元数据；**不新增未核引用**（001 段4 同款教训：Crossref 未核条目不得入稿）。
- 残标=0；数字/DOI/年份逐字取自 crossref_check.txt / lit_takeover2_check.txt / 本地元数据，无改写。
