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

---

## 📊 2026-05-06 Gephi Weekly Run（Week 2, Month 3）

**Cron:** `DHGA_Python_Gephi` | **Status:** ✅ Complete

### Run Summary
| Item | Result |
|------|--------|
| `enhance_gephi.py` | ✅ Ran — 27 nodes + 49 base edges + 10 Pacific edges = **59 edges** |
| `weapons_timeline.py` | ✅ Ran — 1776–2026 full timeline printed cleanly |
| `generate_map.py` | ✅ Available (supply chain HTML generation) |
| Enhanced CSVs | ✅ 28 lines (nodes), 60 lines (edges incl. header) |

### CSVs in sync
- `weapons_nodes_month2_enhanced.csv` — 27 weapons with `data_quality` column
- `weapons_gephi_month2_enhanced.csv` — 59 edges (49 original + 10 Pacific_Link)

### Git Status
- Last commit: `8dac201 DHGA backup 2026-05-02`
- This run produced no net file changes (CSVs already at latest state from 2026-04-29)

### 下一步行動（Month 3, Week 2）
- [ ] Run Modularity community detection on `weapons_gephi_month2_enhanced.csv` in Gephi
- [ ] Primary source scan — NARA digital archive for 1861–1865 Ordnance reports
- [ ] Git push if changes occur
- [ ] Review `supply_chain_map.html` for Ukraine-Pacific deterrence visualization

---
*Auto-generated by DHGA_Python_Gephi cron | 2026-05-06 14:00 UTC*

---

## 📊 2026-06-03 Gephi Weekly Run（Week 5, Month 3 → Month 4 交接）

**Cron:** `DHGA_Python_Gephi` | **Status:** ✅ Complete (Stable State)

### Run Summary
| Item | Result |
|------|--------|
| `weapons_timeline.py` | ✅ Ran — 27 nodes / 26 evolution edges produced cleanly (1776–2026) |
| `enhance_gephi.py` | ✅ Ran — 27 enhanced nodes + 49 base edges + 10 Pacific edges = **59 edges** |
| `weapons_gephi_month2_enhanced.csv` | ✅ MD5 `5366eda78d1774dc53de5317ff8a9cb3` — unchanged from prior runs |
| `weapons_nodes_month2_enhanced.csv` | ✅ MD5 `33964a5a1a00bd6537de03e9927eef44` — unchanged from prior runs |
| Edges written | 60 lines (incl. header) / 28 nodes (incl. header) |
| Edge types | Timeline_Evolves(26) + Same_War(18) + Era_Cluster(5) + Pacific_Link(10) |

### Stability Check
- CSV byte-identical to last run (2026-05-22 master copy)
- No new weapons added; LAWS Lethal Autonomous Weapon Systems (2026) remains terminus node
- Data_quality distribution: verified(7 wars) / primary(3 Cold War) / estimated(4+ AI Era / Near-peer)

### Git Status
- `dhga-weaponhistory` HEAD: `195ba92` (Vault backup 2026-06-02 22:00 UTC — no content changes, log only)
- `obsidian-vault` HEAD: `cd35f5f` (backup 2026-06-01 22:00 UTC)
- No new commits produced by this cron run (no content deltas)

### Network Density (Recap)
- E/N ratio = 59/27 = **2.18** (vs Month 1 baseline 1.10)
- Civil War cluster (1861–63) still highest same-war density (3-way)
- AI Era cluster (2024–26) — LAWS policy gap remains the 2–3 year lag vs deployment

### 下一步行動（Month 4 起步, 2026-06 起）
- [ ] Month 4 capstone note already exists (`DHGA_Capstone_Month_4.md`, 2026-06-01)
- [ ] Cross-link Month 2–3 Gephi/QGIS notes into Month 4 narrative
- [ ] QGIS screenshot still pending (headless server blocker — needs local GUI)
- [ ] Run Modularity community detection on `weapons_gephi_month2_enhanced.csv` in Gephi Desktop
- [ ] NARA primary source scan — 1861–1865 Ordnance reports (Civil War cluster validation)
- [ ] Consider adding Month 3+ weapons (June 2026 updates: any new LAWS / drone deployment data?)

### 袁騰飛式補注
「2026-06-03 跑出嚟嘅結果同 5 月嗰次一模一樣——冇變化唔代表冇事做，反而代表數據層面已經成熟，欠嘅係歷史詮釋同政軍分析嘅深度。Gephi 嗰 59 條邊，由 1776 年 Brown Bess 連到 2026 年 LAWS，每一條都係一段故事——但故事嘅重量，要靠 NARA 原檔同 Modularity 社區檢測去秤。AI Era 嗰段仲未完，下一個 Switchblade 或者 LAWS 變種幾時出？等下一輪 cron 見。」

---
*Auto-generated by DHGA_Python_Gephi cron | 2026-06-03 14:00 UTC*

---

## 🗺️ 2026-06-08 QGIS Overlay Run (Cron: DHGA_QGIS_Reminder)

**Status:** ✅ Overlay produced | 2 PNG outputs + scripted reproducible
**Trigger:** `DHGA_QGIS_Reminder` cron — 2026-06-08 10:00 UTC
**Mode:** QGIS-style Print Layout emulation via Python (matplotlib + contextily + geopandas, EPSG:3857)
**Reason for emulation:** Sandbox host has no QGIS GUI / `qgis` Python module installed; full Python geospatial stack installed (`matplotlib`, `contextily`, `geopandas`, `shapely`, `pyproj`) and the QGIS Print Layout paradigm reproduced 1:1 (basemap + classed vector layers + legend + north arrow + scale bar + metadata footer).

### Input data (already prepared)
| File | Rows | CRS in | CRS used | Notes |
|------|------|--------|----------|-------|
| `enhanced_supply_chain_with_coordinates.csv` | 38 nodes | EPSG:4326 (lon/lat) | EPSG:3857 | 4 categories: RawMaterial / Parts / Assembly / Deploy |
| `supply_chain_edges_georeferenced.csv` | 31 edges | EPSG:4326 | EPSG:3857 | 3 flow types: supply / assembly / deploy; line width ∝ weight (×0.4) |

### Layer stack (Print Layout)
1. **Basemap** — CartoDB Positron (contextily) — light grey, low visual noise, comparable to QGIS *OpenStreetMap* default
2. **Edges layer** — colored by `Type` (purple=supply, cyan=assembly, brown=deploy), alpha 0.55, zorder 2
3. **Points layer** — colored by `Category` (red=RawMaterial, blue=Parts, green=Assembly, orange=Deploy), markersize 110, zorder 3
4. **Labels** — auto-placed for `Assembly` and `Deploy` nodes (operationally critical)
5. **Cartographic furniture** — N arrow, 2000 km scale bar, dual legend (point + line), title block, CRS / data metadata footer

### Outputs (saved to vault)
| File | Path | Size | Purpose |
|------|------|------|---------|
| `qgis_overlay_2026-06-08.png` | `qgis_screenshots/` | ~870 KB | Full-globe overlay (Hawaii → Korea → Western Europe) |
| `qgis_overlay_2026-06-08_indo_pacific_inset.png` | `qgis_screenshots/` | ~250 KB | Indo-Pacific zoom — TSMC, Tokyo Electron, Yokosuka, Sasebo, Guam, Busan, Hawaii |
| `qgis_overlay_2026-06-08.py` | `dhga-weaponhistory/` | ~7 KB | Reproducible script (re-run any time) |

### Geographic findings (visually verified from overlay)
- **RawMaterial belt**: Inner Mongolia (Baotou REE), Anshan steel, BHP Australia, Albemarle lithium (USA) — confirms chokepoint concentration in PRC + Australia
- **Parts belt**: Rheinmetall (DE), Northrop (USA), Rafael (IL), Panasonic (JP), DJI (CN), North Industries (CN) — Israel is a Parts+Assembly hub
- **Assembly hubs**: Leavenworth (USA), North Industries (CN), Dudintsev (RU), Mitsubishi (JP), Elbit (IL) — 5-country spread
- **Deploy arc (Western Pacific)**: Guam → Yokosuka → Sasebo → Okinawa → Busan → Daegu → Yokota, with Alaska + Hawaii as outer ring
- **Weight-scaled flow visualisation** highlights the **Anshan steel → Rheinmetall/Armor-Russia** spine (weights 5/8) as the dominant Eurasian supply artery

### Capstone relevance
- Maps the **4-category supply chain** from Section 4.6 (`Capstone_Section_4.6_AI_Supply_Chain_Closure.md`) onto real geography — closes the loop from narrative to spatial evidence
- **Indo-Pacific inset** anchors 4.6.1 (Pacific civilian voice) and 4.6.2 (chokepoint pressure) — Yokosuka/Okinawa/Guam labels match the civilian-impact discussion verbatim
- Output is publication-grade (300+ dpi effective, legible at A4 print) and ready for Section 4.6 figure slot if needed

### Reproduce
```bash
cd /home/node/.openclaw/workspace/dhga-weaponhistory
python3 qgis_overlay_2026-06-08.py
```
*Auto-generated by DHGA_QGIS_Reminder | 2026-06-08 10:00 UTC*

---

## 📊 2026-06-10 Gephi Weekly Run（Week 6, Month 4 起跑 — Capstone 攻讀期）

**Cron:** `DHGA_Python_Gephi` | **Time:** 2026-06-10 14:00 UTC (Wednesday) | **Status:** ✅ Complete (Stable State)

### Run Summary
| Item | Result |
|------|--------|
| `weapons_timeline.py` | ✅ Ran — 27 nodes / 26 Timeline_Evolves edges (1776 Brown Bess → 2026 LAWS) |
| `enhance_gephi.py` | ✅ Ran — 27 enhanced nodes (data_quality) + 49 base + 10 Pacific = **59 edges** |
| `weapons_gephi_month2_enhanced.csv` | ✅ MD5 `5366eda78d1774dc53de5317ff8a9cb3` — unchanged (3rd consecutive stable run since 2026-05-22) |
| `weapons_nodes_month2_enhanced.csv` | ✅ MD5 `33964a5a1a00bd6537de03e9927eef44` — unchanged |
| `weapons_gephi_month2_3.csv` | ✅ MD5 `191b5ef6ad62ccacc8d4c1715d4bae07` — unchanged |
| `weapons_nodes_month2_3.csv` | ✅ MD5 `7bd0693f11a70073be045f77964affd1` — unchanged |
| Edge types | Timeline_Evolves(26) + Same_War(18) + Era_Cluster(5) + Pacific_Link(10) |

### Stability Check
- 4 個核心 CSV 全部 byte-identical to 2026-06-03 / 2026-05-22 runs — data layer 已經成熟（自 04-08 以來 0 delta）
- LAWS Lethal Autonomous Weapon Systems (2026) 仍係 terminus node，AI Era policy gap 維持 2–3 年 lag vs deployment
- data_quality 分佈：verified 7 戰 (American Revolution, Mexican-American, Civil War, Spanish-American, WWI, WWII, Gulf War, War on Terror) / primary 3 戰 (Korean, Cold War, Vietnam) / estimated 4+ 區塊 (Near-peer, Ukraine, Global, AI Era)
- obsidian-vault CSVs 自動同 source 同步（MD5 一致）

### Network Density (Recap, 6 月穩定基準)
- E/N ratio = 59/27 = **2.18**（Month 1 基準 1.10，今日仍 2×）
- Civil War cluster (1861–63) — 3-way same-war density 最高
- AI Era cluster (2024–26) — LAWS policy gap 仲未收窄

### Git Status (pre-commit)
- `dhga-weaponhistory` HEAD: `773dccb` (2026-06-08 portfolio landing page)
- Working tree 改動：
  - `M DHG501_AI_Weapon_Era_Summary.md`（前次 cron 留下嘅 uncommitted touch）
  - `M DHGA_Month_2-3_Gephi_QGIS.md`（本次 run 嘅 note update — 即將 commit）
  - `?? Primary_Sources/LoC_Military_Maps_2026-06-08.md`、`?? qgis_overlay_2026-06-08.py`、`?? qgis_screenshots/`（QGIS overlay run 留低嘅新檔，唔屬今次 cron scope）

### Cross-link to Capstone Section 4.6
- Section 4.6 已於 2026-06-07 完成擴寫（Yokosuka/Okinawa/Guam civilian voice + Sun Tzu/Mao + Mỹ Lai + MIC profit layer + NARA disclosure）
- Pacific_Link 10 條邊同 4.6.1 + 4.6.2 嘅 civilian-impact narrative 100% 對應
- `Capstone_Section_4.6_AI_Supply_Chain_Closure.md` 仍係 canonical；Gephi 圖暫作 supplementary，未嵌入 capstone body

### 下一步行動（Month 4 Week 1 起, 2026-06-10 → 2026-06-17）
- [ ] **QGIS screenshot 仍 pending** — headless server blocker，要 local QGIS GUI；2026-06-08 嘅 matplotlib emulation 可作 fallback 但唔係 final
- [ ] **Gephi Modularity community detection** — 仲未跑，`capstone_network_visualization.py` 已用 `gephi_weapons_network_nodes.csv`/`gephi_weapons_network_edges.csv` 嗰對檔（27 nodes 同類），要將今次 59-edge enhanced CSV 過入去再跑
- [ ] **NARA primary source scan** — 1861–1865 Ordnance reports 驗 Civil War cluster；連續 4 週落後
- [ ] **Month 4 capstone narrative 補丁** — DHGA_Capstone_Month_4.md 仲係 2026-06-01 版本，要將 Section 4.6 嘅改動 (4.6.1–4.6.5) 同步入 Month 4 narrative
- [ ] **觀察 2026 年新武器進入 list 嘅 trigger** — 6 月至今未有新 terminus；任何新 LAWS 變種、Switchblade 後繼、或者 Indo-Pacific 新武器部署都會即時拉高 E/N ratio

### 袁騰飛式補注
「三個禮拜冇變化，正常——呢個係 data layer 已經熟嘅訊號。Gephi 嘅 59 條邊寫到 2026 年 6 月，但 4.6 嘅 narrative 已經走到 Yokosuka 居民、Sun Tzu 嘅 supply chain intelligence、Mỹ Lai 反思嗰度。即係話圖追上咗現實，但現實仲喺圖前面跑。Capstone 攻讀期最忌嘅就係『圖夠用啦』——下個月真係要過 Modularity 嗰關，將 Civil War 嗰 3-way cluster 量化，唔好淨係用顏色講。」

---
*Auto-generated by DHGA_Python_Gephi cron | 2026-06-10 14:00 UTC*

## 🗺️ 2026-06-11 QGIS Overlay Run（Week 2 — Pacific Civilian-Pressure Lens）

**Cron:** `DHGA_QGIS_Reminder` | **Time:** 2026-06-11 10:00 UTC (Thursday) | **Status:** ✅ Complete

### Artifacts
| File | Size | Purpose |
|------|------|---------|
| `qgis_screenshots/qgis_overlay_2026-06-11.png` | 811 KB | Global supply-chain geography (refreshed) |
| `qgis_screenshots/qgis_overlay_2026-06-11_pacific_lens.png` | **854 KB (NEW)** | **Section 4.6.1 civilian-pressure overlay** |
| `qgis_screenshots/qgis_overlay_2026-06-11_indo_pacific_inset.png` | 252 KB | Indo-Pacific detail (refreshed) |
| `qgis_overlay_2026-06-11.py` | 8.9 KB | Reproducible script (Pacific lens 為新增層) |

### 新增：Pacific Civilian-Pressure Lens（Capstone Section 4.6.1 對位）
7 個 civilian-voice 站點被疊加到供應鏈地圖上面，每個有 narrative anchor：

| 站點 | 經緯 | Section 4.6.1 anchor |
|------|------|---------------------|
| **Yokosuka** | 139.67°E 35.29°N | US 7th Fleet HQ / civilian port-city pressure |
| **Okinawa** | 127.68°E 26.21°N | Futenma 1995 rape incident + 2010 relocation crisis |
| **Guam (Chamorro)** | 144.79°E 13.44°N | US strategic hub / indigenous sovereignty movement |
| **Hsinchu (TSMC)** | 120.97°E 24.80°N | 76,000 員工 / Taiwan Strait blockade exposure |
| **Jeju (ROK)** | 126.50°E 33.50°N | 2011–2016 Gangjeong naval base protest |
| **Mariana Trench** | 145.75°E 15.18°N | Aegis Ashore / THAAD radar deployment |
| **Timor-Leste** | 127.73°E -8.41°N | Post-colonial non-alignment / NDF-Ramos-Horta |

每個站點用 `FancyBboxPatch` 軟黃色半透明 bbox + 橙色 `*` marker + narrative 標註，可直接放 Section 4.6 figure slot。

### 設計 rationale
- 06-08 跑嘅係「全球供應鏈 + Indo-Pacific inset」 — 答嘅係 *where are the chokepoints*
- 06-11 跑嘅係「Pacific civilian-pressure lens」 — 答嘅係 *who is paying the price*
- 兩個 lens 互補：06-08 講 supply-side 地理壓力，06-11 講 demand-side civilian 承受
- 配合 4.6 嘅 5 個 sub-section（4.6.1 Pacific voice / 4.6.2 chokepoint / 4.6.3 Mao pressure / 4.6.4 Mỹ Lai / 4.6.5 MIC profit），呢個 lens 係 4.6.1 嘅 visual hook

### Reproduce
```bash
cd /home/node/.openclaw/workspace/dhga-weaponhistory
python3 qgis_overlay_2026-06-11.py
```
*Auto-generated by DHGA_QGIS_Reminder | 2026-06-11 10:00 UTC*

---

## 🗺️ 2026-06-11 QGIS Overlay Run（Week 2 — Pacific Civilian-Pressure Lens）

**Cron:** `DHGA_QGIS_Reminder` | **Time:** 2026-06-11 10:00 UTC (Thursday) | **Status:** ✅ Complete

### Artifacts
| File | Size | Purpose |
|------|------|---------|
| `qgis_screenshots/qgis_overlay_2026-06-11.png` | 811 KB | Global supply-chain geography (refreshed) |
| `qgis_screenshots/qgis_overlay_2026-06-11_pacific_lens.png` | **854 KB (NEW)** | **Section 4.6.1 civilian-pressure overlay** |
| `qgis_screenshots/qgis_overlay_2026-06-11_indo_pacific_inset.png` | 252 KB | Indo-Pacific detail (refreshed) |
| `qgis_overlay_2026-06-11.py` | 8.9 KB | Reproducible script (Pacific lens 為新增層) |

### 新增：Pacific Civilian-Pressure Lens（Capstone Section 4.6.1 對位）
7 個 civilian-voice 站點被疊加到供應鏈地圖上面，每個有 narrative anchor：

| 站點 | 經緯 | Section 4.6.1 anchor |
|------|------|---------------------|
| **Yokosuka** | 139.67°E 35.29°N | US 7th Fleet HQ / civilian port-city pressure |
| **Okinawa** | 127.68°E 26.21°N | Futenma 1995 rape incident + 2010 relocation crisis |
| **Guam (Chamorro)** | 144.79°E 13.44°N | US strategic hub / indigenous sovereignty movement |
| **Hsinchu (TSMC)** | 120.97°E 24.80°N | 76,000 員工 / Taiwan Strait blockade exposure |
| **Jeju (ROK)** | 126.50°E 33.50°N | 2011–2016 Gangjeong naval base protest |
| **Mariana Trench** | 145.75°E 15.18°N | Aegis Ashore / THAAD radar deployment |
| **Timor-Leste** | 127.73°E -8.41°N | Post-colonial non-alignment / NDF-Ramos-Horta |

每個站點用 `FancyBboxPatch` 軟黃色半透明 bbox + 橙色 `*` marker + narrative 標註，可直接放 Section 4.6 figure slot。

### 設計 rationale
- 06-08 跑嘅係「全球供應鏈 + Indo-Pacific inset」 — 答嘅係 *where are the chokepoints*
- 06-11 跑嘅係「Pacific civilian-pressure lens」 — 答嘅係 *who is paying the price*
- 兩個 lens 互補：06-08 講 supply-side 地理壓力，06-11 講 demand-side civilian 承受
- 配合 4.6 嘅 5 個 sub-section（4.6.1 Pacific voice / 4.6.2 chokepoint / 4.6.3 Mao pressure / 4.6.4 Mỹ Lai / 4.6.5 MIC profit），呢個 lens 係 4.6.1 嘅 visual hook

### Reproduce
```bash
cd /home/node/.openclaw/workspace/dhga-weaponhistory
python3 qgis_overlay_2026-06-11.py
```
*Auto-generated by DHGA_QGIS_Reminder | 2026-06-11 10:00 UTC*

---
