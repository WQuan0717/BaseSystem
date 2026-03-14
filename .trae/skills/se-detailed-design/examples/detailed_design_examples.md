# 详细设计示例

## 示例 1：用户管理系统

### 数据库设计示例

```markdown
## 2. 数据库设计

### 2.2.1 User (用户表)

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | VARCHAR(36) | PK | 用户 ID (UUID) |
| username | VARCHAR(50) | NOT NULL, UNIQUE | 用户名 |
| email | VARCHAR(100) | NOT NULL, UNIQUE | 邮箱 |
| password_hash | VARCHAR(255) | NOT NULL | 密码哈希 |
| role | VARCHAR(20) | NOT NULL, DEFAULT 'user' | 角色 |
| status | VARCHAR(20) | NOT NULL, DEFAULT 'active' | 状态 |
| created_at | TIMESTAMP | NOT NULL, DEFAULT NOW() | 创建时间 |
| updated_at | TIMESTAMP | NOT NULL, DEFAULT NOW() | 更新时间 |

**SQL DDL**:
```sql
CREATE TABLE users (
    id VARCHAR(36) PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user',
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 索引
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_status ON users(status);
```

**Prisma Model**:
```prisma
model User {
  id            String    @id @default(uuid())
  username      String    @unique @db.VarChar(50)
  email         String    @unique @db.VarChar(100)
  passwordHash  String    @map("password_hash") @db.VarChar(255)
  role          String    @default("user") @db.VarChar(20)
  status        String    @default("active") @db.VarChar(20)
  createdAt     DateTime  @default(now()) @map("created_at")
  updatedAt     DateTime  @updatedAt @map("updated_at")
  
  @@map("users")
}
```
```

---

### API 设计示例

```markdown
## 3. API 设计

### 3.2.1 POST /api/auth/register

**描述**: 用户注册

**认证**: 不需要

**请求体**:
```json
{
  "username": "zhangsan",
  "email": "zhangsan@example.com",
  "password": "Password123"
}
```

**成功响应 (201)**:
```json
{
  "code": 201,
  "data": {
    "id": "uuid-123-456",
    "username": "zhangsan",
    "email": "zhangsan@example.com",
    "role": "user",
    "createdAt": "2025-01-01T10:00:00Z"
  },
  "message": "注册成功"
}
```

**错误响应**:

| 错误码 | 说明 | 错误示例 |
|--------|------|---------|
| 400 | 参数错误 | 用户名长度不足 |
| 409 | 冲突 | 用户名已存在 |

```json
{
  "code": 409,
  "errors": [
    {
      "field": "username",
      "message": "用户名已存在"
    }
  ]
}
```

**业务逻辑**:
1. 验证请求参数 (Zod schema)
2. 检查用户名和邮箱唯一性
3. 密码加密 (bcrypt, salt rounds=10)
4. 创建用户记录
5. 返回用户信息 (不含密码)
```

---

### 前端组件设计示例

```markdown
## 6. 前端组件设计

### 6.2.1 UserList 组件

**Props**:
```typescript
interface UserListProps {
  users: User[];
  loading?: boolean;
  onSelect: (user: User) => void;
  onDelete?: (userId: string) => void;
}

interface User {
  id: string;
  username: string;
  email: string;
  role: 'admin' | 'user';
  createdAt: string;
}
```

**实现**:
```typescript
import React, { useState } from 'react';

export function UserList({ users, loading, onSelect, onDelete }: UserListProps) {
  const [selectedId, setSelectedId] = useState<string | null>(null);

  if (loading) {
    return <div>加载中...</div>;
  }

  if (users.length === 0) {
    return <EmptyState message="暂无用户" />;
  }

  return (
    <div className="user-list">
      <header className="user-list-header">
        <h2>用户列表 ({users.length})</h2>
      </header>
      
      <ul className="user-list-items">
        {users.map((user) => (
          <li
            key={user.id}
            className={`user-list-item ${selectedId === user.id ? 'selected' : ''}`}
            onClick={() => {
              setSelectedId(user.id);
              onSelect(user);
            }}
          >
            <div className="user-info">
              <span className="username">{user.username}</span>
              <span className="email">{user.email}</span>
              <span className={`role-badge role-${user.role}`}>{user.role}</span>
            </div>
            
            {onDelete && (
              <button
                className="delete-btn"
                onClick={(e) => {
                  e.stopPropagation();
                  onDelete(user.id);
                }}
              >
                删除
              </button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
```

**样式**:
```css
.user-list {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
}

.user-list-header {
  background: #f5f5f5;
  padding: 16px;
  border-bottom: 1px solid #e0e0e0;
}

.user-list-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  border-bottom: 1px solid #e0e0e0;
  cursor: pointer;
  transition: background 0.2s;
}

.user-list-item:hover {
  background: #f9f9f9;
}

.user-list-item.selected {
  background: #e3f2fd;
}
```
```

---

## 示例 2：RAG 知识库系统

### 数据库设计示例

```markdown
### 2.2.2 Document (文档表)

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | VARCHAR(36) | PK | 文档 ID |
| title | VARCHAR(200) | NOT NULL | 标题 |
| file_path | VARCHAR(500) | NOT NULL | 文件路径 |
| file_type | VARCHAR(20) | NOT NULL | 文件类型 (pdf/docx/xlsx) |
| file_size | INTEGER | NOT NULL | 文件大小 (字节) |
| content | TEXT | NULL | 提取的文本内容 |
| status | VARCHAR(20) | NOT NULL | 状态 (pending/processing/completed/failed) |
| created_by | VARCHAR(36) | FK | 上传者 ID |

**关系**:
- Document N:1 User (created_by → User.id)
- Document 1:N Chunk (document_id → Document.id)
```

---

### API 设计示例

```markdown
### 3.2.5 POST /api/documents/upload

**描述**: 上传文档

**认证**: 需要 (管理员)

**请求类型**: multipart/form-data

**请求体**:
```
file: [binary] (PDF/Word/Excel 文件)
category: string (可选，分类)
```

**成功响应 (201)**:
```json
{
  "code": 201,
  "data": {
    "id": "uuid-789-012",
    "title": "产品手册.pdf",
    "fileType": "pdf",
    "fileSize": 2048000,
    "status": "processing",
    "uploadedAt": "2025-01-01T10:00:00Z"
  },
  "message": "上传成功，正在处理"
}
```

**业务逻辑**:
1. 验证文件类型 (仅允许 pdf, docx, xlsx)
2. 验证文件大小 (< 50MB)
3. 生成唯一文件名 (UUID + 原扩展名)
4. 保存到存储目录
5. 创建文档记录 (status=pending)
6. 触发后台处理任务
7. 返回上传结果
```

---

## 使用指南

1. **参考示例** 编写自己的详细设计
2. **使用脚本生成** - generate_schema.py 生成数据库 schema
3. **保持格式统一** - 便于工程师阅读
4. **工程师直接使用** - 作为编码依据
