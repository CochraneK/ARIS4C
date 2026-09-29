# SPOKE-SAFE 实验代码

```
experiments/
├── EXPERIMENT_TRACKER.md     ← 实验总追踪（这个文件）
└── e1_adv_avh_corpus/        ← E1: 对抗语料库
    ├── generate_corpus.py     ← 语料生成脚本 (S0-S5)
    ├── e2_assertiveness_scorer.py  ← E2: 打分器 (已写好，待运行)
    ├── adv_avh_corpus.jsonl   ← 语料数据 (实时追加)
    └── assertiveness_scores.jsonl  ← 评分数据 (E2产出)
```

### 运行顺序

1. ✅ E1: `python generate_corpus.py` → 生成 500+ 语料  
2. ⏳ E2: `python e2_assertiveness_scorer.py` → 打分器  
3. ⏳ E3: Silent Override 守卫 → Python 拦截逻辑  
4. ⏳ E4: 安全-疗效权衡 → 分析脚本  
5. ⏳ E5: 打包 → 论文资产
