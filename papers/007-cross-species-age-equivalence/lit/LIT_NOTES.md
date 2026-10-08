# LIT_NOTES — ARIS4C-007 stage 1（与冻结设计直接相关，按 5 检索方向）
日期 2026-09-29。渠道: Crossref/EPMC/bioRxiv（OpenAlex 预算耗尽未用）。条目引 REGISTRY citekey。

## D1 生活史理论与寿命标度
- 标度基础: west1997（allometric scaling 一般模型）、brown2019（metabolic theory of life history 延续）→ A0/A1 的体质量标度背景。
- austad1984/austad2007: 最大寿命演化——L_max 与体质量弱标度，长寿命/短寿命谱系系统偏离 → A1 的"最大寿命相对年龄"不是中性坐标；Austad 同时是 AnAge 相关数据传统（圈养-野生记录差异）的来源人物。
- stamps2005: pace-of-life 连续体 → H3 中"生活节奏"特征的文献基础（UNVERIFIED，stage 2 补核）。
- crofts2023: DNA 甲基化速率跨哺乳动物与 L_max 标度——分子层面的寿命标度检验；用 AnAge L_max；代码公开（github.com/elc08/meth_scaling_law）。
- 分歧点: crofts2023 强调"速率随寿命变化"，与 lu2023 的"universal（物种间不变）"主张构成同领域张力 → H1 方向的直接实证线索。

## D2 Translating Time / 事件尺度映射
- clancy2001: 跨哺乳动物发育时间翻译的先驱（脑发育 allometric translation）。
- charvetfinlay2018: 神经发生节奏跨物种翻译——事件尺度方法先例。
- charvet2025: "Translating time" 综述（challenges/progress/future）——框架级总结，事件式翻译的定位与争议。
- januel2026: **A4 复现主对象**（Gibson/Charvet 系）: TT 模型=事件选点(≥2 物种)→Amelia 插补→PCA→0–1 事件尺度→自然样条加权；物种=人/猫/黑猩猩/小鼠；核心结论: 猫脑老化轨迹与人对齐（16 岁猫≈80 多岁人类），猫为人类衰老自然模型。
- charvet2026ch: 事件尺度用于预测神经病理发生——TT 的应用延伸。
- 分歧性结论: TT（事件尺度）给出"猫≈人类八旬"，与朴素寿命比（猫 15 岁≈人类 ~70–90，A0）数值接近但机制不同；TT 覆盖发育+衰老全程，A0 仅线性——支持"映射族分歧"（H1/H2）。

## D3 跨物种/泛哺乳动物表观遗传时钟
- lu2023（**A3 公式 + A6 universal 时钟主对象**）: 3 个 universal 时钟；Clock 3 = "universal log-linear age"，用 ASM+妊娠期（不依赖 L_max；log 尺度解释 >69% L_max 变异）；**1.3× 校正原文: "We multiplied the reported maximum lifespan of non-human or non-mouse species by 1.3"**（= brief 稳健性项的出处）；339 物种/11,754 样本；数据 GSE223748 + 子集 GSE + Zenodo manifest (10.5281/zenodo.7574747)。
- panmam2023: 同刊同卷的泛哺乳动物甲基化时钟（evolutionarily conserved aging effects）；作者元数据在 Crossref/EPMC 缺失，Nature 页已存档待核。
- horvath2013: 人类时间年龄时钟（time-age 类锚点）。
- belsky2021: DunedinPACE——aging 速率（pace），生物年龄类锚点。
- levine2018: GrimAge——预测死亡风险的表观年龄（生物年龄类锚点）。
- altpage2022: 深度学习 pan-tissue 时钟（人类）；方法参照（rel 1）。
- 冻结区分落地: 时间年龄类=horvath2013/lu2023 universal 时钟；生物年龄类=belsky2021/levine2018；两者不得混用（A6 关键区分有明确文献锚点）。

## D4 生存等价/人口学年龄对齐
- medawar1952: 外源死亡率与衰老演化——生存等价（共享人口学位置）的理论起点。
- williams1957: 多效性选择与老年退化（senescence）——死亡率风险结构演化的经典。
- kirkwood1977: ageing 的"计划"论（资源分配权衡）——UNVERIFIED（Crossref 未核到 DOI），stage 2 补核。
- caswell2001: 矩阵种群模型——表 C（生存/死亡风险/余寿）构造的标准方法学。
- brockett2019: 死亡率/生存曲线的精算（数学）建模——A5 等生存概率变体的拟合方法参照。
- equisurv2020: 生存曲线建模与**等价性检验**（R 包）——A5 的统计等价性工具。
- 检索缺口: 未找到"跨物种 actuarial 年龄等价"的直接方法论文献 → A5 属方法组合（非复现已发表单方法），是本课题可贡献的新坐标（符合 H1 框架，不构成对冻结设计的偏离）。

## D5 universal scaling / universal clock
- lu2023: universal log-linear 变换主对象（见 D3）——A3 公式来源；1.3× 校正原文已定位（非人/非鼠 L_max ×1.3）。
- crofts2023: 甲基化速率 × L_max 标度（见 D1）——与 lu2023 同刊同年、主张相反（universal 不变 vs 寿命依赖标度）→ H1 分歧假设的现成文献证据。
- panmam2023: 泛哺乳动物时钟另一篇（见 D3）。
- moqri2022: "universal" 表观时钟（PRC2，人类为主）——对 "universal clock" 术语用法的一个对照（rel 1）。
- anage_data: A0–A3 的共同数据底座（969 哺乳物种三字段齐全，据 lu2023）；AnAge 无 DOI、快照日本站点 502 不可达（见 DATA_PROFILE）。
- 关键可复现性证据: lu2023 与 crofts2023 均公开数据（GSE223748 / GSE136296）且 crofts2023 公开代码 → A3 与 A6 的复现路径明确；A0–A3 所需生活史参数全部来自 AnAge 单源 → 单一数据源偏差风险需在稳健性套件中分层（brief 已含 AnAge 置信度分层项）。
