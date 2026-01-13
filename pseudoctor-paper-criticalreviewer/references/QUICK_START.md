# Quick Start Guide: Critical Academic Reviewer

## ⚡ 3-Minute Onboarding

### What is this skill?
A **critical analysis tool** that cuts through academic jargon to reveal:
- The ONE core insight that makes the paper work
- What's genuinely new (the "Delta")
- Where the method will fail (hidden assumptions & boundaries)

### How is it different from pseudoctor-paper-reader?

| Pseudoctor | Critical Reviewer |
|-----------|-------------------|
| **What does it SAY?** | **What does it MEAN?** |
| Faithful fact extraction | Critical evaluation |
| 40+ fields with evidence | 5 high-density insights |
| Zero external knowledge | Uses SOTA comparison |
| Like a court stenographer | Like a sharp peer reviewer |

---

## 🎯 When to Use Each Skill

### Use **pseudoctor-paper-reader** when you need:
- ✅ Auditable literature review notes
- ✅ Exact claims with evidence locations
- ✅ Complete factual record of the paper
- ✅ To avoid any interpretation bias

### Use **critical-reviewer** when you need:
- ✅ To decide if you should read the full paper
- ✅ To understand the core contribution quickly
- ✅ To write a review or evaluation
- ✅ To judge if the method applies to YOUR problem

### Use **BOTH** (recommended workflow):
```
1. Run pseudoctor → Get factual skeleton
2. Run critical-reviewer → Get insights & critique
3. Result: Facts + Meaning = Deep understanding
```

---

## 📋 Output Structure (5 Sections)

### 1. 核心痛点 (Core Problem)
- One-sentence problem definition
- Why previous approaches failed (with evidence)

**Example** (Transformer paper):
> Problem: RNNs can't parallelize because h_t depends on h_{t-1}
> Previous failure: [x] Computational constraints - sequential bottleneck

### 2. 解题机制 (Solution Mechanism)
- The "aha moment" insight (plain language)
- The 1-2 critical tricks that make it work

**Example**:
> Insight: "Attention can replace recurrence entirely, not just augment it"
> 神来之笔: Scaled dot-product (QK^T/√d_k) enables parallel all-to-all attention

### 3. 创新增量 (Innovation Delta)
- Concrete improvements vs SOTA (numbers!)
- What specific puzzle piece this adds to knowledge

**Example**:
> - Efficiency: 3.5 days vs weeks for comparable models
> - Accuracy: 28.4 BLEU (vs 26.4 previous best)
> - Paradigm shift: First seq2seq with zero recurrence
>
> Adds: "Proof that self-attention alone suffices for SOTA"

### 4. 批判性边界 (Critical Boundaries)
- Hidden assumptions (what must be true for this to work?)
- Open questions (what's still unsolved?)

**Example**:
> Assumption 1: Sufficient data (4.5M sentence pairs)
> Assumption 2: Parallel hardware (8 GPUs)
> Assumption 3: O(n²) memory is acceptable
>
> Left unsolved: How to handle sequences >1000 tokens?

### 5. 一言以蔽之 (Essence on a Napkin)
- ASCII diagram of core mechanism
- The ONE formula/principle that captures everything

**Example**:
```
Attention(Q,K,V) = softmax(QK^T/√d_k)V

Principle: "Replace sequential propagation with parallel
all-to-all attention"
```

---

## 🚀 How to Use

### Method 1: Direct Analysis
```
User: "Please review this paper critically: [paste paper text]"

Critical Reviewer:
→ Phase 1: 去噪 (filter noise - skip background)
→ Phase 2: 提取 (extract delta - find core contribution)
→ Phase 3: 批判 (critical analysis - find boundaries)
→ Output: 5 sections
```

### Method 2: Two-Stage Deep Dive (⭐ Recommended)
```
User: "Read this paper with pseudoctor-paper-reader"
→ Get: Factual card with 40+ fields

User: "Now give me critical insights"
→ Critical Reviewer uses factual card as context
→ Get: 5-section critical analysis

Result: Complete understanding (facts + insights)
```

### Method 3: Comparative Analysis
```
User: "Compare papers A and B - which has the real innovation?"
→ Critical Reviewer analyzes both
→ Focuses on Section 3 (Innovation Delta) comparison
→ Tells you which contribution is incremental vs paradigm-shifting
```

---

## 📖 Examples

### Example 1: Empirical Paper
See `references/example_empirical.md` - Critical review of **"Attention Is All You Need"**

**Highlights**:
- Core insight: "Attention can replace recurrence entirely"
- Key trick: 1/√d_k scaling prevents softmax saturation
- Hidden assumption: O(n²) memory is acceptable (not discussed in paper!)
- Napkin formula: `Attention(Q,K,V) = softmax(QK^T/√d_k)V`

### Example 2: Philosophical Paper
See `references/example_philosophical.md` - Critical review of **Gettier's "Is Justified True Belief Knowledge?"**

**Highlights**:
- Core insight: "Knowledge requires right connection, not just any connection"
- Key trick: Use opponent's own principle (entailment) against them
- Hidden assumption: Intuitions about knowledge are reliable
- Napkin diagram: JTB case where Q is true by luck → not knowledge

---

## 💡 Pro Tips

### ✅ DO:
- Focus on what's genuinely NEW (ignore standard background)
- Demand concrete numbers (not "significant improvement")
- Think about edge cases where method would fail
- Use plain language (avoid parroting jargon)

### ❌ DON'T:
- Don't summarize the abstract (distill the essence)
- Don't list all contributions equally (prioritize the 1-2 key ones)
- Don't give vague criticism ("may not work in all cases")
- Don't be a cheerleader or hostile critic (be rigorous but fair)

---

## 🎓 Quality Standards

### ✅ Good Critical Review:
```
Transformer paper:
"The core insight is treating attention as a complete
replacement for recurrence, enabled by the 1/√d_k scaling
trick. Assumes O(n²) memory is acceptable, which limits
sequence length to ~1000 tokens."

→ Clear insight, specific trick, concrete boundary
```

### ❌ Bad Critical Review:
```
Transformer paper:
"This paper proposes a novel architecture based on
attention mechanisms. It achieves good results.
May not work in all scenarios."

→ Generic, no insight, vague criticism
```

---

## 🔄 Integration Workflow

### Standalone Use
```
Paper → Critical Reviewer → Insights
```
**Use when**: You need quick evaluation, paper selection, or strategic understanding

### Full Deep Dive
```
Paper → Pseudoctor (facts) → Critical Reviewer (insights) → Decision
```
**Use when**: Writing reviews, conducting research, making important decisions

### Comparative Analysis
```
Papers A, B, C → Critical Reviewer → Innovation comparison
```
**Use when**: Choosing which paper to build on, identifying real vs incremental advances

---

## 🐛 Troubleshooting

### "The review is too vague"
→ Provide more paper content, especially: methods, results, comparisons to baselines

### "I want more detail on X"
→ Say: "Expand Section 2 (Solution Mechanism) with more technical depth"

### "This feels too critical"
→ Remember: Identifying boundaries helps you know WHEN to use the method
→ Not criticism for criticism's sake - it's about applicability

### "How is this different from pseudoctor?"
→ Pseudoctor = **"The paper says X"** (with evidence)
→ Critical = **"X means Y, assumes Z, will fail when W"** (with reasoning)

---

## 📊 Comparison Table

| Task | Pseudoctor | Critical Reviewer | Both |
|------|-----------|-------------------|------|
| **Lit review notes** | ✅ Primary | ❌ Skip | ⚠️ Optional |
| **Paper review/evaluation** | ⚠️ Helper | ✅ Primary | ⭐ Best |
| **Quick paper triage** | ❌ Too detailed | ✅ Perfect | ❌ Overkill |
| **Deep understanding** | ⚠️ Facts only | ⚠️ Insights only | ⭐ Complete |
| **Method applicability** | ❌ No judgment | ✅ Boundaries | ⭐ Best |
| **Reproducibility** | ✅ Has details | ❌ High-level | ⭐ Both layers |

---

## 🎯 Example Invocations

### Quick triage
```
"Should I read this paper? Here's the abstract: [paste]"
→ Critical Reviewer gives you Section 1-3 (~2 min)
→ You decide if it's worth full read
```

### Grant review
```
"I need to review this proposal. Here's the paper: [paste]"
→ Critical Reviewer gives full 5-section analysis
→ Section 4 (Boundaries) tells you what's missing
```

### Research strategy
```
"Which is more promising: Paper A or Paper B?"
→ Critical Reviewer compares Section 3 (Innovation Delta)
→ Tells you which is paradigm shift vs incremental
```

### Teaching/Learning
```
"Explain the key insight of [famous paper]"
→ Critical Reviewer gives Section 2 + Section 5
→ You get the "aha moment" + napkin diagram
```

---

## 🔗 Related Skills

- **pseudoctor-paper-reader**: Companion skill for factual extraction
- Use together for complete paper analysis
- See `references/INTEGRATION_GUIDE.md` for workflow patterns

---

## 📝 Output Length

Expect **500-800 words** of high-density insights:
- Much shorter than pseudoctor (which can be 2000+ words)
- But every sentence is actionable insight
- No filler, no repetition

---

## 🚦 Limitations

### This skill DOES:
✅ Cut through jargon to reveal mechanisms
✅ Identify hidden assumptions
✅ Evaluate innovation with evidence

### This skill DOES NOT:
❌ Replace reading the paper (requires full text)
❌ Generate new research ideas (analyzes existing)
❌ Make accept/reject decisions (provides analysis, not verdict)

---

## 🎬 Ready to Start?

Try it now:

```
"Please critically review this paper: [paste your paper text]"
```

Or for two-stage workflow:

```
"First read with /pseudoctor-paper-reader, then critically review"
```

The Critical Reviewer will handle the rest! 🎯
