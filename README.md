# DHGA-WeaponHistory
## Network Analysis of U.S. Military Technology Evolution (1776–2026)

**DHGA Capstone Project** | *Digital History & Global Affairs*

---

## 🎯 Research Question

How has the evolution of U.S. military weapons from the 1776 flintlock to 2026 AI-enabled systems influenced the outcomes of trans-Pacific conflicts?

---

## 📊 Key Findings

This study uses **Louvain community detection** to analyze a network of 32 weapon systems and 41 technological relationships, revealing **three interrelated dynamics**:

| Community | Finding | Description |
|-----------|----------|-------------|
| **Community 0** | Technological Convergence | Modern Indo-Pacific U.S., Chinese, and Russian weapons cluster together |
| **Community 3** | Technological Learning | Soviet small arms (AK-47, AK-74) integrated into U.S. Cold War weapon communities |
| **Community 1** | Technological Rupture | AI/Drone systems forming independent paradigm (Gorgon Stare, Switchblade, LAWS) |

**Modularity Score: 0.5362** | **6 communities detected** (3 analytically significant: 0, 1, 3)

---

## 📁 Repository Structure

```
dhga-weaponhistory/
├── capstone/                  # Capstone thesis (English, ~2,650 words)
├── visualizations/            # Network graphs and maps
│   ├── capstone_network_graph.png
│   ├── qgis_supply_chain_map.png
│   └── working/               # Working HTML iterations (Folium, Plotly)
├── data/                      # Canonical network datasets
│   ├── nodes/gephi_weapons_network_nodes.csv
│   ├── edges/gephi_weapons_network_edges.csv
│   ├── louvain_community_result.csv
│   └── archive/               # Older iterative CSV versions
├── code/                      # Main analysis scripts
│   ├── capstone_network_visualization.py
│   └── archive/               # Older development scripts
├── primary_sources/           # Library of Congress military maps
│   └── LoC_Military_Maps_*.md
├── README.md
├── LICENSE                    # MIT
└── Course weekly reports (DHG5xx) and Capstone work notes
```

---

## 🔗 Key Files

| File | Description |
|------|-------------|
| `capstone/DHGA_Capstone_Complete.md` | Full thesis draft (English) |
| `visualizations/capstone_network_graph.png` | Network visualization (300 dpi) |
| `code/capstone_network_visualization.py` | Python visualization + Louvain analysis |
| `data/nodes/gephi_weapons_network_nodes.csv` | 32 weapon nodes (canonical) |
| `data/edges/gephi_weapons_network_edges.csv` | 41 edge relationships (canonical) |
| `data/louvain_community_result.csv` | Louvain output: community assignments |

---

## 🛠️ Methods

- **Louvain Community Detection** (`python-louvain`, resolution = 0.5)
- **Network Analysis** (NetworkX)
- **Data Visualization** (Matplotlib)
- **Geospatial Mapping** (Folium, Plotly, QGIS)

The dataset uses **two edge types**:
1. **Timeline_Evolves** — Direct technological succession between weapon systems
2. **Pacific_Link** — Cross-Pacific competitive relationships between U.S. and challenger systems

---

## 📖 Literature

- Mumford, L. (1934). *Technique and Civilization*
- Winner, L. (1977). *The Whale and the Reactor*
- Cohen, E. A. (2008). Technology and warfare
- Bonnett, A. (2015). *Left in the Dark*
- Kaiser, W. (2018). Digital history approaches to military innovation
- Blondel, V. D., et al. (2008). Fast unfolding of communities in large networks (Louvain method)

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/szesex/dhga-weaponhistory.git
cd dhga-weaponhistory

# Install dependencies
pip install pandas networkx python-louvain matplotlib

# Run network analysis (regenerates capstone_network_graph.png)
python code/capstone_network_visualization.py
```

---

## 📜 License

MIT License

---

*Last updated: June 2026* | *DHGA Digital History Capstone*
