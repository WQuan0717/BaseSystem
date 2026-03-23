---
name: se-context
description: Manage project context and state across phases. Provides persistent storage for project information, decisions, and progress tracking.
---

# Context Management for Software Engineering

Manage project context using file system for persistence across phases and sessions.

**Previous Skill**: Invoked by se-lifecycle after each phase completion

**Next Skill**: Returns to se-lifecycle for next phase transition

## Core Principles

### 1. Persistence
- Store context in files, not memory
- Survive across agent sessions
- Version control friendly

### 2. Structured Data
- JSON for machine-readable data
- Markdown for human-readable logs
- Clear schema and conventions

### 3. Incremental Updates
- Update context after each phase
- Append to logs, don't overwrite
- Track history and changes

## File Structure

```
docs/context/
├── project_state.json      # 项目状态（机器可读）
├── decisions.md            # 决策记录（人工可读）
├── progress.md             # 进度跟踪（人工可读）
└── history/                # 历史记录
    ├── state_2025-01-01.json
    ├── state_2025-01-02.json
    └── ...
```

## Project State (project_state.json)

### Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["project_name", "current_phase", "last_updated"],
  "properties": {
    "project_name": {
      "type": "string",
      "description": "项目名称"
    },
    "project_type": {
      "type": "string",
      "enum": ["web_app", "mobile_app", "desktop_app", "ai_system", "api_service", "other"],
      "description": "项目类型"
    },
    "project_description": {
      "type": "string",
      "description": "项目简短描述"
    },
    "current_phase": {
      "type": "string",
      "enum": ["init", "requirements", "architecture", "design", "development", "testing", "deployment", "completed"],
      "description": "当前阶段"
    },
    "completed_phases": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["init", "requirements", "architecture", "design", "development", "testing", "deployment"]
      },
      "description": "已完成阶段"
    },
    "pending_phases": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["requirements", "architecture", "design", "development", "testing", "deployment", "completed"]
      },
      "description": "待完成阶段"
    },
    "completion_percentage": {
      "type": "integer",
      "minimum": 0,
      "maximum": 100,
      "description": "完成百分比"
    },
    "complexity": {
      "type": "string",
      "enum": ["simple", "standard", "complex"],
      "description": "项目复杂度"
    },
    "mode": {
      "type": "string",
      "enum": ["fast", "standard", "full"],
      "description": "工作模式"
    },
    "tech_stack": {
      "type": "object",
      "properties": {
        "frontend": { "type": "string" },
        "backend": { "type": "string" },
        "database": { "type": "string" },
        "others": { "type": "array", "items": { "type": "string" } }
      }
    },
    "team_size": {
      "type": "integer",
      "description": "团队规模"
    },
    "start_date": {
      "type": "string",
      "format": "date",
      "description": "开始日期"
    },
    "target_date": {
      "type": "string",
      "format": "date",
      "description": "目标完成日期"
    },
    "last_updated": {
      "type": "string",
      "format": "date-time",
      "description": "最后更新时间"
    },
    "blocking_issues": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "description": { "type": "string" },
          "severity": { "type": "string", "enum": ["low", "medium", "high", "critical"] },
          "created_at": { "type": "string", "format": "date-time" },
          "status": { "type": "string", "enum": ["open", "in_progress", "resolved"] }
        }
      }
    },
    "next_action": {
      "type": "string",
      "description": "下一步行动"
    },
    "metadata": {
      "type": "object",
      "description": "额外元数据"
    }
  }
}
```

### Example

```json
{
  "project_name": "校园学习平台",
  "project_type": "web_app",
  "project_description": "基于Spring Boot的校园学习平台，支持博客和在线答题",
  "current_phase": "architecture",
  "completed_phases": ["init", "requirements"],
  "pending_phases": ["design", "development", "testing", "deployment"],
  "completion_percentage": 30,
  "complexity": "standard",
  "mode": "standard",
  "tech_stack": {
    "frontend": "Vue 3 + Element Plus",
    "backend": "Spring Boot 3.x",
    "database": "MySQL + Redis",
    "others": ["Elasticsearch"]
  },
  "team_size": 1,
  "start_date": "2025-01-01",
  "target_date": "2025-02-01",
  "last_updated": "2025-01-03T10:30:00Z",
  "blocking_issues": [],
  "next_action": "等待用户确认架构图",
  "metadata": {
    "created_by": "requirements-analyst",
    "last_phase_completed": "requirements"
  }
}
```

## Decision Log (decisions.md)

### Format

```markdown
# 决策记录

## 决策模板

### YYYY-MM-DD 决策标题
- **决策ID**: DEC-XXX
- **决策**: [具体决策内容]
- **原因**: [为什么做这个决策]
- **备选方案**: [考虑过但未选择的方案]
- **影响范围**: [影响哪些模块/功能]
- **决策人**: [谁做的决策]
- **状态**: [已确认/待确认/已变更]
- **相关文档**: [链接到相关文档]

---

## 实际决策记录

### 2025-01-01 技术栈选择
- **决策ID**: DEC-001
- **决策**: 使用 Vue 3 + Spring Boot 技术栈
- **原因**: 
  - 团队熟悉这两个框架
  - 生态丰富，文档完善
  - 适合快速开发
- **备选方案**: 
  - React + Node.js（学习成本高）
  - Angular + Java EE（过于重量级）
- **影响范围**: 整个项目架构
- **决策人**: system-architect
- **状态**: 已确认
- **相关文档**: Design.md

### 2025-01-02 数据库选择
- **决策ID**: DEC-002
- **决策**: 使用 MySQL + Redis
- **原因**:
  - MySQL 支持事务和复杂查询
  - Redis 提供缓存支持
  - 两者都是成熟稳定的技术
- **备选方案**:
  - MongoDB（不适合复杂关系查询）
  - PostgreSQL（团队不熟悉）
- **影响范围**: 数据存储层
- **决策人**: detailed-designer
- **状态**: 已确认
- **相关文档**: DetailedDesign.md

### 2025-01-03 认证方案
- **决策ID**: DEC-003
- **决策**: 使用 JWT + Redis Session 混合方案
- **原因**:
  - JWT 支持无状态认证
  - Redis 支持会话管理和登出
  - 兼顾性能和安全性
- **备选方案**:
  - 纯 JWT（无法主动失效）
  - 纯 Session（有状态，扩展性差）
- **影响范围**: 用户认证模块
- **决策人**: detailed-designer
- **状态**: 已确认
- **相关文档**: DetailedDesign.md
```

## Progress Tracking (progress.md)

### Format

```markdown
# 项目进度跟踪

## 项目概览
- **项目名称**: 校园学习平台
- **当前阶段**: 架构设计
- **总体进度**: 30%
- **开始日期**: 2025-01-01
- **目标日期**: 2025-02-01
- **剩余时间**: 29天

---

## 阶段详情

### ✅ 已完成

#### 阶段1: 项目启动 (2025-01-01)
- [x] 项目初始化
- [x] 需求初步沟通
- [x] 确定项目范围
- **耗时**: 1天
- **状态**: 按时完成

#### 阶段2: 需求分析 (2025-01-01 ~ 2025-01-02)
- [x] 需求收集与整理
- [x] 用户角色识别
- [x] 功能列表梳理
- [x] 用例图生成
- [x] 用户确认需求
- **耗时**: 2天
- **状态**: 按时完成
- **交付物**:
  - Requirement.md
  - docs/diagrams/usecase.mmd

---

### 🔄 进行中

#### 阶段3: 架构设计 (2025-01-03 ~ 进行中)
- [x] 技术选型
- [x] 架构图生成
- [ ] 等待用户确认
- [ ] ER图设计
- [ ] API设计
- **预计完成**: 2025-01-05
- **状态**: 等待确认
- **阻塞项**: 等待用户确认架构图

---

### ⏳ 待开始

#### 阶段4: 详细设计
- [ ] 数据库详细设计
- [ ] 类图设计
- [ ] 接口详细设计
- [ ] 流程图设计
- **预计开始**: 2025-01-06
- **预计完成**: 2025-01-08

#### 阶段5: 开发实现
- [ ] 环境搭建
- [ ] 垂直切片1: 用户认证
- [ ] 垂直切片2: 博客功能
- [ ] 垂直切片3: 答题功能
- **预计开始**: 2025-01-09
- **预计完成**: 2025-01-20

#### 阶段6: 测试验证
- [ ] 单元测试
- [ ] 集成测试
- [ ] 性能测试
- **预计开始**: 2025-01-21
- **预计完成**: 2025-01-25

#### 阶段7: 部署交付
- [ ] 部署文档编写
- [ ] 生产环境部署
- [ ] 用户培训
- **预计开始**: 2025-01-26
- **预计完成**: 2025-02-01

---

## 里程碑

| 里程碑 | 计划日期 | 实际日期 | 状态 |
|--------|---------|---------|------|
| 需求确认 | 2025-01-02 | 2025-01-02 | ✅ 完成 |
| 架构确认 | 2025-01-05 | - | 🔄 进行中 |
| 设计完成 | 2025-01-08 | - | ⏳ 待开始 |
| 开发完成 | 2025-01-20 | - | ⏳ 待开始 |
| 测试通过 | 2025-01-25 | - | ⏳ 待开始 |
| 正式上线 | 2025-02-01 | - | ⏳ 待开始 |

---

## 风险与问题

### 当前风险
| 风险 | 可能性 | 影响 | 应对措施 | 负责人 |
|------|--------|------|---------|--------|
| 需求变更 | 中 | 高 | 建立变更控制流程 | 项目经理 |
| 技术难点 | 低 | 中 | 提前进行技术预研 | 架构师 |

### 当前问题
- 无

---

## 最近更新

- 2025-01-03: 完成架构设计，等待用户确认
- 2025-01-02: 完成需求分析，用户已确认
- 2025-01-01: 项目启动
```

## API Reference

### Initialize Project

Create initial project state.

```python
def init_project(name: str, description: str, project_type: str) -> dict:
    """
    Initialize a new project with default state.
    
    Args:
        name: Project name
        description: Project description
        project_type: Type of project
        
    Returns:
        Initial project state dict
    """
    state = {
        "project_name": name,
        "project_type": project_type,
        "project_description": description,
        "current_phase": "init",
        "completed_phases": [],
        "pending_phases": ["requirements", "architecture", "design", "development", "testing", "deployment"],
        "completion_percentage": 0,
        "last_updated": datetime.now().isoformat(),
        "blocking_issues": [],
        "next_action": "开始需求分析"
    }
    save_state(state)
    return state
```

### Update Phase

Update project phase and progress.

```python
def update_phase(phase: str, status: str = "completed") -> dict:
    """
    Update project phase.

    Args:
        phase: Phase name (requirements, architecture, etc.)
        status: completed, in_progress, pending

    Returns:
        Updated project state
    """
    state = load_state()

    if status == "completed":
        if phase not in state["completed_phases"]:
            state["completed_phases"].append(phase)
        if phase in state["pending_phases"]:
            state["pending_phases"].remove(phase)

        # Auto-set next phase
        if state["pending_phases"]:
            state["current_phase"] = state["pending_phases"][0]
        else:
            state["current_phase"] = "completed"

        # After requirements completed, auto-generate skills usage plan
        if phase == "requirements":
            generate_skills_usage_plan()

    elif status == "in_progress":
        state["current_phase"] = phase

    # Calculate completion percentage
    total_phases = len(state["completed_phases"]) + len(state["pending_phases"])
    if total_phases > 0:
        state["completion_percentage"] = int(
            len(state["completed_phases"]) / total_phases * 100
        )

    state["last_updated"] = datetime.now().isoformat()
    save_state(state)
    return state
```

### Add Decision

Record a new decision.

```python
def add_decision(
    decision_id: str,
    title: str,
    decision: str,
    reason: str,
    alternatives: list,
    impact: str,
    decision_maker: str
) -> None:
    """
    Add a new decision to the decision log.
    
    Args:
        decision_id: Unique decision ID (e.g., DEC-001)
        title: Decision title
        decision: The decision made
        reason: Why this decision was made
        alternatives: Alternative options considered
        impact: Scope of impact
        decision_maker: Who made the decision
    """
    entry = f"""
### {datetime.now().strftime('%Y-%m-%d')} {title}
- **决策ID**: {decision_id}
- **决策**: {decision}
- **原因**: {reason}
- **备选方案**: {', '.join(alternatives)}
- **影响范围**: {impact}
- **决策人**: {decision_maker}
- **状态**: 已确认
- **相关文档**: [待补充]

"""
    append_to_file("docs/context/decisions.md", entry)
```

### Update Progress

Update progress tracking.

```python
def update_progress(
    phase: str,
    task: str,
    status: str,  # completed, in_progress, pending
    notes: str = ""
) -> None:
    """
    Update progress for a specific task.
    
    Args:
        phase: Phase name
        task: Task description
        status: Task status
        notes: Additional notes
    """
    # Implementation would update progress.md
    pass
```

### Get Context

Load full project context.

```python
def get_context() -> dict:
    """
    Load complete project context.
    
    Returns:
        Dict containing state, decisions, and progress
    """
    return {
        "state": load_state(),
        "decisions": load_decisions(),
        "progress": load_progress()
    }
```

## Integration with Other Skills

### With se-lifecycle
- Read state to determine current phase
- Update state after phase completion

### With se-requirements
- Initialize project after requirement collection
- Record requirement decisions

### With se-architecture
- Read requirements from context
- Record architecture decisions
- Update phase to "architecture"

### With se-development
- Read design from context
- Update progress during development
- Record implementation decisions

## Best Practices

1. **Always Update After Phase**: Each skill should update context after completion
2. **Record All Decisions**: Even small decisions should be recorded
3. **Keep Progress Updated**: Update progress.md regularly
4. **Version Control**: Commit context files with code
5. **Backup History**: Keep historical states in history/ directory

## Example Workflow

```python
# 1. Initialize project
init_project("校园学习平台", "学习博客和答题系统", "web_app")

# 2. After requirements phase
update_phase("requirements", "completed")
add_decision(
    "DEC-001",
    "技术栈选择",
    "使用 Vue 3 + Spring Boot",
    "团队熟悉，生态丰富",
    ["React + Node.js"],
    "整个项目架构",
    "system-architect"
)

# 3. During architecture phase
update_phase("architecture", "in_progress")
update_progress("architecture", "技术选型", "completed")
update_progress("architecture", "架构图设计", "in_progress")

# 4. Get full context
context = get_context()
print(f"当前阶段: {context['state']['current_phase']}")
print(f"完成度: {context['state']['completion_percentage']}%")
```
