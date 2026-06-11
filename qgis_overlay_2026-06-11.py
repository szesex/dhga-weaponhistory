"""
DHGA Capstone — QGIS-style overlay map generator (Pacific civilian-pressure lens)
Date: 2026-06-11
Layered output emulating QGIS Print Layout:
  - Basemap: CartoDB Positron via contextily
  - Layer 1: Supply chain POINTS (color = Category)
  - Layer 2: FLOW LINES connecting source→target (color = flow type, width = weight)
  - Layer 3: Pacific civilian-pressure lens — semi-transparent annotation boxes
            keyed to Section 4.6.1 (Yokosuka, Okinawa, Guam, TSMC Hsinchu,
            Jeju, ROK, Mariana) — connects supply-chain geography to
            civilian-impact narrative.
Output:
  qgis_screenshots/qgis_overlay_2026-06-11.png (global, refreshed)
  qgis_screenshots/qgis_overlay_2026-06-11_pacific_lens.png (NEW — Pacific civilian lens)
  qgis_screenshots/qgis_overlay_2026-06-11_indo_pacific_inset.png (Indo-Pacific, refreshed)
"""
import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch
from shapely.geometry import Point, LineString
import contextily as ctx
import warnings
warnings.filterwarnings("ignore")

BASE = "/home/node/.openclaw/workspace/dhga-weaponhistory"
OUT_DIR = os.path.join(BASE, "qgis_screenshots")
os.makedirs(OUT_DIR, exist_ok=True)
DATE = "2026-06-11"

# ---------- Load data ----------
nodes = pd.read_csv(os.path.join(BASE, "enhanced_supply_chain_with_coordinates.csv"))
edges = pd.read_csv(os.path.join(BASE, "supply_chain_edges_georeferenced.csv"))

gdf_nodes = gpd.GeoDataFrame(
    nodes,
    geometry=gpd.points_from_xy(nodes["Longitude"], nodes["Latitude"]),
    crs="EPSG:4326",
).to_crs(epsg=3857)

edges["geometry"] = edges.apply(
    lambda r: LineString([(r["Source_Lon"], r["Source_Lat"]), (r["Target_Lon"], r["Target_Lat"])]),
    axis=1,
)
gdf_edges = gpd.GeoDataFrame(edges, geometry="geometry", crs="EPSG:4326").to_crs(epsg=3857)

CAT_COLOR = {
    "RawMaterial": "#d62728",
    "Parts":       "#1f77b4",
    "Assembly":    "#2ca02c",
    "Deploy":      "#ff7f0e",
}
FLOW_COLOR = {
    "supply":   "#9467bd",
    "assembly": "#17becf",
    "deploy":   "#8c564b",
}

# Pacific civilian-pressure markers — keyed to Capstone Section 4.6.1
# (lon, lat, label, narrative_anchor)
PACIFIC_LENS = [
    (139.668, 35.286, "Yokosuka",      "US 7th Fleet HQ\ncivilian port-city\n(4.6.1 Pacific voice)"),
    (127.679, 26.213, "Okinawa",       "Futenma / 1995 rape\nincident, 2010\nrelocation crisis"),
    (144.794, 13.444, "Guam (Chamorro)","US strategic hub;\nindigenous sovereignty\nmovement"),
    (120.969, 24.804, "Hsinchu (TSMC)","76k employees;\nTaiwan Strait\nexposure to blockade"),
    (126.497, 33.499, "Jeju (ROK)",    "Naval base protest\n2011–2016;\nGangjeong village"),
    (145.751, 15.184, "Mariana Trench","Aegis Ashore\nTHAAD radar\ndeployment"),
    (127.730, -8.409, "Timor-Leste",   "Post-colonial;\nNDF/Ramos-Horta\nnon-alignment"),
]

def _common_layers(ax, title, footer_suffix=""):
    """Edges + nodes + basemap shared between figures."""
    for flow_type, color in FLOW_COLOR.items():
        sub = gdf_edges[gdf_edges["Type"] == flow_type]
        sub.plot(ax=ax, color=color, linewidth=sub["Weight"] * 0.4, alpha=0.55, zorder=2)
    for cat, color in CAT_COLOR.items():
        sub = gdf_nodes[gdf_nodes["Category"] == cat]
        sub.plot(ax=ax, color=color, markersize=110, edgecolor="white",
                 linewidth=1.4, marker="o", zorder=3)
    ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron, alpha=0.85, zorder=1)
    ax.set_axis_off()
    ax.set_title(title, fontsize=13, weight="bold", pad=14)

    node_handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor=c,
                           markersize=11, markeredgecolor="white", label=k)
                    for k, c in CAT_COLOR.items()]
    edge_handles = [Line2D([0], [0], color=c, linewidth=2.5, alpha=0.7, label=k)
                    for k, c in FLOW_COLOR.items()]
    leg1 = ax.legend(handles=node_handles, title="POI Category",
                     loc="lower left", bbox_to_anchor=(0.01, 0.01),
                     framealpha=0.95, fontsize=9, title_fontsize=10)
    ax.add_artist(leg1)
    ax.legend(handles=edge_handles, title="Flow (width=weight×0.4)",
              loc="lower left", bbox_to_anchor=(0.01, 0.18),
              framealpha=0.95, fontsize=9, title_fontsize=10)

    xlim = ax.get_xlim(); ylim = ax.get_ylim()
    ax.annotate("N", xy=(xlim[1] - 1.2e6, ylim[1] - 0.6e6),
                fontsize=18, ha="center", weight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.5))
    sb = 2_000_000
    ax.plot([xlim[0] + 0.5e6, xlim[0] + 0.5e6 + sb],
            [ylim[0] + 0.5e6, ylim[0] + 0.5e6], color="black", lw=3)
    ax.text(xlim[0] + 0.5e6 + sb / 2, ylim[0] + 0.7e6, "2000 km",
            ha="center", fontsize=9, weight="bold")

    meta = (f"CRS: EPSG:3857  •  Nodes: {len(gdf_nodes)}  •  Edges: {len(gdf_edges)}\n"
            f"Generated: {DATE} 10:00 UTC  •  DHGA_QGIS_Reminder cron output{footer_suffix}")
    ax.text(0.5, -0.04, meta, transform=ax.transAxes, ha="center", fontsize=8, color="#444")

# ---------- Fig 1: global (refreshed 2026-06-11) ----------
fig, ax = plt.subplots(figsize=(18, 11), dpi=140)
_common_layers(ax,
    "DHGA Capstone — QGIS Overlay: 1776–2026 US Weapons Supply-Chain Geography\n"
    "Layers: OSM Positron basemap • Supply-chain POIs (4 categories) • Flow edges (3 types, weight-scaled)")
out_main = os.path.join(OUT_DIR, f"qgis_overlay_{DATE}.png")
plt.tight_layout()
plt.savefig(out_main, dpi=160, bbox_inches="tight", facecolor="white")
plt.close()
print(f"[OK] Wrote {out_main}")

# ---------- Fig 2: NEW — Pacific civilian-pressure lens ----------
fig2, ax2 = plt.subplots(figsize=(18, 11), dpi=140)
_common_layers(ax2,
    "DHGA Capstone — Pacific Civilian-Pressure Lens (Section 4.6.1)\n"
    "Supply-chain nodes overlaid with civilian-voice sites: Yokosuka, Okinawa, Guam, TSMC Hsinchu, Jeju, Mariana, Timor-Leste",
    footer_suffix="\nLens anchored to Capstone Section 4.6.1 (Pacific civilian voice)")

# Pacific lens annotation boxes (projected to 3857)
import pyproj
to_3857 = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True).transform
for lon, lat, label, narrative in PACIFIC_LENS:
    x, y = to_3857(lon, lat)
    # Soft yellow semi-transparent bbox
    ax2.add_patch(FancyBboxPatch(
        (x - 1.4e5, y - 1.0e5), 2.8e5, 2.0e5,
        boxstyle="round,pad=0.3",
        linewidth=1.2, edgecolor="#cc6600", facecolor="#ffe7b3", alpha=0.55, zorder=5,
    ))
    ax2.plot(x, y, marker="*", markersize=18, color="#cc6600",
             markeredgecolor="white", markeredgewidth=1.2, zorder=6)
    ax2.annotate(f"{label}\n{narrative}",
                 xy=(x, y), xytext=(x + 1.8e5, y + 1.4e5),
                 fontsize=7.5, color="#5a3a00",
                 bbox=dict(boxstyle="round,pad=0.3", fc="#fff4d6",
                           ec="#cc6600", alpha=0.92, lw=0.8),
                 arrowprops=dict(arrowstyle="->", color="#cc6600", lw=0.8),
                 zorder=7)

# Pacific legend
pac_handle = [Line2D([0], [0], marker="*", color="w", markerfacecolor="#cc6600",
                     markersize=14, markeredgecolor="white", label="Civilian-voice site (4.6.1)")]
leg_pac = ax2.legend(handles=pac_handle, title="Section 4.6.1 lens",
                     loc="lower right", bbox_to_anchor=(0.32, 0.01),
                     framealpha=0.95, fontsize=9, title_fontsize=10)
ax2.add_artist(leg_pac)

out_lens = os.path.join(OUT_DIR, f"qgis_overlay_{DATE}_pacific_lens.png")
plt.tight_layout()
plt.savefig(out_lens, dpi=160, bbox_inches="tight", facecolor="white")
plt.close()
print(f"[OK] Wrote {out_lens}")

# ---------- Fig 3: Indo-Pacific inset (refreshed 2026-06-11) ----------
fig3, ax3 = plt.subplots(figsize=(11, 9), dpi=140)
gdf_nodes_indo = gdf_nodes.cx[1.1e7:1.8e7, 1e6:7e6]
gdf_edges_indo = gdf_edges.cx[1.05e7:1.85e7, 0.5e6:7.5e6]
for flow_type, color in FLOW_COLOR.items():
    sub = gdf_edges_indo[gdf_edges_indo["Type"] == flow_type]
    if not sub.empty:
        sub.plot(ax=ax3, color=color, linewidth=sub["Weight"] * 0.55, alpha=0.6, zorder=2)
for cat, color in CAT_COLOR.items():
    sub = gdf_nodes_indo[gdf_nodes_indo["Category"] == cat]
    if not sub.empty:
        sub.plot(ax=ax3, color=color, markersize=140, edgecolor="white",
                 linewidth=1.5, marker="o", zorder=3)
ctx.add_basemap(ax3, source=ctx.providers.CartoDB.Positron, alpha=0.9, zorder=1)
ax3.set_axis_off()
ax3.set_title("DHGA Capstone — QGIS Inset: Indo-Pacific Supply & Deployment Detail",
              fontsize=12, weight="bold")
out_inset = os.path.join(OUT_DIR, f"qgis_overlay_{DATE}_indo_pacific_inset.png")
plt.tight_layout()
plt.savefig(out_inset, dpi=160, bbox_inches="tight", facecolor="white")
plt.close()
print(f"[OK] Wrote {out_inset}")

print("DONE.")
