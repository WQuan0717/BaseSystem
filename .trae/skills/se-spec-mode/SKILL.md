# Spec Mode - Requirement Analysis & Task Breakdown

## Overview

Spec Mode provides a structured approach to requirement analysis and task planning. It combines Trae spec mode workflow with project-specific conventions.

---

## When to Use

Use Spec Mode **before** starting development when:
- User provides a new project idea
- Requirements are vague or need clarification
- Complex features need breakdown

**Typical Flow:**
```
User Input → Spec Mode → Requirement.md → Development (3-Phase)
```

---

## Spec Mode Workflow

### Step 1: Analyze User Input

**Read and understand:**
- User's original request
- Any existing context

**Identify:**
- Core functionality needed
- Target users
- Key constraints

### Step 2: Create Spec Document

Create `docs/spec.md`:

```markdown
# [Project Name] Specification

## Why
[1-2 sentences on problem/opportunity this solves]

## What
[Brief description of the system]

## User Stories

### Story 1: [Title]
**As a** [user type]
**I want to** [action]
**So that** [benefit]

## Features

### Feature 1: [Name]
**Priority:** P0/P1/P2
**Description:** [What it does]

#### Scenario: [Success case]
- **WHEN** [condition]
- **THEN** [expected result]

#### Scenario: [Error case]
- **WHEN** [condition]
- **THEN** [error handling]

## Technical Decisions

| Aspect | Decision | Rationale |
|--------|----------|-----------|
| Frontend | [Choice] | [Reason] |
| Backend | [Choice] | [Reason] |
| Database | [Choice] | [Reason] |

## Out of Scope
- [Feature not included]
- [Feature not included]
```

### Step 3: Create Task List

Create `docs/tasks.md`:

```markdown
# Tasks

## Phase 1: Foundation
- [ ] Task 1.1: [Description]
  - [ ] SubTask: [Detail]
- [ ] Task 1.2: [Description]

## Phase 2: Core Features
- [ ] Task 2.1: [Description]
  - [ ] SubTask: [Detail]

## Phase 3: Polish
- [ ] Task 3.1: [Description]

## Dependencies
- Task 2.1 depends on Task 1.1
- Task 2.2 depends on Task 1.2
```

### Step 4: Create Checklist

Create `docs/checklist.md`:

```markdown
# Verification Checklist

## Requirements Verified
- [ ] All P0 features implemented
- [ ] All P1 features implemented
- [ ] Edge cases handled

## Code Quality
- [ ] No hardcoded values
- [ ] Error handling complete
- [ ] TypeScript types correct

## Testing
- [ ] Unit tests pass
- [ ] E2E tests pass
- [ ] UI/UX verified

## Documentation
- [ ] README complete
- [ ] API docs complete
```

---

## Spec Mode Principles

### 1. Be Specific, Not Vague

| Vague | Specific |
|--------|----------|
| "User can login" | "User can login with email/password, redirect to dashboard on success" |
| "Fast system" | "Page load < 2 seconds on 3G connection" |

### 2. Include Error Scenarios

Every feature should have:
- Happy path scenario
- Error handling scenario
- Edge case scenario

### 3. Prioritize ruthlessly

| Priority | Meaning | Action |
|----------|---------|--------|
| P0 | Must have | Implement first |
| P1 | Should have | Implement second |
| P2 | Nice to have | Implement if time |

### 4. Verify Before Moving On

Before proceeding to development:
- [ ] Spec document is complete
- [ ] Tasks are clear and achievable
- [ ] User approved the spec

---

## Integration with Other Skills

### After Spec Mode

```
Spec Mode complete
    ↓
se-requirements (expand spec into detailed requirements)
    ↓
se-architecture (technical decisions)
    ↓
se-development (3-phase workflow)
```

### Spec Document Locations

| Document | Location |
|----------|----------|
| Spec | `docs/spec.md` |
| Tasks | `docs/tasks.md` |
| Checklist | `docs/checklist.md` |
| Requirements | `docs/Requirement.md` (expanded from spec) |

---

## Example: Blog System Spec

### docs/spec.md

```markdown
# Blog System Specification

## Why
Users need a platform to create, publish, and share blog articles.

## What
A blog system with user authentication, article CRUD, and commenting.

## User Stories

### Story 1: User Registration
**As a** visitor
**I want to** register an account
**So that** I can publish articles

### Story 2: Publish Article
**As a** registered user
**I want to** publish articles
**So that** others can read them

## Features

### Feature 1: User Authentication
**Priority:** P0

#### Scenario: Registration success
- **WHEN** user fills valid registration form
- **THEN** account created, redirect to login

#### Scenario: Registration failure (email exists)
- **WHEN** user registers with existing email
- **THEN** show error "Email already registered"

### Feature 2: Article Management
**Priority:** P0

#### Scenario: Create article
- **WHEN** user clicks "New Article" and submits
- **THEN** article saved, appears in list

## Technical Decisions

| Aspect | Decision | Rationale |
|--------|----------|-----------|
| Frontend | React + Vite | Fast development, good DX |
| Backend | FastAPI | Python, async, auto-docs |
| Database | SQLite | Easy setup, no Docker needed |
```

---

## Output Requirements

**After Spec Mode, you MUST produce:**

1. `docs/spec.md` - Specification document
2. `docs/tasks.md` - Task breakdown
3. `docs/checklist.md` - Verification checklist

**Do NOT proceed to se-requirements until spec.md is approved.**
