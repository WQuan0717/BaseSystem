# Trae 子智能体配置

> 这些配置文件用于在 Trae 中手动创建子智能体，支持并行执行任务。

---

## 📋 什么是子智能体？

子智能体（Subagent）是 Trae 中的**专用智能体**，可以：
- 并行执行独立任务
- 专注于特定领域（如测试、文档）
- 每个子智能体有独立的 40 个 MCP Tools 配额

---

## 🎯 何时使用子智能体？

### ✅ 适用场景（并行）

1. **测试验证** - QA Engineer 与开发并行
   - SOLO Coder 开发功能
   - QA Engineer 并行编写测试用例
   
2. **文档生成** - Technical Writer 与开发并行
   - SOLO Coder 实现代码
   - Technical Writer 并行生成文档

3. **MCP Tools 扩展** - 突破 40 个工具限制
   - 每个子智能体有独立的 40 个工具配额
   - SOLO Coder 可以间接使用更多工具

### ❌ 不适用场景（串行，交给 SOLO Coder）

以下阶段**不需要**子智能体，由 SOLO Coder 调用 Skills 完成：

| 阶段 | 负责 | 原因 |
|------|------|------|
| 需求分析 | SOLO Coder + se-requirements | 强逻辑，需要与用户频繁交互 |
| 架构设计 | SOLO Coder + se-architecture | 强逻辑，需要整体把控 |
| 详细设计 | SOLO Coder + se-detailed-design | 强逻辑，承上启下 |
| 功能开发 | SOLO Coder + se-development | 核心实现，不宜分离 |

---

## 📦 可用子智能体

### 可并行的子智能体（2 个）

| Agent | 用途 | 配置文档 | MCP Tools |
|-------|------|---------|-----------|
| **QA Engineer** | 测试专家 | `qa-engineer.md` | 12 个 |
| **Technical Writer** | 文档专家 | `technical-writer.md` | 12 个 |

### 工具型 Agent（1 个）

| Agent | 用途 | 配置文档 | MCP Tools |
|-------|------|---------|-----------|
| **Agentic Optimizer** | Agent 设计优化 | `agentic-optimizer.md` | 11 个 |

> 💡 **注意**：Agentic Optimizer 不是业务 Agent，而是用于设计和优化其他 Agent 的工具。

---

## 📚 已整合到 Skills 的 Agent

以下 Agent 已整合到对应的 se-* Skills 中，由 SOLO Coder 在适当阶段调用：

| 原 Agent | 整合到 Skill | 说明 |
|---------|-------------|------|
| Requirements Analyst | `se-requirements` | 需求分析方法、5W1H 框架、提问技巧 |
| System Architect | `se-architecture` | 技术选型、开源发现、风险评估 |
| Detailed Designer | `se-detailed-design` | 数据库设计、API 规格、目录结构 |
| Full-stack Engineer | `se-development` | 垂直切片开发、单元测试、代码规范 |

> 💡 **优势**：整合到 Skills 后，SOLO Coder 可以直接调用，无需创建子智能体，减少协调成本。

---

## 🔧 如何创建子智能体

### 方式 1：在 Trae 中手动创建

1. 打开 Trae 设置
2. 进入 "Subagents" 配置
3. 点击 "Create New Subagent"
4. 复制对应配置文件的**三段式内容**：
   - ## 提示词
   - ## 何时调用
   - ## 需要启用的 MCP 工具
5. 保存并启用

### 方式 2：使用 Agentic Optimizer

```bash
# 在 Trae 中调用
invoke agentic-optimizer
```

让 Agentic Optimizer 帮你设计和优化新的 Agent 配置。

---

## 📊 并行工作流示例

### 场景：开发用户管理功能

```
SOLO Coder（主线 - 串行）
├── 需求分析（se-requirements）
├── 架构设计（se-architecture）
├── 详细设计（se-detailed-design）
└── 功能开发（se-development）
    
QA Engineer（并行）
├── 阅读 API 设计
├── 编写测试用例
└── 执行测试验证

Technical Writer（并行）
├── 阅读代码
├── 生成 API 文档
└── 编写用户指南
```

**时间线**：
```
迭代 1: [SOLO: 开发] ──────┐
迭代 2: [SOLO: 开发] ──┬──┼──>
                       │  │
                       │  └─> [QA: 测试迭代 1]
                       │
                       └─────> [Writer: 文档迭代 1]
```

### MCP Tools 分配

```
SOLO Coder:
├── se-lifecycle (工作流决策)
├── se-context (状态管理)
├── se-requirements (需求分析)
├── se-architecture (架构设计)
├── se-detailed-design (详细设计)
├── se-development (开发实现)
├── se-diagram (图表生成)
└── 其他开发工具

QA Engineer:
├── se-testing (测试验证)
├── se-context (读取状态)
└── webapp-testing (Playwright)

Technical Writer:
├── se-documentation (文档生成)
├── se-context (读取状态)
└── docx/pdf (文档格式)
```

---

## 🎯 最佳实践

### 1. 子智能体数量

- **推荐**：1-2 个（QA + Writer）
- **最多**：3 个（+ Optimizer）
- **避免**：过多子智能体导致协调困难

### 2. 通信机制

- **共享状态**：通过 se-context 同步信息
- **定期同步**：每个迭代结束后同步
- **避免**：频繁打断子智能体

### 3. MCP Tools 分配

```
SOLO Coder:
├── se-* skills (核心)
├── mcp-builder (MCP 开发)
└── 其他开发工具

QA Engineer:
├── se-testing
├── webapp-testing
└── Playwright 工具

Technical Writer:
├── se-documentation
├── docx
└── pdf 工具
```

---

## ⚠️ 注意事项

1. **上下文隔离** - 子智能体之间不共享上下文
   - 必须通过 se-context 同步状态
   - 避免直接依赖其他子智能体的输出

2. **任务独立性** - 确保子智能体任务相对独立
   - 避免强依赖关系
   - 减少协调成本

3. **成本控制** - 子智能体会增加 Token 消耗
   - 仅在必要时使用
   - 定期清理不需要的子智能体

---

## 📚 相关文档

- `.trae/rules/project_rules.md` - 工作流规则
- `.trae/skills/se-lifecycle/SKILL.md` - 工作流决策
- `.trae/skills/se-context/SKILL.md` - 状态管理

---

*这些配置文件仅供参考，实际创建需要在 Trae 设置中手动配置*  
*版本：v1.0.0*
