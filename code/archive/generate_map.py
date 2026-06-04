#!/usr/bin/env python3
import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import numpy as np

# Read nodes
nodes = {}
with open('enhanced_supply_chain_with_coordinates.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        nodes[row['Name']] = {
            'lon': float(row['Longitude']),
            'lat': float(row['Latitude']),
            'type': row['Type'],
            'category': row['Category']
        }

# Read edges
edges = []
with open('supply_chain_edges_georeferenced.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        edges.append({
            'source': row['Source'],
            'target': row['Target'],
            'weight': int(row['Weight']),
            'type': row['Type'],
            'source_lon': float(row['Source_Lon']),
            'source_lat': float(row['Source_Lat']),
            'target_lon': float(row['Target_Lon']),
            'target_lat': float(row['Target_Lat'])
        })

# Color mapping
type_colors = {
    'RawMaterial': '#e74c3c',   # Red
    'Parts': '#3498db',          # Blue
    'Assembly': '#2ecc71',       # Green
    'Deploy': '#9b59b6',        # Purple
}

edge_colors = {
    'supply': '#e74c3c',
    'assembly': '#3498db',
    'deploy': '#2ecc71',
}

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(20, 12))

# Set background color (ocean)
ax.set_facecolor('#ecf0f1')

# Draw edges
for edge in edges:
    color = edge_colors.get(edge['type'], '#7f8c8d')
    weight = edge['weight']
    alpha = 0.3 + (weight / 20) * 0.5
    width = weight / 3
    
    ax.annotate('', 
        xy=(edge['target_lon'], edge['target_lat']), 
        xytext=(edge['source_lon'], edge['source_lat']),
        arrowprops=dict(arrowstyle='->', color=color, lw=width, alpha=alpha, 
                       connectionstyle='arc3,rad=0.1'))
    
    # Draw line
    ax.plot([edge['source_lon'], edge['target_lon']], 
            [edge['source_lat'], edge['target_lat']], 
            color=color, linewidth=width, alpha=alpha * 0.7, zorder=1)

# Draw nodes
for name, node in nodes.items():
    color = type_colors.get(node['category'], '#7f8c8d')
    marker = 's' if 'Assembly' in node['type'] else ('^' if 'Deploy' in node['type'] else 'o')
    size = 200 if 'Deploy' in node['type'] else (150 if 'Assembly' in node['type'] else 100)
    
    ax.scatter(node['lon'], node['lat'], c=color, s=size, marker=marker, 
               edgecolors='white', linewidths=2, zorder=5)
    
    # Add label for important nodes
    if any(x in name for x in ['US-', 'Japan', 'China', 'Guam', 'Okinawa']):
        ax.annotate(name.split('/')[0], (node['lon'], node['lat']), 
                   fontsize=7, ha='left', va='bottom', color='#2c3e50',
                   fontweight='bold', zorder=6)

# Set limits
ax.set_xlim(-180, 180)
ax.set_ylim(-60, 80)

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.3)
ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)

# Title
ax.set_title('US Military Weapons Supply Chain - Global Asia Georeference Map\n1776 Flintlock to 2026 AI Weapons', 
            fontsize=16, fontweight='bold', pad=20)

# Legend
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#e74c3c', markersize=12, label='Raw Materials'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#3498db', markersize=12, label='Parts'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor='#2ecc71', markersize=12, label='Assembly'),
    Line2D([0], [0], marker='^', color='w', markerfacecolor='#9b59b6', markersize=12, label='Deploy'),
    Line2D([0], [0], color='#e74c3c', lw=2, label='Supply Chain'),
    Line2D([0], [0], color='#2ecc71', lw=2, label='Deployment'),
]

ax.legend(handles=legend_elements, loc='lower left', fontsize=10)

# Add Pacific annotation
ax.annotate('🌏 Pacific Ocean', xy=(160, 0), fontsize=14, color='#34495e', 
            fontweight='bold', ha='center', style='italic')

plt.tight_layout()
plt.savefig('supply_chain_map.png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("Map saved: supply_chain_map.png")
