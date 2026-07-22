# KerryHuang Claude Code Plugin Marketplace

A multi-plugin marketplace for Claude Code.

## Installation

```bash
# 1. Register marketplace (one-time)
claude plugin marketplace add https://github.com/KerryHuang/kerryhuang-plugins.git

# 2. Install a plugin
claude plugin install sdlc
```

## Available Plugins

| Plugin | Description |
|--------|-------------|
| [sdlc](./plugins/sdlc/README.md) | Software development lifecycle upstream phase tools — requirements, system analysis, specification, verification, and ticket creation |
| [dev-flow](./plugins/dev-flow/README.md) | 跨語言開發工作流 — git 生命週期、工作編排、context 治理 |
| [backend-dotnet](./plugins/backend-dotnet/README.md) | .NET Clean Architecture 後端 — CQRS/Repository/EF Core/Dapper 產碼、測試、agents |
| [frontend-vue](./plugins/frontend-vue/README.md) | Vue 3 + TypeScript + Quasar 前端 — 架構、composable、除錯、i18n、OpenSpec |

## License

MIT License — Copyright (c) 2026 Kerry Huang
