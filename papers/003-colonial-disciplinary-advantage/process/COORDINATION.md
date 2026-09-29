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

## 段2 时间线（2026-09-29/30）

| 时间 | 事件 |
|---|---|
| 09-29 晚 | **executor 段2 运行**（aris.exe，stage2_run.log 283,130 B）→ **21:51 死亡**：OpenAI 400，prompt 131073 > max 131072 tokens（128K 硬顶）；遗留 download_exposure.py + 暴露 raw（COW zip a51e4c5e… / OWID csv 869535c0…，已幂等落盘）+ exposure_parse.py / exposure_parse_tail.py（未合并两段脚本，从未运行） |
| 09-29/30 | **编排器接管**：重读三件（stage2_prompt / DATA_PROFILE / 段1 交付物），残标接力 |
| 09-29/30 | S1 复探（probe_stage2{,b,c,d}.py）：P2 = pipe OR 判明；D 层冻结 `authorships.institutions.country_code`（BR=3,894,507）；窗口 count 143,887 / 136,212 / 535 → `data/probes_stage2.md` |
| 09-29/30 | S2 学科冻结：subfield 复探（4 科无 subfield 坐实）+ s/t/c 锚定探针 → `data/subject_freeze.md`（确认 11 + 对照 6） |
| 09-29/30 | S4 暴露解析：exposure_parse_full.py（executor 残两段 verbatim 合并 + **修复** per-page 300→200 分页）→ Path A 2,617 行/1,133 实体；exposure_merge.py → **339 对**（both 207 / A 58 / B 74；23 宗主国 + 1 未解析；1816–2016） |
| 09-29/30 | S3 IKES：pass1 68 格 → **子代理 spawn 两次失败**（网关 400 reasoning effort 错配）→ Coder B 降级同上下文反转序第二遍 → 68 格全一致、**0 仲裁格** → ikes_scores.csv + permutations.tsv（seed=20260929）+ `data/IKES_freeze.md` |
| 09-29/30 | S5：`data/exposure_manifest.md`（URL/sha256/单源风险披露）+ `data/DESIGN_LOCKED.md` **8/8 冻结**（窗口 ≥1990 主 / H1=log1p / dyad 机械导出 / '?' 排除） |
| 09-29/30 | **段2 收官**：stage2_summary.md + 本账本 + 方案 A 仓库同步 |

## 段2 验收数字

- 交付物：文档 6（probes_stage2 / subject_freeze / IKES_freeze / exposure_manifest / DESIGN_LOCKED / stage2_summary）+ data/ikes/ 4 文件 + code 新增 21 脚本
- P2：count(BR\|US)=36,209,582 ∈ [max, sum) → OR；|BR∩US|=231,722
- 暴露：COW 339 对 / 23 宗主国 / 1816–2016；OWID 119 实体（去殖民时间交叉验证）
- IKES：68 格 pass1=pass2，0 仲裁；确认集 16.45 vs 对照集 8.67
- 零 outcome 纪律：保持（全程无 country×discipline 产出数值物化）

## 段2 已知缺陷/局限（标注，不重跑）

1. Coder B = 同上下文反转序第二遍（子代理网关 400），非真双盲；68 格 100% 一致为共享上下文后果，不构成真 ICR——已入 IKES_freeze.md 强制声明
2. 4 学科无 subfield（Archaeology/Botany/Tropical/Mining）→ concept/topic 锚定，置信度降级须论文披露
3. 宗主国指派单源（COW）；缓解 = 双路径内部交叉验证（both 207 对 = 61% 高置信核心）
4. 1 个未解析宗主国 code（'?'）→ 段3 排除并记录
5. D 层 display_name.search 匿名限流 ×3 = UNVERIFIED（不阻塞，D 层不依赖）
