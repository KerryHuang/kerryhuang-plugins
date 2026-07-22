---
name: ui-ux-pro-max
description: "UI/UX 設計知識庫與智能建議。涵蓋 67 種 styles、96 組 color palettes、56 組 font pairings、98 條 UX guidelines、25 種 charts，橫跨 13 種技術棧（React、Next.js、Vue、Svelte、SwiftUI、React Native、Flutter、Tailwind、shadcn/ui）。觸發詞：UI 設計、UI/UX、版面、配置、配色、色彩、typography、字體搭配、排版、可及性、accessibility、動畫、互動、hover、陰影、漸層、風格選擇、design system；plan／build／create／design／implement／review／fix／improve／optimize／refactor UI code。適用專案：website、landing page、dashboard、admin panel、e-commerce、SaaS、portfolio、blog、mobile app、.html／.tsx／.vue／.svelte。元件：button、modal、navbar、sidebar、card、table、form、chart。風格：glassmorphism、claymorphism、minimalism、brutalism、neumorphism、bento grid、dark mode、responsive、skeuomorphism、flat design。整合 shadcn/ui MCP 進行元件搜尋與範例查詢。"
---
# UI/UX Pro Max — 設計知識庫

Web 與 mobile 應用的完整設計指南。內含 67 種 styles、96 組 color palettes、56 組 font pairings、98 條 UX guidelines、25 種 chart types，橫跨 13 種技術棧。以可搜尋的資料庫搭配優先級導向的建議規則。

## 何時套用

以下情境參照本知識庫：
- 設計新的 UI 元件或頁面
- 挑選 color palettes 與 typography
- 審查程式碼的 UX 問題
- 製作 landing page 或 dashboard
- 落實 accessibility 需求

## 規則類別（依優先級）

| 優先級 | 類別 | 影響 | Domain |
|----------|----------|--------|--------|
| 1 | Accessibility | CRITICAL | `ux` |
| 2 | Touch & Interaction | CRITICAL | `ux` |
| 3 | Performance | HIGH | `ux` |
| 4 | Layout & Responsive | HIGH | `ux` |
| 5 | Typography & Color | MEDIUM | `typography`、`color` |
| 6 | Animation | MEDIUM | `ux` |
| 7 | Style Selection | MEDIUM | `style`、`product` |
| 8 | Charts & Data | LOW | `chart` |

## 速查（Quick Reference）

### 1. Accessibility（CRITICAL）

- `color-contrast` — 正文最低 4.5:1 對比
- `focus-states` — 互動元素要有可見的 focus ring
- `alt-text` — 有意義的圖片要有描述性 alt text
- `aria-labels` — icon-only 按鈕要加 aria-label
- `keyboard-nav` — Tab 順序與視覺順序一致
- `form-labels` — 用 label 搭配 for 屬性

### 2. Touch & Interaction（CRITICAL）

- `touch-target-size` — 觸控目標最小 44x44px
- `hover-vs-tap` — 主要互動用 click／tap，不倚賴 hover
- `loading-buttons` — async 操作進行中禁用按鈕
- `error-feedback` — 錯誤訊息清楚、貼近問題發生處
- `cursor-pointer` — 可點擊元素加上 cursor-pointer

### 3. Performance（HIGH）

- `image-optimization` — 使用 WebP、srcset、lazy loading
- `reduced-motion` — 檢查 prefers-reduced-motion
- `content-jumping` — 為 async 內容預留空間，避免版面跳動

### 4. Layout & Responsive（HIGH）

- `viewport-meta` — width=device-width initial-scale=1
- `readable-font-size` — mobile 正文最小 16px
- `horizontal-scroll` — 內容須容納於 viewport 寬度內
- `z-index-management` — 定義 z-index scale（10、20、30、50）

### 5. Typography & Color（MEDIUM）

- `line-height` — 正文用 1.5–1.75
- `line-length` — 每行限制 65–75 字元
- `font-pairing` — heading／body 字型個性要匹配

### 6. Animation（MEDIUM）

- `duration-timing` — micro-interaction 用 150–300ms
- `transform-performance` — 用 transform／opacity，勿動 width／height
- `loading-states` — skeleton screen 或 spinner

### 7. Style Selection（MEDIUM）

- `style-match` — style 要匹配產品類型
- `consistency` — 全站頁面用同一套 style
- `no-emoji-icons` — 用 SVG icon，不用 emoji

### 8. Charts & Data（LOW）

- `chart-type` — chart 類型要匹配資料類型
- `color-guidance` — 使用符合 accessibility 的色盤
- `data-table` — 提供 table 替代方案以利 accessibility

## 如何使用

透過下方 CLI 工具搜尋特定 domain。

---

## 前置需求（Prerequisites）

確認是否已安裝 Python：

```bash
python3 --version || python --version
```

若未安裝，依使用者的 OS 安裝：

**macOS：**
```bash
brew install python3
```

**Ubuntu/Debian：**
```bash
sudo apt update && sudo apt install python3
```

**Windows：**
```powershell
winget install Python.Python.3.12
```

> 註：CLI 依賴本 skill 內附的 `scripts/`（search.py 等）與 `data/`（設計資料庫 CSV）。若這兩個目錄不在，CLI 無法運作——此時仍可直接參照本文件的速查、專業 UI 規則與交付前檢查表。

---

## 使用流程

當使用者提出 UI/UX 工作（design、build、create、implement、review、fix、improve）時，依此流程進行：

### Step 1：分析使用者需求

從使用者請求中萃取關鍵資訊：
- **Product type**：SaaS、e-commerce、portfolio、dashboard、landing page 等
- **Style 關鍵字**：minimal、playful、professional、elegant、dark mode 等
- **Industry**：healthcare、fintech、gaming、education 等
- **Stack**：React、Vue、Next.js，或預設 `html-tailwind`

### Step 2：產生 Design System（必做）

**一律先用 `--design-system`** 取得帶推理依據的完整建議：

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```

此指令會：
1. 平行搜尋 5 個 domain（product、style、color、landing、typography）
2. 套用 `ui-reasoning.csv` 的推理規則選出最佳匹配
3. 回傳完整 design system：pattern、style、colors、typography、effects
4. 附上要避免的 anti-patterns

**範例：**
```bash
python3 skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service" --design-system -p "Serenity Spa"
```

### Step 2b：持久化 Design System（Master + Overrides 模式）

要跨 session 保存 design system 以利階層式取用，加上 `--persist`：

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "Project Name"
```

會建立：
- `design-system/MASTER.md` — 全域 Source of Truth，含所有設計規則
- `design-system/pages/` — 頁面層級 override 的資料夾

**帶頁面層級 override：**
```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "Project Name" --page "dashboard"
```

會額外建立：
- `design-system/pages/dashboard.md` — 相對於 Master 的頁面專屬差異

**階層式取用如何運作：**
1. 建置特定頁面（例如 Checkout）時，先查 `design-system/pages/checkout.md`
2. 若該頁面檔存在，其規則**覆蓋** Master 檔
3. 若不存在，只用 `design-system/MASTER.md`

### Step 3：以細部搜尋補強（視需要）

取得 design system 後，用 domain 搜尋補充細節：

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**何時用細部搜尋：**

| 需求 | Domain | 範例 |
|------|--------|---------|
| 更多 style 選項 | `style` | `--domain style "glassmorphism dark"` |
| Chart 建議 | `chart` | `--domain chart "real-time dashboard"` |
| UX best practices | `ux` | `--domain ux "animation accessibility"` |
| 替代字型 | `typography` | `--domain typography "elegant luxury"` |
| Landing 結構 | `landing` | `--domain landing "hero social-proof"` |

### Step 4：Stack Guidelines（預設：html-tailwind）

取得實作層級的 best practices。若使用者未指定 stack，**預設用 `html-tailwind`**。

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --stack html-tailwind
```

可用 stacks：`html-tailwind`、`react`、`nextjs`、`vue`、`svelte`、`swiftui`、`react-native`、`flutter`、`shadcn`、`jetpack-compose`

---

## 搜尋參考（Search Reference）

### 可用 Domain

| Domain | 用途 | 範例關鍵字 |
|--------|---------|------------------|
| `product` | 產品類型建議 | SaaS、e-commerce、portfolio、healthcare、beauty、service |
| `style` | UI styles、colors、effects | glassmorphism、minimalism、dark mode、brutalism |
| `typography` | Font pairings、Google Fonts | elegant、playful、professional、modern |
| `color` | 依產品類型的 color palettes | saas、ecommerce、healthcare、beauty、fintech、service |
| `landing` | 頁面結構、CTA 策略 | hero、hero-centric、testimonial、pricing、social-proof |
| `chart` | Chart 類型、library 建議 | trend、comparison、timeline、funnel、pie |
| `ux` | Best practices、anti-patterns | animation、accessibility、z-index、loading |
| `react` | React／Next.js 效能 | waterfall、bundle、suspense、memo、rerender、cache |
| `web` | Web 介面準則 | aria、focus、keyboard、semantic、virtualize |
| `prompt` | AI prompts、CSS 關鍵字 | (style name) |

### 可用 Stack

| Stack | 重點 |
|-------|-------|
| `html-tailwind` | Tailwind utilities、responsive、a11y（DEFAULT） |
| `react` | State、hooks、performance、patterns |
| `nextjs` | SSR、routing、images、API routes |
| `vue` | Composition API、Pinia、Vue Router |
| `svelte` | Runes、stores、SvelteKit |
| `swiftui` | Views、State、Navigation、Animation |
| `react-native` | Components、Navigation、Lists |
| `flutter` | Widgets、State、Layout、Theming |
| `shadcn` | shadcn/ui components、theming、forms、patterns |
| `jetpack-compose` | Composables、Modifiers、State Hoisting、Recomposition |

---

## 範例流程

**使用者請求：** 「為專業護膚服務做一個 landing page」

### Step 1：分析需求
- Product type：Beauty／Spa service
- Style 關鍵字：elegant、professional、soft
- Industry：Beauty／Wellness
- Stack：html-tailwind（預設）

### Step 2：產生 Design System（必做）

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service elegant" --design-system -p "Serenity Spa"
```

**輸出：** 完整 design system，含 pattern、style、colors、typography、effects 與 anti-patterns。

### Step 3：以細部搜尋補強（視需要）

```bash
# 取得 animation 與 accessibility 的 UX 準則
python3 skills/ui-ux-pro-max/scripts/search.py "animation accessibility" --domain ux

# 視需要取得替代 typography 選項
python3 skills/ui-ux-pro-max/scripts/search.py "elegant luxury serif" --domain typography
```

### Step 4：Stack Guidelines

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "layout responsive form" --stack html-tailwind
```

**接著：** 綜合 design system 與細部搜尋結果，實作設計。

---

## 輸出格式（Output Formats）

`--design-system` 支援兩種輸出格式：

```bash
# ASCII box（預設）— 適合 terminal 顯示
python3 skills/ui-ux-pro-max/scripts/search.py "fintech crypto" --design-system

# Markdown — 適合寫進文件
python3 skills/ui-ux-pro-max/scripts/search.py "fintech crypto" --design-system -f markdown
```

---

## 取得更佳結果的訣竅

1. **關鍵字要具體** — 「healthcare SaaS dashboard」優於「app」
2. **多搜幾次** — 不同關鍵字帶出不同洞察
3. **組合 domain** — Style + Typography + Color = 完整 design system
4. **一定要查 UX** — 搜「animation」「z-index」「accessibility」找常見問題
5. **善用 stack flag** — 取得實作層級的 best practices
6. **反覆迭代** — 首次搜尋不匹配就換關鍵字

---

## 專業 UI 通用規則

以下是常被忽略、卻會讓 UI 顯得不專業的問題：

### Icons 與視覺元素

| 規則 | Do | Don't |
|------|----|----- |
| **No emoji icons** | 用 SVG icon（Heroicons、Lucide、Simple Icons） | 拿 emoji（🎨 🚀 ⚙️）當 UI icon |
| **穩定的 hover 狀態** | 用 color／opacity 過渡 | 用 scale transform 造成版面位移 |
| **正確的品牌 logo** | 從 Simple Icons 找官方 SVG | 亂猜或用錯誤的 logo 路徑 |
| **一致的 icon 尺寸** | 固定 viewBox（24x24）搭配 w-6 h-6 | 隨意混用不同 icon 尺寸 |

### 互動與游標

| 規則 | Do | Don't |
|------|----|----- |
| **Cursor pointer** | 所有可點擊／可 hover 的 card 加 `cursor-pointer` | 互動元素留預設游標 |
| **Hover feedback** | 提供視覺回饋（color、shadow、border） | 完全看不出元素可互動 |
| **平滑過渡** | 用 `transition-colors duration-200` | 瞬間切換或太慢（>500ms） |

### Light／Dark Mode

優先使用 design system 的 semantic tokens／CSS variables（如 surface、text、border、muted 等語意色），**不要 hardcode** 十六進位色碼或框架固定色階；dark mode 靠 token 自動切換，避免在樣式邏輯裡寫 dark 模式的條件分支。若專案未提供 token 系統，至少確保下列對比：

| 規則 | Do | Don't |
|------|----|----- |
| **Glass card 淺色模式** | 用 `bg-white/80` 或更高不透明度 | 用 `bg-white/10`（過度透明） |
| **淺色模式文字對比** | 正文用 `#0F172A`（slate-900） | 用 `#94A3B8`（slate-400）當正文 |
| **淺色模式 muted 文字** | 至少 `#475569`（slate-600） | 用 gray-400 或更淺 |
| **邊框可見度** | 淺色模式用 `border-gray-200` | 用 `border-white/10`（看不見） |

### Layout 與 Spacing

| 規則 | Do | Don't |
|------|----|----- |
| **Floating navbar** | 加 `top-4 left-4 right-4` 間距 | 貼死 `top-0 left-0 right-0` |
| **Content padding** | 為固定 navbar 高度預留空間 | 讓內容藏在 fixed 元素後面 |
| **一致的 max-width** | 統一用 `max-w-6xl` 或 `max-w-7xl` | 混用不同的容器寬度 |

---

## 交付前檢查表

交付 UI 程式碼前，逐項確認：

### 視覺品質
- [ ] 沒有拿 emoji 當 icon（改用 SVG）
- [ ] 所有 icon 出自同一套 icon set（Heroicons／Lucide）
- [ ] 品牌 logo 正確（已從 Simple Icons 核對）
- [ ] Hover 狀態不造成版面位移
- [ ] 直接用 theme 色（如 bg-primary），非 var() 包裝

### 互動
- [ ] 所有可點擊元素都有 `cursor-pointer`
- [ ] Hover 狀態提供清楚的視覺回饋
- [ ] 過渡平滑（150–300ms）
- [ ] 鍵盤操作有可見的 focus 狀態

### Light／Dark Mode
- [ ] 優先使用 semantic tokens／CSS variables，未 hardcode 色碼
- [ ] 淺色模式文字對比足夠（最低 4.5:1）
- [ ] Glass／透明元素在淺色模式下可見
- [ ] 邊框在兩種模式下都可見
- [ ] 交付前兩種模式都測過

### Layout
- [ ] Floating 元素與邊緣有適當間距
- [ ] 沒有內容被 fixed navbar 遮住
- [ ] 在 375px、768px、1024px、1440px 皆 responsive
- [ ] mobile 無水平捲動

### Accessibility
- [ ] 所有圖片有 alt text
- [ ] 表單 input 有 label
- [ ] 顏色不是唯一的辨識指標
- [ ] 尊重 `prefers-reduced-motion`
