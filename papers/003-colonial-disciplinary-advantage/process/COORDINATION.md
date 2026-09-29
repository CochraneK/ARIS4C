# COORDINATION — 003 殖民遗产与学科优势（重跑账本）

## 段1 时间线（2026-09）

| 时间 | 事件 |
|---|---|
| 09-25 | RESEARCH_BRIEF.md 冻结（唯一 idea 输入） |
| 09-28 | stage1_prompt.txt 落盘（冻结执行契约） |
| 09-29 18:40–19:08 | **executor 段1 运行**（aris.exe，stage1_run.log 389,971 B）→ **死亡**：stream reason='length'（128K 硬顶）假 Done；遗留 5 个代码文件 + 原检索 50 条 TSV + urls_check |
| 09-29 20:11 | **编排器接管**：supp_search.py 修复 3 处（backoff 3/6/12/24；raw 幂等落盘；no_DOI 分支显式构造） |
| 09-29 20:24 | 补检 run 1（supp_run.log）：12/14 查询 200，s12/s13 503 |
| 09-29 20:29 | 补检 run 2（supp_run2.log，幂等重跑）：**14/14 全 200**；98 条补检（VERIFIED 91 / VAM 5 / UNVERIFIED 2） |
| 09-29 晚 | P1 单维 group_by 验证通过；P2 OR 语义两轮 503 未决 → 入段2 |
| 09-29 晚 | 四件交付物落盘 + 本账本；登记表冻结 **148 条** |

## 验收数字

- REGISTRY.md：148 条（grep `^- [` = 148）；VERIFIED 126 / VAM 15 / UNVERIFIED 5 / MISMATCH 2；重复 2（[076][111]）
- 补检运行：run2 = 98 new / 0 mismatch / 2 unverified（[058] crossref 404、[076] no_DOI 重复）
- P1：5 组（top3：SS 1,136,328 / Med 899,654 / AgBio 555,883）
- 零 outcome 纪律：四件交付物无任何 H 检验统计量/效应值/产出矩阵数值

## 接管记录（executor 死亡 → 编排器补完）

- 死亡判定：stage1_run.log 尾部 + 产物 mtime（19:08 后无新产物）；.claude/sessions 无该会话记录（失败会话不落盘）
- 补完范围：98 条补检（14 条 title.search 精准查询）+ P1/P2 探针 + REGISTRY 合并冻结 + DATA_PROFILE + LIT_NOTES + stage1_summary
- 未重做：executor 原 50 条检索与核实（结果可用，缺陷已标注）

## 已知缺陷（标注，不重跑）

1. supp_search.py dedup `list(csv.DictReader(...))[1:]` 误删原50首行（Wolfe 2006）→ 重复 [111]
2. [076] Balassa 1965 OpenAlex 重复记录（no_DOI）
3. P2 同键多值 OR 语义未验证（两轮 503）

## 段2 队列（排在 002 段4 之前）

1. P2 复探（count(BR,US)） 2. D 层 institution 探针 3. 学科集合冻结（subfield 复探 + crosswalk）
4. IKES 双盲编码 + 仲裁 5. 暴露下载（COW/OWID 自动；Easterly 人工） 6. H1 变换预选 7. 窗口/dyad 集冻结 → DESIGN_LOCKED
- 段2 契约：暴露定义冻结 + 学科集合与 IKES 编码 + OpenAlex 面板构建（stage1_prompt 段2 定义）
