---
name: se-development
description: Development knowledge for software engineering. Provides methods for vertical slice development, unit testing, code standards, and implementation best practices.
---

# Development

Professional knowledge for development phase. Transform DetailedDesign.md into working code with unit tests using vertical slice development.

## Core Principles

### Principle 1: Vertical Slice Development
- Each slice is a complete feature (frontend + backend + database)
- Deliver working functionality incrementally
- Avoid horizontal layering (all frontend, then all backend)

### Principle 2: Test-Driven Development
- Write unit tests alongside code
- Coverage should be ≥ 80%
- Test behavior, not implementation

### Principle 3: Clean Code
- Follow project conventions
- Meaningful names, single responsibility
- Small functions, clear intent

### Principle 4: Incremental Delivery
- Commit frequently with clear messages
- Each commit should be a working state
- Use feature branches for isolation

## Vertical Slice Workflow

### Slice Definition

A vertical slice includes:
1. Database layer (Entity, Repository, Migration)
2. Backend layer (Service, Controller, DTO)
3. Frontend layer (Component, Hook, API call)
4. Unit tests for each layer

### Slice Order

Order slices by:
1. Core authentication/authorization
2. Main business entities CRUD
3. Business logic features
4. Secondary features

### Implementation Steps

For each slice:

```
1. Database Layer
   ├── Create migration
   ├── Define entity/model
   ├── Create repository
   └── Write repository tests

2. Backend Layer
   ├── Define DTO
   ├── Implement service
   ├── Implement controller
   └── Write unit tests

3. Frontend Layer
   ├── Create API client
   ├── Create custom hook
   ├── Implement component
   └── Write component tests

4. Integration
   ├── Run all tests
   ├── Manual verification
   └── Commit with message
```

## Code Standards

### TypeScript

```typescript
// Use explicit types
interface User {
  id: string;
  email: string;
  name: string | null;
}

// Prefer interfaces for objects
interface UserRepository {
  findById(id: string): Promise<User | null>;
  create(data: CreateUserDTO): Promise<User>;
}

// Use async/await
async function getUser(id: string): Promise<User> {
  const user = await repository.findById(id);
  if (!user) {
    throw new NotFoundError('User not found');
  }
  return user;
}
```

### React

```typescript
// Component structure
interface UserListProps {
  users: User[];
  onSelect: (user: User) => void;
}

export function UserList({ users, onSelect }: UserListProps) {
  if (users.length === 0) {
    return <EmptyState message="No users found" />;
  }

  return (
    <ul className="user-list">
      {users.map((user) => (
        <li key={user.id} onClick={() => onSelect(user)}>
          {user.name}
        </li>
      ))}
    </ul>
  );
}
```

### API Routes

```typescript
// Next.js API route
import { NextRequest, NextResponse } from 'next/server';
import { z } from 'zod';

const createSchema = z.object({
  email: z.string().email(),
  name: z.string().min(2).max(100),
});

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const data = createSchema.parse(body);
    
    const user = await userService.create(data);
    
    return NextResponse.json(
      { code: 201, data: user },
      { status: 201 }
    );
  } catch (error) {
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        { code: 400, errors: error.errors },
        { status: 400 }
      );
    }
    return NextResponse.json(
      { code: 500, message: 'Internal server error' },
      { status: 500 }
    );
  }
}
```

## Unit Testing

### Test Structure

```typescript
describe('UserService', () => {
  describe('create', () => {
    it('should create a new user with valid data', async () => {
      // Arrange
      const data = { email: 'test@example.com', name: 'Test' };
      
      // Act
      const user = await service.create(data);
      
      // Assert
      expect(user.email).toBe(data.email);
      expect(user.name).toBe(data.name);
    });

    it('should throw error for duplicate email', async () => {
      // Arrange
      const data = { email: 'existing@example.com', name: 'Test' };
      
      // Act & Assert
      await expect(service.create(data))
        .rejects.toThrow(DuplicateError);
    });
  });
});
```

### Test Coverage

| Layer | Minimum Coverage |
|-------|-----------------|
| Services | 90% |
| Repositories | 80% |
| Controllers | 80% |
| Components | 70% |

## Commit Messages

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

| Type | Description |
|------|-------------|
| feat | New feature |
| fix | Bug fix |
| docs | Documentation |
| style | Formatting |
| refactor | Code refactoring |
| test | Adding tests |
| chore | Maintenance |

### Examples

```
feat(auth): add user registration

- Implement registration endpoint
- Add email validation
- Create user entity

Closes #123
```

## Implementation_Summary.md Template

```markdown
# 实现总结

## 1. 实现概览

### 1.1 完成的功能
- [ ] 功能1
- [ ] 功能2

### 1.2 技术实现
[关键技术实现说明]

## 2. 目录结构
[实际的项目目录结构]

## 3. 已实现模块

### 3.1 模块名称
- 文件: [文件路径]
- 功能: [功能描述]
- 测试: [测试覆盖率]

## 4. 运行说明

### 4.1 环境要求
- Node.js >= 20.x
- PostgreSQL >= 16.x

### 4.2 启动命令
```bash
npm install
npm run migration:run
npm run dev
```

## 5. 已知问题
[已知的问题和限制]

## 6. 后续工作
[待完成的工作]
```

## Quality Checklist

| Check | Criteria |
|-------|----------|
| Tests Pass | All unit tests pass |
| Coverage Met | Coverage ≥ 80% |
| Code Compiles | No TypeScript errors |
| Lint Clean | No ESLint errors |
| Commits Clear | Each commit is a working state |
| Summary Updated | Implementation_Summary.md reflects reality |
