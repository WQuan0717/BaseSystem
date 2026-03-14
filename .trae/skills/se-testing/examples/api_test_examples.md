# API 测试示例

## 示例 1：用户认证 API 测试

### 测试接口

```
POST /api/auth/register
POST /api/auth/login
GET  /api/users/me
```

---

### 测试用例

#### TC-API-001: 用户注册 - 成功

**接口**: `POST /api/auth/register`

**描述**: 验证用户可以成功注册

**请求体**:
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "Password123"
}
```

**期望响应**:
- 状态码：201
- 返回用户 ID
- 不返回密码

**实际响应**:
```json
{
  "code": 201,
  "data": {
    "id": "uuid-123",
    "username": "testuser",
    "email": "test@example.com"
  }
}
```

**状态**: ✅ 通过

---

#### TC-API-002: 用户注册 - 邮箱重复

**接口**: `POST /api/auth/register`

**描述**: 验证邮箱重复时返回错误

**请求体**:
```json
{
  "username": "testuser2",
  "email": "test@example.com",
  "password": "Password123"
}
```

**期望响应**:
- 状态码：409
- 错误信息包含"邮箱已存在"

**实际响应**:
```json
{
  "code": 409,
  "errors": [
    {
      "field": "email",
      "message": "邮箱已存在"
    }
  ]
}
```

**状态**: ✅ 通过

---

#### TC-API-003: 用户登录 - 成功

**接口**: `POST /api/auth/login`

**描述**: 验证用户可以成功登录

**请求体**:
```json
{
  "email": "test@example.com",
  "password": "Password123"
}
```

**期望响应**:
- 状态码：200
- 返回 JWT Token
- Token 有效期 2 小时

**实际响应**:
```json
{
  "code": 200,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresIn": 7200
  }
}
```

**状态**: ✅ 通过

---

#### TC-API-004: 用户登录 - 密码错误

**接口**: `POST /api/auth/login`

**描述**: 验证密码错误时返回错误

**请求体**:
```json
{
  "email": "test@example.com",
  "password": "WrongPassword"
}
```

**期望响应**:
- 状态码：401
- 错误信息"密码错误"

**实际响应**:
```json
{
  "code": 401,
  "message": "密码错误"
}
```

**状态**: ✅ 通过

---

## 示例 2：CRUD API 测试

### 测试接口

```
GET    /api/users
POST   /api/users
GET    /api/users/{id}
PUT    /api/users/{id}
DELETE /api/users/{id}
```

---

### 测试脚本示例

```python
# tests/api/test_users.py
import pytest
import requests


BASE_URL = "http://localhost:8000/api"
TOKEN = None
USER_ID = None


@pytest.fixture(scope="module", autouse=True)
def setup_auth():
    """获取认证 Token"""
    login_data = {
        "email": "admin@example.com",
        "password": "Admin123"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    assert response.status_code == 200
    global TOKEN
    TOKEN = response.json()["data"]["token"]


def get_headers():
    return {"Authorization": f"Bearer {TOKEN}"}


class TestUserCRUD:
    
    def test_create_user(self):
        """测试创建用户"""
        user_data = {
            "username": "test_crud",
            "email": f"test_crud_{pytest.start_time}@example.com",
            "password": "Password123"
        }
        
        response = requests.post(
            f"{BASE_URL}/users",
            json=user_data,
            headers=get_headers()
        )
        
        assert response.status_code == 201
        data = response.json()
        assert data["username"] == user_data["username"]
        assert "id" in data
        
        global USER_ID
        USER_ID = data["id"]
    
    def test_get_all_users(self):
        """测试获取用户列表"""
        response = requests.get(
            f"{BASE_URL}/users",
            headers=get_headers()
        )
        
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
    
    def test_get_user_by_id(self):
        """测试根据 ID 获取用户"""
        response = requests.get(
            f"{BASE_URL}/users/{USER_ID}",
            headers=get_headers()
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == USER_ID
    
    def test_get_user_not_found(self):
        """测试获取不存在的用户"""
        response = requests.get(
            f"{BASE_URL}/users/non-existent-id",
            headers=get_headers()
        )
        
        assert response.status_code == 404
    
    def test_update_user(self):
        """测试更新用户"""
        update_data = {
            "username": "updated_username"
        }
        
        response = requests.put(
            f"{BASE_URL}/users/{USER_ID}",
            json=update_data,
            headers=get_headers()
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == update_data["username"]
    
    def test_delete_user(self):
        """测试删除用户"""
        response = requests.delete(
            f"{BASE_URL}/users/{USER_ID}",
            headers=get_headers()
        )
        
        assert response.status_code == 204
        
        # 验证已删除
        response = requests.get(
            f"{BASE_URL}/users/{USER_ID}",
            headers=get_headers()
        )
        assert response.status_code == 404
```

---

## 运行测试

```bash
# 使用脚本运行
python .trae/skills/se-testing/scripts/run_api_tests.py http://localhost:8000

# 使用 pytest 运行
pytest tests/api/test_users.py -v

# 生成覆盖率报告
pytest --cov=src tests/
```

---

## 使用指南

1. **参考示例** 编写自己的测试
2. **使用模板** 记录测试用例
3. **运行脚本** 自动化测试
4. **生成报告** TestReport.md
