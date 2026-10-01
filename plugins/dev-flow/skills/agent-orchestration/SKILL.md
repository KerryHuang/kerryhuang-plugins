---
name: agent-orchestration
description: 適用於多階段 agent chain（≥2 個 agent 接力）、需要用 output file 交棒、把多步工作流展示給使用者確認、偵測到「工作完成」需清理階段性產物、跨 agent 任務串接決策。涵蓋 chain 規範、output 路徑、清理流程、工作流呈現格式、subagent 作為 context 隔離工具的使用時機。觸發語：「召喚某 agent」「多階段流程」「派 subagent」「工作流規劃」「agent 交棒」「orchestration」。
---

# Agent Orchestration

> 多階段 agent chain 的協調規範。原則：subagent 通常不能再 spawn subagent，多階段流程靠**主對話串接** + **output file 作交棒**。

## 1. Output File Handoff 機制

當一條 chain 有多個 agent 接力時，上游 agent 把結論寫成 output file，下游 agent 讀檔取得 context，避免主對話用「口頭摘要」轉述而丟失細節。

**建議 output 路徑約定**（依專案調整根目錄）：

| Agent 類型 | Output 路徑 | 用途 |
|-----------|------------|------|
| 架構 / 技術選型 | `<workdir>/architecture/{topic}/adr-{seq}-{slug}.md` | ADR：決策、trade-off、補救路線 |
| 領域 / 業務諮詢 | `<workdir>/domain-review/{topic}/report.md` | 諮詢 / 審查報告 |
| 程式碼審查 | `<workdir>/code-review/{topic}/round-{n}.md` | 審查報告（n 為迴圈次數） |
| 除錯 | `<workdir>/debug/{topic}/report.md` | 根因診斷與修復方案 |
| 資料 / 事實探勘 | `<workdir>/data-exploration/{topic}.md`（選用） | 探勘結果 |
| 實作 / 測試 | 直接寫程式碼 / 測試檔 | 不另寫 markdown report |

### 串接規則

- **單次諮詢**：agent 報告主對話即可，不寫檔。
- **多階段 chain（≥2 agent 接力）**：上游 agent **必須**寫 output file，下游讀檔。
- **迴圈**：審查 ⇄ 開發 用 `round-{n}.md` 編號。

### 範例

```
架構決策 → 架構 agent 寫 <workdir>/architecture/feat-x/adr-001-strategy.md
       ↓ 主對話讀檔，召喚下一棒
實作     → 開發 agent 讀 ADR 實作 → 提 PR 引用 ADR
       ↓
審查     → 審查 agent 讀 ADR + code → 寫 <workdir>/code-review/feat-x/round-1.md
```

## 2. 主對話 Chain 行為規範

接到「召喚 X agent」需求時，主對話**必須**：

1. **先檢查上一棒有沒有寫 output file**（依上表路徑）。
2. **若有 output file** → 在召喚 prompt 中明確告知：
   ```
   請先讀 <workdir>/{path}/{file}.md 取得上下文，再執行 {任務}
   ```
3. **若無 output file**（單次諮詢或 chain 起點）→ 在 prompt 中直接提供必要 context。
4. **下一棒回報後** → 若後續還有 chain，提醒下一棒寫 output file。
5. **發現 agent 在報告中寫「建議召喚 X」** → 主動 follow-up 召喚（除非使用者中斷）。

**禁止**：
- 跳過 output file 直接「自己摘要傳給下一棒」（會丟失細節）。
- 連續召喚 ≥3 棒卻不檢查中間 output file（context 失準）。

## 3. Output File 階段性清理

當偵測到「**工作完成**」意圖時（任一觸發即執行清理）：

| 觸發條件 | 範例 |
|---------|------|
| 使用者明確表達結束 | 「完成了」「結束」「告一段落」「收工」「done」 |
| Commit 流程完成 | commit skill 結束後 |
| PR 建立完成 | `gh pr create` / `glab mr create` 成功後 |
| 所有任務完成 | 任務清單全 completed 且使用者沒提新需求 |

### 動作

1. **掃描**本次 chain 產生的 output files（依上表路徑）。
2. **列出找到的檔案**給使用者看（路徑 + 大小 + 類型）。
3. **分兩題詢問**：
   - **Q1（一般 output：domain-review / code-review / debug / data-exploration）**：全部刪除（推薦，階段性產物）／ 部分刪除（指定保留）／ 全部保留。
   - **Q2（ADR — `architecture/`）**：移到永久決策紀錄目錄（如 `decisions/{slug}.md`，推薦）／ 保留原處 ／ 刪除（決策已被取代）。
4. **依選擇執行**：刪除 → `rm`；移動 → `git mv`（保留歷史）；保留 → 不動。
5. **執行後**：簡短回報（X 刪除、Y 移動、Z 保留）。

**禁止**：
- 未經使用者確認自動刪除任何檔案。
- 把 ADR 視為一般 output file 預設刪除（ADR 是決策資產）。

## 4. 工作流展示規則

| 任務複雜度 | 判斷標準 | 行為 |
|-----------|---------|------|
| 單步 | 除錯、查詢、提交、單一 skill | 直接執行 |
| 多步 | 涉及 2+ 命令或 agent | 展示工作流 → 使用者確認 → 執行 |
| 全流程 | 從需求到實作 | 展示完整流程 → 逐階段確認 |

### 工作流展示格式

```
📋 工作流規劃：{任務摘要}

步驟：
1. `{tool/agent}` — {目的} {[平行]/[依賴 N]}
2. `{tool/agent}` — {目的} {[平行]/[依賴 N]}
3. ...

預估涉及：{模組/檔案範圍}
→ 確認後開始執行
```

## 5. Subagent 與 Context 衛生

> 每次召喚 subagent = **全新 context window**。subagent 除了「分工」之外，還是 **context 隔離工具**。

### 心理測試

> **「我之後還需要這些 tool output，還是只要結論？」**

| 我之後需要什麼？ | 做法 |
|---------------|------|
| 只要結論 / 分析 / 判斷 | **派 subagent**（tool output 不污染主 context） |
| 需要完整 tool output 細節（原始檔案內容、原始查詢結果） | 主對話自己做；之後若冗餘再壓縮 context |
| 不確定 | 先假設「只要結論」派 subagent；真要細節再重讀 |

### 典型 subagent delegation 場景（序列，非平行）

| 場景 | 為什麼派 subagent |
|------|-----------------|
| 讀 >5 個檔案才能回答 | 讀檔 tool output 會填滿主 context，只要結論 |
| 驗證實作是否符合規格 | 驗證過程的中間步驟不需留在主對話 |
| 寫文件 / summary | 需翻大量 git diff 但產出只是一段文字 |
| 探勘真實資料 | 查詢結果留在 subagent 的 context 即可 |

### 與平行處理的關係

- **平行處理**：獨立任務平行啟動多 agent 提速。
- **context 隔離**：即使序列任務，subagent 也用來隔離 context。

兩者互補：平行跑多 agent 仍適用 context 隔離原則，每個 subagent 只回報結論。

## 6. 與外部 plugin 的優先順序

當專案自帶 skill/rule 與外部通用 plugin 功能重疊時，**專案資源優先**（更貼合專案慣例），外部 plugin 補足專案沒有的環節。

## 7. 長流程心跳 / sub-agent 健康偵測

當 agent chain ≥ 2 stage 且預估總時長 ≥ 5 分鐘：

- 每個 stage 的 start / done / skip / fail 都主動 emit 簡短心跳給使用者（含時間戳與狀態）。
- 任何單一階段預估 >5 分鐘（大型審查 / 整合測試 / 三方比對等），中途再 emit 1-2 個 mid-stage 進度心跳。
- sub-agent 派出時設預期時長上限，超時明顯（如 1.5×）就 emit 警示。
- 連續失敗 ≥2 次走升級階梯（agent → 顧問 → 使用者），每次升級都告知使用者仍在處理。

> 目的：全自動的長流程中，人幾乎不介入，必須定時回報使用者或自我偵測 sub-agent 是否還活著，不要傻傻地空等。
