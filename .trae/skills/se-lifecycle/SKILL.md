---
name: se-lifecycle
description: Shared knowledge for software engineering lifecycle. Provides phase definitions, document flow, and Knowledge Graph standards. All SE agents MUST invoke this SKILL.
---

# Software Engineering Lifecycle

Shared knowledge base for all software engineering agents. Provides lifecycle context and Knowledge Graph standards for cross-phase collaboration.

## Workflow Decision Rules

### Full Lifecycle (New Project)
Trigger: User wants to build a new system from scratch
- "帮我开发一个XXX系统"
- "我想做一个XXX应用"
- "帮我实现一个XXX平台"
→ Start from Requirements phase

### Partial Lifecycle (Existing Project)
| User Request | Start Phase |
|--------------|-------------|
| "帮我设计架构" | Architecture |
| "帮我设计数据库/API" | Detailed Design |
| "帮我实现这个功能" | Development |
| "帮我测试一下" | Testing |
| "帮我写文档" | Documentation |

### Single Task (Skip Lifecycle)
| User Request | Action |
|--------------|--------|
| "解释这段代码" | Direct answer |
| "修复这个bug" | Direct fix |
| "优化这个函数" | Direct optimize |
| "添加一个字段" | Direct modify |
| "这个报错怎么解决" | Direct debug |

### Decision Flow
```
User Request
    │
    ├─ New system? ──────────────────→ Requirements
    │
    ├─ Specific phase mentioned? ────→ That phase
    │
    └─ Small task? ──────────────────→ Direct execute
```

## Phase Definition

| Phase | Agent | Input | Output | Responsibility |
|-------|-------|-------|--------|----------------|
| Requirements | Requirements Analyst | User ideas | Requirement.md | Define "what to do" |
| Architecture | System Architect | Requirement.md | Design.md | Produce "decisions" |
| Detailed Design | Detailed Designer | Design.md | DetailedDesign.md | Produce "specifications" |
| Development | Full-stack Engineer | DetailedDesign.md | Code + Unit Tests | Produce "code" |
| Testing | QA Engineer | Code + Tests | TestReport.md | Validate quality |
| Documentation | Technical Writer | All docs + Codebase | README.md, API.md, etc. | Document project |

## Phase Transition Rules

**CRITICAL: SOLO Coder is responsible for phase transitions. Subagents return to SOLO Coder after completion.**

### Transition Flow
```
SOLO Coder → Subagent → Complete → Return to SOLO Coder → Next Subagent
```

### Transition Protocol

| Current Phase | Subagent Returns | SOLO Coder Action |
|---------------|------------------|-------------------|
| Requirements | "Requirements complete: Requirement.md" | Invoke system-architect |
| Architecture | "Architecture complete: Design.md" | Invoke detailed-designer |
| Detailed Design | "Detailed design complete: DetailedDesign.md" | Invoke full-stack-engineer |
| Development | "Development complete: Code + Tests" | Invoke qa-engineer |
| Testing | "Testing complete: TestReport.md" | Invoke technical-writer |
| Documentation | "Documentation complete: All docs" | Report project done |

### Subagent Return Format

Each subagent MUST return to SOLO Coder with:
```
## Phase Complete

Status: [SUCCESS/FAILED]
Output: [list created files]
Next Phase: [next phase name]
Message: Ready for next phase. Returning to SOLO Coder.
```

### SOLO Coder Decision Rules

1. **After subagent returns**: Check completion status
2. **If SUCCESS**: Invoke next sub-agent in sequence
3. **If FAILED**: Report error to user, wait for instruction
4. **If last phase**: Report project completion

## Document Flow

```
Requirement.md → Design.md → DetailedDesign.md → Code → TestReport.md → README.md, API.md, DEPLOYMENT.md, CONTRIBUTING.md, CHANGELOG.md
```

## Knowledge Graph Entity Standards

### Entity Types

| Entity Type | Description | Created By |
|-------------|-------------|------------|
| Project | Project basic info | Requirements Analyst |
| Requirement | Requirement entity | Requirements Analyst |
| UserStory | User story | Requirements Analyst |
| Architecture | Architecture decisions | System Architect |
| TechStack | Technology selection | System Architect |
| Risk | Risk assessment | System Architect |
| Database | Database design | Detailed Designer |
| API | API specification | Detailed Designer |
| Module | Module design | Detailed Designer |
| Component | Component implementation | Full-stack Engineer |
| TestCase | Test case | QA Engineer |
| TestReport | Test report | QA Engineer |
| Documentation | Project documentation | Technical Writer |

### Relation Types

| Relation Type | From → To | Description |
|---------------|-----------|-------------|
| HAS_REQUIREMENT | Project → Requirement | Project has requirements |
| HAS_STORY | Requirement → UserStory | Requirement has user stories |
| DECIDES | Requirement → Architecture | Architecture decides based on requirements |
| USES | Architecture → TechStack | Architecture uses tech stack |
| HAS_RISK | Architecture → Risk | Architecture has risks |
| IMPLEMENTS | Architecture → Database | Database implements architecture |
| EXPOSES | Architecture → API | API exposes architecture |
| CONTAINS | Architecture → Module | Architecture contains modules |
| BUILDS | Module → Component | Component builds module |
| TESTS | TestCase → Component | Test case tests component |
| REPORTS | TestReport → TestCase | Report covers test cases |

### Entity Template

```json
{
  "name": "EntityName_ID",
  "entityType": "EntityType",
  "observations": [
    "Key observation 1",
    "Key observation 2"
  ]
}
```

### Relation Template

```json
{
  "from": "SourceEntityName",
  "relationType": "RELATION_TYPE",
  "to": "TargetEntityName"
}
```

## Cross-Phase Context Flow

### Requirements Analyst

**Read before starting:**
```
mcp_Knowledge_Graph_Memory_search_nodes(query="Project")
```

**Store after completion:**
```
mcp_Knowledge_Graph_Memory_create_entities(entities=[
  {name: "Project_{name}", entityType: "Project", observations: ["description", "goals", "constraints"]},
  {name: "Requirement_{id}", entityType: "Requirement", observations: ["description", "priority", "acceptance_criteria"]}
])

mcp_Knowledge_Graph_Memory_create_relations(relations=[
  {from: "Project_{name}", relationType: "HAS_REQUIREMENT", to: "Requirement_{id}"}
])
```

### System Architect

**Read before starting:**
```
mcp_Knowledge_Graph_Memory_search_nodes(query="Requirement")
```

**Store after completion:**
```
mcp_Knowledge_Graph_Memory_create_entities(entities=[
  {name: "Architecture_{name}", entityType: "Architecture", observations: ["pattern", "style", "decisions"]},
  {name: "TechStack_{name}", entityType: "TechStack", observations: ["frontend", "backend", "database", "reasons"]}
])

mcp_Knowledge_Graph_Memory_create_relations(relations=[
  {from: "Requirement_{id}", relationType: "DECIDES", to: "Architecture_{name}"},
  {from: "Architecture_{name}", relationType: "USES", to: "TechStack_{name}"}
])
```

### Detailed Designer

**Read before starting:**
```
mcp_Knowledge_Graph_Memory_search_nodes(query="Architecture")
```

**Store after completion:**
```
mcp_Knowledge_Graph_Memory_create_entities(entities=[
  {name: "Database_{name}", entityType: "Database", observations: ["tables", "relations", "indexes"]},
  {name: "API_{name}", entityType: "API", observations: ["endpoints", "methods", "schemas"]}
])

mcp_Knowledge_Graph_Memory_create_relations(relations=[
  {from: "Architecture_{name}", relationType: "IMPLEMENTS", to: "Database_{name}"},
  {from: "Architecture_{name}", relationType: "EXPOSES", to: "API_{name}"}
])
```

### Full-stack Engineer

**Read before starting:**
```
mcp_Knowledge_Graph_Memory_search_nodes(query="Module")
mcp_Knowledge_Graph_Memory_search_nodes(query="API")
```

**Store after completion:**
```
mcp_Knowledge_Graph_Memory_create_entities(entities=[
  {name: "Component_{name}", entityType: "Component", observations: ["implementation", "tests", "status"]}
])

mcp_Knowledge_Graph_Memory_create_relations(relations=[
  {from: "Module_{name}", relationType: "BUILDS", to: "Component_{name}"}
])
```

### QA Engineer

**Read before starting:**
```
mcp_Knowledge_Graph_Memory_search_nodes(query="Component")
mcp_Knowledge_Graph_Memory_search_nodes(query="API")
```

**Store after completion:**
```
mcp_Knowledge_Graph_Memory_create_entities(entities=[
  {name: "TestCase_{id}", entityType: "TestCase", observations: ["description", "steps", "expected_result"]},
  {name: "TestReport_{date}", entityType: "TestReport", observations: ["summary", "pass_rate", "issues"]}
])

mcp_Knowledge_Graph_Memory_create_relations(relations=[
  {from: "TestCase_{id}", relationType: "TESTS", to: "Component_{name}"},
  {from: "TestReport_{date}", relationType: "REPORTS", to: "TestCase_{id}"}
])
```

### Technical Writer

**Read before starting:**
```
mcp_Knowledge_Graph_Memory_read_graph()
```

**Store after completion:**
```
mcp_Knowledge_Graph_Memory_create_entities(entities=[
  {name: "Documentation_{date}", entityType: "Documentation", observations: ["readme", "api_docs", "deployment_guide", "contributing_guide", "changelog"]}
])
```

## MoSCoW Prioritization

| Priority | Label | Description |
|----------|-------|-------------|
| P0 | Must-have | Critical for MVP, project fails without it |
| P1 | Should-have | Important but not critical, next iteration |
| P2 | Could-have | Nice to have, if time permits |
| P3 | Won't-have | Explicitly out of scope |

## Quality Gates

Each phase has quality gates that must pass before proceeding:

### Requirements → Architecture
- [ ] All P0 features documented
- [ ] Acceptance criteria defined
- [ ] No ambiguous terms

### Architecture → Detailed Design
- [ ] Tech stack selected with reasons
- [ ] Module boundaries defined
- [ ] Risks identified with mitigation

### Detailed Design → Development
- [ ] Database schema complete
- [ ] API specifications complete
- [ ] Directory structure defined

### Development → Testing
- [ ] Unit tests pass
- [ ] Code compiles
- [ ] No critical bugs

### Testing → Release
- [ ] All test cases pass
- [ ] Performance meets requirements
- [ ] Security audit passed

### Documentation → Release
- [ ] README.md complete with quick start
- [ ] API.md documents all endpoints
- [ ] DEPLOYMENT.md verified
- [ ] CONTRIBUTING.md clear
- [ ] CHANGELOG.md updated

## Git Version Control

### Commit Convention

| Type | Description | Example |
|------|-------------|---------|
| feat | New feature | feat: add user login |
| fix | Bug fix | fix: resolve login timeout |
| docs | Documentation | docs: update README |
| refactor | Code refactor | refactor: simplify auth logic |
| test | Test related | test: add login unit tests |
| style | Code style | style: format code |
| chore | Maintenance | chore: update dependencies |

### Branch Strategy (Small Projects)

```
main (production)
  └── develop (development)
        └── feature/* (optional, for complex features)
```

### Git Rules

1. **Commit Timing**
   - After each vertical slice completion
   - After fixing bugs
   - After updating documentation
   - Before switching to another task

2. **Commit Message Format**
   ```
   <type>: <subject>
   
   [optional body]
   ```

3. **Push Rules**
   - Push before ending work session
   - Push before creating PR
   - Ensure tests pass before push

4. **Branch Rules**
   - main: protected, only merge via PR
   - develop: integration branch
   - feature/*: short-lived, delete after merge

### Workflow per Phase

| Phase | Git Operations |
|-------|----------------|
| Requirements | Commit Requirement.md |
| Architecture | Commit Design.md |
| Detailed Design | Commit DetailedDesign.md |
| Development | Commit after each slice, push daily |
| Testing | Commit bug fixes, commit TestReport.md |
| Documentation | Commit all docs, update CHANGELOG.md |
