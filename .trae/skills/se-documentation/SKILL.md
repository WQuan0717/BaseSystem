---
name: se-documentation
description: Documentation generation knowledge for software engineering. Provides methods for README, API docs, deployment guides, and user documentation generation.
---

# Documentation Generation

Professional knowledge for documentation phase. Generate comprehensive project documentation after development completion.

## Core Principles

### Principle 1: User-Centric
- Write for the target audience (developers, users, operators)
- Use clear, simple language
- Provide examples and code snippets

### Principle 2: Accuracy
- Documentation must match actual code behavior
- Keep documentation in sync with code
- Verify all commands and examples work

### Principle 3: Completeness
- Cover all essential aspects
- Include prerequisites, setup, usage, troubleshooting
- Provide links to related resources

### Principle 4: Maintainability
- Structure documentation for easy updates
- Use consistent formatting
- Separate stable content from version-specific content

### Principle 5: Discoverability
- Use clear headings and table of contents
- Include keywords for searchability
- Cross-reference related documentation

## Documentation Types

| Type | Audience | Purpose |
|------|----------|---------|
| README.md | All | Project overview and quick start |
| API.md | Developers | API reference documentation |
| DEPLOYMENT.md | DevOps | Deployment and operations guide |
| CONTRIBUTING.md | Contributors | Development and contribution guide |
| CHANGELOG.md | All | Version history and changes |

## README.md Template

```markdown
# Project Name

Brief description of what this project does and who it's for.

## Features

- Feature 1: Description
- Feature 2: Description

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | [Framework] [version] |
| Backend | [Framework] [version] |
| Database | [Database] [version] |

## Prerequisites

- Node.js >= 20.x
- PostgreSQL >= 16.x
- Docker (optional)

## Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/org/project.git
cd project
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 4. Setup Database

```bash
npm run migration:run
npm run seed:run
```

### 5. Start Development Server

```bash
npm run dev
```

## Project Structure

```
project/
├── frontend/          # Frontend application
├── backend/           # Backend application
├── docs/              # Documentation
└── scripts/           # Utility scripts
```

## Available Scripts

| Script | Description |
|--------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run test` | Run tests |

## API Documentation

See [API.md](./API.md) for detailed API documentation.

## Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for deployment guide.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for contribution guidelines.

## License

[MIT](./LICENSE)
```

## API.md Template

```markdown
# API Documentation

Base URL: `http://localhost:3000/api/v1`

## Authentication

All authenticated endpoints require a Bearer token:

```http
Authorization: Bearer <token>
```

## Endpoints

### Authentication

#### POST /auth/register

Register a new user.

**Request Body:**
```json
{
  "email": "string (required, valid email)",
  "password": "string (required, min 8 chars)",
  "name": "string (optional, max 100 chars)"
}
```

**Response (201):**
```json
{
  "code": 201,
  "message": "User registered successfully",
  "data": {
    "id": "uuid",
    "email": "user@example.com"
  }
}
```

**Errors:**
- 400: Invalid request body
- 409: Email already exists

#### POST /auth/login

Authenticate user and get token.

**Request Body:**
```json
{
  "email": "string (required)",
  "password": "string (required)"
}
```

**Response (200):**
```json
{
  "code": 200,
  "data": {
    "token": "jwt_token",
    "user": { "id": "uuid", "email": "user@example.com" }
  }
}
```

## Error Response Format

```json
{
  "code": 400,
  "message": "Error description",
  "errors": [
    { "field": "email", "message": "Invalid email format" }
  ]
}
```
```

## DEPLOYMENT.md Template

```markdown
# Deployment Guide

## Prerequisites

- Docker & Docker Compose
- PostgreSQL 16.x (if not using Docker)
- Domain name (optional)
- SSL certificate (optional)

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| NODE_ENV | Environment | Yes |
| DATABASE_URL | PostgreSQL connection | Yes |
| JWT_SECRET | JWT signing secret | Yes |

## Docker Deployment

### 1. Clone and Configure

```bash
git clone https://github.com/org/project.git
cd project
cp .env.example .env
```

### 2. Build and Run

```bash
docker-compose up -d
```

### 3. Verify

```bash
curl http://localhost:3000/health
```

## Production Checklist

- [ ] Environment variables configured
- [ ] Database migrations run
- [ ] SSL certificate installed
- [ ] Monitoring setup
- [ ] Backup strategy in place

## Troubleshooting

### Database Connection Failed
- Check DATABASE_URL is correct
- Verify database is running

### Application Won't Start
- Check logs: `docker-compose logs app`
- Verify environment variables
```

## CONTRIBUTING.md Template

```markdown
# Contributing Guide

## Development Setup

### Prerequisites

- Node.js >= 20.x
- PostgreSQL >= 16.x

### Setup Steps

1. Fork and clone the repository
2. Install dependencies: `npm install`
3. Copy environment: `cp .env.example .env`
4. Start database: `docker-compose up -d postgres`
5. Run migrations: `npm run migration:run`
6. Start dev server: `npm run dev`

## Development Workflow

### Branch Naming

- `feature/xxx` - New features
- `fix/xxx` - Bug fixes
- `docs/xxx` - Documentation updates

### Commit Messages

Follow conventional commits:

```
<type>(<scope>): <subject>

Types: feat, fix, docs, style, refactor, test, chore
```

### Pull Request Process

1. Create a feature branch
2. Make your changes
3. Run tests: `npm run test`
4. Run linter: `npm run lint`
5. Submit pull request

## Code Standards

- Use TypeScript strict mode
- Follow ESLint rules
- Write tests for new features
```

## CHANGELOG.md Template

```markdown
# Changelog

All notable changes will be documented here.

## [Unreleased]

### Added
- New features to be released

## [1.0.0] - 2024-01-01

### Added
- Initial release
- User authentication
- RESTful API endpoints

### Security
- JWT-based authentication
- Password hashing
```

## Quality Checklist

| Check | Criteria |
|-------|----------|
| README Complete | All sections filled, commands verified |
| API Docs Accurate | All endpoints documented |
| Deployment Guide Valid | Steps verified |
| Contributing Clear | Setup steps work |
| Changelog Updated | All changes documented |
