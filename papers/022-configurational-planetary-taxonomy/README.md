# ARIS4C022 · Planetary Taxonomy × fsQCA

把“什么算行星 / 矮行星 / 卫星 / 小天体”写成可检验的构型分类问题。火星按当前 IAU 定义明确是行星，因此它是正对照，不是悬案。

## 当前 canonical 数据层

- 50 个冻结案例。
- `raw_physical_core_v0.1.csv`：34/50 JPL 核心物理数据。
- `orbital_geometry_v0.2.csv`：8 行星 JPL approximate elements；5 矮行星 derived-a；21 卫星 JPL Mean Elements；16 小天体待 SBDB。
- `derived_physics_v0.2.csv`：34 个案例的重力、逃逸速度、密度诊断和太阳环境；13 个直接绕日天体 Margot Π。
- `evidence_state_v0.3.csv`：两批盲编码后已有 **82/300** 个证据状态单元完成。
- `EVIDENCE_STATE_PROTOCOL.md` v0.2：已经明确“现存/持续地下海洋”与“远古 paleo-ocean”不能混为一类。

## Evidence batches

Batch 01：8 大行星 + Ceres + Pluto。

Batch 02：Moon、Io、Europa、Ganymede、Callisto、Enceladus、Titan、Triton、Charon。

当前覆盖：
- composition 19/50
- atmosphere 18/50
- differentiation 18/50
- geology 9/50
- present/persistent ocean 5/50
- tidal heating 13/50

这已经把最重要的反例结构带进数据：Ganymede/Titan 比 Mercury 大却仍是卫星；Europa/Enceladus 有强地下海洋证据；Io 是极端潮汐火山体；Charon 则是大质量比、古老重铺表面的边界案例。

## 当前 gate

1. live JPL SBDB：16 个小天体；
2. live SBDB/Horizons：5 个矮行星轨道；
3. 继续盲编码剩余 31 个天体；
4. source-conflict audit；
5. 然后才冻结 fsQCA calibration。

**仍未查看任何 QCA solution。**
