---
name: subagent-creator
description: Guide for creating and optimizing agent prompts for the Trae platform. Use when users want to create a new agent, optimize an existing agent configuration, or need guidance on agent prompt design.
---

# Subagent Creator

Create and optimize agent prompts for the Trae platform with verified real tools.

## Agent Configuration Standard Format

Every agent configuration file MUST follow this three-section structure:

```markdown
## 提示词

```markdown
[Role Definition → Core Responsibilities → Operation Guide]
```

## 何时调用

```markdown
Use this agent when [brief description in English].

<example><context>[context in English]</context>user: "[message in user's language]" <commentary>[rationale in English]</commentary> assistant: "[response in user's language]"</example>
```

## 需要启用的MCP工具

```markdown
| MCP Server | 勾选数量 | 说明 |
|-----------|---------|------|
| ServerName | X/Y | 全选 / 仅勾选：tool1, tool2, tool3 |

> 💡 **提示**：[Additional notes about tool usage]
```

```

**CRITICAL**: 
- No other content is allowed except these three sections (and optionally a new SKILL if needed)
- Do NOT include the format explanation line (the one starting with `提示词部分作为...`) in the output file — that's only for this SKILL document

## Workflow

### Step 1: Tool Discovery (REQUIRED - Execute Before Any Design)

**1.1 Read MCP Configuration**
- Linux: `Read(file_path="~/.trae-cn-server/data/Machine/mcp.json")`
- Windows: `Read(file_path="C:\\Users\\{username}\\AppData\\Roaming\\Trae CN\\User\\mcp.json")`
- Parse and record all MCP Server names

**1.2 Read MCP Tool Details**
- Linux: `LS(path="~/.trae-cn-server/data/User/globalStorage/.mcp_gallery_cache")`
- Windows: `LS(path="C:\\Users\\{username}\\AppData\\Roaming\\Trae CN\\User\\globalStorage\\.mcp_gallery_cache")`
- Then read specific files: `Read(file_path=".../{server_name}.json")`
- Count tools and record exact tool names (e.g., `mcp_Excel_excel_read_sheet`)

**1.3 Search SKILL Documents**
- Linux: `LS(path="~/.trae-cn/skills")`
- Windows: `LS(path="C:\\Users\\{username}\\.trae-cn\\skills")`
- Search files: `Glob(pattern=".../**/SKILL.md")`

**1.4 Verify Tool Authenticity**
- NEVER invent or hallucinate tools that do not exist
- Only recommend tools verified through the above steps
- Double-check tool count from MCP cache JSON files

### Step 2: Design Agent Prompt

**Role Definition** (1-2 sentences):
- Clear, concise description of what the agent does

**Core Responsibilities** (3-5 items):
- Key professional areas and tasks
- Use action verbs

**Operation Guide**:
- Work phases with specific steps
- Tool usage with exact names and examples
- Quality checklists
- Exception handling scenarios

### Step 3: Design "When to Invoke" Section

**CRITICAL: Must start with an English summary sentence!**

```markdown
Use this agent when [brief description in English].

<example><context>[context in English]</context>user: "[message in user's language]" <commentary>[rationale in English]</commentary> assistant: "[response in user's language]"</example>
```

Guidelines:
- **First line MUST be an English summary sentence** (e.g., "Use this agent when technical documentation needs to be created.")
- Use English for context and commentary (for SOLO Coder understanding)
- Use user's language for user messages and assistant responses
- Provide 2-4 specific examples
- Cover common use cases

### Step 4: Define MCP Tools Section

**CRITICAL: MCP Tool Count Limit (MAX 40)**

Count INDIVIDUAL TOOLS, not just MCP Servers. Many MCP Servers have 10+ tools (GitHub has 27 tools!).

**Verify tool count from MCP cache JSON files!**

Structure:
```markdown
| MCP Server | 勾选数量 | 说明 |
|-----------|---------|------|
| ServerName | X/Y | 全选 / 仅勾选：tool1, tool2, tool3 |

> 💡 **提示**：[Additional notes about tool usage]
```

**Fine-grained tool selection strategy:**
1. List ALL tools from each MCP Server (read from JSON cache)
2. Count the exact number of tools
3. Mark which ones are ESSENTIAL and which are UNNECESSARY
4. Only recommend the ESSENTIAL tools
5. Provide clear instructions: "Check these 3 tools, uncheck the rest"

### Step 5: Output and Save

Save the agent configuration to:
```
{project_root}/.trae/agents/{agent-name}.md
```

## Built-in Tools Reference

These tools are always available (no MCP required):

| Category | Tool Name | Function |
|----------|-----------|----------|
| File Operations | Read | Read file content |
| File Operations | Write | Write file content |
| File Operations | LS | List directory |
| File Operations | Glob | Pattern matching |
| Command Execution | RunCommand | Execute terminal commands |
| Search & Navigation | SearchCodebase | Semantic code search |
| Search & Navigation | Grep | Regex search |
| Network Tools | WebSearch | Web search |
| Network Tools | WebFetch | Fetch web pages |
| Task Management | TodoWrite | Task list management |
| Interaction | AskUserQuestion | Ask user questions |
| Other | Skill | Execute custom SKILL |

## Enhanced MCP Recommendations

| MCP Server | Use Case | Tool Count |
|-----------|----------|------------|
| Sequential Thinking | Complex analysis, comparing options | 1 |
| Context7 | Reference many documents | 2 |
| Knowledge Graph Memory | Long-term projects | 9 |

## SKILL Creation Rules (CRITICAL)

When creating new SKILLs using skill-creator, follow these rules:

**Directory Location:**
- SKILL directory **MUST** be under project root: `{project_root}/.trae/skills/{skill-name}`
- **NEVER** create SKILLs in system directory `~/.trae-cn/skills` (cannot delete from sandbox)

**init_skill.py Usage:**
```bash
# Correct - Point to project directory
python3 ~/.trae-cn/skills/skill-creator/scripts/init_skill.py {skill-name} --path {project_root}/.trae/skills

# Wrong - Pointing to system directory
python3 ... --path ~/.trae-cn/skills  # FORBIDDEN
```

## Quality Checklist

Before finalizing an agent configuration:

- [ ] MCP configuration has been read and parsed
- [ ] Relevant MCP tool cache files have been read, including individual tool lists
- [ ] Tool count verified from MCP cache JSON files
- [ ] SKILL documents have been searched and reviewed
- [ ] All tools mentioned in prompt are verified real
- [ ] INDIVIDUAL MCP tools counted (not just Servers)
- [ ] Total MCP tools DO NOT EXCEED 40
- [ ] Fine-grained tool selection provided (which to check/uncheck)
- [ ] Prompt follows Trae's standard format (three sections)
- [ ] "When to Invoke" section starts with English summary sentence
- [ ] "When to Invoke" section has 2-4 examples
- [ ] Language matches user's preference for examples

## Common Issues and Solutions

### Issue: Missing English Summary in "When to Invoke"
**Solution**: Always start with "Use this agent when [description]." before the examples.

### Issue: Wrong Tool Count
**Solution**: Read the MCP cache JSON file and count the tools in the "tools" object. Do not guess.

### Issue: Hallucinated Tools
**Solution**: Always run Step 1 (Tool Discovery) before designing. Use exact tool names from MCP cache files.

### Issue: Wrong Tool Names
**Solution**: Read the specific MCP cache JSON file to get exact names (e.g., `mcp_Excel_excel_read_sheet` not `mcp_Excel_read_sheet`)

### Issue: Format Violations
**Solution**: Remove any content that isn't part of 提示词, 何时调用, or 需要启用的MCP工具

## Prompt Design Principles

### AI-Friendly vs User-Friendly

1. **Prompt Content**: Must be AI-friendly
   - Use plain text, avoid ASCII diagrams or visual elements
   - AI only reads text, cannot interpret visual diagrams
   - Clear structure with headers and lists

2. **MCP Tools Section**: Must be user-friendly
   - Use table format showing tool count (e.g., "3/10")
   - Clear instructions on which tools to check/uncheck
   - This is the ONLY section humans need to understand
