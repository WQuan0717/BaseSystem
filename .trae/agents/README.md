# Trae Subagent Configuration

> These configuration files are for manually creating subagents in Trae.

---

## Subagent Architecture

This platform uses a **two-agent model**:

| Agent | Role | Context |
|-------|------|---------|
| **SOLO Coder** | Development | Knows everything about implementation |
| **QA Engineer** | Testing | Independent, only knows requirements |

**Why separate?**
```
SOLO Coder (Development AI):
- Implements features
- Knows the code
- Tends to say "it's done" without thorough testing

QA Engineer (Testing AI):
- Independent testing
- Only knows requirements
- Objectively finds bugs
- Like a real QA engineer
```

---

## When to Use Subagents

### Use Case 1: QA Testing (RECOMMENDED)

**When development completes a feature or phase:**
```
SOLO Coder → Completes feature
    ↓
Invoke QA Engineer
    ↓
QA Engineer → Tests independently
    ↓
QA Engineer → Reports bugs in docs/TestReport.md
    ↓
SOLO Coder → Fixes bugs
    ↓
QA Engineer → Regression test
    ↓
Pass → Next phase
```

### Use Case 2: MCP Tools Extension

If you need more than 40 tools, use subagents.

---

## Available Subagents

### Business Agent (1)

| Agent | Purpose | Config | MCP Tools |
|-------|---------|--------|-----------|
| **QA Engineer** | Independent testing | `qa-engineer.md` | 20 |

### Tool Agent (1)

| Agent | Purpose | Config | MCP Tools |
|-------|---------|--------|-----------|
| **Agentic Optimizer** | Agent design optimization | `agentic-optimizer.md` | 11 |

---

## QA Engineer Workflow

### Step 1: Development Completes

```
SOLO Coder completes feature X
    ↓
SOLO Coder says: "Please test feature X"
```

### Step 2: QA Starts Testing

```
QA Engineer reads Requirement.md
QA Engineer reviews deliverables
QA Engineer starts services
QA Engineer takes UI screenshots
QA Engineer runs E2E tests
QA Engineer evaluates UI/UX
```

### Step 3: QA Reports

```
QA Engineer writes docs/TestReport.md
QA Engineer lists all bugs found
QA Engineer gives approval or rejection
```

### Step 4: Development Fixes

```
SOLO Coder reads docs/TestReport.md
SOLO Coder fixes P0 bugs first
SOLO Coder says: "Fixed, please retest"
```

### Step 5: QA Regression

```
QA Engineer runs regression tests
QA Engineer verifies fixes
Pass → "Approved for next phase"
Fail → Back to Step 4
```

---

## QA Engineer Testing Scope

| Category | What QA Tests |
|----------|---------------|
| **Functionality** | Does it work as specified? |
| **UI/UX** | Is it visually consistent and intuitive? |
| **Interaction** | Does user know what to do? |
| **Error Handling** | Are errors caught and shown? |
| **Performance** | Is it fast enough? |

---

## Approval Criteria

**Development can proceed ONLY when:**

| Criterion | Requirement |
|-----------|-------------|
| P0 Bugs | 0 remaining |
| P1 Bugs | All fixed OR documented as known issues |
| UI/UX Score | >= 7/10 |
| Regression | All previous features still work |

---

## How to Create QA Engineer Subagent

### Step 1: In Trae Settings

1. Open Trae Settings
2. Go to "Subagents" configuration
3. Click "Create New Subagent"
4. Name it "QA Engineer"
5. Copy content from `agents/qa-engineer.md`
6. Save and enable

### Step 2: Enable Playwright MCP

QA Engineer needs Playwright tools for UI testing:
- playwright_navigate
- playwright_screenshot
- playwright_click
- playwright_fill
- playwright_evaluate

---

## SOLO Coder Workflow (Updated)

```
se-requirements → Requirement.md
    ↓
se-architecture → Design.md
    ↓
se-detailed-design → DetailedDesign.md
    ↓
ui-ux-pro-max + frontend-design → Design System
    ↓
SOLO Coder: Frontend + Mock Data
    ↓
SOLO Coder: Backend (feature by feature)
    ↓
┌─────────────────────────────────────┐
│  QA Engineer (Independent Test)      │
│  1. Test functionality               │
│  2. Test UI/UX                      │
│  3. Report bugs                     │
│  4. Regression testing                │
└─────────────────────────────────────┘
    ↓ (Pass)
SOLO Coder: Fix bugs if any
    ↓
┌─────────────────────────────────────┐
│  QA Engineer (Final Test)           │
└─────────────────────────────────────┘
    ↓ (Pass)
se-documentation → README.md, API.md
    ↓
Project Complete
```

---

## MCP Tools Allocation

```
SOLO Coder (40 tools):
├── se-lifecycle, se-context, se-requirements
├── se-architecture, se-detailed-design
├── se-development, frontend-design
├── webapp-testing, se-documentation
├── mcp_builder, skill-creator
└── other development tools

QA Engineer (40 tools):
├── playwright_navigate, playwright_screenshot
├── playwright_click, playwright_fill
├── playwright_select, playwright_evaluate
├── Read, Write, RunCommand
├── Glob, Grep
└── mcp_Knowledge_Graph_Memory_*
```

---

## Related Documents

- `.trae/rules/project_rules.md` - Workflow rules
- `.trae/skills/se-lifecycle/SKILL.md` - Workflow decisions
- `.trae/skills/se-development/SKILL.md` - Development process
- `.trae/agents/qa-engineer.md` - QA Engineer config

---

*These config files are for reference only. Actual creation requires manual configuration in Trae settings.*
