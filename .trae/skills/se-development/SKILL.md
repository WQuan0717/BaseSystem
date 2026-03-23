---
name: se-development
description: Development knowledge for software engineering. Provides methods for vertical slice development, unit testing, code standards, and implementation best practices.
---

# Development

Professional knowledge for development phase. Transform DetailedDesign.md into working code with unit tests using vertical slice development.

**Previous Skill**: se-detailed-design (reads DetailedDesign.md)

**Next Skill**: se-testing (after development is complete)

## Core Principles

### Principle 1: Vertical Slice Development
- Each slice is a complete feature (frontend + backend + database)
- Deliver working functionality incrementally
- Avoid horizontal layering (all frontend, then all backend)

### Principle 2: Test-Driven Development
- Write unit tests alongside code
- Coverage should be ≥ 80%
- Test behavior, not implementation

### Principle 3: Frontend Change Verification
**MANDATORY: After ANY frontend modification, run:**
1. Type check: `npm run type-check`
2. ESLint: `npm run lint`
3. Unit tests: `npm test`
4. Playwright E2E tests: `cd tests/e2e && playwright test`
5. Check screenshots in `tests/e2e/screenshots/`

### Principle 4: Port Conflict Resolution
**Before starting services, check for port conflicts:**
```bash
# Check port 8000 (backend)
netstat -ano | findstr :8000

# Check port 3000 (frontend)
netstat -ano | findstr :3000

# If port is occupied, kill the process and restart
# DO NOT change to a different port
taskkill /F /PID <process_id>
```

### Principle 5: Clean Code
- Follow project conventions
- Meaningful names, single responsibility
- Small functions, clear intent

### Principle 6: Incremental Delivery
- Commit frequently with clear messages
- Each commit should be a working state
- Use feature branches for isolation

### Principle 7: Environment-Aware Configuration
- Use environment variables for all API/interface URLs
- Support multiple environments: local, Docker, production
- Never hardcode interface URLs

### Principle 8: WSL2 Compatibility
- Current environment: WSL2 (Ubuntu 24.04)
- Use `ls -la` instead of `ls` to check files
- Some tools may not work in WSL, use appropriate commands

### Principle 9: Test File Management
- Test files are never deleted after use
- Create new test files in `test_to_be_deleted/` directory
- This allows later review and reuse

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

### Commit Granularity

**When to commit:**
- After completing each vertical slice (user story)
- After fixing a bug
- After updating documentation
- Before switching to another task

**What each commit should contain:**
- One complete feature or fix
- Working state (all tests pass)
- Clear, descriptive message

**Commit size guidelines:**
| Slice Size | Files | Lines | When to Commit |
|------------|-------|-------|----------------|
| Small | 1-5 | < 100 | Daily |
| Medium | 5-15 | 100-500 | After completion |
| Large | 15+ | 500+ | Split into smaller slices |

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

**IMPORTANT: All checks must be ACTUALLY EXECUTED, not just declared. You must run the commands and verify the results.**

### Pre-Development Verification

| Check | Command to Run | Expected Result |
|-------|----------------|-----------------|
| Node.js available | `node --version` | Version displayed |
| Package manager available | `npm --version` or `pnpm --version` | Version displayed |

### Post-Implementation Verification

| Check | Command to Run | Expected Result |
|-------|----------------|-----------------|
| Dependencies installed | `npm install` or `pnpm install` | No errors, node_modules created |
| Entry point exists | Check `src/index.tsx` or `src/main.tsx` or `index.html` | File exists and is not empty |
| Code compiles | `npm run build` or `npm run type-check` | Build successful, no errors |
| Lint clean | `npm run lint` | No lint errors |
| Unit tests pass | `npm test` | All tests pass |
| Coverage met | `npm test -- --coverage` | Coverage ≥ 80% for services |
| Dev server starts | `npm run dev` | Server starts without errors |

### Final Verification

| Check | Command to Run | Expected Result |
|-------|----------------|-----------------|
| **Frontend page loads** | Open browser to `localhost:PORT` | Page renders without errors |
| **Backend API responds** | `curl localhost:PORT/api/health` or similar | API responds with 200 |
| **Database connection** | Check application logs | No database connection errors |
| Commits clear | `git log` | Each commit is a working state |
| Summary updated | Review Implementation_Summary.md | Document reflects actual implementation |

## Environment-Aware API Configuration

### Configuration Template

For frontend applications, use environment variables with fallback logic:

```typescript
// src/config/api.ts
const isDocker = import.meta.env.VITE_DOCKER_ENV === 'true';

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL    // 1. Manual override first
  || (isDocker ? '' : 'http://localhost:8000');                  // 2. Otherwise, auto-detect by environment
```

### Environment Variable Convention

| Variable | Purpose | Example |
|---------|---------|---------|
| `VITE_API_BASE_URL` | Manual API base URL override | `https://api.example.com` |
| `VITE_DOCKER_ENV` | Docker environment flag | `true` or `false` |

### Backend Configuration (Python/FastAPI)

```python
# backend/config.py
import os

class Config:
    # Docker environment
    DOCKER_ENV = os.getenv("DOCKER_ENV", "false") == "true"

    # API URL based on environment
    API_BASE_URL = os.getenv("VITE_API_BASE_URL") or \
                   ("http://nginx:80" if DOCKER_ENV else "http://localhost:8000")
```

### Usage Rules

1. **Never hardcode URLs**: Always use environment variables
2. **Support local dev**: `localhost:8000` for backend
3. **Support Docker**: Use container service names (e.g., `nginx`)
4. **Support production**: Use configured production URLs

### Example .env File

```bash
# .env.development
VITE_DOCKER_ENV=false
VITE_API_BASE_URL=

# .env.production
VITE_DOCKER_ENV=false
VITE_API_BASE_URL=https://api.production.com

# .env.docker
VITE_DOCKER_ENV=true
VITE_API_BASE_URL=
```
