#!/usr/bin/env python3
"""
US Military Weapons Timeline: 1776-2026
DHGA Project | Digital History Methods
"""

TIMELINE = [
    (1776, "Flintlock Musket (Brown Bess)", "American Revolution", "Smoothbore muzzle-loading; 50-100 yards range"),
    (1783, "Flintlock Pistol & Cavalry Carbines", "American Revolution", "Cavalry weapon specialization begins"),
    (1846, "Springfield Model 1841 Rifle", "Mexican-American War", "First widespread rifled musket adoption"),
    (1861, "Rifled Musket (Springfield/Enfield)", "Civil War", "Minié ball ammo; 300+ yards effective range"),
    (1861, "Gatling Gun Model 1861", "Civil War", "First recoil-operated machine gun"),
    (1863, "Ironclad Warships", "Civil War", "Steam-powered ironclads debut"),
    (1898, "Krag-Jorgensen & M1893 Springfield", "Spanish-American War", "Magazine-fed rifles; 5-round capacity"),
    (1917, "M1917 Enfield / M1903 Springfield", "WWI", "Massive production; trench warfare dominates"),
    (1918, "M1918 BAR", "WWI", "First portable automatic rifle; 20-round magazine"),
    (1941, "M1 Garand", "WWII", "Semi-automatic; standard US Army issue"),
    (1942, "M3 Grease Gun Submachine Gun", "WWII", ".45 ACP; cheap mass production"),
    (1944, "M1 Carbine", "WWII", "Lightweight; paratrooper & support troops"),
    (1945, "Atomic Bomb", "WWII", "Nuclear weapons era; strategic bombing"),
    (1950, "M14 Rifle", "Korean War", "7.62mm NATO; selective fire capability"),
    (1952, "Hydrogen Bomb", "Cold War", "Thermonuclear weapons; megaton yield"),
    (1964, "M16 Rifle", "Vietnam War", "5.56mm NATO; plastic stock; lightweight"),
    (1967, "M60 General Purpose Machine Gun", "Vietnam War", "7.62mm; belt-fed; 600-700 rpm"),
    (1970, "AGM-45 Shrike Anti-radiation Missile", "Vietnam War", "First operationally successful anti-radiation missile"),
    (1991, "M1A1 Abrams Tank", "Gulf War", "120mm gun; composite armor; thermal sight"),
    (1991, "F-117 Nighthawk Stealth Aircraft", "Gulf War", "First stealth aircraft; precision bombing"),
    (1991, "Tomahawk Cruise Missile", "Gulf War", "Land-attack cruise missile; 1500+ km range"),
    (2001, "MQ-1 Predator Drone", "War on Terror", "UAV for ISR & strike; Hellfire missiles"),
    (2003, "M4 Carbine Modernized", "War on Terror", "Modular; picatinny rail; fully automatic"),
    (2020, "F-35 Lightning II Block 4", "Near-peer competition", "Stealth + sensor fusion; network-centric warfare"),
    (2022, "Switchblade 600 Kamikaze Drone", "Ukraine War", "Loitering munition; man-portable; 40+ km range"),
    (2024, "AI-Powered ISR (Gorgon/Stare)", "Global", "Computer vision; multiple drone tracking"),
    (2026, "LAWS Lethal Autonomous Weapon Systems", "AI Era", "AI selects & engages targets; no human in loop"),
]

# Gephi CSV Generation
def generate_gephi_csv():
    csv = "Source,Target,Weight,Type\n"
    for i in range(len(TIMELINE)-1):
        _, weapon_a, war_a, _ = TIMELINE[i]
        _, weapon_b, war_b, _ = TIMELINE[i+1]
        csv += f"{weapon_a[:20]},{weapon_b[:20]},1,Evolves\n"
    return csv

if __name__ == "__main__":
    print("=== US Military Weapons Timeline: 1776-2026 ===\n")
    for year, weapon, war, tech in TIMELINE:
        print(f"[{year}] {weapon}")
        print(f"  War: {war} | Tech: {tech}\n")
    
    csv = generate_gephi_csv()
    with open("/home/node/.openclaw/workspace/dhga-weaponhistory/weapons_timeline.csv", "w") as f:
        f.write(csv)
    print("✅ Gephi CSV saved")
    print(f"📊 Total: {len(TIMELINE)} nodes, {len(TIMELINE)-1} edges")
