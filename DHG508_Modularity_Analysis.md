# DHG508 Week 7 Modularity Analysis
## 40-Node Bipartite Network — 2026-05-11

## 📊 數據結構確診

**網絡類型：** 雙極網絡（Bipartite Network）
- **27 武器節點（Source）** — 每把武器係一個歷史技術變量
- **40 結果節點（Target）** — Political_Continuation / Friction / Center_of_Gravity
- **40 條邊** — 每把武器連接到佢 enable 的歷史 outcome

**核心發現：** 零對武器共享同一個 outcome——呢個 CSV 的設計目的係理論論證，唔係社群檢測。

---

## 🎯 7 個時期集群（Periodization）

| 時期 | 節點數 | 核心武器 |
|------|--------|---------|
| 1776-1840 | 2 | Flintlock Musket, Flintlock Pistol |
| 1846-1865 | 6 | Springfield Rifle, Gatling, Ironclad |
| 1898-1918 | 4 | Krag-Jorgensen, M1903 Springfield, BAR |
| 1941-1952 | 8 | M1 Garand, Atomic Bomb, H-Bomb |
| 1950-1970 | 4 | M14, M16, M60 |
| 1991-2003 | 7 | Abrams, F-117, Tomahawk, Predator |
| 2020-2026 | 9 | F-35, Switchblade, LAWS, Gorgon/Stare |

---

## 📊 Clausewitz Category 分布

| Category | 節點數 | 佔比 |
|----------|--------|------|
| Friction_Type | 12 | 30% |
| Tactical_CoG | 10 | 25% |
| Strategic_CoG | 9 | 22.5% |
| Political_Context | 8 | 20% |
| Ethical_CoG | 1 | 2.5% |

---

## 🔍 Control Group 分析

**AK-47、HQ-17、TOR-M1 不在這個 40-node CSV 內**
- 佢哋喺 33-node 版本先有（包含 10 條新增 Control_Comparison edges）
- 呢個驗證咗：呢個 CSV 係 Clausewitz 理論分析，唔係武器比較網絡

---

## ✅ Week 7 結論

1. **Modularity Score = 0**（因為 bipartite 結構限制）
2. **有意義的集群 = 7 個時期**（符合歷史時間線）
3. **Friction 最多（30%）**——支持 Cohen 的「戰爭阻力」理論
4. **Control Group 需要返 33-node 版本先做到真正社群分析**

---

## ⚠️ Gephi 操作建議

如果要用 40-node 版本做 Modularity：
1. **Gephi → Tools → Multimode Networks Projection**
2. Source: Weapon nodes, Target: Outcome nodes
3. 投影後再跑 Modularity（Resolution 0.5）

---

## Month 2 Capstone Visualization（500字版）

Month 2：數位歷史方法與視覺化實踐（DHG502）

**中文版：**
Month 2 專注數位歷史方法實踐，主要成果包括 Gephi control group 網絡圖（33 nodes、79 edges）及 Plotly 互動供應鏈地圖（https://szesex.github.io/dhga-weaponhistory/supply_chain_with_battlefields.html）。

Gephi 網絡清晰呈現 4 大集群：Civil War（Rifled Musket + Gatling + Ironclads）、WWII（M1 Garand → Atomic Bomb）、Gulf War（Abrams + F-117 + Tomahawk）、AI Era（Gorgon/Stare → LAWS）。新增 10 條 Control_Comparison edges（AK-47 vs M16、HQ-17 vs F-35、TOR-M1 vs LAWS），成功將 Bias Score 由 3.3/5 提升至 4.5/5，有效平衡美國中心敘事。Pacific_Link（綠色）象徵美國武器對亞洲地緣影響，MiddleEast_Link（橙色）展示全球衝突延伸。

Plotly 互動地圖進一步將抽象網絡轉化為可 hover、可 zoom、可 filter 的空間視覺化，疊加 1776 革命戰場與太平洋島嶼戰場，真正實現從 Gephi 抽象網絡到 QGIS/Plotly 地理疊加的數位方法閉環。

**English Version：**
Month 2 focused on digital history methods practice, with key deliverables including the Gephi control-group network graph (33 nodes, 79 edges) and the Plotly interactive supply-chain map (https://szesex.github.io/dhga-weaponhistory/supply_chain_with_battlefields.html).

The Gephi network clearly presents four major clusters: Civil War (Rifled Musket + Gatling + Ironclads), WWII (M1 Garand → Atomic Bomb), Gulf War (Abrams + F-117 + Tomahawk), and AI Era (Gorgon/Stare → LAWS). Ten new Control_Comparison edges (AK-47 vs M16, HQ-17 vs F-35, TOR-M1 vs LAWS) were added, successfully raising the Bias Score from 3.3/5 to 4.5/5 and balancing the US-centric narrative. Pacific_Link (green) symbolizes US weapons' impact on Asian geopolitics, while MiddleEast_Link (orange) extends to global conflicts.

The Plotly interactive map further transforms the abstract network into a hoverable, zoomable, filterable spatial visualization, overlaying 1776 Revolutionary War battlefields with Pacific island battlefields, achieving a full digital methods loop from Gephi abstraction to QGIS/Plotly geographic overlay.

---

## Capstone Literature Review

### DHG508: Literature Review — 技術變革與戰爭形態的理論框架

**一、核心理論：Cohen 的路徑依賴與技術擴散**
Cohen（1996）的《Force and Progress》提出：武器技術的進步唔係線性的，而係路徑依賴的——每個技術節點都會影響下一個階段的選擇集合。Flintlock 決定了來福槍的發展方向，來福槍決定了機關槍的需求，機關槍決定了戰壕系統的邏輯。呢個理論解釋了點解 1776 年的 European 武器供應鏈會塑造 2026 年的 AI 武器架構。

**二、批評性修正：Stahlberg 的多極化視角**
Stahlberg（2020）批評 Cohen 的「單一技術路徑」假設，指出：真正的武器擴散係多極化的——AK-47 的全球化證明左非美國系統可以點樣反制美國技術路徑。呢個批評為 DHG508 的 Control Group 方法提供左理論基礎：必須將非美國武器（AK-47、HQ-17、TOR-M1）納入分析框架，唔可以假設美國係唯一技術變量的來源。

**三、數位歷史方法：Bonnett 的網絡地理學**
Bonnett（2016）的《Digital History》提出：網絡圖（如 Gephi）可以揭示文字論證無法呈現的關係結構。但 Bonnett 同時警告：網絡圖唔可以脫離地理空間——抽象節點需要坐標數據先可以防止「去脈絡化」的危險。DHG508 的 QGIS/Plotly 方法正正係回應呢個警告：將 Gephi 的抽象網絡重新嵌入地理空間，實現 Cohen 理論的空間化。

**四、道德框架：AI 武器的歷史連續性**
Kaiser（2019）的《Autonomous Weapons》論證：AI 決策系統唔係突然出現的，而係從精確制導武器（1991 Gulf War）一路演變過來的。呢個連續性論點為 DHG508 的「1776 → 2026」時間線提供道德基礎——如果我哋接受 Flintlock 係戰爭工具，咁我哋就無法拒絕 AI 武器的歷史邏輯，除非我哋願意否認整條技術變革的連續性。

**五、結論：DHG508 的理論位置**
DHG508 位於 Cohen（技術決定論）、Stahlberg（多極化批判）、Bonnett（數位方法）、Kaiser（AI倫理）四個理論框架的交集。呢個交集允許我哋提出一個命題：美國軍武從 1776 到 2026 的發展路徑，唔係例外，而係技術變革全球擴散的其中一個變量。