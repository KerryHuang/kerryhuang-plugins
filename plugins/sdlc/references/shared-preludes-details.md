# Shared Preludes — 細節與實證

> `shared-preludes.md` 是每棒都載的常駐卡，只留要點；本檔放案例、做法細節與實證。
> **命中才讀**：只讀與當下情境同名的節，不整檔載入。

## 核心原則：先推導，再詢問

一條規格鏈的耗時主要花在**等人回答**。主鏈九個 skill 合計五十餘處 `AskUserQuestion`，
大半有可推導的答案。

| # | 來源 | 可推導什麼 |
|---|------|-----------|
| 1 | 同族既有產出（同型功能的票／規格／頁面） | team／label／priority／estimate／due、命名慣例、章節結構、狀態流轉 |
| 2 | 專案慣例（`CLAUDE.md`、`.claude/rules/`、功能清單、既有路由表） | 指派對象、模組歸屬、代號與 route 格式、分支與 commit 規則 |
| 3 | 上游文件（FRD／SAD／`analysis/*.yml`／原型） | 範圍、欄位、開發範圍、畫面數、是否涉權限 |

只有三種情況才發問：(a) 不同答案導致實質不同的工作（lite／standard、方案 A／B）；
(b) 業務裁決（欄寬、撞名復活或建新列、範圍納不納某畫面）；(c) 不可逆或高影響（補主鍵、刪 View、force push、跨客戶批次異動）。

> 實證：`linear-create` 規定問九輪，實際只問一輪——先查同族功能既有票，labels、priority、estimate、due、命名全部推導得到，省八輪往返、品質未降。

自我檢查：這題我查過同族既有產出了嗎？查得到，為什麼還在問？

## 互動詢問規範

1. 必用 `AskUserQuestion`，不可用純文字選單模擬。例外：自由文字輸入（路徑、貼入內容、憑證）。
2. 每題附建議：推薦選項置首標「（推薦）」，一行理由寫進 description；預設值類標「（預設）」置首（UI 預選第一個）。
3. 有相依性逐題問。**同質獨立裁決可批次**——三條同時滿足：彼此獨立、每項附具體建議、同一類決策。
   批次做法：先以文字單獨收尾一回合列全部項目（編號、問題、建議、落點），明說「未回覆者視同採納」；
   下一回合單一 `AskUserQuestion`（`全部採納建議（推薦）`／`我要指定調整項目`／`逐項討論`）。
   判斷分界：**選項相依→逐題；只是量多→批次**。把獨立項拆成 15 個往返是流程延誤最大單一來源。
4. 回合可見性：長內容必須以文字收尾單獨結束一回合，下一回合才進確認閘道——同回合「先印再問」使用者看不到內容。

## 核心原則：權威來源優先序

| 層級 | 什麼算這一層 | 可以拿它決定什麼 |
|------|------------|----------------|
| ① 權威 | `templates/`、`references/` 的格式定義；一手證據（舊系統原始碼、DB 實撈、封包） | 格式、結構、結論 |
| ② 參數 | 既有同類產出（前一張票、前一份規格、前一個原型） | 只有在地化參數 |
| ③ 線索 | `analysis/*.yml`、docs 既有規格、他人結論 | 指出要去查哪裡，不是答案 |

> 三次實證（同一條鏈）：原型照自己前一版改而沒讀公版→版型錯三輪；
> BFS 照抄 `reuse-scan.yml`「後端無授權層」→結論是錯的（機制在 handler 層），
> 四份文件宣稱一件做不到的事；開票照抄兩天前的同族票→缺模組行、標題重複被完整複製。
> 共同點不是不知道規則，是**手邊有個看起來很像的東西所以沒去看規則**。

## 核心原則：決策回寫的掃描義務

回寫前列全部落點：① 四份規格（範圍敘述、編號表、SPEC-INDEX、CHANGELOG）② `analysis/*.yml` ③ 上游既定敘述
（被推翻的結論常同時在 FRD §1 背景與 SAD §2 快照）。逐項掃過再動手。

| # | 要求 | 不做的後果 |
|---|------|-----------|
| 1 | 契約異動先完整枚舉現行契約再寫差異 | 「全面更名」被寫成「四處微調」，下游整份對不上 |
| 2 | `analysis/*.yml` 與規格同批更新 | 機讀檔過期比缺失更糟，下游照它走回舊結論 |
| 3 | 以語意單位全檔 grep，不用行號清單 | 同一敘述換句話說就掃不到 |
| 4 | **取代不追加**：被取代的舊敘述必刪；回寫後正文淨增 >10% 在 `decisions.md` 記一列理由 | 每輪回寫只加不減，文件體積在鏈上單向成長 |

> 實證：dev-readiness 五項回寫後 `verifying-specs` 抓 5 項 CRITICAL，4 項同一根因——回寫沒掃乾淨。

> 這與 `dev-readiness` 的「回寫前先重讀該檔」是兩件事：那條防覆蓋並行修改，本條防漏落點。

## Step 0.3: Plugin 版本對版

執行中的 skill 內容來自快取，不會因 repo 更新自動生效；落差常在鏈**進行中**發生。
鏈起頭與每個硬性停點（SAD→BFS、dev-readiness→verifying-specs、verifying-specs→linear-create）各對一次。
比對對象為 marketplace（`kerryhuang-plugins`）上的最新版本；查不到則略過。

> 實證：多次因 plugin 版本落差，下游依舊版規範產出而需整份重寫；票面新規範已落地、執行時仍跑舊版。

## 核心原則：技術中立

1. 規格描述做什麼、輸入輸出、業務規則，不規範 framework／library／ORM／演算法／設計模式。
2. 選型由 RD／PG 決定；SAD 技術建議僅為設計階段參考。
3. 不得不出現技術片段時加註：`> 💡 實作方式以 RD/PG 最終決定為準，本處僅為設計階段參考`。
4. 完工回寫：PR 合併後依實作修訂，changelog 註「v{x.y} 完工回寫：實作對齊」；`decisions.md` 每筆 TD 的「待實作定案」改成實際做法。
5. **手段層同樣不定案**：快取、鎖、佇列、儲存位置、併發原語、重試與補償做法、索引策略——寫 TD（約束＋現況＋陷阱），分界線是「會不會被外面看見」：回應碼、降級或停用、資料語意、Migration 先後這些是契約或風險，SA／PO 定；怎麼做到，Dev 定。

## Step 0.5: Docs 同步

docs 與程式碼同 repo 時略過。docs 在獨立 repo 時，開工前先 pull 一次；Session 級快取：同一 session 已有任一 sdlc skill 跑過→一行帶過略過。
例外必重做：使用者明說 docs 有外部更新、本 session 搬過檔、本 session 已對 docs commit/push。

## Step 0.7: Graphify 查詢（選配）

依 `graphify-integration.md` Query 區塊。同功能同 session 只查一次；切換功能才重查。

## Step 0.8: 分析落檔與共用

| 產物 | 路徑 | 首個產出者 | 內容 |
|------|------|-----------|------|
| DB 結構事實 | `analysis/db-analysis.yml` | `system-analysis`（lite 鏈為 `specify-backend`） | 欄位、型別、長度、可空、約束、FK、狀態欄語意、抽樣。**首段 `_index:` 列 tables 清單** |
| 既有實作盤點 | `analysis/reuse-scan.yml` | `system-analysis` | 路由清單、Handler／Entity／Repository 對照、共用 API、跨模組引用點 |
| 現有畫面勘察 | `analysis/ui-survey.md` | 最先做 UI 分析者 | URL、截圖、DOM 欄位清單、操作按鈕、攔截端點、操作記錄 |
| 顧問桌結論 | `analysis/consultant-notes.md` | 開桌的 skill | 日期、編制、逐項結論與證據、未解爭點 |
| 功能上下文 | `analysis/_context.yml` | 鏈上第一棒 | 功能名、模組、目錄、各文件路徑、票號、`chain_profile`、`chain_origin`（`foxpro`＝由 `foxpro-analyzer` 寫入的舊系統移植鏈）。**≤5KB 純指標，禁放分析內容**（膨脹到 19KB 被 5 棒重複讀） |
| 決策 | `decisions.md` | 鏈上第一個拍板者 | 見 `decision-record.md` |

讀寫協定：先讀對應檔命中即用；每筆記 `source`／`scanned_at`；缺項才補查並追加回同一檔；
`scanned_at` 後有 migration／codebase／畫面改版→重查受影響項；這些是中間產物，結論要進規格仍依 owner 矩陣。
`db-analysis.yml` 下游用 `grep -n '^  {TABLE}:'` 定位只讀該表段，不整檔讀（30KB 以上的檔被 4 棒各讀一次＝120KB 重複）。

否定結論必標證據強度：

| 標記 | 意義 | 下游可以怎麼用 |
|------|------|--------------|
| `confirmed` | 窮舉過所有可能落點後確認不存在 | 可直接當前提 |
| `not_found_by` | 只掃過特定範圍，須寫明掃了什麼 | 只能當線索，下游要補掃 |

```yaml
權限機制:
  結論: 無授權層
  證據強度: not_found_by
  掃描範圍: "controller attribute（grep [Authorize]）"
  未掃範圍: "handler 內呼叫的服務、middleware、pipeline behavior"
```

> 「掃過沒找到」與「確認不存在」差一個量詞，下游成本差一整條鏈（曾四份文件一起宣稱一件做不到的事）。

## 顧問桌

派發 `domain-advisor` 的時機、編制與流程唯一定義在 `consultant-desk.md`；
`requirement`／`system-analysis`／`dev-readiness`／`specify-frontend` 一律引用，不各自定義。

## PDF 轉檔通則

任何 PDF→Word／Excel 一律 `sdlc:pdf-converter`，不得土法手轉。產出 .docx／.xlsx 放該功能 docs 目錄
（與 FRD 同目錄）並隨 docs 版控；來源 PDF 一併複製；中間產物放 `.tmp/pdf-converter/`。
