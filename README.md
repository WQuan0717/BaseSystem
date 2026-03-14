# Trae 平台

> 一个完整的 AI 辅助开发平台，为你的项目提供标准化的软件工程能力。

---

## 🚀 快速开始

### 安装

```bash
# 方式 1：使用安装脚本（推荐）
curl -o trae-install.py https://raw.githubusercontent.com/WQuan0717/BaseSystem/trae-platform-test/.trae/install.py
python trae-install.py

# 方式 2：手动复制
git clone -b trae-platform-test --depth 1 https://github.com/WQuan0717/BaseSystem.git temp
cp -r temp/.trae /path/to/your/project/
rm -rf temp
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
│   └── ...                   # 其他工具 skills
├── agents/                   # 子智能体配置（可选）
│   ├── README.md             # 使用指南
│   ├── qa-engineer.md        # QA 工程师
│   ├── technical-writer.md   # 技术作家
│   └── agentic-optimizer.md  # Agent 优化师
├── install.py                # 安装脚本
├── README.md                 # 平台说明
└── INSTALL.md                # 安装指南
```

---

## 🎯 核心特性

### 1. 精简 Rules

- `user_rules.md` - 用户偏好和习惯
- `project_rules.md` - 基础设计规则
- 总计 < 200 行，避免上下文冗余

### 2. 增强 Skills

每个 se-* Skill 包含：
- `SKILL.md` - 完整文档
- `scripts/` - 可执行脚本
- `templates/` - 模板文件
- `examples/` - 使用示例

### 3. 智能 Agents

- **串行阶段** - 由 SOLO Coder 调用 Skills 完成
- **并行阶段** - 创建子智能体（QA、Writer）提升效率
- **工具型** - Agentic Optimizer 用于设计 Agent

### 4. 安装模式

- 不是克隆仓库，而是安装包分发
- 运行 `install.py` 即可安装到任何项目
- 自包含设计，所有文档在 `.trae/` 内部

---

## 📚 文档

所有文档都在 `.trae/` 内部：

- **INSTALL.md** - 安装指南
- **README.md** - 平台说明
- **agents/README.md** - 子智能体使用指南
- **rules/** - 用户和基础规则
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

## 🤖 工作流

### 串行阶段（SOLO Coder）

```
需求分析 → 架构设计 → 详细设计 → 功能开发
   ↓           ↓           ↓          ↓
se-requirements → se-architecture → se-detailed-design → se-development
```

### 并行阶段（子智能体）

```
SOLO Coder（开发） ──┬──> QA Engineer（测试）
                     └──> Technical Writer（文档）
```

---

## 📦 安装方式

### 方式 1：使用安装脚本（推荐）

```bash
curl -o trae-install.py https://raw.githubusercontent.com/WQuan0717/BaseSystem/trae-platform-test/.trae/install.py
python trae-install.py
```

### 方式 2：手动复制

```bash
git clone -b trae-platform-test --depth 1 https://github.com/WQuan0717/BaseSystem.git temp
cp -r temp/.trae /path/to/your/project/
rm -rf temp
```

### 方式 3：使用 GitHub CLI

```bash
gh repo clone WQuan0717/BaseSystem
cd BaseSystem
git checkout trae-platform-test
cp -r .trae /path/to/your/project/
```

---

## ✅ 安装验证

```bash
# 检查目录结构
ls .trae/

# 应该看到：
# ├── rules/
# │   ├── user_rules.md
# │   └── project_rules.md
# ├── skills/
# │   ├── se-lifecycle/
# │   ├── se-context/
# │   └── ...
# ├── agents/
# │   ├── README.md
# │   ├── qa-engineer.md
# │   └── ...
# ├── install.py
# ├── README.md
# └── INSTALL.md
```

---

## 🎓 学习路径

1. **安装平台** - 运行安装脚本
2. **阅读规则** - 了解 `user_rules.md` 和 `project_rules.md`
3. **查看 Skills** - 浏览 `.trae/skills/se-*/SKILL.md`
4. **实践项目** - 在实际项目中使用
5. **可选扩展** - 根据需要创建子智能体

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
3. 查看 `agents/README.md` 了解子智能体配置

---

## 📝 许可证

MIT License

---

*版本：v1.0.0*  
*测试分支：trae-platform-test*
