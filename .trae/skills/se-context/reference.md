# se-context Reference

## 脚本使用说明

### init_context.py - 初始化项目上下文

```bash
# 基本用法
python .trae/skills/se-context/scripts/init_context.py "项目名称"

# 指定项目类型
python .trae/skills/se-context/scripts/init_context.py "校园学习平台" "web_app"
```

**项目类型选项：**
- `web_app` - Web 应用（默认）
- `mobile_app` - 移动应用
- `ai_system` - AI 系统
- `api_service` - API 服务

---

### update_context.py - 更新项目状态

```bash
# 更新阶段
python .trae/skills/se-context/scripts/update_context.py phase requirements
python .trae/skills/se-context/scripts/update_context.py phase architecture
python .trae/skills/se-context/scripts/update_context.py phase development

# 添加阻塞问题
python .trae/skills/se-context/scripts/update_context.py add-issue "数据库连接失败" high
python .trae/skills/se-context/scripts/update_context.py add-issue "API 响应慢" medium

# 解决阻塞问题
python .trae/skills/se-context/scripts/update_context.py resolve-issue 0

# 查看当前状态
python .trae/skills/se-context/scripts/update_context.py show
```

---

## 项目状态 Schema

```json
{
  "project_name": "项目名称",
  "project_type": "web_app",
  "current_phase": "requirements",
  "completed_phases": ["init"],
  "pending_phases": ["architecture", "design", "development", "testing", "documentation"],
  "completion_percentage": 17,
  "tech_stack": {
    "frontend": "Vue 3 + Vite + TypeScript",
    "backend": "Python + FastAPI",
    "database": "PostgreSQL + pgvector",
    "others": ["Redis"]
  },
  "start_date": "2025-01-01",
  "target_date": "2025-03-01",
  "last_updated": "2025-01-01T10:00:00",
  "blocking_issues": [
    {
      "description": "问题描述",
      "severity": "high",
      "status": "open",
      "created_at": "2025-01-01T10:00:00"
    }
  ],
  "next_action": "下一步行动"
}
```

---

## 阶段定义

| 阶段 | 说明 | 输出 |
|------|------|------|
| init | 项目初始化 | 项目状态文件 |
| requirements | 需求分析 | Requirement.md |
| architecture | 架构设计 | Design.md |
| design | 详细设计 | DetailedDesign.md |
| development | 开发实现 | 代码 + 测试 |
| testing | 测试验证 | TestReport.md |
| documentation | 文档生成 | README.md 等 |

---

## 历史备份

所有状态更新都会自动备份到 `docs/context/history/` 目录：

```
docs/context/history/
├── state_2025-01-01_100000.json
├── state_2025-01-01_120000.json
└── state_2025-01-02_090000.json
```

可以通过比较历史文件查看项目状态变化。

---

## 与 se-lifecycle 集成

```python
# 在 se-lifecycle 中调用
from se_context.scripts.update_context import update_phase, add_blocking_issue

# 阶段完成时更新
update_phase(state, "architecture")

# 遇到问题时添加阻塞问题
add_blocking_issue(state, "技术选型困难", "high")
```

---

## 最佳实践

1. **每次阶段转换时更新状态**
2. **阻塞问题及时解决**
3. **定期查看历史备份**
4. **保持状态文件与实际情况一致**
