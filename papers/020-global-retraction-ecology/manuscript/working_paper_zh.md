# 全球科学撤稿生态
## 事件—作品重建、Reason 生态、撤稿时序与引用余生

**ARIS4C-020 · 中文工作稿 · confirmatory analysis 前版本 · 2026-09-24**

### 摘要

既有撤稿研究常用国家、期刊、出版商或撤稿原因的绝对数量进行描述，但这些数量同时受到论文产量、学科构成、问题发现机制、出版商清理政策、大规模撤稿事件以及论文获得“被撤稿机会”的时间影响。本研究建立一个全学科、可复现的分析框架：以 Retraction Watch 全量数据作为撤稿事件主表，以 Crossref/OpenAlex 补充作品元数据、论文母体分母和引用网络。2026-09-23 快照共 72,606 条记录，其中 67,197 条为 Retraction；可获得 61,155 个唯一且可用的原论文 DOI。发表至撤稿的中位时滞为 490 天（1.34 年；P25=153，P75=1,061）。撤稿 Reason 呈显著多标签结构，平均每条 Retraction 含 3.96 个 Reason。确定性的 OpenAlex 1,000 DOI pilot 匹配 996 条（99.6%），首个全量分片匹配 15,146/15,255（99.29%），无 API 错误。当前结果证明“事件→作品”重建与跨库 enrichment 管线可行，但国家/学科/出版商风险比较仍锁定，直至完整 DOI 匹配、论文母体分母、右删失规则、Reason ontology 审查、mass-event 敏感性和 work-type 一致性门全部通过。

### 与最接近研究的边界

2026 年 Venturini、Urbinati 与 Gallo 的预印本 *The Retraction Epidemic in Science Across Publishers, Fields, and Countries* 已经使用超过 1.07 亿条 OpenAlex works，对 1992–2021 发表 cohort 进行每论文/每作者撤稿 incidence、学科/国家/出版商比较、fractional country weighting、负二项 exposure model、撤稿时滞和集中度/Gini 分析。Oppenlaender（2026）也已对十大出版商的撤稿率、原因、时间与地域模式进行分析。

因此，020 **不再把“全球分母校正”“国家/学科/出版商撤稿率”“研究撤稿时滞”单独作为创新点**。020 必须向更深一层推进：

- 直接以完整 RWDB 事件表定义撤稿总体，而不是以 OpenAlex `is_retracted` 标记定义病例；
- 将重复 notice/event 追溯并合并为唯一 scholarly work；
- 显式报告 RWDB × OpenAlex 的误标、漏标、一 DOI 多 Work candidate；
- 保留 110 个实际观察 Reason 的多标签共现结构，并做正交 facet；
- 对 paper mill / publisher cleanup / mass-retraction cluster 做 leave-cluster-out 敏感性；
- 建立真正包含未撤稿论文右删失的 time-to-event 分析，而非只通过截断近期 cohort 处理；
- 在同一 work spine 上分析撤稿后的 citation afterlife。

### 一、核心研究问题

本研究不问“谁撤稿最多”这么简单的问题，而区分：

1. RWDB 实际记录了多少撤稿事件？
2. 在相同论文产量与发表 cohort 下，撤稿率如何变化？
3. 从发表到撤稿需要多久，这一时滞如何随学科、时代和 Reason 变化？
4. 多个 Reason 如何共现，哪些是内容问题、哪些是调查流程或 notice 状态？
5. 2023 等年份的高峰有多少来自 paper mill / 批量清理事件？
6. 撤稿之后，论文还会持续获得多少引用？

### 二、数据与单位

主事件总体固定为 `RetractionNature == Retraction`。EOC、Correction 和 Reinstatement 单独保留，但不进入主撤稿率分子。

数据库同时维护：

- **事件表**：以 RWDB Record ID 为主键；
- **作品表**：优先以规范化 OriginalPaperDOI 为主键，缺 DOI 时再使用 PMID。

因此，同一原论文存在多条撤稿记录时，在“撤稿事件”分析中全部保留，在“论文撤稿率”分析中只计为一个作品。

### 三、初步数据审计

2026-09-23 快照：

- 全部记录：72,606
- Retraction：67,197
- EOC：3,719
- Correction：1,530
- Reinstatement：160
- 有可用原论文 DOI 的 Retraction：61,316
- 唯一原论文 DOI：61,155
- RWDB Reason 原子标签：110 个

### 四、撤稿时滞

所有 67,197 条 Retraction 的发表日期和撤稿日期均可按当前格式解析，未发现负时滞。

- P10：38 天
- P25：153 天
- 中位数：**490 天**
- P75：1,061 天
- P90：2,194 天

这说明近期发表论文天然缺少“被撤稿的观察时间”，因此不能直接把 2024/2025 cohort 与十年前的论文做朴素撤稿率比较。

### 五、Reason 的正交表示

不建立一个强制互斥的“唯一撤稿原因”。

保留官方原子标签，并附加六个可并存 facet：

1. 受影响对象：data / image / results / text / methods / authorship / peer review 等；
2. 失效机制：error / unreliable / duplication / plagiarism / fabrication / manipulation / paper mill / generated content 等；
3. 伦理与合规；
4. 调查/流程角色；
5. notice / lifecycle 状态；
6. 证据具体度。

这样可以避免把 “Investigation by Journal/Publisher” 和 “Error in Data” 当成同一逻辑层级的原因。

### 六、当前结果

2023 年记录到 13,227 条 Retraction，是 2022 年 5,591 条的 2.37 倍，也是 2024 年 6,383 条的 2.07 倍。该高峰目前仅视为“数据库中的撤稿事件高峰”，不能先解释为科研不端突然翻倍。

Reason 平均每条 Retraction 有 **3.96 个标签**。因此所有 Reason 百分比允许总和超过 100%。

OpenAlex 连接测试：

- 固定 SHA-256 抽样 1,000 DOI：996/1,000 = **99.6%**
- 全量 shard 0：15,146/15,255 = **99.2855%**
- API error：0

### 七、明确禁止的早期解释

在 denominator gate 完成之前，不允许把：

- 中国撤稿绝对数量高 → 解释为中国撤稿风险高；
- 某出版社撤稿数量高 → 解释为其质量更差；
- 2023 高峰 → 解释为科研不端发生率突然增加；
- affiliation → 解释为责任主体；
- citation → 解释为引用者认可撤稿论文；
- Reason label → 自动解释为作者故意不端。

### 八、下一门

1. 完成 OpenAlex 剩余三个 DOI 分片。
2. 冻结 OpenAlex eligible work types。
3. 构建 year × field 论文分母。
4. 完成 110-label Reason facet 全映射并人工审查。
5. 识别 mass-retraction/paper-mill 集中事件。
6. 冻结 mature cohort / right censoring 规则。
7. 构建撤稿论文的匹配非撤稿对照。
8. 解锁正式比较性 Results。
