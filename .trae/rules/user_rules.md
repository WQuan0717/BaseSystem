# User Rules (示例配置)

这是一个示例个人规则配置，您可以根据自己的需求进行修改和使用。

---

## Profile
- Graduate student, AI major (RAG Agent direction)
- Average coding skills, heavily rely on AI tools
- Project scale: small applications, thesis projects, industry RAG agents

## Software Engineering Lifecycle

Use SOLO Coder mode with sub-agents. Invoke `se-lifecycle` SKILL for workflow decision rules.

| Phase | Sub-agent | Output |
|-------|-----------|--------|
| Requirements | requirements-analyst | Requirement.md |
| Architecture | system-architect | Design.md |
| Detailed Design | detailed-designer | DetailedDesign.md |
| Development | full-stack-engineer | Code + Tests |
| Testing | qa-engineer | TestReport.md |
| Documentation | technical-writer | README.md etc |

## Tech Stack

**Web Projects:** Vue 3 + Vite + TypeScript | Node.js + Express | PostgreSQL + Prisma | Redis

**AI/RAG Projects:** Python + FastAPI | PostgreSQL + pgvector | LangChain/LlamaIndex | Vue 3 or Streamlit

## Working Style
- Use TodoWrite for complex tasks
- Provide complete code examples, not fragments
- Add Chinese comments for clarity
- Keep simple, avoid over-engineering
- Small projects use monolith architecture, no microservices
