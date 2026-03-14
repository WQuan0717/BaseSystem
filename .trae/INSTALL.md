# Trae 平台安装指南

> 如何安装 Trae 平台到你的项目中

---

## 📦 安装方式

### 方式 1：使用安装脚本（推荐）

```bash
# 1. 下载安装脚本
curl -o trae-install.py https://github.com/yourname/trae-platform/raw/main/install.py

# 2. 运行安装脚本
python trae-install.py

# 3. 验证安装
ls .trae/
```

### 方式 2：手动复制

```bash
# 1. 克隆仓库
git clone https://github.com/yourname/trae-platform.git

# 2. 复制 .trae 目录到你的项目
cp -r trae-platform/.trae /path/to/your/project/

# 3. 验证安装
ls /path/to/your/project/.trae/
```

### 方式 3：使用包管理器（未来）

```bash
# 通过 pip 安装（计划中）
pip install trae-platform

# 初始化到当前项目
trae init
```

---

## ✅ 安装后验证

```bash
# 检查目录结构
ls .trae/

# 应该看到：
# ├── rules/
# │   ├── user_rules.md
# │   └── project_rules.md
# └── skills/
#     ├── se-lifecycle/
#     ├── se-context/
#     └── ...
```

---

## 🚀 快速开始

### 1. 初始化项目

```bash
# 在项目根目录运行
python .trae/skills/se-context/scripts/init_context.py "我的项目"
```

### 2. 查看可用 Skills

```bash
ls .trae/skills/

# 核心 Skills:
# - se-lifecycle      工作流决策
# - se-context        状态管理
# - se-requirements   需求分析
# - se-architecture   架构设计
# - se-detailed-design 详细设计
# - se-development    开发实现
# - se-diagram        图表生成
# - se-testing        测试验证
# - se-documentation  文档生成
# - skill-creator     Skill 开发工具
```

### 3. 开始使用

```bash
# 在 Trae 对话中调用 Skills
invoke se-lifecycle
invoke se-development
invoke se-testing
```

---

## 📋 目录结构

```
你的项目/
├── .trae/                    # ← 安装到这里
│   ├── rules/
│   │   ├── user_rules.md     # 用户规则
│   │   └── project_rules.md  # 基础规则
│   └── skills/
│       ├── se-lifecycle/
│       ├── se-context/
│       ├── se-requirements/
│       ├── se-architecture/
│       ├── se-detailed-design/
│       ├── se-development/
│       ├── se-diagram/
│       ├── se-testing/
│       ├── se-documentation/
│       └── skill-creator/
├── src/                      # 你的代码
├── tests/                    # 你的测试
└── docs/                     # 你的文档
```

---

## 🔄 更新

### 检查更新

```bash
python .trae/skills/se-lifecycle/scripts/check_update.py
```

### 更新平台

```bash
# 方式 1：重新安装
python trae-install.py --update

# 方式 2：手动更新
git pull origin main
cp -r .trae/skills/* /path/to/your/project/.trae/skills/
```

---

## 🛠️ 配置

### 项目特定规则

安装后，创建项目特定规则：

```bash
# 创建项目特定规则文件
cat > .trae/project_specific_rules.md << 'EOF'
# 项目特定规则

## 技术栈选型
- 前端：Vue 3 + Vite
- 后端：Python + FastAPI

## 目录结构约定
src/
├── features/  # 功能模块
└── shared/    # 共享资源
EOF
```

---

## ❓ 常见问题

### Q: 安装后找不到 Skills？
A: 检查 `.trae/` 目录是否正确复制到项目根目录

### Q: 如何调用 Skills？
A: 在 Trae 对话中使用 `invoke se-xxx` 命令

### Q: 如何添加新 Skills？
A: 参考 `.trae/skills/skill-creator/SKILL.md`

### Q: 如何修改规则？
A: 编辑 `.trae/rules/project_rules.md`

---

## 📚 文档位置

所有文档都在 `.trae/` 内部：

| 文档 | 位置 |
|------|------|
| 用户规则 | `.trae/rules/user_rules.md` |
| 基础规则 | `.trae/rules/project_rules.md` |
| Skill 文档 | `.trae/skills/se-xxx/SKILL.md` |
| 使用示例 | `.trae/skills/se-xxx/examples/` |
| 模板 | `.trae/skills/se-xxx/templates/` |

---

## 🎯 核心理念

1. **只保留 `.trae/`** - 这是全部
2. **安装包模式** - 通过安装获取，不是克隆
3. **自包含** - 所有文档在 `.trae/` 内部
4. **按需扩展** - 核心精简，按需添加

---

*安装完成后，删除安装脚本，只保留 `.trae/`*  
*版本：v1.0.0*
