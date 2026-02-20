---
name: se-testing
description: Testing knowledge for software engineering. Provides methods for API testing, E2E testing, test case design, and TestReport.md generation.
---

# Testing

Professional knowledge for testing phase. Validate code quality through API testing, E2E testing, and generate TestReport.md.

## Core Principles

### Principle 1: Test Coverage First
- All P0 features must have test cases
- Critical paths must have E2E tests
- Edge cases must have unit tests

### Principle 2: Independent Tests
- Each test should be independent
- No shared state between tests
- Tests should be repeatable

### Principle 3: Clear Test Documentation
- Test cases should be self-documenting
- Include preconditions, steps, expected results
- Document test data requirements

### Principle 4: Risk-Based Testing
- Prioritize testing based on risk and impact
- P0 features get most testing effort
- Focus on critical user paths

### Principle 5: Automation First
- Automate all repetitive tests
- API tests should be fully automated
- E2E tests for critical flows

## Test Types

| Type | Purpose | Tools |
|------|---------|-------|
| Unit Tests | Test individual functions | Jest, Vitest |
| Integration Tests | Test module interactions | Jest, Supertest |
| API Tests | Test API endpoints | Postman, curl |
| E2E Tests | Test user flows | Playwright, Cypress |
| Performance Tests | Test load and response | k6, Artillery |

## Test Case Design

### Test Case Template

```markdown
### TC-001: [Test Case Name]

**Priority**: P0/P1/P2

**Type**: Functional/API/E2E

**Preconditions**:
- Condition 1
- Condition 2

**Test Data**:
```json
{
  "email": "test@example.com",
  "password": "Test@123"
}
```

**Steps**:
1. Step 1
2. Step 2
3. Step 3

**Expected Result**:
- Result 1
- Result 2

**Actual Result**:
[To be filled during execution]

**Status**: Pass/Fail/Blocked
```

### Test Scenarios

**Authentication:**
- TC-001: User registration with valid data
- TC-002: User registration with duplicate email
- TC-003: User login with valid credentials
- TC-004: User login with invalid password
- TC-005: Token refresh

**CRUD Operations:**
- TC-010: Create resource with valid data
- TC-011: Create resource with invalid data
- TC-012: Read resource by ID
- TC-013: Update resource
- TC-014: Delete resource

**Edge Cases:**
- TC-020: Empty input validation
- TC-021: Maximum length validation
- TC-022: Special characters handling
- TC-023: Concurrent access

## API Testing

### Test Structure

```typescript
describe('POST /api/v1/users', () => {
  it('should create user with valid data', async () => {
    const response = await request(app)
      .post('/api/v1/users')
      .send({
        email: 'test@example.com',
        password: 'Test@123',
        name: 'Test User'
      });

    expect(response.status).toBe(201);
    expect(response.body.data.email).toBe('test@example.com');
  });

  it('should return 400 for invalid email', async () => {
    const response = await request(app)
      .post('/api/v1/users')
      .send({
        email: 'invalid-email',
        password: 'Test@123'
      });

    expect(response.status).toBe(400);
    expect(response.body.errors).toBeDefined();
  });
});
```

### API Test Checklist

| Check | Description |
|-------|-------------|
| Status Code | Correct HTTP status |
| Response Body | Correct data structure |
| Headers | Correct headers |
| Validation | Input validation works |
| Authentication | Auth required endpoints |
| Error Handling | Error responses correct |

## E2E Testing

### Playwright Example

```typescript
import { test, expect } from '@playwright/test';

test('user can register and login', async ({ page }) => {
  // Navigate to registration
  await page.goto('/register');
  
  // Fill form
  await page.fill('[name="email"]', 'test@example.com');
  await page.fill('[name="password"]', 'Test@123');
  await page.fill('[name="confirmPassword"]', 'Test@123');
  
  // Submit
  await page.click('button[type="submit"]');
  
  // Verify redirect to dashboard
  await expect(page).toHaveURL('/dashboard');
  
  // Logout
  await page.click('[data-testid="logout"]');
  
  // Login
  await page.goto('/login');
  await page.fill('[name="email"]', 'test@example.com');
  await page.fill('[name="password"]', 'Test@123');
  await page.click('button[type="submit"]');
  
  // Verify logged in
  await expect(page.locator('[data-testid="user-email"]'))
    .toHaveText('test@example.com');
});
```

### E2E Test Scenarios

| Scenario | Priority |
|----------|----------|
| User registration flow | P0 |
| User login flow | P0 |
| Password reset flow | P1 |
| Profile update flow | P1 |
| Main business flow | P0 |

## TestReport.md Template

```markdown
# 测试报告

## 1. 测试概览

### 1.1 测试范围
[测试覆盖的功能和模块]

### 1.2 测试环境
- 操作系统: [OS]
- 浏览器: [Browser]
- 数据库: [Database]
- 测试时间: [Date]

### 1.3 测试统计

| 指标 | 数值 |
|------|------|
| 测试用例总数 | X |
| 通过数 | X |
| 失败数 | X |
| 阻塞数 | X |
| 通过率 | X% |

## 2. 测试结果

### 2.1 功能测试

| 用例ID | 用例名称 | 优先级 | 状态 |
|--------|----------|--------|------|
| TC-001 | 用户注册 | P0 | Pass |
| TC-002 | 用户登录 | P0 | Pass |

### 2.2 API 测试

| 接口 | 方法 | 状态 | 备注 |
|------|------|------|------|
| /api/v1/users | POST | Pass | - |

### 2.3 E2E 测试

| 场景 | 状态 | 备注 |
|------|------|------|
| 注册登录流程 | Pass | - |

## 3. 问题清单

### 3.1 严重问题 (P0)
| 编号 | 描述 | 状态 |
|------|------|------|
| - | 无 | - |

### 3.2 一般问题 (P1)
| 编号 | 描述 | 状态 |
|------|------|------|
| BUG-001 | 问题描述 | Open |

### 3.3 建议改进 (P2)
| 编号 | 描述 | 状态 |
|------|------|------|
| - | 无 | - |

## 4. 测试结论

### 4.1 质量评估
[对系统质量的总体评价]

### 4.2 发布建议
- [ ] 可以发布
- [ ] 需要修复 P0 问题后发布
- [ ] 不建议发布

### 4.3 风险提示
[潜在的风险和注意事项]
```

## Quality Checklist

| Check | Criteria |
|-------|----------|
| P0 Coverage | All P0 features have test cases |
| API Tested | All endpoints tested |
| E2E Critical | Critical flows have E2E tests |
| Issues Documented | All bugs documented |
| Report Complete | TestReport.md follows template |
