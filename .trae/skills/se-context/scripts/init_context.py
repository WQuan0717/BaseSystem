#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
初始化项目状态
创建 docs/context/ 目录结构和初始状态文件
同时生成 SKILLS_USAGE.md 技能使用表
"""

import json
import os
from datetime import datetime
from pathlib import Path


def generate_skills_usage(project_name: str):
    """生成项目技能使用表"""
    skills_usage = f"""# {project_name} - Skills 使用表

> 本项目专用的 Skills 调用参考表，根据项目规则自动生成。

## 📋 工作流程

所有项目统一采用完整流程，由 subagent 自动判断、修改和推进：

```
需求分析 → 用例图 → 自动确认
架构设计 → 架构图+ER 图 → 自动确认
详细设计 → 类图 + 流程图 → 自动确认
迭代开发 → 垂直切片 → 自动验收
测试验证 → 测试报告 → 完成
```

## 🔧 Skills 调用规范

| 阶段 | 必须调用的 Skill | 调用时机 | 输出文档 |
|------|-----------------|----------|----------|
| 🌐 全局 | `se-lifecycle` | 项目开始 | 生命周期上下文 |
| 📝 需求 | `se-requirements` | 需要结构化需求 | Requirement.md |
| 🏗️ 架构 | `se-architecture` | 需求明确后 | Design.md |
| 📐 详细设计 | `se-detailed-design` | 架构确定后 | DetailedDesign.md |
| 💻 开发 | `se-development` | 详细设计后 | 代码 + 单元测试 |
| 🧪 测试 | `se-testing` | 开发完成后 | TestReport.md |
| 📖 文档 | `se-documentation` | 测试完成后 | README.md 等 |
| 📊 画图 | `se-diagram` | 各阶段需要图表时 | Mermaid 图表 |
| 💾 状态 | `se-context` | 每个阶段完成后 | 更新 project_state.json |

**重要**：每个阶段完成后，必须调用 `se-context` 更新项目状态！

## 📚 详细文档

- `se-lifecycle/SKILL.md` - 工作流程和阶段定义
- `se-requirements/SKILL.md` - 需求分析规范
- `se-architecture/SKILL.md` - 架构设计指南
- `se-detailed-design/SKILL.md` - 详细设计方法
- `se-development/SKILL.md` - 开发实现最佳实践
- `se-testing/SKILL.md` - 测试策略和用例设计
- `se-documentation/SKILL.md` - 文档生成标准
- `se-diagram/SKILL.md` - 图表生成教程
- `se-context/SKILL.md` - 状态管理规范

## 💡 使用提示

1. **项目启动时**：阅读 `se-lifecycle/SKILL.md` 了解完整流程
2. **每个阶段前**：查看对应 Skill 的 `SKILL.md` 了解详细规范
3. **需要图表时**：调用 `se-diagram`，提供图表类型和内容
4. **阶段完成后**：必须调用 `se-context` 更新状态

---

*生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*基于规则：.trae/rules/project_rules.md*
"""

    skills_usage_path = "SKILLS_USAGE.md"
    with open(skills_usage_path, "w", encoding="utf-8") as f:
        f.write(skills_usage)
    print(f"✓ 创建文件：{skills_usage_path}")


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

    # 生成技能使用表
    generate_skills_usage(project_name)

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
        sys.exit(1)
    
    project_name = sys.argv[1]
    project_type = sys.argv[2] if len(sys.argv) > 2 else "web_app"
    init_context(project_name, project_type)
