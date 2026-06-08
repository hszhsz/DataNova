# 开源数仓 / Data Agent 项目盘点

> 就像 Coding Agent 改写了软件研发，数据仓库建设也正在被 Agent 改写。本文盘点开源领域里值得关注的数仓 / Data Agent 项目，按它们在数仓建设链路中的定位分类。

## 一、数据工程 Agent（最接近"数仓建设"本身）

| 项目 | 定位 | 特点 |
|---|---|---|
| **Datus** ([Datus-ai/Datus-agent](https://github.com/Datus-ai/Datus-agent)) | 开源数据工程 Agent，类 Claude Code 的 CLI SQL 客户端 | 把数据工程从"建表+管道"转向"交付带领域上下文的 Agent"；构建可演进的 Context Layer（schema 元数据、参考 SQL、语义模型、指标、领域知识），支持 Plan Mode、Subagent 打包、MetricFlow 语义层、BIRD/Spider 2.0 评测 |
| **agentic-data-engineering 类项目** ([GitHub Topic](https://github.com/topics/agentic-data-engineering)) | 面向 dbt/SQL/云数仓的 agentic 数据工程框架 | 聚集了一批"100+ 工具、覆盖多种数仓、AI 驱动"的 CLI 型数据工程 Agent |

## 二、上下文层 / 语义层（让 Agent 能"读懂数仓"的底座）

| 项目 | 定位 | 特点 |
|---|---|---|
| **Wren AI** ([Canner/WrenAI](https://github.com/Canner/WrenAI)) | 面向业务数据的开源 Context Layer | 给 Agent 补上 schema 之外的东西：业务语义、示例、记忆、治理；agent-driven 设计，可被 Claude Code、Codex 等编码 Agent 直接驱动 |
| **Bonnard / ktx 等** ([semantic-layer Topic](https://github.com/topics/semantic-layer)) | 可执行的数据语义/上下文层 | 让 Claude Code、Codex 等通过 MCP + skills + memory + 语义层准确查数 |

> 这一类很关键——数仓 Agent 表现好坏几乎完全取决于上下文质量，所以"语义层/上下文层"本身正成为开源热点。

## 三、Text-to-SQL / Agentic Analytics（从"查询"切入，向建模延伸）

| 项目 | 定位 | 特点 |
|---|---|---|
| **Vanna** ([vanna-ai/vanna](https://github.com/vanna-ai/vanna)) | 开源 Text-to-SQL，通过 Agentic Retrieval 生成 SQL | 2.0 重写，强调用户级权限过滤、内置聊天组件、生产化部署 |
| **nao** | 专为数据分析打造的开源 analytics agent | SQL/dbt/数仓原生，强调内置 context、评测与治理基础设施 |
| **Cube Analyst** 等 PoC | 基于语义层的对话式 BI Agent | 用 LLM 理解问题、探索语义层、构造结构化查询 |

## 四、生态/工具化方向（把现有数仓栈"Agent 友好化"）

- **dbt + AI / dbt MCP Server / dbt Agent Skills**：dbt 把数仓建设代码化，再通过 MCP server 和开源的 "Agent Skills" 让 AI 编码 Agent 能正确地在 dbt 项目里建模、写测试。

## 学术视角

arXiv 综述《LLM/Agent-as-Data-Analyst: A Survey》把这一方向归纳为五大设计目标：语义感知、多模态融合、自治管道、工具增强、开放世界任务支持，可作为体系化理解的参考。

---

## 小结

- 真正面向"数仓建设全链路"的开源 Agent，目前最有代表性的是 **Datus**（数据工程 Agent）和 **Wren AI**（上下文层）。
- 其余多数仍偏 **Text-to-SQL / Agentic Analytics**（查询侧），但都在向建模、治理延伸。
- 共同主线是：**上下文 / 语义层是数仓 Agent 的胜负手**。
