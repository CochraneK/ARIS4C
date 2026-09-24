# ARIS4C022 · Planetary Taxonomy × fsQCA

把“什么算行星 / 矮行星 / 卫星 / 小天体”写成可检验的构型分类问题。按当前 IAU 太阳系定义，火星明确是行星，因此它在本研究中是正对照，不是悬案。

## 当前数据骨架

冻结样本仍为 50 个天体：8 行星、5 IAU 矮行星、21 天然卫星、16 小天体 / 边界案例。

当前 canonical layers：

- [raw_physical_core_v0.1.csv](data/raw_physical_core_v0.1.csv)：34/50 有 JPL 核心物理数据。
- [orbital_geometry_v0.2.csv](data/orbital_geometry_v0.2.csv)：
  - 8 行星使用 JPL J2000 approximate elements；Earth 明确标记为 Earth-Moon barycenter proxy；
  - 5 矮行星仍保留显式 derived a，等待 live SBDB/Horizons；
  - 21 卫星使用 JPL Mean Elements；
  - 16 小天体仍为 `NA_NOT_INGESTED`。
- [derived_physics_v0.2.csv](data/derived_physics_v0.2.csv)：34 个案例的重力、逃逸速度、密度诊断、太阳环境；13 个直接绕日案例的 Margot Π。
- [evidence_state_v0.1.csv](data/evidence_state_v0.1.csv)：50 个案例的组成/大气/分异/活动/海洋/潮汐证据矩阵，目前全部保持 `PENDING_REVIEW`。
- [EVIDENCE_STATE_PROTOCOL.md](process/EVIDENCE_STATE_PROTOCOL.md)：在看 QCA 结果之前冻结的证据编码规则。
- [ORBIT_SOURCE_HARDENING_AUDIT.md](data/ORBIT_SOURCE_HARDENING_AUDIT.md)：v0.1 period-derived a 与 v0.2 JPL planet elements 的差异审计。

## 模型分层

- M0：IAU 定义 benchmark，只校验管线，不称为“发现”。
- M1：Margot / Soter 动力学判据审计。
- M2：反循环 physical-signature model。
- M3：卫星边界。
- M4：探索 geophysical similarity fuzzy set，与官方 planet 类别严格分开。

主 QCA 仍控制在约 4–6 个核心条件。

## 当前 gate

1. 获取 16 个小天体的 live JPL SBDB raw JSON；
2. 用 SBDB/Horizons 替换 5 个矮行星剩余的 derived-a；
3. 按冻结协议盲编码 composition / atmosphere / differentiation / activity / ocean / tidal heating；
4. 完成 source-conflict audit；
5. **之后**才冻结 fsQCA calibration。

**到目前为止仍没有查看任何 QCA solution。**
