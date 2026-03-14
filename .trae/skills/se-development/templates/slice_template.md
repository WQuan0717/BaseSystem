# 垂直切片开发模板

## 切片开发流程

```bash
# 1. 初始化切片
python .trae/skills/se-development/scripts/init_slice.py "用户注册" user User

# 2. 实现数据库层
# 编辑：src/backend/models/user.py
# 编辑：src/backend/repositories/user_repository.py

# 3. 实现业务层
# 编辑：src/backend/services/user_service.py

# 4. 实现 API 层
# 编辑：src/backend/api/controllers/user_controller.py

# 5. 实现前端
# 编辑：src/frontend/src/api/user/api.ts
# 编辑：src/frontend/src/hooks/user/useUser.ts
# 编辑：src/frontend/src/components/user/UserList.tsx

# 6. 运行测试
pytest tests/backend/user/
npm test -- user
```

---

## 切片目录结构

```
src/
├── backend/
│   ├── models/
│   │   └── user.py
│   ├── repositories/
│   │   └── user_repository.py
│   ├── services/
│   │   └── user_service.py
│   └── api/
│       └── controllers/
│           └── user_controller.py
├── frontend/
│   └── src/
│       ├── api/
│       │   └── user/
│       │       └── api.ts
│       ├── hooks/
│       │   └── user/
│       │       └── useUser.ts
│       └── components/
│           └── user/
│               └── UserList.tsx
└── tests/
    ├── backend/
    │   └── user/
    │       └── test_service.py
    └── frontend/
        └── user/
            └── test_hook.test.tsx
```

---

## 测试覆盖率检查

```bash
# 后端覆盖率
pytest --cov=src/backend tests/backend/
coverage html

# 前端覆盖率
npm test -- --coverage
```

---

## Commit 模板

```bash
git commit -m "feat(user): 实现用户注册功能

- 实现 UserRepository
- 实现 UserService
- 实现 UserController
- 实现前端组件
- 添加单元测试

Closes #123"
```

---

## 使用指南

1. **运行 init_slice.py** 生成骨架
2. **按顺序实现** 各层代码
3. **编写测试** 保证覆盖率
4. **运行检查** 确保质量
