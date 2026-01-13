# Quick Start Guide: Pseudoctor Paper Reader

## ⚡ 5-Minute Onboarding

### What is this skill?
A **faithful extraction assistant** that creates structured "Paper Reading Cards" - auditable summaries where **every claim** is backed by **direct evidence** from the original text.

### Core Philosophy
🚫 **NO guessing, NO external knowledge, NO speculation**
✅ **ONLY what the paper explicitly states, with evidence**

---

## 🎯 Quick Usage

### Step 1: Provide Paper Text
Give me any portion of the paper (abstract, methods, full PDF text, etc.)

### Step 2: I Auto-Detect Type
I'll classify it as:
- 【实证/技术论文】 → Gets method/experiment structure
- 【哲学/思辨论文】 → Gets argument/concept structure
- 【混合型论文】 → Gets both structures
- 【无法判断】 → I'll explain what's missing

### Step 3: Get Structured Card
A 10-section reading card with evidence for every claim

---

## 📋 Output Structure Preview

### Universal Sections (All Papers)
0. **Paper ID** - Title, authors, venue
1. **Problem & Motivation** - What problem? Why important?
2. **Key Contribution** - What's the core claim/contribution?

### For Empirical/Technical Papers (D1)
3. **Assumptions** - What must be true for this to work?
4. **Benefits/Claims** - What advantages does it claim?
5. **Method Skeleton** - Key steps & formulas (only)
6. **Experiments** - What was validated? Coverage check!
7. **Limitations** - What does the paper admit doesn't work?
8. **Applicability** - When to use/not use this?

### For Philosophical Papers (D2)
3. **Key Concepts** - Important terms & definitions
4. **Distinctions** - Critical conceptual boundaries (A vs B)
5. **Argument Skeleton** - Premises → Inferences → Conclusion
6. **Argument Audit** - Is the argument sound? Objections?
7. **Limitations** - What's left unresolved?
8. **Scope** - What's in/out of the discussion?

### Final Sections (All Papers)
9. **What to Steal** - Reusable ideas/techniques from this paper
10. **Missing Pieces** - What I couldn't extract (and why)

---

## 🔍 Evidence Format

Every claim follows this pattern:

```
**Claim**: [Your extracted conclusion]
  证据摘录: "Direct quote from paper (20-50 words)"
  位置标记: p.5, Section 3.2, para.2
```

**Location markers** (best to worst):
1. ✅ `p.5, Section 3.2, para.2` (page + section + paragraph)
2. ✅ `Introduction, para.3` (section + paragraph)
3. ⚠️ `Related Work, second-to-last paragraph` (description)
4. ⚠️ `near beginning of Results` (vague, use only if necessary)

---

## 🛡️ Faithfulness Markers

When the paper doesn't explicitly state something, I use:

| Marker | Meaning |
|--------|---------|
| 【原文未明确说明】 | Not explicitly stated |
| 【无法从原文唯一推出】 | Cannot uniquely infer |
| 【原文未提供相关部分】 | Section not provided |
| 【原文存在矛盾】 | Author contradicts themselves |
| 【疑似原文错误】 | Suspected error (but quoted exactly) |
| 【无法判断】 | Cannot determine from available text |

**See full reference table in SKILL.md Section H**

---

## 🎓 Examples

### Example 1: Technical Paper
See `references/example_empirical.md` for complete card of "Attention Is All You Need" (Transformer paper)

**Key features shown:**
- Method skeleton with 4 key steps
- Only 2 key formulas (not all 15+ in paper)
- Coverage check: which claims were actually validated?
- Explicit "Skip explanation" for omitted derivations

### Example 2: Philosophical Paper
See `references/example_philosophical.md` for complete card of Gettier's "Is Justified True Belief Knowledge?"

**Key features shown:**
- Argument chain: P1→P2→P3→I1→I2→C
- Identification of implicit premises (marked as 【原文未提供桥梁论证】)
- Analysis of thought experiments (Gettier cases)
- Recognition that paper "only destroys, doesn't build" new theory

---

## 💡 Pro Tips

### ✅ DO:
- Provide paper text in chunks (I handle partial papers)
- Ask follow-up questions about specific sections
- Add more paper text later (I'll update the card)
- Request deeper dive into formulas/arguments

### ❌ DON'T:
- Ask me to evaluate the paper (I only extract)
- Expect me to complete missing information
- Ask for related papers (I only work with provided text)
- Request general knowledge about the topic

---

## 🔄 Multi-Round Interaction

You can iterate with me:

### Round 1: Initial Extraction
**You:** [Paste abstract + introduction]
**Me:** Partial card + Section 10 lists what's missing

### Round 2: Add More Content
**You:** [Paste methods section]
**Me:** Updated card + explicit statement: "新证据改变了Section 3 假设清单"

### Round 3: Deep Dive
**You:** "Explain Formula 2 in more detail"
**Me:** Expanded explanation (still evidence-bound)

---

## 🚦 When to Use This Skill

### ✅ Perfect for:
- Understanding unfamiliar papers without bias
- Creating auditable literature review notes
- Extracting reusable techniques from papers
- Fact-checking claims about what papers say
- Teaching students faithful reading practices

### ⚠️ Not ideal for:
- Asking "Is this paper good?" (I don't evaluate)
- "Find papers about X" (I don't search)
- "What's the state of the art?" (I don't aggregate)

---

## 🐛 Troubleshooting

### "You're not giving me evidence!"
→ Check if your provided text actually contains the info you're asking about. Section 10 will list missing pieces.

### "Too much detail!" / "Not enough detail!"
→ Tell me! I can adjust granularity within faithfulness constraints.

### "Why so many 【原文未明确说明】?"
→ That's the point! It shows what the paper *doesn't* prove, which is critical for honest reading.

---

## 📖 Full Documentation

This is a **quick start**. For complete specification:
- **Full protocol**: See main `SKILL.md`
- **Evidence standards**: SKILL.md Section 2
- **Type criteria**: SKILL.md Section "Automatic Paper Type Recognition"
- **Quality checklist**: SKILL.md Section H
- **All markers**: SKILL.md "Quick Reference: Standard Markers" table

---

## 🎯 Your First Card

Ready to try? Paste your paper text and say:

> "Please read this paper using the pseudoctor-paper-reader skill"

I'll handle the rest! 📄✨
