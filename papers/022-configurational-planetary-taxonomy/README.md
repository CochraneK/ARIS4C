# ARIS4C022 · Planetary Taxonomy × fsQCA

把“什么算行星 / 矮行星 / 卫星 / 小天体”写成可检验的构型分类问题。火星仍是正对照，不是分类悬案。

## 当前 canonical 数据层

- 50 个冻结案例。
- `raw_physical_core_v0.1.csv`：34/50 JPL 核心物理数据。
- `orbital_geometry_v0.2.csv`：8 行星 JPL approximate elements；5 矮行星 derived-a；21 卫星 JPL Mean Elements；16 小天体待 SBDB。
- `derived_physics_v0.2.csv`：34 个案例的重力、逃逸速度、密度诊断和太阳环境。
- `evidence_state_v0.4.csv`：三批盲编码后 **139/300** 个证据状态单元完成。
- `SOURCE_CONFLICT_AUDIT.md`：开始区分真正冲突与旧知识被新证据更新。

## Evidence coverage

- composition 34/50
- atmosphere 24/50
- differentiation 24/50
- geology 23/50
- present/persistent ocean 14/50
- tidal heating 20/50

现在 **所有 34 个行星 / 矮行星 / 选定卫星至少都有 composition evidence state**；组成层剩下的 16 个空缺恰好就是小天体/SBDB stratum。

Batch 03 还加入了一个重要的科学审计案例：Mimas 的老式“冻结、无活动”直觉与 2024 Nature 的年轻全球海洋结果并存。仓库不把旧来源删除，而是记为 **temporal supersession**：新证据更新了内部结构判断，但老来源对“表面几乎无活动”的描述仍然有价值。

## 当前 gate

1. live JPL SBDB：16 个小/边界天体；
2. live SBDB/Horizons：5 个矮行星轨道；
3. 继续扫描 139 个已编码单元的 source conflict；
4. 完成小天体证据层；
5. **之后**才冻结 fsQCA calibration。

**仍未查看任何 QCA solution。**
