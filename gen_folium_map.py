import folium
import pandas as pd
from folium import plugins

# 1. Load the edge CSV
df = pd.read_csv('/home/node/.openclaw/workspace/dhga-weaponhistory/supply_chain_edges_georeferenced.csv')

# 2. Create map centered on Pacific
m = folium.Map(location=[35, 140], zoom_start=3, tiles='cartodbpositron')

# 3. Draw supply chain lines
for _, row in df.iterrows():
    if pd.notna(row['Source_Lon']) and pd.notna(row['Target_Lon']):
        link_type = str(row.get('Type', 'supply')).lower()
        if 'supply' in link_type:
            color = '#2ecc71'
        elif 'assembly' in link_type:
            color = '#e67e22'
        else:
            color = '#e74c3c'
        
        folium.PolyLine(
            locations=[[row['Source_Lat'], row['Source_Lon']], [row['Target_Lat'], row['Target_Lon']]],
            weight=3,
            color=color,
            popup=f"{row['Source']} → {row['Target']}"
        ).add_to(m)

# 4. Draw nodes
node_set = set()
for _, row in df.iterrows():
    if pd.notna(row['Source_Lon']):
        node_key = (row['Source_Lon'], row['Source_Lat'])
        if node_key not in node_set:
            node_set.add(node_key)
            folium.CircleMarker(
                location=[row['Source_Lat'], row['Source_Lon']],
                radius=6,
                popup=row['Source'],
                color='#3498db',
                fill=True
            ).add_to(m)
    if pd.notna(row['Target_Lon']):
        node_key = (row['Target_Lon'], row['Target_Lat'])
        if node_key not in node_set:
            node_set.add(node_key)
            folium.CircleMarker(
                location=[row['Target_Lat'], row['Target_Lon']],
                radius=6,
                popup=row['Target'],
                color='#3498db',
                fill=True
            ).add_to(m)

# 5. Overlay 1776 Revolutionary War battlefields
revolutionary_battlefields = [
    {"name": "West Point", "lat": 41.3870, "lon": -73.9580},
    {"name": "Yorktown", "lat": 37.2370, "lon": -76.5090},
    {"name": "Boston", "lat": 42.3601, "lon": -71.0589},
]
for b in revolutionary_battlefields:
    folium.Marker(
        location=[b["lat"], b["lon"]],
        popup=f"⚔️ {b['name']} (1776)",
        icon=folium.Icon(color="red", icon="star")
    ).add_to(m)

# 6. Overlay Pacific island battlefields
pacific_battlefields = [
    {"name": "Iwo Jima", "lat": 24.75, "lon": 141.3},
    {"name": "Okinawa", "lat": 26.5018, "lon": 127.678},
    {"name": "Guadalcanal", "lat": -9.43, "lon": 159.95},
]
for b in pacific_battlefields:
    folium.Marker(
        location=[b["lat"], b["lon"]],
        popup=f"💥 {b['name']} (WWII Pacific)",
        icon=folium.Icon(color="purple", icon="star")
    ).add_to(m)

# 7. Save HTML
m.save('/home/node/.openclaw/workspace/dhga-weaponhistory/supply_chain_folium.html')
print("✅ Folium map saved to supply_chain_folium.html")
print(f"   Nodes plotted: {len(node_set)}")
print(f"   Edges plotted: {len(df)}")