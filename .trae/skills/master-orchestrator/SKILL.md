---
name: master-orchestrator
description: Master orchestrator for immersive development. Coordinates all phases, manages workflow, and ensures visualization-driven development.
---

# Master Orchestrator

Central coordinator for the immersive development workflow.

## When to Invoke

Invoke this SKILL when:
- Starting a new project
- Transitioning between phases
- Need to determine next steps
- Coordinating multiple sub-agents

## Workflow Modes

### Mode Selection

| Complexity | Features | Duration | Mode | Documents |
|------------|----------|----------|------|-----------|
| Simple | < 3 | < 1 week | fast | README only |
| Standard | 3-10 | 2-4 weeks | standard | Full lifecycle + diagrams |
| Complex | > 10 | > 1 month | full | Complete + deployment |

### Auto-Detect Complexity

Based on:
- Number of user roles mentioned
- Number of features described
- Integration requirements
- Data complexity

## Standard Workflow

### Phase 1: Requirements Analysis

**Entry**: User describes project idea
**Exit**: Confirmed use case diagram

Steps:
1. Invoke `requirements-analyst` agent
2. Generate Requirement.md
3. Invoke `se-diagram` to create usecase.mmd
4. Present use case diagram to user
5. Wait for user confirmation
6. Invoke `se-context` to update state

**Confirmation Required**: Yes
**Output Files**:
- Requirement.md
- docs/diagrams/usecase.mmd
- docs/context/project_state.json (updated)

### Phase 2: Architecture Design

**Entry**: Requirements confirmed
**Exit**: Confirmed architecture and ER diagrams

Steps:
1. Read Requirement.md and usecase.mmd
2. Invoke `system-architect` agent
3. Generate Design.md
4. Invoke `se-diagram` to create:
   - architecture.mmd
   - erdiagram.mmd
5. Present diagrams to user
6. Wait for user confirmation
7. Record tech stack decisions
8. Invoke `se-context` to update state

**Confirmation Required**: Yes
**Output Files**:
- Design.md
- docs/diagrams/architecture.mmd
- docs/diagrams/erdiagram.mmd
- docs/context/decisions.md (updated)

### Phase 3: Detailed Design

**Entry**: Architecture confirmed
**Exit**: Confirmed class and flow diagrams

Steps:
1. Read Design.md and architecture diagrams
2. Invoke `detailed-designer` agent
3. Generate DetailedDesign.md
4. Invoke `se-diagram` to create:
   - classdiagram.mmd
   - flowchart.mmd
5. Present diagrams to user
6. Wait for user confirmation
7. Invoke `se-context` to update state

**Confirmation Required**: Yes
**Output Files**:
- DetailedDesign.md
- docs/diagrams/classdiagram.mmd
- docs/diagrams/flowchart.mmd

### Phase 4: Development

**Entry**: Design confirmed
**Exit**: Working code with tests

Steps:
1. Read all design documents and diagrams
2. Identify vertical slices
3. For each slice:
   a. Invoke `full-stack-engineer` agent
   b. Generate code
   c. Run tests
   d. Present to user
   e. Wait for confirmation
   f. Update progress.md
4. Invoke `se-context` to update state

**Confirmation Required**: Per slice
**Output**: Working code in src/

### Phase 5: Testing

**Entry**: Development complete
**Exit**: Test report

Steps:
1. Invoke `qa-engineer` agent
2. Run comprehensive tests
3. Generate TestReport.md
4. Present results
5. Fix issues if any
6. Invoke `se-context` to update state

**Confirmation Required**: Yes
**Output**: TestReport.md

### Phase 6: Deployment

**Entry**: Tests passed
**Exit**: Deployed application

Steps:
1. Generate deployment docs
2. Create deployment diagram
3. Deploy to target environment
4. Verify deployment
5. Update README.md
6. Final state update

**Confirmation Required**: Yes
**Output**: README.md, deployment docs

## Coordination Protocol

### Before Starting Any Phase

```
1. Read docs/context/project_state.json
2. Check current phase
3. Verify prerequisites completed
4. Load relevant context
```

### After Completing Any Phase

```
## Phase Complete: [Phase Name]

### Status: SUCCESS

### Deliverables
- [x] [File 1]
- [x] [File 2]

### Decisions Made
- [Decision 1]
- [Decision 2]

### Next Phase
[Next phase name]

### User Action Required
[What user needs to do]
```

### User Confirmation Points

Must pause and wait for user:
1. After use case diagram
2. After architecture diagrams
3. After detailed design diagrams
4. After each vertical slice
5. After test report

## Error Handling

### Phase Failure

If a phase fails:
1. Record failure reason
2. Update blocking_issues
3. Present options to user:
   - Retry phase
   - Modify requirements
   - Skip to next phase
   - Abort project

### Context Loss

If context files missing:
1. Check git history
2. Reconstruct from documents
3. Re-initialize if necessary

## Integration with Other Skills

### se-lifecycle
- Provides phase definitions
- Defines entry/exit criteria

### se-diagram
- Generates all visualizations
- Called at each design phase

### se-context
- Manages state persistence
- Updates after each phase

### Sub-agents
- requirements-analyst
- system-architect
- detailed-designer
- full-stack-engineer
- qa-engineer

## Quick Reference

### Project Initialization
```bash
python .trae/tools/init_project.py "Name" "Description"
```

### Check Status
```bash
python .trae/tools/project_status.py
```

### Generate Diagram
```
Invoke se-diagram with type and content
```

### Update Context
```
Invoke se-context to update state
```

## Best Practices

1. Always check context before starting
2. Generate diagrams before user confirmation
3. Update state after each phase
4. Record all decisions
5. Keep progress.md updated
6. Version control all diagrams

## Common Patterns

### Pattern: Retry Failed Phase
```
User: "The use case diagram is missing X"
→ Update diagram
→ Re-present to user
→ Update state
```

### Pattern: Skip Phase
```
User: "I already have the design"
→ Load existing design
→ Validate completeness
→ Proceed to next phase
```

### Pattern: Parallel Development
```
For complex projects:
→ Split into parallel tracks
→ Coordinate via context
→ Merge at integration points
```
