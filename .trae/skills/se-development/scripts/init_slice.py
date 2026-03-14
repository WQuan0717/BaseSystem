#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
初始化垂直切片
创建功能模块的目录结构和基础代码骨架
"""

import os
from pathlib import Path
from datetime import datetime


def init_slice(slice_name: str, module_name: str, entity_name: str):
    """
    初始化垂直切片
    
    Args:
        slice_name: 切片名称 (如：用户注册)
        module_name: 模块名称 (如：user)
        entity_name: 实体名称 (如：User)
    """
    
    # 目录结构
    dirs = [
        f"src/backend/api/routes",
        f"src/backend/api/controllers",
        f"src/backend/services",
        f"src/backend/models",
        f"src/backend/repositories",
        f"src/frontend/src/components/{module_name}",
        f"src/frontend/src/hooks/{module_name}",
        f"src/frontend/src/api/{module_name}",
        f"tests/backend/{module_name}",
        f"tests/frontend/{module_name}",
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ 创建目录：{dir_path}")
    
    # 生成后端文件
    generate_backend_files(module_name, entity_name)
    
    # 生成前端文件
    generate_frontend_files(module_name, entity_name)
    
    # 生成测试文件
    generate_test_files(module_name, entity_name)
    
    # 生成切片说明
    generate_slice_readme(slice_name, module_name, entity_name)
    
    print(f"\n✅ 垂直切片 '{slice_name}' 初始化完成!")
    print(f"下一步：实现业务逻辑")


def generate_backend_files(module_name: str, entity_name: str):
    """生成后端文件"""
    
    # Repository
    repo_content = f'''from typing import Optional, List
from src.backend.models.{module_name.lower()} import {entity_name}


class {entity_name}Repository:
    """{entity_name} 数据访问层"""
    
    def __init__(self, db):
        self.db = db
    
    def find_by_id(self, id: str) -> Optional[{entity_name}]:
        """根据 ID 查找"""
        pass
    
    def find_all(self) -> List[{entity_name}]:
        """查找所有"""
        pass
    
    def create(self, data: dict) -> {entity_name}:
        """创建记录"""
        pass
    
    def update(self, id: str, data: dict) -> Optional[{entity_name}]:
        """更新记录"""
        pass
    
    def delete(self, id: str) -> bool:
        """删除记录"""
        pass
'''
    
    with open(f"src/backend/repositories/{module_name.lower()}_repository.py", "w", encoding="utf-8") as f:
        f.write(repo_content)
    print(f"✓ 创建 Repository: {module_name.lower()}_repository.py")
    
    # Service
    service_content = f'''from typing import List, Optional
from src.backend.repositories.{module_name.lower()}_repository import {entity_name}Repository
from src.backend.models.{module_name.lower()} import {entity_name}


class {entity_name}Service:
    """{entity_name} 业务逻辑层"""
    
    def __init__(self, repository: {entity_name}Repository):
        self.repository = repository
    
    def get_by_id(self, id: str) -> Optional[{entity_name}]:
        """根据 ID 获取"""
        return self.repository.find_by_id(id)
    
    def get_all(self) -> List[{entity_name}]:
        """获取所有"""
        return self.repository.find_all()
    
    def create(self, data: dict) -> {entity_name}:
        """创建"""
        # TODO: 添加业务验证
        return self.repository.create(data)
    
    def update(self, id: str, data: dict) -> Optional[{entity_name}]:
        """更新"""
        return self.repository.update(id, data)
    
    def delete(self, id: str) -> bool:
        """删除"""
        return self.repository.delete(id)
'''
    
    with open(f"src/backend/services/{module_name.lower()}_service.py", "w", encoding="utf-8") as f:
        f.write(service_content)
    print(f"✓ 创建 Service: {module_name.lower()}_service.py")
    
    # Controller
    controller_content = f'''from fastapi import APIRouter, HTTPException
from typing import List
from src.backend.services.{module_name.lower()}_service import {entity_name}Service
from src.backend.models.{module_name.lower()} import {entity_name}Create, {entity_name}Response


router = APIRouter(prefix="/api/{module_name.lower()}", tags=["{module_name}"])


@router.get("", response_model=List[{entity_name}Response])
async def get_all(service: {entity_name}Service):
    """获取所有{module_name}"""
    return service.get_all()


@router.get("/{{id}}", response_model={entity_name}Response)
async def get_by_id(id: str, service: {entity_name}Service):
    """根据 ID 获取"""
    result = service.get_by_id(id)
    if not result:
        raise HTTPException(status_code=404, detail="资源不存在")
    return result


@router.post("", response_model={entity_name}Response, status_code=201)
async def create(data: {entity_name}Create, service: {entity_name}Service):
    """创建"""
    return service.create(data.dict())


@router.put("/{{id}}", response_model={entity_name}Response)
async def update(id: str, data: {entity_name}Create, service: {entity_name}Service):
    """更新"""
    result = service.update(id, data.dict())
    if not result:
        raise HTTPException(status_code=404, detail="资源不存在")
    return result


@router.delete("/{{id}}", status_code=204)
async def delete(id: str, service: {entity_name}Service):
    """删除"""
    if not service.delete(id):
        raise HTTPException(status_code=404, detail="资源不存在")
'''
    
    with open(f"src/backend/api/controllers/{module_name.lower()}_controller.py", "w", encoding="utf-8") as f:
        f.write(controller_content)
    print(f"✓ 创建 Controller: {module_name.lower()}_controller.py")


def generate_frontend_files(module_name: str, entity_name: str):
    """生成前端文件"""
    
    # API Client
    api_content = f'''import axios from 'axios';

export interface {entity_name} {{
  id: string;
  createdAt: string;
  updatedAt: string;
}}

export interface {entity_name}Create {{
  // 定义创建字段
}}

const API_BASE = '/api/{module_name.lower()}';

export async function get{entity_name}s(): Promise<{entity_name}[]> {{
  const response = await axios.get(API_BASE);
  return response.data;
}}

export async function get{entity_name}ById(id: string): Promise<{entity_name}> {{
  const response = await axios.get(`${{API_BASE}}/${{id}}`);
  return response.data;
}}

export async function create{entity_name}(data: {entity_name}Create): Promise<{entity_name}> {{
  const response = await axios.post(API_BASE, data);
  return response.data;
}}

export async function update{entity_name}(id: string, data: {entity_name}Create): Promise<{entity_name}> {{
  const response = await axios.put(`${{API_BASE}}/${{id}}`, data);
  return response.data;
}}

export async function delete{entity_name}(id: string): Promise<void> {{
  await axios.delete(`${{API_BASE}}/${{id}}`);
}}
'''
    
    with open(f"src/frontend/src/api/{module_name.lower()}/api.ts", "w", encoding="utf-8") as f:
        f.write(api_content)
    print(f"✓ 创建 API Client: api.ts")
    
    # Hook
    hook_content = f'''import {{ useState, useEffect }} from 'react';
import {{ get{entity_name}s, get{entity_name}ById, create{entity_name}, update{entity_name}, delete{entity_name}, {entity_name} }} from '../api/{module_name.lower()}/api';

export function use{entity_name}s() {{
  const [{entity_name}s, set{entity_name}s] = useState<{entity_name}[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetch{entity_name}s = async () => {{
    setLoading(true);
    try {{
      const data = await get{entity_name}s();
      set{entity_name}s(data);
      setError(null);
    }} catch (err) {{
      setError('加载失败');
    }} finally {{
      setLoading(false);
    }}
  }};

  useEffect(() => {{
    fetch{entity_name}s();
  }}, []);

  const create = async (data: any) => {{
    const newItem = await create{entity_name}(data);
    set{entity_name}s([...{entity_name}s, newItem]);
    return newItem;
  }};

  const update = async (id: string, data: any) => {{
    const updatedItem = await update{entity_name}(id, data);
    set{entity_name}s({entity_name}s.map(item => item.id === id ? updatedItem : item));
    return updatedItem;
  }};

  const delete_ = async (id: string) => {{
    await delete{entity_name}(id);
    set{entity_name}s({entity_name}s.filter(item => item.id !== id));
  }};

  return {{ {entity_name}s, loading, error, fetch{entity_name}s, create, update, delete_ }};
}}
'''
    
    with open(f"src/frontend/src/hooks/{module_name.lower()}/use{entity_name.lower()}.ts", "w", encoding="utf-8") as f:
        f.write(hook_content)
    print(f"✓ 创建 Custom Hook: use{entity_name.lower()}.ts")
    
    # Component
    component_content = f'''import React from 'react';
import {{ use{entity_name}s }} from '../../hooks/{module_name.lower()}/use{entity_name.lower()}';

export function {entity_name}List() {{
  const {{ {entity_name}s, loading, error }} = use{entity_name}s();

  if (loading) {{
    return <div>加载中...</div>;
  }}

  if (error) {{
    return <div>错误：{{error}}</div>;
  }}

  if ({entity_name}s.length === 0) {{
    return <div>暂无数据</div>;
  }}

  return (
    <div className="{module_name.lower()}-list">
      <h2>{entity_name}列表</h2>
      <ul>
        {{{entity_name}s.map(item => (
          <li key={{item.id}}>{{item.id}}</li>
        ))}}
      </ul>
    </div>
  );
}}
'''
    
    with open(f"src/frontend/src/components/{module_name.lower()}/{entity_name}List.tsx", "w", encoding="utf-8") as f:
        f.write(component_content)
    print(f"✓ 创建 Component: {entity_name}List.tsx")


def generate_test_files(module_name: str, entity_name: str):
    """生成测试文件"""
    
    # Backend test
    backend_test_content = f'''import pytest
from src.backend.services.{module_name.lower()}_service import {entity_name}Service


class Test{entity_name}Service:
    """{entity_name}Service 测试"""
    
    def test_create(self):
        """测试创建"""
        # TODO: 实现测试
        pass
    
    def test_get_by_id(self):
        """测试根据 ID 获取"""
        # TODO: 实现测试
        pass
    
    def test_update(self):
        """测试更新"""
        # TODO: 实现测试
        pass
    
    def test_delete(self):
        """测试删除"""
        # TODO: 实现测试
        pass
'''
    
    with open(f"tests/backend/{module_name.lower()}/test_service.py", "w", encoding="utf-8") as f:
        f.write(backend_test_content)
    print(f"✓ 创建 Backend Test: test_service.py")
    
    # Frontend test
    frontend_test_content = f'''import {{ renderHook, waitFor }} from '@testing-library/react';
import {{ use{entity_name}s }} from '../../src/hooks/{module_name.lower()}/use{entity_name.lower()}';


describe('use{entity_name}s', () => {{
  it('should load {entity_name}s on mount', async () => {{
    const {{ result }} = renderHook(() => use{entity_name}s());
    
    expect(result.current.loading).toBe(true);
    
    await waitFor(() => {{
      expect(result.current.loading).toBe(false);
    }});
    
    expect(result.current.{entity_name}s).toBeDefined();
  }});
}});
'''
    
    with open(f"tests/frontend/{module_name.lower()}/test_hook.test.tsx", "w", encoding="utf-8") as f:
        f.write(frontend_test_content)
    print(f"✓ 创建 Frontend Test: test_hook.test.tsx")


def generate_slice_readme(slice_name: str, module_name: str, entity_name: str):
    """生成切片说明"""
    
    readme_content = f'''# 垂直切片：{slice_name}

## 实现进度

- [ ] 数据库 Migration
- [ ] Repository 层
- [ ] Service 层
- [ ] Controller 层
- [ ] 前端 API Client
- [ ] 前端 Components
- [ ] 单元测试
- [ ] 集成测试

## 文件清单

### 后端
- `src/backend/repositories/{module_name.lower()}_repository.py`
- `src/backend/services/{module_name.lower()}_service.py`
- `src/backend/api/controllers/{module_name.lower()}_controller.py`

### 前端
- `src/frontend/src/api/{module_name.lower()}/api.ts`
- `src/frontend/src/hooks/{module_name.lower()}/use{entity_name.lower()}.ts`
- `src/frontend/src/components/{module_name.lower()}/{entity_name}List.tsx`

### 测试
- `tests/backend/{module_name.lower()}/test_service.py`
- `tests/frontend/{module_name.lower()}/test_hook.test.tsx`

## 测试命令

```bash
# 运行后端测试
pytest tests/backend/{module_name.lower()}/

# 运行前端测试
npm test -- {module_name.lower()}
```

## 下一步

1. 实现 Repository 层数据库操作
2. 实现 Service 层业务逻辑
3. 实现 Controller 层 API 接口
4. 实现前端组件
5. 编写单元测试
6. 运行测试验证
'''
    
    with open(f"src/{module_name.lower()}_slice_README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"✓ 创建切片说明：{module_name.lower()}_slice_README.md")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 4:
        print("用法：python init_slice.py <切片名称> <模块名> <实体名>")
        print("示例：python init_slice.py '用户注册' user User")
        sys.exit(1)
    
    slice_name = sys.argv[1]
    module_name = sys.argv[2]
    entity_name = sys.argv[3]
    
    init_slice(slice_name, module_name, entity_name)
