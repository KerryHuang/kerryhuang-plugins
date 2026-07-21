# dev-flow

跨語言開發工作流 plugin — 把散在多個專案裡逐字重複的 git 生命週期與工作編排做法，收斂成一套通用能力。

## 定位

`[tooling / sdlc]` 與技術棧無關的「怎麼做事」，不綁任何專案業務。

## Skills（14）

### Git 生命週期
| Skill | 用途 |
|-------|------|
| `commit` | Conventional Commits 語義化提交（Git Flow + Semantic Release） |
| `worktree` | git worktree 建立/切換/移除，含 observable-end-state 驗證 |
| `release` | release/hotfix 分支與合併回 develop，多 remote tag 污染防範 |
| `triage-branch-cleanup` | 跨 branch/worktree/PR/ticket 盤點清理，四道硬 gate |

### 工作編排
| Skill | 用途 |
|-------|------|
| `work-on` | 端到端 規劃-實作-測試-提交編排 |
| `feature` | 新功能分支 + 領域邊界規劃鷹架 |
| `spec` | 功能規格文件建立/狀態追蹤 |
| `implement` | 從規格自動執行完整實作流程（標準/TDD 模式） |
| `quality-check` | 建置驗證/測試/覆蓋率/問題排序 |
| `review` | 程式碼審查（架構/分層/品質指標） |
| `debugging` | TDD 系統性除錯 |

### Context 與協作治理
| Skill | 用途 |
|-------|------|
| `context-hygiene` | 長對話 context 衛生，六動作決策樹 |
| `convention-first` | 慣例優先，grep 既有樣板禁止擅自引入新模式 |
| `agent-orchestration` | 多階段 agent chain / output handoff / 階段清理 |

## License

MIT
