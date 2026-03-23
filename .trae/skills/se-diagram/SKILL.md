---
name: se-diagram
description: Generate Mermaid diagrams for software engineering. Creates usecase, architecture, ER, class, and flowchart diagrams from text descriptions.
---

# Diagram Generation for Software Engineering

Generate Mermaid diagrams from text descriptions and design documents.

**Previous Skill**: Invoked by other phase skills (se-requirements, se-architecture, se-detailed-design)

**Next Skill**: Returns to calling skill

## Core Principles

### 1. Text to Diagram
- Parse natural language or structured text
- Generate corresponding Mermaid syntax
- Ensure diagram accuracy and completeness

### 2. Standard Notation
- Follow UML standards for structure diagrams
- Use clear, readable naming conventions
- Include relationships and cardinalities

### 3. Completeness
- Include all entities/actors mentioned
- Show all relationships
- Add necessary attributes/fields

## Diagram Types

### 1. Use Case Diagram (usecase.mmd)

**Input**: Requirement description, user roles, features
**Output**: Mermaid usecase diagram

**Generation Rules**:
1. Identify all actors (users, external systems)
2. Identify all use cases (features/functions)
3. Group related use cases into packages
4. Connect actors to use cases they interact with

**Template**:
```mermaid
usecaseDiagram
    actor "Actor1" as A1
    actor "Actor2" as A2
    
    package "System Name" {
        usecase "Use Case 1" as UC1
        usecase "Use Case 2" as UC2
        usecase "Use Case 3" as UC3
    }
    
    A1 --> UC1
    A1 --> UC2
    A2 --> UC3
    
    UC1 ..> UC2 : <<include>>
    UC3 ..> UC2 : <<extend>>
```

**Example Generation**:
```
Input: "校园学习平台有学生、教师、管理员三种角色。学生可以浏览博客、发布博客、在线答题。教师可以组卷、审核文章。管理员可以管理用户。"

Output:
```mermaid
usecaseDiagram
    actor "学生" as Student
    actor "教师" as Teacher
    actor "管理员" as Admin
    
    package "校园学习平台" {
        usecase "浏览博客" as UC1
        usecase "发布博客" as UC2
        usecase "在线答题" as UC3
        usecase "组卷" as UC4
        usecase "审核文章" as UC5
        usecase "用户管理" as UC6
    }
    
    Student --> UC1
    Student --> UC2
    Student --> UC3
    Teacher --> UC4
    Teacher --> UC5
    Admin --> UC6
```
```

### 2. Architecture Diagram (architecture.mmd)

**Input**: Tech stack, system components, deployment info
**Output**: Mermaid graph showing system architecture

**Generation Rules**:
1. Group components by layer (client, gateway, backend, data)
2. Show connections between components
3. Include technology labels
4. Indicate data flow direction

**Template**:
```mermaid
graph TB
    subgraph "客户端层"
        A[Vue 3 + Element Plus]
        B[移动端APP]
    end
    
    subgraph "网关层"
        C[Nginx反向代理]
        D[API Gateway]
    end
    
    subgraph "服务层"
        E[Spring Boot应用]
        F[用户服务]
        G[业务服务]
    end
    
    subgraph "数据层"
        H[(MySQL主库)]
        I[(MySQL从库)]
        J[(Redis缓存)]
        K[(Elasticsearch)]
    end
    
    A --> C
    B --> D
    C --> E
    D --> E
    E --> F
    E --> G
    F --> H
    F --> J
    G --> H
    G --> I
    G --> K
```

### 3. ER Diagram (erdiagram.mmd)

**Input**: Database design, entity descriptions
**Output**: Mermaid ER diagram

**Generation Rules**:
1. Identify all entities (tables)
2. Identify attributes for each entity
3. Mark primary keys (PK) and foreign keys (FK)
4. Define relationships with cardinalities

**Template**:
```mermaid
erDiagram
    USER ||--o{ ARTICLE : writes
    USER ||--o{ COMMENT : writes
    ARTICLE ||--o{ COMMENT : has
    ARTICLE }o--o{ TAG : tagged_with
    
    USER {
        bigint id PK
        varchar username
        varchar email
        varchar password
        enum role
        timestamp created_at
    }
    
    ARTICLE {
        bigint id PK
        varchar title
        text content
        bigint author_id FK
        enum status
        timestamp published_at
    }
    
    COMMENT {
        bigint id PK
        text content
        bigint author_id FK
        bigint article_id FK
        timestamp created_at
    }
    
    TAG {
        int id PK
        varchar name
        varchar color
    }
```

**Relationship Notations**:
- `||--o{` : One to Many
- `||--||` : One to One
- `}o--o{` : Many to Many
- `}|--|{` : Many to One

### 4. Class Diagram (classdiagram.mmd)

**Input**: Module design, class descriptions
**Output**: Mermaid class diagram

**Generation Rules**:
1. Identify all classes
2. Define attributes (visibility + type)
3. Define methods (visibility + params + return)
4. Show relationships (inheritance, composition, association)

**Template**:
```mermaid
classDiagram
    class UserController {
        -UserService userService
        +login(LoginDTO dto) Response
        +register(RegisterDTO dto) Response
        +getUserProfile() UserVO
        +updateProfile(UpdateDTO dto) Response
    }
    
    class UserService {
        -UserRepository userRepo
        -PasswordEncoder encoder
        +authenticate(email, password) User
        +createUser(dto) User
        +updateUser(id, dto) User
        +deleteUser(id) void
        +getUserById(id) User
    }
    
    class UserRepository {
        +findById(id) Optional~User~
        +findByEmail(email) Optional~User~
        +findByUsername(username) Optional~User~
        +save(user) User
        +deleteById(id) void
    }
    
    class User {
        -Long id
        -String username
        -String email
        -String password
        -Role role
        -LocalDateTime createdAt
        +getters()
        +setters()
    }
    
    class LoginDTO {
        +String email
        +String password
    }
    
    class UserVO {
        +Long id
        +String username
        +String email
        +Role role
    }
    
    UserController --> UserService : uses
    UserService --> UserRepository : uses
    UserRepository --> User : manages
    UserController ..> LoginDTO : receives
    UserController ..> UserVO : returns
```

**Visibility Notations**:
- `+` : public
- `-` : private
- `#` : protected
- `~` : package

**Relationship Types**:
- `-->` : Association
- `..>` : Dependency
- `--|>` : Inheritance
- `--*` : Composition
- `--o` : Aggregation

### 5. Flowchart (flowchart.mmd)

**Input**: Business process description
**Output**: Mermaid flowchart

**Generation Rules**:
1. Identify start and end points
2. Identify decision points (diamonds)
3. Identify process steps (rectangles)
4. Show alternative paths

**Template**:
```mermaid
flowchart TD
    Start([开始]) --> CheckAuth{用户已登录?}
    
    CheckAuth -->|否| Login[跳转登录页]
    Login --> InputCred[输入账号密码]
    InputCred --> Validate{验证通过?}
    Validate -->|否| ShowError[显示错误]
    ShowError --> InputCred
    Validate -->|是| CheckAuth
    
    CheckAuth -->|是| LoadData[加载数据]
    LoadData --> Display[显示界面]
    Display --> UserAction{用户操作}
    
    UserAction -->|操作A| ProcessA[处理A]
    UserAction -->|操作B| ProcessB[处理B]
    UserAction -->|退出| Logout[注销登录]
    
    ProcessA --> SaveData[保存数据]
    ProcessB --> SaveData
    SaveData --> ShowResult[显示结果]
    ShowResult --> Display
    
    Logout --> ClearSession[清除会话]
    ClearSession --> End([结束])
```

**Node Types**:
- `[文本]` : Process
- `{文本}` : Decision
- `([文本])` : Start/End
- `[[文本]]` : Subroutine
- `[(文本)]` : Database
- `{{文本}}` : Preparation

## Usage Workflow

### Step 1: Identify Diagram Type
Based on current phase:
- Requirements → Use Case Diagram
- Architecture → Architecture + ER Diagram
- Detailed Design → Class + Flowchart

### Step 2: Extract Information
Parse input for:
- Entities/Actors
- Attributes/Features
- Relationships
- Processes/Flows

### Step 3: Generate Mermaid Syntax
Follow templates and rules above.

### Step 4: Validate
Check for:
- Completeness (all elements included)
- Correctness (valid Mermaid syntax)
- Clarity (readable names and labels)

### Step 5: Save and Reference
- Save to `docs/diagrams/[filename].mmd`
- Reference in main document
- Include in version control

## Integration with Other Skills

### With se-requirements
Input: Requirement.md
Output: usecase.mmd

### With se-architecture
Input: Design.md
Output: architecture.mmd + erdiagram.mmd

### With se-detailed-design
Input: DetailedDesign.md
Output: classdiagram.mmd + flowchart.mmd

## Best Practices

1. **Keep it Simple**: Don't include too many elements in one diagram
2. **Consistent Naming**: Use consistent naming conventions
3. **Group Related Elements**: Use subgraphs/packages for organization
4. **Show Key Relationships**: Focus on important connections
5. **Update with Changes**: Keep diagrams in sync with code

## Common Patterns

### Web Application Pattern
```mermaid
graph LR
    A[浏览器] --> B[前端Vue]
    B --> C[后端API]
    C --> D[(数据库)]
```

### CRUD Pattern
```mermaid
flowchart TD
    A[列表页] --> B{操作}
    B -->|新增| C[创建页]
    B -->|编辑| D[编辑页]
    B -->|删除| E[确认删除]
    B -->|查看| F[详情页]
    C --> G[保存]
    D --> G
    E --> H[删除]
    G --> A
    H --> A
```

### Authentication Pattern
```mermaid
flowchart TD
    A[访问页面] --> B{已登录?}
    B -->|是| C[正常访问]
    B -->|否| D[跳转登录]
    D --> E[输入凭证]
    E --> F{验证成功?}
    F -->|是| G[创建会话]
    F -->|否| H[显示错误]
    H --> E
    G --> C
```
