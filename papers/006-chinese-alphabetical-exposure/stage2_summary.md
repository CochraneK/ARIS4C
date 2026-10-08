# stage2_summary — ARIS4C-006 段2修复 run（2026-09-30）

本 run：本地计算+文档，0 次 API 查询。分析脚本 data/s2_analysis.py；结果 data/s2_pilot_results.json（§1–§4）；冻结文档 STAGE2_FREEZE.md。

## Pilot 7 条最新状态
1. P1 覆盖 — PASS：4 领域 counts（2010–2024 CN）math 142,544 / physics 340,328 / nursing 42,464 / medicine 1,610,478；领域 filter 形态 primary_topic.field.id:<fid> probe OK（probe key 显示 bug 无数据影响）。
2. P2 语境变异 — PARTIAL：field 级 ExcessAlpha 分化清晰（math +0.162 vs physics −0.021 / nursing +0.001 / medicine −0.015）；journal×field×year 220 cells 但最大 cell n=6（100 篇/领域碎片化），var=0.173、range 1.948 由稀疏 cell 主导 → journal 级判定延至 Stage 3 全面板。
3. P3 解析 — PASS：2603 署名（100% 罗马化，0 汉字名）tier2 覆盖 79.6%（≥50% 闸）；both-token-match 29.6% 已 flag；50 条抽查入 §3。5D 正式 blind 验证在 Stage 3 执行。
4. P4 消歧诊断 — DEFERRED：Stage 3 入口闸（全面板构建后、主拟合前；失败则收窄/停止）。
5. P5 基线复现 — PASS（继承）：ChineseNames 23 首字母占比在盘，unknown=0，宿主已复现。
6. P6 稳定性 — PASS：排除两作者后 ExcessAlpha Pearson=0.990、max|Δ|=0.047（两作者 n=35/14/4/5，math/physics/nursing/medicine）。
7. P7 closest prior — PASS（继承段1）。

## 关键数字与决定
- 暴露估计器：Exp 已接入人口频率 h_n（familyname.csv n.1930_2008，1806 姓→391 拼音），均匀 A–Z 零假设弃用；Obs=全署名解析且拼音键非降序。
- 抽取预算（Stage 3）：页数 713/1702/213/8053=10,681>5,000 → 确定性子采样 published 升序每 k=3 页取 1 → 预估 3,562 查询。
- 样本局限：sort=publication_year:desc 使 4×100 偏 2024 最新；raw 名全罗马化 → 5B 为主路径（5A 汉字路径保留供 Stage 3）。

## 交付
STAGE2_FREEZE.md（70 行：8 冻结项+证据表+P4 闸+预算+6 deviations）；data/s2_pilot_results.json（§1–§4）；data/s2_analysis.py。
DONE stage2 006