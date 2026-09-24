# ARIS4C022 · Planetary Taxonomy × fsQCA

把“什么算行星 / 矮行星 / 卫星 / 小天体”写成可检验的构型分类问题。火星按当前 IAU 定义明确是行星，因此它是正对照，不是悬案。

## 当前 canonical 数据层

- 50 个冻结案例：8 行星 + 5 矮行星 + 21 卫星 + 16 小/边界天体。
- `raw_physical_core_v0.1.csv`：34/50 有 JPL 核心物理数据。
- `orbital_geometry_v0.2.csv`：8 行星 JPL approximate elements；5 矮行星 derived-a；21 卫星 JPL Mean Elements；16 小天体待 SBDB。
- `derived_physics_v0.2.csv`：34 个案例的重力、逃逸速度、密度诊断和太阳环境；13 个直接绕日天体的 Margot Π。
- `evidence_state_v0.2.csv`：第一批 10 个锚点已开始盲编码，41/300 个证据状态单元不再是 pending。
- `EVIDENCE_STATE_PROTOCOL.md`：编码规则在看 QCA 之前冻结。
- `EVIDENCE_CODING_AUDIT.md`：记录当前证据覆盖和保守决策。

## Anchor batch 01

对象：Mercury、Venus、Earth、Mars、Jupiter、Saturn、Uranus、Neptune、Ceres、Pluto。

已编码：
- composition 10/50
- atmosphere 10/50
- differentiation 10/50
- geological activity 1/50
- direct-Sun tidal heating N/A 10/50

没有为了提高完整率而把未知写成“没有”。Ocean、更多 geology 以及卫星 tidal heating 会使用更专门的任务/论文来源。

## 当前 gate

1. live JPL SBDB：16 个小天体；
2. live SBDB/Horizons：5 个矮行星轨道；
3. 继续盲编码 40 个天体，优先大卫星和边界天体；
4. source-conflict audit；
5. 然后才冻结 fsQCA calibration。

**仍未查看任何 QCA solution。**
