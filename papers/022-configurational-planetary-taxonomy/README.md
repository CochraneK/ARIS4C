# ARIS4C022 · Planetary Taxonomy × fsQCA

把“什么算行星 / 矮行星 / 卫星 / 小天体”写成可检验的构型分类问题。火星仍是正对照，不是分类悬案。

## 已冻结的 M2

主 M2 在看任何结果前固定为：

1. SCALE → escape velocity
2. BULK_MATERIAL → density proxy
3. ATMOSPHERE_RETENTION → atmosphere evidence
4. INTERNAL_ORGANIZATION → differentiation evidence
5. SOLAR_ENERGY → relative insolation

定义性/轨道层级/动力学判据不能进入 M2 条件。Geology/ocean/tidal heating 只进入预声明 sensitivity。

## 数据与证据

- 50 个冻结案例。
- physical / orbit / derived 数值层目前 34/50 完整到主量级。
- composition evidence-state 50/50。
- `evidence_state_v0.7.csv` 增加 readiness-targeted Batch 06。
- `M2_READINESS_GAP_MAP_v0.2.csv` 给每一个案例标出五条件具体缺口。

## Readiness：19 → 25

当前主条件 substantive coverage：

- SCALE 34/50
- BULK_MATERIAL 34/50
- ATMOSPHERE_RETENTION **28/50**
- INTERNAL_ORGANIZATION **36/50**
- SOLAR_ENERGY 34/50

五条件完整：**25/50**。

分层门槛：
- planets 8/8：PASS
- dwarf planets **4/5：PASS**
- satellites **13/21：PASS**
- small/boundary **0/16：FAIL**

因此现在已经不是“矮行星/卫星证据不足”在卡研究，真正主瓶颈是 **16 个 small/boundary 的 JPL SBDB numeric layer**。

## 当前 gate

1. 取得 16-case live SBDB physical/orbit snapshot；
2. 让至少 10 个 small/boundary 同时拥有五个主条件；
3. atmosphere 28 → >=40；
4. internal organization 36 → >=40；
5. complete cases 25 → >=35；
6. 然后冻结 calibration；
7. **再第一次看 QCA。**

目前 calibration / truth table / consistency / PRI / coverage / solution 仍全部未查看。
