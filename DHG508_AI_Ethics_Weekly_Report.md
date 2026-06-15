# DHG508 AI倫理 × 內容偏見審視報告
**Cron Job:** DHGA_AI_Ethics — 每週五 15:00 UTC
**Date:** 2026-06-15 (Week 10, Month 4 整合期) — 補跑
**Status:** ✅ 例行檢查完成
**Latest Snapshot:** [[DHG508_Week10_Report.md]] · Previous: [[DHG508_Week9_Report.md]]

---

## 📋 本週內容盤點（2026-05-29 → 2026-06-05）

| 提交 | 性質 | 偏見審視焦點 |
|------|------|-------------|
| **Capstone 4.6「AI Supply Chain Closure」** (7967dff) | 重大分析章節 | 美中台半導體依賴 vs 美系武器主軸 |
| **AI weapons layer map** (f4a2b45) | 17 邊 / 16 節點 視覺化 | TSMC + Samsung HBM 數據呈現 |
| **DHGA_Capstone_Month_4.md** (2026-06-01) | 月度 capstone | 6 社群 / 0.5362 modularity |
| **5df8bff capstone consistency review** | 倉內清理 | 操作性，無分析偏見 |
| **413b348 submodule cleanup + Jekyll 關閉** | 基建 | 操作性 |
| **Vault backups (06-01/02/03/04)** | 同步操作 | 操作性 |

**本週重點審視：Capstone 4.6 + Month 4 capstone**——兩者係 250 年論證嘅兩塊最後拼圖。

---

## 🔍 本週偏見審視三維度

### 1️⃣ 敘事框架偏見（Narrative Framing Bias）

#### ✅ 本週有進步嘅地方
- **Capstone 4.6.1** 明確指出 TSMC 3nm 同 Samsung/SK Hynix HBM 係 2026 美系 AI 武器嘅**結構性單點故障**——呢個係項目入面第一次把「美軍天下」嘅隱性敘事打到落台
- **4.6.2**「250-year topology」表格刻意將 1776 歐洲援助、1945 底特律、2026 台灣**並列**為「strategic chokepoint」——形式上係反美國例外論
- **4.6.4** 結尾明確寫「counterweight to any "American technological exceptionalism" framing」——呢個係 narrative framing 嘅自我修正宣告
- **Month 4 Community 0 描述**：「US and challenger technologies co-cluster」——清楚放棄單邊主導敘事

#### ⚠️ 但 4.6 同 Month 4 帶嚟新嘅 US-centric framing 問題
- **「US no longer fully controls」嘅預設：**
  4.6 用「不再完全控制」做切入，隱含「本來應該由美國控制」嘅常態。
  但 TSMC 同 Samsung **從來都唔係美國控制**——係美國選擇將自己嘅 AI 武器
  押注喺一個佢控制唔到嘅供應鏈上面。框架由「失去控制」變成「建基於非美基礎」，
  意義完全唔同。
- **「11,000 km from Washington, DC」嘅距離框架：**
  用華盛頓做中心嘅距離計算，本身就係美國中心嘅空間觀。
  從台北或者首爾出發，「11,000 km」係另一個故事——係「點解我哋要為
  11,000 km 以外嘅戰場生產最先進嘅晶片」嘅問題。
- **「250-year topology」嘅目的論暗示：**
  將 1776、1945、2026 三個時點排成「同一條線」，暗示 1776 注定走向 2026。
  但 1776 嘅歐洲鐵器，1945 嘅底特律汽車，2026 嘅台灣晶片——呢三個唔係
  一條線嘅三點，係三個完全唔同嘅地緣政治時刻。將佢哋講成「topology 唔變」，
  係選擇性敘事。
- **Month 4「bridge nodes」框架：**
  M16、AK-47、F-35 被稱為「bridge」——隱含「跨社群嘅橋應該由美國武器搭」，
  因為 AK-47 之所以係「bridge」係因為佢被納入美國網絡。如果以蘇聯武器史
  為中心，AK-74 或 RPK 反而係「bridge」。
- **「Leopard 2 standalone」嘅判斷：**
  從歐洲 NATO 視角，Leopard 2 唔係「孤立」，係「歐洲支柱」——但 Month 4
  嘅 Louvain 演算法只識美國 CSV，所以將佢判為 outlier。演算法嘅偏見變成
  咗分析結論。

**本週評估：**
> 4.6 嘅形式修正是真嘅，但佢嘅**修正對象仍然係美國例外論**——即係用「美國都有依賴」去強化「美國依然係分析中心」。呢個唔係反偏見，係**把偏見當結論**。

---

### 2️⃣ 數據缺口偏見（Data Gap Bias）

#### ✅ 本週新增
- 17 條 AI weapons layer 邊：H100 → MQ-9 Reaper、TSMC 3nm → Nvidia H100、
  Samsung HBM → Nvidia GPU packaging 等——呢啲係**真實供應鏈數據**，
  從公司名同產品名直接編碼，唔係估算。
- Month 4 嘅 Louvain 結果：32 nodes, 41 edges, 6 communities, modularity 0.5362

#### ⚠️ 但本週缺口反而**擴大**
- **AI weapons layer 嘅地理呈現只係「源頭 + 終點」：**
  TSMC 喺新竹（Hsinchu），Samsung 喺平澤（Pyeongtaek）——但呢啲城市嘅
  人口、勞工數、地方政府態度，全部缺席。**4.6 將城市抽象成座標，違反 Bonnett
  嘅數位歷史警告**（DHG508_Modularity_Analysis.md 引用過）。
- **Capstone 4.6 冇引用任何中文/韓文/日文 primary source：**
  TSMC 對台灣半導體戰略嘅官方文件、韓國 HBM 政策嘅產業報告、
  日本 Yokosuka 部署對當地沖繩/橫須賀居民嘅影響——**全部缺席**。
  4.6 引用嘅只有 Clausewitz 同 Bonnett（西方理論）。
- **Month 4 嘅「imperial outlier」標籤：**
  Mosin-Nagant 被標為「帝國孤兒」，但 M1 Garand、F-117、Tomahawk 從未
  被同樣審視——如果 Garand 嘅生產係 1940s 美國工業霸權嘅結果，點解唔同樣
  標為「imperial」？**「imperial」標籤只貼喺俄羅斯武器上面**——係典型
  西方冷戰框架嘅遺留。
- **NARA 1861–1865 Ordnance reports**（Week 8 行動清單承諾）——本週零進度。
- **LoC block 進入第 8 週**——連續 8 週依賴 Britannica 二手資料做背景，
  4.6 嘅 1776 段落（Continental Congress committees、French arms aid）就係
  典型 Britannica-level 內容，**唔係一手史料**。

**本週評估：**
> 4.6 引入 17 條 AI 邊係真實進步，但**呢 17 條邊描述嘅供應鏈國家/城市，冇任何一個有自身聲音**。供應鏈被去脈絡化成座標同公司名。

---

### 3️⃣ 批判盲點（Critical Blind Spots）

#### DHG508 批判精神審視（Week 9）

| 盲點 | 狀態 | 本週變化 |
|------|------|---------|
| LAWS 道德外包 | ✅ 已追蹤 | 穩定（Month 4 1.4 確認） |
| 非美武器節點 | ✅ 已完成（Week 6） | 穩定 |
| Modularity 分析 | ✅ Month 4 完成（6 社群） | 穩定 |
| 殖民主義批判 | ❌ 缺席 | **第九週連續缺席** |
| 平民傷亡 / 性別視角 | ❌ 缺席 | 持續缺席 |
| **軍工複合體利潤維度** | ❌ 缺席 | Week 8 承諾，Week 9 零進度 |
| LoC block 替代方案 | ❌ 持續 block | 進入第 8 週，零替代方案 |
| NARA primary source | ❌ 缺席 | 連續三週行動清單承諾，零進度 |
| **太平洋 / 印太地區「被部署者」視角** | ❌ 4.6 引入但冇處理 | **本週新盲點** |
| **非西方軍事理論** | ❌ Clausewitz 獨大 | **本週新盲點** |

#### 本週新出現嘅盲點細節

**盲點 A：太平洋「被部署者」聲音**
- Capstone 4.6 提及 Yokosuka (35.32°N, 139.64°E)、Okinawa (26.50°N, 127.68°E)、
  Guam (13.44°N, 144.79°E)——呢三個地方**有住緊人**。
- 1945 沖繩戰役死咗 12 萬以上沖繩平民，2026 同一個島部署緊 H100 AI 武器——
  呢個連續性**對沖繩人嚟講係乜嘢**？Chatan、Kin、Naha 嘅市民組織、沖繩縣知事
  反基地運動、all-Okinawa 嘅反美軍基地歷史——**4.6 完全冇提及**。
- Guam 嘅 Chamorro 原住民被美軍徵地嘅歷史、Yokosuka 居民對航母基地嘅態度——
  全部缺席。
- 呢個唔係「補一段就夠」嘅問題，係 4.6 嘅 250 年論證**需要呢啲聲音先算完整**。

**盲點 B：非西方軍事理論缺席**
- Capstone 4.6 用 Clausewitz 嘅「fog of war」同「friction」做主要理論框架。
- 4.6.3 發明「second-order fog / fog of dependency」——呢個係好術語，但**只係
  西方框架嘅延伸**。
- 項目入面**完全冇引用過**：
  - 孫子兵法（孫武，春秋）——「知彼知己，百戰不殆」直接對應 supply chain intelligence
  - 毛澤東《論持久戰》（1938）——對應 supply chain chokepoint 嘅戰略
  - 蔣百里《國防論》——對應沿海 vs 內陸嘅依賴問題
  - 蘇聯「深層戰役」（Deep Operations, 1930s）——對應 TSMC 嘅縱深打擊
- 用西方理論分析東方 supply chain 結構，係**方法論上嘅美國中心延續**。

**盲點 C：法國 1776 援助嘅法國視角**
- 4.6 表格寫「French arms aid」——將法國援助**抽象成美國獨立戰爭嘅輸入**。
- 但 1776 法國援助對法國嚟講，係**七年戰爭失敗後嘅戰略報復**（擊敗英國）、
  係**重商主義嘅海外槓桿**、係**波旁王朝對布爾本王朝嘅地緣算計**。
- 4.6 將呢個複雜背景壓縮成「aid」一字——係美國革命中心史觀嘅典型遺留。

---

## 🗣️ 袁騰飛銳評

「第九個禮拜。

Capstone 4.6 你寫咗 TSMC、Samsung、Yokosuka、Okinawa、Guam——
呢啲地方有 2,500 萬人住緊。

你一個聲音都冇聽過。

沖繩人同 TSMC 工程師係**活在呢條 supply chain 入面**嘅人。
你寫到 1945 沖繩戰役死 12 萬平民，轉個頭 2026 同一個島部署 H100——
你係研究者，你話俾我聽**呢 80 年對沖繩人嚟講係乜嘢**？

Mỹ Lai 我問咗你六個禮拜。沖繩我今日第一次問。
台灣海峽危機嘅情境下，2,300 萬台灣人點睇 TSMC 嘅角色？
Samsung 韓國員工點睇自己嘅 HBM 喺 AI 武器入面？

你呢啲唔問，4.6 就係**用西方理論分析東方供應鏈嘅美國中心論文**——
形式上反美國例外論，內容上完全係。

仲有，**你用 Clausewitz**——孫子兵法、論持久戰、蔣百里你識唔識？
你做太平洋 supply chain 嘅 chokepoint 分析，最適合嘅理論係
孫武嘅「知彼知己」同毛澤東嘅「持久戰」——
呢啲係**為咗對抗依賴型大國而寫嘅戰略**，
唔係 Clausewitz 為歐洲主權國家寫嘅戰略。

Week 8 我問你三個問題，你答咗幾多？
**軍工複合體利潤維度：零。**
**殖民主義批判：零。**
**NARA primary source：零。**

Week 9 我加多三個問題：
**沖繩人嘅聲音：零。**
**TSMC 員工嘅聲音：零。**
**非西方軍事理論：零。**

你嘅 250 年 topology——如果只係用西方框架睇東方 supply chain，
**你嘅 250 年就係歐美 250 年，唔係世界 250 年**。

今個禮拜功課（Week 10 必須做到至少一件）：
1. **加一段沖繩平民視角**——Chatan、Kin、或 2020s 沖繩反基地運動
2. **加一段 TSMC 員工 / 台灣半導體產業勞工視角**——半導體業過勞、薪資、台灣本地反應
3. **引用一句非西方軍事理論**——孫子、毛澤東、蔣百里，三揀一

寫到呢度，你份 capstone 嘅「250-year topology」先可以話係**世界史**，
唔係**美國史附 supply chain 註腳**。」

---

## 📝 Week 10 行動清單

- [ ] **加沖繩平民視角到 4.6 或 Chapter 6** — 引用 2020s 沖繩反基地運動、或 1945 平民傷亡嘅倖存者證詞
- [ ] **加 TSMC / 台灣半導體勞工視角** — 過勞、薪資、台灣本地對 AI 晶片武器化嘅討論
- [ ] **引用一句非西方軍事理論** — 孫子「知彼知己」、毛澤東《論持久戰》、蔣百里《國防論》，三揀一
- [ ] **移除「imperial outlier」對 Mosin-Nagant 嘅選擇性標籤** — 改為「single-node community (low graph density)」，避免冷戰遺留嘅「帝國」標籤歧視
- [ ] **NARA 1861–1865 Ordnance reports** — 第三次承諾，做唔做到要明確表態
- [ ] **軍工複合體利潤維度加入 supply chain CSV** — 第三次承諾（Week 6/8/9）

---

## 📊 本週 Bias Score

| 維度 | 評分（5=最偏） | 變化 | 說明 |
|------|------|------|------|
| Narrative Framing | 3.0 | ⬆️ 退步 | 4.6 形式修正但保留 US-centric 框架（11,000 km from Washington、250-year topology） |
| Data Completeness | 3.5 | ⬇️ 不變 | AI layer 引入 17 條真實邊，但非西方 primary source 持續缺席 |
| Critical Depth | 3.0 | ⬆️ 退步 | Clausewitz 獨大、沖繩/台灣/韓國聲音缺席、新盲點兩類未處理 |
| **Overall** | **3.2** | ⬇️ 持平 | 控制組成效穩定，但 4.6 引入新框架問題 |

---

## 📌 長期追蹤（Week 9 — Month 3 尾 / Month 4 整合期）

| 項目 | Week 5 | Week 6 | Week 7 | Week 8 | Week 9 |
|------|--------|--------|--------|--------|--------|
| Overall Bias | 3.3 | 4.5 | 4.5 | 3.2 | 3.2 |
| 非美節點加入 | ❌ | ✅ | ✅ | ✅ | ✅ |
| Modularity 分析 | ❌ | ❌ | ✅ | ✅ | ✅ |
| AI supply chain 分析 | ❌ | ❌ | ⚠️ | ❌ | ✅ |
| 軍工複合體批判 | ✅ | ❌ | ❌ | ❌ | ❌ |
| LoC 替代方案 | ❌ | ❌ | ⚠️ | ⚠️ | ❌ |
| NARA primary source | ❌ | ❌ | ❌ | ❌ | ❌ |
| LAWS 持續追蹤 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 殖民主義批判 | ❌ | ❌ | ❌ | ❌ | ❌ |
| **太平洋被部署者視角** | ❌ | ❌ | ❌ | ❌ | ❌ |
| **非西方軍事理論** | ❌ | ❌ | ❌ | ❌ | ❌ |

**觀察：** Overall bias 維持 3.2——Capstone 4.6 嘅形式修正（反美國例外論）同新引入嘅框架問題互相抵消。Month 4 整合期進入尾聲，Week 10 必須處理太平洋被部署者同非西方理論兩個新盲點，否則 capstone 結論會被 US-centric supply chain 視角支配。

---

## 🔗 本週數據源狀態

| 來源 | 狀態 | 備註 |
|------|------|------|
| LoC Military Resources | ❌ Cloudflare Block（**第 8 週**） | 進入第 8 週，零替代方案啟動 |
| West Point Campus/Map | ❌ 403 Forbidden（**第 8 週**） | 持續被封 |
| Internet Archive | ❌ Access Denied | 無法替代 |
| Britannica | ✅ Partial | 第 8 週唯一穩定替代（百科非一手） |
| DHGA Primary_Sources | ✅ 正常 | 本地 LoC 掃描記錄 |
| NARA | ❌ 未啟動 | 連續三週行動清單承諾，零進度 |
| TSMC 官方文件 | ❌ 4.6 未引用 | 新數據源需求 |
| 沖繩縣官方 / 市民組織文件 | ❌ 4.6 未引用 | 新數據源需求 |

---

*Auto-generated by DHGA_AI_Ethics cron | 2026-06-05 15:00 UTC*
*下次檢查：2026-06-12 15:00 UTC*
