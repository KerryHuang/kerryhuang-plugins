---
name: commit
description: 建立符合 Conventional Commits 規範的語義化提交訊息，支援 Git Flow + Semantic Release 工作流程。Use when creating git commits, "commit 這些變更", "幫我提交", "建立 commit", "semantic commit".
---

# 建立語義化提交

產生並建立遵循 Conventional Commits 規範的提交訊息。

## 工作流程

1. **檢查狀態** - `git status && git branch`（確認在正確分支，非 main/develop 直接提交）
2. **檢視變更** - `git diff --staged`（未 stage 則先逐檔 `git status --short` 指名 add，禁止 `git add -A`）
3. **分析並產生訊息** - 依變更內容判定 type / scope，寫成 Conventional Commits 格式
4. **使用者批准** - 提交前先出示訊息供確認
5. **建立提交** - `git commit -m "..."`

## 提交類型

### 版本號變更

| 類型 | 說明 | 版本影響 |
|------|------|----------|
| `feat` | 新功能 | MINOR |
| `fix` | Bug 修復 | PATCH |
| `perf` | 效能改進 | PATCH |
| `feat!` | 破壞性變更 | MAJOR |

### 無版本號變更

| 類型 | 說明 |
|------|------|
| `docs` | 文件變更 |
| `style` | 格式調整 |
| `refactor` | 重構 |
| `test` | 測試 |
| `build` | 建置系統 |
| `ci` | CI/CD |
| `chore` | 維護 |

## Scope 建議

Scope 依專案實際模組命名，取變更集中的區域。常見面向：

### 架構層級
`domain`, `application`, `persistence`, `presentation`, `api`, `ui`

### 基礎設施
`db`, `docker`, `ci`, `deps`, `tests`, `config`, `build`

> 沒有明確 scope 時可省略；不要硬套不存在的模組名。

## Git Flow 整合

```bash
# 功能開發
git flow feature start user-auth
git commit -m "feat(auth): implement JWT authentication"
git flow feature finish user-auth

# 發布版本
git flow release start auto
git flow release finish -n auto  # -n 跳過自動 tag
```

## 重要規則

- ✅ 使用英文撰寫提交訊息主體
- ✅ 使用 `-n` 跳過 Git Flow 自動 tag（版本號交給 Semantic Release / CI）
- ❌ 不要手動建立 Git tag
- ❌ 不要直接在 main/develop 提交
- ❌ 禁止 `git add -A` / `git add .`——逐檔指名 add，提交前複驗 staged 只含本次變更
