# Integration Guide: Pseudoctor + Critical Reviewer

## Overview

This guide shows how to use **pseudoctor-paper-reader** and **pseudoctor-paper-criticalreviewer** together for maximum insight.

**Core principle**: Facts first, then interpretation.

```
Pseudoctor (WHAT) → Critical Reviewer (SO WHAT) → You (NOW WHAT)
```

---

## The Two-Layer Analysis Model

### Layer 1: Factual Skeleton (Pseudoctor)
- **Question**: "What does the paper claim?"
- **Output**: Evidence-bound facts, 40+ structured fields
- **Philosophy**: Zero interpretation, pure extraction
- **Time**: 5-10 minutes of thorough reading

### Layer 2: Critical Insights (Critical Reviewer)
- **Question**: "What does it mean? What are the boundaries?"
- **Output**: 5 high-density analytical sections
- **Philosophy**: Rigorous evaluation with external knowledge
- **Time**: 3-5 minutes of distillation

### Result: Complete Understanding
- Facts + Meaning + Applicability = Decision-ready knowledge

---

## Workflow Patterns

### Pattern 1: Sequential Deep Dive (⭐ Recommended for Important Papers)

**Use when**: Writing reviews, making research decisions, deep learning

```bash
# Step 1: Extract facts
User: "Please read this paper with /pseudoctor-paper-reader"
→ Output: Complete factual card
→ Save as: paper_facts.md

# Step 2: Analyze critically
User: "Now critically review the same paper with /pseudoctor-paper-criticalreviewer"
→ Critical Reviewer can reference factual card from context
→ Output: 5-section critical analysis
→ Save as: paper_critique.md

# Step 3: Synthesize
You now have:
- What they claim (with evidence) ← Pseudoctor
- What it means (with boundaries) ← Critical Reviewer
- How to decide if it applies to YOU ← Your judgment
```

**Example prompt**:
```
I have a paper on [topic]. Please:
1. First extract facts with /pseudoctor-paper-reader
2. Then provide critical analysis with /pseudoctor-paper-criticalreviewer
3. Finally, tell me: Should I use this method for [my use case]?
```

---

### Pattern 2: Quick Triage (For Paper Filtering)

**Use when**: Deciding which papers to read fully, screening literature

```bash
# Fast track: Critical review only
User: "Quick critical review of this paper: [paste abstract + intro]"
→ Critical Reviewer provides Sections 1-3
→ You decide: Read full paper? Or skip?

# If interesting: Follow up with pseudoctor
User: "This looks relevant. Now do full extraction with /pseudoctor-paper-reader"
→ Get complete factual card
```

**Time savings**:
- Critical review: 3 min → Decide in 3 min
- Full pseudoctor: 10 min → Only for papers that pass triage

---

### Pattern 3: Comparative Analysis (For Method Selection)

**Use when**: Choosing between competing approaches, identifying SOTA

```bash
# Step 1: Extract facts from all candidates
For each paper A, B, C:
  → Run /pseudoctor-paper-reader
  → Save factual cards

# Step 2: Comparative critical analysis
User: "I have factual cards for papers A, B, C. Compare their innovation deltas."
→ Critical Reviewer focuses on Section 3 (Innovation Delta)
→ Outputs comparison table:
  - Paper A: Efficiency improvement (2x faster)
  - Paper B: Paradigm shift (new approach)
  - Paper C: Incremental (minor tweak)

# Step 3: Decision
You choose based on:
- Pseudoctor: What they actually claim (facts)
- Critical Reviewer: What's genuinely new (delta)
- Your needs: Which delta matters for your problem?
```

---

### Pattern 4: Review Writing (For Peer Review)

**Use when**: Writing conference/journal reviews, grant evaluations

```bash
# Preparation phase
1. Run /pseudoctor-paper-reader
   → Sections 3-6: Understand their method & experiments
   → Section 7: What limitations they admit
   → Section 9: What's reusable

2. Run /pseudoctor-paper-criticalreviewer
   → Section 1: Verify problem novelty
   → Section 2: Assess core insight
   → Section 3: Evaluate innovation claims
   → Section 4: Find hidden assumptions they missed

# Writing phase
Use pseudoctor for:
- ✅ "The authors claim X" (cite Section 2 evidence)
- ✅ "The experiments show Y" (cite Section 6 evidence)
- ✅ "They acknowledge Z limitation" (cite Section 7)

Use critical reviewer for:
- ✅ "The core contribution is [Section 2 insight]"
- ✅ "However, the method assumes [Section 4 assumption], which limits applicability to [scenarios]"
- ✅ "Compared to SOTA, this improves [Section 3 delta]"

# Your review structure
**Summary**: [From Critical Reviewer Section 1-2]
**Strengths**: [From Critical Reviewer Section 3]
**Weaknesses**: [From Critical Reviewer Section 4 + Pseudoctor Section 7]
**Detailed Comments**: [From Pseudoctor evidence]
**Decision**: [Your judgment]
```

---

## Skill Interaction Matrix

| You Want To... | Start With | Then Use | Output |
|---------------|------------|----------|--------|
| **Understand deeply** | Pseudoctor | Critical Reviewer | Facts + Insights |
| **Decide quickly** | Critical Reviewer | (Pseudoctor if passed) | Triage decision |
| **Write review** | Pseudoctor | Critical Reviewer | Review draft |
| **Compare methods** | Pseudoctor (all) | Critical Reviewer (compare) | Method selection |
| **Extract techniques** | Pseudoctor | (Skip Critical) | Reusable ideas |
| **Evaluate novelty** | Critical Reviewer | (Verify with Pseudoctor) | Innovation assessment |
| **Find limitations** | Critical Reviewer Sec 4 | Pseudoctor Sec 7 | Complete boundary map |
| **Teach/Explain** | Critical Reviewer Sec 5 | Pseudoctor Sec 2,5 | Napkin + Details |

---

## Example: Complete Workflow for Transformer Paper

### Step 1: Factual Extraction (Pseudoctor)
```
User: "/pseudoctor-paper-reader, please read 'Attention Is All You Need'"

Pseudoctor Output (abbreviated):
- Section 0: Vaswani et al., NeurIPS 2017
- Section 2: Core contribution = "purely attention-based architecture"
  证据摘录: "The Transformer is the first transduction model relying entirely on self-attention..."
- Section 5: Method skeleton
  Step 1: Embed + positional encoding
  Step 2: N=6 encoder layers with multi-head attention
  Formula 1: Attention(Q,K,V) = softmax(QK^T/√d_k)V
- Section 6: Experiments
  WMT'14 EN-DE: 28.4 BLEU vs 26.4 previous best
- Section 7: Limitations
  【原文未明确说明】计算复杂度问题
```

### Step 2: Critical Analysis
```
User: "/pseudoctor-paper-criticalreviewer, please analyze the same paper"

Critical Reviewer Output (abbreviated):
1. 核心痛点: RNNs prevent parallelization (sequential bottleneck)
   前人困境: ✅ Computational constraints

2. 解题机制:
   核心直觉: "Attention can replace recurrence entirely"
   神来之笔: Scaled dot-product enables parallel all-to-all attention

3. 创新增量:
   - Efficiency: 3.5 days vs weeks
   - BLEU: 28.4 vs 26.4 (+2.0)
   - Paradigm shift: First zero-recurrence seq2seq
   本质: "Proof that self-attention alone suffices for SOTA"

4. 批判性边界:
   隐形假设:
   - Assumption 1: O(n²) memory acceptable (limits to ~1000 tokens)
   - Assumption 2: Parallel hardware (8 GPUs required)
   未解之谜:
   - How to scale to long sequences (>1000 tokens)?

5. 一言以蔽之:
   Attention(Q,K,V) = softmax(QK^T/√d_k)V
   "Replace sequential propagation with parallel all-to-all attention"
```

### Step 3: Synthesis
```
You now know:

FROM PSEUDOCTOR:
✅ Exact claims with evidence locations
✅ Detailed method steps (6 layers, 8 heads, etc.)
✅ Specific experimental setup (WMT'14, beam search, etc.)
✅ What limitations authors admit (none explicitly about O(n²)!)

FROM CRITICAL REVIEWER:
✅ Core insight (attention replaces recurrence)
✅ Key innovation (parallel processing)
✅ Hidden assumption (O(n²) memory - NOT mentioned in paper!)
✅ Boundary (fails for sequences >1000 tokens)

YOUR DECISION:
"This is perfect for translation (sentences <100 tokens),
but I need to process 10K-token documents → Transformer won't work.
Need to look for Longformer/BigBird variants."
```

---

## Cross-Reference Guide

### To Verify Critical Reviewer Claims

When Critical Reviewer says something, verify with Pseudoctor:

| Critical Reviewer Claim | Pseudoctor Verification |
|------------------------|------------------------|
| "Core insight is X" | Check Section 2 (Key Contribution) evidence |
| "Improves by Y%" | Check Section 6 (Experiments) results |
| "Assumes Z" | Check Section 3 (Assumptions) - if not there, it's hidden! |
| "Leaves unsolved W" | Check Section 7 (Limitations) + Section 10 (Missing) |

### To Enrich Pseudoctor Facts

When Pseudoctor gives facts, interpret with Critical Reviewer:

| Pseudoctor Fact | Critical Reviewer Interpretation |
|----------------|----------------------------------|
| "Formula: Attention(...)" | Section 2: Why this formula matters (神来之笔) |
| "Results: 28.4 BLEU" | Section 3: What delta this represents vs SOTA |
| "【原文未明确说明】" | Section 4: Likely hidden assumption |
| "Method: Step 1,2,3..." | Section 5: Distill to essence (napkin diagram) |

---

## Common Mistakes to Avoid

### ❌ Mistake 1: Using only Critical Reviewer
**Problem**: No evidence trail, can't verify claims
**Solution**: At minimum, get Pseudoctor Section 6 (Experiments) for concrete numbers

### ❌ Mistake 2: Using only Pseudoctor
**Problem**: Drowning in facts, can't see forest for trees
**Solution**: At minimum, get Critical Reviewer Section 5 (Essence) for big picture

### ❌ Mistake 3: Running in wrong order
**Problem**: Critical Reviewer lacks context without factual foundation
**Solution**: For deep dive, always Pseudoctor first → Critical Reviewer second

### ❌ Mistake 4: Expecting same output
**Problem**: Pseudoctor says "【原文未明确说明】", Critical Reviewer speculates
**Solution**: This is BY DESIGN. Pseudoctor = safe facts, Critical = reasoned interpretation

---

## Decision Trees

### Should I use Pseudoctor, Critical Reviewer, or both?

```
Are you writing a lit review that needs citations?
  YES → Start with Pseudoctor (need evidence locations)
    ↓
    Do you also need to evaluate novelty?
      YES → Add Critical Reviewer
      NO → Pseudoctor alone is sufficient

  NO → Do you need to make a quick decision?
    YES → Critical Reviewer only (triage mode)
    NO → Do you need deep understanding?
      YES → Both (Pseudoctor first, then Critical Reviewer)
      NO → Critical Reviewer only (quick insights)
```

### Which sections do I need from each skill?

```
For reproducibility:
  - Pseudoctor: Sections 5 (Method), 6 (Experiments)
  - Critical: Section 2 (核心直觉 for understanding)

For evaluation/review:
  - Pseudoctor: Sections 2,6,7 (Claims, Results, Limitations)
  - Critical: All 5 sections

For teaching/explaining:
  - Pseudoctor: Sections 1,2,5 (Problem, Contribution, Method)
  - Critical: Sections 2,5 (Insight, Napkin)

For applicability assessment:
  - Pseudoctor: Section 8 (Applicability)
  - Critical: Section 4 (批判性边界)

For literature survey:
  - Pseudoctor: Sections 0,1,2,9,10 (ID, Problem, Contribution, Reusable, Missing)
  - Critical: Sections 1,3 (核心痛点, 创新增量)
```

---

## Advanced Patterns

### Pattern 5: Iterative Refinement

```bash
Round 1: Critical Reviewer (quick pass)
  → Identifies Section 4 assumption: "Needs large data"

Round 2: Pseudoctor (verify assumption)
  → Section 6: "WMT'14 has 4.5M sentence pairs"
  → Confirms: Large data assumption is real

Round 3: Critical Reviewer (deep dive on this point)
  User: "Expand on data requirements - how much is needed?"
  → Critical analysis of data scaling (if mentioned in paper)
```

### Pattern 6: Multi-Paper Synthesis

```bash
For papers A, B, C on same topic:

Step 1: Run Pseudoctor on all three
  → Get factual cards

Step 2: Critical Reviewer comparative analysis
  User: "Given these 3 factual cards, compare innovation deltas"
  → Output: Innovation comparison table

Step 3: Pseudoctor cross-reference
  → Verify Critical Reviewer's claims with original evidence

Result: Evidence-based comparison
```

---

## Output Management

### File Organization

```
project/
├── papers/
│   ├── transformer/
│   │   ├── original.pdf
│   │   ├── pseudoctor_factual_card.md    ← Pseudoctor output
│   │   ├── critical_review.md            ← Critical Reviewer output
│   │   └── my_notes.md                   ← Your synthesis
│   ├── bert/
│   │   ├── original.pdf
│   │   ├── pseudoctor_factual_card.md
│   │   └── critical_review.md
│   └── gpt/
│       └── ...
└── comparisons/
    └── transformers_comparison.md        ← Multi-paper synthesis
```

### Citation Format

When writing:

```markdown
## Background

The Transformer architecture [1] uses self-attention to replace recurrence.
Specifically, it computes attention as:

  Attention(Q,K,V) = softmax(QK^T/√d_k)V  [1, Section 3.2.1]

This achieves 28.4 BLEU on WMT'14 EN-DE, improving over the previous
best result of 26.4 BLEU [1, Table 2].

**Critical insight**: The key innovation is treating attention as a
complete replacement for recurrence, not a supplement [Critical Review].
However, this assumes O(n²) memory is acceptable, limiting sequence
length to ~1000 tokens [Critical Review, Section 4].

[1] Vaswani et al., "Attention Is All You Need", NeurIPS 2017
    - Factual card: papers/transformer/pseudoctor_factual_card.md
    - Critical review: papers/transformer/critical_review.md
```

---

## Troubleshooting Integration

### Issue 1: Critical Reviewer contradicts Pseudoctor
**Cause**: Pseudoctor found evidence that Critical Reviewer's interpretation missed
**Solution**: Trust Pseudoctor for facts, use Critical Reviewer for interpretation
**Example**:
- Pseudoctor: "【原文未明确说明】computational complexity"
- Critical: "Assumes O(n²) memory acceptable"
- Resolution: Critical's assumption is INFERRED (reasonable but not stated)

### Issue 2: Pseudoctor is too detailed, Critical too vague
**Cause**: Different tools, different granularity
**Solution**: Use Pseudoctor for specific claims, Critical for big picture
**Example**:
- Pseudoctor: "Step 1: Embed input... Step 2: Pass through N=6 layers..."
- Critical: "神来之笔: Scaled dot-product enables parallel attention"
- Use both: Pseudoctor tells you HOW, Critical tells you WHY

### Issue 3: Both skills give different "core contributions"
**Cause**: Pseudoctor quotes authors, Critical interprets impact
**Solution**: Authors' claim vs actual contribution can differ
**Example**:
- Pseudoctor: "Authors claim: 'new architecture for seq2seq'"
- Critical: "Real contribution: Proof that attention can replace recurrence"
- Reality: Critical's interpretation is sharper

---

## Summary: Best Practices

1. **For deep understanding**: Always use both (Pseudoctor → Critical)
2. **For quick triage**: Critical Reviewer first, Pseudoctor if needed
3. **For writing**: Pseudoctor for citations, Critical for insights
4. **For comparison**: Pseudoctor (all papers) → Critical (compare)
5. **For verification**: Critical makes claim → Pseudoctor confirms evidence
6. **For teaching**: Critical (essence) + Pseudoctor (details)

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────┐
│         SKILL SELECTION GUIDE                           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Need citations?           → Pseudoctor                 │
│  Need quick decision?      → Critical Reviewer          │
│  Need deep understanding?  → Both                       │
│  Need to compare papers?   → Both (Pseudo all, Crit compare) │
│  Need to write review?     → Both (Pseudo evidence, Crit insights) │
│  Need to teach concept?    → Critical (essence) first   │
│  Need to reproduce?        → Pseudoctor (methods)       │
│  Need to find limits?      → Critical (boundaries)      │
│                                                         │
├─────────────────────────────────────────────────────────┤
│         WORKFLOW PATTERNS                               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Sequential Deep Dive:     Pseudo → Critical → Decide   │
│  Quick Triage:             Critical → (Pseudo if pass)  │
│  Comparative Analysis:     Pseudo all → Critical compare│
│  Review Writing:           Pseudo + Critical → Draft    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

**Last Updated**: 2026-01-11
**Version**: 1.0
