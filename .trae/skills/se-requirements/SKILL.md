---
name: se-requirements
description: Requirements analysis knowledge for software engineering. Provides methods for requirement elicitation, MoSCoW prioritization, questioning techniques, and Requirement.md generation.
---

# Requirements Analysis

Professional knowledge for requirements phase. Transform vague user ideas into structured Requirement.md.

## Core Principles

### Principle 1: Question First
- If user input is vague, ask 3-5 high-value questions before generating document
- Focus on: users, core flows, must-have features, scale expectations
- Avoid technical jargon in questions

### Principle 2: No Technical Terms
- Define "what to do", not "how to implement"
- Use business language, not technical language
- Let architects decide technology choices

### Principle 3: Implicit Mining
- Proactively consider exception paths and edge cases
- Think about: error handling, permissions, data validation
- Ask about non-functional requirements (performance, security, scalability)

### Principle 4: Downstream Friendly
- Include inputs for Architect, Designer, Engineer, QA
- Clear acceptance criteria for each requirement
- Prioritize with MoSCoW

## Questioning Framework

### 5W1H Analysis

| Dimension | Questions |
|-----------|-----------|
| Who | Who are the users? What roles exist? |
| What | What is the core functionality? What problem to solve? |
| When | When is the deadline? What phases? |
| Where | Where will it be used? Web/Mobile/Desktop? |
| Why | Why build this? What's the business value? |
| How | How should it work? Any constraints? |

### High-Value Questions

**For vague ideas:**
1. 这个系统的主要使用者是谁？他们需要解决什么核心问题？
2. 请描述一下最核心的 1-2 个业务流程是怎样的？
3. 有没有哪些功能是必须在第一版就实现的？
4. 预期的用户规模和数据量大概是多少？

**For Excel workflows:**
1. 你们目前的 Excel 流程主要是做什么的？
2. 涉及哪些角色和人员？
3. 最核心的业务步骤有哪些？
4. 线上化后希望解决什么问题？

**For existing ideas:**
1. 你们目前有哪些具体的想法？
2. 这个项目的主要目标是什么？
3. 有没有哪些功能是必须优先实现的？

## Requirement Elicitation

### Input Sources
- User interviews (direct conversation)
- Excel files (business process documentation)
- PDF documents (specifications, contracts)
- Existing systems (analysis of current workflow)

### Analysis Steps
1. Read all input sources
2. Extract functional requirements
3. Extract non-functional requirements
4. Identify user roles and permissions
5. Identify data entities
6. Identify business rules
7. Prioritize with MoSCoW

## Requirement.md Template

```markdown
# 项目需求文档

## 1. 项目概述

### 1.1 项目背景
[为什么做这个项目？解决什么问题？]

### 1.2 项目目标
[项目要达成的目标，可量化的指标]

### 1.3 范围边界
[包含什么，不包含什么]

## 2. 用户角色

| 角色 | 描述 | 权限级别 |
|------|------|---------|
| 角色1 | 描述 | 权限 |

## 3. 功能需求

### 3.1 P0 必须实现

#### REQ-001: [功能名称]

**描述**: [功能描述]

**用户故事**: 作为 [角色]，我希望 [功能]，以便 [价值]

**验收标准**:
- [ ] 标准1
- [ ] 标准2

**业务规则**:
- 规则1
- 规则2

### 3.2 P1 应该实现

[同上格式]

### 3.3 P2 可以实现

[同上格式]

### 3.4 P3 暂不实现

[同上格式]

## 4. 非功能需求

### 4.1 性能要求
- 响应时间: [要求]
- 并发用户: [数量]
- 数据量: [预期规模]

### 4.2 安全要求
- 认证方式: [方式]
- 数据保护: [要求]
- 权限控制: [要求]

### 4.3 可用性要求
- 可用性: [99.9%等]
- 备份策略: [策略]

## 5. 数据需求

### 5.1 核心数据实体

| 实体 | 描述 | 主要属性 |
|------|------|---------|
| 实体1 | 描述 | 属性列表 |

### 5.2 数据关系
[实体之间的关系描述]

## 6. 约束条件

### 6.1 技术约束
[现有系统、技术栈限制等]

### 6.2 业务约束
[法规、政策、业务规则等]

### 6.3 时间约束
[里程碑、截止日期等]

## 7. 附录

### 7.1 术语表
| 术语 | 定义 |
|------|------|
| 术语1 | 定义 |

### 7.2 参考文档
- 文档1
- 文档2
```

## Quality Checklist

| Check | Criteria |
|-------|----------|
| Completeness | All P0 features documented |
| Clarity | No ambiguous terms |
| Testability | Acceptance criteria defined |
| Traceability | Each requirement has ID |
| Prioritization | MoSCoW applied |
| Downstream Ready | Contains inputs for next phases |
