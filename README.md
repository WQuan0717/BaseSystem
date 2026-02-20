# BaseSystem

软件工程生命周期标准化系统，基于 Trae IDE 的 SOLO Coder 模式实现。

## 项目简介

BaseSystem 提供了一套完整的软件工程生命周期标准化流程，包括：

- 需求分析
- 架构设计
- 详细设计
- 开发实现
- 测试验证
- 文档生成

## 技术栈

### Web 项目
- 前端: Vue 3 + Vite + TypeScript
- 后端: Node.js + Express
- 数据库: PostgreSQL + Prisma
- 缓存: Redis

### AI/RAG 项目
- 后端: Python + FastAPI
- 数据库: PostgreSQL + pgvector
- AI 框架: LangChain/LlamaIndex
- 前端: Vue 3 或 Streamlit

## 项目结构

```
.
├── .trae/
│   ├── agents/          # 子智能体配置
│   └── skills/          # 技能模块
└── README.md
```

## 使用方式

1. 在 Trae IDE 中使用 SOLO Coder 模式
2. 根据任务需求自动调用对应的子智能体
3. 遵循软件工程生命周期标准流程

## 许可证

MIT License
