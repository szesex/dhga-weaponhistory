import folium
import pandas as pd
from folium import plugins

# ============================================================
# Load data
# ============================================================
supply_df = pd.read_csv('/home/node/.openclaw/workspace/dhga-weaponhistory/supply_chain_edges_georeferenced.csv')
ai_df = pd.read_csv('/home/node/.openclaw/workspace/dhga-weaponhistory/ai_weapons_layer.csv')

# ============================================================
# Create map centered on Pacific
# ============================================================
m = folium.Map(location=[35, 140], zoom_start=3, tiles='cartodbpositron')

# ============================================================
# Layer 1: Original Supply Chain (non-AI)
# ============================================================
def get_color(link_type):
    t = str(link_type).lower()
    if 'supply' in t:
        return '#2ecc71'  # green
    elif 'assembly' in t:
        return '#e67e22'  # orange
    elif 'deploy' in t:
        return '#9b59b6'  # purple
    return '#e74c3c'     # red

# Draw supply chain edges
for _, row in supply_df.iterrows():
    if pd.notna(row['Source_Lon']) and pd.notna(row['Target_Lon']):
        folium.PolyLine(
            locations=[[row['Source_Lat'], row['Source_Lon']], [row['Target_Lat'], row['Target_Lon']]],
            weight=2,
            color=get_color(row.get('Type', 'supply')),
            opacity=0.6,
            popup=f"{row['Source']} → {row['Target']} ({row.get('Type','')})"
        ).add_to(m)

# Draw supply chain nodes
node_set = set()
for _, row in supply_df.iterrows():
    for lon_key, lat_key, name_key in [('Source_Lon','Source_Lat','Source'), ('Target_Lon','Target_Lat','Target')]:
        if pd.notna(row[lon_key]):
            node_key = (row[lon_key], row[lat_key])
            if node_key not in node_set:
                node_set.add(node_key)
                folium.CircleMarker(
                    location=[row[lat_key], row[lon_key]],
                    radius=5,
                    popup=row[name_key],
                    color='#3498db',
                    fill=True,
                    fillColor='#3498db',
                    fillOpacity=0.7
                ).add_to(m)

print(f"✅ Supply chain layer: {len(node_set)} nodes, {len(supply_df)} edges")

# ============================================================
# Layer 2: AI Weapons Layer
# ============================================================
ai_colors = {
    'ai_chip': '#ff6b6b',      # red - AI chips
    'ai_memory': '#ffd93d',     # yellow - HBM memory
    'ai_fabrication': '#6bcb77', # green - TSMC fab
    'ai_deploy': '#4d96ff',     # blue - deployment
}

ai_node_set = set()

for _, row in ai_df.iterrows():
    if pd.notna(row['Source_Lon']) and pd.notna(row['Target_Lon']):
        link_type = str(row.get('Type', 'ai_chip')).lower()
        color = ai_colors.get(link_type, '#ff6b6b')
        
        # Draw AI edge
        folium.PolyLine(
            locations=[[row['Source_Lat'], row['Source_Lon']], [row['Target_Lat'], row['Target_Lon']]],
            weight=4,
            color=color,
            opacity=0.9,
            popup=f"🤖 {row['Source']} → {row['Target']} ({link_type})"
        ).add_to(m)
        
        # Draw source node
        src_key = (row['Source_Lon'], row['Source_Lat'])
        if src_key not in ai_node_set:
            ai_node_set.add(src_key)
            folium.CircleMarker(
                location=[row['Source_Lat'], row['Source_Lon']],
                radius=8,
                popup=f"🤖 {row['Source']}",
                color=color,
                fill=True,
                fillColor=color,
                fillOpacity=0.8
            ).add_to(m)
        
        # Draw target node
        tgt_key = (row['Target_Lon'], row['Target_Lat'])
        if tgt_key not in ai_node_set:
            ai_node_set.add(tgt_key)
            folium.CircleMarker(
                location=[row['Target_Lat'], row['Target_Lon']],
                radius=8,
                popup=f"🎯 {row['Target']}",
                color=color,
                fill=True,
                fillColor=color,
                fillOpacity=0.8
            ).add_to(m)

print(f"✅ AI weapons layer: {len(ai_node_set)} nodes, {len(ai_df)} edges")

# ============================================================
# Layer 3: 1776 Revolutionary War Battlefields
# ============================================================
revolutionary_battlefields = [
    {"name": "West Point", "lat": 41.3870, "lon": -73.9580, "note": "1776-1781 關鍵要塞"},
    {"name": "Yorktown", "lat": 37.2370, "lon": -76.5090, "note": "1781年 康沃利斯投降"},
    {"name": "Boston", "lat": 42.3601, "lon": -71.0589, "note": "1770 Boston Massacre"},
]
for b in revolutionary_battlefields:
    folium.Marker(
        location=[b["lat"], b["lon"]],
        popup=f"⚔️ {b['name']} (1776 Revolutionary War)<br>{b['note']}",
        icon=folium.Icon(color="red", icon="star")
    ).add_to(m)

# ============================================================
# Layer 4: WWII Pacific Battlefields
# ============================================================
pacific_battlefields = [
    {"name": "Iwo Jima", "lat": 24.75, "lon": 141.3, "note": "1945.2-3 硫磺島"},
    {"name": "Okinawa", "lat": 26.5018, "lon": 127.678, "note": "1945.4-6 沖繩戰役"},
    {"name": "Guadalcanal", "lat": -9.43, "lon": 159.95, "note": "1942.8-1943.2 瓜島"},
]
for b in pacific_battlefields:
    folium.Marker(
        location=[b["lat"], b["lon"]],
        popup=f"💥 {b['name']} (WWII Pacific)<br>{b['note']}",
        icon=folium.Icon(color="purple", icon="star")
    ).add_to(m)

# ============================================================
# Layer 5: AI Era Deployment Markers (NEW)
# ============================================================
ai_deployment_sites = [
    {"name": "Alaska AI Command", "lat": 61.2180, "lon": -149.9000, "note": "AI作戰中心 - 北美防空"},
    {"name": "Hawaii AI Hub", "lat": 21.3069, "lon": -157.8260, "note": "Pacific AI樞紐"},
    {"name": "Yokosuka AI Base", "lat": 35.3228, "lon": 139.6386, "note": "Japan AI部署 - 橫須賀"},
    {"name": "Guam AI Station", "lat": 13.4443, "lon": 144.7937, "note": "Pacific AI前哨 - 關島"},
    {"name": "Okinawa AI Point", "lat": 26.5018, "lon": 127.6780, "note": "AI定點打擊 - 沖繩"},
]
for site in ai_deployment_sites:
    folium.Marker(
        location=[site["lat"], site["lon"]],
        popup=f"🤖 {site['name']} (AI Era)<br>{site['note']}",
        icon=folium.Icon(color="blue", icon="cog", prefix='fa')
    ).add_to(m)

# ============================================================
# Legend
# ============================================================
legend_html = '''
<div style="position: fixed; bottom: 50px; left: 50px; z-index: 1000; background: white; padding: 15px; border-radius: 8px; box-shadow: 0 0 15px rgba(0,0,0,0.3); font-family: Arial, sans-serif; font-size: 12px;">
<b>🗺️ 美國軍武供應鏈 1776-2026</b><br><br>
<b>傳統供應鏈：</b><br>
<span style="color:#2ecc71;">●</span> 原材料/零件 Supply<br>
<span style="color:#e67e22;">●</span> 組裝 Assembly<br>
<span style="color:#9b59b6;">●</span> 部署 Deploy<br><br>
<b>🤖 AI武器層：</b><br>
<span style="color:#ff6b6b;">●</span> AI芯片 (H100/MI300/TPU)<br>
<span style="color:#ffd93d;">●</span> HBM記憶體 (三星/SK/美光)<br>
<span style="color:#6bcb77;">●</span> AI代工 (台積電3nm)<br>
<span style="color:#4d96ff;">●</span> AI部署<br><br>
<b>⚔️ 戰場：</b><br>
<span style="color:red;">★</span> 1776革命戰場<br>
<span style="color:purple;">★</span> WWII Pacific<br>
<span style="color:blue;">⚙</span> AI Era部署點
</div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

# ============================================================
# Save
# ============================================================
output_path = '/home/node/.openclaw/workspace/dhga-weaponhistory/supply_chain_ai_weapons.html'
m.save(output_path)
print(f"\n✅ AI Weapons Layer map saved: {output_path}")
print(f"   Total nodes: {len(node_set) + len(ai_node_set)}")
print(f"   Total edges: {len(supply_df) + len(ai_df)}")