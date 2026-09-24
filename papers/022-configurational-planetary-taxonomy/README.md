# ARIS4C022 · Planetary Taxonomy × fsQCA

把“什么算行星 / 矮行星 / 卫星 / 小天体”写成可检验的构型分类问题。火星仍是正对照，不是分类悬案。

## 当前 canonical 数据层

- 50 个冻结案例。
- `raw_physical_core_v0.1.csv`：34/50 JPL 核心物理数据。
- `orbital_geometry_v0.2.csv`：8 行星 JPL approximate elements；5 矮行星 derived-a；21 卫星 JPL Mean Elements；16 小天体数值层待 SBDB。
- `derived_physics_v0.2.csv`：34 个案例已有重力、逃逸速度、密度诊断和太阳环境。
- `evidence_state_v0.5.csv`：四批盲编码后 **157/300** 个证据状态完成。
- `SOURCE_CONFLICT_AUDIT.md`：冲突/时间更新审计已启动。

## Evidence coverage

- composition 39/50
- atmosphere 25/50
- differentiation 29/50
- geology 24/50
- present/persistent ocean 15/50
- tidal heating 25/50

Batch 04 新增 Vesta、Eros、Bennu、Ryugu、Itokawa。

其中新增 `CARBONACEOUS_HYDRATED`，专门容纳 Bennu/Ryugu 这类返回样品显示含水矿物和古代水蚀变的碳质小天体；它们不能被误写成 Ceres/冰卫星意义上的 `ROCK_ICE_MIXED`，更不能因为母体曾有液态水就自动得到“现存地下海洋”。

现在 16 个 small/boundary cases 中已有 5 个进入高置信证据层，剩余 11 个主要是 Pallas/Hygiea/Interamnia 和远端 TNO 边界组。

## 当前 gate

1. 继续剩余 11 个小/边界天体证据编码；
2. live JPL SBDB：16 个小天体数值快照；
3. live SBDB/Horizons：5 个矮行星轨道替换；
4. 完整 source-conflict audit；
5. **之后**冻结 fsQCA calibration。

**仍未查看任何 QCA solution。**
