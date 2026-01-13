# Pseudoctor Paper Reader

> Faithful and structured paper extraction with evidence binding. Extract structured information from academic papers without speculation or external knowledge injection.

## Overview

**Pseudoctor Paper Reader** is a faithful paper reading assistant that:

- **Extracts only what's in the original text** - No speculation or guessing
- **Binds every claim to evidence** - Direct quotes with precise locations
- **Auto-identifies paper type** - Empirical/Technical, Philosophical/Speculative, or Hybrid
- **Outputs structured cards** - Reusable, auditable summaries with traceable evidence

This is the **third stage** of a complete literature analysis workflow. Use it **after** `pseudoctor-literature-mapper` has identified must-read papers.

## Key Features

### 1. Faithful Extraction (Zero Hallucination)

**Supreme Principle**: All outputs must have clear basis in original text

- **【原文未明确说明】** - Original text does not explicitly state
- **【无法从原文唯一推出】** - Cannot be uniquely inferred from original text
- **【原文未提供相关部分】** - Original text does not provide relevant section

### 2. Evidence Binding

Every key conclusion/point includes:

1. **Evidence excerpt** - 20-50 word direct quote
2. **Location marker** - Precise positioning in descending specificity:
   - **Best**: Page + Section + Paragraph (e.g., "p.5, Method-2.1, para.2")
   - **Good**: Section + Paragraph (e.g., "Introduction, para.3")
   - **Acceptable**: Section + Description (e.g., "Related Work, second-to-last paragraph")

### 3. Automatic Paper Type Recognition

| Paper Type | Identification Criteria | Output Modules |
|------------|------------------------|----------------|
| **Empirical/Technical** | Has Method/Algorithm/Experiments/Results structure | D1: 3A/3B/3C/Verification |
| **Philosophical/Speculative** | Focuses on arguments, conceptual analysis | D2: Concept—Argument—Objection—Boundary |
| **Hybrid** | Both empirical evaluation AND philosophical argumentation | D1 + D2 merged sections |
| **Undetermined** | Insufficient information | Output based on available content |

### 4. Structured Paper Reading Card

**Universal Sections** (all paper types):
- **0**: Paper ID (Title, Authors, Venue, Year, Scope)
- **1**: Problem & Motivation
- **2**: Key Contribution / Central Claim

**Branch Modules** (by paper type):

#### For Empirical/Technical Papers (D1):
- **3A**: Assumptions (Conditions for validity)
- **3B**: Benefits/Claims (Advantages under assumptions)
- **3C**: Method Skeleton (Key steps/formulas, 3-5 key points)
- **Verification**: Experiments/Evaluation (What was validated)
- **3D**: Limitations (Explicitly admitted + potential drawbacks)
- **Applicability**: Best/worst use cases

#### For Philosophical/Speculative Papers (D2):
- **Key Concepts**: Terminology table with definitions
- **Distinctions & Framework**: Key A vs B distinctions
- **Argument Skeleton**: Premise → Inference → Conclusion chain
- **Argument Audit**: Support correspondence, objections, counterexamples
- **Limitations / Open Questions**: Admitted limitations
- **Scope & Applicability**: Discussion boundaries and qualifiers

**Closing Sections** (all paper types):
- **9**: What to Steal (Reusable ideas/frameworks)
- **10**: Ambiguities & Missing Pieces

### 5. Conceptual Skeleton Extraction

**Skip Proofs, Extract Ideas**:
- Focus on "conceptual architecture/core ideas/argumentation structure"
- Skip intermediate derivations/minor details (but MUST declare what was skipped)
- Extract only key skeleton that will ultimately be used

## When to Use

- **Understanding research papers** without external bias
- **Creating auditable summaries** with traceable evidence
- **Extracting reusable insights** and frameworks from academic texts
- **Multi-round paper discussion** with evidence-based responses
- **Literature review preparation** requiring accurate citation
- **Teaching/learning** from papers with verifiable sources

## Quick Start

```
/pseudoctor-paper-reader [paste paper text]
```

### Input Requirements

| Aspect | Requirement |
|--------|-------------|
| **Format** | Academic paper text (full or sections) |
| **Language** | Any language (original preserved in evidence) |
| **Scope** | Title + Abstract minimum; Abstract + Introduction + Conclusion recommended |

## Output Structure

### Paper Reading Card (In Strict Order)

```
0) Paper ID
   - Title, Authors, Venue/Year, Text scope description

1) Problem & Motivation
   - One-sentence problem definition + evidence + location
   - Why important + evidence + location

2) Key Contribution / Central Claim
   - Core contribution in ≤5 sentences + evidence + location
   - How distinguished from existing work + evidence + location

[Branch: D1 or D2 based on paper type]

D1) Empirical/Technical Papers:
   3) 3A Assumptions
   4) 3B Benefits/Claims
   5) 3C Method Skeleton
   6) Experiments/Evaluation (Verification)
   7) 3D Limitations
   8) Applicability

D2) Philosophical/Speculative Papers:
   3) Key Concepts & Definitions
   4) Distinctions & Framework
   5) Argument Skeleton
   6) Argument Audit
   7) Limitations / Open Questions
   8) Scope & Applicability

[Closing Sections]
   9) What to Steal (Reusable ideas)
   10) Ambiguities & Missing Pieces
```

## Language Support

### Global Rule: Internal Processing

- **Always use English** for paper analysis, section identification, technical terminology, and internal reasoning
- **Rationale**: Academic papers use English terminology; ensures precision in extraction and evidence binding

### Output Language

- **Detect user's language** (Chinese/English/Mixed) from input
- **Match output language** to user's preference automatically
- **Bilingual elements**:
  - Paper titles: Always English (original)
  - Technical terms: Always English (e.g., "self-attention", "transformer")
  - Evidence quotes: Always original language (usually English)
  - Card field labels: Match user's input language (e.g., "问题定义 / Problem" or "Problem")
  - Explanations: Match user's input language

### Domain-Specific Language Exceptions

**For domain-specific papers** (Chinese literature, TCM, philosophy, etc.):

- **Keep technical terms in original language** with translation in parentheses
- Examples:
  - 意象 (imagery / mental image)
  - 意境 (artistic conception / aesthetic realm)
  - 辨证论治 (pattern differentiation and treatment in TCM)
  - 理 (principle/li) - translation often inadequate

**Evidence quotes**: ALWAYS preserve original language regardless of user preference (faithfulness requirement)

## Handling Contradictions & Errors

### 1. Author Self-Contradiction
- Mark BOTH claims with **【原文存在矛盾】**
- List both contradictory statements with evidence and locations
- Do NOT attempt to resolve or choose one over the other

### 2. Apparent Factual Errors
- Mark with **【疑似原文错误】**
- Quote exactly as written, do NOT correct
- Briefly note why you suspect an error

### 3. Ambiguous/Unclear Statements
- Mark with **【原文表述不明确】**
- List possible interpretations if 2-3 clear ones exist

### 4. Missing Critical Sections
- Explicitly list in Section 10 (Ambiguities & Missing Pieces)
- Specify: **【需要[章节名]以完成[哪些栏位]】**

## Documentation

| File | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Complete methodology (50KB) |
| [references/QUICK_START.md](references/QUICK_START.md) | 5-minute tutorial with examples |
| [references/example_empirical.md](references/example_empirical.md) | Transformer paper (empirical) |
| [references/example_philosophical.md](references/example_philosophical.md) | Gettier paper (philosophical) |

## Usage Example

```
User: [Pastes Transformer paper text]

[Output]:

类型判断 / Type Judgment: 【实证/技术论文】(Empirical/Technical Paper)
Rationale: Original text contains clear Method/Experiments/Results/Evaluation structure

---

## Paper Reading Card

### 0) Paper ID
- **Title**: Attention Is All You Need
  证据摘录: "Attention Is All You Need"
  位置标记: Title page

- **Authors**: Vaswani et al.
  证据摘录: "Ashish Vaswani, Noam Shazeer, Niki Parmar, ..."
  位置标记: Title page

...

### 1) Problem & Motivation
- **One-sentence problem definition**:
  Recurrent neural networks (RNNs) suffer from sequential computation that prevents parallelization during training.
  证据摘录: "The predominant approach... sequential computation... precludes parallelization within training examples"
  位置标记: Introduction, para.1

...

### 3A) Assumptions
- **Assumption 1**: Self-attention can capture long-range dependencies without recurrence
  证据摘录: "The Transformer... allows... significantly more parallelization"
  位置标记: Abstract, para.2

...

[Continue through all sections with evidence binding]
```

## Quality Standards

### ✅ Good Paper Reading Card Characteristics

- Every claim has evidence excerpt (20-50 words) + location marker
- Used 【】markers correctly and consistently
- Type judgment matches actual output sections (D1/D2/Hybrid)
- Using original text terminology (not paraphrasing)
- Skipped details explicitly declared in "跳过说明"
- No external knowledge or common sense used to fill gaps

### ❌ Poor Paper Reading Card Characteristics

- Claims without evidence or vague location markers
- Missing 【】markers for unsupported content
- Wrong output structure (D1 for philosophical paper, etc.)
- Paraphrasing with own words instead of original terminology
- Unclear what was skipped vs. extracted
- External knowledge injected to "complete" analysis

## Companion Skills

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| **pseudoctor-lit-search** | Literature search and screening | Start of workflow |
| **pseudoctor-literature-mapper** | Domain mapping and faction analysis | After screening |
| **pseudoctor-paper-reader** | Faithful extraction with evidence binding | Current skill |
| **pseudoctor-paper-criticalreviewer** | Critical analysis and innovation assessment | After understanding |

**Complete workflow**:
```
pseudoctor-lit-search → pseudoctor-literature-mapper → pseudoctor-paper-reader → pseudoctor-paper-criticalreviewer
(Find & Screen)         (Organize & Map)                (Understand)             (Evaluate & Critique)
```

## Comparison: Pseudoctor vs Critical Reviewer

| Aspect | Pseudoctor Paper Reader | Critical Reviewer |
|--------|------------------------|-------------------|
| **Question** | "What does it say?" | "What does it mean?" |
| **Output** | 40+ fields, evidence-bound | 5 sections, high-density |
| **Stance** | Neutral recorder | Critical evaluator |
| **External knowledge** | ❌ Never | ✅ When justified |
| **Length** | 2000+ words | 500-800 words |
| **Best for** | Citations, lit reviews | Reviews, decisions |
| **Evidence binding** | Every claim with quotes | Key insights with evidence |
| **Paper types** | Auto-detects 3 types | Unified 5-section output |

**Use together** for complete understanding!

## Integration Workflow

### Two-Stage Deep Dive (Recommended)
```
Paper
  ↓
[Pseudoctor Paper Reader] → Factual card (40+ fields)
  ↓
[Critical Reviewer] → Insights (5 sections)
  ↓
Complete understanding
```

### Quick Triage
```
Paper
  ↓
[Critical Reviewer] → Sections 1-3
  ↓
Worth reading? YES → [Pseudoctor Paper Reader] for details
               NO → Skip paper
```

### Comparative Analysis
```
Papers A, B, C
  ↓
[Pseudoctor Paper Reader] × 3 → Factual cards
  ↓
[Critical Reviewer] → Compare Section 3 (Innovation Delta)
  ↓
Method selection
```

## Limitations

### This Skill DOES

✅ Extract faithfully from provided text only
✅ Bind every claim to evidence with location
✅ Identify paper type automatically
✅ Output structured, auditable reading cards
✅ Handle contradictions/errors in original text
✅ Support domain-specific language preservation

### This Skill DOES NOT

❌ Inject external knowledge or common sense
❌ Speculate or guess missing information
❌ Replace reading the original paper
❌ Generate new research ideas
❌ Provide literature surveys
❌ Make accept/reject decisions

## Version & Status

- **Version**: 1.0
- **Last Updated**: 2026-01-13
- **Companion Skills**: pseudoctor-paper-criticalreviewer, pseudoctor-lit-search, pseudoctor-literature-mapper
- **Status**: Production Ready ✅
- **Languages**: Bilingual (Chinese/English)

## Getting Started

1. **Prepare your paper** - Full text or key sections (Abstract + Introduction + Conclusion minimum)
2. **Run the skill**: `/pseudoctor-paper-reader [paste paper text]`
3. **Review output** - Check evidence binding and completeness
4. **Follow up** - Ask questions about specific sections for deeper extraction
5. **Optional**: Use `/pseudoctor-paper-criticalreviewer` for critical insights

**Ready to read?** Try: `/pseudoctor-paper-reader [paste your paper text]` 🚀
