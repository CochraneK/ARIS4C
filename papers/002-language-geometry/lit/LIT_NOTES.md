# LIT_NOTES.md — 文献汇编（ARIS4C-002 段1 · 与 REGISTRY 同步冻结）

> 冻结：2026-09-27 00:0x · 驱动器段1 接管直写补完（第 10 次接管·接力 6，未重跑 LLM）；与 REGISTRY（冻结件 2a，2026-09-26 22:2x 接力 3）同步冻结。
> 29 条 = REGISTRY 登记 29 条（A8+B8+C5+D3+E5；§F 跨域误命中不入引用宇宙）；无登记表外条目。编号沿用 REGISTRY。
> 核实来源：`results/crossref_check.txt`（executor 16:32，179 行：157 OK / 9 无 DOI / 13 FAIL:404；DOI 大小写重复行在候选表已去重，两文件计数口径差 9）+ `results/lit_takeover2_check.txt`（接力 2 22:06 补核，4 组）。书目字段一律以 Crossref 返回为准（REGISTRY 逐字摘取）。
> 每条一句话相关性；书目细节以 REGISTRY 为准。

## §A 圆形序贯方法（8 条）
- **A1** Armstrong, Guzmán & Sing Long 2021（SIAM J. Math. Data Sci.）— 严格圆形序贯最优算法（精确解基准）；本篇 n≤3573 下 O(n³) 不可行 → RESEARCH_PLAN §2.1 预注册局部搜索（2-opt+随机重启 seed=42×3）。
- **A2** Carmona, Chepoi, Naves & Préat 2023（SIAM J. Math. Data Sci.）— 简单最优严格圆形序贯算法（段2/3 实现参照）；arXiv:2205.04694 重复条目 FAIL:404 不登记。
- **A3** Laporte 1978（J. Comput. Appl. Math.）— 序贯问题与 TSP 关联（Robinson 距离序贯的理论基础）。
- **A4** Concas, Fenu, Rodriguez & Vandebril 2023（Numer. Algorithms）— 谱方法序贯在双 Fiedler 值下的适用边界（M1 布局谱诊断参照）。
- **A5** Hubert 1974（Br. J. Math. Stat. Psychol.）— 图论/非度量技术的近似序贯应用（方法先例；Crossref 题名行内截断，照抄存目）。
- **A6** Hubert & Schultz 1976（Br. J. Math. Stat. Psychol.）— QAP 通用数据分析策略（序贯/布局问题统一视角）。
- **A7** Weber 1978（BHL, 10.5962/bhl.title.5189）— 考古学序贯应用（方法外推先例）。
- **A8** Gower & Rossman 1969 — 圆形序贯统计方法出处（RESEARCH_PLAN §2.1）；**无 DOI**，接力 2 补核未返回 1969 对应条目（仅 2002 书章×2 + Multiobjective Seriation 3 条相关）→ 按二手引文登记，题名/载体不补造。

## §B 全局结构 / 几何 / 对称性（8 条）
- **B1** Kemp 2026（Nat. Commun.）— 跨语言范畴系统对称性（**域内与「全局结构」主张最近邻**；自有语料，未用三层）。
- **B2** Evans & Levinson 2009（BBS 32(5)）— 语言多样性挑战普遍语假说（H3 跨层稳健性 + claims 纪律背景；引 WALS 前版作背景）。
- **B3** Piantadosi & Gibson 2014（Cogn. Sci. 38(4)，Crossref 卷年 2014/候选表 OpenAlex 年 2013）— 绝对普遍语的定量频率标准（段2 边际基线判据背景；WALS 前版）。
- **B4** Levinson & Meira 2003（Language）— 空间拓扑概念自然性（几何语言论先例；Crossref 作者列表 2 名+空位、题名行内截断，照抄存目）。
- **B5** Amalric et al. 2017（PLOS Comput. Biol.）— 人类几何基元/规则快速习得（几何表征背景，非类型学）。
- **B6** Port et al. 2018（Math. Comput. Sci.）— 句法持续同调（语言结构拓扑度量先例）。
- **B7** Port, Karidi & Marcolli 2022（Math. Comput. Sci.）— 句法结构拓扑分析（B6 同脉络）。
- **B8** Evangelopoulos et al. 2020（Pattern Recognition 103:107192）— 球面嵌入圆形布局（跨域方法；M1 布局诊断可参考）。

## §C 层次 / 树感知 / 潜因子比较器（5 条）
- **C1** Jäger & Wahle 2021（Front. Psychol. 12）— 系统发育类型学（遗传 vs 扩散信号分解；M3 层次比较器理论依据；WALS+自采）。
- **C2** Murawaki 2015（NAACL HLT）— 类型学连续空间表征+系统发育应用（MDS 潜因子比较器先例；题名行内截断）。
- **C3** Neureiter et al. 2022（Research Square 预印本）— 语言树接触检测（贝叶斯系统发育+水平转移；题名行内截断、Crossref 载体空）。
- **C4** Verkerk et al. 2025（Nat. Hum. Behav. 10(1):126–136）— 时空系统发育语法约束（空间先验 → M5 先验解释检查对照先例；自有+Glottolog 地理）。
- **C5** Bjerva et al. 2019（NAACL HLT）— 类型学概率生成模型（潜因子比较器先例）。

## §D WALS 特征预测任务（3 条）
- **D1** Bjerva et al. 2020（SIGTYP 2020 共享任务）— WALS 特征预测共享任务（留出/评估协议参照；WALS）。
- **D2** Vastl, Zeman & Rosa 2020（SIGTYP 2020）— 嵌入+条件概率预测（非圆形强基线参照；题名行内截断；WALS）。
- **D3** Gutkin & Sproat 2020（SIGTYP 2020, NEMO）— 约束特征预测频率推断（WALS）。

## §E 数据层描述文献（5 条）
- **E1** Graff et al. 2025（Sci. Data 12, 10.1038/s41597-024-04319-4）— **TLI/GBI 数据层来源论文**：自 5 个已发表库策展 GBI（Grambank 源）与 TLI（输入=WALS+AUTOTYP+PHOIBLE+Lexibank）；最小化特征逻辑/强统计依赖；densified 形式降缺失（摘要已核，本 run Crossref 返回）。
- **E2** Skirgård et al. 2023（Sci. Adv. 9(16)）— **GBI 特征体系来源**（Grambank）。
- **E3** Dryer & Haspelmath (eds.) 2013（WALS Online, wals.info, CC-BY-4.0）— WALS 数据层（本地 `data/raw/wals/metadata.json` 书目；原书无 DOI，接力 2 补核 3 条命中均为书评：Hoffmann 2009 / Schulze 2007 / Bright 2007）。
- **E4** Hammarström et al. 2025（Glottolog 5.2.1, glottolog.org, CC-BY-4.0）— 语系标签+系统发育+地理（本地 `data/raw/glottolog/cldf-metadata.json` bibliographicCitation 定版 5.2.1）。
- **E5** Forkel et al. 2018（Sci. Data 5:180058, 10.1038/sdata.2018.205）— CLDF 数据基础设施（三数据层元数据格式；crossref_check.txt 未含此条，接力 2 补核 OK）。

## 核实状态
- 29 条：**26/29 条 Crossref 核验 OK**（25 条见 crossref_check.txt，E5 见 lit_takeover2_check.txt 补核）；3 条无 DOI（A8 补核未命中按二手引文 / E3、E4 本地数据层元数据书目），无编造补全。
- 候选池口径：188 条唯一候选（raw 279 → 去重 179 + anchor 9）；crossref_check 179 行 = 157 OK / 9 无 DOI / 13 FAIL:404；登记表按 REGISTRY「覆盖下限核对」四条自 OK 集+本地元数据集选取，DOI 大小写重复行已去重。
- **阴性发现（REGISTRY §0，逐字入终稿 provenance）**：「语言元素周期表」假设在 OpenAlex 无域内索引来源（7 轮检索 'periodic' 命中 4 条全跨域）；假设入口 = `RESEARCH_BRIEF.md`（受检主张），域内最近邻 = B1–B4；不编造假设来源。
- 引用纪律：段2–5 只可引用本表 29 条 + 数据层本地元数据（E1–E5 所钉版本地文件）；新增引用须补 Crossref 核并追加「段2 增补」小节（001 段4 同款教训：Crossref 未核条目不得入稿）。
- 冻结：随 REGISTRY 冻结（冻结件 2b）；残标=0（本件 CHUNK/ZCHUNK 扫描=0）。
