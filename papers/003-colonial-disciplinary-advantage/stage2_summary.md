# stage2 收官摘要（编排器接管补完 · executor 死于 128K）

**状态：DESIGN_LOCKED 8/8 冻结 · 零 outcome 纪律保持 · 段3 解锁**

## S1 便宜探针
- P2 同键多值 = **pipe `|` OR 语义**：count(BR|US)=36,209,582 ∈ [max=32,546,581, sum=36,441,304)；|BR∩US|=231,722；AND 排除。
- D 层 institution filter 冻结：`authorships.institutions.country_code:XX`（BR=3,894,507）；`institutions.countries` 等 3 路径 4xx。
- 窗口证据：BR×Mat≥1990=143,887（97.4%）vs ≥2000=136,212（92.2%）；GB×Mat 1900s=535。

## S2 学科冻结（data/subject_freeze.md）
- 确认 11 科 + 对照 6 科；subfield 优先 > concept > topic；Linguistics pipe OR 跨 A&H/SS。
- 缺口（须论文披露）：Archaeology/Botany/Tropical/Mining 无 subfield，concept/topic 锚定；1105 近似含 ecology；tropical 农业维度缺失。

## S3 IKES 双盲（data/IKES_freeze.md + data/ikes/）
- 68 格 pass1=pass2，**0 仲裁格**；确认集均值 16.45 vs 对照集 8.67。
- 前 5 科：Anthropology/Botany/Law 19，Mining/TropMed 18。
- 局限：子代理 spawn 失败（网关 400 reasoning effort）→ Coder B 降级为同上下文反转序第二遍，**不得声称独立 Coder B**（已入 freeze 文档）。
- 100 置换落盘（seed=20260929）供段3/4 H2 null 分布。

## S4 暴露（data/exposure_manifest.md）
- COW v3.1 双路径：Path A（Entities.pdf 区间）2617 行/1133 实体；Path B（contcol master）281 对；**合并 339 对 = both 207 / A 58 / B 74**，23 宗主国 + 1 未解析，1816–2016。
- OWID = 去殖民时间交叉验证（119 实体）；/colonialism 页实为政体枢纽（无殖民专属 CSV）→ **宗主国 raw 源仅 COW**（单源风险已声明）。
- Easterly 403 = MANUAL_REQUIRED（不阻塞）。

## S5 DESIGN_LOCKED（data/DESIGN_LOCKED.md）
8/8：① pipe OR ② country_code ③ 学科冻结 ④ IKES 冻结 ⑤ 暴露 manifest ⑥ H1=log1p ⑦ 窗口 **≥1990 主 + ≥2000 敏感性** ⑧ 主 dyad 集 = exposure_pair_merged 机械导出（'?' 排除并记录）。

## 交付物（本段新增）
- 文档 6：probes_stage2.md / subject_freeze.md / IKES_freeze.md / exposure_manifest.md / DESIGN_LOCKED.md / 本文件
- 数据 4：data/ikes/{pass1.tsv, pass2.tsv, ikes_scores.csv, permutations.tsv}
- 脚本：exposure_parse_full.py（executor 残稿合并 + per-page 300→200 修复）/ exposure_merge.py / ikes_compare.py / ikes_finalize.py / probe_stage2{,b,c,d}.py / dump_ids.py 等
- raw 只落沙盒（COW zip + OWID csv，sha256 见 manifest）

## 段3 任务
1. 主 dyad 集导出（OpenAlex country code 映射 + 排除清单）
2. 面板构建：主 dyad × 11 科 filter × ≥1990（BR 基线 143,887 ≈ 719 页 @200/页，幂等+backoff）
3. H2 单调性 + 置换 null（permutations.tsv）
4. 方案 A 同步（raw 不入库）
