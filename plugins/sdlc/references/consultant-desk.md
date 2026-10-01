# 顧問桌（唯一定義處）

> `domain-advisor` 的觸發時機、編制、流程。
> `explore` / `requirement` / `system-analysis` 直接引用本檔；其他 skill 經 `shared-preludes.md` 間接適用。一律引用本檔，不各自定義。

## 核心規則：一條規格鏈只開一次顧問桌

同一功能的 FRD → SAD → BFS → FFS 是**同一批 domain 問題**的四種寫法。
顧問在 FRD 階段答過的邊界，到 SAD 階段不會有新答案——**重開一次桌，只是把同樣的結論再聽一遍**。

| 階段 | 預設 | 說明 |
|------|------|------|
| `requirement`（FRD） | **不開**（除非命中下方「FRD 例外」） | 此時只有需求描述，顧問缺乏可審的設計，產出多為泛論 |
| `system-analysis`（SAD） | **開（主場）** | Step 3 已完成 codebase/DB 勘察、Step 4-8 已有三流與方案，證據最足、問題最具體 |
| `specify-frontend`（FFS） | 不派 domain 顧問 | UI 動線問題，非 domain 邊界 |
| `dev-readiness` | 不派；domain 疑點併入 SAD 階段既有結論 | 該階段是驗「規格有無落實」，不是重新做 domain 判斷 |

**FRD 例外**（命中任一才在 requirement 階段開桌，且開了就在 FRD 註記，SAD 階段改用「差異複審」）：

- 全新業務概念，既有系統與既有 docs 皆無對應；
- 需求本身的**業務邊界未定**（做不做得到、算不算同一件事），不先釐清就寫不出 US；
- 涉及聚合根／狀態機的**歸屬爭議**（這張單據到底屬於誰、誰能改）。

> 這條例外對應「有 domain 邊界必叫顧問」的嚴謹度要求——**鏈上叫過一次即滿足**，
> 不要求每個階段各叫一次。

## 觸發式單點諮詢（分析過程中就地介入）

顧問桌是**階段末審查**（草稿完成後整份審）。但有些問題等到階段末才問就太晚了——
方向從第 4 步就歪了，第 8 步整份審只會告訴你「要重做」。

因此在 `system-analysis` **Step 4~6 分析過程中**，一旦命中下列訊號，
**當場派一次單點諮詢**（`domain-advisor`，只問命中的那一個點），不等 Step 8.3。

| 訊號 | 為什麼不能等 |
|------|------------|
| 出現**狀態流轉**（單據／訂單／申請的生命週期） | 狀態機定義錯，後面的三流分析、VR、並發處理全部要重來 |
| **聚合根歸屬**不明（這張單據屬於誰、誰能改、跟誰一起異動） | 邊界切錯會讓 API 粒度與交易範圍整組錯位 |
| **客戶變體**（同功能各客戶行為不同） | 沒先確認變體維度，方案會建立在「只有一種行為」的假設上 |
| **產品邊界**（多產品線或多種客群共用同一系統／資料庫） | 判錯會讓整份規格對錯客群 |

**做法**（單點、便宜、不打斷主線）：

```
subagent_type: "sdlc:domain-advisor"
prompt: |
  mode: review
  scope: single-point            # 只回答這一個問題，不做整體審查
  question: {命中的具體問題，含當下已知證據}
  evidence_bundle: {analysis/db-analysis.yml 與 reuse-scan.yml 的相關片段}
```

結論即時併入當下的分析步驟，並**追加寫入** `analysis/consultant-notes.md`。

> **與 Step 8.3 的關係**：觸發式諮詢已解決的點，Step 8.3 整份審時**不重問**——
> 把已解結論一併給顧問，要求它只審「尚未觸及的面向」。
> 全部 domain 面向都已在過程中單點問過時，Step 8.3 可降為快速複核。

## 編制：單顧問

只派 `domain-advisor`，以 `AskUserQuestion` 讓使用者選，**推薦選項置首**：
`domain-advisor 單顧問（推薦）` / `跳過`。

## 流程

### 單顧問（1 個 agent 回合）

```
subagent_type: "sdlc:domain-advisor"
prompt: |
  mode: review
  context: {該階段成果摘要——SAD 為工作流/資料流摘要 + 推薦方案 + _sad-draft.md 路徑}
  evidence_bundle: {既有勘察結果；SAD 階段直接用 Step 3 成果與 analysis/*.yml，不重派 scout}
```

### scout 派發

只在**沒有既有勘察結果**時派 `sdlc:scout`（典型為 requirement 階段命中 FRD 例外）。
SAD 階段一律不派——Step 3 與 `analysis/db-analysis.yml`、`analysis/reuse-scan.yml` 已是 evidence_bundle。

## 產出整合

| 顧問輸出 | 落點 |
|---------|------|
| 兩方共識的缺口／L3 差距 | 補進當階段草稿的對應段落 |
| 仍需釐清 / 主線無法裁決的衝突 | 併入該 skill 的確認門或疑問點總清查，依 `shared-preludes.md`「同質獨立裁決可批次」一次問完 |
| Domain 重大風險 | 確認門明確告知，建議先解決 |

顧問桌成果**必須落檔**至 `analysis/consultant-notes.md`（依 `shared-preludes.md` Step 0.8）：
諮詢日期、編制、逐項結論與證據、未解爭點、已裁決項與理由。
同時在該階段正式文件記一行「已諮詢 {顧問}／日期／結論見 analysis/consultant-notes.md」。

下游 skill **先讀這份檔**：已有結論的問題不重問顧問、不重問使用者；
只有落檔內容未涵蓋的新問題才單獨補派，補完的結論**追加寫回同一份檔**。
