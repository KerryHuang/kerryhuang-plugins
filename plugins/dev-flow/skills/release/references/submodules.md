# 子模組處理

子模組有改動時，**必須先 commit 子模組、再 commit 主 repo**：

```bash
# Step 1：先 commit 並 push 子模組
cd <submodule-path>
git add -u && git commit -m "fix(scope): 修復描述"
git push origin <branch>

# Step 2：回主 repo，更新 submodule ref
cd "$(git rev-parse --show-toplevel)"
git add <submodule-path>          # 逐檔指名，勿 git add -A
git commit -m "chore: 更新 <submodule> submodule ref"
```
