# 项目规则

> Trae 平台基础规则，定义核心工作流程和 Skills 调用规范。

## ⚠️ MANDATORY FIRST STEP

**在开始任何工作之前，AI 必须：**

```
1. 读取 se-lifecycle/SKILL.md - 了解完整工作流程
2. 读取 se-spec-mode/SKILL.md - 需求分析模式
3. 读取 se-development/WORKFLOW.md - 开发流程
4. 基于以上创建 todo 列表
```

❌ **不读取 = 不知道流程 = 无法正确执行**

---

## 🎯 核心原则

### 1. 项目启动流程

```
用户需求
    ↓
┌─────────────────────────────────────────────────────┐
│ 步骤 1: 读取 Skills                                │
│ - se-lifecycle/SKILL.md                           │
│ - se-spec-mode/SKILL.md                           │
│ - se-development/WORKFLOW.md                      │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│ 步骤 2: 创建 todo 列表                            │
│ - 基于 Skills 创建任务列表                         │
│ - 按阶段顺序执行                                   │
└─────────────────────────────────────────────────────┘
    ↓
执行
```

### 2. 完整工作流程

```
┌─────────────────────────────────────────────────────┐
│ PHASE 0: Spec Mode                                │
│ invoke se-spec-mode                                │
│ → spec.md + tasks.md + checklist.md               │
│ → 用户确认后才能继续                               │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│ PHASE 1: Frontend UI/UX + Mock                   │
│ invoke se-spec-mode → se-development/PHASE1        │
│ → 前端 + Mock 数据                                 │
│ → QA Engineer 评审 UI/UX                          │
│ → 用户验收 + 说"继续开发"                          │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│ PHASE 2: Backend Implementation                   │
│ invoke se-development/PHASE2                      │
│ → 后端功能逐个实现                                 │
│ → 每个功能 E2E 测试 + 回归测试                     │
│ → QA Engineer 验证                                │
│ → 用户验收 + 说"继续开发"                          │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│ PHASE 3: Handoff + Documentation                  │
│ invoke se-development/PHASE3                      │
│ → 测试账号准备                                     │
│ → README + API + DEPLOYMENT                       │
│ → 用户最终验收                                     │
└─────────────────────────────────────────────────────┘
```

---

## 📋 Skills 清单

| Skill | 用途 | 调用时机 |
|-------|------|----------|
| `se-lifecycle` | 工作流程总览 | 项目开始时 |
| `se-spec-mode` | 需求分析与任务分解 | Spec 阶段 |
| `se-context` | 项目状态管理 | 阶段切换时 |
| `se-requirements` | 详细需求分析 | Requirements 阶段 |
| `se-architecture` | 架构设计 | Architecture 阶段 |
| `se-detailed-design` | 详细设计 | Detailed Design 阶段 |
| `se-development/PHASE1` | 前端 + Mock | Development 阶段 1 |
| `se-development/PHASE2` | 后端实现 | Development 阶段 2 |
| `se-development/PHASE3` | 交付文档 | Development 阶段 3 |
| `qa-engineer` | 独立测试 | 每个 phase 结束后 |
| `se-documentation` | 文档生成 | 项目完成前 |

---

## 🤖 Agent 模式

| 模式 | 使用场景 |
|------|----------|
| **agent** (默认) | 单一任务，快速实现 |
| **plan** | 多步骤，需要规划 |
| **spec** | 复杂需求，需要详细设计 |

---

## ⚠️ 强制规则

### AI 不得：

- ❌ 不读取 Skills 就开始工作
- ❌ 跳过任何阶段
- ❌ 跳过 QA 测试
- ❌ 跳过用户验收
- ❌ 自己判断"完成了"

### AI 必须：

- ✅ 先读取 se-lifecycle
- ✅ 按阶段顺序执行
- ✅ 每个阶段通过检查点
- ✅ 用户说"继续开发"才能进下一阶段

---

## 💡 最佳实践

### 阶段执行

1. **完成当前阶段的所有检查点**
2. **调用 QA Engineer 进行测试**
3. **等待用户确认**
4. **才能进入下一阶段**

### 检查点示例

```
PHASE 1 检查点：
- [ ] 设计系统已记录
- [ ] 所有前端页面存在
- [ ] Mock 数据结构存在
- [ ] 前端可独立运行
- [ ] QA Engineer 批准 UI/UX
- [ ] 用户说"继续开发"
```

---

*详细实践文档在各 Skills 中*
