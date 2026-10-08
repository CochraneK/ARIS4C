# stage1_summary — ARIS4C-005（fix3 最小修复）
日期 2026-09-30 · 依据：在盘 s3_fix_results.json + lit/REGISTRY.md + 本地 RW 核查 + 新查询 2（Q1/Q2）· 未重下载、未重检索

## S1 冻结设计确认（复述）
- E1/E2/E3 三层范围不得混用；主时间宇宙 2000–2025
- 七条禁令（撤稿≠造假 等）；冻结损失本体 5 类；冻结新概念 11 个（先校准再使用）
- 六模块 A–F 架构；Gate 1–5；人工审计 6 级裁决；模块 B 主模型=分层贝叶斯二元潜类
- Non-Goals：不做国家排名、不追求单一总账、不生成具名清单；fix3 未新增假设或模块（仅文档级修复）

## 文献概况（S2/S4）
- REGISTRY 35 条，VERIFIED 35/35（Crossref DOI 核对），5 方向各 ≥5；d5 因同名词污染 curated 7 条
- 关键发现：(1) 患病率估计依方法差异巨大（d1）(2) 撤稿≠造假、reason coding 不一致（d2）(3) 引用上下文类型学可复用（d3）(4) LCMCR/MSE 成熟但无 misconduct 患病率先例（d4）(5) 成本估计皆个案/专家级（d5）

## 数据可行性 6 项 verdict（S3）
1. 宇宙分母：PASS — Q1 meta.count=220028794（2000–2025，快照 2026-09-30）
2. RW 源：CAUTION — 在盘 rw_retractions.csv 实为 retractionwatch.com 网页保存件（非结构化 CSV）；段2 重取官方 CSV 后列 E1 映射（只列映射）
3. 模块 B 字段：CAUTION — doi 192/200、abstract 155/200；retraction 字段 list-query 缺失（filter 400 / 覆盖 0）
4. 模块 D RePORTER：CAUTION — probe ERR，见响应摘录
5. 模块 C 引用字段：CAUTION — list-query 无 cites，需按 ids 第二批量查询（绕行方案就位）
6. Gate 可判性：Gate 1 可初判；2 部分可判；3/4 可初判（caution）；5 CAUTION（需 key）

## Gate 初判
- Gate 1 初判通过（分母+宇宙在盘）· Gate 2 待段2（RW 重取+口径定稿）
- Gate 3 待段2（RW doi 集物化）· Gate 4 待段2（第二批量查询）· Gate 5 CAUTION（需 key）

## 总体 verdict
GO-with-caution — 三项 caution：(a) retraction 字段 list-query 缺失（filter 400 / 覆盖 0）(b) cites 需 ids 第二批量查询 (c) 在盘 RW CSV 损坏（实为 HTML 网页件）；三项均有段2 绕行方案（per-id 查询 / ids 第二查询 / 重取官方 CSV），其余各项有在盘证据；全程零 outcome（未算任何率、未跑模型）

DONE stage1fix3 005
