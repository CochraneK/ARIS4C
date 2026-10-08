# ARIS4C-005 stage3a summary — 模块 A 物化（核心描述性，可独立发表）
2026-10-08 | 输入=RESEARCH_BRIEF.md 冻结设计 | 零网络、无新增假设/模块/概念、段1/2 交付物未改动、RW CSV(67MB) 仅 python 解析
## T0 环境与完整性 — PASS：pandas 3.0.5 导入 OK；RW CSV SHA256=manifest ok (69477e2e1c1a)；6 在盘指针全在；末尾空列已 drop
## T1 E1 分子 — PASS（e1_numerators.csv 62784 行 + e1_counts.json）
仅 Retraction 类，按 OriginalPaperDOI 去重保留最晚 RetractionDate（多 notice DOI 16 个）→ 总单位 62784（with-doi/no-doi 拆分与 pre_dedup 明细在 e1_counts.json）
宇宙 orig 2000–2025：62784 行；排除 pre2000=977 / post2025=41 / NA=0（均报告、无静默丢弃）；no-doi 行单独计数
112 reason 映射 unmapped=0 → E1_CANDIDATE=16316 / NON_E1=7251 / UNDECIDED=39217；日期 NA：orig 0% / retr 0%（未插补）
## T2 校正延迟 — PASS（correction_delay.json）：有效 62784（NA=0，未插补）；median=1.32y；CDF@5y=0.8745
p25/p75/p90 与 CDF@1/3/10/20y 在 json；by_bucket(n/median/CDF@5y) 在 json；delay<0=0（日期质量，仅报告）；同年内(0≤d<1)=0.4052
## T3 检出率 — PASS（detection_rates.json）：分母=222,714,158（stage2 P4 实测、2000–2025 publication_year 口径、冻结；秒级漂移只注记、段3b 重钉 1 次）
per100k：all retractions≈28.19 / E1_CANDIDATE≈7.33（n×1e5/DEN，精确值在 json）；逐年 2000–2025 + 全 subject 降序在 json
detection_bias_warning 写入全部 3 个 json 顶层：检出≠患病；notice 级 reason≠裁定；RW 覆盖随时空异质（检测偏倚）
## 七禁令自检 — 7 项全合规：1 撤稿≠造假✓ 2 不可重复≠造假✓ 3 无自报率×论文数当患病率✓ 4 无国家/期刊撤稿率当 misconduct 流行率✓
5 无任意复合分✓ 6 无归属规则不称关联基金为浪费✓ 7 无模型标注被埋没杰作✓（country top20 仅计数分布，非排名）
## 段3b 移交（Gate 1）：审计子集 n=300，按 orig 5 年分层（2000-04/05-09/10-14/15-19/20-24+尾层），seed=20261008
DOI batch≤100/query；title 抽查 10；分母重钉 1 次；OpenAlex 预算≤13 查询；已知局限=检测偏倚/reason≠裁定/no-doi 未去重/分母秒级漂移
## T4 在盘核验（各 T1/T2/T3 运行时已确认落盘）
$ ls data/stage3/ = correction_delay.json, detection_rates.json, e1_counts.json, e1_numerators.csv（4 件均非空）
$ wc -l data/stage3/e1_numerators.csv = 62785（表头 1 + unique papers 62784，据 T1 运行输出推算，假定字段内无换行）
DONE stage3a 005
