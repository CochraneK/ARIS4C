# ARIS4C-005 stage2 收官（fix，2026-10-08）

机器空窗 8 天；上一 run 于 T5 前死于上下文溢出（reason=length）。本次最小续跑 T3/T4/T5（宿主代跑+代写），T1/T2 沿用已验收。

## 逐项验收

| 项 | 内容 | 状态 | 关键数值 |
|---|---|---|---|
| T1 | RW 官方 CSV | ✅ PASS（在盘） | retraction_watch.csv 67,038,098B（2026-09-29 生成） |
| T2 | E1 三桶映射 | ✅ PASS（在盘） | rw_e1_mapping.csv 5,457B |
| T3 | 分母单年 probe | ✅ PASS（本 run） | P1=10,220,607 · P2=11,592,932 · P3=400 · P4=222,714,158 |
| T4 | RePORTER 重试 | ⚠️ CAUTION（本 run） | HTTP 404（需 key/端点），Module D 仍 BLOCKED |
| T5 | DATA_PROFILE + 本文件 | ✅ PASS（宿主代写） | DATA_PROFILE 新版（≤70 行）+ 本文件 |

## 关键结论
- 分母：单年过滤正常（P1≠P2 且均 ≪P4），**无退化**；2000–2025 正典分母 = **222,714,158**（vs 09-30 的 220,028,794，+2.7M 正常漂移）
- P3（publication_date 区间）400 不可用 → 记 limitation，分母走 publication_year 口径
- RePORTER 404 → 模块 D（NIH 归属）BLOCKED（需 key），不影响主线 A/B/C
- 零 outcome 纪律保持：未算率、未跑模型；撤稿≠造假；notice≠裁定

## 移交段3
- 分母固定（222,714,158），RW 官方 CSV + E1 映射可物化
- 主线 A/B/C 可物化；模块 D 降级可选（待 key）
- stage3 契约按 stage2_prompt.txt 定义

DONE stage2 005
