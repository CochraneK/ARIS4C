# DATA_PROFILE — ARIS4C-007 stage 1 可行性核查
日期 2026-09-29。仅测可得性/量级；未复现任何映射、未拟合参数、未下载全量数据。
本网络为白名单代理：Crossref/EPMC/bioRxiv/nature.com 可达；genomics.senescence.info(AnAge) 502 不可达。

## 1. AnAge（表 A 基础）
- 公开入口: https://genomics.senescence.info/species/index.html（由 crofts2023 数据可用性段确认）；anagedb.org 为前端。
- 快照: 快照当日站点自本网络 502 不可达 → **无法当日冻结版本**；stage 2 需换网络或改走代理。
- 量级（据 lu2023 全文）: AnAge 中 969 个哺乳物种有 妊娠期+性成熟年龄(ASM)+最大寿命 三字段；其亚集 339 物种有甲基化数据。
- 字段结构: 最大寿命有证据质量/记录来源字段（lu2023 指出"许多物种最大寿命知识不准确"，故用 1.3× 校正并另设 Clock 3）；圈养/野生来源字段存在（具体 schema 待 stage 2 取数确认）。
- verdict: 可得（经文献内描述）但**当日无法直接取快照** → 缓解: 用 lu2023/crofts2023 补充材料中 clock-era AnAge 表（brief 稳健性项本身要求 clock-era 快照）。

## 2. Translating Time（A4）
- 方法原文: januel2026（预印 10.1101/2025.07.31.667772；Biology Open 2026, 10.1242/bio.062604），Gibson/Charvet 系。方法全文自含: 事件选点(≥2 物种共有)→Amelia 插补 n=10→PCA 降噪→事件尺度(0–1 归一)→自然样条加权拟合。
- 数据: 事件表由所引文献汇编（AD 神经病理年龄 de Sousa 2023、血液 91 项检验/47 猫→78 项/45 猫、脑结构指标）；正文无独立 Data availability 段；补充材料文件未在本快照 HTML 中列出（bioRxiv 页面可达，stage 2 可直接取补充文件）。
- 覆盖物种: 人、猫（宠物/ colony/野生 3 群）、黑猩猩、小鼠（4 物种）。事件数: 数十量级（Fig.1 事件轴 ~10+ 时间点，血液 78 项指标为连续测量）。
- 复现子集可行性: 高——方法逐步可执行；原始事件表需从补充材料/所引文献重建。

## 3. 已发表 A6 时钟（候选 ≥3，含泛哺乳动物）
- (a) lu2023: 3 个 universal 时钟（Clock1/2 基于 L_max；Clock3="universal log-linear age" 用 ASM+妊娠期，不依赖 L_max；log 尺度解释 >69% L_max 变异）；339 物种/11,754 样本；数据 GSE223748(全量)+~20 子集 GSE；阵列 manifest+CpG 注释 Zenodo 10.5281/zenodo.7574747；阵列经 Epigenetic Clock Development Foundation (clockfoundation.org) 提供。**时钟权重公开性: 补充材料/代码需 stage 2 确认**。
- (b) panmam2023 (10.1038/s43587-023-00463-5): 泛哺乳动物甲基化时钟（与 lu2023 同刊同卷；作者元数据缺失待核）；数据应同 Consortium 系，需 stage 2 核 DAV 段。
- (c) crofts2023: 非时钟但速率标度分析，代码公开 github.com/elc08/meth_scaling_law（Python 3.11.4），数据 GSE223748+GSE136296(黑猩猩)——可作为 A6 对照基准。
- (d) 人类参考时钟（时间年龄 vs 生物年龄区分的锚点）: horvath2013（时间年龄）、belsky2021 DunedinPACE（速率/生物年龄）、levine2018 GrimAge（死亡风险/生物年龄）。
- 输入平台: Mammalian Methylation Consortium 自定义阵列（非 450K/EPIC 直接兼容，需 manifest 映射）；人类时钟用 450K/EPIC。
- verdict: 可得（GEO/Zenodo/ClockFoundation 均在公共域；GEO 可达性 stage 2 验证；全量 GSE223748 体积可能 GB 级，建议先取子集 GSE174758/GSE184211 等验证管线）。

## 4. 表 C 人口学曲线（候选源，未下载）
- 人类: Human Mortality Database (mortality.org)——高质量年龄别死亡率，首选。
- 小鼠: 发表队列研究（如 GSE223748 所含实验室队列有年龄+死亡信息可重建）；标准品系曲线发表文献。
- 犬: 兽医队列/衰弱研究（januel2026 所用 45 猫+犬队列文献；犬健康/衰弱子集对应 Tier 4）。
- 野生种群: 逐物种发表种群研究（灵长类、蝙蝠等），质量参差；AnAge 本身以最大寿命记录为主，不含系统生存曲线。
- verdict: 仅约 2–4 物种（人、小鼠、犬、或灵长类）有可重建曲线 → A5 天然窄覆盖（与冻结设计"有充分死亡信息的物种"一致）。

## 5. 表 A/B/E 构造量级
- 表 A: A0–A3 合格物种 ≈ AnAge 三字段齐全者（lu2023: 969 哺乳物种，其中 185 物种在 Consortium 有年龄数据）；完整网格物种（A0–A6 全层）= 4–10（人/鼠/猫/黑猩猩为核心）。
- 表 B: 4 物种 × 数十事件（TT 汇编）+ AnAge 生活史锚点（受孕/出生/成熟）→ 约 100–300 行。
- 表 E: 评估点 = 预指定标准化年龄分位数（如 0–1 共 11 点）× 物种（10–100）× 7 映射 → 约 700–7,000 行；A6 列仅在 339 物种 ∩ 平台映射物种上非空。

## 6. Step 1–5 阻塞点初判
- Step 1 (A0–A3): **最大风险 = AnAge 快照不可达（502）**。缓解: lu2023/crofts2023 补充材料内嵌 AnAge 表（clock-era，恰好是 brief 稳健性项要求的版本）；若补充材料无全表，需 stage 2 换网络出口。
- Step 2 (A4): 事件表在补充材料/所引文献，bioRxiv 可达 → 阻塞小。
- Step 3 (A5): 曲线覆盖窄（2–4 物种）→ 不阻塞但范围受限。
- Step 4 (A6): GSE223748 体积+GEO 可达性待验；时钟权重公开性待确认 → 中等风险。
- Step 5: 依赖前四步，无独立阻塞。
- 未决识别项: **Animal-Age 基线模型**在 Crossref/EPMC 均无记录（疑为未索引预印本/软件包）→ stage 2 再查；兜底 = 直接按冻结 A2 定义用表 B 锚点自建分段映射。
