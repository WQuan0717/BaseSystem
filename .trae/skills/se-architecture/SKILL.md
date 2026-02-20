---
name: se-architecture
description: Architecture design knowledge for software engineering. Provides methods for tech stack selection, open-source discovery, risk assessment, and Design.md generation.
---

# Architecture Design

Professional knowledge for architecture phase. Transform Requirement.md into Design.md with tech stack decisions and architecture patterns.

## Core Principles

### Principle 1: Don't Reinvent the Wheel
- First reaction should be "is there an existing solution?" not "how to build"
- Search GitHub, npm, and open-source communities
- Evaluate maturity, maintenance, and community support

### Principle 2: Pragmatic Selection
- Startup projects prefer modular monolith over microservices
- Choose boring technology over exciting but immature options
- Consider team expertise and learning curve

### Principle 3: Risk First
- Every tech selection must identify risks
- Create backup plans for high-risk choices
- Document trade-offs and decision rationale

### Principle 4: Downstream Friendly
- Design.md must contain minimum info for Detailed Designer
- Clear module boundaries and responsibilities
- Explicit integration points between modules

## Tech Stack Selection

### Evaluation Criteria

| Criterion | Weight | Questions |
|-----------|--------|-----------|
| Maturity | High | How long has it existed? Production ready? |
| Community | High | Active development? Good documentation? |
| Performance | Medium | Meets requirements? Benchmarks available? |
| Learning Curve | Medium | Team familiar? Good tutorials? |
| Ecosystem | Medium | Plugins available? Integrations? |
| License | Low | MIT/Apache? Commercial friendly? |

### Selection Process

1. Extract technical keywords from requirements
2. Search for open-source solutions (GitHub, npm, Web)
3. Evaluate and score candidates (1-5 for each criterion)
4. Calculate weighted scores
5. Make decision with documented reasons

### Common Tech Stacks

**Frontend:**
- React + Next.js (SSR, SSG, API routes)
- Vue + Nuxt.js
- Svelte + SvelteKit

**Backend:**
- Node.js + Express/Fastify/NestJS
- Python + FastAPI/Django
- Go + Gin/Echo

**Database:**
- PostgreSQL (relational, complex queries)
- MongoDB (document, flexible schema)
- Redis (cache, sessions)

**Deployment:**
- Vercel/Netlify (frontend, serverless)
- Docker + VPS (full control)
- Cloud services (AWS/GCP/Azure)

## Architecture Patterns

### Monolithic Architecture
- Best for: Startups, MVP, small teams
- Pros: Simple deployment, easy debugging, lower latency
- Cons: Harder to scale, single point of failure

### Modular Monolith
- Best for: Growing startups, medium teams
- Pros: Clear boundaries, easier to split later
- Cons: Still single deployment unit

### Microservices
- Best for: Large teams, high scale, complex domains
- Pros: Independent scaling, technology diversity
- Cons: Operational complexity, distributed system challenges

## Risk Assessment

### Risk Categories

| Category | Examples |
|----------|----------|
| Technical | New technology, complex integration |
| Operational | Deployment complexity, monitoring |
| Security | Data exposure, authentication |
| Performance | Scalability, latency |
| Team | Learning curve, expertise gap |

### Risk Template

```markdown
### RISK-001: [Risk Name]

**Category**: [Technical/Operational/Security/Performance/Team]

**Probability**: [High/Medium/Low]

**Impact**: [High/Medium/Low]

**Description**: [What could go wrong]

**Mitigation**: [How to prevent or reduce impact]

**Backup Plan**: [What to do if it happens]
```

## Design.md Template

```markdown
# 技术架构设计文档

## 1. 架构概述

### 1.1 设计目标
[架构要达成的目标]

### 1.2 架构风格
[单体/模块化单体/微服务]

### 1.3 核心决策
[关键的技术决策及其理由]

## 2. 技术选型

### 2.1 技术栈总览

| 层级 | 技术 | 版本 | 选型理由 |
|------|------|------|---------|
| 前端 | React | 18.x | 理由 |
| 后端 | Node.js | 20.x | 理由 |
| 数据库 | PostgreSQL | 16.x | 理由 |

### 2.2 开源组件

| 组件 | 用途 | GitHub | 许可证 |
|------|------|--------|--------|
| 组件1 | 用途 | 链接 | MIT |

## 3. 系统架构

### 3.1 架构图
[架构图或描述]

### 3.2 模块划分

| 模块 | 职责 | 依赖 |
|------|------|------|
| 模块1 | 职责 | 依赖模块 |

### 3.3 模块边界
[模块之间的接口和边界定义]

## 4. 数据架构

### 4.1 数据存储
[数据库选型和数据存储策略]

### 4.2 数据流
[数据如何在系统中流动]

## 5. 接口设计

### 5.1 API 风格
[REST/GraphQL/RPC]

### 5.2 接口协议
[认证、版本控制、错误处理]

## 6. 部署架构

### 6.1 部署方式
[Docker/K8s/Serverless]

### 6.2 环境规划
[开发/测试/生产环境]

## 7. 风险评估

### 7.1 风险清单
[列出识别的风险]

### 7.2 缓解措施
[每个风险的应对策略]

## 8. 附录

### 8.1 技术调研
[技术选型的调研过程和对比]

### 8.2 参考资料
[参考的文档和资源]
```

## Quality Checklist

| Check | Criteria |
|-------|----------|
| Tech Stack Selected | All layers have technology choices with reasons |
| Open Source Verified | All recommended repos have valid links |
| Module Boundaries | Clear responsibilities and interfaces |
| Risks Identified | At least 3 risks with mitigation plans |
| Downstream Ready | Contains enough info for Detailed Designer |
