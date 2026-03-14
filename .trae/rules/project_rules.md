# 基础设计规则

> 这是 Trae 平台的基础规则，在所有项目中通用，项目开始前已存在。

## 工作流程
```
需求分析 → 用例图 → 用户确认
架构设计 → 架构图+ER图 → 用户确认
详细设计 → 类图+流程图 → 用户确认
迭代开发 → 垂直切片 → 每轮验收
测试验证 → 测试报告 → 完成
```

## 复杂度判断
- **simple**: <3 页面，无数据库 → 直接开发 → 验收
- **standard**: 3-10 页，单库 → 需求 → 架构 → 开发 → 验收
- **complex**: >10 页，多服务 → 完整流程（需求→架构→详细设计→迭代开发→测试）

## 技术栈
| 层级 | 技术 |
|------|------|
| 前端 | Vue 3 + Vite + TypeScript |
| 后端 | Python + FastAPI |
| 数据库 | PostgreSQL + pgvector |
| 缓存 | Redis |

## Skills 调用

| 阶段 | Skill | 调用时机 |
|------|-------|----------|
| 全局 | invoke se-lifecycle | 任何项目开始时，获取生命周期上下文 |
| 需求 | invoke se-requirements | 用户想法模糊，需要结构化需求文档 |
| 架构 | invoke se-architecture | 需求明确后，设计系统架构 |
| 详细设计 | invoke se-detailed-design | 架构确定后，设计数据库和 API |
| 开发 | invoke se-development | 详细设计后，编写代码 |
| 测试 | invoke se-testing | 开发完成后，验证系统质量（可与开发并行） |
| 文档 | invoke se-documentation | 测试完成后，生成项目文档（可与测试并行） |
| 画图 | invoke se-diagram | 任何需要图表时（用例图、架构图、流程图等） |
| 状态 | invoke se-context | 需要持久化项目上下文时 |

## Agent 模式
- **agent**: 单一任务，快速实现（默认）
- **plan**: 多步骤，需要规划
- **spec**: 复杂需求，需要详细设计

## 并行策略
- **串行**: 需求→架构→详细设计→开发（强依赖）
- **可并行**: 测试、文档可与开发同时进行
- **Subagent**: 仅在多个独立模块需同时开发时使用（最多 2-3 个）

---

## 开发最佳实践

### 1. Playwright 测试规范
- **测试目录**: `tests/e2e/` - 所有 Playwright 测试脚本和截图统一存放
- **截图保存**: `tests/e2e/screenshots/` - 按功能模块分类保存
- **前置检查**: 任何前端修改后，必须运行 Playwright 进行故障排查

```bash
# 运行 E2E 测试
cd tests/e2e
playwright test

# 截图自动保存在 tests/e2e/screenshots/
```

### 2. 测试用例设计标准
使用标准软件测试方法设计测试用例：
- **等价类划分** - 有效/无效输入分类
- **边界值分析** - 最小值、最大值、边界点
- **正交实验法** - 多因素组合测试
- **错误推测法** - 基于经验的异常场景

### 3. 端口冲突处理
启动服务前先检查端口占用：
```bash
# 检查端口占用
netstat -ano | findstr :8000
netstat -ano | findstr :3000

# 强制终止占用进程后重启，而不是更换端口
taskkill /F /PID <进程 ID>
```

### 4. WSL 文件查看
在 WSL 环境中，使用以下命令查看更新的文件：
```bash
ls -la      # 显示隐藏文件和详细信息
ls -lt      # 按修改时间排序
find . -mmin -5  # 查找 5 分钟内修改的文件

# 使用 WSL 辅助脚本（位于 se-context/skills/scripts/wsl_helper.py）
python .trae/skills/se-context/scripts/wsl_helper.py recent 5
python .trae/skills/se-context/scripts/wsl_helper.py port 8000
python .trae/skills/se-context/scripts/wsl_helper.py kill-port 8000
```

### 5. 积极使用 Skills
遇到问题时，优先检查和调用合适的 Skills：
```bash
# 检查可用 Skills
ls .trae/skills/

# 查看 Skill 文档
cat .trae/skills/se-*/SKILL.md

# 调用 Skill
invoke se-detailed-design
```

---

## 编码原则

### 避免过度设计
- ✅ 告诉 LLM 正确的方向
- ❌ 不要此地无银三百两
- ❌ 避免过多不必要的否定
- ✅ 保持提示词简洁聚焦

### 前端修改检查清单
任何前端修改后：
1. ✅ 运行类型检查：`npm run type-check`
2. ✅ 运行 ESLint：`npm run lint`
3. ✅ 运行单元测试：`npm test`
4. ✅ 运行 Playwright E2E 测试
5. ✅ 检查截图对比（如有视觉回归测试）

---

## 相关文档

- `user_rules.md` - 用户偏好和习惯
- `project_specific_rules.md` - 当前项目的特定规则（开发中产生）

---

*这是 Trae 平台基础规则，适用于所有项目*
