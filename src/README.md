# Source Code

本目录用于 DataNova 的探索性实现代码。

按"三层架构 + 七个 Agent"组织，规划如下（占位，随路线图逐步填充）：

```
src/
├── foundation/      # 底座层：元数据采集、语义层、可信指标
├── agents/          # 能力层：七个专业 Agent
│   ├── modeling/    # 建模 Agent
│   ├── query/       # 问数 Agent
│   ├── quality/     # 数据质量 Agent (DQC)
│   ├── lineage/     # 元数据 / 血缘 Agent
│   ├── metrics/     # 指标治理 Agent
│   ├── ops/         # 运维 / 排障 Agent
│   └── assets/      # 资产治理 Agent
├── orchestrator/    # 调度层：编排 Agent
└── eval/            # 评测框架：SQL 跑通率、数据准确率
```

> 详见 [ROADMAP](../ROADMAP.md)。当前处于 Phase 0（调研与选型），代码将随阶段推进逐步加入。
