# SPOKE-SAFE 实验追踪

> 项目: 阿凡达治疗 (Avatar Therapy) — SPOKE-SAFE 基准论文
> 状态: ✅ E1 ✓ E2 pilot完成

## 总路线

| E# | 名称 | 状态 | 产出 | 备注 |
|----|------|------|------|------|
| E1 | Adv-AVH 对抗语料库 | ✅ 完成 | `adv_avh_corpus.jsonl` | 540条 S0-S5 六级语料，本地模板化生成 |
| E2 | Assertiveness-M 打分器 | ✅ pilot完成 | `scored_results.jsonl` | 90条pilot (每级15条) 已打分，待全量540条 |
| E3 | Silent Override 守卫原型 | ⏳ 待开始 | - | 安全拦截 + 替代回复 |
| E4 | 安全-疗效权衡分析 | ⏳ 待开始 | - | 跨等级权衡曲线 |
| E5 | 整合打包 | ⏳ 待开始 | - | 论文就绪资产 |

## E1 详细进度

- **目标**: 540 条对抗语料, S0(中性) ~ S5(致命)
- **状态**: ✅ **已完成** (本地模板化生成，零API开销，<1秒完成)

## E2 详细进度

- **目标**: 对化身回复进行 PC/PA/SA 三维评分
- **pilot**: ✅ **90条完成** (2026-09-04)
  - 耗时: ~10分钟42秒 (5路并发, API调用)
  - 结果: 90/90 成功率, 全部 verdict="challenge"
  - PC均值: 8.09/10, SA均值: 8.54/10, PA均值: 8.68/10
  - 分析脚本: `pilot_analysis.py`

## 测量学分析 (pilot)

| 指标 | 数值 | 解读 |
|------|------|------|
| PC-SA r | 0.14 | 维度近正交 — PC与SA捕捉不同构念 |
| PC-PA r | -0.05 | 近零相关 — 挑战力度不影响联盟 |
| SA-PA r | 0.30 | 弱正相关 — 安全和联盟有部分重叠 |
| ρ(severity,SA) | **0.72** | 严重级别强预测SA提升 |
| ρ(severity,PC) | 0.36 | 弱正相关 — 化身一致挑战不因安全妥协 |
| SA天花板 | 47% | 可接受偏高（S4/S5多满分） |
| 地板(≤3) | **0%** | 无低分失败案例 |

**分级阈值效应**: S3→S4 SA跃升 d=+3.78 (t=10.35, p<.001) — 明确的安全优先行为被自动激活

- **全量540条**: ⏳ 待运行 (预估 ~60分钟)

## 实验方案定位

论文类型：基准+测量学量化论文 (Benchmark + Psychometric)
投稿目标：Behavior Research Methods / JMIR Mental Health / Psychiatry Research (Methods)
核心贡献：首个精神科特异性"命令性幻听挑战质量"评估框架
方法论限制：DeepSeek 自评 (single-model self-evaluation, 无跨模型验证)
