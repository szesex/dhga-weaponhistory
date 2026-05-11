# DHG508 Week 7 AI Ethics Report
## 2026-05-11

### 中文版

本週 Bias Score 維持 4.5/5（上週已從 3.3/5 提升）。control group（AK-47 1947、HQ-17 2015、TOR-M1 2016）已同步所有 CSV，新增 10 條 Control_Comparison edges，有效平衡美國中心敘事。

Gephi Modularity 分析結果：
- 40-node 版本為 bipartite 結構（武器 → outcome），Modularity Score = 0（無武器共享 outcome）
- 改用 Periodization 分組後得出 7 個有意義時期集群
- Friction_Type 佔比最高（30%），支持 Clausewitz「戰爭阻力」理論

Plotly 互動地圖已上線 GitHub Pages，1776 革命戰場 + Pacific 島嶼戰場已疊加，視覺化層面完成。

剩餘問題：LoC/West Point 仍被 Cloudflare 封鎖，NARA primary source scan 需手動跟進。

### English Version

This week Bias Score remains 4.5/5 (improved from 3.3/5 last week). Control group (AK-47 1947, HQ-17 2015, TOR-M1 2016) has been synchronized to all CSVs with 10 new Control_Comparison edges, effectively balancing the US-centric narrative.

Gephi Modularity results:
- The 40-node version is bipartite (weapon → outcome), Modularity Score = 0 (no shared outcomes between weapons)
- Using Periodization grouping produced 7 meaningful period clusters
- Friction_Type the largest category (30%), supporting Clausewitz's "friction of war" theory

The Plotly interactive map is now live on GitHub Pages with 1776 Revolutionary War battlefields + Pacific island battlefields overlaid. Visualization layer completed.

Remaining issues: LoC/West Point still blocked by Cloudflare, NARA primary source scan needs manual follow-up.

### 行動建議（Week 8 重點）

1. 用 33-node 版本（79 edges）重新跑 Modularity（Resolution 0.5）
2. 手動補 NARA 1861-1865 Ordnance reports
3. 更新 GitHub Pages StoryMap
4. Gephi Multimode Networks Projection（40-node 版本做 Projection 分析）

### 袁騰飛式總結

歷史唔係口號大於行動，而係要即刻落實！control group + Modularity 分析一做，bias score 就從 3.3/5 衝上 4.5/5——呢個就係 DHG508 真正批判精神！不過 LoC 封鎖同 NARA scan 仲係老問題，繼續努力啦，勿忘「讀歷史即是讀人心」！