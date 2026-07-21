---
name: quality-check
description: 全面程式碼品質檢查——建置驗證、測試執行、覆蓋率分析、問題優先排序。Use when validating code quality before commit or deployment, "品質檢查", "quality check", "跑測試看覆蓋率", "提交前檢查", "建置測試驗證".
---

# 品質檢查

執行全面的品質驗證並產出詳細報告。以 .NET 為例列指令，其他工具鏈比照替換。

## 工作流程

1. **還原依賴** — `dotnet restore`
2. **建置檢查** — `dotnet build -c Release --no-restore`（Release 組態）
3. **執行測試** — `dotnet test --logger:trx --results-directory TestResults`
4. **程式碼分析** — 啟用分析器並將警告視為錯誤 `dotnet build /p:RunAnalyzers=true /p:WarningsAsErrors=true`
5. **智能分析** — 複雜結果委派品質分析型 subagent 做模式識別與修復排序（見下）

## 常用指令

```bash
# 完整品質檢查
dotnet restore && dotnet build -c Release && dotnet test --logger:trx

# 帶覆蓋率
dotnet test --collect:"XPlat Code Coverage" --results-directory TestResults

# 格式檢查
dotnet format --verify-no-changes

# 套件檢查
dotnet list package --outdated
dotnet list package --vulnerable
```

## 品質標準

### 建置
- 無編譯錯誤
- 無編譯警告（警告視為錯誤）

### 測試
- 所有測試通過
- 無跳過的測試

### 覆蓋率（依層級遞減，數值可依專案調整）
- Domain: 90%+
- Application: 85%+
- Infrastructure: 75%+

## 問題優先級

| 優先級 | 類型 | 行動 |
|--------|------|------|
| 🔴 Critical | 編譯錯誤、測試失敗 | 立即修復 |
| 🟡 High | 品質警告、低覆蓋率 | 今天修復 |
| 🟠 Medium | 技術債、程式碼異味 | 本週修復 |
| 🟢 Low | 清理、格式化 | 待辦清單 |

## 智能分析（委派）

複雜問題委派品質分析型 subagent，要求它：

1. **模式識別** — 按根本原因分組相似的錯誤/警告。
2. **優先排序** — 用「影響 × 工作量」矩陣排序（對應上表優先級）。
3. **可行建議** — 每個問題類別給：檔案:行位置、根因說明、修復方案與程式碼範例、預估修復時間。
4. **修復排程** — 分「立即（接下來數小時）／短期（本週）／長期改進」。

## 報告格式

```
=== 品質檢查報告 ===

【建置狀態】
✅ 建置成功    ⚠️ 警告: 0    ❌ 錯誤: 0

【測試結果】
✅ 通過: {n}    ❌ 失敗: 0    ⏭️ 跳過: {n}
總計: {n}    成功率: {%}

【測試覆蓋率】
Domain / Application / Infrastructure：各層 % 與總體 %

【品質分數】: {0-100}

【關鍵問題】 / 【建議】 / 【下一步驟】
```

## 故障排除

```bash
# 建置失敗：清理並重建
dotnet clean && dotnet restore && dotnet build

# 測試失敗：詳細輸出
dotnet test -v detailed --logger:trx

# 依賴問題：清 NuGet 快取
dotnet nuget locals all --clear && dotnet restore --force
```

## 何時執行

- 建立提交之前
- 開 Pull Request 之前
- 完成重大重構後
- 作為 CI/CD 驗證的一部分

## 與其他 skill 銜接

- `work-on` — 實作段落完成後的品質閘門
- `review` — 審查前先跑品質檢查
- `commit` — 提交前先驗證
