# U.S. Military Technological Evolution and Trans-Pacific Conflict Outcomes (1776–2026)

**A Network Analysis Approach**

This repository documents a digital history research project examining how U.S. military technology evolved from flintlock muskets in 1776 to AI-enabled lethal autonomous weapons systems (LAWS) in 2026, and how these technological changes shaped outcomes in trans-Pacific conflicts.

The project integrates historical training, network analysis, and critical historiography to challenge linear narratives of technological progress and U.S.-centric interpretations of military innovation.

---

## Research Question

How did U.S. military technological change from 1776 to 2026 influence trans-Pacific war outcomes? What structural patterns of technological convergence, learning, and rupture can be identified through network analysis of weapon systems and their supply chains?

---

## Key Findings

Using Louvain community detection on a 32-node weapon system network (41 edges, modularity 0.5362), the project identifies three core dynamics:

| Community | Dynamic | Key Insight |
|-----------|----------------------------|-------------|
| **0** | Technological Convergence | Partial functional convergence between U.S., Chinese, and Russian systems in stealth, integrated air defence, precision strike, and unmanned/AI technologies since the mid-2010s |
| **3** | Technological Learning | Evidence of structural learning, with U.S. systems showing relational proximity to challenger systems (e.g. M16 near AK-47/AK-74) |
| **1** | Technological Rupture | AI and drone systems (Gorgon Stare, Switchblade, LAWS) form a distinct new community, indicating a potential paradigm shift |

**Additional Critical Dimension**:
- **Profit-Driven Inertia**: Supply chain topology is reinforced by the profit logic of the U.S. military-industrial complex, creating structural lock-in and concentrated geographic risk (particularly in Taiwan and South Korea).

The analysis incorporates civilian perspectives from Okinawa, Guam, and Taiwan, non-Western strategic frameworks, and critiques of technological determinism.

---

## Methodology

- **Network Construction**: 32-node weapon system network (U.S. systems + control group challengers)
- **Community Detection**: Louvain algorithm (resolution = 0.5)
- **Data Sources**: Secondary synthesis of military-technical history with control group comparison
- **Visualization**: Gephi, Python (NetworkX + python-louvain), Folium interactive maps
- **Critical Framework**: Clausewitzian friction + Maoist protracted war logic + structural coupling analysis
- **Ethics Review**: Ongoing auditing addressing Western-centrism, victor's history, and civilian costs

---

## Project Structure

```
dhga-weaponhistory/
├── README.md
├── capstone/
│   └── DHGA_Capstone_Complete.md
├── courses/
│   └── HKU_History/
│       ├── README.md
│       └── HKU_History_Courses.md   # 72 courses (official 2025-26)
├── data/
│   ├── edges/
│   ├── nodes/
│   ├── timeline/
│   ├── supply_chain/
│   └── louvain_community_result.csv
├── visualizations/
│   ├── supply_chain_folium.html
│   └── capstone_community_graph.png
├── code/
│   ├── capstone_network_visualization.py
│   ├── gen_folium_map.py
│   ├── gen_map.py
│   └── enhance_gephi.py
├── Primary_Sources/
├── docs/
│   └── index.html
└── OpenClaw_Vault_Backup_*.md
```

---

## Key Outputs

- Full research paper with Discussion and Conclusion
- Interactive supply chain visualization (Folium)
- Weapon network community detection graph
- Curated HKU History undergraduate courses list (72 courses) aligned with project themes

---

## Supporting Resources

### HKU History Undergraduate Courses (2025-26)

A curated selection of **72 undergraduate courses** from the University of Hong Kong History Department and cross-listed programmes has been added to support the Historical Training component.

- **Location**: [`courses/HKU_History/HKU_History_Courses.md`](courses/HKU_History/HKU_History_Courses.md)
- Courses are categorized thematically with relevance assessments and Tier recommendations (Tier 1 = highest relevance to the capstone).
- Includes History-coded courses and cross-listed Survey/Seminar courses from other departments.

This resource strengthens comparative analysis (e.g. Atlantic vs Pacific systems) and critical approaches to empire, technology, race, gender, and global historical methods.

---

## Technical Stack

- **Network Analysis**: Python (NetworkX, python-louvain), Gephi
- **Visualization**: Folium, Matplotlib
- **Workflow Automation**: OpenClaw multi-agent system
- **Version Control & Documentation**: Git, Markdown, Obsidian

---

## Current Status

**Completion**: ~93%

**Completed**:
- Network analysis and community detection
- Full Discussion chapter with theoretical implications
- Integration of ethics critique (civilian perspectives, non-Western frameworks, profit-driven inertia)
- Curated HKU History courses list (official 2025-26)
- Interactive visualizations and landing page (`docs/index.html`)

**Remaining**:
- Final embedding of visualizations into the capstone document
- GitHub Pages activation (Settings → Pages)
- Minor final proofreading

---

## How to Use This Repository

1. Review `capstone/DHGA_Capstone_Complete.md` for the complete argument and findings.
2. Explore `data/` for network data and Louvain results.
3. Open visualizations in `visualizations/` for interactive maps and graphs.
4. Use `courses/HKU_History/HKU_History_Courses.md` as a structured reading list for historical training.

---

## Author

**Author**: Saba  
**Project Type**: Digital history research project (Capstone thesis)  
**Focus**: U.S. military technology, trans-Pacific conflicts, network analysis, and critical historiography (1776–2026)

---

## License

This repository is shared for academic, portfolio, and educational purposes.
Please cite appropriately if used in other work.

**Last Updated**: 2026-06-08
