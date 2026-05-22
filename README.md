# DHGA-WeaponHistory
## Network Analysis of U.S. Military Technology Evolution (1776-2026)

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

**Modularity Score: 0.53** | **6-8 Communities**

---

## 📁 Repository Structure

```
dhga-weaponhistory/
├── capstone/           # Capstone thesis (~2,800 words)
├── visualizations/      # Network graphs and maps
├── data/               # Raw datasets
│   ├── nodes/         # Gephi node CSV
│   ├── edges/         # Gephi edge CSV
│   └── timeline/      # Weapon timeline data
├── code/              # Python analysis scripts
├── primary_sources/   # NARA, Library of Congress references
├── docs/              # GitHub Pages files
└── obsidian-vault/    # Research notes
```

---

## 🔗 Key Files

| File | Description |
|------|-------------|
| `capstone/DHGA_Capstone_Complete.md` | Full thesis draft (Chinese + English) |
| `visualizations/capstone_network_graph.png` | Network visualization (300dpi) |
| `code/capstone_network_visualization.py` | Python visualization script |
| `data/nodes/gephi_weapons_network_nodes.csv` | 32 weapon nodes |
| `data/edges/gephi_weapons_network_edges.csv` | 41 edge relationships |

---

## 🛠️ Methods

- **Louvain Community Detection** (python-louvain)
- **Network Analysis** (NetworkX)
- **Data Visualization** (Matplotlib)
- **Geospatial Mapping** (Folium)

---

## 📖 Literature

- Mumford, L. (1934). *Technique and Civilization*
- Winner, L. (1977). *The Whale and the Reactor*
- Kaiser, W. (2018). Digital history approaches to military innovation
- Cohen, E. A. (2008). Technology and warfare

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/dhga-weaponhistory.git
cd dhga-weaponhistory

# Run network analysis
pip install pandas networkx python-louvain matplotlib
python code/capstone_network_visualization.py
```

---

## 📜 License

MIT License

---

*Generated: May 2026* | *DHGA Digital History Capstone*