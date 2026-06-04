#!/usr/bin/env python3
"""
DHGA Month 2 Gephi CSV Enhancer
- Adds data_quality column to nodes and edges
- Adds symbolic Pacific edges (US_Export_to_Asia)
- Output: weapons_gephi_month2_enhanced.csv
"""

import csv
import os

VAULT_DIR = "/home/node/.openclaw/workspace/dhga-weaponhistory"

# ── 1. Load nodes ──────────────────────────────────────────────────────────
nodes_raw = []
nodes_path = os.path.join(VAULT_DIR, "weapons_nodes_month2_3.csv")
with open(nodes_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        nodes_raw.append(row)

# ── 2. Load edges ────────────────────────────────────────────────────────────
edges_raw = []
edges_path = os.path.join(VAULT_DIR, "weapons_gephi_month2_3.csv")
with open(edges_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        edges_raw.append(row)

# ── 3. Assign data_quality to nodes ─────────────────────────────────────────
# Logic:
#   - LoC/NARA documented wars (American Revolution, Civil War, WWI, WWII,
#     Gulf War, War on Terror): verified
#   -冷戰 Cold War era weapons (Korean War, Vietnam War): primary
#   - Near-peer / AI Era (2020+): estimated (no official combat use yet)
#   - All others: estimated

war_quality = {
    "American Revolution":    "verified",
    "Mexican-American War":   "verified",
    "Civil War":              "verified",
    "Spanish-American War":   "verified",
    "WWI":                    "verified",
    "WWII":                   "verified",
    "Korean War":             "primary",
    "Cold War":               "primary",
    "Vietnam War":            "primary",
    "Gulf War":               "verified",
    "War on Terror":          "verified",
    "Near-peer competition":  "estimated",
    "Ukraine War":             "estimated",
    "Global":                 "estimated",
    "AI Era":                 "estimated",
}

def node_quality(year, war):
    # Exact year-based overrides
    if year == 2026:
        return "estimated"
    if war in war_quality:
        return war_quality[war]
    return "estimated"

# ── 4. Build enhanced nodes CSV ─────────────────────────────────────────────
nodes_out = os.path.join(VAULT_DIR, "weapons_nodes_month2_enhanced.csv")
fieldnames_nodes = ["Id", "Label", "Year", "War", "Tech_Key", "data_quality"]

with open(nodes_out, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames_nodes)
    writer.writeheader()
    for row in nodes_raw:
        yr = int(row["Year"])
        war = row["War"].strip()
        dq = node_quality(yr, war)
        writer.writerow({
            "Id":          row["Id"],
            "Label":       row["Label"],
            "Year":        row["Year"],
            "War":         row["War"],
            "Tech_Key":    row["Tech_Key"],
            "data_quality": dq,
        })

print(f"✅ Enhanced nodes → {nodes_out}")

# ── 5. Build enhanced edges CSV ─────────────────────────────────────────────
# data_quality based on edge type
#   Timeline_Evolves = primary (documented tech lineage from primaries)
#   Same_War         = verified (same war, multiple sources)
#   Era_Cluster      = estimated (analytical grouping, not all documented)

edge_quality = {
    "Timeline_Evolves": "primary",
    "Same_War":         "verified",
    "Era_Cluster":      "estimated",
}

# ── 6. Add symbolic Pacific edges ──────────────────────────────────────────
# Virtual edges linking US weapons to Asia-Pacific context
# Format: Source, Target, Weight, Type, data_quality, Pacific_Link

# Key Pacific entry points per era:
# - 1898 Spanish-American War → Philippines → first Pacific foothold
# - WWII → Pacific Theater islands (Guam, Okinawa, Philippines)
# - Korean War → US weapons flow to South Korea
# - Vietnam War → US weapons to South Vietnam, Thailand
# - Near-peer 2020s → Japan, Taiwan, Philippines arms sales

pacific_edges = [
    # (Source nodeId fragment, Target label, Weight, Type, Pacific_Link)
    ("Krag-Jorgensen",    "Pacific_Foothold_1898", 2, "Pacific_Link",    "verified",   "Spanish-American War → Philippines occupation; first major Pacific US base"),
    ("M1918 BAR",         "Pacific_Foothold_1898", 1, "Pacific_Link",    "verified",   "WWII Pacific Theater: Guam, Okinawa, Philippines; heavy weapon deployment"),
    ("M1 Garand",         "Pacific_Theater_WWII",  3, "Pacific_Link",   "primary",    "M1 Garand widespread in Pacific island campaigns; documented in NARA records"),
    ("Atomic Bomb",       "Pacific_Theater_WWII",  2, "Pacific_Link",   "verified",   "Atomic bombings: Hiroshima (6 Aug 1945), Nagasaki (9 Aug 1945) – Pacific dimension of nuclear era"),
    ("M14 Rifle",         "Korean_War_Pacific",    2, "Pacific_Link",   "primary",    "US weapons supplied to South Korean forces; Korean War (1950–53) – first major Cold War Pacific conflict"),
    ("M16 Rifle",         "Vietnam_War_Pacific",   3, "Pacific_Link",   "primary",    "M16 standard issue for US forces in Vietnam; documented LoC NARA service records"),
    ("M1A1 Abrams Tank",  "Indo-Pacific_Modern",   2, "Pacific_Link",   "estimated",  "Abrams exports to Japan, Taiwan; Indo-Pacific strategic alliance hardware"),
    ("F-35 Lightning",    "Indo-Pacific_Modern",   3, "Pacific_Link",   "estimated",  "F-35 deployed to Japan (F-35J), South Korea, Australia; network-centric warfare Pacific"),
    ("Switchblade",       "Ukraine_Pacific_Era",   1, "Pacific_Link",   "estimated",  "Switchblade 600 to Ukraine; similar systems sought by Taiwan, Philippines – drone-era Pacific deterrence"),
    ("LAWS Lethal",       "AI_Pacific_Future",     2, "Pacific_Link",   "estimated",  "LAWS development US-led; Pacific allies (Japan, S.Korea, Australia) reviewing AI weapons ethics – next Pacific arms race"),
]

# We need to map the source Id fragments to actual node Ids
# The node Ids in the CSV are truncated (e.g., "Flintlock Musket (Brown B")
# Build a lookup by checking if node Id STARTS WITH our fragment

def find_node_id(fragment):
    """Find actual node Id that starts with given fragment."""
    for row in nodes_raw:
        if row["Id"].startswith(fragment):
            return row["Id"]
    return None

edges_out = os.path.join(VAULT_DIR, "weapons_gephi_month2_enhanced.csv")
fieldnames_edges = ["Source", "Target", "Weight", "Type", "data_quality", "Pacific_Link"]

with open(edges_out, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames_edges)
    writer.writeheader()

    # Write existing edges with data_quality
    for row in edges_raw:
        edge_type = row["Type"].strip()
        dq = edge_quality.get(edge_type, "estimated")
        writer.writerow({
            "Source":       row["Source"],
            "Target":       row["Target"],
            "Weight":       row["Weight"],
            "Type":         row["Type"],
            "data_quality": dq,
            "Pacific_Link": "",
        })

    # Write symbolic Pacific edges
    for src_frag, tgt_label, weight, etype, dq, plink in pacific_edges:
        src_id = find_node_id(src_frag)
        if src_id:
            writer.writerow({
                "Source":       src_id,
                "Target":       tgt_label,
                "Weight":       weight,
                "Type":         etype,
                "data_quality": dq,
                "Pacific_Link": plink,
            })
        else:
            print(f"⚠️  Warning: could not match node fragment '{src_frag}'")

print(f"✅ Enhanced edges (+ {len(pacific_edges)} Pacific edges) → {edges_out}")

# ── 7. Summary stats ────────────────────────────────────────────────────────
print(f"\n📊 Summary:")
print(f"   Nodes: {len(nodes_raw)} original → enhanced with data_quality")
print(f"   Edges: {len(edges_raw)} original + {len(pacific_edges)} Pacific = {len(edges_raw)+len(pacific_edges)} total")
print(f"   Edge types added: Pacific_Link (symbolic, labelled 'estimated'/'verified'/'primary')")
