# Changelog

格式：每次改動 `skills/`、`agents/`、`references/` 時，於最上方新增版本條目並同步 bump 版號（規則見 `.claude/rules/version-consistency.md`）。

## [2.1.0] - 2026-10-22

### 新增
- `references/analysis-rigor.md`：上游分析下結論前的六條嚴謹度閘（來源查齊、深度到源頭、現況對齊、維度齊全、domain 邊界必叫顧問、證據優先）、結論分級與踩雷細則索引；`shared-preludes.md` 加一節指路，`consultant-desk.md` FRD 例外改指此檔。
- `hooks/agent-model-guard.py`（＋`hooks.json`、測試）：派通用 subagent（general-purpose／Explore／Plan／claude）沒指定 model 時補 `sonnet`；專用 agent、fork、明確指定者不動，解析失敗 fail-open。
- `domain-advisor` 新增 `mode: triage`：規格鏈開票前逐題分流暫定決策（撤題／顧問裁定／交 PO）。

### 變更
- **問題漏斗：實證 → 顧問 → 使用者**（`shared-preludes` 常駐卡與 details）：每題先用一手證據驗證問題本身，證據推翻前提就撤題；實證後仍要判斷的交 domain 顧問；兩層都解不了才問使用者，題目附「已查過什麼、顧問怎麼看」。推導來源補第 ④ 項「現行 codebase」。
- **平台／UI 慣例以現行 codebase 為準**：分頁、格式、對話框、匯出列印、錯誤與空狀態照既有先例直接定案、附檔案路徑，不提問、不記暫定。
- **規格鏈中途裁決：暫定不停下，開票前集中問**（details 新節）；`decision-record.md` 決策表加 `狀態` 欄（`定案`／`暫定`）、「暫定決策」與「引用他鏈決策」兩節，`拍板` 欄新增 `證據`。
- **互動詢問一律一次一題**：移除「同質獨立裁決批次表決」；新增第 5 條「題目自明」（自帶背景、白話先行代碼放括號、選項寫後果、一題一件事）。
- `dispatch-conventions.md`：§四翻案級斷言採信前自己 grep；§五 agent 紀律（不刪暫存、只用清單內工具、找檔先看頂層、長 python 先落檔、SQL 帶 `DB_NAME()` 與 `TOP N`）；主 session 長 python 同樣落檔。`spec-writer`／`report-writer` 加不刪暫存與無 `Edit` 的寫法。
- `skill-design.md`：平行派工第 5 件事（fork skill 前景派發）、「skill 要主動提議，不靠使用者記得時機」、「攔截／確認類 hook 除了 exit 2 任何失敗都是放行」。
- 流程型 skill 結尾補「完成後依動線用 AskUserQuestion 建議下一步」：`qa-verify`、`foxpro-analyzer`、`meeting-minutes`、`interview-prep`。
- `verify-against-source.md` 新增「缺席長得像成功」；`analysis-standards.md` 新增「集合性質不能逐列篩選」。
- 模型與上限：`spec-writer` opus→sonnet、`verifying-specs` 釘 `model: sonnet`（不隨主 session 漂移）；`qa-runner-ui` maxTurns 150→350、`manual-explorer` 150→300，`scout` 新設 100、`spec-sampler` 新設 80（依實測用量約 2 倍）。
- `verifying-specs`：修正棒逐條對 `file:line` 親手改、不派 subagent 整章重寫；單文件 `--full`／`--recheck` 連續第三輪就停。

## [2.0.0] - 2026-10-01

### BREAKING
- `specify` 拆為 `specify-backend`（BFS）與 `specify-frontend`（FFS）。
- `linear-ticket-defaults.md`、`linear-workflow.md` 移至 `skills/linear-create/references/`。

### 架構
- 主 session 統整派工、`spec-writer` agent 落檔、每棒載入 `references/shared-preludes.md`。
- 勘察產物共用 `{功能目錄}/analysis/`；依功能規模走完整鏈或 lite 鏈（`chain-profile.md`）。

### 新增
- skills：explore、interview-prep、dev-readiness、qa-verify、live-drive、operation-manual、linear-triage、linear-reply、linear-illustrate、linear-daily-report、linear-weekly-report、issue-triage、dev-feedback、meeting-minutes、sample-verify、pdf-converter、write-doc。
- agents：spec-writer、domain-advisor、scout、report-writer、spec-sampler、doc-fidelity-reviewer、browser-surveyor、qa-planner、qa-runner-ui、qa-fixture、manual-explorer、manual-writer、manual-reviewer。
- references：legacy-parity、decision-record、boundary-dimensions、verify-against-source、spec-dedup-and-budget 等。
- Pi harness 對照（`references/harness-terms.md`、`package.json`）與 `scripts/test_harness_neutral.py`。

### 變更
- Linear team／label／assignee 改由專案 `CLAUDE.md` 設定或執行時查詢，不再寫死。
- 選配整合（Linear、chrome-devtools、唯讀 DB、Graphify）不可用時降級或跳過。

> 2.0.0 之前的版本未逐版記錄。
