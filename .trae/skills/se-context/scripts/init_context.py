#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
初始化项目状态
创建 docs/context/ 目录结构和初始状态文件
同时生成 skills_rules.md 技能使用规则
"""

import json
import os
from datetime import datetime
from pathlib import Path


SKILLS_RULES_TEMPLATE = """# {project_name} - Skills 使用规则

> 本项目专用的 Skills 使用规范，基于 BaseSystem 规则自动生成。

## 🎯 核心原则

### 必要 vs 可选

- **必要 Skills** - 每个项目必须使用的核心 Skills
- **可选 Skills** - 根据具体需求灵活选用，不是每个项目都必须

### 动态扩展

在需求分析阶段完成后，必须：
1. 分析项目需求，识别需要哪些额外 Skills
2. 制定详细的 Skills 使用计划
3. 记录在项目上下文中，作为执行指南

---

## 📋 必要 Skills（所有项目必须使用）

| 阶段 | Skill | 说明 |
|------|-------|------|
| 🌐 全局 | `se-lifecycle` | 工作流程协调，必须首先调用 |
| 📝 需求 | `se-requirements` | 结构化需求分析 |
| 🏗️ 架构 | `se-architecture` | 系统架构设计 |
| 📐 详细设计 | `se-detailed-design` | 数据库和 API 设计 |
| 💻 开发 | `se-development` | 代码实现 |
| 🧪 测试 | `webapp-testing` | 测试验证 |
| 📖 文档 | `se-documentation` | 文档生成 |
| � 画图 | `se-diagram` | 图表生成（各阶段需要时） |
| �💾 状态 | `se-context` | 状态管理（每个阶段后） |

---

## 🔧 可选 Skills（根据需求选用）

### 文档生成相关

| Skill | 适用场景 | 调用时机 |
|-------|----------|----------|
| `docx` | 需要生成 Word 文档 | 文档阶段 |
| `pdf` | 需要生成 PDF 或处理 PDF 表单 | 文档阶段 |
| `pptx` | 需要生成 PowerPoint | 文档阶段 |
| `xlsx` | 需要生成 Excel 电子表格 | 文档阶段 |

### 前端相关

| Skill | 适用场景 | 调用时机 |
|-------|----------|----------|
| `frontend-design` | 需要专业前端界面设计指导 | 开发阶段 |
| `ui-ux-pro-max` | 需要 UI/UX 设计参考 | 开发阶段 |

### 开发工具相关

| Skill | 适用场景 | 调用时机 |
|-------|----------|----------|
| `mcp-builder` | 需要构建 MCP Server 集成外部 API | 开发阶段 |
| `webapp-testing` | 需要 Web 应用自动化测试 | 测试阶段 |
| `web-artifacts-builder` | 需要构建复杂 Web UI 组件 | 开发阶段 |

### 创建与设计相关

| Skill | 适用场景 | 调用时机 |
|-------|----------|----------|
| `skill-creator` | 需要创建新的 Skill | 开发阶段 |
| `subagent-creator` | 需要创建新的子智能体 | 开发阶段 |
| `theme-factory` | 需要设计主题或样式 | 开发阶段 |
| `brand-guidelines` | 需要品牌设计指导 | 开发阶段 |
| `canvas-design` | 需要视觉设计 | 开发阶段 |
| `algorithmic-art` | 需要算法生成艺术 | 开发阶段 |

### 协作与沟通

| Skill | 适用场景 | 调用时机 |
|-------|----------|----------|
| `doc-coauthoring` | 需要协作写作 | 文档阶段 |
| `internal-comms` | 需要内部沟通文档 | 文档阶段 |

---

## 📊 决策流程

### 1. 项目启动时

```
检查所有可用 Skills
    ↓
识别必要 Skills（9 个）
    ↓
记录在项目上下文中
```

### 2. 需求分析完成后

```
分析需求文档
    ↓
识别技术领域（前端、文档、测试等）
    ↓
选择对应领域的可选 Skills
    ↓
更新项目上下文的 Skills 使用计划
```

### 3. 每个阶段开始时

```
查看项目上下文的 Skills 使用计划
    ↓
调用必要 Skill（必须）
    ↓
根据当前任务调用可选 Skills（按需）
    ↓
记录调用的 Skill 到阶段日志
```

---

## 💡 使用策略

### 何时调用可选 Skills？

- **需要生成特定格式文档** → 调用对应文档类 Skill
  - 例如：需要生成 Word 报告 → `docx`
  - 例如：需要生成 Excel 数据表 → `xlsx`

- **技术栈涉及特定领域** → 调用对应领域 Skill
  - 例如：需要 Web 界面 → `frontend-design`
  - 例如：需要外部 API 集成 → `mcp-builder`

- **遇到特定问题** → 调用问题解决类 Skill
  - 例如：Web 应用测试 → `webapp-testing`
  - 例如：需要创建新 Skill → `skill-creator`

### 何时不调用？

- **任务简单，核心 Skills 足够** → 不调用
- **领域不相关** → 不调用
- **时间紧迫，可后续补充** → 标记为待办，不阻塞

---

## 📝 记录要求

每次调用 Skill 后，必须在 `docs/context/skills_log.md` 中记录：

```markdown
## [日期时间] - [Skill 名称]

**阶段**: [当前阶段]
**触发原因**: [为什么调用这个 Skill]
**输入**: [调用前的状态/文档]
**输出**: [生成的文档/代码]
**效果评估**: [是否达到预期]
```

---

## 🔄 动态更新

项目进行中，如果发现新的需求或问题：

1. **重新评估可选 Skills** - 是否需要新的领域 Skill
2. **更新 Skills 使用计划** - 记录到项目上下文
3. **回溯调用** - 如果之前遗漏，及时补充

---

## 📚 参考文档

- 各 Skill 的 `SKILL.md` - 详细功能说明
- `project_rules.md` - 核心工作流程
- `se-lifecycle/SKILL.md` - 生命周期管理

---

*生成时间：{timestamp}*
*基于规则：.trae/rules/skills_rules.md*
"""


def generate_skills_rules(project_name: str):
    """生成项目技能使用规则"""
    skills_rules_path = ".trae/rules/skills_rules.md"

    skills_rules_content = SKILLS_RULES_TEMPLATE.format(
        project_name=project_name,
        timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    with open(skills_rules_path, "w", encoding="utf-8") as f:
        f.write(skills_rules_content)
    print(f"✓ 创建文件：{skills_rules_path}")


def init_context(project_name: str, project_type: str = "web_app"):
    """初始化项目上下文"""

    # 创建目录结构
    dirs = [
        "docs/context",
        "docs/context/history"
    ]

    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ 创建目录：{dir_path}")

    # 生成技能使用规则
    generate_skills_rules(project_name)

    # 初始化项目状态
    state = {
        "project_name": project_name,
        "project_type": project_type,
        "current_phase": "init",
        "completed_phases": [],
        "pending_phases": ["requirements", "architecture", "design", "development", "testing", "documentation"],
        "completion_percentage": 0,
        "tech_stack": {
            "frontend": "",
            "backend": "",
            "database": "",
            "others": []
        },
        "start_date": datetime.now().strftime("%Y-%m-%d"),
        "target_date": "",
        "last_updated": datetime.now().isoformat(),
        "blocking_issues": [],
        "next_action": "开始需求分析"
    }

    # 保存项目状态
    state_path = "docs/context/project_state.json"
    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(f"✓ 创建文件：{state_path}")

    # 备份历史
    history_path = f"docs/context/history/state_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.json"
    with open(history_path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(f"✓ 创建历史备份：{history_path}")

    print("\n✅ 项目上下文初始化完成!")
    return state


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("用法：python init_context.py <项目名称> [项目类型]")
        print("示例：python init_context.py 我的项目 web_app")
        sys.exit(1)

    project_name = sys.argv[1]
    project_type = sys.argv[2] if len(sys.argv) > 2 else "web_app"

    init_context(project_name, project_type)
