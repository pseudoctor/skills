# Pseudoctor Literature Search

> Academic domain search and rapid screening expert. Quickly build keyword matrices, generate Boolean search queries, create screening table templates, and filter from hundreds of papers to the most relevant 20-30.

## Overview

**Pseudoctor Literature Search** helps you conduct systematic literature reviews by:

1. **Finding comprehensively** ("找全") - Build comprehensive keyword matrices
2. **Filtering rapidly** ("筛快") - Screen hundreds of papers down to 20-30 core papers
3. **Multiple output formats** - TSV/CSV/Markdown/Notion/Feishu/Google Sheets

This is the **first stage** of a complete literature analysis workflow. Use it before `pseudoctor-literature-mapper` for domain mapping and faction analysis.

## Key Features

### 1. Keyword Matrix Generation

Automatically generates comprehensive keyword categories:

| Category | Purpose | Minimum Count |
|----------|---------|---------------|
| **Core Concepts** | Central domain concepts | 3-8 |
| **Synonyms/Variants** | Alternate terms and abbreviations | ≥5 per concept |
| **Tasks/Applications** | Use cases and applications | ≥10 |
| **Methods/Models/Metrics** | Technical approaches | ≥10 (or "待补" if unknown) |
| **Exclusion Terms** | Filter irrelevant directions | ≥10 |

### 2. Boolean Search Query Builder

Generates **3 types of optimized queries**:

- **Broad Recall**: OR-heavy, maximum coverage
- **Precision Recall**: AND-heavy, focused results
- **Review-Specific**: Targets surveys, overviews, meta-analyses

Each query includes:
- Directly pasteable search string
- Database compatibility notes
- Tuning guidance (how to loosen/tighten)

**Database Syntax Support**: Google Scholar, Web of Science, PubMed, Scopus, IEEE Xplore, arXiv

### 3. Rapid Screening SOP

Two-stage filtering process:

```
Initial Results (hundreds of papers)
      ↓ First Round (Title + Abstract, ≤2 min/paper)
30-40 papers (preliminary relevance)
      ↓ Second Round (Introduction + Conclusion, ≤6 min/paper)
20-30 papers (high relevance, ready for deep analysis)
```

**First Round Signals** (Title + Abstract):
- ✅ Include: Core keywords in title, explicit research questions/methods/results in abstract
- ❌ Exclude: Different domain, pure theory without validation, wrong language, non-academic content

**Second Round Signals** (Introduction + Conclusion):
- ✅ Include: Clear research gap/contribution, can critique others' work, concrete results/insights in conclusion
- ✅ Priority: Papers with experimental/case support
- ❌ Exclude: Repetitive work, no clear contribution

### 4. Screening Table Template

**17 Essential Fields** (bilingual):

| Field | Description | Type |
|-------|-------------|------|
| Paper_ID | Unique identifier (P001, P002...) | Text |
| Title | Full paper title | Text |
| Authors | First author or "First author et al." | Text |
| Year | Publication year | Number |
| Venue/Source | Journal/Conference name | Text |
| URL/DOI | Access link or DOI | URL |
| Material_Type | Journal/Conference/arXiv/Survey | Select |
| Keywords_Matched | Which search keywords matched | Text |
| Task/Application | What problem it solves | Text |
| First_Read | Completed first-round reading (Y/N) | Checkbox |
| 1-sentence_Summary | What the paper does (20-40 words) | Text |
| Relevance_Score | 0-5 rating, 5 = most relevant | Number |
| Reason_Keep_or_Drop | Why kept or dropped | Text |
| Is_Review | Survey paper flag (Y/N) | Checkbox |
| Candidate_School | Preliminary faction classification | Text |
| Must_Read_Level | Must-read/Optional/Skim | Select |
| Notes | Other remarks | Text |

### 5. Multiple Output Formats

| Option | Format | Best For |
|--------|--------|----------|
| **A** | TSV (tab-separated) | Excel/Sheets/Feishu paste ⭐ Recommended |
| **B** | CSV (comma-separated) | Database import, programmatic processing |
| **C** | Markdown table | Documentation, Notion, readability |
| **D** | Notion schema | Notion database setup with field types |
| **E** | Feishu/Multidimensional schema | Feishu multidimensional tables |
| **F** | Google Sheets friendly | TSV + data validation rules |

## When to Use

- **Learning a new domain** - Need to quickly build a knowledge map
- **Systematic Literature Review** - Comprehensive coverage with quality filtering
- **Literature review sections** - Pre-writing research organization
- **Understanding research frontiers** - Quick overview of recent progress
- **Project technical due diligence** - Pre-project feasibility research
- **PhD proposal/Grant application** - Thorough literature groundwork

## Quick Start

```
/pseudoctor-lit-search I want to research [your topic]
```

### Initial Information Needed

| Field | Required | Default |
|-------|----------|---------|
| Research topic/domain | ✅ Yes | - |
| Sub-problem/application | ✅ Yes | - |
| Time range | Optional | Last 10 years |
| Focus | Optional | Theory + Application |
| Material types | Optional | Journals + Conferences + arXiv |
| Target database | Optional | Auto-recommend |
| Languages | Optional | Chinese + English |
| Target scale | Optional | Round 1: 30-40, Round 2: 20-30 |

## Usage Workflow

### Stage A: Initialization

1. **Gather inputs** - Ask minimal questions, use defaults with 【假设】 marking
2. **Choose output format** - Select from options A-F (asked only once)

### Stage B: Generation

After format selection, output in strict order:

1. **Keyword Matrix** - Core concepts, synonyms, tasks, methods, exclusions
2. **Boolean Search Queries** - At least 3 sets with database syntax guides
3. **Screening SOP** - First and second-round standards with signals
4. **Screening Table Template** - 17 fields in chosen format with 2 example rows
5. **Step 1 Reading Instructions** - How to batch-read Abstract+Introduction

### Stage C: Data Collection

**Reading Strategy** (Review-First):
1. **Prioritize surveys** (Is_Review = Y): Fast domain overview
2. **Highly-cited papers**: Usually important work
3. **Recent 3 years**: Latest progress
4. **All core keywords hit**: Highest relevance

**1-Minute Note Fields** (minimum required):
- Paper_ID, Title
- 1-sentence_Summary (20-40 words)
- Relevance_Score (0-5)
- Keywords_Matched
- Reason_Keep_or_Drop

### Stage D: Pass to Next Stage

**Minimum data package**:
- Complete screening table (30-40 rows)
- 1-sentence summaries for each

**Complete data package** (recommended):
- Screening table
- Abstract+Introduction key points for each
- List of survey papers (Is_Review = Y)

**Data handoff**: Pass screening table directly to `pseudoctor-literature-mapper` for faction analysis and deep dive.

## Language Support

### Global Rule: Internal Processing

- **Always use English** for search queries, keyword generation, Boolean expressions, and internal reasoning
- **Rationale**: Academic databases primarily use English indexing; English keywords yield more comprehensive results

### Output Language

- **Detect user's language** (Chinese/English/Mixed) from input
- **Match output language** to user's preference automatically
- **Bilingual elements**:
  - Keywords: Always English (with Chinese translation in parentheses if user is Chinese)
  - Boolean queries: Always English (industry standard)
  - Table headers: Bilingual (e.g., "标题 / Title", "作者 / Authors")
  - Explanations: Match user's input language

### Domain-Specific Language Exceptions

**Critical Override**: The "Always use English" rule has important exceptions for:

**Category A**: Language & Literature Studies
- Chinese Literature → Use Chinese keywords
- Japanese Literature → Use Japanese keywords

**Category B**: Regional & Political Studies
- Chinese Politics & Ideology → Use Chinese
- Regional Studies → Use regional language

**Category C**: Traditional & Cultural Studies
- Traditional Chinese Medicine → Use Chinese
- Buddhism & Religious Studies → Use source language

**Category D**: Local Legal & Social Systems
- National legal systems → Use official language

For domain-specific fields, use **parallel bilingual search**:
1. Primary search: Domain language (e.g., Chinese for Chinese literature)
2. Secondary search: English for comparative studies
3. Merge and deduplicate results

## Complete Literature Workflow

```
【Stage 1】pseudoctor-lit-search (current skill)
Input: Research topic/sub-question
Output: 30-40 core papers + screening table + keyword matrix

        ↓ (screening table as input)

【Stage 2】pseudoctor-literature-mapper
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

## Documentation

| File | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Complete methodology (50KB) |
| [references/QUICK_START.md](references/QUICK_START.md) | 5-minute tutorial |
| [references/INTEGRATION.md](references/INTEGRATION.md) | Integration guide with mapper |
| [references/example_boolean.md](references/example_boolean.md) | Boolean query examples |
| [references/example_keywords.md](references/example_keywords.md) | Keyword matrix examples |
| [references/example_table.md](references/example_table.md) | Complete screening table example |

## Usage Example

```
User: "I want to research Transformer applications in time series forecasting"

[Output]:

## 1. Keyword Matrix

### Core Concepts
- Transformer
- Time Series Forecasting
- Attention Mechanism
- Temporal Data
...

### Synonyms/Variants
- Transformer: Self-Attention Model, Attention-based Model, ...
- Time Series: Temporal Data, Sequential Data, Time-series, ...

### Tasks/Applications
- Forecasting, Prediction, Nowcasting, ...
...

### Methods/Models
- Informer, Autoformer, Transformer-based, ...
...

### Exclusions
- Image Classification, Computer Vision, Speech Recognition, ...

## 2. Boolean Search Queries

[Broad Recall Query]
("Transformer" OR "Self-Attention" OR "Attention Mechanism")
  AND ("Time Series" OR "Temporal Data")
  AND ("Forecasting" OR "Prediction")

适用数据库: Google Scholar, Scopus
调参建议:
  - 放宽: Add ("Informer" OR "Autoformer")
  - 收紧: Add AND "benchmark"

[Precision Recall Query]
...

[Review-Specific Query]
...

## 3. Screening SOP
...

## 4. Screening Table Template (TSV format)

Paper_ID	Title	Authors	Year	...
P001	[Example: Transformer for Time Series]	[Li et al.]	2023	...
...

## 5. Reading Instructions
...
```

## Quality Standards

### ✅ Good Output Characteristics

- Keyword matrix covers all 5 categories with sufficient quantity
- Boolean queries include at least 3 types with database syntax notes
- Screening SOP has clear inclusion/exclusion signals
- Screening table has all 17 fields with 2 example rows
- Example rows use placeholders (e.g., [Example Title]), not fabricated papers
- Output format matches user selection (A/B/C/D/E/F)

### ❌ Poor Output Characteristics

- Missing keyword categories or insufficient quantities
- Only 1-2 Boolean query types
- Vague screening criteria
- Missing fields in screening table
- Fabricated paper information in examples
- Wrong output format

## Iteration Protocol

### When First Round Has Problems

| Problem | Symptom | Adjustment Strategy |
|---------|---------|---------------------|
| Too few results (<100) | Keywords too narrow | Add synonyms, expand with OR |
| Too many results (>1000) | Keywords too broad | Add AND conditions, add exclusion terms |
| Low quality | Keywords imprecise | Reverse-engineer from high-quality papers |
| No surveys | Review query insufficient | Run dedicated review query |
| Poor timeliness | Year range too strict | Expand time window |
| Domain drift | Keyword ambiguity | Strengthen exclusion list |

### Iteration Flow

```
Round 1: Initial search
      ↓
Evaluate recall volume and quality
      ↓
Adjust keyword matrix / Boolean queries
      ↓
Round 2: Optimized search
      ↓
Target achieved OR continue iterating
```

## Output Quality Checklist

Before final delivery, verify:

### ✅ Section 1: Keyword Matrix
- [ ] Core concepts: 3-8
- [ ] Synonyms/variants: ≥5 per core concept
- [ ] Tasks/applications: ≥10
- [ ] Methods/models/metrics: ≥10 (or marked "待补")
- [ ] Exclusion terms: ≥10

### ✅ Section 2: Boolean Queries
- [ ] At least 3 query sets
- [ ] Includes: Broad + Precision + Review-specific
- [ ] Each has database compatibility notes
- [ ] Each has tuning guidance
- [ ] Provides database syntax conversion guide

### ✅ Section 3: Screening SOP
- [ ] First-round standards: Inclusion/exclusion lists
- [ ] Second-round standards: Decision rules
- [ ] Convergence path: Hundreds → 30-40 → 20-30

### ✅ Section 4: Screening Table
- [ ] All 17 essential fields
- [ ] Bilingual field names (Chinese/English)
- [ ] 2 example rows with placeholders
- [ ] Format matches user selection
- [ ] Examples use [brackets], not fabricated papers

### ✅ Section 5: Reading Instructions
- [ ] Review-first strategy explained
- [ ] Abstract+Introduction-only reading specified
- [ ] 1-minute note fields checklist
- [ ] Minimum data package defined
- [ ] Data handoff to literature-mapper explained

### ✅ Overall Check
- [ ] Output format matches user choice (A/B/C/D/E/F)
- [ ] No fabricated real paper information
- [ ] Next workflow step explained

## Companion Skills

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| **pseudoctor-lit-search** | Search + Screen | Start literature review (current skill) |
| **pseudoctor-literature-mapper** | Faction analysis + Deep dive | After screening 30-40 papers |
| **pseudoctor-paper-reader** | Faithful detail extraction | When deep understanding needed |
| **pseudoctor-paper-criticalreviewer** | Critical evaluation | When assessing innovation |

**Complete workflow**: Search → Screen → Factions → Deep Read → Critique → Innovate

## Version & Status

- **Version**: 2.0 (Optimized)
- **Last Updated**: 2026-01-13
- **Status**: Production Ready ✅
- **Languages**: Bilingual (Chinese/English)

---

## Getting Started

1. **Define your research topic** - Be specific about domain and questions
2. **Run the skill**: `/pseudoctor-lit-search [your topic]`
3. **Select output format** - Choose from A-F options
4. **Execute searches** - Use generated Boolean queries in databases
5. **Screen papers** - Follow two-stage SOP to converge to 20-30 papers
6. **Pass to next stage** - Use screening table with `pseudoctor-literature-mapper`

**Ready to search?** Try: `/pseudoctor-lit-search I want to research [your topic]` 🚀
