# ARIS4C022 · Planetary Taxonomy × fsQCA

把“什么算行星 / 矮行星 / 卫星 / 小天体”写成可检验的构型分类问题。火星仍是正对照，不是分类悬案。

## 当前数据底座

- 50 个冻结案例。
- `raw_physical_core_v0.1.csv`：34/50 有 JPL 核心物理数据。
- `orbital_geometry_v0.2.csv`：8 行星 JPL approximate elements；5 矮行星 derived-a；21 卫星 JPL Mean Elements；16 小天体数值层待 SBDB。
- `derived_physics_v0.2.csv`：34 个案例已有重力、逃逸速度、密度诊断和太阳环境。
- `evidence_state_v0.6.csv`：188/300 个证据状态完成，composition evidence-state **50/50**。
- `SOURCE_REGISTRY.md`：全部 evidence key 可在当前版本解析。
- `SOURCE_CONFLICT_AUDIT.md`：4 个差异案例已 adjudicate，0 个 unresolved conflict。

## M2 已经冻结，但还不能跑

在没有查看任何 QCA 结果的情况下，主 M2 固定为 5 个非定义性条件族：

1. **SCALE** → escape velocity
2. **BULK_MATERIAL** → density（物质状态 proxy，不等于“真实组成”）
3. **ATMOSPHERE_RETENTION** → atmosphere evidence
4. **INTERNAL_ORGANIZATION** → differentiation evidence
5. **SOLAR_ENERGY** → relative insolation

Pilot-0 原来的 INTERNAL_ACTIVITY 被提前移到 sensitivity，因为“地质活动”对固态天体和气态巨行星并不具有同一测量语义。

同时明确禁止把 direct-Sun orbit、satellite status、cleared neighborhood、Margot Π、Soter μ、roundness 等定义/动力学标签偷偷放回 M2。

## Readiness audit

当前五条件完整案例只有 **19/50**：

- planets 8/8
- dwarf planets 2/5
- satellites 9/21
- small/boundary bodies 0/16

所以当前结论是：**FAIL — not calibration-ready**。

冻结的最低门槛是：
- 每个主条件 >=40/50 substantive values；
- 五条件完整案例 >=35/50；
- 完整 strata 至少 8 planets / 4 dwarfs / 12 satellites / 10 small bodies。

这一步的意义是防止后面看到结果不好再删变量、换阈值、缩样本。

## 下一步

只补 readiness-critical 缺口：

1. live JPL SBDB 16-case numeric snapshot；
2. 替换 5 个矮行星 derived-a；
3. atmosphere 从 25 substantive cases 提到 >=40；
4. differentiation 从 32 提到 >=40；
5. 达到 complete-case / strata gate；
6. 然后冻结 calibration anchors；
7. **再第一次看 QCA 结果。**

**目前 calibration、truth table、consistency、PRI、coverage、solution 全部仍未查看。**
