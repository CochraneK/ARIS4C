# DATA_PROFILE — ARIS4C-005 stage2（fix，2026-10-08）
快照 2026-10-08 · 来源：T1 RW 官方 CSV（在盘）+ T2 E1 映射（在盘）+ T3 分母 probe（本 run）+ T4 RePORTER 重试（本 run）+ stage1 S3 沿用
纪律：零 outcome（不算率、不跑模型）；撤稿≠造假；notice≠裁定

## #1 RW 官方 CSV（取代 stage1 损坏网页-CSV）
- 来源：data/raw/rw_official/retraction_watch.csv（67,038,098B，2026-09-29 生成，官方 gitlab.com/crossref/retraction-watch-data raw）
- 四类 notice + Revision 膨胀口径注记：CSV 含多类 notice，Retraction 为真撤稿类；Revision 等 notice 会膨胀行数，计数须按类型过滤
- 状态：PASS（取代 stage1 的 1,391 行网页-CSV——后者无日期/reason-code 字段，曾降 CAUTION）
- 局限：撤稿≠造假；notice 级 reason code ≠ 裁定级结论

## #2 E1 三桶映射（E1 计数口径）
- 来源：data/rw_e1_mapping.csv（5,457B，E1 = confirmed severe integrity failure）
- 三桶映射：reason code → 三桶（仅列映射，不算率）
- 声明：notice≠裁定（映射仅定计数口径，不构成造假认定）
- 状态：PASS

## #3 OpenAlex 分母 probe（P1–P4，2026 API 单年验证，本 run）
- P1 publication_year:2015 = 10,220,607
- P2 publication_year:2020 = 11,592,932
- P3 publication_date:2000-01-01-2025-12-31 = ERROR 400（日期区间 filter 不可用，记 limitation）
- P4 publication_year:2000-2025 = 222,714,158（正典分母）
- 判定：P1≠P2 且均远小于 P4 → 单年过滤正常、无退化；P4 vs 09-30 实测 220,028,794 = +2.7M（8 天正常漂移，非退化）
- 正典分母：**222,714,158**（2000–2025，publication_year 口径）
- 局限：P3 publication_date 区间 400 不可用；meta.count 秒级漂移，段3 物化时重新固定（记录当时值）

## #4 RePORTER（模块 D 归属，本 run T4 重试）
- Probe：api.reporter.nih.gov/v2/awards（verify=False，placeholder key）→ **HTTP 404**
- 结论：CAUTION — RePORTER 不可达（404/需 key），模块 D（受援机构归属）BLOCKED，需申请 API key
- 局限：404 可能为端点路径变更或无 key 阻断；不影响主线 A/B/C

## #5 模块 B pilot 字段覆盖（stage1 S3 沿用）
- 200 篇样本：doi 192/200 · cited_by_count 200/200 · abstract 155/200 · concepts 200/200 · pl_source_display_name 169/200
- CAUTION：retraction 字段 list-query 缺失（filter retracted:true→400；select retracted→400，2026-09 schema）
- 绕行：撤稿判定 = 官方 RW CSV 本地 doi 集合 ∩ 宇宙 doi；个别核验走 per-id detail 查询（doi 覆盖 96%）

## #6 模块 C 引用上下文字段（stage1 S3 沿用）
- 200 篇样本：list-query 不返回 cites（cites_key 0/200），但 ids 可在响应内获得
- 绕行：per-page=200 分页收集 ids → 第二批量 works?ids=…&select=concepts,abstract（限速+backoff）取上下文分类特征

## #7 Gate 1–5 段2 判定
- Gate 1 宇宙/分母：PASS — 正典分母 222,714,158（P4，过滤未退化）
- Gate 2 E1 计数口径：PASS — RW 官方 CSV + E1 三桶映射在盘（不算率，零 outcome）
- Gate 3 模块 B 字段：PASS（caution）— retraction 字段缺失，绕行方案就位
- Gate 4 模块 C 引用：PASS（caution）— 第二批量查询绕行方案就位
- Gate 5 模块 D 归属：BLOCKED（RePORTER 404/需 key）
