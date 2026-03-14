# README 模板

## 标准 README 结构

```markdown
# [项目名称]

[项目简介：一句话描述项目是做什么的]

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 目录

- [功能特性](#-功能特性)
- [快速开始](#-快速开始)
- [安装说明](#-安装说明)
- [使用指南](#-使用指南)
- [API 文档](#-api 文档)
- [技术栈](#-技术栈)
- [项目结构](#-项目结构)
- [开发指南](#-开发指南)
- [常见问题](#-常见问题)
- [贡献](#-贡献)
- [许可证](#-许可证)

## ✨ 功能特性

- **功能 1**: [描述]
- **功能 2**: [描述]
- **功能 3**: [描述]

## 🚀 快速开始

### 前置要求

- Node.js >= 20.x
- Python >= 3.10
- PostgreSQL >= 16.x

### 一键启动（开发环境）

```bash
# 克隆项目
git clone https://github.com/yourname/project.git
cd project

# 安装依赖
npm install
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填写数据库连接等配置

# 启动后端
cd backend
python main.py

# 启动前端（新终端）
cd frontend
npm run dev
```

访问 http://localhost:3000

## 📦 安装说明

### 后端安装

```bash
cd backend

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 运行数据库迁移
prisma migrate dev

# 启动服务
python main.py
```

### 前端安装

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build
```

## 📖 使用指南

### 1. 用户注册

访问 http://localhost:3000/register，填写注册表单。

### 2. 用户登录

使用注册的邮箱和密码登录。

### 3. [核心功能]

[详细使用说明]

## 📚 API 文档

### 认证接口

#### POST /api/auth/register

注册新用户

**请求体**:
```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```

**响应**:
```json
{
  "code": 201,
  "data": {
    "id": "string",
    "username": "string",
    "email": "string"
  }
}
```

#### POST /api/auth/login

用户登录

**请求体**:
```json
{
  "email": "string",
  "password": "string"
}
```

**响应**:
```json
{
  "code": 200,
  "data": {
    "token": "string",
    "expiresIn": 7200
  }
}
```

完整 API 文档：[docs/API.md](docs/API.md)

## 🛠️ 技术栈

**前端**:
- Vue 3 + Vite + TypeScript
- TailwindCSS
- Pinia (状态管理)
- Vue Router

**后端**:
- Python 3.10+
- FastAPI
- PostgreSQL
- Prisma ORM
- JWT 认证

**开发工具**:
- Git
- pytest (测试)
- ESLint + Prettier

## 📁 项目结构

```
project/
├── backend/              # 后端代码
│   ├── api/             # API 路由
│   ├── services/        # 业务逻辑
│   ├── models/          # 数据模型
│   └── main.py          # 入口文件
├── frontend/            # 前端代码
│   └── src/
│       ├── components/  # 组件
│       ├── hooks/       # Hooks
│       └── api/         # API 客户端
├── docs/                # 文档
├── tests/               # 测试
└── README.md            # 本文件
```

## 🔧 开发指南

### 代码规范

```bash
# 后端格式化
black src/ tests/

# 前端格式化
npm run lint
npm run format
```

### 运行测试

```bash
# 后端测试
cd backend
pytest

# 前端测试
cd frontend
npm test
```

### 提交规范

遵循 [Conventional Commits](https://www.conventionalcommits.org/)

```
feat: 新功能
fix: 修复 bug
docs: 文档更新
style: 代码格式
refactor: 重构
test: 测试
chore: 构建/工具
```

## ❓ 常见问题

### Q: 数据库连接失败？

A: 检查 `.env` 文件中的 `DATABASE_URL` 配置，确保 PostgreSQL 服务已启动。

### Q: 前端跨域问题？

A: 后端已配置 CORS，确保前端请求携带正确的 headers。

### Q: [其他问题]？

A: [解答]

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

MIT License - [LICENSE](LICENSE)

## 👥 作者

- [你的名字] - [GitHub](https://github.com/yourname)

## 🙏 致谢

感谢以下开源项目：
- [FastAPI](https://fastapi.tiangolo.com/)
- [Vue 3](https://vuejs.org/)
- [Prisma](https://www.prisma.io/)

---

*Last updated: 2025-01-01*
```

---

## 快速开始模板

```markdown
# 快速开始

## 5 分钟上手指南

### 1. 环境准备

确保已安装：
- Node.js 20+
- Python 3.10+
- PostgreSQL 16+

### 2. 安装

```bash
git clone <repo-url>
cd <project-name>
npm install
pip install -r requirements.txt
```

### 3. 配置

```bash
cp .env.example .env
# 编辑 .env，配置数据库连接
```

### 4. 启动

```bash
# 后端
python backend/main.py

# 前端（新终端）
npm run dev
```

### 5. 访问

打开浏览器访问：http://localhost:3000

## 下一步

- [查看完整文档](docs/README.md)
- [API 参考](docs/API.md)
- [部署指南](docs/DEPLOYMENT.md)
```

---

## 使用指南

1. **复制模板** 到项目根目录
2. **填写内容** 根据实际情况
3. **保持更新** 每次版本更新
4. **添加徽章** 版本、License、构建状态
