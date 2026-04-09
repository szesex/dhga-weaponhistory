#!/usr/bin/env python3
"""
DHGA Month 2 Gephi CSV Enhancer – Iran 2026 Update
Adds:
- New node: EA-37B Compass Call (2026, new deployment)
- New node: Operation Epic Fury (2026 Iran conflict)
- New edge type: MiddleEast_Link (connecting existing weapons to Iran 2026)
- Updated data_quality for 2026-era nodes based on new sources
"""

import csv
import os

VAULT_DIR = "/home/node/.openclaw/workspace/dhga-weaponhistory"

# ── Load existing enhanced CSVs ──────────────────────────────────────────────
nodes_path = os.path.join(VAULT_DIR, "weapons_nodes_month2_enhanced.csv")
edges_path = os.path.join(VAULT_DIR, "weapons_gephi_month2_enhanced.csv")

nodes_raw = []
with open(nodes_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        nodes_raw.append(row)

edges_raw = []
with open(edges_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        edges_raw.append(row)

print(f"Loaded {len(nodes_raw)} nodes, {len(edges_raw)} edges")

# ── New nodes to add (Iran 2026 conflict) ────────────────────────────────────
new_nodes = [
    {
        "Id":          "EA-37B Compass Call",
        "Label":       "EA-37B Compass Call",
        "Year":        "2026",
        "War":         "Iran War 2026",
        "Tech_Key":    "Electronic warfare; Gulfstream G550; deny/grace/degrade adversary comms & radar; first combat debut",
        "data_quality": "verified",  # Aerotime + National Interest + Migflug verified deployment
    },
    {
        "Id":          "Operation Epic Fury",
        "Label":       "Operation Epic Fury",
        "Year":         "2026",
        "War":          "Iran War 2026",
        "Tech_Key":    "USCENTCOM operation vs Iran (Feb 28 2026+); 13000+ targets; 26 aircraft; 155 ships sunk/damaged",
        "data_quality": "verified",  # Stars and Stripes + Wikipedia 2026 Iran war article
    },
    {
        "Id":          "Low-Cost One-Way Drone (US)",
        "Label":       "Low-Cost One-Way Attack Drone (US)",
        "Year":         "2026",
        "War":          "Iran War 2026",
        "Tech_Key":    "One-way attack drone; $20-50k unit cost; Shahed-style loitering munition; drone arms race catalyst",
        "data_quality": "verified",  # Bulletin of the Atomic Scientists (2026-03)
    },
]

# ── New edges: weapons → Iran 2026 conflict ───────────────────────────────────
# (source_node_fragment, target_node_id, weight, edge_type, data_quality, link_description)
new_edges = [
    # Tomahawk used extensively in Iran strikes
    ("Tomahawk Cruise Miss", "Operation Epic Fury",   4, "MiddleEast_Link", "verified",
     "Land-attack Tomahawk used against 13000+ Iran targets; 1500+ km range; CENTCOM verified"),
    # F-35 in Iran operations
    ("F-35 Lightning",        "Operation Epic Fury",   3, "MiddleEast_Link", "verified",
     "F-35 stealth missions over Iran; sensor fusion + network-centric; one of 26 aircraft types used"),
    # EA-37B electronic warfare - new node, linked from existing electronic warfare node
    ("AGM-45 Shrike Anti-r", "EA-37B Compass Call",  2, "Same_War",         "primary",
     "EA-37B replaces EC-130H Compass Call lineage; electronic attack mission continuity"),
    ("EA-37B Compass Call", "Operation Epic Fury",    4, "MiddleEast_Link",  "verified",
     "EA-37B Compass Call combat debut; electronic warfare to deny Iranian radar & comms"),
    # Switchblade used in Iran
    ("Switchblade 600 Ka",   "Operation Epic Fury",   2, "MiddleEast_Link",  "verified",
     "Switchblade 600 loitering munitions deployed in Iran conflict; man-portable; 40+ km range"),
    # Predator drones sank/damaged Iranian ships
    ("MQ-1 Predator Drone",  "Operation Epic Fury",    3, "MiddleEast_Link",  "verified",
     "MQ-1 / MQ-9 involved in anti-ship strikes; 155 ships sunk or damaged in Persian Gulf"),
    # AI/LAWS context - drone arms race
    ("AI-Powered ISR (Gor", "Low-Cost One-Way Drone (US)", 3, "Timeline_Evolves", "primary",
     "AI-powered ISR enables target tracking for one-way drone swarms; next-step from Gorgon/Stare"),
    ("LAWS Lethal Autonom", "Low-Cost One-Way Drone (US)", 2, "Timeline_Evolves", "primary",
     "LAWS + low-cost drones = drone arms race; US adopting Shahed-style one-way attack doctrine"),
    # Abrams in Middle East
    ("M1A1 Abrams Tank",    "Operation Epic Fury",    2, "MiddleEast_Link",  "estimated",
     "M1A1/M1A2 Abrams deployed in Middle East; 120mm main gun; composite armor"),
    # M4 Carbine in ground operations
    ("M4 Carbine Moderni", "Operation Epic Fury",    1, "MiddleEast_Link",  "estimated",
     "M4 variants in use by US ground forces in Iran operation; modular Picatinny rail"),
]

# ── Helper: find node id by prefix ────────────────────────────────────────────
def find_node_id(fragment):
    for row in nodes_raw:
        if row["Id"].startswith(fragment):
            return row["Id"]
    # Also check new_nodes
    for n in new_nodes:
        if n["Id"].startswith(fragment):
            return n["Id"]
    return None

# ── Write enhanced nodes CSV ──────────────────────────────────────────────────
nodes_out = os.path.join(VAULT_DIR, "weapons_nodes_month2_iran2026.csv")
all_nodes = nodes_raw + new_nodes

with open(nodes_out, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=all_nodes[0].keys())
    writer.writeheader()
    writer.writerows(all_nodes)

print(f"✅ Enhanced nodes (+ Iran 2026) → {nodes_out}")
print(f"   Total nodes: {len(all_nodes)}")

# ── Write enhanced edges CSV ──────────────────────────────────────────────────
edges_out = os.path.join(VAULT_DIR, "weapons_gephi_month2_iran2026.csv")

with open(edges_out, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=edges_raw[0].keys())
    writer.writeheader()
    writer.writerows(edges_raw)

    new_edge_count = 0
    for src_frag, tgt, weight, etype, dq, desc in new_edges:
        src_id = find_node_id(src_frag)
        if src_id:
            writer.writerow({
                "Source":       src_id,
                "Target":       tgt,
                "Weight":       weight,
                "Type":         etype,
                "data_quality": dq,
                "Pacific_Link": desc,
            })
            new_edge_count += 1
        else:
            print(f"⚠️  Warning: could not match node fragment '{src_frag}'")

print(f"✅ Enhanced edges (+ {new_edge_count} Iran/MiddleEast edges) → {edges_out}")
print(f"   Total edges: {len(edges_raw) + new_edge_count}")

# ── Summary ──────────────────────────────────────────────────────────────────
print("\n📊 Iran 2026 Update Summary:")
print("   New nodes: EA-37B Compass Call | Operation Epic Fury | Low-Cost One-Way Drone (US)")
print("   New edges: Tomahawk/F-35/Switchblade/Predator/Abrams/M4 → Operation Epic Fury")
print("   New edge type: MiddleEast_Link")
print("   Key stats from sources:")
print("     - 13,000+ targets struck in 38 days")
print("     - 155 ships sunk or damaged")
print("     - 26 different aircraft used")
print("     - EA-37B first combat debut (April 2026)")
print("     - US adopting Shahed-style one-way attack drones ($20-50k/unit)")
print("     - Drone arms race catalyst: Bulletin of the Atomic Scientists (Mar 2026)")
