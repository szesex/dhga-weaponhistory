import pandas as pd
import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ==================== 檔案路徑 ====================
NODES_PATH = "/home/node/.openclaw/workspace/gephi_weapons_network_nodes.csv"
EDGES_PATH = "/home/node/.openclaw/workspace/gephi_weapons_network_edges.csv"
OUTPUT_PATH = "/home/node/.openclaw/workspace/capstone_network_graph.png"

# 讀取數據
nodes_df = pd.read_csv(NODES_PATH)
edges_df = pd.read_csv(EDGES_PATH)

# 建立網絡
G = nx.Graph()

for _, row in nodes_df.iterrows():
    G.add_node(
        row['Id'],
        label=row.get('Label', row['Id']),
        year=row.get('Year'),
        control_group=row.get('Control_Group', 'FALSE') == 'TRUE',
        era=row.get('Era'),
        data_quality=row.get('data_quality')
    )

for _, row in edges_df.iterrows():
    src = row.get('csvSource', row.get('Source', ''))
    tgt = row.get('Target', '')
    weight = row.get('Weight', 1)
    G.add_edge(src, tgt, weight=weight, type=row.get('Type', ''))

print(f"Network built: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# ==================== LOUVAIN 社群檢測 ====================
partition = community_louvain.best_partition(G, weight='weight', resolution=0.5)
modularity_score = community_louvain.modularity(partition, G, weight='weight')

print(f"Modularity Score: {modularity_score:.4f}")
print(f"Communities: {len(set(partition.values()))}")

# ==================== 視覺化設置 ====================
plt.figure(figsize=(20, 16))
pos = nx.spring_layout(G, k=2, iterations=100, seed=42)

# 定義顏色（英文標籤版本）
community_colors = {
    0: '#FF6B6B',   # Red - Tech Convergence
    1: '#4ECDC4',   # Teal - AI/Drone
    2: '#45B7D1',   # Blue - Early Era
    3: '#96CEB4',   # Green - Cold War Small Arms
    4: '#FFEAA7',   # Yellow
    5: '#DDA0DD',   # Plum
    6: '#98D8C8',   # Light Green
    7: '#F7DC6F',   # Gold
    8: '#BB8FCE',   # Lavender
    9: '#85C1E2',   # Light Blue
    10: '#F8B500',  # Orange
    11: '#C0392B',  # Dark Red
}

# 節點顏色
node_colors = [community_colors.get(partition[node], '#CCCCCC') for node in G.nodes()]

# 節點大小（根據連接度）
node_sizes = [300 + G.degree(node) * 100 for node in G.nodes()]

# 區分 Control Group（用金色邊框）
node_edge_colors = ['#FFD700' if G.nodes[node].get('control_group') else '#333333' for node in G.nodes()]
node_edge_widths = [4 if G.nodes[node].get('control_group') else 1.5 for node in G.nodes()]

# 邊的顏色和粗細
edge_colors = []
edge_widths = []
for u, v in G.edges():
    edge_type = G.edges[u, v].get('type', '')
    if edge_type == 'Pacific_Link':
        edge_colors.append('#00FF00')  # Green Pacific_Link
        edge_widths.append(3)
    elif edge_type == 'Timeline_Evolves':
        edge_colors.append('#888888')  # Gray Timeline
        edge_widths.append(2)
    else:
        edge_colors.append('#CCCCCC')
        edge_widths.append(1)

# 繪製網絡
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=edge_widths, alpha=0.6)
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes,
                       edgecolors=node_edge_colors, linewidths=node_edge_widths, alpha=0.9)

# 標籤（英文）
labels = {node: G.nodes[node].get('label', node) for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_size=8, font_weight='bold')

# 圖例（英文）
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#FF6B6B', markersize=15, label='Community 0: Tech Convergence'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#4ECDC4', markersize=15, label='Community 1: AI/Drone Era'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#45B7D1', markersize=15, label='Community 2: Early Era'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#96CEB4', markersize=15, label='Community 3: Cold War Small Arms'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFD700', markeredgecolor='#333333', markeredgewidth=3, markersize=15, label='Control Group (China/Russia)'),
    Line2D([0], [0], color='#00FF00', linewidth=3, label='Pacific_Link Edges'),
    Line2D([0], [0], color='#888888', linewidth=2, label='Timeline_Evolves Edges'),
]

plt.legend(handles=legend_elements, loc='upper left', fontsize=10)

plt.title(f"DHGA Capstone: US Military Weapons Network Analysis\nModularity Score: {modularity_score:.4f} | {len(set(partition.values()))} Communities", 
         fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

# 保存
plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight', facecolor='white')
print(f"\n✅ Graph saved to: {OUTPUT_PATH}")

plt.close()