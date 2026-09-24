# ARIS4C022 · Planetary Taxonomy × fsQCA

把“什么算行星 / 矮行星 / 卫星 / 小天体”写成可检验的构型分类问题。火星仍是正对照，不是分类悬案。

## 当前 canonical 数据层

- 50 个冻结案例。
- `raw_physical_core_v0.1.csv`：34/50 JPL 核心物理数据。
- `orbital_geometry_v0.2.csv`：8 行星 JPL approximate elements；5 矮行星 derived-a；21 卫星 JPL Mean Elements；16 小天体数值层待 SBDB。
- `derived_physics_v0.2.csv`：34 个案例已有重力、逃逸速度、密度诊断和太阳环境。
- `evidence_state_v0.6.csv`：五批盲编码后 **188/300** 个证据状态完成。
- `SOURCE_REGISTRY.md`：当前版本完整解析全部 evidence source key。
- `SOURCE_CONFLICT_AUDIT.md` v0.2：4 个差异案例已完成 adjudication，目前 0 个 unresolved conflict。

## 一个重要里程碑：composition 50/50

现在 50 个案例的 composition **全部有 evidence state**，但不等于全部有确定组成。

- 直接/强约束：例如 Vesta、Bennu、Ryugu、Varuna。
- 模型推断：例如 Quaoar、Orcus、Salacia。
- 明确不确定：例如 Sedna、Gonggong、Varda、Ixion。
- 因此“50/50”表示证据状态完整，而不是人为把未知强行补齐。

Batch 05 还强化了一个核心规则：**表面有某种冰 ≠ 整个天体就是某种 bulk composition**。

## 当前 coverage

- composition **50/50**
- atmosphere 26/50
- differentiation 37/50
- geology 24/50
- present/persistent ocean 15/50
- tidal heating 36/50

## 当前 gate

剩余工作不再是机械把 300 格全部填满。下一步应：

1. 取得 live JPL SBDB 16-case numeric snapshot；
2. 替换 5 个矮行星 derived-a；
3. 从当前证据矩阵选择 M2 真正需要的 4–6 个正交 condition families；
4. 只补这些条件族所需的关键缺失；
5. 冻结 calibration anchors；
6. **之后**第一次查看 QCA 结果。

**仍未查看任何 QCA solution。**
