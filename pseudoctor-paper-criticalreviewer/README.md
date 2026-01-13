# Pseudoctor Paper Critical Reviewer

## Overview

A **critical analysis skill** that penetrates academic jargon to reveal core insights, innovation deltas, and boundary conditions.

**Companion to**: [pseudoctor-paper-reader](../pseudoctor-paper-reader) - Use together for complete understanding.

---

## Quick Start

### 3-Second Pitch
"Transforms dense papers into 5-section insights: Problem → Solution → Innovation → Boundaries → Essence"

### Install & Use
```bash
# Use directly
/pseudoctor-paper-criticalreviewer [paste paper text]

# Or after pseudoctor
/pseudoctor-paper-reader [paper]  # Get facts
/pseudoctor-paper-criticalreviewer [same paper]  # Get insights
```

### Example Output
```
1. 核心痛点: RNNs can't parallelize (sequential bottleneck)
2. 解题机制: "Attention replaces recurrence" + scaled dot-product
3. 创新增量: 2x speed, +2 BLEU, paradigm shift
4. 批判性边界: Assumes O(n²) memory (hidden limitation!)
5. 一言以蔽之: Attention(Q,K,V) = softmax(QK^T/√d_k)V
```

---

## Documentation

| File | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Complete methodology & execution protocol |
| [QUICK_START.md](references/QUICK_START.md) | 3-min tutorial with examples |
| [INTEGRATION_GUIDE.md](references/INTEGRATION_GUIDE.md) | How to combine with pseudoctor-paper-reader |
| [example_empirical.md](references/example_empirical.md) | Full review: Transformer paper |
| [example_philosophical.md](references/example_philosophical.md) | Full review: Gettier paper |

---

## Key Features

### 🎯 High-Density Output
- 5 sections, 500-800 words total
- No filler, every sentence is actionable
- Plain language (no jargon parroting)

### 🔍 Penetrating Analysis
- Identifies the 1-2 "神来之笔" (critical tricks)
- Extracts hidden assumptions authors don't state
- Reveals boundaries where methods fail

### ⚡ Fast Triage
- Quick assessment: Is this worth reading?
- Compare innovations: Which paper is paradigm-shifting?
- Applicability check: Will this work for MY problem?

### 🤝 Integrates with Pseudoctor
- Pseudoctor = WHAT (facts with evidence)
- Critical Reviewer = SO WHAT (insights & boundaries)
- Together = Complete understanding

---

## Use Cases

| Task | Recommended Workflow |
|------|---------------------|
| **Paper review/evaluation** | Critical Reviewer → (verify with Pseudoctor) |
| **Quick paper triage** | Critical Reviewer only (Sections 1-3) |
| **Deep understanding** | Pseudoctor → Critical Reviewer → Synthesize |
| **Method selection** | Critical Reviewer (compare Section 3 deltas) |
| **Literature survey** | Critical Reviewer (essence) + Pseudoctor (citations) |
| **Teaching/Explaining** | Critical Reviewer Section 5 (napkin diagram) |

---

## Philosophy

### What This Skill Is
- A **sharp peer reviewer** who cuts through superficiality
- Focused on **essence** over comprehensiveness
- **Rigorous but fair** - celebrates innovation, exposes weak reasoning

### What This Skill Is NOT
- Not a summarizer (distills, not paraphrases)
- Not a fact recorder (that's pseudoctor's job)
- Not a decision-maker (provides analysis, not verdicts)

---

## Output Structure

### 1. 核心痛点 (Core Problem)
- One-sentence problem definition
- Why previous approaches failed (with category)

### 2. 解题机制 (Solution Mechanism)
- Core "aha moment" insight (plain language)
- The 1-2 critical tricks ("神来之笔")

### 3. 创新增量 (Innovation Delta)
- Concrete improvements vs SOTA (with numbers!)
- What puzzle piece this adds to knowledge

### 4. 批判性边界 (Critical Boundaries)
- Hidden assumptions (with impact analysis)
- Unsolved problems & new issues introduced

### 5. 一言以蔽之 (Essence on a Napkin)
- ASCII diagram of core mechanism
- The ONE formula/principle that captures everything

---

## Examples

### Transformer Paper (Empirical)
```
核心直觉: "Attention can replace recurrence entirely, not just augment it"

神来之笔: Scaled dot-product (QK^T/√d_k) enables parallel all-to-all
attention without sequential dependencies

隐形假设: O(n²) memory is acceptable
→ Limits sequence length to ~1000 tokens
→ Paper doesn't discuss this! (discovered later)

一言以蔽之:
  Input → [Multi-Head Attention] → [FFN] → Output
           ↑_____________| (no recurrence!)
```

### Gettier Paper (Philosophical)
```
核心直觉: "Knowledge requires the RIGHT connection between belief
and truth, not just ANY connection"

神来之笔: Use opponent's own principle (entailment preserves
justification) to construct counterexamples

隐形假设: Intuitions about knowledge cases are reliable
→ If wrong, entire argument collapses
→ Experimental philosophy later showed cross-cultural variation

一言以蔽之:
  P (false) → S justified in believing P
      ↓ entailment
  Q (true) → S has JTB in Q
  But: Q is true by LUCK → not knowledge
```

---

## Comparison: Pseudoctor vs Critical Reviewer

| Aspect | Pseudoctor | Critical Reviewer |
|--------|-----------|-------------------|
| **Question** | "What does it say?" | "What does it mean?" |
| **Output** | 40+ fields, evidence-bound | 5 sections, high-density |
| **Stance** | Neutral recorder | Critical evaluator |
| **External knowledge** | ❌ Never | ✅ When justified |
| **Length** | 2000+ words | 500-800 words |
| **Best for** | Citations, lit reviews | Reviews, decisions |

**Use together** for complete analysis!

---

## Integration Workflow

### Two-Stage Deep Dive (Recommended)
```
Paper
  ↓
[Pseudoctor] → Factual card (40+ fields)
  ↓
[Critical Reviewer] → Insights (5 sections)
  ↓
Decision
```

### Quick Triage
```
Paper
  ↓
[Critical Reviewer] → Sections 1-3
  ↓
Worth reading? YES → [Pseudoctor] for details
               NO → Skip paper
```

### Comparative Analysis
```
Papers A, B, C
  ↓
[Pseudoctor] × 3 → Factual cards
  ↓
[Critical Reviewer] → Compare Section 3 (Innovation Delta)
  ↓
Method selection
```

---

## Quality Standards

### ✅ Good Critical Review
- Reveals core mechanism (not just lists features)
- Provides concrete evidence (numbers, theorems)
- Identifies specific assumptions (not vague "may require data")
- Enables reader to judge applicability

### ❌ Bad Critical Review
- Paraphrases abstract
- Lists all contributions equally
- Vague criticism ("may not work in all cases")
- No evidence for claims

---

## Getting Started

1. **Read**: [QUICK_START.md](references/QUICK_START.md) (3 minutes)
2. **See examples**:
   - [Empirical paper review](references/example_empirical.md)
   - [Philosophical paper review](references/example_philosophical.md)
3. **Try it**: `/pseudoctor-paper-criticalreviewer [paste your paper]`
4. **Learn workflow**: [INTEGRATION_GUIDE.md](references/INTEGRATION_GUIDE.md)

---

## Files

```
pseudoctor-paper-criticalreviewer/
├── SKILL.md                    # Complete methodology (11KB)
├── README.md                   # This file
└── references/
    ├── QUICK_START.md          # 3-min tutorial (9KB)
    ├── INTEGRATION_GUIDE.md    # Workflow patterns (15KB)
    ├── example_empirical.md    # Transformer review (8KB)
    └── example_philosophical.md # Gettier review (10KB)

Total: ~53KB of documentation
```

---

## Limitations

### This skill DOES
✅ Cut through jargon to reveal mechanisms
✅ Identify hidden assumptions
✅ Evaluate innovation with evidence
✅ Provide actionable insights

### This skill DOES NOT
❌ Replace reading the paper
❌ Generate new research ideas
❌ Provide literature surveys
❌ Make accept/reject decisions

---

## Integration with Literature Workflow

This skill integrates with the complete literature analysis pipeline:

```
pseudoctor-lit-search → pseudoctor-literature-mapper → pseudoctor-paper-reader → pseudoctor-paper-criticalreviewer
(Find & Screen)         (Organize & Map)                (Understand)             (Evaluate & Critique)
```

**Use this skill** when you need to:
- Evaluate the innovation delta of core papers
- Assess applicability to your specific problem
- Compare multiple approaches
- Prepare for peer review or paper evaluation

## Companion Skills

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| **pseudoctor-lit-search** | Literature search and screening | Start of workflow |
| **pseudoctor-literature-mapper** | Domain mapping and faction analysis | After screening |
| **pseudoctor-paper-reader** | Faithful paper extraction | Before critical review |
| **pseudoctor-paper-criticalreviewer** | Critical analysis and innovation assessment | Current skill |

## Version & Status

- **Created**: 2026-01-11
- **Last Updated**: 2026-01-13
- **Version**: 1.0.0
- **Companion Skills**: pseudoctor-paper-reader, pseudoctor-lit-search, pseudoctor-literature-mapper
- **Status**: Production Ready ✅

---

## License & Credits

Created as companion to **pseudoctor-paper-reader**.

**Special Thanks**: This skill is inspired by and builds upon the "论文X光机" (Paper X-Ray) prompt by **李继刚 (@lijigang)**. The original prompt philosophy emphasizes:
- 去噪 (denoise) → 提取 (extract) → 批判 (critique)
- High-density output, no filler
- Structural thinking over superficial summarization
- Revealing core mechanisms and hidden assumptions

The "论文X光机" prompt has been adapted and extended to integrate with the pseudoctor literature analysis workflow, adding evidence binding, bilingual support, and companion skill integration.

---

## Support

- **Questions**: See [QUICK_START.md](references/QUICK_START.md) FAQ
- **Workflow help**: See [INTEGRATION_GUIDE.md](references/INTEGRATION_GUIDE.md)
- **Examples**: Check [references/](references/) directory

---

**Ready?** Try: `/pseudoctor-paper-criticalreviewer [paste your paper text]` 🚀
