# Pseudoctor Literature Mapper

> Domain map construction and faction deep-dive for academic literature. Build research landscapes identifying schools of thought, organize papers by timeline and mutual criticisms, and converge to core papers for deep analysis.

## Overview

**Pseudoctor Literature Mapper** transforms first-round literature screening results (30-40 papers) into structured domain maps that reveal:

1. **Schools of thought ("factions")** - Methodological approaches and their boundaries
2. **Evolution timelines** - How ideas developed and influenced each other
3. **Mutual criticisms** - What factions critique about each other
4. **Innovation opportunities** - Gaps and directions for new research

This is the **second stage** of a complete literature analysis workflow. Use it **after** `pseudoctor-lit-search`.

## Key Features

### 1. Domain Map Construction

**Automatically organizes papers into**:

- **Core Papers Hierarchy** (3 levels):
  - **Must-Read**: Foundational or paradigm-shifting work
  - **Optional**: Important but not essential
  - **Awareness**: Good to know for context

- **Faction Classification**:
  - Faction name & boundaries
  - Core idea/concept
  - Representative papers

- **Faction Characteristics** (with evidence from Abstract/Introduction/Conclusion):
  - Pros/Advantages
  - Cons/Limitations
  - Key assumptions

### 2. Timeline & Evolution Analysis

Organizes papers by:
- **Chronological order** within each faction
- **Influence chains** - how papers cite and build on each other
- **Turning points** - paradigm shifts or major innovations

### 3. Mutual Criticism Extraction

Identifies:
- What Faction A critiques about Faction B
- How Faction B responds
- Unresolved debates between factions

### 4. Convergence Strategy

From 30-40 papers → **~20 core papers** with:
- Refined keywords for second-round search
- Clear exclusion reasons for dropped papers
- **2-3 factions selected for deep-dive** with rationale

### 5. Deep Reading Framework

**3A/3B/3C/3D Extraction Template** for each paper:

| Component | Question | Purpose |
|-----------|----------|---------|
| **3A: Core Assumptions** | Under what conditions is this valid? Are assumptions realistic? | Identify boundary conditions |
| **3B: Main Benefits** | What advantages under these assumptions? | Understand value proposition |
| **3C: Key Mechanisms** | Which formulas/steps/tricks deliver benefits? (3-5 key points) | Extract conceptual skeleton |
| **3D: Main Limitations** | What doesn't work? (from mutual criticisms) | Identify failure modes |

**Execution Modes**:

- **Mode A - Template Only**: Empty 3A/3B/3C/3D templates for user to fill
- **Mode B - Partial Fill** (DEFAULT): Use A/I/C to partially fill, mark uncertain items
- **Mode C - Full Extraction**: Complete all fields with full text

### 6. Innovation Opportunity Matrix

Generates:
- **Comparison matrix**: Factions × (pros/cons/assumptions/scenarios/costs/improvements)
- **Recommended approaches**: 2-3 routes with rationale
- **Innovation opportunities**: Derived from pros/cons × scenario needs alignment
- **Next action checklist**

## When to Use

- **After** completing initial literature screening (e.g., using `pseudoctor-lit-search`)
- When you have 30-40 screened papers and need to understand the research landscape
- When preparing literature review sections or research proposals
- When identifying research gaps and innovation directions
- When you need to understand different methodological approaches and their trade-offs

## Quick Start

```
/pseudoctor-literature-mapper [paste your screening table]
```

### Input Requirements

Provide one of:

| Input Type | Description | Minimum Fields |
|------------|-------------|----------------|
| **Screening table** | From pseudoctor-lit-search | Title, Authors, Year, 1-sentence_Summary |
| **Paper list + summaries** | Abstract/Introduction/Conclusion key points | Title, Authors, Year, Summaries |
| **Core paper list** | Manually curated important papers | Title, Authors, Year |

**Recommended fields** (accelerate faction analysis):
- `Is_Review` - Prioritize surveys for overview
- `Candidate_School` - Preliminary faction classification
- `Keywords_Matched` - Help with categorization

## 8-Step Workflow

### Step 1: Input Confirmation & Format Selection

- Confirm input type
- Choose output format (Markdown / Comparison Table / Notion / Feishu / PPT Outline)

### Step 2: Domain Map (Abstract/Introduction/Conclusion only)

**2A**: Core papers hierarchy (must-read/optional/awareness levels)

**2B**: Faction classification
- Faction name, boundary, core idea
- Representative papers

**2C**: Faction characteristics
- Pros/cons with evidence from A/I/C

**Pause Point**: Ask user if they want to continue to Step 3 (detailed analysis) or skip to Step 4 (convergence)

### Step 3: Faction + Timeline Organization (if user continues)

- Group core papers by faction, sort by year
- Extract mutual criticisms between factions
- Deliver: Faction comparison table

### Step 4: Convergence

- Refined keywords (second-round search queries)
- ~20 core papers list with exclusion reasons
- Select 2-3 factions for deep-dive with rationale

### Step 5: Evaluation Dimensions

- Key questions the field cares about
- Consensus evaluation dimensions
- Scenario-specific weights

### Step 6-7: Deep Reading Plan

**Reading sequence recommendations**:
1. Highly-cited papers
2. Easier-to-understand papers
3. Chronological order

**3A/3B/3C/3D extraction** for each selected faction

**Critical warning**: Focus on conceptual skeleton - avoid being "killed by proofs/derivations"

**Success case bias check**: Do examples/experiments only show successful cases? What failure scenarios are NOT covered?

### Step 8: Final Synthesis

- Opportunity/comparison matrix
- Recommended approaches (2-3 routes)
- Innovation opportunity list
- Next action checklist

## Output Format Options

| Format | Best For | Features |
|--------|----------|----------|
| **Markdown** | Documentation, easy reading | Structured sections, tables, code blocks |
| **Comparison Table** | Quick faction comparison | Side-by-side faction characteristics |
| **Notion Schema** | Notion database | Field types, multi-select properties |
| **Feishu Schema** | Feishu multidimensional tables | Field types, views, filters |
| **PPT Outline** | Presentations | Slide structure with key points |

## Language Support

### Global Rule: Internal Processing

- **Always use English** for paper analysis, faction naming, technical terminology, and internal reasoning
- **Rationale**: Academic papers and faction names are internationally recognized in English; ensures consistency

### Output Language

- **Detect user's language** (Chinese/English/Mixed) from input
- **Match output language** to user's preference automatically
- **Bilingual elements**:
  - Paper titles: Always English (original)
  - Faction names: Always English (e.g., "Informer School", "Decomposition Approach")
  - Technical terms: Always English (with Chinese translation if user is Chinese)
  - Table headers: Bilingual (e.g., "派别 / Faction", "优点 / Pros")
  - Explanations: Match user's input language

### Domain-Specific Language Exceptions

**For domain-specific fields** (Chinese literature, TCM, regional politics, etc.):

- Use **bilingual faction names**: `{Domain Language Name} ({English Translation})`
- Examples:
  - 唐诗意象派 (Tang Poetry Imagery School)
  - 伤寒学派 (Shanghan School in TCM)
  - 习近平思想研究派 (Xi Jinping Thought Research School)

**Paper title handling**:
- English papers: Keep English title
- Chinese papers: Original Chinese + (English translation if available)
- Japanese papers: Original Japanese + (English/Chinese translation if available)

## Handling Limited Information

| Scenario | Strategy |
|----------|----------|
| **Only Titles + Abstracts** | Skip to Step 4 (convergence), identify must-read papers, then obtain full papers |
| **Mixed Access** (some full, some abstract-only) | Prioritize full-text papers in Step 2, mark others as "[pending full text]" |
| **Screening Table Only** | Request user to provide at least abstracts for top 20-30 papers |

**Minimum requirement**: Title + Abstract + Year for all papers

## Complete Literature Workflow

```
【Stage 1】pseudoctor-lit-search
Input: Research topic/sub-question
Output: 30-40 core papers + screening table + keyword matrix

        ↓ (screening table as input)

【Stage 2】pseudoctor-literature-mapper (current skill)
Input: Stage 1 screening table + A+I+C summaries
Output:
  - Faction comparison table (schools/method factions)
  - Timeline and evolution
  - ~20 core papers convergence list
  - Deep reading plan + extraction templates
  - Innovation opportunity matrix

        ↓ (must-read papers list)

【Stage 3】pseudoctor-paper-reader (optional)
Input: Must-read paper full texts
Output: Evidence-bound detailed paper cards

        ↓

【Stage 4】pseudoctor-paper-criticalreviewer (optional)
Input: Core papers
Output: Critical insights + innovation delta assessment
```

## Usage Example

```
User: [Pastes screening table of 35 papers on time series forecasting]

[Output]:

## Step 2: Domain Map

### 2A: Core Papers Hierarchy

**Must-Read Level** (8 papers):
- P001: "Informer: Beyond Efficient Transformer..." [Zhou et al., 2021]
  → Rationale: 1000+ citations, established Transformer-for-time-series paradigm
- P003: "Autoformer: Decomposition Transformers..." [Wu et al., 2021]
  → Rationale: Novel decomposition approach, highly cited
...

**Optional Level** (15 papers):
...

**Awareness Level** (12 papers):
...

### 2B: Faction Classification

**Faction 1: Pure Attention School**
- Core Idea: Direct application of Transformer attention mechanisms
- Boundary: No classical time-series components (no decomposition, no autocorrelation)
- Representative Papers: P001, P005, P012

**Faction 2: Decomposition-Based School**
- Core Idea: Decompose series first, then apply Transformer
- Boundary: Explicit trend/seasonality decomposition
- Representative Papers: P003, P008, P015

**Faction 3: Hybrid School**
- Core Idea: Combine Transformer with classical models (ARIMA, ETS)
- Boundary: Uses both attention and statistical components
- Representative Papers: P007, P018, P022

### 2C: Faction Characteristics

**Faction 1: Pure Attention School**
- Pros:
  • Can capture complex non-linear patterns [Evidence: P001, Abstract]
  • Parallel computation enables fast training [Evidence: P005, Introduction]
- Cons:
  • Requires large datasets [Evidence: P012, Experiments]
  • Struggles with long sequences (memory O(n²)) [Evidence: P001, Limitations]
- Key Assumptions:
  • Sufficient training data available [Evidence: P005, Assumptions]
  • Computational resources not a constraint [Evidence: P012, Discussion]
...

[Continue through Steps 3-8]
```

## Documentation

| File | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Complete methodology and execution protocol |
| [references/QUICK_START.md](references/QUICK_START.md) | 3-minute tutorial (bilingual) |
| [references/workflow-en.md](references/workflow-en.md) | Complete 8-step workflow (English) |
| [references/workflow-zh.md](references/workflow-zh.md) | 完整8步工作流程（中文）|
| [references/templates-en.md](references/templates-en.md) | Output format templates (English) |
| [references/templates-zh.md](references/templates-zh.md) | 输出格式模板（中文）|

## Companion Skills

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| **pseudoctor-lit-search** | Keyword matrix + Boolean queries + screening | **BEFORE** this skill |
| **pseudoctor-literature-mapper** | Faction analysis + domain mapping | Current skill |
| **pseudoctor-paper-reader** | Faithful extraction with evidence binding | During deep-dive phase |
| **pseudoctor-paper-criticalreviewer** | Critical analysis + innovation delta | After understanding core papers |

**Complete workflow**:
```
pseudoctor-lit-search → pseudoctor-literature-mapper → pseudoctor-paper-reader → pseudoctor-paper-criticalreviewer
(Find & Screen)         (Organize & Map)                (Understand)             (Evaluate & Critique)
```

## Quality Standards

### ✅ Good Domain Map Characteristics

- Clear faction boundaries with defining characteristics
- Evidence-based pros/cons (from A/I/C only)
- Chronological organization showing evolution
- Mutual criticisms explicitly extracted
- Realistic convergence to 20 core papers
- Actionable innovation opportunities

### ❌ Poor Domain Map Characteristics

- Vague or overlapping faction definitions
- Unsupported claims (no evidence citations)
- Missing timeline or evolution analysis
- No mutual criticism extraction
- Unclear convergence rationale
- Generic innovation suggestions

## Version & Status

- **Version**: 2.0 (Bilingual)
- **Last Updated**: 2026-01-13
- **Status**: Production Ready ✅
- **Languages**: Bilingual (Chinese/English)

---

## Getting Started

1. **Complete first-round screening** with `pseudoctor-lit-search` to get 30-40 papers
2. **Prepare screening table** with Title, Authors, Year, 1-sentence_Summary
3. **Run the skill**: `/pseudoctor-literature-mapper [paste screening table]`
4. **Review domain map** in Step 2, decide on continuing to Step 3
5. **Get convergence** to ~20 core papers + 2-3 factions for deep-dive
6. **Follow deep reading plan** with 3A/3B/3C/3D framework

**Ready to map your domain?** Try: `/pseudoctor-literature-mapper [paste screening table]` 🚀
