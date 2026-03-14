# 详细设计模板

## DetailedDesign.md 标准结构

```markdown
# [项目名称] 详细设计文档

## 1. 设计概述

### 1.1 设计目标
[详细设计要达成的目标]

### 1.2 设计范围
[包含哪些模块的详细设计]

### 1.3 读者对象
- 全栈工程师
- 测试工程师

## 2. 数据库设计

### 2.1 ER 图
[ER 图链接]

### 2.2 数据表详细设计

#### 2.2.1 [表名]

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | VARCHAR(36) | PK | 主键 |
| username | VARCHAR(50) | NOT NULL, UNIQUE | 用户名 |

**SQL DDL**:
```sql
CREATE TABLE [table_name] (
    id VARCHAR(36) PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    -- 其他字段
);
```

**Prisma Model**:
```prisma
model [ModelName] {
  id        String   @id @default(uuid())
  username  String   @unique
  // 其他字段
}
```

### 2.3 索引设计
| 表名 | 字段 | 索引类型 | 原因 |
|------|------|---------|------|
| User | email | UNIQUE | 快速查找 |

## 3. API 设计

### 3.1 API 概览
| 模块 | 路由前缀 | 说明 |
|------|---------|------|
| 认证 | /api/auth | 用户认证 |
| 用户 | /api/users | 用户管理 |

### 3.2 API 详细设计

#### 3.2.1 POST /api/[module]/[action]

**描述**: [接口描述]

**请求头**:
```
Content-Type: application/json
Authorization: Bearer {token}
```

**请求体**:
```json
{
  "field1": "value1",
  "field2": "value2"
}
```

**响应体 (成功)**:
```json
{
  "code": 200,
  "data": {
    "id": "123",
    "username": "test"
  },
  "message": "成功"
}
```

**响应体 (失败)**:
```json
{
  "code": 400,
  "errors": [
    {
      "field": "username",
      "message": "用户名已存在"
    }
  ]
}
```

**业务逻辑**:
1. 验证请求数据
2. 检查唯一性约束
3. 创建记录
4. 返回结果

## 4. 目录结构

```
src/
├── api/                  # API 层
│   ├── routes/          # 路由
│   ├── controllers/     # 控制器
│   └── middleware/      # 中间件
├── services/            # 业务逻辑层
│   ├── UserService.py
│   └── AuthService.py
├── models/              # 数据模型层
│   ├── User.py
│   └── Repository.py
├── frontend/            # 前端
│   ├── src/
│   │   ├── components/  # 组件
│   │   ├── hooks/       # 自定义 Hooks
│   │   └── api/         # API 客户端
│   └── package.json
└── tests/               # 测试
    ├── unit/           # 单元测试
    └── integration/    # 集成测试
```

## 5. 模块设计

### 5.1 [模块名]

#### 5.1.1 职责
[模块负责的功能]

#### 5.1.2 接口
```python
class [ModuleName]:
    def __init__(self, repository: [RepositoryName]):
        pass
    
    def [method_name](self, [params]) -> [ReturnType]:
        """方法说明"""
        pass
```

#### 5.1.3 依赖关系
- 依赖：[依赖模块]
- 被依赖：[被依赖模块]

## 6. 前端组件设计

### 6.1 组件列表
| 组件名 | 路径 | 说明 |
|--------|------|------|
| UserList | src/components/UserList.tsx | 用户列表 |
| UserForm | src/components/UserForm.tsx | 用户表单 |

### 6.2 组件详细设计

#### UserList

**Props**:
```typescript
interface UserListProps {
  users: User[];
  onSelect: (user: User) => void;
  onDelete?: (id: string) => void;
}
```

**状态**:
```typescript
const [loading, setLoading] = useState(false);
const [error, setError] = useState<string | null>(null);
```

**UI 结构**:
```tsx
<div className="user-list">
  <header>用户列表</header>
  <ul>
    {users.map(user => (
      <li key={user.id}>{user.name}</li>
    ))}
  </ul>
</div>
```

## 7. 安全设计

### 7.1 认证机制
- JWT Token
- 有效期 2 小时
- Refresh Token 7 天

### 7.2 权限控制
| 角色 | 权限 |
|------|------|
| 用户 | 查看自己的数据 |
| 管理员 | 管理所有数据 |

### 7.3 数据验证
- 输入验证 (Zod)
- SQL 注入防护 (参数化查询)
- XSS 防护 (转义输出)

## 8. 性能优化

### 8.1 数据库优化
- 索引设计
- 查询优化
- 缓存策略

### 8.2 前端优化
- 懒加载
- 虚拟滚动
- 防抖节流

## 9. 错误处理

### 9.1 错误码定义
| 错误码 | 说明 |
|--------|------|
| 400 | 请求参数错误 |
| 401 | 未认证 |
| 403 | 无权限 |
| 404 | 资源不存在 |
| 500 | 服务器错误 |

### 9.2 错误处理策略
- 统一错误处理中间件
- 前端错误提示
- 后端错误日志

## 10. 测试策略

### 10.1 单元测试
- 服务层测试覆盖率 > 90%
- 仓库层测试覆盖率 > 80%

### 10.2 集成测试
- API 端到端测试
- 关键业务流程测试

### 10.3 测试数据
- 使用 Factory 模式生成测试数据
- 每个测试独立数据
```

---

## API 设计模板

```markdown
### [HTTP 方法] [路径]

**描述**: [一句话描述]

**认证**: [需要/不需要]

**权限**: [角色要求]

**请求参数**:

| 参数 | 位置 | 类型 | 必填 | 说明 |
|------|------|------|------|------|
| id | path | string | 是 | 资源 ID |
| page | query | number | 否 | 页码 |

**请求体**:
```json
{
  "field": "value"
}
```

**成功响应 (200)**:
```json
{
  "code": 200,
  "data": {}
}
```

**错误响应**:
| 错误码 | 说明 |
|--------|------|
| 400 | 参数错误 |
| 404 | 资源不存在 |

**业务逻辑**:
1. 步骤 1
2. 步骤 2
3. 步骤 3
```

---

## 使用指南

1. **复制模板** 到项目根目录
2. **填写数据库设计** - 使用 generate_schema.py 生成
3. **填写 API 设计** - 使用 API 模板
4. **绘制 ER 图** - 使用 se-diagram
5. **工程师使用** - 作为编码依据
