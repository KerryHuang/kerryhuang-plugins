# kerryhuang-plugins

A Claude Code plugin for **software development lifecycle upstream phases** — everything before implementation: requirements, system analysis, specification, verification, and ticket creation.

> [繁體中文版](README.zh-TW.md)

## Installation

```bash
# 1. Register marketplace (one-time)
claude plugin marketplace add git@github.com:KerryHuang/kerryhuang-plugins.git

# 2. Install plugin
claude plugin install sdlc

# For private repos, set GitLab token for auto-updates:
# Windows: System Environment Variable GITLAB_TOKEN = glpat_xxx
# Linux/macOS: export GITLAB_TOKEN=glpat_xxx in ~/.bashrc or ~/.zshrc
```

## Skills

### Core Workflow

| Skill | Command | Description |
|-------|---------|-------------|
| **requirement** | `/sdlc:requirement` | Write functional requirement documents (FRD / CR-FRD) as a senior PM |
| **system-analysis** | `/sdlc:system-analysis` | Analyze workflow, information flow, and data flow from FRD to produce SAD |
| **specify** | `/sdlc:specify` | Create backend/frontend specification documents (BFS / FFS / CR-BFS / CR-FFS) |
| **verifying-specs** | `/sdlc:verifying-specs` | Validate spec quality, architecture feasibility, and cross-document consistency |
| **linear-create** | `/sdlc:linear-create` | Create Linear ticket hierarchies (Feature: PM > QA > Dev / Bug: QA > Dev) |

### Specialized

| Skill | Command | Description |
|-------|---------|-------------|
| **foxpro-analyzer** | `/sdlc:foxpro-analyzer` | Analyze FoxPro legacy systems for migration (UI, CRUD, validation, data comparison) |

### Self-Evolution

| Skill | Command | Description |
|-------|---------|-------------|
| **plugin-healthcheck** | `/sdlc:plugin-healthcheck` | Check against latest Claude Code plugin specs, produce health report |
| **retrospective** | `/sdlc:retrospective` | Extract improvements from session experience, evolve plugin content |

## Integration with Superpowers

This plugin is designed to work alongside the [superpowers](https://github.com/anthropics/claude-code-superpowers) plugin.

- **superpowers** drives the process (brainstorming, planning, executing, reviewing)
- **sdlc** produces the documents (FRD, SAD, BFS, verification reports)

Install both plugins for the full pipeline:

```bash
claude plugin install sdlc
claude plugin install superpowers
```

## Development Pipeline

### New Feature Flow

```
[ superpowers:brainstorming ]        → design doc
         ↓
[ sdlc:requirement ]                 → FRD
         ↓
[ sdlc:system-analysis ]             → SAD
         ↓
[ sdlc:specify ]                     → BFS
         ↓
[ sdlc:verifying-specs ]             → verification report
         ↓
[ sdlc:linear-create ]               → Linear tickets
         ↓
[ superpowers:writing-plans ]        → implementation plan
         ↓
[ superpowers:subagent-driven-development ]
         ↓
[ superpowers:verification-before-completion ]
         ↓
[ superpowers:requesting-code-review ]
         ↓
[ superpowers:finishing-a-development-branch ]
```

### Change Request Flow

> CR flow skips brainstorming — requirements are already clear.

```
[ sdlc:requirement --change ]        → CR-FRD
         ↓
[ sdlc:specify --change ]            → CR-BFS + CR-FFS
         ↓
[ sdlc:verifying-specs ]             → verification report
         ↓
[ sdlc:linear-create ]               → Linear tickets
         ↓
[ superpowers:writing-plans ]        → (continues as above)
```

## Workflow (sdlc only)

```
requirement → system-analysis → specify → verifying-specs → [hand off to implementation]
    FRD            SAD           BFS+FFS      verified
    PM role        SA role       Dev role
```

For feature changes, use `--change` flag:
```
/sdlc:requirement --change → system-analysis → /sdlc:specify --change
       CR-FRD                      SAD              CR-BFS + CR-FFS
```

## Core Principle: No Guessing

All analysis/spec skills enforce a strict no-guessing policy:

1. **Search first** — look for answers in the project codebase, docs, and DB
2. **Ask with suggestions** — if not found, ask the user with recommended solutions
3. **Confirm before writing** — all questions resolved before any document is written
4. **Pre-write checklist** — final review of all collected information before writing

## Templates

| Template | File | Purpose |
|----------|------|---------|
| FRD | `templates/frd.md` | Functional Requirement Document |
| CR-FRD | `templates/cr-frd.md` | Change Request FRD |
| SAD | `templates/sad.md` | System Analysis Document |
| BFS | `templates/bfs.md` | Backend Functional Specification |
| CR-BFS | `templates/cr-bfs.md` | Change Request BFS |
| FFS | `templates/ffs.md` | Frontend Functional Specification |
| CR-FFS | `templates/cr-ffs.md` | Change Request FFS |

## References

| Reference | Purpose |
|-----------|---------|
| `upstream-workflow.md` | Phase sequence and responsibilities |
| `analysis-standards.md` | MES domain analysis framework |
| `response-structure-standards.md` | API response nested structure standards |
| `linear-workflow.md` | Linear ticket lifecycle and handoff rules |
| `linear-ticket-defaults.md` | Ticket defaults, assignees, and description templates |
| `auto-verification-loop.md` | Auto-verify and fix cycle after document writing |

## Project Structure

```
kerryhuang-plugins/
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
├── skills/
│   ├── requirement/SKILL.md
│   ├── system-analysis/SKILL.md
│   ├── specify/SKILL.md
│   ├── verifying-specs/SKILL.md    + references/
│   ├── linear-create/SKILL.md
│   ├── foxpro-analyzer/SKILL.md    + references/ + scripts/
│   ├── plugin-healthcheck/SKILL.md
│   └── retrospective/SKILL.md
├── references/
├── templates/
└── README.md
```

## Customization

This plugin uses **placeholders** for team-specific values. After installation, update these in `references/`:

| Placeholder | Example |
|-------------|---------|
| `{PM_team}` | `MoldPlanPM` |
| `{QA_team}` | `MoldPlanQA` |
| `{Dev_team}` | `MoldPlanDev` |
| `{QA_assignee}` | `weijyunye` |
| `{backend_assignee}` | `tony.tsai` |
| `{frontend_assignee}` | `weihuang` |

Project-specific technical details (CQRS, MediatR, EF Core, etc.) should be defined in your project's `.claude/rules/` — the plugin provides the universal workflow, and project rules provide the technical specifics. Both are merged at runtime.

## License

MIT License — Copyright (c) 2026 Kerry Huang
