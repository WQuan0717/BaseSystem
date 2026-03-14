# Trae 平台

> 一个完整的 AI 辅助开发平台，为你的项目提供标准化的软件工程能力。

---

## 🚀 快速开始

### 安装

```bash
# 方式 1：使用安装脚本
python install.py

# 方式 2：手动复制
# 将整个 .trae 目录复制到你的项目根目录
```

### 使用

```bash
# 1. 初始化项目
python .trae/skills/se-context/scripts/init_context.py "我的项目"

# 2. 在 Trae 中调用 Skills
invoke se-lifecycle
invoke se-development
```

---

## 📁 目录结构

```
.trae/
├── rules/                    # 规则（自动加载）
│   ├── user_rules.md         # 用户偏好
│   └── project_rules.md      # 基础规则
├── skills/                   # 技能（按需调用）
│   ├── se-lifecycle/         # 工作流决策
│   ├── se-context/           # 状态管理
│   ├── se-requirements/      # 需求分析
│   ├── se-architecture/      # 架构设计
│   ├── se-detailed-design/   # 详细设计
│   ├── se-development/       # 开发实现
│   ├── se-diagram/           # 图表生成
│   ├── se-testing/           # 测试验证
│   ├── se-documentation/     # 文档生成
│   └── skill-creator/        # Skill 开发工具
├── agents/                   # 子智能体配置模板（手动创建）
│   ├── README.md             # 子智能体使用指南
│   ├── qa-engineer.md        # QA 工程师配置
│   └── technical-writer.md   # 技术作家配置
├── install.py                # 安装脚本
└── INSTALL.md                # 安装指南
```

---

## 🎯 核心 Skills

### 工作流（9 个）

| Skill | 用途 | 脚本 |
|-------|------|------|
| **se-lifecycle** | 工作流决策 | ❌ |
| **se-context** | 状态管理 | ✅ 2 个 |
| **se-requirements** | 需求分析 | ❌ |
| **se-architecture** | 架构设计 | ❌ |
| **se-detailed-design** | 详细设计 | ✅ 1 个 |
| **se-development** | 开发实现 | ✅ 1 个 |
| **se-diagram** | 图表生成 | ✅ 1 个 |
| **se-testing** | 测试验证 | ✅ 1 个 |
| **se-documentation** | 文档生成 | ❌ |

### 工具（1 个）

| Skill | 用途 |
|-------|------|
| **skill-creator** | 创建新 Skills |

---

## 🤖 子智能体（可选）

子智能体用于**并行执行**独立任务，每个子智能体有独立的 40 个 MCP Tools 配额。

| 子智能体 | 用途 | 配置文档 |
|---------|------|---------|
| **QA Engineer** | 测试专家 | `agents/qa-engineer.md` |
| **Technical Writer** | 文档专家 | `agents/technical-writer.md` |

**使用方式**：
1. 阅读 `agents/README.md` 了解子智能体配置
2. 在 Trae 设置中手动创建子智能体
3. 启动子智能体与 SOLO Coder 并行工作

---

## 📚 文档

所有文档都在 `.trae/` 内部：

- **INSTALL.md** - 安装指南
- **rules/user_rules.md** - 用户规则
- **rules/project_rules.md** - 基础规则
- **skills/xxx/SKILL.md** - 各 Skill 的使用文档

---

## 🔧 常用命令

### 项目管理

```bash
# 初始化项目
python .trae/skills/se-context/scripts/init_context.py "项目名称"

# 查看状态
python .trae/skills/se-context/scripts/update_context.py show

# 更新阶段
python .trae/skills/se-context/scripts/update_context.py phase development
```

### 开发工具

```bash
# 生成数据库 Schema
python .trae/skills/se-detailed-design/scripts/generate_schema.py

# 初始化垂直切片
python .trae/skills/se-development/scripts/init_slice.py "用户管理" user User

# 生成图表
python .trae/skills/se-diagram/scripts/generate_mermaid.py

# 运行测试
python .trae/skills/se-testing/scripts/run_api_tests.py http://localhost:8000
```

---

## 🎓 学习路径

1. **阅读 INSTALL.md** - 了解安装方法
2. **阅读 rules/** - 了解规则和最佳实践
3. **查看 skills/** - 学习各 Skill 的使用
4. **实践项目** - 在实际项目中使用

---

## 🔄 更新

```bash
# 检查更新
python .trae/skills/se-lifecycle/scripts/check_update.py

# 更新平台
python install.py --update
```

---

## 📞 帮助

### 遇到问题？

1. 查看 `.trae/INSTALL.md`
2. 查看对应 Skill 的 `SKILL.md`
3. 运行平台检查：
   ```bash
   python .trae/skills/se-lifecycle/scripts/check_platform.py
   ```

---

*版本：v1.0.0*  
*许可证：MIT*
