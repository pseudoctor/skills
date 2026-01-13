# Article Analysis Master

> A comprehensive analytical tool for structured article summarization, argumentation analysis, core insight extraction, Feynman-style explanations, and writing style assessment.

## Overview

**Article Analysis Master** conducts in-depth analysis of provided articles from the perspective of a senior scholar/editor. It strictly bases analysis on original content, uses the Toulmin argumentation model to examine argument chains and hidden assumptions in argumentative articles, and flexibly adjusts the analytical framework based on article type.

## Key Features

### Comprehensive Analysis Framework

- **Article Type Recognition**: Automatically identifies and adapts to:
  - Academic papers
  - Commentaries/Op-eds
  - News reports
  - Narrative essays
  - Surveys/Reviews

- **Argumentative Analysis** (for argumentative articles):
  - Toulmin model breakdown (Claim, Data, Warrant, Backing, Qualifier, Rebuttal)
  - Argument structure strength assessment
  - Identification of potential weaknesses

- **Narrative Analysis** (for non-argumentative articles):
  - Structural organization analysis
  - Narrative technique evaluation
  - Content presentation characteristics

### Core Outputs

1. **Structured Summary** - 2-5 main topics with key points and supporting details
2. **Core Viewpoints & Insights** - Key arguments, unique perspectives, and challenging points
3. **Toulmin Argument Analysis** - Complete breakdown of argumentation structure
4. **Feynman Learning Explanation** - Simple explanations using everyday analogies
5. **Learning Resources** - Curated recommendations based on article themes
6. **Visualization Suggestions** - 2-3 proposals for data/concept representation
7. **Q&A Section** - 3-5 questions across cognitive levels (understanding, application, critical, extended)
8. **Writing Style Analysis** - Introduction strategy, structure, transitions, tone, language features

## When to Use

- **Academic reading** - Deeply understand research papers and essays
- **Critical reading** - Analyze argumentation quality and logical structure
- **Literature review preparation** - Extract and organize key insights from multiple sources
- **Teaching & learning** - Create educational explanations of complex content
- **Content analysis** - Evaluate writing style and rhetorical strategies

## Quick Start

```
/article-analysis-master [paste your article text]
```

### Input Validation Requirements

| Requirement | Minimum Threshold |
|-------------|-------------------|
| **Word count** | ≥ 100 words |
| **Format** | Text with paragraph structure |
| **Completeness** | Full article (not abstract only) |

If input doesn't meet requirements, the skill will prompt for appropriate content.

## Usage Example

```
User: Please analyze this academic paper on transformer architecture...

[Article Analysis Master Output]:

Zero: Article Type Judgment
- Article Type: Academic Paper
- Framework: Argumentative Analysis (Complete 10-step)

One: Basic Information
1. Title: Attention Is All You Need
2. Authors: Vaswani et al.
...

Two: Structured Summary
### Core Innovation
**The transformer architecture entirely replaces recurrence with attention mechanisms**
[Detailed summary with evidence]

Three: Core Viewpoints and Key Insights
...

Four: Toulmin Model Argument Analysis
...

[Continue through all sections]
```

## Output Structure

### For Argumentative Articles

1. **Article Type Judgment** - Classification and framework selection
2. **Basic Information** - Title, author, venue, keywords, abstract, core conclusion
3. **Structured Summary** - Main topics with key points
4. **Core Viewpoints & Insights** - Arguments, unique insights, challenging points
5. **Toulmin Argument Analysis** - Complete structural breakdown
6. **Feynman Learning Explanation** - Simple analogy-based explanation
7. **Learning Resources** - Curated recommendations
8. **Visualization Suggestions** - Data/concept representation proposals
9. **Q&A** - Multi-level questions and answers
10. **Writing Style Analysis** - Rhetorical strategy assessment

### For Non-Argumentative Articles

Sections 1-3, 5-10 remain the same, with **Section 4** replaced by:
- **Narrative Structure/Content Organization Analysis** - Structure type, organization, narrative techniques, presentation characteristics

## Language Support

- **Input**: Simplified Chinese, English, or mixed
- **Output**: Simplified Chinese (maintains original language for titles/author names with translations)
- **Names**: Standardized format with bilingual rendering
  - Foreign names in Chinese articles: "约翰·史密斯 (John Smith)"
  - Chinese names: "李明 (Li Ming)"

## Core Principles

### Faithfulness
- Analysis based **only** on original text
- Explicitly mark content not verifiable from source: "【原文未提及】" (Not mentioned in original)
- Only external resources allowed: clearly marked "（推荐资源，非原文内容）" (Recommended resource, not from original)

### Critical Thinking
- Focus on identifying unstated assumptions and logical weak points
- Avoid empty generalizations
- Provide specific, evidence-based analysis

### Depth Over Breadth
- Prefer deep analysis of few key points
- Avoid superficial coverage of all sections

## Documentation

| File | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Complete methodology and execution protocol |
| [references/quick-guide.md](references/quick-guide.md) | Quick start guide |
| [references/example-analysis.md](references/example-analysis.md) | Complete analysis example |

## Example Use Cases

### Case 1: Academic Paper Analysis
```
Input: Research paper on machine learning
Output:
- Problem definition and motivation
- Methodological approach (3A/3B/3C framework)
- Experimental evaluation coverage
- Limitations and applicability
```

### Case 2: Commentary/Essay Analysis
```
Input: Opinion piece on climate policy
Output:
- Argument structure (Toulmin model)
- Hidden assumptions identification
- Logical fallacy detection
- Persuasive strategy analysis
```

### Case 3: Narrative Text Analysis
```
Input: Literary essay or memoir
Output:
- Narrative structure assessment
- Thematic organization
- Stylistic device analysis
- Emotional tone evaluation
```

## Quality Standards

### ✅ Good Analysis Characteristics

- Every claim grounded in original text with specific references
- Explicit marking of inferences vs. direct statements
- Balanced critical assessment (acknowledges contributions and limitations)
- Clear section structure following template
- Specific examples and evidence excerpts

### ❌ Poor Analysis Characteristics

- Unsupported assertions or external knowledge injection
- Superficial paraphrasing without insight
- Missing section on argument structure (for argumentative pieces)
- Vague criticism without specific evidence
- Incomplete template sections

## Limitations

### This Skill DOES

✅ Analyze structure and argumentation based on provided text
✅ Extract and organize key viewpoints with evidence binding
✅ Identify assumptions and logical gaps
✅ Provide educational explanations (Feynman technique)
✅ Recommend relevant learning resources

### This Skill DOES NOT

❌ Retrieve external information or verify claims
❌ Generate new research ideas
❌ Replace domain expert evaluation
❌ Handle extremely short texts (<100 words)
❌ Process pure data tables without narrative

## Version & Status

- **Version**: 1.0
- **Last Updated**: 2026-01-13
- **Status**: Production Ready ✅
- **Language**: Primarily Chinese output with English technical terms

## Integration Notes

This skill is designed for standalone article analysis and does not require companion skills. For academic paper workflows, consider pairing with:

- **pseudoctor-lit-search** - Literature search and screening
- **pseudoctor-paper-reader** - Faithful paper extraction
- **pseudoctor-paper-criticalreviewer** - Critical paper evaluation

---

## Getting Started

1. **Prepare your article** - Ensure text is ≥100 words with clear structure
2. **Run the skill**: `/article-analysis-master [paste article text]`
3. **Review output** - Check all 10 sections for completeness
4. **Follow up** - Ask questions about specific sections for deeper analysis

**Ready to analyze?** Try: `/article-analysis-master [paste your article]` 🚀
