# DHGA-WeaponHistory

## Network Analysis of U.S. Military Technology Evolution (1776–2026)

**Digital History & Global Affairs (DHGA) Capstone** · Submitted June 2026  
*Author: Saba* · *GitHub: [@szesex](https://github.com/szesex)*

[![Repo size](https://img.shields.io/github/repo-size/szesex/dhga-weaponhistory?style=flat-square)](https://github.com/szesex/dhga-weaponhistory)
[![Commits](https://img.shields.io/github/commit-activity/m/szesex/dhga-weaponhistory?style=flat-square)](https://github.com/szesex/dhga-weaponhistory/commits/master)
[![Last commit](https://img.shields.io/github/last-commit/szesex/dhga-weaponhistory?style=flat-square)](https://github.com/szesex/dhga-weaponhistory/commits/master)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)
[![Made with: Python](https://img.shields.io/badge/made%20with-Python%203-3776AB?style=flat-square&logo=python&logoColor=white)](#-methods--tools)

> 🌐 **Live project site:** *(enable GitHub Pages on `master` / `/docs` to publish → [setup instructions](docs/))*

---

## 🎯 Research Question

> *How has the evolution of U.S. military weapons — from the 1776 flintlock musket to 2026 AI-enabled systems — influenced the outcomes of trans-Pacific conflicts?*

This study treats military technology as a **relational network**, not a linear timeline. By applying **Louvain community detection** to 32 weapon systems and 41 technological relationships, it uncovers structural patterns of convergence, learning, rupture, and profit-driven inertia across 250 years of military innovation.

---

## 📊 Key Findings

The Louvain analysis (modularity **0.5362**) identifies **six communities**, four of which carry the main interpretive load:

| Community | Theme | Diagnostic Pattern |
|:---------:|-------|--------------------|
| **C0** | 🛰️ *Indo-Pacific Convergence* | Modern U.S., Chinese, and Russian weapons cluster together — Cold War bipolarity has dissolved into a multipolar techno-strategic field. |
| **C1** | 🤖 *AI/Autonomy Rupture* | LAWS, Gorgon Stare, Switchblade, Reaper form an isolated paradigm — the first community with no analog-era ancestry. |
| **C3** | 🔁 *Cold-War Learning* | Soviet small arms (AK-47, AK-74) integrate into U.S. weapon communities — proof of bidirectional technological transfer. |
| **(C0+) 💰** | *Profit-Driven Inertia* | A military–industrial complex layer (Lockheed / Raytheon / General Dynamics → F-35, Patriot, JASSM) explains why some legacy platforms survive past their technological relevance. *(see §4.6.5)* |

**Headline numbers:** 32 nodes · 41 edges · 6 communities · modularity 0.5362 · span 1776–2026 (250 years).

---

## 🗂️ Repository Structure

```
dhga-weaponhistory/
├── capstone/
│   └── DHGA_Capstone_Complete.md       # Full thesis (~2,800 words, English, Chicago)
├── data/
│   ├── nodes/                          # Gephi node CSVs
│   ├── edges/                          # Gephi edge CSVs
│   ├── supply_chain/                   # Georeferenced supply chain data
│   ├── timeline/                       # Weapon timeline CSVs
│   └── louvain_community_result.csv    # Community assignment output
├── code/
│   ├── capstone_network_visualization.py
│   ├── gen_folium_map.py
│   ├── gen_map.py
│   ├── generate_map.py
│   ├── enhance_gephi.py
│   ├── enhance_gephi_iran2026.py
│   └── weapons_timeline.py
├── visualizations/
│   ├── capstone_network_graph.png      # Static 300 dpi network graph
│   ├── supply_chain_folium.html        # Interactive Folium map
│   ├── supply_chain_plotly.html        # Interactive Plotly map
│   ├── supply_chain_ai_weapons.html    # AI weapons overlay
│   └── supply_chain_with_battlefields.html
├── Primary_Sources/                    # NARA, LOC, DOD reference material
├── docs/                               # GitHub Pages landing site
│   └── index.html
└── README.md
```

---

## 🛠️ Methods & Tools

| Layer | Tool | Purpose |
|-------|------|---------|
| Network construction | `NetworkX` | Build directed multigraph of weapons & relations |
| Community detection | `python-louvain` | Louvain modularity optimization |
| Visualization (static) | `Matplotlib` | Final 300 dpi network graph |
| Visualization (geo) | `Folium` + `Plotly` | Interactive supply-chain & battle maps |
| Georeferencing | `QGIS` | Battlefield / supply-line coordinates |
| Network exploration | `Gephi` | Layout + filtering, CSV in/out |
| Versioning | `Git` + `GitHub` | Audit trail for every analytical step |

### Methodological notes

- Edge coding captures **four relation types**: direct descent, technical lineage, doctrinal inheritance, and adversarial imitation.
- Modularity is reported at the resolution that maximises the *interpretive* separation of C0/C1/C3 (not a one-shot default).
- All weapon selection decisions and date ranges are documented in `capstone/DHGA_Capstone_Complete.md` §3.

---

## 🔭 Visualizations

| Artifact | Type | File |
|----------|------|------|
| Network graph (300 dpi) | Static PNG | [`visualizations/capstone_network_graph.png`](visualizations/capstone_network_graph.png) |
| Supply chain map | Interactive HTML (Folium) | [`supply_chain_folium.html`](supply_chain_folium.html) |
| Supply chain + battlefields | Interactive HTML (Folium) | [`supply_chain_with_battlefields.html`](supply_chain_with_battlefields.html) |
| AI weapons overlay | Interactive HTML (Folium) | [`supply_chain_ai_weapons.html`](supply_chain_ai_weapons.html) |
| Plotly network | Interactive HTML (Plotly) | [`supply_chain_plotly.html`](supply_chain_plotly.html) |
| Map generator | Python | [`code/gen_folium_map.py`](code/gen_folium_map.py) |

---

## 📖 How to Reproduce

```bash
# 1. Clone
git clone https://github.com/szesex/dhga-weaponhistory.git
cd dhga-weaponhistory

# 2. Environment
python3 -m venv .venv && source .venv/bin/activate
pip install pandas networkx python-louvain matplotlib folium plotly

# 3. Re-run network analysis
python code/capstone_network_visualization.py

# 4. Re-render any interactive map
python code/gen_folium_map.py
python code/gen_map.py
```

Outputs land in `visualizations/`. CSV in `/data` is the single source of truth — all scripts read from it.

---

## 📚 Selected References

- Blondel, V. D., Guillaume, J.-L., Lambiotte, R., & Lefebvre, E. (2008). Fast unfolding of communities in large networks. *JSTAT*.
- Bonnett, A. (2015). *The Geographies of Historical Militarism.*
- Cohen, E. A. (2008). *Technology and Warfare.*
- Mumford, L. (1934). *Technics and Civilization.*
- Winner, L. (1977). *The Whale and the Reactor.*

Full bibliography (Chicago Author-Date) is in the capstone document.

---

## ⚖️ Ethics Statement

This work studies weapon systems as *historical and technological artifacts*, not as operational guides. AI weapons are analyzed at the systems level (LAWS doctrine, Gorgon Stare sensor architecture, Switchblade loitering munitions) — not at the level of targeting solutions. All primary sources are public-record (NARA, Library of Congress, DoD publications). See `DHG508_AI_Ethics_Weekly_Report.md` for the running ethics-review log.

---

## 📜 License

MIT — see [`LICENSE`](LICENSE).

---

*Capstone submitted to the DHGA programme, June 2026. Repo continuously updated; this README is the portfolio entry point.*
