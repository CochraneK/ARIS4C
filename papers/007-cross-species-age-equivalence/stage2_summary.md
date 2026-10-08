# stage2_summary — ARIS4C-007 cross-species age equivalence（2a+2b 合并）, 2026-09-29

## 完成度
- S1 方法图谱: ✅ figures/method_map.md（A0–A6 概念图 + 方法卡 + 表 E 约定；A4/A5/A6 仅概念, 属段3）
- S2 数据表 (2a): ✅ tableA 9 物种 × 22 列；tableB 75 事件行（10 类事件, anAge/PanTHERIA 双估计）
- S3 映射脚本: ✅ code/a0_natural_lifespan.py, a1_max_age.py, a2_lifespan_anchors.py, a3_loglinear.py（各读表 A(+B) → 写自带片段；docstring 含公式/设计/代理选择/365.25 d/y）
- 表 E: ✅ data/tableE_partial.csv 216 行 = 9 物种 × q∈{0.25,0.5,0.75,0.90,0.95,0.99} × 4 方法；每格 = 双输入(anAge/PanTHERIA)下区间 [out_low,out_high,out_mid]，不压单点
- 一键复现: ✅ python code/run_all.py（exit 0, 216 行核对）
- 抽查: ✅ code/spotcheck.py exit 0 — 人/小鼠 × A1/A3 共 13 项全 PASS；A3 六参考值 (lit/clock3_formulas.txt) 容差 1e-6 全中（m̂ 人=1.705769, 鼠=3.698807；y 4 值全中）

## 关键决策与来源
- AnAge 快照: lu2023 MOESM3 (43587_2023_462_MOESM3_ESM.xlsx, Table S1.13), 快照日期 2026-09-30, 5473 行 × 105 列 → data/suppl/anage_lu2023_snapshot.csv；provenance 见 data/manifests/sources.csv。
- A0 代理: tableA 与快照均无典型/预期寿命列（仅 maxanAge 与 PanTHERIA.MaxLongevity_m）→ L_typ := anAge max_age_yrs, PT 交叉核验给区间（理由已写入 docstring）。
- A2: Animal-Age GitHub 基线检索 0 结果（前次已查）→ 自建逐段线性锚点映射（anAge 主锚 conception/birth/weaning/sexmat_f；PT 行作敏感性；人类 anAge 锚点为参照系；单调性守卫）。
- A3: lu2023 formula (4)(5)(8)(9), m̂=5·(G/ASM)^0.38 默认版（不依赖 L_max）；oracle m*（formula 6, 1.3× 校正）仅稳健性, 不作默认, 未实现为默认路径。
- 双估计约定: anAge 主、PanTHERIA 敏感性（区间输出），与 2a 建议一致。

## 已知问题（带入段3）
1. PT 双估计未定标: 同一事件 anAge/PT 双值（如人 weaning 639 vs 725.86 d）, 本段以区间处理, 单值选择待段3。
2. References 列 float 损坏: 犬/猫/狐獴/马 anAge References 编号列表前次转 CSV 损坏 (4.34e+35), 不可恢复；段3 若需逐条文献须重读 xlsx（本段未动）。
3. PanTHERIA 2023 数据库论文 DOI 未验证（manifest 已 flag）。
4. A2 老年段仅线性外推（sexmat 锚后粗糙, 如猪 q=0.25 → 107–245 人年）; 猫缺 weaning_PT 行; A3 的 G 无 PT 行 → 共享 anAge 值（docstring 已声明）。

## 段3 预估（A4/A5/A6）
- A4 复现 (Translating Time, Crofts 2023): 阻塞点 = crofts2023.xml 公式/协议提取（段3 解禁 XML 后做）+ tableB PT 事件覆盖不对称；预计 1 会话。
- A5 构造 (生存等价): 阻塞点 = 冻结表无存活数据, 需外部死亡率数据源；方法选型 (S(t) 匹配 vs hazard) 需先冻结；预计 ≥1.5 会话。
- A6 时钟应用 (分子时钟): 阻塞点 = 无输入甲基化数据（s3_clock1/2/3 权重在盘但不可直接应用）, 组织/训练细节需再从 lu2023 提取；若仅构建"应用框架"可行；预计 1 会话。
