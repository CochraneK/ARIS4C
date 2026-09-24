# ARIS4C022 · Planetary Taxonomy × fsQCA

## 一句话

把“什么算行星 / 矮行星 / 卫星 / 小天体”写成可检验的**构型分类问题**：比较轨道层级、动力学主导、自引力/球形、质量与尺度、组成、气体、热演化、地质活动和恒星环境等条件的必要性、充分性与等效路径。

## 科学边界

本项目不把已确定的天文学事实包装成悬案。按当前 IAU 太阳系定义，火星是八颗行星之一；因此“火星到底是行星还是卫星”在主分析里作为**正对照**，不是待裁决结果。

QCA 在这里主要用作 **configurational taxonomy / set-theoretic comparison**，而不是把分类标签误写成自然因果关系。若 outcome 直接使用 IAU 分类，我们讨论的是“哪些条件组合重现或挑战分类边界”，不是“这些条件造成了行星”。

## 核心问题

1. 哪些条件对“IAU 行星”是必要或充分的？
2. 行星、矮行星、天然卫星、小天体之间是否存在不同但等效的特征配置？
3. 质量、直径、密度、气体/矿物组成、生命周期等直觉变量，在加入轨道层级与动力学主导后还有多少分类信息？
4. Margot / Soter 一类动力学判据能否单独或与其他条件组合区分八大行星与边界天体？
5. “比某些行星更大却仍是卫星”的案例能否清楚展示：**分类首先取决于它绕谁运行，而不是单纯大小**？

## 第一阶段案例框架

目标约 40–60 个太阳系天体，分层抽样：

- 8 大行星；
- 5 个 IAU 正式认可的矮行星；
- 代表性大型/中型卫星（Moon, Io, Europa, Ganymede, Callisto, Titan, Triton, Charon, Enceladus 等）；
- 代表性小行星 / 小天体（如 Vesta, Pallas, Hygiea 等）；
- 预留边界案例与敏感性样本。

第二阶段再考虑外行星系统；不在太阳系定义尚未泛化的地方偷换 IAU 标签。

## 方法

- csQCA：定义性/离散条件；
- fsQCA：质量、半径、动力学主导、密度、气体包层、地质活性等连续条件；
- 必要条件分析；
- 充分条件 truth table + complex / intermediate / parsimonious solutions；
- consistency / coverage / PRI；
- calibration sensitivity；
- leave-one-case-out / 边界案例稳健性；
- 与聚类 / 降维的描述性结果并列，避免把 QCA 当万能分类器。

详见 [RESEARCH_PLAN.md](process/RESEARCH_PLAN.md) 与 [VARIABLES_AND_CALIBRATION.md](process/VARIABLES_AND_CALIBRATION.md)。

## 当前状态

已完成问题重构、方法边界、变量族、公式族和权威数据源骨架。下一 gate 是冻结 40–60 个案例清单，并自动抓取/人工核验第一版 case matrix。
