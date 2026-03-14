# 开发示例 - CRUD 完整实现

## 示例：用户管理 CRUD

### 1. Model (Prisma)

```prisma
model User {
  id        String   @id @default(uuid())
  username  String   @unique @db.VarChar(50)
  email     String   @unique @db.VarChar(100)
  password  String   @db.VarChar(255)
  role      String   @default("user") @db.VarChar(20)
  createdAt DateTime @default(now()) @map("created_at")
  updatedAt DateTime @updatedAt @map("updated_at")
  
  @@map("users")
}
```

---

### 2. Repository 层

```python
# src/backend/repositories/user_repository.py
from typing import Optional, List
from prisma import Prisma


class UserRepository:
    def __init__(self, db: Prisma):
        self.db = db
    
    async def find_by_id(self, id: str) -> Optional[dict]:
        return await self.db.user.find_unique(where={"id": id})
    
    async def find_by_email(self, email: str) -> Optional[dict]:
        return await self.db.user.find_unique(where={"email": email})
    
    async def find_all(self) -> List[dict]:
        return await self.db.user.find_many(order={"createdAt": "desc"})
    
    async def create(self, data: dict) -> dict:
        return await self.db.user.create(data=data)
    
    async def update(self, id: str, data: dict) -> Optional[dict]:
        return await self.db.user.update(where={"id": id}, data=data)
    
    async def delete(self, id: str) -> bool:
        await self.db.user.delete(where={"id": id})
        return True
```

---

### 3. Service 层

```python
# src/backend/services/user_service.py
from src.backend.repositories.user_repository import UserRepository
from src.backend.utils.password import hash_password
from src.backend.exceptions import DuplicateError, NotFoundError


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    async def get_by_id(self, id: str) -> dict:
        user = await self.repository.find_by_id(id)
        if not user:
            raise NotFoundError("用户不存在")
        return user
    
    async def get_all(self) -> list:
        return await self.repository.find_all()
    
    async def create(self, data: dict) -> dict:
        # 检查邮箱是否已存在
        existing = await self.repository.find_by_email(data["email"])
        if existing:
            raise DuplicateError("邮箱已存在")
        
        # 密码加密
        data["password"] = hash_password(data["password"])
        
        return await self.repository.create(data)
    
    async def update(self, id: str, data: dict) -> dict:
        # 移除密码字段（不允许直接更新）
        data.pop("password", None)
        
        user = await self.repository.update(id, data)
        if not user:
            raise NotFoundError("用户不存在")
        return user
    
    async def delete(self, id: str) -> bool:
        return await self.repository.delete(id)
```

---

### 4. Controller 层

```python
# src/backend/api/controllers/user_controller.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from src.backend.services.user_service import UserService
from src.backend.database import get_db
from pydantic import BaseModel, EmailStr


router = APIRouter(prefix="/api/users", tags=["users"])


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    role: str
    createdAt: str


@router.get("", response_model=List[UserResponse])
async def get_users(service: UserService = Depends()):
    """获取所有用户"""
    return await service.get_all()


@router.get("/{id}", response_model=UserResponse)
async def get_user(id: str, service: UserService = Depends()):
    """根据 ID 获取用户"""
    try:
        return await service.get_by_id(id)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="用户不存在")


@router.post("", response_model=UserResponse, status_code=201)
async def create_user(
    data: UserCreate,
    service: UserService = Depends()
):
    """创建用户"""
    try:
        return await service.create(data.dict())
    except DuplicateError:
        raise HTTPException(status_code=409, detail="邮箱已存在")


@router.put("/{id}", response_model=UserResponse)
async def update_user(
    id: str,
    data: UserCreate,
    service: UserService = Depends()
):
    """更新用户"""
    try:
        return await service.update(id, data.dict())
    except NotFoundError:
        raise HTTPException(status_code=404, detail="用户不存在")


@router.delete("/{id}", status_code=204)
async def delete_user(id: str, service: UserService = Depends()):
    """删除用户"""
    try:
        await service.delete(id)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="用户不存在")
```

---

### 5. 前端 API Client

```typescript
// src/frontend/src/api/user/api.ts
import axios from 'axios';

export interface User {
  id: string;
  username: string;
  email: string;
  role: string;
  createdAt: string;
}

export interface UserCreate {
  username: string;
  email: string;
  password: string;
}

const API_BASE = '/api/users';

export async function getUsers(): Promise<User[]> {
  const response = await axios.get(API_BASE);
  return response.data;
}

export async function getUserById(id: string): Promise<User> {
  const response = await axios.get(`${API_BASE}/${id}`);
  return response.data;
}

export async function createUser(data: UserCreate): Promise<User> {
  const response = await axios.post(API_BASE, data);
  return response.data;
}

export async function updateUser(id: string, data: UserCreate): Promise<User> {
  const response = await axios.put(`${API_BASE}/${id}`, data);
  return response.data;
}

export async function deleteUser(id: string): Promise<void> {
  await axios.delete(`${API_BASE}/${id}`);
}
```

---

### 6. 前端 Hook

```typescript
// src/frontend/src/hooks/user/useUser.ts
import { useState, useEffect } from 'react';
import { getUsers, createUser, updateUser, deleteUser, User, UserCreate } from '../api/user/api';

export function useUsers() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchUsers = async () => {
    setLoading(true);
    try {
      const data = await getUsers();
      setUsers(data);
      setError(null);
    } catch (err) {
      setError('加载失败');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const create = async (data: UserCreate) => {
    const newUser = await createUser(data);
    setUsers([...users, newUser]);
    return newUser;
  };

  const update = async (id: string, data: UserCreate) => {
    const updatedUser = await updateUser(id, data);
    setUsers(users.map(user => user.id === id ? updatedUser : user));
    return updatedUser;
  };

  const delete_ = async (id: string) => {
    await deleteUser(id);
    setUsers(users.filter(user => user.id !== id));
  };

  return { users, loading, error, fetchUsers, create, update, delete_ };
}
```

---

### 7. 前端组件

```typescript
// src/frontend/src/components/user/UserList.tsx
import React, { useState } from 'react';
import { useUsers } from '../../hooks/user/useUser';
import { UserCreate } from '../../api/user/api';

export function UserList() {
  const { users, loading, error, create, delete_ } = useUsers();
  const [showForm, setShowForm] = useState(false);

  if (loading) return <div>加载中...</div>;
  if (error) return <div>错误：{error}</div>;

  return (
    <div className="user-list">
      <header className="flex justify-between">
        <h2>用户列表 ({users.length})</h2>
        <button onClick={() => setShowForm(true)}>添加用户</button>
      </header>

      <table>
        <thead>
          <tr>
            <th>用户名</th>
            <th>邮箱</th>
            <th>角色</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.username}</td>
              <td>{user.email}</td>
              <td>
                <span className={`badge ${user.role}`}>{user.role}</span>
              </td>
              <td>
                <button onClick={() => delete_(user.id)}>删除</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {showForm && (
        <UserForm
          onSubmit={async (data) => {
            await create(data);
            setShowForm(false);
          }}
          onCancel={() => setShowForm(false)}
        />
      )}
    </div>
  );
}
```

---

### 8. 单元测试

```python
# tests/backend/user/test_service.py
import pytest
from src.backend.services.user_service import UserService
from src.backend.exceptions import DuplicateError, NotFoundError


@pytest.fixture
def user_service():
    # 设置测试 fixture
    pass


@pytest.mark.asyncio
async def test_create_user(user_service):
    """测试创建用户"""
    data = {
        "username": "test",
        "email": "test@example.com",
        "password": "Password123"
    }
    
    user = await user_service.create(data)
    
    assert user["username"] == "test"
    assert user["email"] == "test@example.com"
    assert "password" not in user or user["password"] != "Password123"


@pytest.mark.asyncio
async def test_create_duplicate_email(user_service):
    """测试创建重复邮箱"""
    data = {
        "username": "test2",
        "email": "existing@example.com",
        "password": "Password123"
    }
    
    with pytest.raises(DuplicateError):
        await user_service.create(data)


@pytest.mark.asyncio
async def test_get_user_not_found(user_service):
    """测试获取不存在的用户"""
    with pytest.raises(NotFoundError):
        await user_service.get_by_id("non-existent-id")
```

---

## 使用指南

1. **参考示例** 编写自己的 CRUD
2. **复制粘贴** 可用代码
3. **根据项目调整** 字段和逻辑
4. **保证测试覆盖率** > 80%
