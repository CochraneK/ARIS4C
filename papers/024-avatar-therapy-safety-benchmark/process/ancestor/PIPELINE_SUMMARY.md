# Pipeline Summary

**Problem**：LLM 驱动的化身治疗缺乏精神科特异性、可复现、跨模型可比的"挑战质量 + 安全"评估工具。
**Final Method Thesis**：SPOKE-SAFE — 命令性幻听对抗基准 + 治疗性坚定度指标 + Silent Override 安全架构 + 安全-疗效权衡曲线。
**Final Verdict**：READY（计算侧可执行贡献）；临床 RCT = REVISE（下游 Stage 1）。
**Date**：2026-09-07

## Final Deliverables
- Proposal: `refine-logs/FINAL_PROPOSAL.md`
- Review summary: `refine-logs/REVIEW_SUMMARY.md`
- Refinement report: `refine-logs/REFINEMENT_REPORT.md`
- Experiment plan: `refine-logs/EXPERIMENT_PLAN.md`
- Experiment tracker: `refine-logs/EXPERIMENT_TRACKER.md`

## Contribution Snapshot
- **Dominant contribution**：首个精神科特异性、可复现、跨模型可比的 LLM 化身"挑战质量+安全"评估框架（基准+指标+安全架构+权衡数据）。
- **Optional supporting**：Silent Override 半自动安全架构工程设计与护栏延迟基准。
- **Explicitly rejected complexity**：2×2 因子 RCT、VR 具身、跨文化现场部署、语音 SER 剂量——下游/`needs manual`。

## Must-Prove Claims
- C1：Adv-AVH 基准区分不同 LLM 化身后端（效应量≥0.5）。
- C2：Assertiveness-M 与精神科医生评分 ICC>0.8。
- C3：Silent Override S4/S5 自动降级 TPR≥0.95、守卫延迟<1s。
- C4（发现性）：护栏不牺牲挑战效力的权衡曲线。

## First Runs to Launch
1. E1 — Adv-AVH 基准构建 + 多后端区分度
2. E3 — Silent Override 原型 + 降级正确率/延迟（可与 E1 并行）
3. E2 — 指标构造效度自洽检查（E1 后）

## Main Risks
- **无临床验证**：指标/过渡为测量工具，明确非临床声明。
- **碰撞**（UCL/KCL 预印本）：差异化收敛到公共基准资产 + 指标 + 权衡数据。
- **指标只是情感分类器**：构造效度 + 区分度 + 预测效度（真实 ICC 需 `needs manual clinical review`）。

## Next Action
- 计算侧：`/experiment-bridge`（实现 E1-E5）或 `/run-experiment`。
- 临床侧：接入临床共同 PI + 伦理，进入下游 Stage 1。
