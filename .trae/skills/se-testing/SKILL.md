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

## Test Case Design Methods

### 1. Equivalence Partitioning (等价类划分)

Divide input data into valid and invalid equivalence classes.

**Example: Username validation (6-20 characters)**

| Test Case | Input | Expected | Class |
|-----------|-------|----------|-------|
| TC-001 | "testuser" | Valid | Valid equivalence |
| TC-002 | "ab" | Invalid | Too short |
| TC-003 | "verylongusername123" | Invalid | Too long |
| TC-004 | "test@user" | Invalid | Invalid characters |

### 2. Boundary Value Analysis (边界值分析)

Test at the boundaries of input domains.

**Example: Age field (18-65)**

| Test Case | Input | Expected | Boundary |
|-----------|-------|----------|----------|
| TC-001 | 17 | Invalid | Below minimum |
| TC-002 | 18 | Valid | Minimum boundary |
| TC-003 | 19 | Valid | Just above minimum |
| TC-004 | 64 | Valid | Just below maximum |
| TC-005 | 65 | Valid | Maximum boundary |
| TC-006 | 66 | Invalid | Above maximum |

### 3. Orthogonal Array Testing (正交实验法)

For multi-factor combinations, use orthogonal arrays to reduce test cases.

**Example: Login with different browsers and user roles**

| Test Case | Browser | User Role | Network |
|-----------|---------|-----------|---------|
| TC-001 | Chrome | Admin | WiFi |
| TC-002 | Firefox | User | 4G |
| TC-003 | Safari | Guest | 3G |

### 4. Error Guessing (错误推测法)

Based on experience, guess where errors might occur.

**Common error scenarios:**
- Null/empty inputs
- Special characters in input
- Concurrent operations
- Network failures
- Database connection failures
- Timeout scenarios

### 5. State Transition Testing (状态转换测试)

Test transitions between system states.

**Example: Order status transitions**

```
Created → Paid → Shipped → Delivered
   ↓        ↓       ↓         ↓
Cancelled  Refund  Return   Complete
```

## Test Case Template

```markdown
### TC-[ID]: [Test Name]

**Module**: [Module Name]

**Test Method**: [Equivalence/Boundary/Orthogonal/Error Guessing]

**Preconditions**:
- [Condition 1]
- [Condition 2]

**Test Data**:
```json
{
  "field": "value"
}
```

**Test Steps**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected Result**:
- [Expected 1]
- [Expected 2]

**Actual Result**: [Fill after execution]

**Status**: ⬜ Pass ⬜ Fail ⬜ Blocked
```

## Playwright E2E Testing

### Directory Structure

```
tests/e2e/
├── tests/
│   ├── auth.spec.ts        # Authentication tests
│   ├── user.spec.ts        # User management tests
│   └── order.spec.ts       # Order flow tests
├── screenshots/
│   ├── auth/
│   ├── user/
│   └── order/
├── videos/
└── playwright.config.ts
```

### Frontend Change Verification

**Mandatory check after ANY frontend modification:**

```bash
# 1. Run type check
npm run type-check

# 2. Run ESLint
npm run lint

# 3. Run unit tests
npm test

# 4. Run Playwright E2E tests
cd tests/e2e
playwright test

# 5. Check screenshots for visual regressions
# Screenshots saved in tests/e2e/screenshots/
```

### Screenshot Comparison

```typescript
// tests/e2e/tests/visual.spec.ts
import { test, expect } from '@playwright/test';

test('visual regression - homepage', async ({ page }) => {
  await page.goto('/');
  
  // Take screenshot and compare with baseline
  await expect(page).toHaveScreenshot('homepage.png', {
    fullPage: true,
    maxDiffPixels: 100, // Allow small differences
  });
});
```

## API Testing

### Test Coverage Requirements

| Layer | Minimum Coverage |
|-------|-----------------|
| Services | 90% |
| Repositories | 80% |
| Controllers | 80% |
| API Endpoints | 100% |

### API Test Example

```python
# tests/api/test_users.py
import pytest


class TestUserAPI:
    """User API tests with comprehensive coverage"""
    
    # Equivalence partitioning
    def test_create_user_valid_data(self):
        """Valid user creation"""
        pass
    
    def test_create_user_invalid_email(self):
        """Invalid email format"""
        pass
    
    # Boundary value analysis
    def test_create_user_username_min_length(self):
        """Username at minimum length (3 chars)"""
        pass
    
    def test_create_user_username_max_length(self):
        """Username at maximum length (50 chars)"""
        pass
    
    # Error guessing
    def test_create_user_duplicate_email(self):
        """Duplicate email should fail"""
        pass
    
    def test_create_user_sql_injection(self):
        """SQL injection attempt should fail"""
        pass
```

## Test Report Template

```markdown
# Test Report

## Test Summary

| Metric | Value |
|--------|-------|
| Total Test Cases | 0 |
| Passed | 0 |
| Failed | 0 |
| Blocked | 0 |
| Pass Rate | 0% |

## Test Coverage

| Module | Coverage |
|--------|----------|
| Services | 0% |
| Controllers | 0% |
| API | 0% |

## Defects Found

| ID | Severity | Description | Status |
|----|----------|-------------|--------|
| BUG-001 | High | [Description] | Open |

## Test Environment

- **OS**: [Operating System]
- **Browser**: [Browser Version]
- **Database**: [Database Version]
- **Test Date**: [Date]

## Conclusion

⬜ Pass - Ready for release
⬜ Conditional Pass - Minor issues to fix
⬜ Fail - Critical issues found
```

## Quality Checklist

| Check | Criteria |
|-------|----------|
| Test Design | Used standard methods (equivalence, boundary, etc.) |
| Coverage | All P0 features covered |
| Independence | Each test is independent |
| Documentation | Clear test cases with expected results |
| Automation | Repetitive tests automated |
| E2E Tests | Critical user paths tested |
| Visual Tests | Playwright screenshots for UI changes |
