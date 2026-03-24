# Trae Subagent Configuration

> These configuration files are for manually creating subagents in Trae.

---

## What is a Subagent?

Subagents are **dedicated agents** in Trae that can:
- Execute independent tasks in parallel
- Focus on specific domains (e.g., documentation)
- Each subagent has its own 40 MCP Tools quota

---

## When to Use Subagents

### Use Cases (Parallel)

1. **Documentation Generation** - Technical Writer runs parallel to development
   - SOLO Coder implements code
   - Technical Writer generates documentation simultaneously

2. **MCP Tools Extension** - Break through 40 tool limit
   - Each subagent has independent 40 tools quota
   - SOLO Coder can indirectly use more tools

### Not Applicable (Sequential, handled by SOLO Coder)

These phases **do NOT need subagents**, handled by SOLO Coder via Skills:

| Phase | Handler | Reason |
|-------|---------|--------|
| Requirements | SOLO Coder + se-requirements | Needs frequent user interaction |
| Architecture | SOLO Coder + se-architecture | Needs overall control |
| Detailed Design | SOLO Coder + se-detailed-design | Connects phases |
| Development | SOLO Coder + se-development | Core implementation |
| Testing | SOLO Coder + webapp-testing | All-in-one testing toolkit |

---

## Available Subagents

### Business Agent (1)

| Agent | Purpose | Config | MCP Tools |
|-------|---------|--------|-----------|
| **Technical Writer** | Documentation expert | `technical-writer.md` | 12 |

### Tool Agent (1)

| Agent | Purpose | Config | MCP Tools |
|-------|---------|--------|-----------|
| **Agentic Optimizer** | Agent design optimization | `agentic-optimizer.md` | 11 |

> 💡 **Note**: Agentic Optimizer is not a business agent, but a tool for designing and optimizing other agents.

---

## How to Create a Subagent

### Step 1: In Trae Settings

1. Open Trae Settings
2. Go to "Subagents" configuration
3. Click "Create New Subagent"
4. Copy the **three-section content** from the config file:
   - ## 提示词 (Prompt)
   - ## 何时调用 (When to Invoke)
   - ## 需要启用的 MCP 工具 (MCP Tools to Enable)
5. Save and enable

### Step 2: Using Agentic Optimizer

```bash
# Invoke in Trae
invoke agentic-optimizer
```

Let Agentic Optimizer help you design and optimize new agent configurations.

---

## Best Practices

### 1. Number of Subagents

- **Recommended**: 1 (Technical Writer)
- **Maximum**: 2 (+ Optimizer for creating new agents)
- **Avoid**: Too many subagents cause coordination difficulties

### 2. MCP Tools Allocation

```
SOLO Coder:
├── se-* skills (core workflow)
├── webapp-testing (testing)
├── mcp-builder (MCP development)
└── other development tools

Technical Writer:
├── se-documentation
├── docx/pdf (document formats)
└── other writing tools
```

---

## Related Documents

- `.trae/rules/project_rules.md` - Workflow rules
- `.trae/skills/se-lifecycle/SKILL.md` - Workflow decisions
- `.trae/skills/se-context/SKILL.md` - State management
- `.trae/skills/webapp-testing/SKILL.md` - Testing toolkit

---

*These config files are for reference only. Actual creation requires manual configuration in Trae settings.*
