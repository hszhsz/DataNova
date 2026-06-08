# 贡献指南 (Contributing to DataNova)

感谢你对 DataNova 的关注！本项目用于探索"企业 Data Agent / 数仓 Agent 化"的建设过程，欢迎以多种形式参与。

## 你可以贡献什么

- **文档**：补充开源项目盘点、最佳实践、案例分析（放在 `docs/`）。
- **方案**：架构设计、Agent 设计、评测方法的讨论与改进。
- **代码**：未来 `src/` 下的探索性实现（如问数 Agent、语义层适配器等）。
- **Issue**：提出问题、想法、纠错。

## 提交流程

1. Fork 本仓库并新建分支：`git checkout -b feature/your-topic`
2. 提交改动，遵循下方 commit 规范。
3. 发起 Pull Request，描述清楚动机与改动内容。

## Commit 规范

采用 [Conventional Commits](https://www.conventionalcommits.org/) 风格：

| 前缀 | 含义 |
|---|---|
| `feat:` | 新功能 |
| `fix:` | 修复 |
| `docs:` | 文档 |
| `refactor:` | 重构 |
| `chore:` | 杂项 |

示例：`docs: add 语义层最佳实践`

## 文档风格

- Markdown 编写，结论前置。
- 图表优先用 Mermaid 代码块（GitHub 可直接渲染）。
- 引用外部资料时给出来源链接。

## 行为准则

请保持友善、尊重、建设性的讨论氛围。

## License

贡献的内容默认以本仓库的 [MIT License](LICENSE) 授权。
