# PHASE 2: Backend Implementation

## ⚠️ IMPORTANT

**You are in PHASE 2. PHASE 1 must be complete first.**

**Do NOT read `PHASE3-handoff.md` until PHASE 2 is complete.**

---

## YOUR TASK NOW

Implement backend features one by one, integrating with existing frontend.

---

## PREREQUISITES

Before starting PHASE 2, verify PHASE 1 is complete:

| Checkpoint | Verification |
|------------|--------------|
| [ ] Frontend structure exists | `ls src/views/` |
| [ ] Mock data exists | `ls src/mocks/` |
| [ ] Frontend runs | `npm run dev` works |
| [ ] User approved | User said "继续开发" |

---

## STEP 1: Environment Setup

### 1.1 Start Database (Docker)

```bash
# Check if Docker is available
docker --version

# Start database services
docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:8
docker run -d --name redis -p 6379:6379 redis:7

# For projects needing other services
docker run -d --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=root postgres:15
```

### 1.2 Backend Structure

```
backend/
├── src/
│   ├── controllers/     # API endpoints
│   ├── services/      # Business logic
│   ├── repositories/  # Database operations
│   ├── models/        # Data models
│   └── middleware/    # Auth, validation
├── tests/
│   └── e2e/          # Playwright tests
└── package.json
```

---

## STEP 2: Feature Order

**Develop features in this order. Each feature must be tested before moving to next.**

```
1. Foundation (MUST be first)
   ├── Database connection
   ├── Authentication/Authorization
   └── API structure

2. Core Features (based on frontend needs)
   ├── Feature A
   ├── Feature B
   └── Feature C
```

### Feature List (from Requirement.md)

| Feature | Priority | Status |
|---------|----------|--------|
| User Authentication | P0 | Pending |
| User Management | P1 | Pending |
| ... | ... | ... |

---

## STEP 3: Implement Each Feature

### 3.1 Database Model

**`backend/src/models/User.ts`**
```typescript
export interface User {
  id: number;
  email: string;
  username: string;
  password: string;
  createdAt: Date;
}
```

### 3.2 Repository

**`backend/src/repositories/UserRepository.ts`**
```typescript
import { User } from '../models/User';
import { pool } from '../config/database';

export class UserRepository {
  async findByEmail(email: string): Promise<User | null> {
    const result = await pool.query(
      'SELECT * FROM users WHERE email = ?',
      [email]
    );
    return result[0] || null;
  }

  async create(user: Omit<User, 'id'>): Promise<User> {
    const result = await pool.query(
      'INSERT INTO users (email, username, password) VALUES (?, ?, ?)',
      [user.email, user.username, user.password]
    );
    return { id: result.insertId, ...user };
  }
}
```

### 3.3 Service

**`backend/src/services/AuthService.ts`**
```typescript
import { UserRepository } from '../repositories/UserRepository';
import { hash, compare } from '../utils/crypto';

export class AuthService {
  private userRepo = new UserRepository();

  async register(data: { email: string; username: string; password: string }) {
    const hashedPassword = await hash(data.password);
    const user = await this.userRepo.create({
      ...data,
      password: hashedPassword
    });
    return { id: user.id, email: user.email, username: user.username };
  }

  async login(email: string, password: string) {
    const user = await this.userRepo.findByEmail(email);
    if (!user) throw new Error('User not found');

    const valid = await compare(password, user.password);
    if (!valid) throw new Error('Invalid password');

    return { id: user.id, email: user.email, username: user.username };
  }
}
```

### 3.4 Controller

**`backend/src/controllers/AuthController.ts`**
```typescript
import { Router } from 'express';
import { AuthService } from '../services/AuthService';

const router = Router();
const authService = new AuthService();

router.post('/register', async (req, res) => {
  try {
    const user = await authService.register(req.body);
    res.json({ success: true, data: user });
  } catch (error: any) {
    res.status(400).json({ success: false, error: error.message });
  }
});

router.post('/login', async (req, res) => {
  try {
    const user = await authService.login(req.body.email, req.body.password);
    res.json({ success: true, data: user });
  } catch (error: any) {
    res.status(401).json({ success: false, error: error.message });
  }
});

export default router;
```

---

## STEP 4: Replace Mock with Real API

### 4.1 Update Frontend API Client

**`src/api/client.ts`**
```typescript
const API_BASE = 'http://localhost:8000/api';

export const api = {
  login: (email: string, password: string) =>
    fetch(`${API_BASE}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    }).then(r => r.json()),

  register: (data: any) =>
    fetch(`${API_BASE}/auth/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    }).then(r => r.json())
};
```

### 4.2 Update Frontend to Use Real API

**`src/views/Login.tsx`**
```tsx
import { api } from '@/api/client';

export default function Login() {
  const handleSubmit = async (email: string, password: string) => {
    const result = await api.login(email, password);
    if (result.success) {
      // Redirect to dashboard
    } else {
      // Show error
    }
  };
}
```

---

## STEP 5: E2E Testing

### 5.1 Create E2E Test

**`tests/e2e/auth.spec.ts`**
```typescript
import { test, expect } from '@playwright/test';

test('user login with valid credentials', async ({ page }) => {
  await page.goto('/login');

  // Use pressSequentially for real keyboard input
  await page.locator('#email').pressSequentially('test@example.com', { delay: 50 });
  await page.locator('#password').pressSequentially('Test123!', { delay: 50 });
  await page.click('button[type="submit"]');

  await page.waitForURL('**/dashboard', { timeout: 10000 });
  await expect(page.locator('.user-name')).toBeVisible();
});
```

### 5.2 Run E2E Tests

```bash
cd tests/e2e
npx playwright test
```

### 5.3 Regression Testing

**Before moving to next feature, verify ALL previous features still work:**

```bash
# Run all E2E tests
npx playwright test

# Verify no regression
```

---

## ✅ COMPLETION CHECKPOINTS

**You CANNOT proceed to PHASE 3 until ALL checkpoints pass:**

| Checkpoint | Verification |
|------------|--------------|
| [ ] Database connected | `curl localhost:3306` |
| [ ] Backend runs | `npm run dev` |
| [ ] Auth feature works | E2E test passes |
| [ ] Feature 1 tested | E2E test passes |
| [ ] Feature 2 tested | E2E test passes |
| [ ] ... | ... |
| [ ] QA approved | See QA report |
| [ ] User said "继续开发" | User input received |

---

## 🚫 DO NOT

- Do NOT skip features
- Do NOT skip E2E testing
- Do NOT claim feature complete without testing
- Do NOT read `PHASE3-handoff.md`

---

## 📞 GET HELP

If stuck:
1. Check database connection
2. Verify API endpoints work with curl
3. Run E2E tests with verbose output
4. Check backend logs
