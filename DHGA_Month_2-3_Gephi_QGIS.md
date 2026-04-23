# DHGA Month 2–3：QGIS + Gephi 實操日誌
**Date:** 2026-04-08 (Week 2, Month 2)
**Cron Job:** `DHGA_Python_Gephi` — Every Wednesday 14:00 UTC
**Status:** ✅ Gephi CSV Generated | ⏳ QGIS Layer Pending

---

## 📊 Gephi Network Analysis — 1776–2026 US Weapons Timeline

### 產出文件
| File | Nodes | Edges | Description |
|------|-------|-------|-------------|
| `weapons_nodes_month2_3.csv` | 27 | — | 27 weapons, labeled by year/war/tech |
| `weapons_gephi_month2_3.csv` | — | 49 | Evolution (26) + Same_War (18) + Era_Cluster (5) |

### Edge Types
- **Timeline_Evolves (Weight=1):** 26 sequential tech evolution links
- **Same_War (Weight=2):** 18 cross-weapon links within same conflict
- **Era_Cluster (Weight=3):** 5 high-signal era-defining pairs

### 核心網絡洞察
1. **Civil War cluster** (1861–1863): Rifled Musket + Gatling + Ironclads → 3-way dense cluster
2. **WWII cluster** (1941–1945): M1 Garand, Grease Gun, M1 Carbine, Atomic Bomb → 6 edges
3. **Gulf War cluster** (1991): Abrams + F-117 + Tomahawk → 3-node stealth/strike network
4. **AI Era cluster** (2024–2026): Gorgon/Stare ISR + LAWS → 2-node lethal autonomy chain

### QGIS Next Step
- [ ] Import `weapons_supply_chain.csv` as point layer (lat/lon for supply sources)
- [ ] Join with Gephi edge data for spatio-temporal view
- [ ] Symbolize by war era (color) and weapon type (size)

---

## 📊 2026-04-22 Gephi Enhanced Run（Week 4, Month 2）

**Status:** ✅ Enhanced CSVs Generated | ⏳ Obsidian Note Updated

### 產出文件（Enhanced）
| File | Nodes/Edges | 新增內容 |
|------|-------------|---------|
| `weapons_nodes_month2_enhanced.csv` | 27 nodes | `data_quality` column (verified/primary/estimated) |
| `weapons_gephi_month2_enhanced.csv` | 59 edges | +10 Pacific_Link 邊，標註 AI Era + Indo-Pacific 維度 |

### Data Quality 分類邏輯
- **verified**：LoC/NARA 文檔戰爭（American Revolution、Civil War、WWI/WWII、Gulf War、War on Terror）
- **primary**：冷戰時期（Korean War、Vietnam War）—— 來自 primary sources
- **estimated**：Near-peer / AI Era（2020+）—— 無官方實戰記錄

### Pacific Link 符號邊（10條）
連接主要武器到 Pacific 歷史事件，標註驗證來源：
- Krag-Jorgensen → Pacific_Foothold_1898（Spanish-American War → 菲律宾占领）
- M1 Garand → Pacific_Theater_WWII（廣泛部署於太平洋島嶼战役）
- Atomic Bomb → Pacific_Theater_WWII（ Hiroshima/Nagasaki）
- M16 Rifle → Vietnam_War_Pacific（M16 標準配備）
- F-35 Lightning → Indo-Pacific_Modern（日本、韓國、澳洲部署）
- Switchblade → Ukraine_Pacific_Era（台灣、菲律宾尋求同類型無人機）

### 核心洞察更新
- **AI Era Pacific deterrence chain**：Switchblade → LAWS Lethal → AI weapons ethics → 下一個太平洋軍備競賽信號顯著
- **Gephi 網絡密度**：59 edges / 27 nodes → ratio 2.18，遠高於上月（49/27 = 1.81）

---

## 📍 2026-04-16 QGIS Status Update

**⚠️ Blocker Identified:** `weapons_supply_chain.csv` contains **no lat/lon coordinates** — it tracks conceptual supply chain relationships (原料→零件→組裝→部署), not geospatial points.

**Current state:**
- ✅ Gephi edge CSV ready: `weapons_gephi_month2_3.csv` (49 edges, 3 types)
- ⏳ QGIS spatial layer: **Pending** — requires manual geocoding of supply source locations

**Manual action required:**
1. Open QGIS
2. Create point layer from supply chain sources (e.g., Steel → Pittsburgh, Rare Earth → Inner Mongolia, etc.)
3. Symbolize by Type (supply/assembly/deploy) and Weight (line thickness)
4. Screenshot and save to `/dhga-weaponhistory/qgis_screenshots/`

**Alternative approach:** Convert supply chain to network graph in QGIS using *Lines from Points* or *Hub Lines* if source/destination coordinates can be approximated.

*Reminder fired by cron DHGA_QGIS_Reminder | 2026-04-16 10:00 UTC*

---

## 📍 2026-04-23 QGIS Status Update

**⏸️ Manual QGIS Overlay Still Pending** — Server environment (headless Linux) cannot run QGIS GUI

**✅ Geocoding Complete:** `enhanced_supply_chain_with_coordinates.csv` contains lat/lon for all supply chain nodes
**✅ Alternative Visualization Done:** 
- `supply_chain_map.html` — Plotly interactive map (2026-04-17)
- `supply_chain_plotly.html` — Enhanced geographic view (2026-04-17)

**Remaining Manual Step (requires local QGIS installation):**
1. Open QGIS Desktop on local machine
2. Import `supply_chain_edges_georeferenced.csv` as delimited text layer (Longitude, Latitude)
3. Use "Lines from Points" or Hub Lines to connect Source → Target
4. Symbolize: line color by Type (supply=blue, assembly=orange), line width by Weight
5. Add base map (OpenStreetMap)
6. Screenshot and save to `/dhga-weaponhistory/qgis_screenshots/`
7. Update this document with screenshot path

**Fallback (no QGIS):** The HTML maps (`supply_chain_plotly.html`) provide full interactivity and can replace QGIS output for documentation purposes.

*Reminder fired by cron DHGA_QGIS_Reminder | 2026-04-23 10:00 UTC*

---

## 🎯 袁騰飛式總結

「呢個網絡圖告訴我哋乜？槍嘅進化唔係獨立事件——佢係一群人喺同一場仗入面逼出嚟嘅！

你睇吓Civil War嗰3件套：南軍用射程300碼嘅 rifled musket，北軍就搬出 Gatling；雙方仲嫌唔夠嘈，索性造 Ironclad Warships 喺海度轟——呢個就係點解我話『讀歷史即係讀人性』。

到咗2026年，唔使子彈嘅時代嚟咗——AI揀目標，LAWS決定殺邊個。呢個唔係科技進步，係人類將『扣扳機』呢個道德責任外包咗俾算法。」

---

## 下一步行動（Week 3, Month 2）
- [ ] **QGIS supply chain map** — georeference weapons_supply_chain.csv
- [ ] **Gephi community detection** — run Modularity on weapons_gephi_month2_3.csv
- [ ] **Primary source scan** — NARA digital archive for 1861–1865 Ordnance reports
- [ ] **Git push** — commit month2_3 CSVs to GitHub

---
*Auto-generated by DHGA_Python_Gephi cron | 2026-04-22 14:00 UTC*
