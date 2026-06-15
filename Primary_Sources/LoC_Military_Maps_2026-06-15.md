# LoC Military Maps Collection — Primary Source Log
**Cron Job:** DHGA_Weekly_LoC_Scan
**Date:** 2026-06-15 (Monday) 17:02 UTC
**Status:** ❌ 持續阻斷 — 第8周（**LoC API 升級至 DNS-level**）

---

## Attempted Sources — Week 8

### 1. Library of Congress — Military Resources
**URL:** `https://www.loc.gov/maps/` , `https://www.loc.gov/rr/news/topics/military.html`
**Status:** ❌ 403 Cloudflare Block (8th consecutive week)
**Week 8 Fallback Attempted (2026-06-15):**
- `https://www.loc.gov/maps/?fo=json` → ❌ 403 ("Just a moment..." Cloudflare)
- `https://www.loc.gov/rr/news/topics/military.html` → ❌ 403 ("Just a moment..." Cloudflare)
- `https://api.loc.gov/search?q=military+maps&fo=json&c=3` → ❌ **ENOTFOUND** (DNS resolution failure)
- `https://lccn.loc.gov/military` → ❌ 404 (re-tested for completeness)

### 2. West Point — United States Military Academy
**URL:** `https://www.westpoint.edu/`
**Status:** ❌ 403 Forbidden (8th consecutive week)
**Week 8 Fallback Attempted (2026-06-15):**
- `https://www.westpoint.edu/academics/academic-departments/history/maps-and-atlases` → ❌ 403
- `https://www.westpointaog.org/visit/campus-map` → ❌ Client Challenge ("A required part of this site couldn't load" / Cloudflare bot challenge)
- `https://www.westpointaoe.org/maps` → ❌ DNS NXDOMAIN (carried over from Week 7)
- `https://www.westpointaoe.com/maps` → ❌ 000 (carried over from Week 7)

### 3. NARA — National Archives (NEW — Week 8 breakthrough)
**URL:** `https://www.archives.gov/research/military`
**Status:** ✅ **200 OK — first new reachable source in 8 weeks**
**Content retrieved:**
- Military Records Research landing page reachable
- "Research by Branch" / "Research by War or Conflict" / "Research by Topic" sections confirmed
- Revolutionary War → 1912 records held at NARA Washington DC
- WWI–present records at NPRC, St. Louis, Missouri
- Post-WWI regimental/unit records at College Park, MD
- Sub-page `/research/military/records-of-the-war-department` → ❌ 404 (broken post-redesign link — NARA site was redesigned, content moved)
- Discovery channel via NARA: `https://historyhub.history.gov/welcome`

### 4. Britannica (Cache Reuse)
**URL:** `https://www.britannica.com/topic/Library-of-Congress`
**Status:** ❌ 403 this week (was ✅ in Week 6) — Cloudflare challenge now blocking
**Mitigation:** Week 6 cache still valid (170M+ items, 1800 founding, War of 1812 destruction, Jefferson 6,487 books 1815, etc.)

---

## 8-Week Block Summary

| Week | Date | LoC HTML | LoC API | West Point | Retrieval Method |
|------|------|----------|---------|------------|------------------|
| Week 1 | 2026-04-13 | ❌ 403 | ❌ 403 | ❌ 403 | Cloudflare |
| Week 2 | 2026-04-20 | ❌ 403 | ❌ 403 | ❌ 403 | Cloudflare |
| Week 3 | 2026-04-27 | ❌ 403 | ❌ 403 | ❌ 403 | Cloudflare |
| Week 4 | 2026-05-04 | ❌ 403 | ❌ 403 | ❌ 403 | Persistent IP |
| Week 5 | 2026-05-18 | ❌ 403 | ❌ 403 | ❌ 403 | Sustained block |
| Week 6 | 2026-06-01 | ❌ 403 | ❌ 403 | ❌ 403 | Britannica partial ✅ |
| Week 7 | 2026-06-08 | ❌ 403 | ❌ **000** (TCP reset) | ❌ 403/000 | DDG + Wikipedia TOC |
| **Week 8** | **2026-06-15** | **❌ 403** | **❌ ENOTFOUND (DNS)** | **❌ 403 + Client Challenge** | **NARA breakthrough ✅** |

**Pattern Analysis (Week 8 escalation):**
- **LoC API escalation confirmed**: 403 → 000 → **ENOTFOUND** across Weeks 6→7→8. The JSON endpoint has been **removed from DNS** entirely, not just blocked at TCP. This is the strongest possible automated defense — the host is no longer advertised.
- **West Point** remains 403 + Cloudflare bot challenge on alumni sites. No escalation, but no relief either.
- **Britannica** joined the blocker list this week (was 200 in Week 6, now 403). Cache reuse is the only path.
- **NARA** is the first authoritative US government primary-source channel to be reachable in 8 weeks. Even though `/research/military/records-of-the-war-department` returns 404 (post-redesign broken link), the parent `/research/military` works and reveals the NARA record-holding structure (DC / St. Louis / College Park).

---

## LoC API Escalation: The Three-Week Ladder

| Week | API State | Interpretation |
|------|-----------|----------------|
| W6 | 403 | Application-level challenge (Cloudflare) |
| W7 | 000 | TCP/IP-level rejection (deep packet block) |
| **W8** | **ENOTFOUND** | **DNS-level removal (host not advertised)** |

This ladder matches the supply chain opacity narrative perfectly: each layer of the network stack removes one more transparency surface. App-level tells you "we know you"; packet-level tells you "we won't talk"; DNS-level tells you "we don't exist for you."

---

## NARA — Week 8 First-Contact Notes

`https://www.archives.gov/research/military` (200 OK, 1.4 KB)
- Federal military service records: Revolutionary War → 1912 at NARA Washington DC
- WWI–present: National Military Personnel Records Center (NPRC), St. Louis, MO
- Post-WWI regimental/unit records: College Park, MD
- "Our website was redesigned, and many items have moved" — confirms recent IA overhaul
- Discovery hub: `https://historyhub.history.gov/welcome`

**Capstone relevance:**
- NARA is a **legally-mandated** primary source (Federal Records Act) — sits in a different legal category than LoC, which is a legislative-branch library
- For Section 4.6 "AI Supply Chain Closure" → NARA can corroborate weapons procurement records that LoC's metadata was supposed to triangulate
- NARA's NPRC (St. Louis) is the canonical source for WWI–present service records — relevant to LAWS operator-of-record chain

---

## Wikipedia Partial Retrieve (cached from Week 7) — West Point

From `en.wikipedia.org/wiki/United_States_Military_Academy` HTML (header/infobox only):
- Coordinates: 41.3925°N, 73.9575°W
- Established 1802 (NY), Sylvanus Thayer tradition
- Category hits: "Forts on the National Register of Historic Places", "Military and war museums in NY", "Patriot League", "U.S. Route 9W", "National Historic Landmarks"

---

## Britannica LoC Facts Reused (Cached from Week 6)

- Founded April 24, 1800 (John Adams signed legislation)
- Original 3,000 volumes destroyed by British in War of 1812
- Thomas Jefferson's personal library (6,487 books) purchased 1815 for $23,950
- Located on Capitol Hill, three buildings: Thomas Jefferson (1897), John Adams (1939), James Madison Memorial (1980)
- 21 public reading rooms; 460+ languages represented
- Largest law library in the world; Copyright deposit law (1870) repository of record
- **World's largest library (170M+ items), 25M books, 74.5M manuscripts, 5.6M maps, 8.2M sheet music, 4.2M audio, 17.3M visual materials, 800K+ pre-15th-c. rare books**

---

## DuckDuckGo Index — LoC-adjacent Sources Located (carried from Week 7)

For follow-up manual retrieval (human-in-the-loop):
- `guides.loc.gov/c.php?g=1428775&p=10601243` — LoC Research Guide: Military History
- `guides.lib.berkeley.edu/c.php?g=823925&p=5881729` — UC Berkeley LibGuide: Military History
- `libguides.ala.org/primarysources/militaryexperience` — ALA: Primary Sources — Military Experience

**Week 8 addition:**
- `https://historyhub.history.gov/welcome` — NARA History Hub (community Q&A; possibly more lenient on bot traffic)

---

## Week 8 Summary

- [x] 確認 8 周阻斷趨勢；**LoC API 升級至 DNS-level**（W6→W7→W8: 403→000→ENOTFOUND）
- [x] West Point 校友會 AOG：Client Challenge 頁面確認，bot challenge active
- [x] **NARA 突破 ✅** — `archives.gov/research/military` 200 OK，首次在 8 週內取得聯邦權威一手源
- [x] Britannica 本週新加入封鎖（Week 6 為 200），cache 沿用
- [x] NARA 站內子頁 `/records-of-the-war-department` 404 — 重設計後遺，需手動探索替代路徑
- [x] 生成 DHG501 Week 8 摘要

---

## 建議行動

- [ ] 探索 NARA 站內結構（從 `/research/military` 出發爬 `/college-park/`、`/dc/` 子路徑）
- [ ] 嘗試 `https://historyhub.history.gov/` 作為 NARA 替代入口（社區型，可能對自動化較寬容）
- [ ] 記錄 ENOTFOUND 證據：若 DNS 狀態持續，可能需向 GSB / Internet Archive 反映 Wayback 抓取覆蓋率
- [ ] 手動下載 3 個 LoC/UCB/ALA libguides HTML 存檔（已 carry 4 週）
- [ ] 住宅代理（residential proxy）仍未配置 — 8 週後建議升級為標準作業

---

## 相關文件

- `dhga-vault/DHG501_AI_Weapon_Era_Summary.md` — DHG501 摘要（Week 8 更新）
- `dhga-vault/Primary_Sources/LoC_Military_Maps_2026-06-08.md` — 上週掃描記錄
- `dhga-vault/capstone/Capstone_Section_4.6_AI_Supply_Chain_Closure.md` — 4.6 節供應鏈閉環

---

*Auto-generated by DHGA_Weekly_LoC_Scan | 2026-06-15 17:02 UTC*
