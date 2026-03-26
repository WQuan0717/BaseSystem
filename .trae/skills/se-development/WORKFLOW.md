# ForgeMind Development Workflow

## ⚠️ STRICT PHASE SEQUENCE

**Complete phases in order. Do NOT skip phases.**

---

## PHASE OVERVIEW

```
┌─────────────────────────────────────────────────────────┐
│ PHASE 1: Frontend UI/UX + Mock Data                   │
│          ↓                                              │
│          [QA Review → User Verification]                │
│          ↓                                              │
├─────────────────────────────────────────────────────────┤
│ PHASE 2: Backend Implementation                        │
│          ↓                                              │
│          [Feature by Feature → QA Testing]              │
│          ↓                                              │
├─────────────────────────────────────────────────────────┤
│ PHASE 3: Handoff + Documentation                       │
│          ↓                                              │
│          [Test Accounts → README → User Accept]         │
└─────────────────────────────────────────────────────────┘
```

---

## PHASE 1: Frontend UI/UX + Mock Data

### What to do

1. **Read design requirements**
   - Read `Requirement.md`
   - Use ui-ux-pro-max for design system
   - Document design in `src/design-system.md`

2. **Create frontend structure**
   ```
   src/
   ├── views/           # All pages
   ├── components/     # Reusable components
   ├── mocks/          # Mock data
   │   ├── data/       # JSON mock data
   │   ├── handlers/   # Mock API handlers
   │   └── index.ts    # Mock entry
   └── design-system.md
   ```

3. **Create all pages with mock data**
   - Login/Register pages
   - Dashboard
   - All feature pages
   - All use design system

4. **Verify frontend works**
   - Run `npm run dev`
   - All pages load
   - All mock interactions work

### Gate: Before PHASE 2

**You CANNOT proceed to PHASE 2 until:**

| Check | Done? |
|-------|-------|
| All pages exist | ☐ |
| Design system documented | ☐ |
| Mock data structure exists | ☐ |
| Frontend runs standalone | ☐ |
| QA Engineer approved UI/UX | ☐ |
| User said "继续开发" | ☐ |

---

## PHASE 2: Backend Implementation

### What to do

1. **Start database (Docker)**
   ```bash
   docker run -d --name mysql -p 3306:3306 mysql:8
   docker run -d --name redis -p 6379:6379 redis:7
   ```

2. **Implement features in order**
   ```
   1. Foundation (Auth) - MUST be first
   2. Feature A
   3. Feature B
   ...
   ```

3. **For each feature:**
   - Create database model
   - Create API endpoint
   - Replace mock with real API
   - Run E2E test
   - Verify regression

4. **Test each feature**
   - Use pressSequentially for real input
   - Run Playwright tests
   - Verify no regression

### Gate: Before PHASE 3

**You CANNOT proceed to PHASE 3 until:**

| Check | Done? |
|-------|-------|
| All features implemented | ☐ |
| All E2E tests pass | ☐ |
| QA approved | ☐ |
| User said "继续开发" | ☐ |

---

## PHASE 3: Handoff + Documentation

### What to do

1. **Start all services**
   ```bash
   docker start mysql redis
   cd backend && npm run dev
   cd frontend && npm run dev
   ```

2. **Create test accounts**
   ```bash
   # Admin
   curl -X POST http://localhost:8000/api/auth/register \
     -H "Content-Type: application/json" \
     -d '{"email":"admin@test.com","password":"Admin123!","role":"admin"}'

   # User
   curl -X POST http://localhost:8000/api/auth/register \
     -H "Content-Type: application/json" \
     -d '{"email":"user@test.com","password":"User123!","role":"user"}'
   ```

3. **Generate documentation**
   - `README.md` - Quick start guide
   - `API.md` - API documentation
   - `DEPLOYMENT.md` - Deployment guide

4. **Final verification**
   - User accepts system
   - Project complete

---

## QUICK REFERENCE

### File Locations

| Phase | Instructions | Checkpoints |
|-------|--------------|--------------|
| PHASE 1 | `skills/se-development/PHASE1-frontend.md` | Frontend complete |
| PHASE 2 | `skills/se-development/PHASE2-backend.md` | Backend complete |
| PHASE 3 | `skills/se-development/PHASE3-handoff.md` | Handoff complete |

### Important Rules

1. **DO NOT skip phases**
2. **DO NOT read next phase file early**
3. **DO verify all checkpoints before proceeding**
4. **DO ask user for verification at gates**

---

## START NOW

**Read `Requirement.md` to understand the project, then:**

```
1. Use ui-ux-pro-max for design system
2. Create frontend with mock data
3. Verify frontend works
4. Wait for user confirmation
5. Only then read PHASE 2 instructions
```

---

## HELP

If stuck:
1. Re-read current phase instructions
2. Check checkpoint requirements
3. Verify file structure matches expectations
4. Ask user if unclear
