# ARIS4C022 · Planetary Taxonomy × fsQCA

把“什么算行星 / 矮行星 / 卫星 / 小天体”写成可检验的构型分类问题。按当前 IAU 太阳系定义，火星明确是行星，因此它在本研究中是正对照，不是悬案。

## Pilot-0

已冻结 50 个太阳系天体：8 行星、5 IAU 矮行星、21 天然卫星、16 小天体/边界案例。

核心文件：
- [case_frame_v0.1.csv](data/case_frame_v0.1.csv)
- [DATA_DICTIONARY.md](data/DATA_DICTIONARY.md)
- [CASE_FRAME_FREEZE.md](process/CASE_FRAME_FREEZE.md)
- [MODEL_LADDER.md](process/MODEL_LADDER.md)
- [VARIABLES_AND_CALIBRATION.md](process/VARIABLES_AND_CALIBRATION.md)

## 模型分层

- M0：IAU 定义 benchmark，只做管线校验，不称为“发现”。
- M1：Margot / Soter 动力学判据的定量审计。
- M2：反循环模型，只看质量/尺度、组成、气体保持、内部活动、太阳能量环境等非定义性物理特征。
- M3：卫星边界，重点看 Ganymede、Titan、Triton、Charon 等“很像行星但轨道层级不同”的案例。
- M4：探索 geophysical similarity fuzzy set，但与官方 planet 类别严格分开。

主 QCA 控制在约 4–6 个核心条件；其他变量进入替代指标与敏感性分析。

## 下一 gate

为 50 个案例建立带字段级 provenance 的 IAU/NASA/JPL 原始物理与轨道矩阵，并按论文原式实现 Margot/Soter 动力学指标。

## 首批真实数据

已把 NASA NSSDC 的 10 个主要天体比较表作为 provenance seed 落盘：八大行星 + Moon + Pluto。它不是最终 50-body 矩阵，而是先验证单位、轨道参照系和派生公式。

这一小步已经抓出一个很重要的问题：NASA 紧凑表里的 Diameter 是**赤道直径**，不能默认当作平均体积半径去重算巨行星密度；Gravity 也包含自转效应，巨行星按 1-bar 层定义。因此 022 不会把“网页上几个数字”直接拼成看似精确的统一矩阵。

见：
- `data/raw/nasa_nssdc_planetary_fact_sheet_seed.csv`
- `process/NASA_SEED_QC.md`
- `process/SOURCE_INGESTION_PLAN.md`
