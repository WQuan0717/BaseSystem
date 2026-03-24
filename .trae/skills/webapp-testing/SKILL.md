---
name: webapp-testing
description: Toolkit for testing web applications. Provides test case design methods, Playwright automation, API testing, and test report generation.
license: Complete terms in LICENSE.txt
---

# Web Application Testing

Comprehensive testing toolkit that combines test case design methodology with Playwright automation.

## Testing Workflow

```
1. Design test cases using standard methods
2. Execute tests using Playwright automation
3. Generate TestReport.md
```

## Test Case Design Methods

### 1. Equivalence Partitioning

Divide input data into valid and invalid equivalence classes.

**Example: Username validation (6-20 characters)**

| Test Case | Input | Expected | Class |
|-----------|-------|----------|-------|
| TC-001 | "testuser" | Valid | Valid equivalence |
| TC-002 | "ab" | Invalid | Too short |
| TC-003 | "verylongusername123" | Invalid | Too long |
| TC-004 | "test@user" | Invalid | Invalid characters |

### 2. Boundary Value Analysis

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

### 3. Orthogonal Array Testing

For multi-factor combinations, use orthogonal arrays to reduce test cases.

**Example: Login with different browsers and user roles**

| Test Case | Browser | User Role | Network |
|-----------|---------|-----------|---------|
| TC-001 | Chrome | Admin | WiFi |
| TC-002 | Firefox | User | 4G |
| TC-003 | Safari | Guest | 3G |

### 4. Error Guessing

Based on experience, guess where errors might occur.

**Common error scenarios:**
- Null/empty inputs
- Special characters in input
- Concurrent operations
- Network failures
- Database connection failures
- Timeout scenarios

### 5. State Transition Testing

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

## Test Coverage Requirements

| Layer | Minimum Coverage |
|-------|-----------------|
| Services | 90% |
| Repositories | 80% |
| Controllers | 80% |
| API Endpoints | 100% |

## Playwright Automation

**Helper Scripts Available**:
- `scripts/with_server.py` - Manages server lifecycle (supports multiple servers)

**Always run scripts with `--help` first** to see usage. DO NOT read the source until you try running the script first and find that a customized solution is absolutely necessary.

### Decision Tree

```
User task → Is it static HTML?
    ├─ Yes → Read HTML file directly to identify selectors
    │         ├─ Success → Write Playwright script using selectors
    │         └─ Fails/Incomplete → Treat as dynamic (below)
    │
    └─ No (dynamic webapp) → Is the server already running?
        ├─ No → Run: python scripts/with_server.py --help
        │        Then use the helper + write simplified Playwright script
        │
        └─ Yes → Reconnaissance-then-action:
            1. Navigate and wait for networkidle
            2. Take screenshot or inspect DOM
            3. Identify selectors from rendered state
            4. Execute actions with discovered selectors
```

### Example: Using with_server.py

**Single server:**
```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
```

**Multiple servers (e.g., backend + frontend):**
```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python your_automation.py
```

### Automation Script Template

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:5173')
    page.wait_for_load_state('networkidle')
    # ... your automation logic
    browser.close()
```

### Reconnaissance-Then-Action Pattern

1. **Inspect rendered DOM**:
   ```python
   page.screenshot(path='/tmp/inspect.png', full_page=True)
   content = page.content()
   page.locator('button').all()
   ```

2. **Identify selectors** from inspection results

3. **Execute actions** using discovered selectors

## Common Pitfall

❌ **Don't** inspect the DOM before waiting for `networkidle` on dynamic apps

✅ **Do** wait for `page.wait_for_load_state('networkidle')` before inspection

## Frontend Change Verification

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

## Screenshot Comparison

```typescript
// tests/e2e/tests/visual.spec.ts
import { test, expect } from '@playwright/test';

test('visual regression - homepage', async ({ page }) => {
  await page.goto('/');

  // Take screenshot and compare with baseline
  await expect(page).toHaveScreenshot('homepage.png', {
    fullPage: true,
    maxDiffPixels: 100,
  });
});
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
| Servers Running | Backend and frontend servers started |
| API Responds | curl or request to backend API succeeds |

## Reference Files

- **examples/** - Examples showing common patterns:
  - `element_discovery.py` - Discovering buttons, links, and inputs on a page
  - `static_html_automation.py` - Using file:// URLs for local HTML
  - `console_logging.py` - Capturing console logs during automation
