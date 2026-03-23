---
name: se-context
description: Manage project context and state across phases. Provides persistent storage for project information, decisions, and progress tracking.
---

# Context Management for Software Engineering

Manage project context using file system for persistence across phases and sessions.

**Previous Skill**: Invoked by se-lifecycle after each phase completion

**Next Skill**: Returns to se-lifecycle for next phase transition

## Core Principles

### 1. Persistence
- Store context in files, not memory
- Survive across agent sessions
- Version control friendly

### 2. Structured Data
- JSON for machine-readable data
- Markdown for human-readable logs
- Clear schema and conventions

### 3. Incremental Updates
- Update context after each phase
- Append to logs, don't overwrite
- Track history and changes

## File Structure

```
docs/context/
├── project_state.json      # Project state (machine-readable)
├── decisions.md            # Decision log (human-readable)
├── progress.md             # Progress tracking (human-readable)
└── history/                # Historical records
    ├── state_2025-01-01.json
    ├── state_2025-01-02.json
    └── ...
```

## Project State (project_state.json)

### Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["project_name", "current_phase", "last_updated"],
  "properties": {
    "project_name": {
      "type": "string",
      "description": "Project name"
    },
    "project_type": {
      "type": "string",
      "enum": ["web_app", "mobile_app", "desktop_app", "ai_system", "api_service", "other"],
      "description": "Project type"
    },
    "project_description": {
      "type": "string",
      "description": "Brief project description"
    },
    "current_phase": {
      "type": "string",
      "enum": ["init", "requirements", "architecture", "design", "development", "testing", "deployment", "completed"],
      "description": "Current phase"
    },
    "completed_phases": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["init", "requirements", "architecture", "design", "development", "testing", "deployment"]
      },
      "description": "Completed phases"
    },
    "pending_phases": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["requirements", "architecture", "design", "development", "testing", "deployment", "completed"]
      },
      "description": "Pending phases"
    },
    "completion_percentage": {
      "type": "integer",
      "minimum": 0,
      "maximum": 100,
      "description": "Completion percentage"
    },
    "complexity": {
      "type": "string",
      "enum": ["simple", "standard", "complex"],
      "description": "Project complexity"
    },
    "mode": {
      "type": "string",
      "enum": ["fast", "standard", "full"],
      "description": "Working mode"
    },
    "tech_stack": {
      "type": "object",
      "properties": {
        "frontend": { "type": "string" },
        "backend": { "type": "string" },
        "database": { "type": "string" },
        "others": { "type": "array", "items": { "type": "string" } }
      }
    },
    "team_size": {
      "type": "integer",
      "description": "Team size"
    },
    "start_date": {
      "type": "string",
      "format": "date",
      "description": "Start date"
    },
    "target_date": {
      "type": "string",
      "format": "date",
      "description": "Target completion date"
    },
    "last_updated": {
      "type": "string",
      "format": "date-time",
      "description": "Last updated timestamp"
    },
    "blocking_issues": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "description": { "type": "string" },
          "severity": { "type": "string", "enum": ["low", "medium", "high", "critical"] },
          "created_at": { "type": "string", "format": "date-time" },
          "status": { "type": "string", "enum": ["open", "in_progress", "resolved"] }
        }
      }
    },
    "next_action": {
      "type": "string",
      "description": "Next action to take"
    },
    "metadata": {
      "type": "object",
      "description": "Additional metadata"
    }
  }
}
```

### Example

```json
{
  "project_name": "Campus Learning Platform",
  "project_type": "web_app",
  "project_description": "A campus learning platform with blog and quiz features",
  "current_phase": "architecture",
  "completed_phases": ["init", "requirements"],
  "pending_phases": ["design", "development", "testing", "deployment"],
  "completion_percentage": 30,
  "complexity": "standard",
  "mode": "standard",
  "tech_stack": {
    "frontend": "Vue 3 + Element Plus",
    "backend": "Spring Boot 3.x",
    "database": "MySQL + Redis",
    "others": ["Elasticsearch"]
  },
  "team_size": 1,
  "start_date": "2025-01-01",
  "target_date": "2025-02-01",
  "last_updated": "2025-01-03T10:30:00Z",
  "blocking_issues": [],
  "next_action": "Waiting for user to confirm architecture diagram",
  "metadata": {
    "created_by": "requirements-analyst",
    "last_phase_completed": "requirements"
  }
}
```

## Decision Log (decisions.md)

### Format

```markdown
# Decision Log

## Decision Template

### YYYY-MM-DD Decision Title
- **Decision ID**: DEC-XXX
- **Decision**: [Specific decision made]
- **Reason**: [Why this decision was made]
- **Alternatives**: [Options considered but not chosen]
- **Impact**: [Which modules/features are affected]
- **Decision Maker**: [Who made the decision]
- **Status**: [Confirmed/Pending/Changed]
- **Related Docs**: [Links to related documentation]

---

## Actual Decision Records

### 2025-01-01 Tech Stack Selection
- **Decision ID**: DEC-001
- **Decision**: Use Vue 3 + Spring Boot
- **Reason**:
  - Team is familiar with both frameworks
  - Rich ecosystem and complete documentation
  - Suitable for rapid development
- **Alternatives**:
  - React + Node.js (high learning curve)
  - Angular + Java EE (too heavyweight)
- **Impact**: Entire project architecture
- **Decision Maker**: system-architect
- **Status**: Confirmed
- **Related Docs**: Design.md

### 2025-01-02 Database Selection
- **Decision ID**: DEC-002
- **Decision**: Use MySQL + Redis
- **Reason**:
  - MySQL supports transactions and complex queries
  - Redis provides caching
  - Both are mature and stable technologies
- **Alternatives**:
  - MongoDB (not suitable for complex relational queries)
  - PostgreSQL (team is not familiar)
- **Impact**: Data storage layer
- **Decision Maker**: detailed-designer
- **Status**: Confirmed
- **Related Docs**: DetailedDesign.md

### 2025-01-03 Authentication Strategy
- **Decision ID**: DEC-003
- **Decision**: Use JWT + Redis Session hybrid
- **Reason**:
  - JWT supports stateless authentication
  - Redis supports session management and logout
  - Balances performance and security
- **Alternatives**:
  - Pure JWT (cannot invalidate actively)
  - Pure Session (stateful, poor scalability)
- **Impact**: User authentication module
- **Decision Maker**: detailed-designer
- **Status**: Confirmed
- **Related Docs**: DetailedDesign.md
```

## Progress Tracking (progress.md)

### Format

```markdown
# Project Progress Tracking

## Project Overview
- **Project Name**: Campus Learning Platform
- **Current Phase**: Architecture Design
- **Overall Progress**: 30%
- **Start Date**: 2025-01-01
- **Target Date**: 2025-02-01
- **Remaining Time**: 29 days

---

## Phase Details

### ✅ Completed

#### Phase 1: Project Init (2025-01-01)
- [x] Project initialization
- [x] Initial requirement discussion
- [x] Define project scope
- **Duration**: 1 day
- **Status**: Completed on time

#### Phase 2: Requirements Analysis (2025-01-01 ~ 2025-01-02)
- [x] Requirements collection
- [x] User role identification
- [x] Feature list organization
- [x] Use case diagram generation
- [x] User confirmed requirements
- **Duration**: 2 days
- **Status**: Completed on time
- **Deliverables**:
  - Requirement.md
  - docs/diagrams/usecase.mmd

---

### 🔄 In Progress

#### Phase 3: Architecture Design (2025-01-03 ~ in progress)
- [x] Tech stack selection
- [x] Architecture diagram generation
- [ ] Waiting for user confirmation
- [ ] ER diagram design
- [ ] API design
- **Expected Completion**: 2025-01-05
- **Status**: Waiting for confirmation
- **Blocking Items**: Waiting for user to confirm architecture diagram

---

### ⏳ Pending

#### Phase 4: Detailed Design
- [ ] Database detailed design
- [ ] Class diagram design
- [ ] Interface detailed design
- [ ] Flowchart design
- **Expected Start**: 2025-01-06
- **Expected Completion**: 2025-01-08

#### Phase 5: Development
- [ ] Environment setup
- [ ] Vertical Slice 1: User Authentication
- [ ] Vertical Slice 2: Blog Feature
- [ ] Vertical Slice 3: Quiz Feature
- **Expected Start**: 2025-01-09
- **Expected Completion**: 2025-01-20

#### Phase 6: Testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] Performance tests
- **Expected Start**: 2025-01-21
- **Expected Completion**: 2025-01-25

#### Phase 7: Deployment
- [ ] Deployment documentation
- [ ] Production deployment
- [ ] User training
- **Expected Start**: 2025-01-26
- **Expected Completion**: 2025-02-01

---

## Milestones

| Milestone | Planned Date | Actual Date | Status |
|-----------|--------------|-------------|---------|
| Requirements Confirmed | 2025-01-02 | 2025-01-02 | ✅ Completed |
| Architecture Confirmed | 2025-01-05 | - | 🔄 In Progress |
| Design Completed | 2025-01-08 | - | ⏳ Pending |
| Development Completed | 2025-01-20 | - | ⏳ Pending |
| Testing Passed | 2025-01-25 | - | ⏳ Pending |
| Production Launch | 2025-02-01 | - | ⏳ Pending |

---

## Risks and Issues

### Current Risks
| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| Requirement Changes | Medium | High | Establish change control process | Project Manager |
| Technical Difficulty | Low | Medium | Conduct technical research early | Architect |

### Current Issues
- None

---

## Recent Updates

- 2025-01-03: Architecture design completed, waiting for user confirmation
- 2025-01-02: Requirements analysis completed, user confirmed
- 2025-01-01: Project initiated
```

## API Reference

### Initialize Project

Create initial project state.

```python
def init_project(name: str, description: str, project_type: str) -> dict:
    """
    Initialize a new project with default state.
    
    Args:
        name: Project name
        description: Project description
        project_type: Type of project
        
    Returns:
        Initial project state dict
    """
    state = {
        "project_name": name,
        "project_type": project_type,
        "project_description": description,
        "current_phase": "init",
        "completed_phases": [],
        "pending_phases": ["requirements", "architecture", "design", "development", "testing", "deployment"],
        "completion_percentage": 0,
        "last_updated": datetime.now().isoformat(),
        "blocking_issues": [],
        "next_action": "开始需求分析"
    }
    save_state(state)
    return state
```

### Update Phase

Update project phase and progress.

```python
def update_phase(phase: str, status: str = "completed") -> dict:
    """
    Update project phase.

    Args:
        phase: Phase name (requirements, architecture, etc.)
        status: completed, in_progress, pending

    Returns:
        Updated project state
    """
    state = load_state()

    if status == "completed":
        if phase not in state["completed_phases"]:
            state["completed_phases"].append(phase)
        if phase in state["pending_phases"]:
            state["pending_phases"].remove(phase)

        # Auto-set next phase
        if state["pending_phases"]:
            state["current_phase"] = state["pending_phases"][0]
        else:
            state["current_phase"] = "completed"

        # After requirements completed, auto-generate skills usage plan
        if phase == "requirements":
            generate_skills_usage_plan()

    elif status == "in_progress":
        state["current_phase"] = phase

    # Calculate completion percentage
    total_phases = len(state["completed_phases"]) + len(state["pending_phases"])
    if total_phases > 0:
        state["completion_percentage"] = int(
            len(state["completed_phases"]) / total_phases * 100
        )

    state["last_updated"] = datetime.now().isoformat()
    save_state(state)
    return state
```

### Add Decision

Record a new decision.

```python
def add_decision(
    decision_id: str,
    title: str,
    decision: str,
    reason: str,
    alternatives: list,
    impact: str,
    decision_maker: str
) -> None:
    """
    Add a new decision to the decision log.
    
    Args:
        decision_id: Unique decision ID (e.g., DEC-001)
        title: Decision title
        decision: The decision made
        reason: Why this decision was made
        alternatives: Alternative options considered
        impact: Scope of impact
        decision_maker: Who made the decision
    """
    entry = f"""
### {datetime.now().strftime('%Y-%m-%d')} {title}
- **决策ID**: {decision_id}
- **决策**: {decision}
- **原因**: {reason}
- **备选方案**: {', '.join(alternatives)}
- **影响范围**: {impact}
- **决策人**: {decision_maker}
- **状态**: 已确认
- **相关文档**: [待补充]

"""
    append_to_file("docs/context/decisions.md", entry)
```

### Update Progress

Update progress tracking.

```python
def update_progress(
    phase: str,
    task: str,
    status: str,  # completed, in_progress, pending
    notes: str = ""
) -> None:
    """
    Update progress for a specific task.
    
    Args:
        phase: Phase name
        task: Task description
        status: Task status
        notes: Additional notes
    """
    # Implementation would update progress.md
    pass
```

### Get Context

Load full project context.

```python
def get_context() -> dict:
    """
    Load complete project context.
    
    Returns:
        Dict containing state, decisions, and progress
    """
    return {
        "state": load_state(),
        "decisions": load_decisions(),
        "progress": load_progress()
    }
```

## Integration with Other Skills

### With se-lifecycle
- Read state to determine current phase
- Update state after phase completion

### With se-requirements
- Initialize project after requirement collection
- Record requirement decisions

### With se-architecture
- Read requirements from context
- Record architecture decisions
- Update phase to "architecture"

### With se-development
- Read design from context
- Update progress during development
- Record implementation decisions

## Best Practices

1. **Always Update After Phase**: Each skill should update context after completion
2. **Record All Decisions**: Even small decisions should be recorded
3. **Keep Progress Updated**: Update progress.md regularly
4. **Version Control**: Commit context files with code
5. **Backup History**: Keep historical states in history/ directory

## Example Workflow

```python
# 1. Initialize project
init_project("Campus Learning Platform", "Blog and quiz system", "web_app")

# 2. After requirements phase
update_phase("requirements", "completed")
add_decision(
    "DEC-001",
    "Tech Stack Selection",
    "Use Vue 3 + Spring Boot",
    "Team is familiar, rich ecosystem",
    ["React + Node.js"],
    "Entire project architecture",
    "system-architect"
)

# 3. During architecture phase
update_phase("architecture", "in_progress")
update_progress("architecture", "Tech stack selection", "completed")
update_progress("architecture", "Architecture diagram design", "in_progress")

# 4. Get full context
context = get_context()
print(f"Current phase: {context['state']['current_phase']}")
print(f"Completion: {context['state']['completion_percentage']}%")
```
