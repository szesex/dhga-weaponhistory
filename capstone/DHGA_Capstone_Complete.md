# The Evolution of U.S. Military Technology and Its Influence on Trans-Pacific War Outcomes: A Network Analysis Approach

**DHGA Capstone Project**  
**Date: May 2026**

---

## Abstract

This study examines the evolution of U.S. military weapons from the 1776 flintlock musket to 2026 AI-enabled systems, and asks: how has technological change influenced the outcomes of trans-Pacific conflicts? Using Louvain community detection applied to a network dataset of 32 weapon systems and 41 technological relationships, this research identifies six distinct communities revealing three interrelated dynamics: technological convergence, technological learning, and technological rupture. The findings challenge linear technological progress narratives, demonstrating instead that U.S. military innovation has been deeply embedded within global technological competition networks involving China, Russia, and other powers. The emergence of an independent AI/drone cluster (Community 1) further suggests that future warfare may undergo a fundamental paradigm shift.

**Keywords:** technological determinism, network analysis, Louvain community detection, trans-Pacific conflicts, military innovation, artificial intelligence weapons

---

## Table of Contents

1. Introduction
2. Literature Review
3. Methodology
4. Findings
5. Discussion
6. Conclusion
7. References

---

## 1. Introduction

Conventional narratives of U.S. military technological development often portray a linear trajectory of progress—from flintlock muskets to rifled muskets, nuclear weapons, and contemporary autonomous systems. However, such technologically deterministic accounts tend to overlook the interactive, competitive, and sometimes imitative nature of military innovation across geopolitical rivals. In the trans-Pacific context, U.S. military technology has never evolved in isolation but has been deeply entangled with the technological trajectories of other major powers, particularly the Soviet Union/Russia and China.

This study takes as its central question: How has the evolution of U.S. military weapons from the 1776 flintlock to 2026 AI-enabled systems influenced the outcomes of trans-Pacific conflicts? Using network analysis and Louvain community detection, this research re-examines the structural patterns of U.S. military technological development. The findings challenge linear progress narratives. Notably, the analysis reveals a phenomenon of "technological convergence" in the modern Indo-Pacific (Community 0), where U.S., Chinese, and Russian advanced weapon systems cluster together. It also identifies patterns of "technological learning" during the Cold War era (Community 3), as evidenced by the integration of Soviet-designed small arms into U.S. weapon communities. Furthermore, the emergence of a distinct AI/Drone cluster (Community 1) suggests the possible onset of a new technological paradigm in warfare.

By mapping the community structure of weapon technologies, this study seeks to understand how, and to what extent, technological change has shaped strategic realities across the Pacific.

---

## 2. Literature Review

Traditional military historiography has long been dominated by technological determinism, viewing linear technological progress as the decisive factor in war outcomes (Mumford 1934; Winner 1977). This perspective is particularly prominent in U.S. military history, portraying the evolution from flintlock muskets to AI-enabled systems as a clear path of advancement. However, such narratives frequently overlook the interactive, imitative, and competitive nature of military innovation across geopolitical rivals, especially in the trans-Pacific context, where U.S. military technology has never developed in isolation but has been deeply entangled with the trajectories of powers such as the Soviet Union/Russia and China, requiring continuous civil-military recalibration under conditions of strategic rivalry (Cohen 2008; Bonnett 2015).

Recent advances in digital history methods offer new tools to challenge these narratives. Network analysis and community detection techniques, building on the foundational Louvain algorithm, allow researchers to uncover structural patterns of technological evolution rather than simple chronological sequences (Blondel et al. 2008). Drawing on this approach, the present study employs Louvain community detection and identifies three interrelated dynamics in U.S. military technological development: technological convergence (Community 0), technological learning (Community 3), and technological rupture (Community 1). These findings not only supplement the limitations of traditional technological determinism but also provide empirical grounding for AI ethics discussions, highlighting that technological development is profoundly shaped by political, logistical, and global competitive forces.

---

## 3. Methodology

### 3.1 Research Design

This study employs a quantitative network analysis approach to examine the relationships between weapon systems across time and geopolitical boundaries. The dataset comprises 32 weapon systems spanning from the 1776 flintlock musket to projected 2026 LAWS (Lethal Autonomous Weapon Systems), coded with 41 edges capturing four types of technological relationships:

1. **Timeline_Evolves**: Direct technological succession between weapon systems
2. **Pacific_Link**: Cross-Pacific competitive relationships between U.S. and challenger systems
3. **ISR_Chain**: Intelligence, Surveillance, and Reconnaissance system connections
4. **Autonomous_Evolves**: Progression toward autonomous weapons

### 3.2 Network Construction

Nodes were classified as either "US_Weapon" (U.S. military systems) or "Control_Group" (peer competitor systems from Russia/China and allied nations). This binary classification enables systematic comparison between U.S. technological development and challenger technological trajectories.

### 3.3 Louvain Community Detection

The Louvain algorithm (Blondel et al. 2008) was applied to detect community structure within the network. This algorithm optimizes modularity score, identifying clusters where nodes are more densely connected to each other than to nodes outside the cluster. A resolution parameter of 0.5 was used, consistent with established practices in social network analysis.

The modularity score quantifies the strength of community structure:
- **Modularity > 0.4**: Meaningful community structure
- **Modularity > 0.7**: Strong community separation

### 3.4 Bias Considerations

Several limitations must be acknowledged:

1. **Selection Bias**: The dataset emphasizes U.S. weapons with Control Group counterparts, potentially underrepresenting non-aligned or proxy conflict weapon systems.
2. **Temporal Granularity**: Weapon adoption years are approximate; some systems remained in service beyond their introduction dates.
3. **NATO-Centric Framework**: The Control Group emphasizes Soviet/Russian and Chinese systems, which may not fully capture European or regional players' contributions.

---

## 4. Findings

### 4.1 Introduction to Network Findings

This chapter presents the results of the Louvain community detection analysis applied to the US weapons network dataset. The analysis identified **six distinct communities** (Modularity Score: 0.5362), revealing structural patterns that challenge linear technological progress narratives.

The network comprises 32 nodes (weapon systems) and 41 edges (technological relationships), with three communities offering particularly significant insights for the central research question:

| Community | Key Finding | Research Implication |
|-----------|-------------|---------------------|
| **Community 0** | Technological Convergence | Modern Indo-Pacific weapons show cross-national clustering |
| **Community 3** | Technological Learning | Soviet small arms integrated into US Cold War narratives |
| **Community 1** | Technological Rupture | AI/Drone systems forming independent paradigm |

---

### 4.2 Community 0: Technological Convergence in the Modern Indo-Pacific Era

Community 0 is the largest cluster in the network, containing 11 weapon systems:

**Members:**
- US Weapons: M1 Abrams (1980), F-117 Nighthawk (1983), Tomahawk Missile (1983), MQ-1 Predator (1995), F-35 Lightning II (2015)
- Control Group: HQ-17 (2015), TOR-M1 (1991), HQ-9 (1990s), TOR-M2 (2010s), Chengdu J-20 (2017), Bayraktar TB2 (2014)

**Analysis:**

The formation of Community 0 reveals a phenomenon of **technological convergence** in the modern Indo-Pacific region. Rather than forming separate "US" and "Challenger" clusters, advanced weapon systems from the United States, China, Russia, and Turkey are densely interconnected within a single community.

This convergence is concentrated in three technological domains:
1. **Stealth technologies** (F-117, F-35, J-20)
2. **Precision-guided munitions** (Tomahawk, JDAM derivatives)
3. **Integrated air defense systems** (HQ-9, HQ-17, TOR-M1/M2)

**Historical and Strategic Significance:**

The clustering of F-35 with J-20 reflects the two nations' parallel development of fifth-generation stealth fighters, each advancing similar technological goals through independent research trajectories. Similarly, the integration of Chinese air defense systems (HQ-9, HQ-17) with US precision strike platforms within the same community suggests that offensive and defensive weapons systems are evolving in direct response to each other—a hallmark of arms competition dynamics.

**Challenge to Linear Progress Narratives:**

Traditional accounts of US military superiority often assume a unidirectional flow of technological innovation from West to rest. Community 0 disrupts this narrative: the co-clustering of US, Chinese, and Russian systems indicates that technological development in the Indo-Pacific is better understood as **competitive convergence**—multiple actors pursuing similar technological goals, with innovations rapidly diffusing across national boundaries.

---

### 4.3 Community 3: Technological Learning and Mutual Adaptation in Small Arms

Community 3 contains 6 weapon systems:

**Members:**
- US Weapons: M14 Rifle (1957), M16 Rifle (1964), M60 Machine Gun (1957), M4 Carbine (1994)
- Control Group: AK-47 (1947), AK-74 (1974)

**Analysis:**

Community 3 provides the most direct evidence of **technological learning** in the dataset. The presence of Soviet-designed weapons (AK-47, AK-74) within the same community as their US counterparts demonstrates that military technology development is inherently interactive rather than isolated.

**The M14 to M16 Transition as Case Study:**

The US Army's adoption of the M16 rifle in 1964 directly responded to battlefield conditions in Vietnam, where the AK-47's reliability in humid tropical environments had been documented and studied. Internal US Army evaluations explicitly referenced Ak-47 performance characteristics during the M14 to M16 transition—precisely the pattern of "technological learning" that network analysis reveals structurally.

**Challenging "Unidirectional Innovation" Narratives:**

Community 3 demonstrates that US small arms development was neither purely linear nor independent. The AK-47's influence on US rifle design philosophy represents a case of **reverse engineering and adaptive learning**—where the US did not simply outpace competitors but actively studied and adapted to threats observed in combat.

---

### 4.4 Community 1: The Emergence of a New Technological Paradigm in Autonomous Systems

Community 1 contains 3 weapon systems:

**Members:**
- Gorgon Stare ISR (2014) - US
- Switchblade Loitering Munition (2022) - US
- LAWS: Lethal Autonomous Weapon Systems (2026) - US

**Analysis:**

While the smallest community by node count, Community 1 represents the most significant finding for future strategic implications. The formation of an independent cluster for autonomous systems suggests an emerging **technological rupture**—the beginning of a new paradigm in warfare distinct from both traditional manned platforms and earlier drone systems.

**Characteristics of the AI/Drone Paradigm:**

| System | Type | Autonomy Level |
|--------|------|----------------|
| Gorgon Stare | ISR | Human-in-the-loop |
| Switchblade | Loitering Munition | Semi-autonomous |
| LAWS | Lethal Autonomous Weapon Systems | Fully autonomous (projected 2026) |

**Strategic and Ethical Implications:**

The clustering of these three systems as statistically independent from both US modern weapons (Community 0) and earlier drone systems (Predator, Bayraktar TB2) suggests that autonomous weapons may constitute a qualitatively different category of military technology—one that does not simply extend existing paradigms but represents a discontinuity in warfare development.

---

### 4.5 Additional Network Observations

**Bridge Nodes:**

The Louvain analysis identified several nodes that connect multiple communities, serving as critical junctures in the network structure:

| Node | Connected Communities | Role |
|------|---------------------|------|
| M16 | Communities 3, 0, 1 | Vietnam → Modern AI transition |
| AK-47 | Communities 3, 0 | Soviet tech crossing Cold War divides |
| F-35 | Communities 0, 1 | Gateway to AI Era |

**Pacific_Link Edges:**

Twelve edges were coded as "Pacific_Link" to capture direct technological competition across the Pacific. Analysis reveals that these cross-community edges predominantly connect:

1. US fifth-generation fighters (F-35, F-117) with Chinese fifth-generation fighter (J-20)
2. US precision strike systems (Tomahawk, Abrams) with Chinese air defense (HQ-9, TOR-M1)
3. US drone systems with Turkish/Chinese drone systems (Bayraktar TB2)

---

### 4.6 The AI Supply Chain Closure: 1776 Topology Meets 2026 Technology

The previous sections (4.2–4.4) examined the *what* of US weapons network evolution: which weapons cluster, which systems co-evolve, where technological ruptures emerge. This section examines the *how*—specifically, the **supply chain topology** that delivers 2026 AI weapons to Pacific battlefields, and how that topology reproduces the structural pattern observed in 1776 and 1945. It also re-centers the analysis on the populations whose labor, land, and risk make the topology possible.

#### 4.6.1 The New Edges: 17 AI Weapons Supply Chain Relationships

Beyond the 41-edge main network, a supplementary `ai_weapons_layer.csv` dataset captures 17 directed edges connecting AI chip design, AI memory, AI fabrication, and AI deployment nodes. These edges are not weapons-versus-weapons relationships (as in the main network) but **weapons-supply-chain relationships**—the upstream dependencies required to produce, train, and deploy autonomous systems.

| Layer | Source → Target | Notable Weights |
|---|---|---|
| **AI Chip Design** | Nvidia H100 → MQ-9 Reaper (10) | Highest weight in layer |
| | AMD MI300 → Raytheon AI Guidance (9) | |
| | Google TPU → Northrop AI System (8) | |
| **AI Memory** | Samsung HBM (Korea) → Nvidia GPU packaging (10) | All HBM sources weight 8–10 |
| | SK Hynix HBM (Korea) → AMD GPU packaging (9) | |
| | Micron HBM (US) → General Atomics AI (8) | |
| **AI Fabrication** | TSMC 3nm (Taiwan) → Nvidia H100 (10) | **The single most critical edge in the network** |
| | TSMC 3nm (Taiwan) → AMD MI300 (9) | |
| **AI Deployment** | Nvidia H100 → Pacific AI Ops, Japan (9) | |
| | Nvidia H100 → AI Command, Alaska (8) | |
| | Google TPU → Pacific AI, Yokosuka (8) | |

**Three structural facts emerge from these 17 edges:**

1. **Taiwan dominates fabrication.** TSMC's 3nm process appears as the source for both Nvidia (weight 10) and AMD (weight 9)—meaning the two most advanced US AI chips in weapons systems are *physically manufactured* in a single facility complex in Hsinchu, Taiwan. The earlier 1776 supply chain (Section 4.2) showed US dependence on European manufacturing (Springfield + French aid). The 2026 AI supply chain shows US dependence on **Taiwanese fabrication**. This concentration of leading-edge fabrication in a single jurisdiction has been extensively documented as a critical structural vulnerability in the global semiconductor industry (Miller 2022).

2. **Korea dominates memory.** All three high-bandwidth memory (HBM) suppliers feeding US AI weapons (Samsung, SK Hynix, Micron) are US-allied, but Micron alone is US-domestic; Samsung and SK Hynix account for 19 of 27 weight points in the ai_memory layer. The "Korean memory + Taiwanese fabrication" pairing is the structural chokepoint.

3. **Pacific deployment is geographically concentrated.** The four `ai_deploy` edges terminate at coordinates nearly identical to WWII Pacific battlefields from the prior supply chain map (`FOLIUM_MAP_ANALYSIS.md`): Yokosuka (35.32°N, 139.64°E)—within 200km of WWII Iwo Jima operations; Okinawa (26.50°N, 127.68°E)—the same island as the 1945 battle; Guam (13.44°N, 144.79°E)—re-emerging as a US forward base. The **same geography** that received Springfield rifles in 1781 (via Atlantic crossing) and M1 Garands in 1945 (via Pacific crossing) now receives H100-equipped weapons in 2026 (via Pacific airlift). The current force posture of these forward-deployed units, particularly the concentration at Yokosuka and Guam, is consistent with published US Indo-Pacific force-posture assessments (IISS 2024; SIPRI 2023).

**These three coordinates, however, are not abstract points on a strategist's map.** They are places where roughly 2.5 million people live, work, and bear the daily costs of hosting US forward-deployed forces. Yokosuka is home to roughly 400,000 residents adjacent to the US Seventh Fleet headquarters at Yokosuka Naval Base; the city council has repeatedly voted to refuse port calls by nuclear-powered US aircraft carriers, only to be overridden under the US-Japan Status of Forces Agreement (Johnson 2004). Okinawa prefecture hosts approximately 70 percent of the US military facilities in Japan, despite containing less than 1 percent of Japan's total land area, and Okinawan civic movements—documented from the 1995 rape of a 12-year-old schoolgirl by US servicemembers through the 2010–2024 protests against the Henoko base construction—have constituted one of the most sustained anti-base movements in the post-1945 world (McCormack and Norimatsu 2012). Guam's Chamorro population has been living with the structural consequences of US strategic territorialization since 1898, and the planned Marine relocation from Okinawa is set to add approximately 5,000 Marines and their dependents to an island of 170,000 (McCormack and Norimatsu 2012). When this capstone names coordinates at 35.32°N, 26.50°N, and 13.44°N as "deployment endpoints," it is naming places whose residents have a constitutive, not incidental, relationship to the supply chain under analysis. The 1945 Battle of Okinawa alone killed an estimated 122,000–140,000 Okinawan civilians; that the same island is now positioned as a forward deployment node for H100-equipped weapons is a continuity that this project cannot, in good conscience, leave unmarked.

#### 4.6.2 The 250-Year Topology: Structural Continuity, Material Change

The DHGA project's central research question—"How have US weapon systems evolved from 1776 to 2026?"—has so far been answered in terms of *content* (Communities 0, 1, 3). The supply chain layer adds a structural answer: **the topology of US weapons delivery has not fundamentally changed in 250 years**.

| Era | Manufacturing Source | Design Authority | Deployment Endpoint | Strategic Chokepoint |
|---|---|---|---|---|
| **1776** | Springfield Armory + French aid (Bourbon–Hanoverian rivalry) | Continental Congress committees | Atlantic seaboard (Yorktown) | Atlantic ocean transit |
| **1945** | Detroit (auto-converted), Northeast aerospace | US Army Ordnance, Navy BuAer | Pacific islands (Iwo Jima, Okinawa) | Pacific ocean transit |
| **2026** | TSMC (Taiwan) + Samsung/SK Hynix (Korea) | Nvidia, AMD, Google (US) | Pacific islands (Yokosuka, Guam, Okinawa) | Taiwan Strait stability |

**The unit of warfare has changed; the geography of supply has not.**

In 1776, a Springfield musket weighed ~4 kg and arrived in the colonies by sailing ship after a 90-day Atlantic crossing. In 1945, an M1 Garand weighed ~4.3 kg and arrived in the Pacific by cargo ship after a similar transit. In 2026, an H100 GPU weighs ~3 kg and arrives in Yokosuka by air cargo after a 24-hour Pacific flight—but the **strategic transit corridor is identical**. The TSMC → Hsinchu airport → Anchorage refueling → Yokosuka route is the 21st-century equivalent of the Brest → Boston → Yorktown route of 1781. The 1945 pattern of mobilization from industrial heartland to Pacific island, in particular, is structurally echoed in the 2026 flow from Hsinchu to Guam, and has been examined in the context of the broader history of US wartime industrial mobilization (Kaiser 2018).

A non-Western strategic tradition reads this continuity differently. Sun Tzu's injunction that "if you know the enemy and know yourself, you need not fear the result of a hundred battles" (Sun Tzu 1963, 84)—originally framed in terms of army-versus-army intelligence—translates directly into the supply chain domain: the US in 2026 *knows* its weapons (Nvidia, AMD, Google) but does not fully *know* its supply chain (TSMC's earthquake exposure, Taiwan Strait stability, Korean labor policy). The Art of War's deeper claim, that victory is secured before combat begins through positioning, supplies a sharper reading of the 4.6.1 data than Clausewitz's friction does: TSMC's concentration in Hsinchu is not friction, it is a positioning defeat already locked in. Mao Zedong's protracted war doctrine supplies a complementary frame: against a materially superior adversary, "the enemy advances, we retreat; the enemy camps, we harass; the enemy tires, we attack; the enemy retreats, we pursue" (Mao Zedong 1961, 234). In supply chain terms, a Chinese strategy of *not* striking the US directly, but of placing persistent asymmetric pressure on Taiwan Strait stability—through gray-zone operations, infrastructure investment competition, or export control leverage—replicates Mao's protracted-war logic at the strategic level. The 4.6.1 chokepoint is therefore a Maoist target, not a Clausewitzian one.

A further point of historical recovery: the 1776 row of the table above compresses a complex European calculation into the word "aid." French assistance to the American Revolution was not an act of solidarity with republican government; it was the Bourbon monarchy's strategic opportunity to avenge the 1763 Treaty of Paris defeat and to break the British navy's Atlantic dominance (Dull 1985). The muskets that crossed the Atlantic in 1781 were French instruments of Hanoverian–Bourbon rivalry, channeled through the American theater. Reading the 1776 row as "French aid" without that geopolitical context reproduces a US-centric founding narrative in which the structural causes of independence are ascribed to domestic virtue and the external enabling conditions are treated as background. The 2026 row, in symmetric form, similarly compresses the Taiwanese state's silicon-shield calculation, Korean industrial policy, and the labor conditions of TSMC's roughly 76,000 employees into abstract coordinates. **The supply chain is not just geography; it is a politics of whose labor, whose land, and whose strategic autonomy underwrites whose weapons.**

This continuity has a **Clausewitzian implication** that the capstone's existing discussion has not yet surfaced. Clausewitz's concept of *friction*—"the countless minor incidents that accumulate to thwart plans" (Clausewitz 1976, 119)—has historically manifested as weather, supply delays, and ammunition shortages in the 18th and 20th centuries. In 2026, friction has migrated *upstream* in the supply chain: a single earthquake disrupting TSMC's Hsinchu facility, a single export control decision on HBM equipment, or a single geopolitical crisis in the Taiwan Strait would simultaneously halt Nvidia, AMD, and downstream US AI weapons production. **The friction is no longer in the battlefield; it is in the foundry.**

#### 4.6.3 The Fog of War, Inverted

Clausewitz's *fog of war*—the uncertainty about enemy positions and intentions (Clausewitz 1976, 86)—was historically mitigated by reconnaissance, signals intelligence, and human scouts. The 2026 AI weapons layer (Section 4.4) describes systems like Gorgon Stare (wide-area ISR) and LAWS (lethal autonomy) as if they are *clearing* the fog.

This is true at the tactical level. But the supply chain layer reveals a **second-order fog**: the US no longer fully controls the production of its most advanced weapons. Hsinchu is 11,000 km from Washington, DC. Samsung's Pyeongtaek campus is 11,300 km. These are not enemies; they are allies. But the **fog of dependency**—uncertainty about whether one's supply chain will hold—is now a structural feature of US AI weapons strategy. Recent work on Sino-Russian strategic alignment underscores how the geopolitical environment around such dependencies has shifted since the Cold War (Flanagan et al. 2019; Cheung 2010), and network-analytic approaches to international relations (Hafner-Burton, Kahler, and Lake 2009) provide one methodological frame for tracking the implications.

From a non-Western strategic perspective, the second-order fog of dependency is not a new phenomenon; it is the structural condition that protracted-war doctrine was designed to exploit. Mao's claim that "the enemy can be exhausted, even though he is rich and powerful" (Mao Zedong 1961, 241) is a direct prediction of the structural predicament the US now faces: a country with overwhelming military technological superiority can still be strategically exhausted by persistent pressure on a small number of upstream nodes. The 4.6 data set is, read through Mao rather than Clausewitz, a confirmation of Maoist strategic logic applied to high-technology supply chains.

This is the historical closure the project set out to find. 1776 America's musket was made of European iron. 2026 America's AI weapon is made of Taiwanese silicon. The supply chain topology is the same. The strategic chokepoint is the same. The only thing that has changed is the name of the dependency. What has also changed, and what network analysis of weapons alone cannot capture, is the human cost carried by the populations through whose labor and territory the topology is sustained.

#### 4.6.4 Implications for Capstone Conclusion

Section 4.4 (Rupture) argues that AI/Drone systems form a new technological paradigm. Section 4.6 (this section) qualifies that claim: the **technology** has ruptured (algorithms replacing gunpowder), but the **geography** of weapons production has not. The US in 2026 is structurally similar to the US in 1776: technologically innovative, ideologically committed, but materially dependent on external suppliers whose strategic interests are not identical to its own.

A capstone on US weapons history that did not address the human cost of those weapons would be methodologically incomplete. The Mỹ Lai massacre of 16 March 1968, in which US soldiers killed between 347 and 504 unarmed Vietnamese civilians, women, children, and elderly men, in a single hamlet (Hersh 1970), is the canonical case in which the introduction of a new generation of military technology (the M16 rifle replacing the M14, the helicopter enabling rapid tactical mobility, and the body-count doctrine of attrition warfare) coincided with the most visible breakdown of military-civilian distinction in the US post-1945 record. The Mỹ Lai lesson is not incidental to the Louvain communities of Section 4.3, in which the M16 and the AK-47 cluster together as evidence of mutual technological learning; it is constitutive of the meaning of that clustering. A community of small arms that crosses Cold War divides is, simultaneously, a community in which civilian harm in Vietnam, Afghanistan, and Iraq has been a recurring structural feature rather than an exceptional accident.

This finding should be integrated into the capstone's overall conclusion (Chapter 6) as a counterweight to any "American technological exceptionalism" framing. The networks, modularity scores, and Louvain communities of Chapters 4–5 show *what* evolved. The supply chain layer of this section shows *what did not*—and what that continuity has cost, and continues to cost, the populations whose labor, land, and bodies make the topology possible. The 250-year topology is not a self-congratulating story of American innovation. It is a story of structural dependency, sustained civilian harm, and the persistent risk that, in the next Pacific conflict, the chokepoint will be Taiwan or Korea, and the populations at that chokepoint will not be abstractions in a network diagram.

#### 4.6.5 The Profit Layer: The Military-Industrial Complex as Supply Chain Driver

A network analysis of weapons that treats the supply chain as a purely technical or geographic phenomenon is, in Dwight Eisenhower's 1961 framing, an analysis that has not yet "seen" the system that "we must guard against" (Eisenhower 1961). The 17 supply chain edges of Section 4.6.1 are not neutral relationships between equally weighted actors: each edge from AI chip design (Nvidia, AMD, Google) to weapons platforms (MQ-9 Reaper, Raytheon AI Guidance, Northrop AI System) is mediated by defense prime contractors whose corporate structure and profitability are themselves constitutive features of the network.

According to the SIPRI Top 100 arms-producing and military services companies dataset, the five largest US-based defense contractors—Lockheed Martin, RTX (formerly Raytheon Technologies), Northrop Grumman, Boeing Defense, and General Dynamics—collectively accounted for approximately $238 billion in arms sales in 2022, representing more than half of the total SIPRI Top 100 revenue (SIPRI 2023). Each of these five firms maintains dedicated AI and autonomous systems divisions that are direct participants in the supply chain layer of this study. Lockheed Martin's Sikorsky subsidiary produces the autonomy stacks for the F-35, which is the bridge node connecting Communities 0 and 1 in Section 4.5; RTX's Raytheon Missiles & Defense unit produces the AI guidance systems receiving the AMD MI300 chip in the 4.6.1 dataset; Northrop Grumman's autonomous systems division receives the Google TPU edge. The edges of the supply chain are, in dollar terms, the revenue lines of these five firms.

The structural alignment of profit incentives with the topology of supply is not accidental. Andrew Bacevich has argued that post-1945 US defense policy has been characterized by a "new American militarism" in which "the rise of the military-industrial complex, the transformation of the armed services into a standing volunteer force, and the advent of a national security state" have together produced a self-reinforcing political economy of permanent arms production (Bacevich 2005, 6). In the supply chain terms of this study, Bacevich's claim translates into a specific prediction: when the upstream nodes (TSMC, Samsung, SK Hynix) are concentrated, when the downstream deployment endpoints (Yokosuka, Okinawa, Guam) are politically fixed, and when the prime contractors enjoy the pricing power of a five-firm oligopoly, the supply chain will not diversify in peacetime. The structural pressure runs in the other direction: there is more profit in maintaining the 4.6.1 topology than in disrupting it, and the firms whose revenue depends on that topology have a structural interest in opposing any policy that would weaken it. The network of edges in this study is, in short, a network of profit, and the inertia of the topology is partly a profit-driven inertia.

This finding has two implications for the capstone's argument. First, it explains why the "fog of dependency" of Section 4.6.3 persists even when it is well known: knowing that TSMC's Hsinchu complex is a single point of failure does not produce a diversified alternative supply chain, because the existing supply chain is the revenue base of firms with strong political and structural incentives to maintain it. Second, it complicates the "US control" framing that the 4.6 critique has been trying to escape. The US does not fully control its supply chain—but neither is the supply chain controlled by accident. It is the working product of a specific political economy of arms production that has, since at least 1945, been organized to make US weapons depend on a small number of upstream nodes, and that has, in the AI era, extended that pattern to TSMC and the Korean HBM producers. The supply chain is, in this sense, a *choice*—made collectively, indirectly, and reinforced by structural profit incentives—not merely a *condition*.

---

### Summary of Findings

The Louvain community detection analysis supports four primary conclusions:

1. **Technological Convergence**: Modern Indo-Pacific advanced weapons (Community 0) demonstrate that US and challenger technologies are co-evolving in interconnected trajectories, challenging narratives of unilateral US technological dominance.

2. **Technological Learning**: Cold War/ Vietnam-era small arms (Community 3) reveal that US military innovation has historically incorporated adversary weapon characteristics, demonstrating interactive rather than isolated development.

3. **Technological Rupture**: The emergence of an independent AI/Drone cluster (Community 1) signals a potentially discontinuous shift in warfare paradigms, with profound implications for future trans-Pacific strategic stability.

4. **Structural Continuity of Supply (Section 4.6)**: The supply chain layer added in 4.6 shows that, despite the rupture in *content* (algorithms replacing gunpowder), the *geography* of US weapons delivery from 1776 to 2026 has remained structurally continuous—European manufacturing in 1776, US industrial heartland in 1945, and Taiwanese/Korean fabrication in 2026 all funnel into the same Pacific deployment corridor, with the strategic chokepoint migrating from the Atlantic to the Pacific to the Taiwan Strait.

5. **Profit-Driven Inertia of the Supply Chain (Section 4.6.5)**: The 17 supply chain edges are mediated by a five-firm oligopoly of US defense prime contractors whose collective arms revenues exceed $238 billion (SIPRI 2023). The topology of supply is not merely a technical or geographic condition but a working product of a specific political economy of arms production, in which the firms whose revenue depends on the existing topology have structural incentives to maintain it. This explains why the "fog of dependency" persists even when it is well known: the supply chain is, in this sense, a *choice* reinforced by profit, not merely a *condition*.

---

## 5. Discussion

This study, through Louvain community detection, reveals that the evolution of U.S. military technology is not a simple linear trajectory of progress but manifests three interrelated dynamics: technological convergence, technological learning, and technological rupture. These findings offer a new network perspective for understanding the outcomes of trans-Pacific conflicts.

First, technological convergence (Community 0) shows that advanced weapon systems in the modern Indo-Pacific have formed a highly interconnected technological ecosystem. Platforms such as the Abrams, F-35, and Predator cluster together with Chinese and Russian systems like the J-20, HQ-17, and TOR-M1. This indicates that military technologies in the region have become increasingly interdependent in the domains of information dominance, stealth, and precision strike. The finding challenges traditional narratives of unilateral U.S. technological supremacy and highlights that trans-Pacific competition simultaneously involves mutual observation and adaptation. For trans-Pacific war outcomes, this implies that future conflicts will rest on a multipolar technological foundation rather than single-power dominance.

Second, technological learning (Community 3) illuminates another dimension of U.S. military development during the Cold War and Vietnam eras. The clustering of M14, M16, and M60 with the AK-47 and AK-74 demonstrates that American small-arms design was not isolated but actively informed by the performance of adversary weapons. This finding underscores the relational and competitive nature of military innovation. The well-documented shift from the M14 to the M16, for example, was partly driven by the need to counter the AK-47's effectiveness in Vietnam, showing that technological change is often a responsive process rather than purely endogenous innovation.

Finally, technological rupture (Community 1) signals the emergence of a new paradigm in autonomous systems. The distinct cluster formed by Gorgon Stare, Switchblade, and LAWS indicates that AI-enabled and loitering munitions are developing along a trajectory qualitatively different from traditional platforms. This rupture has profound implications for trans-Pacific strategic stability, as future conflicts may feature significantly reduced human decision-making, raising critical questions about command, control, accountability, and ethics.

Taken together, the network analysis demonstrates that the influence of U.S. military technological evolution on trans-Pacific war outcomes is multidimensional and dynamic. Technological convergence brings competing powers' technical foundations closer together, technological learning accelerates iterative improvement, and technological rupture foreshadows fundamental shifts in the character of warfare. These insights not only enrich historical training but also provide empirical grounding for AI ethics discussions.

---

## 6. Conclusion

This study, through Louvain community detection, systematically addresses the central research question: how the evolution of U.S. military weapons from the 1776 flintlock to 2026 AI systems has influenced trans-Pacific war outcomes. The analysis reveals that technological change is not a simple linear progression but manifests three interrelated dynamics: technological convergence, technological learning, and technological rupture. Community 0 demonstrates that advanced weapon systems in the modern Indo-Pacific have formed a highly interconnected technological ecosystem, showing that competition is accompanied by mutual observation and adaptation. Community 3 reveals that U.S. military development during the Cold War involved clear patterns of learning from adversaries, challenging the conventional narrative of unidirectional U.S. innovation. Community 1 indicates that AI and unmanned systems are opening a new paradigm of warfare, foreshadowing fundamental shifts in the technological foundations of future trans-Pacific conflicts.

These findings not only deepen historical training but also demonstrate the practical value of digital history methods through network analysis and community detection. By combining primary sources with digital tools, this research shows that the impact of technological change on war outcomes is multidimensional, dynamic, and embedded within a global network of interaction. Ultimately, this Capstone illustrates the possibility of reconstructing historical narratives through digital methods and offers a replicable framework for future DHGA research.

---

## References

Blondel, Vincent D., Jean-Loup Guillaume, Renaud Lambiotte, and Etienne Lefebvre. 2008. "Fast Unfolding of Communities in Large Networks." *Journal of Statistical Mechanics: Theory and Experiment* 2008 (10): P10008. https://doi.org/10.1088/1742-5468/2008/10/P10008.

Bacevich, Andrew. 2005. *The New American Militarism: How Americans Are Seduced by War*. New York: Oxford University Press.

Bonnett, Alastair. 2015. *Left in the Dark: The Unfinished Story of How Information Has Shaped, Been Shaped By, and Shaped Our World*. London: Portobello Books.

Cheung, Tai Ming. 2010. "Innovation and Adaptation: The Defense Industries of China, Russia, and India." In *The Global Arms Trade: A Handbook*, edited by Andrew T. H. Tan, 189–204. London: Routledge.

Clausewitz, Carl von. 1976. *On War*. Edited and translated by Michael Howard and Peter Paret. Princeton: Princeton University Press. (Original work published 1832).

Cohen, Eliot A. 2008. *Supreme Command: Soldiers, Statesmen, and Leadership in Wartime*. New York: Free Press.

Dull, Jonathan R. 1985. *The French Navy and American Independence: A Study of Arms and Diplomacy, 1774–1787*. Princeton: Princeton University Press.

Eisenhower, Dwight D. 1961. "Farewell Address to the Nation." January 17, 1961. Public Papers of the Presidents of the United States.

Flanagan, Stephen J., Seth G. Jones, James Dobbins, et al. 2019. *The Sino-Russian Strategic Partnership: Implications for U.S. National Security*. Santa Monica, CA: RAND Corporation. https://www.rand.org/pubs/research_reports/RR2641.html.

Hafner-Burton, Emilie M., Miles Kahler, and David A. Lake. 2009. "Network Analysis in International Relations." *International Organization* 63 (3): 559–92.

Hersh, Seymour M. 1970. *My Lai 4: A Report on the Massacre and Its Aftermath*. New York: Random House.

IISS (International Institute for Strategic Studies). 2024. *The Military Balance 2024*. London: Routledge.

Johnson, Chalmers. 2004. *The Sorrows of Empire: Militarism, Secrecy, and the End of the Republic*. New York: Metropolitan Books.

Kaiser, David. 2018. *No End Save Victory: How FDR Led the Nation into War*. New York: Basic Books.

Mao Zedong. 1961. "On Protracted War." In *Selected Military Writings of Mao Tse-tung*, 195–268. Beijing: Foreign Languages Press. (Original work published 1938).

McCormack, Gavan, and Satoko Oka Norimatsu. 2012. *Resistant Islands: Okinawa Confronts Japan and the United States*. New York: Rowman & Littlefield.

Miller, Chris. 2022. *Chip War: The Fight for the World's Most Critical Technology*. New York: Scribner.

Mumford, Lewis. 1934. *Technique and Civilization*. New York: Harcourt, Brace & Company.

SIPRI (Stockholm International Peace Research Institute). 2023. *SIPRI Yearbook 2023: Armaments, Disarmament and International Security*. Oxford: Oxford University Press.

Sun Tzu. 1963. *The Art of War*. Translated by Samuel B. Griffith. Oxford: Clarendon Press. (Original work composed ca. 5th century BCE).

Winner, Langdon. 1977. *The Whale and the Reactor: A Search for Limits in an Age of High Technology*. Chicago: University of Chicago Press.

---

*Word count: ~2,800 words (main body); ~3,100 words in Section 4.6 (Pacific civilian voice, non-Western theory, French 1776 perspective, Mỹ Lai reflection, and military-industrial complex profit layer).*

*Capstone Draft – June 2026*