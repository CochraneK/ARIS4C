# ARIS4C022 · Planetary Taxonomy × fsQCA

火星仍是正对照，不是分类悬案。主 M2 在任何结果曝光前固定为五个非定义性条件：escape velocity、density proxy、atmosphere evidence、differentiation evidence、relative insolation。

## Readiness 已经 PASS

优先 10 个 small/boundary 数值锚点已经进入新数据层：

Vesta · Pallas · Hygiea · Interamnia · Eros · Bennu · Ryugu · Itokawa · Quaoar · Orcus

当前主条件 substantive coverage：

- SCALE **44/50**
- BULK_MATERIAL **44/50**
- ATMOSPHERE_RETENTION **41/50**
- INTERNAL_ORGANIZATION **40/50**
- SOLAR_ENERGY **44/50**
- 五条件完整 **37/50**

完整 strata：
- planets 8/8
- dwarf planets 4/5
- satellites 15/21
- small/boundary **10/16**

全部超过此前已经冻结的门槛，因此 **M2 readiness = PASS**。

## 这次没有为了过门槛偷改规则

JPL SBDB live object API 在当前执行环境不可读，所以在输入替代来源前，先冻结了 `NUMERIC_ACQUISITION_ADDENDUM.md`：

- 允许 mission/PDS、JPL static orbit、同行评审动力学/掩星；
- 允许明确标记的 source-derived 值；
- 禁止百科/社区值补表；
- 禁止把 binary system mass 静默当成 primary mass；
- 禁止看到结果以后再改 readiness 门槛。

因此 Quaoar 和 Orcus 都显式做了 companion mass correction。

## 当前 canonical 数据

- `raw_physical_core_v0.2.csv`
- `orbital_geometry_v0.3.csv`
- `derived_physics_v0.3.csv`
- `evidence_state_v1.0.csv`
- `NUMERIC_ACQUISITION_AUDIT.md`
- `M2_READINESS_AUDIT_v1.0.md`

## 下一步

**冻结 calibration anchors。**

这一步仍然不能看 truth table、consistency、PRI、coverage 或 QCA solution。只有 calibration 完全冻结后，才允许第一次真正运行 M2。

所以现在的状态不是“研究完成”，而是终于从数据/证据准备阶段进入正式分析前的最后一道门。
