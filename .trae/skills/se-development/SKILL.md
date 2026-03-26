---
name: se-development
description: Development knowledge for software engineering. Provides methods for vertical slice development, unit testing, code standards, and implementation best practices.
---

# Development

Professional knowledge for development phase. Transform DetailedDesign.md into working code with unit tests using vertical slice development.

**Previous Skill**: se-detailed-design (reads DetailedDesign.md)

**Next Skill**: webapp-testing (after development is complete)

## Core Principles

### Principle 1: Frontend-First with Mock Data
- Develop complete frontend first using mock data
- Frontend includes all page layouts and interactions
- Mock data simulates backend responses
- Frontend should be independently complete before backend starts

### ⚠️ MANDATORY PHASE GATES

**Before starting frontend development:**
- [ ] UI/UX Design completed (ui-ux-pro-max + frontend-design)
- [ ] Design system documented (colors, typography, components)

**Before starting backend development:**
- [ ] All frontend pages exist (check: `ls src/views/`)
- [ ] Mock data structure exists (check: `ls src/mocks/`)
- [ ] Frontend can run standalone with mock data

**Before proceeding to testing:**
- [ ] Backend features implemented with E2E tests
- [ ] All E2E tests pass (including regression)
- [ ] TestReport.md generated

**⚠️ DO NOT skip these gates! Each gate MUST be verified before proceeding.**

### Principle 2: Backend Vertical Iteration
- Backend developed feature by feature, not all at once
- Each feature includes: API + Database operations + Business logic
- After each feature, run E2E tests (including regression)
- Next feature can only use already-tested features
- Foundation features (auth, infrastructure) must be developed first

### Principle 3: Test-Driven Development
- Write unit tests alongside code
- Coverage should be ≥ 80%
- Test behavior, not implementation

### Principle 4: Frontend Change Verification
**MANDATORY: After ANY frontend modification, run:**
1. Type check: `npm run type-check`
2. ESLint: `npm run lint`
3. Unit tests: `npm test`
4. Playwright E2E tests: `cd tests/e2e && playwright test`
5. Check screenshots in `tests/e2e/screenshots/`

### Principle 5: Environment Setup Strategy

**Database Services: Use Docker (start once, run long-term)**
```bash
# Start MySQL
docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:8

# Start Redis
docker run -d --name redis -p 6379:6379 redis:7

# Stop when done
docker stop mysql redis
```

**Backend & Frontend: Use Local Development (fast iteration, easy debug)**
```bash
# Backend (local)
cd backend && npm install && npm run dev

# Frontend (local)
cd frontend && npm install && npm run dev
```

**Why this strategy?**
| Component | Docker | Local | Reason |
|-----------|--------|-------|--------|
| Database | ✅ Start once | ❌ Complex setup | Easy start/stop, no local install |
| Backend | ❌ Rebuild image each time | ✅ Fast iteration | Quick code changes, hot reload |
| Frontend | ❌ Rebuild image each time | ✅ Hot reload | Quick code changes, fast debug |

**Connection strings:**
```bash
# Backend connects to Docker database
DATABASE_URL=mysql://localhost:3306/mydb

# Frontend connects to local backend
VITE_API_BASE_URL=http://localhost:8000
```

**When to use Docker for backend/frontend:**
- Production deployment
- CI/CD pipelines
- Testing exact production environment

**When to use local development:**
- During active development
- Debugging
- Quick iteration

### Principle 6: Port Conflict Resolution

**SMART Decision Process for Port Conflicts:**

```
1. Check if service is already running in current terminal
   ├─ YES: Use existing service (don't start new one)
   └─ NO: Continue to step 2
           ↓
2. Check port conflict
   └─ Port is FREE: Start service directly
           ↓
   Port is OCCUPIED: Analyze what is using it
           ↓
   ┌─────────────────────────────────────────┐
   │  What is using the port?                 │
   ├─────────────────────────────────────────┤
   │  This Project's Service?                  │
   │  ├─ YES: Kill existing process, use port │
   │  │   (It should not be running twice)    │
   │  │                                        │
   │  └─ NO (Other project's service)          │
   │      └─ Change to different port          │
   │         (Don't kill other project's work) │
   └─────────────────────────────────────────┘
```

**Decision Rules:**

| Situation | Action | Reason |
|-----------|--------|--------|
| Service already running in this terminal | Use existing | Don't duplicate |
| Port occupied by THIS project | Kill process, reuse port | Should only run once |
| Port occupied by OTHER project | Change to different port | Don't disrupt other work |

**How to Check:**

```bash
# Step 1: Check if service is already running
# Look at current terminal - is there a running dev server?

# Step 2: Check what is using the port
netstat -ano | findstr :8000

# Example output:
# TCP    0.0.0.0:8000    0.0.0.0:0    LISTENING    12345

# Step 3: Check what process 12345 is
tasklist /FI "PID eq 12345"
# Or on Linux/Mac:
# lsof -i :8000

# Step 4: Analyze and decide
# If it's node.exe/python.exe running YOUR project → Kill it
# If it's another project's service → Change port
```

**Port Change Rule:**
- This project ports: 3000 (frontend), 8000 (backend), 3306 (mysql), 6379 (redis)
- If conflict and it's not this project: Change to 3001, 8001, 3307, 6378

### Principle 7: Clean Code
- Follow project conventions
- Meaningful names, single responsibility
- Small functions, clear intent

### Principle 8: Incremental Delivery
- Commit frequently with clear messages
- Each commit should be a working state
- Use feature branches for isolation

### Principle 9: Environment-Aware Configuration
- Use environment variables for all API/interface URLs
- Support multiple environments: local, Docker, production
- Never hardcode interface URLs

### Principle 10: WSL2 Compatibility
- Current environment: WSL2 (Ubuntu 24.04)
- Use `ls -la` instead of `ls` to check files
- Some tools may not work in WSL, use appropriate commands

### Principle 11: Test File Management
- Test files are never deleted after use
- Create new test files in `test_to_be_deleted/` directory
- This allows later review and reuse

## Development Workflow (Frontend-First + Backend Vertical Iteration)

This workflow combines the best of waterfall (complete frontend design first) and agile (vertical feature iteration).

### Phase 1: UI/UX Foundation

**Before writing business code, establish UI/UX foundation:**

1. **ui-ux-pro-max** - Query design system recommendations
   ```bash
   python3 skills/ui-ux-pro-max/scripts/search.py "<project type> <keywords>" --design-system
   ```
   - Returns style, color, typography suggestions
   - Establishes visual language

2. **frontend-design** - Generate UI code based on recommendations
   - Create consistent components
   - Establish design tokens (CSS variables)
   - Build page layouts and interactions

### Phase 2: Frontend Development (with Mock Data)

**Goal: Complete all frontend before backend starts**

1. **Create Mock Data Structure**
   ```
   src/mocks/
   ├── data/           # Mock data files
   │   ├── users.json
   │   ├── articles.json
   │   └── comments.json
   ├── handlers/       # Mock API handlers
   │   ├── auth.ts
   │   ├── users.ts
   │   ├── articles.ts
   │   └── comments.ts
   └── index.ts        # Mock server entry
   ```

2. **Mock Data Rules**
   - Each API endpoint has a mock handler
   - Mock data covers all possible responses (success, error, edge cases)
   - Mock handlers mirror real API structure exactly
   - Use realistic data, not "test1", "test2"

3. **Frontend Development with Mock**
   - All pages and components use mock API
   - All interactions and states handled
   - Loading, error, empty states all implemented
   - Frontend is **independently complete**

4. **Verify Frontend Completeness**
   - All pages render correctly
   - All interactions work
   - All edge cases handled
   - No placeholder comments like "// TODO: implement later"

### ⚠️ MANDATORY: QA Review After Frontend + Mock

**After frontend with mock data is complete, BEFORE starting backend:**

```
Frontend + Mock Complete
    ↓
Invoke QA Engineer (UI/UX Review)
    ↓
QA Engineer:
- Takes screenshots
- Evaluates visual design
- Checks design consistency
- Reports design issues
    ↓
Development AI fixes design problems
    ↓
QA Engineer approves design
    ↓
ONLY THEN proceed to backend
```

**Why this gate?**
- Early design issues are cheap to fix
- Late design issues (after backend) are expensive
- Frontend style should be finalized before backend integration

### Phase 3: Backend Vertical Iteration

**Goal: Implement backend features one by one, each with full testing**

**Backend Feature Order:**
```
1. Foundation (MUST be first)
   ├── Authentication/Authorization
   ├── Database connection
   └── Basic API structure

2. Core CRUD (based on frontend needs)
   ├── User management
   ├── Main entity operations
   └── Related entity operations

3. Business Logic
   └── Complex features
```

**For Each Backend Feature:**

```
1. Implement Feature
   ├── Database layer (Entity, Migration)
   ├── Service layer (Business logic)
   ├── Controller layer (API endpoints)
   └── DTO/Validation

2. Replace Mock with Real API
   ├── Frontend calls real backend
   ├── Remove mock import
   └── Keep same interface

3. Run E2E Tests (REGRESSION REQUIRED)
   ├── Current feature works
   ├── All previous features still work
   └── No regression in existing functionality

4. Commit
   └── Clear message: "feat: implement user CRUD with E2E tests"
```

### Phase 4: Handoff Preparation (Before User Testing)

**Goal: Prepare system for user verification - user can run and test immediately**

**Step 1: Start Services (Smart Port Conflict Resolution)**
```bash
# 1. Check if services already running
# Look at current terminal

# 2. If not running, start required services:
# Database (Docker - start once)
docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:8
docker run -d --name redis -p 6379:6379 redis:7
# For projects needing Elasticsearch:
docker run -d --name elasticsearch -p 9200:9200 -e discovery.type=single-node elasticsearch:8

# 3. Backend (Local - fast iteration)
cd backend && npm install && npm run dev

# 4. Frontend (Local - hot reload)
cd frontend && npm install && npm run dev
```

**Step 2: Prepare Test Accounts**
```bash
# Create test accounts with different roles (if multi-role system)
# Admin account
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","email":"admin@test.com","password":"Admin123!","role":"admin"}'

# User account
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"user","email":"user@test.com","password":"User123!","role":"user"}'

# Guest account (if applicable)
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"guest","email":"guest@test.com","password":"Guest123!","role":"guest"}'
```

**Step 3: Document Test Credentials**
```markdown
## Test Accounts for User Verification

| Role | Email | Password | Permissions |
|------|-------|----------|-------------|
| Admin | admin@test.com | Admin123! | Full access |
| User | user@test.com | User123! | Standard access |
| Guest | guest@test.com | Guest123! | Limited access |

**Registration is also available - users can register their own accounts.**
```

**Step 4: Verify System is Ready**
```bash
# Check backend is running
curl http://localhost:8000/api/health

# Check frontend is running
curl http://localhost:5173

# Verify login works
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@test.com","password":"Admin123!"}'
```

**Step 5: Document How to Run**
```markdown
## Quick Start Guide

### 1. Start Database Services (Docker)
```bash
docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:8
docker run -d --name redis -p 6379:6379 redis:7
```

### 2. Start Backend
```bash
cd backend
npm install
npm run dev
```

### 3. Start Frontend
```bash
cd frontend
npm install
npm run dev
```

### 4. Access System
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### 5. Test Accounts
- Admin: admin@test.com / Admin123!
- User: user@test.com / User123!
```

### Why This Order?

| Phase | Benefit |
|-------|---------|
| UI/UX Foundation | Consistent design system, no AI slop |
| Frontend with Mock | Complete UI before backend, parallel work possible |
| Backend Vertical | Each feature tested, no regression, agile iteration |

### Comparison with Traditional Approaches

| Approach | Frontend | Backend | Testing | Limitation |
|----------|----------|---------|---------|-------------|
| Traditional Waterfall | Incomplete until end | Late | Late | Frontend dependent on backend |
| Traditional Vertical Slices | Mixed with backend | Mixed with frontend | Late | UI design inconsistent |
| **This Approach** | Complete first | Feature by feature | After each feature | Best of both worlds |

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
