# ARIS4C-005 stage3b summary — Gate 1：审计子集 DOI/标题匹配 + 原因编码（n=300）
2026-10-08 | 输入=stage3a 冻结产物（只读） | 网络=仅 OpenAlex，用 7/15 查询，data/raw 零新增文件
## 关键数字
| 项目 | 值 |
|---|---|
| 审计子集 | 300/60348（with-DOI），六层配额 7/21/65/60/144/3（2000-04…2025 尾层），seed 20261008，层内 SHA256 排序 |
| DOI 匹配覆盖 | 297/300 = 0.99（3 批×100，原始 JSON 在 _evidence/batch1-3.json） |
| 逐年未匹配 | 2017：1 例（6.2%）；2023：1 例（6.7%）；第 3 例落于子集 n<5 层（n≥5 守卫不评 2× 规则，详见 gate1_decision.json） |
| bucket 分布（300） | 三桶计数见文末「DONE 前核验」节（实时 Import-Csv 统计） |
| unmapped reason | 0（子集 reason 提及全部命中在盘 112-reason 映射，data/rw_e1_mapping.csv） |
| title 抽查 | 3/3 查询（无缺题跳过）：exact 1，any 2，HTTP400 1（标题含通配符，OpenAlex 拒绝，见 title_spotcheck.json） |
| 分母重钉 | 222714158 = 冻结 222714158，drift 0.000%（<0.5%，仅注记） |
## Gate 1 判定
**PASS_WITH_LIMITATIONS** — coverage 0.99 ≥ 0.85 且 unmapped=0，但 2017/2023 未匹配率（6.2%/6.7%）> 2× 全局 1.0%，系统性 artifact 条款未全绿，不构成完整 PASS；coverage ≥ 0.70 → PASS_WITH_LIMITATIONS。两信号各仅 1 例（小样本），无管道系统性损坏证据。
局限性：① 2017/2023 各 1 例触发 2× 规则；② 第 3 例未匹配在 n<5 层，未纳入 2× 评估；③ 1 例 title 抽查因 HTTP400 未能验证（标题含 * 或 ?）；④ 分母漂移 0.0%（非 limitation）。检出≠患病：本段仅判数据管道质量，不涉患病率。
## 段4 移交（模块 B）
Gate 1 非 FAIL → 模块 B 启动：分层文章样本 5000-10000 自动表征 + 人工裁决金标 + 分层贝叶斯潜类模型；结果带 Gate 1 PASS_WITH_LIMITATIONS 警示。交付物：data/stage3b/{audit_subset.csv, subset_selection.json, doi_match_results.csv, rw_subset_lookup.json, title_spotcheck.json, denominator_reprobe.json, gate1_decision.json, reason_coding_subset.json, _evidence/×6} + data/code/s3b_{t0,select,match,spotcheck,gate}.py
## DONE 前核验（实时统计）
bucket_dist: 
NON_E1=34 E1_CANDIDATE=73 UNDECIDED=193
unmatched (doi year): 
10.1177/014616720026200 2000 | 10.26355/eurrev_201708_13284 2017 | 10.1016/j.crphar.2022 2023

ls data/stage3b/ (recursive, name size):
data\stage3b\_evidence 1
data\stage3b\audit_subset.csv 38077
data\stage3b\denominator_reprobe.json 304
data\stage3b\doi_match_results.csv 119024
data\stage3b\gate1_decision.json 22014
data\stage3b\reason_coding_subset.json 322
data\stage3b\rw_subset_lookup.json 94800
data\stage3b\subset_selection.json 405
data\stage3b\title_spotcheck.json 2547
data\stage3b\_evidence\batch1.json 36916
data\stage3b\_evidence\batch2.json 37052
data\stage3b\_evidence\batch3.json 37673
data\stage3b\_evidence\denominator.json 17621
data\stage3b\_evidence\spotcheck_02.json 33807
data\stage3b\_evidence\spotcheck_03.json 20027

wc -l stage3b_summary.md (pre-append): 17
DONE stage3b 005
