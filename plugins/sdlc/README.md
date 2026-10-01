# sdlc

Claude Code 外掛，涵蓋**軟體開發生命週期的上游與驗收**：需求探索、需求文件、系統分析、前後端規格、開發就緒度、規格驗證、開票，以及完工後的實機驗收與操作手冊。

規格書一律**技術中立**：只寫行為、契約、資料語意、權限邊界與上線風險；框架、快取、鎖、佇列等手段層由開發者決定，規格中遇到手段層問題一律寫成 TD 技術決策留置。

## 安裝

```bash
# 1. 註冊 marketplace（一次性）
claude plugin marketplace add https://github.com/KerryHuang/kerryhuang-plugins.git

# 2. 安裝外掛（建議搭配 superpowers）
claude plugin install sdlc
claude plugin install superpowers
```

## 專案設定

在專案根目錄的 `CLAUDE.md` 加入以下設定鍵，全部選填：

```markdown
sdlc-docs-path: ../docs
sdlc-linear-teams: PM=<team>, SA=<team>, QA=<team>, Dev=<team>
sdlc-linear-assignees: QA=<email>, backend=<email>, frontend=<email>
sdlc-linear-labels: PM=<label>, SA=<label>, QA=<label>, backend=<label>, frontend=<label>
sdlc-program-code-inventory: system/feature-inventory.md
sdlc-spec-rules-since: 2026-10-01
```

| 設定鍵 | 用途 | 未設定時 |
|---|---|---|
| `sdlc-docs-path` | 規格文件根目錄（文中稱 `{docs-root}`） | 專案內 `docs/` |
| `sdlc-linear-teams`／`-assignees`／`-labels` | 各票種開在哪個 team、指派給誰、必帶哪些 label | 執行時以 Linear MCP 查詢並讓你選 |
| `sdlc-program-code-inventory` | 功能代碼盤點文件位置（權限控管用） | 跳過功能代碼查核 |
| `sdlc-spec-rules-since` | 畫面規格新規範的生效日，早於此日且本次未觸及的畫面降為 INFO | 全部文件都適用 |

選配整合：Linear MCP、`chrome-devtools` MCP（實機操作）、唯讀 DB 查詢 MCP、Graphify。偵測不到就降級或跳過，不會中斷流程。

## 技能一覽

### 規格鏈

| 技能 | 用法 | 產出 |
|---|---|---|
| **explore** | `/sdlc:explore [功能描述]` | 探索摘要（六維引導問答） |
| **interview-prep** | `/sdlc:interview-prep [素材…] 或 [受訪者／主題]` | 已知／未知盤點或訪談大綱 |
| **requirement** | `/sdlc:requirement [--change] {需求描述}` | FRD／CR-FRD |
| **system-analysis** | `/sdlc:system-analysis [功能名稱或 FRD 路徑]` | SAD（工作流、資訊流、資料流） |
| **specify-backend** | `/sdlc:specify-backend [--change] {功能描述}` | BFS／CR-BFS |
| **specify-frontend** | `/sdlc:specify-frontend [--change] {功能描述}` | FFS／CR-FFS |
| **dev-readiness** | `/sdlc:dev-readiness [功能目錄]` | 就緒度報告：對抗式找出邊界缺口並回寫規格 |
| **verifying-specs** | `/sdlc:verifying-specs [文件] [--cross] [--recheck] [--quick\|--full]` | 驗證報告 |

### Linear

| 技能 | 用法 | 說明 |
|---|---|---|
| **linear-create** | `/sdlc:linear-create {描述}` | 建立票樹（Feature：PM→SA→QA→Dev；Bug：QA→Dev） |
| **linear-triage** | `/sdlc:linear-triage <票號>` | 判型：Feature 引導進規格鏈，Bug 找根因 |
| **linear-reply** | `/sdlc:linear-reply <票號>` | 回覆票上未答留言並回寫規格 |
| **linear-illustrate** | `/sdlc:linear-illustrate <票號> [畫面]` | 為票補實機截圖與標註 |
| **linear-daily-report** | `/sdlc:linear-daily-report [--project] [--date]` | 每日進度報表 |
| **linear-weekly-report** | `/sdlc:linear-weekly-report [--project] [--date]` | 週會報表與簡報 |
| **issue-triage** | `/sdlc:issue-triage [會議記錄或回饋清單]` | 回饋分類成 Bug／Enhancement／Feature |
| **dev-feedback** | `/sdlc:dev-feedback [--apply] {票號}` | 開發端對票面的回饋，回頭修正 plugin |

### 實機與驗收

| 技能 | 用法 | 說明 |
|---|---|---|
| **live-drive** | `/sdlc:live-drive <investigate\|manual\|e2e\|explore> [URL]` | 操作執行中的系統；正式環境禁止異動 |
| **qa-verify** | `/sdlc:qa-verify <功能或票號>` | 依 FFS 驗收標準逐條實機驗收 |
| **operation-manual** | `/sdlc:operation-manual <功能目錄或 URL>` | 操作手冊與教育訓練簡報（PDF／PPTX） |
| **sample-verify** | `/sdlc:sample-verify <規格> [原始碼範圍]` | 抽樣原始碼驗證規格覆蓋度 |

### 文件工具

| 技能 | 用法 | 說明 |
|---|---|---|
| **meeting-minutes** | `/sdlc:meeting-minutes [即時\|整理] [主題]` | 結構化會議記錄 |
| **pdf-converter** | `/sdlc:pdf-converter <PDF> [--to word\|excel]` | PDF 轉 Word／Excel，含回轉驗證 |
| **write-doc** | `/sdlc:write-doc [路徑]` | 把口述或既有內容落檔 |
| **foxpro-analyzer** | `/sdlc:foxpro-analyzer {檔案路徑}` | FoxPro 舊系統分析，起頭的鏈套用 parity 模式 |

### 自我進化

| 技能 | 用法 | 說明 |
|---|---|---|
| **retrospective** | `/sdlc:retrospective [--apply] [skill]` | 從使用經驗提取改進點 |
| **plugin-healthcheck** | `/sdlc:plugin-healthcheck [--fix]` | 對照 Claude Code 官方規範的健康檢查 |

## 架構

- **主 session 統整派工**：蒐證、撰寫、審查都派給專責 agent，主 session 只做決策與驗收（`references/dispatch-conventions.md`）。
- **spec-writer 落檔**：FRD／SAD／BFS／FFS 由 `spec-writer` agent 依範本、證據檔與已拍板決策寫入。
- **共用前置規則**：每一棒都先載入 `references/shared-preludes.md`（先推導再詢問、不猜測、權威來源優先序、技術中立）。
- **分析產物共用**：勘察結果落在 `{功能目錄}/analysis/`，下游先讀再補缺，不重複蒐證。
- **chain profile**：依功能規模走完整鏈或 lite 鏈，小功能不付大功能的流程稅（`references/chain-profile.md`）。

Agents：spec-writer、domain-advisor、scout、report-writer、spec-sampler、doc-fidelity-reviewer、browser-surveyor、qa-planner、qa-runner-ui、qa-fixture、manual-explorer、manual-writer、manual-reviewer。

## 完整流程

```
[ sdlc:explore ] 或 [ superpowers:brainstorming ]
         ↓
[ sdlc:requirement ]        → FRD
         ↓
[ sdlc:system-analysis ]    → SAD
         ↓
[ sdlc:specify-backend ]    → BFS
         ↓
[ sdlc:specify-frontend ]   → FFS
         ↓
[ sdlc:dev-readiness ]      → 就緒度報告
         ↓
[ sdlc:verifying-specs ]    → 驗證報告
         ↓
[ sdlc:linear-create ]      → Linear tickets
         ↓
[ superpowers:writing-plans ] → 實作 → 審查
         ↓
[ sdlc:qa-verify ]          → 驗收報告
```

功能調整（CR）從 `requirement --change` 開始，接 `specify-backend --change`、`specify-frontend --change`，其餘相同。各棒的前置條件與交棒規則見 `references/pipeline.md` 與 `references/handoff-protocol.md`。

## 範本

| 範本 | 檔案 |
|---|---|
| FRD／CR-FRD | `templates/frd.md`、`templates/cr-frd.md` |
| SAD | `templates/sad.md` |
| BFS／CR-BFS | `templates/bfs.md`、`templates/cr-bfs.md` |
| FFS／CR-FFS | `templates/ffs.md`、`templates/cr-ffs.md` |
| 訪談大綱、需求彙整、會議記錄 | `templates/interview-outline.md`、`templates/requirement-synthesis.md`、`templates/meeting-minutes.md` |

完整範例在 `templates/examples/`。

## 其他 harness

skills 以 Claude Code 用語撰寫。在 Pi 等其他 harness 執行時，先讀 `references/harness-terms.md` 做工具與路徑對照；`package.json` 是 Pi 的套件清單。`scripts/test_harness_neutral.py` 會擋下沒有對照的 Claude 專屬用語。

## 授權

MIT 授權 — Copyright (c) 2026 Kerry Huang
