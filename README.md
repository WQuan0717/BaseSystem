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

### 前置准备

本项目需要在 Trae IDE 中使用。关于如何创建和管理自定义智能体，请参考官方文档：
[创建并管理智能体 - TRAE 文档](https://docs.trae.ai/ide/agent?_lang=zh#dc8000ac)

### 智能体创建方式

在 Trae IDE 中创建自定义智能体有两种方式：

#### 1. 智能生成（推荐）
- 在 AI 对话输入框中输入 `@`，点击浮起面板底部的「创建智能体」
- 点击右上角「智能生成」按钮
- 描述智能体的功能、使用场景、使用时机等
- 按需修改自动生成的参数后点击「创建」

#### 2. 手动创建
- 在「创建智能体」面板中手动配置以下参数：
  - **头像**（可选）：上传图片作为智能体头像
  - **名称**：输入智能体的名称
  - **提示词**：输入提示词规范智能体的行为
  - **可被其他智能体调用**：开启后可被 SOLO Coder 调用
  - **工具**：配置 MCP Server 和内置工具

### 项目使用流程

1. 在 Trae IDE 中使用 SOLO Coder 模式
2. 根据任务需求自动调用对应的子智能体
3. 遵循软件工程生命周期标准流程

## 许可证

MIT License
