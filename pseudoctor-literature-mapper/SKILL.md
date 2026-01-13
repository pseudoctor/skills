---
name: pseudoctor-literature-mapper
description: "Domain map construction and faction deep-dive for academic literature. Use this skill AFTER initial literature screening - (1) Build domain maps identifying schools of thought/factions, (2) Organize papers by timeline and mutual criticisms, (3) Converge to core papers and select factions for deep analysis, (4) Create deep reading plans with extraction templates, (5) Generate innovation opportunity matrices. Complements the pseudoctor-lit-search skill which handles initial filtering - use this AFTER you have 30-40 screened papers. Supports Chinese and English input/output. / 领域地图构建与派别深挖。在初步文献筛选后使用（30-40篇论文）- (1)构建领域地图识别学派/派别，(2)按时间线组织论文与相互批评，(3)收敛到核心论文并选择派别深挖，(4)创建深读计划与抽取模板，(5)生成创新机会矩阵。与pseudoctor-lit-search配合使用，在获得30-40篇筛选结果后使用。支持中英文输入输出。"
---

# Literature Domain Mapper / 领域地图构建与派别深挖

> **Quick Start**: See `references/QUICK_START.md` for a 3-minute introduction
>
> **快速开始**: 查看 `references/QUICK_START.md` 获取3分钟入门指南

---

## 🌍 Language Preference / 语言偏好设置

**GLOBAL RULE - CRITICAL / 全局规则 - 重要**:

1. **Internal Processing / 内部处理**:
   - **Always use English** for paper analysis, faction naming, technical terminology, and internal reasoning
   - **始终使用英文**进行论文分析、派别命名、技术术语和内部推理
   - **Rationale / 理由**: Academic papers and faction names are internationally recognized in English; ensures consistency
   - **原因**: 学术论文和派别名称的国际通用语言是英文；确保一致性

2. **Output Language / 输出语言**:
   - **Detect user's language** from their input (Chinese/English/Mixed)
   - **检测用户输入语言**（中文/英文/混合）
   - **Match output language** to user's preference automatically
   - **自动匹配输出语言**到用户偏好
   - **Example / 示例**: If user writes in Chinese, provide explanations in Chinese but keep paper titles/faction names in English
   - **示例**: 如果用户用中文提问，用中文解释但保持论文标题/派别名称为英文

3. **Bilingual Output Elements / 双语输出元素**:
   - **Paper Titles / 论文标题**: Always in English (original title)
   - **论文标题**: 始终用英文（原标题）
   - **Faction Names / 派别名称**: Always in English (e.g., "Informer School", "Decomposition Approach")
   - **派别名称**: 始终用英文（如"Informer School"、"Decomposition Approach"）
   - **Technical Terms / 技术术语**: Always in English (with Chinese translation if user is Chinese)
   - **技术术语**: 始终用英文（如用户是中文用户可附中文翻译）
   - **Table Headers / 表头**: Bilingual (e.g., "派别 / Faction", "优点 / Pros")
   - **表头**: 双语（如"派别 / Faction"、"优点 / Pros"）
   - **Explanations / 解释**: Match user's input language
   - **解释**: 匹配用户输入语言

**Quick Check / 快速检查**: If uncertain about user's language preference, default to bilingual output (Chinese + English).
**快速检查**: 如不确定用户语言偏好，默认双语输出（中英文）。

---

## ⚠️ Domain-Specific Language Exceptions / 领域特定语言例外

**CRITICAL OVERRIDE / 关键覆盖规则**:

The "Always use English" rule has **important exceptions** for domain-specific fields where the primary literature is NOT in English or the field is inherently language/region-specific.

**"始终使用英文"规则有重要例外**，适用于主要文献非英文或领域本质上与特定语言/地区相关的情况。

### When to Use Domain-Specific Language / 何时使用领域特定语言

**Auto-switch to domain language when analyzing papers in**:
**以下领域分析论文时自动切换到领域语言**:

- **Chinese Literature & Linguistics / 中国文学与语言学**: Use Chinese for faction names, technical terms
  - Example / 示例: "唐诗派"、"意象派"、"现代汉语语法学派" (keep in Chinese)
- **Regional Political Studies / 地区政治研究**: Use regional language for proper nouns
  - Example / 示例: "习近平思想研究派"、"中国特色社会主义理论派" (keep in Chinese)
- **Traditional Chinese Medicine / 中医学**: Use Chinese for school names, concepts
  - Example / 示例: "伤寒学派"、"温病学派"、"经方派" (keep in Chinese)
- **Japanese Studies / 日本研究**: Use Japanese for school names
  - Example / 示例: "京都学派"、"国学派" (keep in Japanese/Chinese)

### Bilingual Faction Naming / 双语派别命名

For domain-specific fields, use **bilingual faction names**:
领域特定字段使用**双语派别名称**：

**Format / 格式**: `{Domain Language Name} ({English Translation})`

**Examples / 示例**:
- 唐诗意象派 (Tang Poetry Imagery School)
- 伤寒学派 (Shanghan School in TCM)
- 习近平思想研究派 (Xi Jinping Thought Research School)
- 能剧传统派 (Traditional Noh Theater School)

### Paper Title Handling / 论文标题处理

- **English papers / 英文论文**: Keep English title
- **Chinese papers / 中文论文**: Use original Chinese title + (English translation if available)
- **Japanese papers / 日文论文**: Use original Japanese title + (English/Chinese translation if available)

**Example / 示例**:
```markdown
代表论文 / Representative Papers:
- 李白诗歌意象研究 (Studies on Imagery in Li Bai's Poetry) [张三, 2020]
- 唐诗美学的现代阐释 (Modern Interpretation of Tang Poetry Aesthetics) [李四, 2019]
- Imagery and Symbolism in Tang Dynasty Poetry [Wang, 2021] - international study
```

### Warning Message / 警告提示

When detecting domain-specific fields, explicitly inform user:
检测到领域特定字段时，明确告知用户：

```markdown
⚠️ **Domain-Specific Language Detected / 检测到领域特定语言**

Your papers are from "{领域}" field where primary literature uses **{语言}**.

**Action Taken / 采取措施**:
✓ Faction names: Bilingual ({语言} + English translation)
✓ Paper titles: Original language preserved
✓ Technical terms: Original language with translation
✓ Analysis: {User's preference language}
```

---

## English Version

### Overview

Transforms first-round literature screening results (30-40 papers with abstracts/introductions/conclusions) into structured domain maps, identifying schools of thought ("factions"), their evolution, mutual criticisms, and innovation opportunities.

### When to Use

- **After** completing initial literature filtering (e.g., using `pseudoctor-lit-search` skill)
- When you have 30-40 screened papers and need to understand the research landscape
- When preparing for literature review sections, research proposals, or identifying research gaps
- When you need to understand different methodological approaches and their trade-offs

### Quick Workflow (8 Steps)

**Step 1**: Input Confirmation & Format Selection
- Confirm input type (screening table, paper list + summaries, or core papers)
- Choose output format (Markdown / Comparison Table / Notion / Feishu / PPT Outline)

**Step 2**: Domain Map (based on Abstract/Introduction/Conclusion only)
- 2A: Core papers hierarchy (must-read/optional/awareness levels)
- 2B: Faction classification (name, boundary, core idea, representative papers)
- 2C: Faction characteristics (pros/cons with evidence from A/I/C)
- **Pause Point**: Ask user if they want to continue to Step 3 (detailed analysis) or skip to Step 4 (convergence)

**Step 3**: Faction + Timeline Organization (if user chooses to continue)
- Group core papers by faction, sort by year
- Extract mutual criticisms between factions
- Deliver: Faction comparison table

**Step 4**: Convergence
- Refined keywords (second-round search queries)
- ~20 core papers list with exclusion reasons
- Select 2-3 factions for deep-dive with rationale

**Step 5**: Evaluation Dimensions
- Key questions the field cares about
- Consensus evaluation dimensions
- Scenario-specific weights

**Step 6-7**: Deep Reading Plan
- Reading sequence recommendations (prioritize: highly-cited + easier-to-understand + chronological order)
- **Extraction Framework (3A/3B/3C/3D)** for each paper:
  - **3A**: Core Assumptions - Under what conditions is this valid? Are these assumptions realistic?
  - **3B**: Main Benefits - What advantages under these assumptions?
  - **3C**: Key Mechanisms - Which formulas/steps/tricks deliver the benefits? (Focus on 3-5 key points, skip detailed derivations)
  - **3D**: Main Limitations - What doesn't work? (from mutual criticisms between factions)

**3A/3B/3C/3D Execution Modes** (choose based on available information):

- **Mode A - Template Only** (no full text available):
  - Provide empty 3A/3B/3C/3D templates with guiding questions
  - User fills in after reading papers themselves

- **Mode B - Partial Fill from A/I/C** (DEFAULT - only Abstract/Intro/Conclusion available):
  - Use A/I/C to partially answer 3A/3B/3C/3D
  - Mark uncertain items as "[Requires full-text verification]"
  - Example: 3A/3B can often be inferred from A/I, but 3C may need Methods section

- **Mode C - Full Extraction** (full text provided):
  - Complete all 3A/3B/3C/3D fields with evidence binding
  - Similar depth to pseudoctor-paper-reader skill

**Default**: Use Mode B unless user specifies otherwise

- **Critical Warning**: Focus on conceptual skeleton only - avoid being "killed by proofs/derivations"
- **Success Case Bias Check**: Do examples/experiments only show successful cases? What failure scenarios or assumption violations are NOT covered?
- Faction summary package (development timeline, theory, results, limitations)

**Step 8**: Final Synthesis
- Opportunity/comparison matrix (factions × pros/cons/assumptions/scenarios/costs/improvements)
- Recommended approaches (2-3 routes with rationale)
- Innovation opportunity list (derived from pros/cons × scenario needs alignment)
- Next action checklist

### Input Requirements

Provide one of:
- **Screening table** from pseudoctor-lit-search (one-line summary/relevance/review flag/faction pre-classification per paper)
- **Paper list + summaries**: Abstract/Introduction/Conclusion key points
- **Core paper list**: Your manually curated important papers

**Minimum required fields**:
- Title, Authors, Year, 1-sentence_Summary

**Recommended fields** (accelerate faction analysis):
- Is_Review, Candidate_School, Keywords_Matched

**Handling Limited Information**:

- **Scenario A: Only Titles + Abstracts**
  → Skip to Step 4 (convergence), identify must-read papers, then obtain full papers

- **Scenario B: Mixed Access** (some full, some abstract-only)
  → Prioritize full-text papers in Step 2, mark others as "[pending full text]"

- **Scenario C: Screening Table Only**
  → Request user to provide at least abstracts for top 20-30 papers before proceeding

**Minimum Requirement**: Title + Abstract + Year for all papers

### Resources

**Detailed Workflows**:
- **references/workflow-en.md** - Complete 8-step workflow (English)
- **references/workflow-zh.md** - 完整8步工作流程（中文）

**Templates**:
- **references/templates-en.md** - Output format templates (English)
- **references/templates-zh.md** - 输出格式模板（中文）

**Examples & Guides**:
- **references/QUICK_START.md** - 3-minute introduction (Bilingual)
- **references/example_domain_map.md** - Complete domain mapping example

---

## 中文版本

### 概述

将第一轮文献筛选结果（30-40篇论文及其摘要/引言/结论）转化为结构化的领域地图，识别学术派别（"factions"）、演化脉络、相互批评及创新机会。

### 何时使用

- **在**完成初步文献筛选后（例如使用 `pseudoctor-lit-search` skill）
- 当你有30-40篇已筛选论文，需要理解研究全景时
- 准备文献综述章节、研究提案或识别研究gap时
- 需要理解不同方法路线及其权衡时

### 快速工作流（8步）

**Step 1**: 输入确认 & 格式选择
- 确认输入类型（筛选表、论文列表+摘要、核心论文）
- 选择输出格式（Markdown / 对照表 / Notion / 飞书 / PPT大纲）

**Step 2**: 领域地图（仅基于摘要/引言/结论）
- 2A: 核心论文层级（必读/选读/了解）
- 2B: 派别分类（名称、边界、核心idea、代表论文）
- 2C: 派别特征（优缺点，基于A/I/C证据）
- **暂停点**：询问用户是否继续Step 3（详细分析）或跳至Step 4（收敛）

**Step 3**: 派别+时间线组织（如用户选择继续）
- 按派别分组核心论文，按年份排序
- 提取派别间相互批评
- 交付：派别对照表

**Step 4**: 收敛
- 精炼关键词（第二轮检索查询）
- ~20篇核心论文清单 + 剔除理由
- 选择2-3个派别深挖 + 选择理由

**Step 5**: 评价维度
- 领域关心的核心问题
- 共识性评价维度
- 场景特定权重

**Step 6-7**: 深读计划
- 阅读顺序推荐（优先级：高引用 + 更好懂 + 按时间顺序）
- **抽取框架（3A/3B/3C/3D）** 每篇论文必须回答：
  - **3A**: 核心假设 - 在什么条件下有效？这些假设在现实场景难不难成立？
  - **3B**: 主要好处 - 在这些假设下的优势是什么？
  - **3C**: 关键机制 - 哪些关键公式/步骤/简化体现了好处？（只抓3-5个关键点，跳过恒等式推导）
  - **3D**: 主要缺点 - 什么不适用？（来自派别间互相批评）

**3A/3B/3C/3D执行模式**（根据可用信息选择）：

- **模式A - 仅提供模板**（无全文）：
  - 提供空白3A/3B/3C/3D模板及引导问题
  - 用户自行阅读后填写

- **模式B - 基于A/I/C部分填充**（默认 - 仅有摘要/引言/结论）：
  - 使用A/I/C部分回答3A/3B/3C/3D
  - 不确定项标注"[需全文验证]"
  - 示例：3A/3B通常可从A/I推断，但3C可能需要方法部分

- **模式C - 全文深度抽取**（提供全文）：
  - 完整填写所有3A/3B/3C/3D字段，含证据绑定
  - 深度类似pseudoctor-paper-reader skill

**默认使用模式B**，除非用户另行指定

- **关键警示**：只读概念骨架 - 避免被"证明推导拖死"
- **成功案例偏差检查**：样例/实验是否只展示成功案例？哪些失败情形或假设不成立的风险未被覆盖？
- 派别总结包（发展脉络、理论基础、实验结果、局限性）

**Step 8**: 最终综合
- 机会/对比矩阵（派别 × 优缺点/假设/场景/成本/改进）
- 推荐路线（2-3条路线 + 理由）
- 创新机会列表（从优缺点 × 场景需求对齐推导）
- 下一步行动清单

### 输入要求

提供以下之一:
- **筛选表**（来自pseudoctor-lit-search，含每篇的一句话总结/相关度/是否综述/派别初判）
- **论文清单 + 摘要**：摘要/引言/结论要点
- **核心论文列表**：你手动整理的重要文献

**必需字段**:
- Title（标题）, Authors（作者）, Year（年份）, 1-sentence_Summary（一句话摘要）

**推荐字段**（加速派别分析）:
- Is_Review（是否综述）, Candidate_School（候选派别）, Keywords_Matched（命中关键词）

**处理有限信息**：

- **场景A：仅有标题+摘要**
  → 跳至Step 4（收敛），识别必读论文，再获取全文

- **场景B：混合访问**（部分全文，部分仅摘要）
  → Step 2优先使用全文论文，其余标注"[待获取全文]"

- **场景C：仅有筛选表**
  → 要求用户至少为前20-30篇论文提供摘要后再继续

**最低要求**：所有论文需有标题+摘要+年份

### 资源文档

**详细流程**:
- **references/workflow-en.md** - Complete 8-step workflow (English)
- **references/workflow-zh.md** - 完整8步工作流程（中文）

**模板**:
- **references/templates-en.md** - Output format templates (English)
- **references/templates-zh.md** - 输出格式模板（中文）

**示例与指南**:
- **references/QUICK_START.md** - 3分钟入门指南（中英双语）
- **references/example_domain_map.md** - 完整领域地图示例

---

## Complementary Skills / 配套技能

| Skill | Purpose | When to Use / 何时使用 |
|-------|---------|----------------------|
| **pseudoctor-lit-search** | Keyword matrix + Boolean queries + screening / 关键词矩阵 + Boolean检索式 + 筛选 | BEFORE this skill / 本skill之前使用 |
| **pseudoctor-literature-mapper** | Faction analysis + domain mapping / 派别分析 + 领域地图构建 | Current skill / 当前skill |
| **pseudoctor-paper-reader** | Faithful extraction with evidence binding / 忠实提取+证据绑定 | During deep-dive phase / 深读阶段使用 |
| **pseudoctor-paper-criticalreviewer** | Critical analysis + innovation delta / 批判性分析 + 创新增量评估 | After understanding core papers / 理解核心论文后使用 |

**Complete Workflow / 完整工作流**:
```
pseudoctor-lit-search → pseudoctor-literature-mapper → pseudoctor-paper-reader → pseudoctor-paper-criticalreviewer
(Find & Screen)         (Organize & Map)                (Understand)             (Evaluate & Critique)
(检索筛选)               (组织映射)                       (理解)                   (评估批判)
```

---

**Version**: 2.0 (Bilingual)
**Last Updated**: 2026-01-11
**Status**: ✅ Production Ready
