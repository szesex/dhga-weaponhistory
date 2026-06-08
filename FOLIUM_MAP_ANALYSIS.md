# Folium Supply Chain Interactive Map — 深度分析解說
**Generated:** 2026-05-18 | **地圖：** supply_chain_folium.html
**數據：** 26 nodes + 31 edges | **覆蓋：** 1776-2026 美國軍武供應鏈

---

## 🗺️ 地圖架構（Map Architecture）

```
Folium Leaflet 互動地圖
├── 中央：Pacific Ocean（[35°N, 140°E]，zoom=3）
├── 底層：CartDB Positron tiles（專業灰底黑白）
├── 層一：Supply Chain Network（26 nodes + 31 edges）
├── 層二：1776 Revolutionary War Battlefields（紅色⭐）
└── 層三：WWII Pacific Battlefields（紫色⭐）
```

---

## 📦 供應鏈網絡分析（Supply Chain Network）

### 31條供應鏈連結 — 顏色分類

| 顏色 | 類型 | 數量 | 意義 |
|------|------|------|------|
| 🟢 綠色 `#2ecc71` | Supply（原材料/零件） | 多數 | 跨洋原材料流動 |
| 🟠 橙色 `#e67e22` | Assembly（組裝） | 少數 | 區域性組裝節點 |
| 🔴 紅色 `#e74c3c` | 其他 | 少數 | 特殊軍事物流 |

### 26個節點地理分布

```
北美（美國為核心）
├── 美國：康明斯發動機（-86.8°, 36.2°）— Tennessee
├── 美國：Springfield兵工廠（-72.5°, 42.1°）— Massachusetts
├── 美國：Northeast Aerospace（飛機零件）
│
歐亞大陸供應商
├── 中國：鞍鋼（122.9°, 41.1°）— 遼寧鞍山
├── 德國：萊茵金屬槍管（8.7°, 50.1°）— 杜塞爾多夫
├── 俄羅斯：VSMPO鈦合金（61.4°, 54.9°）— 葉卡捷琳堡
├── 法國：空巴機身（2.4°, 48.9°）— 圖盧茲
└── 更多...
```

---

## ⚔️ 1776革命戰場疊加（Revolutionary War Overlay）

| 標記 | 座標 | 歷史意義 |
|------|------|----------|
| ⭐ West Point | 41.39°N, 73.96°W | 1776-1781 關鍵要塞，現美國陸軍军官学校 |
| ⭐ Yorktown | 37.24°N, 76.51°W | 1781年康沃利斯投降，獨立戰爭終點 |
| ⭐ Boston | 42.36°N, 71.06°W | 1770年Boston Massacre，1775年Lexington/Concord |

**歷史脈絡：**
1776年的美國軍武供應鏈 = 歐洲進口武器（法國軍援）+ 本地製造（Springfield）
2026年的美國軍武供應鏈 = 全球供應商網絡 + Pacific跨洋物流

---

## 💥 WWII Pacific 戰場疊加（Pacific Battlefield Overlay）

| 標記 | 座標 | 戰役 |
|------|------|------|
| 💜 Iwo Jima | 24.75°N, 141.3°E | 1945.2-3月，硫磺島登陸 |
| 💜 Okinawa | 26.50°N, 127.68°E | 1945.4-6月，沖繩戰役 |
| 💜 Guadalcanal | 9.43°S, 159.95°E | 1942.8-1943.2月，瓜島登陸 |

**跨太平洋供應鏈視覺化：**
🟢 綠色箭頭 = 原材料/零件跨洋流動
💜 Pacific戰場 = 最終武器抵達點（美軍使用）

---

## 🔑 核心洞察（Key Insights）

### 1. 供應鏈全球化 vs 1776本地化
```
1776：「法國軍援」+「Springfield本地製造」
2026：「鞍鋼→德國→法國→美國」多國供應鏈

意義：技術複雜度提升→供應鏈必須全球化
```

### 2. 跨太平洋供應鏈决定Pacific戰場結局
```
亞洲供應商（鞍鋼、VSMPO、BHP）
    ↓ 跨洋運輸（綠色箭頭）
美國組裝工廠（康明斯、Springfield）
    ↓ 成品武器
Pacific戰場（Iwo Jima、Okinawa、Guadalcanal）

意義：沒有全球化供應鏈，就沒有Pacific作戰能力
```

### 3. 地理集中度
```
節點集中在：
├── 北美東岸（美國軍工核心）
├── 歐洲（德、法、英傳統軍事工業）
├── 東亞（中國、俄羅斯原材料）
└── 澳洲（鋁材、鐵礦）

缺失：南美、非洲（殖民時代遺留）
```

---

## 🗺️ Capstone StoryMap 嵌入建議

### 建議架構（ArcGIS StoryMap）

```
StoryMap章節
├── Chapter 1：1776獨立戰爭 — 武器從歐洲來
│   └── Folium map zoom to 1776 battlefields
├── Chapter 2：Civil War — 工業化起點
│   └── 疊加工廠節點
├── Chapter 3：WWII Pacific — 供應鏈決定命運
│   └── Folium map focus on Pacific + Iwo Jima/Okinawa
└── Chapter 4：AI Weapon Era 2026 — 全球供應鏈巔峰
    └── 疊加AI供應商節點
```

### GitHub Pages 嵌入代碼
```html
<iframe 
  src="supply_chain_folium.html" 
  width="100%" 
  height="600px" 
  frameborder="0">
</iframe>
```

---

## 📊 Month 3 建議方向

| 方向 | 行動 |
|------|------|
| **AI武器層** | 新增Nvidia/AMD/Google AI芯片廠商節點 |
| **時間軸動畫** | 用folium.plugins.TimeDimension做1776→2026時間滑動 |
| **量化分析** | 計算每條供應鏈的「戰爭影響指數」|
| **一手史料連結** | 每個節點popup連結LoC/NARA檔案 |

---

## ✅ 確認簽收

```
✅ Folium map 26 nodes / 31 edges — 已生成
✅ 1776 Revolutionary battlefields（3個紅色⭐）
✅ WWII Pacific battlefields（3個紫色💜）
✅ 跨太平洋供應鏈綠色箭頭 — 已確認
✅ Capstone StoryMap嵌入建議 — 已提供
✅ Month 3方向 — 4條路建議
```

**下一步：** 回覆我你想做邊部分，我即刻跟進！