---
name: pseudoctor-business-review
description: Generate objective, data-driven business analysis reports from raw business datasets. Use for requests like "生意分析/业务数据分析/经营分析报告/商业数据洞察" that require strict data QA, multi-dimensional KPI analysis, and a professional HTML report with Chart.js and a fixed corporate color system. Outputs must be fact-based only, no recommendations.
---

# Pseudoctor Business Review

## Overview

Produce comprehensive, data-only business analysis reports in HTML. Follow a strict methodology (data QA → KPI system → multi-dimensional analysis → FACT/WHY/SO WHAT) and enforce the specified visual system and color rules.

## Workflow

1. Load the full prompt spec in `references/prompt.md` and follow it verbatim.
2. If a user provides a reference HTML format, mirror its structure and visual hierarchy; use `assets/template/report_template.html` as the default format baseline.
2. Inspect the dataset schema and time coverage; list fields, granularity, and coverage.
3. Run data quality checks (missing, outliers, duplicates) and report impacts.
4. Build the KPI system and compute metrics with formulas and units.
5. Perform time series, dimension comparison, structure, and cross analyses.
6. Convert insights into FACT → WHY → SO WHAT, keeping strict neutrality.
7. Render a full HTML report with Chart.js and the mandated color system.
8. Validate that all charts, tables, and components follow the color checklist.

## Output Requirements (Hard Constraints)

- Output only data facts and analytical insights; no actions, recommendations, or opportunity/problem framing.
- Do not limit length; keep the report detailed, specific, and logically structured.
- Disclose data sources and assumptions; document cleaning and imputation logic.
- Provide traceable numbers for every key statement; keep units explicit.
- HTML must be responsive and use the exact color palette and gradients from `references/prompt.md`.
- Must include these sections in this order: 数据概览 → 时间序列 → 品牌结构与产品 → 门店 → SKU → 交叉 → 结构与集中度 → 洞察 → 库存风险 → 附录. Keep the executive summary KPI block at the top.
- Must include required interactivity and UX elements (hover tooltips, collapse/expand, smooth scroll, back-to-top, print/export support) as defined in `references/prompt.md`.
- Must satisfy WCAG AAA contrast for core content and use only listed HEX colors; no unlisted colors.
- If a target format is provided, keep its section order and layout while enforcing the mandated palette and constraints.

## Dimension Selection Rules

- Fixed dimensions (must exist): 品牌、门店、SKU销售数量、SKU销售金额. Always include these in KPI and analysis.
- Optional dimensions: 区域/省区、零售客户名称等，若存在则追加分析（不改变固定结构顺序）。
- If any fixed dimension is missing or >50% missing, keep the section but clearly label “数据缺失/无法评估” and avoid substitute dimensions unless the user explicitly allows it.

## Report Structure (Locked)

- 数据概览：数据来源、时间范围、完整性/缺失率、去重情况。
- 时间序列：月度销售金额趋势 + 日度销售金额趋势 + 品牌月度结构 + 销售数量月度趋势。
- 品牌结构与产品：品牌明细（迄今 vs 当月）、品牌占比、品牌数量、品牌占比变化、Top20 产品金额、Top30 产品排名变化、产品月度变化、热销稳定性。
- 门店：Top20 门店金额、Top10 明细、Top30 排名变化、Top20 稳定性、Top5 效率雷达图。
- SKU：Top10（数量/金额）与明细折叠。
- 交叉：品牌×门店 Top10 组合 + 高效门店特征（Top5 vs 全店均值）。
- 结构与集中度：品牌/门店/SKU 集中度。
- 洞察：FACT → WHY → SO WHAT（至少 4 条，全部量化）。
- 库存风险：库存周转概览 + 风险预警表（门店×SKU）。
- 附录：数据来源与口径说明。

## Final Compliance Checklist

- All mandatory sections present and populated with data-backed content.
- All KPIs include formulas, units, and data sources.
- All charts use Chart.js and the specified palette order.
- All interactions and responsive rules implemented.
- No recommendation or action language present.

## When to Read References

- Always read `references/prompt.md` before generating any report.
- Use it as the single source of truth for structure, analysis depth, and visual specs.

## Resources

- `references/prompt.md`: Full prompt spec including methodology, structure, and complete color system.
- `assets/template/report_template.html`: Baseline HTML + Chart.js skeleton aligned with the required section structure and color system.
