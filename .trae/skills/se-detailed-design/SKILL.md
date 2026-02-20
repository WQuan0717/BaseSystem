---
name: se-detailed-design
description: Detailed design knowledge for software engineering. Provides methods for database design, API specification, directory structure, and DetailedDesign.md generation.
---

# Detailed Design

Professional knowledge for detailed design phase. Transform Design.md into DetailedDesign.md with executable specifications.

## Core Principles

### Principle 1: Executable Specifications
- Detailed enough for Full-stack Engineer to code directly
- Include SQL statements, not just table descriptions
- Include request/response examples, not just endpoint names

### Principle 2: Contract First
- Define interface protocols before internal implementation
- API contracts are agreements between frontend and backend
- Database schema is the foundation of data layer

### Principle 3: Dependency Inversion
- Business logic depends on abstractions, not implementations
- Define interfaces before implementations
- Use dependency injection for flexibility

### Principle 4: High Cohesion, Low Coupling
- Module internal functions should be related
- Modules communicate through well-defined interfaces
- Minimize dependencies between modules

## Database Design

### Design Process

1. Identify entities from requirements
2. Define attributes for each entity
3. Identify relationships between entities
4. Normalize (3NF usually sufficient)
5. Add indexes for query optimization
6. Consider partitioning for large tables

### Table Design Template

```sql
-- 用户表
CREATE TABLE users (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email       VARCHAR(255) NOT NULL UNIQUE,
    password    VARCHAR(255) NOT NULL,
    name        VARCHAR(100),
    status      VARCHAR(20) NOT NULL DEFAULT 'active',
    created_at  TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

-- 索引
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_status ON users(status);

-- 注释
COMMENT ON TABLE users IS '用户表';
COMMENT ON COLUMN users.id IS '用户ID';
COMMENT ON COLUMN users.email IS '邮箱地址';
```

### Relationship Types

| Relationship | SQL Implementation |
|--------------|-------------------|
| One-to-One | Foreign key with UNIQUE constraint |
| One-to-Many | Foreign key |
| Many-to-Many | Junction table |

## API Design

### RESTful Conventions

| Method | Path | Action | Description |
|--------|------|--------|-------------|
| GET | /users | list | List users |
| GET | /users/:id | get | Get user by ID |
| POST | /users | create | Create user |
| PUT | /users/:id | update | Update user |
| DELETE | /users/:id | delete | Delete user |

### API Specification Template

```markdown
### POST /api/v1/users

创建新用户

**Request Headers:**
```
Content-Type: application/json
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "string (min 8 chars)",
  "name": "string (optional, max 100 chars)"
}
```

**Response 201:**
```json
{
  "code": 201,
  "message": "User created successfully",
  "data": {
    "id": "uuid",
    "email": "user@example.com",
    "name": "John Doe",
    "createdAt": "2024-01-01T00:00:00Z"
  }
}
```

**Response 400:**
```json
{
  "code": 400,
  "message": "Validation error",
  "errors": [
    {"field": "email", "message": "Invalid email format"}
  ]
}
```
```

### Error Response Format

```json
{
  "code": 400,
  "message": "Error description",
  "errors": [
    {"field": "fieldName", "message": "Error message"}
  ]
}
```

## Directory Structure

### Next.js Full-Stack Project

```
project/
├── frontend/                    # Frontend application
│   ├── src/
│   │   ├── app/                # Next.js App Router
│   │   │   ├── (auth)/         # Auth group routes
│   │   │   │   ├── login/
│   │   │   │   └── register/
│   │   │   ├── (dashboard)/    # Dashboard group routes
│   │   │   │   └── dashboard/
│   │   │   ├── api/            # API routes
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx
│   │   ├── components/         # Reusable components
│   │   │   ├── ui/             # Base UI components
│   │   │   └── features/       # Feature components
│   │   ├── lib/                # Utilities
│   │   │   ├── api.ts          # API client
│   │   │   ├── auth.ts         # Auth utilities
│   │   │   └── utils.ts        # Helper functions
│   │   ├── hooks/              # Custom hooks
│   │   ├── types/              # TypeScript types
│   │   └── styles/             # Global styles
│   ├── public/                 # Static assets
│   ├── package.json
│   └── tsconfig.json
├── backend/                     # Backend application (if separate)
│   ├── src/
│   │   ├── modules/            # Feature modules
│   │   │   ├── users/
│   │   │   │   ├── users.controller.ts
│   │   │   │   ├── users.service.ts
│   │   │   │   ├── users.repository.ts
│   │   │   │   └── users.dto.ts
│   │   ├── common/             # Shared code
│   │   │   ├── middleware/
│   │   │   ├── guards/
│   │   │   ├── decorators/
│   │   │   └── filters/
│   │   ├── config/             # Configuration
│   │   └── main.ts
│   ├── prisma/
│   │   └── schema.prisma
│   ├── package.json
│   └── tsconfig.json
├── docs/                        # Documentation
│   ├── Requirement.md
│   ├── Design.md
│   └── DetailedDesign.md
├── scripts/                     # Utility scripts
├── docker-compose.yml
├── .env.example
└── README.md
```

## DetailedDesign.md Template

```markdown
# 详细设计文档

## 1. 设计概述

### 1.1 设计目标
[详细设计要达成的目标]

### 1.2 设计原则
[遵循的设计原则]

## 2. 数据库设计

### 2.1 ER 图
[实体关系图]

### 2.2 表结构

#### 表名: users
[表结构定义，包含字段、类型、约束、索引]

### 2.3 数据字典
[所有表的详细说明]

## 3. API 设计

### 3.1 API 概览
[所有 API 的列表]

### 3.2 API 详细规格
[每个 API 的详细规格]

## 4. 模块设计

### 4.1 模块划分
[模块列表和职责]

### 4.2 模块详细设计
[每个模块的详细设计]

## 5. 目录结构
[项目目录结构]

## 6. 环境配置

### 6.1 环境变量
[需要的环境变量列表]

### 6.2 依赖安装
[依赖安装命令]

## 7. 核心流程

### 7.1 用户注册流程
[流程图或时序图]

### 7.2 用户登录流程
[流程图或时序图]

## 8. 附录

### 8.1 代码规范
[代码风格和规范]

### 8.2 测试策略
[测试方法和覆盖率要求]
```

## Quality Checklist

| Check | Criteria |
|-------|----------|
| Database Complete | All tables with SQL, indexes, comments |
| API Complete | All endpoints with request/response examples |
| Directory Structure | Matches tech stack conventions |
| Environment Setup | All env vars documented |
| Downstream Ready | Engineer can code directly from spec |
