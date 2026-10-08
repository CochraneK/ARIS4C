# stage1_summary — ARIS4C-007（2026-09-29）
运行: ARIS4C-007 重跑 stage 1 | executor 模型 Deepseek-Flash-V4-正式版 | 工具调用 35 内 | 零 outcome 计算（未复现任何 A0–A6 映射、未拟合参数）。

## S1 冻结设计确认（复述）
- 本体 A0–A6: A0 朴素寿命比 / A1 最大寿命相对 / A2 生活史锚点（Animal-Age 为基线）/ A3 log-linear（Lu et al.）/ A4 Translating Time 事件尺度 / A5 生存等价 / A6 分子-表观遗传时钟。
- 主假设方向=跨阶段非一致性（H1），不预设哪种映射更好；H1–H5 全冻结，未新增假设。
- A6 关键区分: 时间年龄时钟 vs 生物年龄时钟，不得混用（文献锚点: horvath2013 vs belsky2021/levine2018）。
- 验证 Tier 1–4（无单一金标准，报告层间一致性，不压成单一分数）。
- 数据架构 5 张表 A–E；输出=区间/分布，不是单一数字。
- 稳健性/证伪最小集 12 项（含 1.3× 校正、圈养 vs 野生、leave-one-order-out）。
- Non-Goals: 不在结果感知参数拟合后再报告 A0–A3。

## 文献概况（REGISTRY: 25 条 / VERIFIED 21；渠道 Crossref+EPMC+bioRxiv，OpenAlex 当日免费预算耗尽未用）
1. **A3 主对象确认**: Lu et al. 2023 "Universal DNA methylation age across mammalian tissues" (Nat Aging, 10.1038/s43587-023-00462-6)；1.3× 校正原文定位（非人/非鼠 L_max ×1.3）；Clock 3=log-linear age 用 ASM+妊娠期。
2. **A4 主对象确认**: Januel et al.（Gibson/Charvet 系）2025 预印/2026 Biology Open "Cat brains age like humans: Translating Time..."；方法自含（事件尺度+样条），4 物种（人/猫/黑猩猩/小鼠）。
3. **A6 候选**: lu2023（3 universal 时钟, GSE223748, Zenodo manifest）、panmam2023（10.1038/s43587-023-00463-5, 作者元数据待核）、crofts2023（代码公开）、horvath2013/belsky2021/levine2018（人类参考时钟）。
4. **分歧性结论**: lu2023（universal 不变）vs crofts2023（速率随 L_max 标度）同刊同年对立 → H1 的现成文献证据；TT 事件尺度 vs A0 线性在猫上机制分歧。
5. **缺口**: Animal-Age 基线在 Crossref/EPMC 无记录（stage 2 再查，兜底自建 A2 锚点映射）；A5 无已发表直接方法（= 本课题新坐标）；4 条 UNVERIFIED 已注明原因。

## 数据可行性（DATA_PROFILE 6 项 verdict）
1. AnAge: 可得性=文献内确认（969 物种三字段）；**站点快照日本站点 502 不可达** → 缓解: 用 lu2023/crofts2023 补充材料的 clock-era AnAge 表。
2. Translating Time: 方法全文自含、bioRxiv 可达、事件表在补充材料/所引文献 → **可行（高）**。
3. A6 时钟: ≥3 候选含泛哺乳动物；GEO/Zenodo/ClockFoundation 公共域；权重公开性+GEO 可达性 stage 2 验证 → **可行（中）**。
4. 表 C 曲线: 仅 2–4 物种（人/小鼠/犬/灵长类）有可重建公开曲线 → **可行但窄**（与冻结设计一致）。
5. 表 A/B/E 量级: 完整网格 4–10 物种；表 B ~100–300 行；表 E ~700–7,000 行 → **量级可控**。
6. Step 1–5 阻塞点: **Step 1 的 AnAge 快照 = 最大风险**（有缓解路径）；Step 2 阻塞小；Step 4 中等风险；Step 5 无独立阻塞。

## 总体 verdict: **GO-with-caution**
理由: 三大复现对象（A3 Lu2023、A4 Translating Time、A6 泛哺乳动物时钟）全部定位到公开数据源，复现路径明确；H1 已有文献级分歧证据，课题问题成立。Caution: (a) AnAge 站点自本网络不可达——stage 2 第一步必须落实快照来源（补充材料内嵌表或换网络出口）；(b) Animal-Age 基线未识别——需 stage 2 识别或启用兜底自建 A2；(c) panmam2023 作者元数据与 lu2023 时钟权重公开性待核；(d) A5 覆盖天然窄（2–4 物种），需在稿件中限定声明。
