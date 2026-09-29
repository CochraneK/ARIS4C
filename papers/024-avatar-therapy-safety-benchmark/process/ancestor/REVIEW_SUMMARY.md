# Review Summary — SPOKE-SAFE 提案

> **日期**：2026-09-07
> **评审后端**：DeepSeek（同族 best-effort；**非交叉模型裁定**——本环境无 Codex/Oracle/manual，llm-chat HTTP 评审解析为同族 `dsv4-dspark` 且 fail-closed）。
> **初始评分**：4/10（当前临床 RCT 形态），不建议直接资助。

## 关键批评（采纳）
1. pilot 为 LLM 自评，非临床验证；power_challenge 8.67 是循环构念。
2. 因子设计剂量等价是范畴错误（AT 本质交互）。
3. Silent Override 对真实精神病未经验证（无延迟/宕机/危机冻结协议）。
4. 坚定度指标是解法导向、未嵌入患者结局。
5. 纯计算探针无人在环 = 无真实性可行性证据。

## 采纳的修正
- 两阶段（Stage 1 人机回环 → Stage 2 预注册 RCT），拒绝一步到位。
- 计算侧先行：Adv-AVH 基准 + 坚定度指标 + Silent Override + 权衡曲线，作为**测量工具**提交，不做疗效声明。
- 收敛主张：不称"首个 LLM 化身"，称"首个复现开源的精神科特异性评估框架 + 权衡证据"。

## 遗留（投稿/后续前必须）
- 真人 ICC 效度验证；临床共同 PI；伦理。
