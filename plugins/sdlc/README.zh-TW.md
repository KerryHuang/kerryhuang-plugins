# kerryhuang-plugins

Claude Code 外掛，用於**軟體開發生命週期上游階段** — 實作之前的所有工作：需求、系統分析、規格、驗證、開票。

> [English Version](README.md)

## 安裝

```bash
# 1. 註冊 marketplace（一次性）
claude plugin marketplace add git@github.com:KerryHuang/kerryhuang-plugins.git

# 2. 安裝外掛
claude plugin install sdlc

# 私有 repo 需設定 GitLab token 以支援自動更新：
# Windows：系統環境變數 GITLAB_TOKEN = glpat_xxx
# Linux/macOS：在 ~/.bashrc 或 ~/.zshrc 加入 export GITLAB_TOKEN=glpat_xxx
```

## 技能一覽

### 核心工作流

| 技能 | 指令 | 說明 |
|------|------|------|
| **requirement** | `/sdlc:requirement` | 以資深 PM 角色撰寫功能需求文件（FRD / CR-FRD） |
| **system-analysis** | `/sdlc:system-analysis` | 從 FRD 分析工作流、資訊流、資料流，產出系統分析文件（SAD） |
| **specify** | `/sdlc:specify` | 建立後端/前端功能規格書（BFS / FFS / CR-BFS / CR-FFS） |
| **verifying-specs** | `/sdlc:verifying-specs` | 驗證規格品質、架構可行性、跨文件一致性 |
| **linear-create** | `/sdlc:linear-create` | 建立 Linear 票層級結構（Feature: PM→QA→Dev / Bug: QA→Dev） |

### 專業工具

| 技能 | 指令 | 說明 |
|------|------|------|
| **foxpro-analyzer** | `/sdlc:foxpro-analyzer` | 分析 FoxPro 舊系統（畫面、CRUD、驗證、資料比對） |

### 自我進化

| 技能 | 指令 | 說明 |
|------|------|------|
| **plugin-healthcheck** | `/sdlc:plugin-healthcheck` | 對比 Claude Code 官方最新規範，產出健康報告 |
| **retrospective** | `/sdlc:retrospective` | 從 session 使用體驗中提取改進點，進化 plugin 內容 |

## 與 Superpowers 整合

本 plugin 設計上與 [superpowers](https://github.com/anthropics/claude-code-superpowers) plugin 搭配使用。

- **superpowers** — 驅動流程（brainstorming、規劃、執行、審查）
- **sdlc** — 產出文件（FRD、SAD、BFS、驗證報告）

安裝兩個 plugin 以使用完整流程：

```bash
claude plugin install sdlc
claude plugin install superpowers
```

## 完整開發流程

### 新功能流程

```
[ superpowers:brainstorming ]        → 設計文件
         ↓
[ sdlc:requirement ]                 → FRD 功能需求文件
         ↓
[ sdlc:system-analysis ]             → SAD 系統分析文件
         ↓
[ sdlc:specify ]                     → BFS 後端功能規格書
         ↓
[ sdlc:verifying-specs ]             → 驗證報告
         ↓
[ sdlc:linear-create ]               → Linear tickets
         ↓
[ superpowers:writing-plans ]        → 實作計畫
         ↓
[ superpowers:subagent-driven-development ]
         ↓
[ superpowers:verification-before-completion ]
         ↓
[ superpowers:requesting-code-review ]
         ↓
[ superpowers:finishing-a-development-branch ]
```

### CR 流程（功能調整）

> CR 流程需求已明確，跳過 brainstorming，直接開始。

```
[ sdlc:requirement --change ]        → CR-FRD
         ↓
[ sdlc:specify --change ]            → CR-BFS + CR-FFS
         ↓
[ sdlc:verifying-specs ]             → 驗證報告
         ↓
[ sdlc:linear-create ]               → Linear tickets
         ↓
[ superpowers:writing-plans ]        → （同上後半段）
```

## 工作流程（僅 sdlc）

```
需求文件 → 系統分析 → 功能規格書 → 驗證規格書 → [交付實作]
  FRD        SAD       BFS+FFS      已驗證
  PM角色     SA角色    開發者角色
```

功能調整使用 `--change` 參數：
```
/sdlc:requirement --change → 系統分析 → /sdlc:specify --change
       CR-FRD                   SAD         CR-BFS + CR-FFS
```

## 核心原則：不猜測

所有分析/規格技能遵循嚴格的不猜測政策：

1. **先找答案** — 在專案程式碼、文件、DB 中搜尋
2. **帶建議詢問** — 找不到就問使用者，附上建議方案
3. **確認後才寫** — 所有疑問解決後才開始撰寫文件
4. **寫前總清查** — 撰寫前最終檢查所有已收集資訊

## 範本

| 範本 | 檔案 | 用途 |
|------|------|------|
| FRD | `templates/frd.md` | 功能需求文件 |
| CR-FRD | `templates/cr-frd.md` | 功能調整需求文件 |
| SAD | `templates/sad.md` | 系統分析文件 |
| BFS | `templates/bfs.md` | 後端功能規格書 |
| CR-BFS | `templates/cr-bfs.md` | 功能調整後端規格書 |
| FFS | `templates/ffs.md` | 前端功能規格書 |
| CR-FFS | `templates/cr-ffs.md` | 功能調整前端規格書 |

## 參考文件

| 參考文件 | 用途 |
|---------|------|
| `upstream-workflow.md` | 上游階段順序與職責 |
| `analysis-standards.md` | MES 領域分析框架 |
| `response-structure-standards.md` | API Response 巢狀結構規範 |
| `linear-workflow.md` | Linear 票生命週期與交接規則 |
| `linear-ticket-defaults.md` | 票預設值、指派人、描述範本 |
| `auto-verification-loop.md` | 文件寫完後自動驗證修復循環 |

## 專案結構

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
├── README.md
└── README.zh-TW.md
```

## 客製化

本外掛使用**佔位符**表示團隊特定值。安裝後需在 `references/` 中替換：

| 佔位符 | 範例 |
|--------|------|
| `{PM_team}` | `MoldPlanPM` |
| `{QA_team}` | `MoldPlanQA` |
| `{Dev_team}` | `MoldPlanDev` |
| `{QA_assignee}` | `weijyunye` |
| `{backend_assignee}` | `tony.tsai` |
| `{frontend_assignee}` | `weihuang` |

專案特定的技術細節（CQRS、MediatR、EF Core 等）應定義在專案的 `.claude/rules/` 中 — 外掛提供通用工作流，專案 rules 提供技術規範，兩者在執行時自動合併。

## 授權

MIT 授權 — Copyright (c) 2026 Kerry Huang
