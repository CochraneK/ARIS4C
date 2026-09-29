# 002-language-geometry · 段4 摘要（stage4_summary）

- 日期：2026-09-30 ｜ 模式：**编排器直写**（冻结 RESEARCH_PLAN §7：段4 双语稿件不跑 LLM）
- 未重跑 LLM、未重算任何数字；全部数字逐字转录自冻结落盘 JSON（来源映射见 paper/paper_EN_notes.md §1）

## 1. 交付物（本段新增）

| 文件 | 内容 |
|---|---|
| `paper/paper_EN.md` | 英文母版：标题+Abstract+§1 引言（主张/阴性来源/H1–H4 预注册/claims 政策）+§2 数据与文献登记+§3 M1+§4 M2+§5 M3+§6 M4/H3+§7 稳健性×4+§8 讨论+§9 局限×7+§10 claims+参考文献 29 条 |
| `paper/paper_ZH.md` | 忠实简体中文版（与 EN 母版逐节对应，数字逐字一致） |
| `paper/paper_EN_notes.md` | 数字→来源映射表、全精度 top-1、执行 provenance（段1/2 executor 死于 128K + 接力直写；段3 正常）、M1 null 计划-实现偏差披露、sha256 8 件表、WALS 守卫/skip 清单、m4 quirk 引用指引、冻结日期 |

## 2. 门控状态

| 门 | 状态 |
|---|---|
| 数字对盘（6 关键值 + H3 verdict + leaveout 9 格 抽盘 JSON） | PASS（本段开工前 spot-check 全命中，见 notes §1） |
| 引用纪律（只引 REGISTRY 29 条 + 本地元数据） | PASS（参考文献 29 条逐字摘自 lit/REGISTRY.md；3 条无 DOI 如实标注；截断题名 5 条加 [truncated] 注） |
| claims 5 条 adherence | PASS（§10 逐条核对；item 3 头条措辞 = 注册措辞"周期性结构不提供留出预测力"） |
| quirk 披露 | PASS（§5 M3 reading + §9 局限 3 + notes §7 三处） |
| 残标检查 | 0（grep TODO/FIXME/XXX/TBD/placeholder/to-be-filled 于 paper/ → 无匹配） |

## 3. 关键裁定（冻结，逐字）

- **H3 verdict：**「H3 拒绝/降级（逐层依据见 basis；探索性聚合、非新增假设）」
- **头条表述（claims item 3）：** 周期性结构不提供留出预测力。
- H1：TLI 3 表 circular_better（p ≤ 1.17e-06），GBI 2 表 marginal_better（p ≤ 4.02e-21），WALS 名义 circular（perm_p=null）。
- H2：UPGMA 5 主表全拒绝（CI 下界 0.0465–0.1008… 最强 GBI_stat 0.1144 / TLI_stat_large 0.1008）；MDS 3 表拒绝（TLI_large / GBI_stat / GBI_log）。
- 稳健性：leaveout 唯一离群源 = GBI 层；leakage_sens 无翻转；M5a GBI 双 worse=TRUE（圆形差于地理先验）；随机 2-D null 2 表已执行（p≈0.31–0.54 → 低维几何一般性质）、4 表预算未执行。

## 4. 遗留（带往段5/段6）

1. 随机 2-D null 4 表未执行（预算）——建议大预算补跑（可选增强，非判定依赖）。
2. `m3_WALS.json` 缺 `h2_direction` 键（缺口 2，已在 notes/正文披露）。
3. m4 H1 符号 quirk（缺口 1，已披露 + 引用规则固化）。
4. 段5 待办：paper.json（stage5_final）+ final_FROZEN.txt + git 同步（排除 .log/.npz/>5MB/草稿）+ commit/push。
