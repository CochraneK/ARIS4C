# ARIS4C022 · Planetary Taxonomy × fsQCA

把“什么算行星 / 矮行星 / 卫星 / 小天体”写成可检验的构型分类问题。按当前 IAU 太阳系定义，火星明确是行星，因此它在本研究中是正对照，不是悬案。

## Pilot-0 · case-frame freeze

已冻结 50 个太阳系天体：

- 8 行星
- 5 IAU 矮行星
- 21 天然卫星
- 16 小天体 / 分类边界案例

## Pilot-1 · raw/orbit/derived data spine

当前已形成三层可复现数据链：

1. [raw_physical_core_v0.1.csv](data/raw_physical_core_v0.1.csv)
   - 50/50 行已物化
   - 34/50 已有 JPL 核心物理值
   - 16 个小天体保持显式 `NA_NOT_INGESTED`

2. [orbital_geometry_v0.1.csv](data/orbital_geometry_v0.1.csv)
   - 21 个卫星采用 JPL Mean Elements：主天体半长轴、偏心率、倾角、周期、frame、epoch、ephemeris
   - 13 个直接绕日天体暂以 JPL 公转周期按 Kepler 三定律推导 heliocentric a，并明确标成 derived，而非伪装成 catalog raw value
   - 16 个小天体继续等待冻结的 JPL SBDB snapshot

3. [derived_physics_v0.1.csv](data/derived_physics_v0.1.csv)
   - 34 个案例：表面重力、逃逸速度、球形平均半径密度诊断、太阳距离、相对辐照
   - 13 个直接绕日天体：Margot Π
   - 卫星不错误套用 Margot Π

另见 [MISSINGNESS_AUDIT.md](data/MISSINGNESS_AUDIT.md)。

## 模型分层

- M0：IAU 定义 benchmark，只做管线校验，不称为“发现”。
- M1：Margot / Soter 动力学判据的定量审计。
- M2：反循环模型，只看尺度、组成、大气保持、内部活动、太阳能量环境等非定义性物理特征。
- M3：卫星边界，重点看 Ganymede、Titan、Triton、Charon 等“物理上很像行星但轨道层级不同”的案例。
- M4：探索 geophysical similarity fuzzy set，但与官方 planet 类别严格分开。

主 QCA 仍控制在约 4–6 个核心条件；其余变量只进入替代指标与敏感性分析。

## 当前 gate

先完成 16 个小天体的 JPL SBDB 原始快照，再冻结 composition / atmosphere / internal activity 等证据状态层；随后才允许冻结 fsQCA calibration anchors。

**还没有查看任何 QCA solution。**
