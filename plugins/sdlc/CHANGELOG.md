# Changelog

格式：每次改動 `skills/`、`agents/`、`references/` 時，於最上方新增版本條目並同步 bump 版號（規則見 `.claude/rules/version-consistency.md`）。

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
