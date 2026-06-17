"""
DHGA Capstone — QGIS-style overlay map generator
Date: 2026-06-08
Layered output emulating QGIS Print Layout:
  - Basemap: OpenStreetMap / CartoDB Positron via contextily
  - Layer 1: Supply chain POINTS (color = Category: RawMaterial/Parts/Assembly/Deploy)
  - Layer 2: FLOW LINES connecting source→target (color = flow type: supply/assembly/deploy, width = weight)
  - Legend, north arrow, scale bar, title
Output:
  qgis_screenshots/qgis_overlay_2026-06-08.png (high-res)
  qgis_screenshots/qgis_overlay_2026-06-08_legend.png (legend crop)
"""
import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from shapely.geometry import Point, LineString
import contextily as ctx
import warnings
warnings.filterwarnings("ignore")

BASE = "/home/node/.openclaw/workspace/dhga-weaponhistory"
OUT_DIR = os.path.join(BASE, "qgis_screenshots")
os.makedirs(OUT_DIR, exist_ok=True)

# ---------- Load data ----------
nodes = pd.read_csv(os.path.join(BASE, "enhanced_supply_chain_with_coordinates.csv"))
edges = pd.read_csv(os.path.join(BASE, "supply_chain_edges_georeferenced.csv"))

# Node geometry
gdf_nodes = gpd.GeoDataFrame(
    nodes,
    geometry=gpd.points_from_xy(nodes["Longitude"], nodes["Latitude"]),
    crs="EPSG:4326",
).to_crs(epsg=3857)

# Edge geometry
edges["geometry"] = edges.apply(
    lambda r: LineString([(r["Source_Lon"], r["Source_Lat"]), (r["Target_Lon"], r["Target_Lat"])]),
    axis=1,
)
gdf_edges = gpd.GeoDataFrame(edges, geometry="geometry", crs="EPSG:4326").to_crs(epsg=3857)

# ---------- Color mapping (QGIS-classified style) ----------
CAT_COLOR = {
    "RawMaterial": "#d62728",  # red — raw inputs (high geopolitical sensitivity)
    "Parts":       "#1f77b4",  # blue — components
    "Assembly":    "#2ca02c",  # green — integration sites
    "Deploy":      "#ff7f0e",  # orange — forward deployment
}
FLOW_COLOR = {
    "supply":   "#9467bd",  # purple
    "assembly": "#17becf",  # cyan
    "deploy":   "#8c564b",  # brown
}

# ---------- Plot ----------
fig, ax = plt.subplots(figsize=(18, 11), dpi=140)

# Edges first (under points)
for flow_type, color in FLOW_COLOR.items():
    sub = gdf_edges[gdf_edges["Type"] == flow_type]
    sub.plot(ax=ax, color=color, linewidth=sub["Weight"] * 0.4, alpha=0.55, zorder=2)

# Nodes
for cat, color in CAT_COLOR.items():
    sub = gdf_nodes[gdf_nodes["Category"] == cat]
    sub.plot(ax=ax, color=color, markersize=110, edgecolor="white", linewidth=1.4, marker="o", zorder=3)
    # Label selected key nodes (deploy sites) for QGIS-label-style annotation
    for _, r in sub.iterrows():
        if r["Category"] in ("Deploy", "Assembly"):
            ax.annotate(
                r["Name"].split("/")[1] if "/" in r["Name"] else r["Name"],
                xy=(r.geometry.x, r.geometry.y),
                xytext=(6, 6), textcoords="offset points",
                fontsize=7.5, color="#222", zorder=4,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.75),
            )

# Basemap
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron, alpha=0.85, zorder=1)
ax.set_axis_off()
ax.set_xlim(gdf_nodes.total_bounds[[0, 2]].min() - 2e6, gdf_nodes.total_bounds[[0, 2]].max() + 2e6)
ax.set_ylim(gdf_nodes.total_bounds[[1, 3]].min() - 1.5e6, gdf_nodes.total_bounds[[1, 3]].max() + 1.5e6)

# Title block
ax.set_title(
    "DHGA Capstone — QGIS Overlay: 1776–2026 US Weapons Supply-Chain Geography\n"
    "Layers: OSM Positron basemap • Supply-chain POIs (4 categories) • Flow edges (3 types, weight-scaled)",
    fontsize=13, weight="bold", pad=14,
)

# ---------- Legend ----------
node_handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor=c, markersize=11,
                       markeredgecolor="white", label=k) for k, c in CAT_COLOR.items()]
edge_handles = [Line2D([0], [0], color=c, linewidth=2.5, alpha=0.7, label=k) for k, c in FLOW_COLOR.items()]
leg1 = ax.legend(handles=node_handles, title="POI Category (point)", loc="lower left",
                 bbox_to_anchor=(0.01, 0.01), framealpha=0.95, fontsize=9, title_fontsize=10)
ax.add_artist(leg1)
ax.legend(handles=edge_handles, title="Flow Type (line, width=weight×0.4)", loc="lower left",
          bbox_to_anchor=(0.01, 0.18), framealpha=0.95, fontsize=9, title_fontsize=10)

# North arrow + scale (QGIS-style)
xlim = ax.get_xlim(); ylim = ax.get_ylim()
ax.annotate("N", xy=(xlim[1] - 1.2e6, ylim[1] - 0.6e6), fontsize=18, ha="center", weight="bold",
            arrowprops=dict(arrowstyle="->", lw=1.5))
scalebar_len = 2000_000  # 2000 km in EPSG:3857 meters
ax.plot([xlim[0] + 0.5e6, xlim[0] + 0.5e6 + scalebar_len], [ylim[0] + 0.5e6, ylim[0] + 0.5e6],
        color="black", lw=3)
ax.text(xlim[0] + 0.5e6 + scalebar_len / 2, ylim[0] + 0.7e6, "2000 km",
        ha="center", fontsize=9, weight="bold")

# Footer / metadata
meta = ("CRS: EPSG:3857 (Web Mercator)  •  Nodes: {n}  •  Edges: {e}\n"
        "Source: enhanced_supply_chain_with_coordinates.csv + supply_chain_edges_georeferenced.csv\n"
        "Generated: 2026-06-08 10:00 UTC  •  DHGA_QGIS_Reminder cron output")
ax.text(0.5, -0.04, meta.format(n=len(gdf_nodes), e=len(gdf_edges)),
        transform=ax.transAxes, ha="center", fontsize=8, color="#444")

out_main = os.path.join(OUT_DIR, "qgis_overlay_2026-06-08.png")
plt.tight_layout()
plt.savefig(out_main, dpi=160, bbox_inches="tight", facecolor="white")
plt.close()
print(f"[OK] Wrote {out_main}")

# ---------- Inset: Indo-Pacific zoom (QGIS overview-map style) ----------
fig2, ax2 = plt.subplots(figsize=(11, 9), dpi=140)
gdf_nodes_indo = gdf_nodes.cx[1.1e7:1.8e7, 1e6:7e6]  # rough Indo-Pacific bbox in 3857
gdf_edges_indo = gdf_edges.cx[1.05e7:1.85e7, 0.5e6:7.5e6]
for flow_type, color in FLOW_COLOR.items():
    sub = gdf_edges_indo[gdf_edges_indo["Type"] == flow_type]
    if not sub.empty:
        sub.plot(ax=ax2, color=color, linewidth=sub["Weight"] * 0.55, alpha=0.6, zorder=2)
for cat, color in CAT_COLOR.items():
    sub = gdf_nodes_indo[gdf_nodes_indo["Category"] == cat]
    if not sub.empty:
        sub.plot(ax=ax2, color=color, markersize=140, edgecolor="white", linewidth=1.5,
                 marker="o", zorder=3)
        for _, r in sub.iterrows():
            ax2.annotate(r["Name"].split("/")[1] if "/" in r["Name"] else r["Name"],
                         xy=(r.geometry.x, r.geometry.y), xytext=(7, 7),
                         textcoords="offset points", fontsize=8, color="#222",
                         bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.8),
                         zorder=4)
ctx.add_basemap(ax2, source=ctx.providers.CartoDB.Positron, alpha=0.9, zorder=1)
ax2.set_axis_off()
ax2.set_title("DHGA Capstone — QGIS Inset: Indo-Pacific Supply & Deployment Detail",
              fontsize=12, weight="bold")
out_inset = os.path.join(OUT_DIR, "qgis_overlay_2026-06-08_indo_pacific_inset.png")
plt.tight_layout()
plt.savefig(out_inset, dpi=160, bbox_inches="tight", facecolor="white")
plt.close()
print(f"[OK] Wrote {out_inset}")

print("DONE.")
