# Quick Start: Literature Domain Mapper / 快速开始：领域地图构建

**3-minute introduction to domain mapping and faction analysis / 3分钟了解领域地图与派别分析**

---

## English Version

### What You Need

**Input**:
- 30-40 screened papers from Phase 1 (pseudoctor-lit-search)
- Each paper's Abstract + Introduction + Conclusion summaries
- Screening table with required fields (Title, Authors, Year, 1-sentence_Summary)

**Or**:
- Your manually curated core paper list (minimum 20 papers)

### What You Will Get

**8-Step Comprehensive Analysis**:

1. **Domain Map** - Core papers hierarchy (must-read/optional/awareness)
2. **Faction Classification** - Identify 3-5 schools of thought with representative papers
3. **Faction Comparison Table** - Pros/cons/assumptions/scenarios for each faction
4. **Convergence to 20 Papers** - From 30-40 → ~20 core papers with exclusion reasons
5. **Evaluation Dimensions** - Key questions & consensus metrics in the field
6. **Deep Reading Plan** - Recommended reading sequence + extraction templates
7. **Faction Summaries** - Development timeline + theory + results + limitations for each faction
8. **Innovation Opportunity Matrix** - 2-3 recommended routes + specific innovation opportunities

**Final Output**: Complete domain understanding + research gaps + innovation entry points

---

### 3-Minute Example

**Scenario**: Transformers for Time Series Forecasting

#### Input (from pseudoctor-lit-search)
```tsv
Title	Authors	Year	1-sentence_Summary	Is_Review	Candidate_School
Informer: Beyond Efficient Transformer...	Zhou et al.	2021	Proposed ProbSparse attention to reduce complexity to O(L log L)	N	Informer派
Autoformer: Decomposition Transformers...	Wu et al.	2021	Introduced sequence decomposition + auto-correlation	N	Decomposition派
FEDformer: Frequency Enhanced...	Zhou et al.	2022	Frequency-domain attention with Fourier transform	N	Frequency派
... (24 papers total)
```

#### Step 1: Choose Output Format
```
Options:
A - Markdown report
B - Comparison table (recommended for quick overview)
C - Notion adapted
D - Feishu adapted
E - PPT outline

User selects: B (Comparison Table)
```

#### Step 2-3: Domain Map & Faction Classification

**Output**: 5 factions identified

| Faction | Core Idea | Representative Papers | Pros | Cons |
|---------|-----------|----------------------|------|------|
| **Informer派** | ProbSparse attention for efficiency | Informer (AAAI 2021) | O(L log L) complexity, handles long sequences | Sparse attention may lose info |
| **Decomposition派** | Decompose series into trend+seasonal | Autoformer (NeurIPS 2021) | Interpretable, captures periodicity | Decomposition assumption may not fit all data |
| **Frequency派** | Frequency-domain attention | FEDformer (ICML 2022) | Efficient in frequency domain, captures long-term | Overhead for non-periodic data |
| **Linear派** | Simple linear models | DLinear (AAAI 2023) | Extremely fast, sometimes SOTA | Limited expressiveness |
| **Patching派** | Treat time series as patches (like ViT) | PatchTST (ICLR 2023) | Channel-independence, strong generalization | Patch size tuning needed |

#### Step 4: Convergence

**From 24 papers → 20 core papers**

**Excluded (4 papers)**:
- P010 (ETSformer) - arXiv preprint, not peer-reviewed
- P020 (LightTS) - arXiv preprint, limited validation
- P022 (Duplicate of P004)
- P021 (Domain-specific: Earth System, less generalizable)

**Retained**: 20 core papers across 5 factions

#### Step 5-7: Deep Reading Plan

**Recommended Reading Sequence**:
1. **Start with Reviews** (2 papers): P012 (Transformers Survey), P013 (Deep Learning Survey)
2. **Core Factions** (8 papers): Informer → Autoformer → FEDformer → PatchTST → DLinear → iTransformer → TimesNet → Non-stationary Transformer
3. **Important Variants** (5 papers): TFT, Pyraformer, Crossformer, Fedformer, Foundation Model (TimeGPT)
4. **Supporting Works** (5 papers): RevIN, Koopa, Adaptive Norm, Scaleformer, MICN

**Extraction Framework (3A/3B/3C/3D) for Each Paper**:
- **3A - Assumptions**: What does this method assume? Under what conditions is it valid? Are these assumptions realistic in practice?
  - Example: "Time series has sparse self-attention patterns" (Informer)
- **3B - Benefits**: What advantages under these assumptions?
  - Example: "O(L log L) complexity instead of O(L²)"
- **3C - Mechanisms**: How does it work? Which formulas/steps/tricks deliver the benefits? (Focus on 3-5 key points, skip derivations)
  - Example: "Selects top-K queries based on sparsity measurement"
- **3D - Limitations**: What doesn't work? What failure scenarios? (from mutual criticisms)
  - Example: "K needs manual tuning, may fail on dense dependencies"

**3A/3B/3C/3D Execution Modes**:
- **Mode A - Template Only**: No full text → Provide empty templates for you to fill after reading
- **Mode B - Partial Fill from A/I/C** (DEFAULT): Only have Abstract/Intro/Conclusion → Partially fill 3A/3B/3C/3D, mark "[Requires full-text verification]" where uncertain
- **Mode C - Full Extraction**: Full text provided → Complete all fields with evidence binding

**Critical Warnings**:
- Focus on conceptual skeleton only - avoid being "killed by proofs/derivations"
- Check for success case bias: Do examples only show successful cases? What risks are NOT covered?

#### Step 8: Innovation Opportunity Matrix

| Opportunity | Faction Combination | Potential Improvement | Technical Challenge |
|-------------|--------------------|-----------------------|---------------------|
| **1. Frequency-Decomposition Fusion** | Frequency + Decomposition | Dual modeling in both domains | Computational cost, how to fuse? |
| **2. Adaptive Patching** | Patching + Non-stationary | Dynamic patch size based on distribution shift | Patch boundary detection, online update |
| **3. Lightweight Informer** | Informer + Linear | Combine ProbSparse + linear layers for efficiency | Sparse pattern learning, hyperparameter sensitivity |

**Recommended Routes**:
1. **Route A (Recommended)**: Frequency-Decomposition Fusion
   - **Rationale**: Combines strengths of two proven approaches (ICML 2022 + NeurIPS 2021)
   - **Next Steps**: Implement Fourier-based decomposition, test on ETT datasets

2. **Route B**: Adaptive Patching with Non-stationarity Handling
   - **Rationale**: Addresses distribution shift problem in real-world data
   - **Next Steps**: Design patch size adaptation algorithm, validate on non-stationary benchmarks

3. **Route C**: Lightweight Efficient Transformers for Edge Deployment
   - **Rationale**: Growing need for on-device time series forecasting
   - **Next Steps**: Combine ProbSparse + knowledge distillation, optimize for mobile

---

### Workflow Diagram

```
Input: 30-40 screened papers from pseudoctor-lit-search
  ↓
Step 1: Choose output format (Markdown/Table/Notion/Feishu/PPT)
  ↓
Step 2-3: Domain Map + Faction Classification (5 factions identified)
  ↓
Step 4: Convergence (40 → 20 core papers)
  ↓
Step 5: Evaluation Dimensions (MSE, MAE, efficiency, interpretability)
  ↓
Step 6-7: Deep Reading Plan (sequence + templates)
  ↓
Step 8: Innovation Opportunity Matrix (3 routes, 5 specific opportunities)
  ↓
Output: Complete domain understanding + research gaps + next steps
```

---

### Time Investment

| Stage | Time | Notes |
|-------|------|-------|
| Input preparation | 30-60 min | Organize screening table from Phase 1 |
| Step 1-3 (Domain Map + Factions) | 1-1.5 hours | Identify factions, compare |
| Step 4 (Convergence) | 30-45 min | Narrow down to 20 papers |
| Step 5-7 (Reading Plan) | 1-1.5 hours | Design reading sequence + templates |
| Step 8 (Opportunity Matrix) | 1 hour | Identify innovation opportunities |
| **Total** | **3.5-4.5 hours** | Complete domain mapping |

---

### Next Steps After Domain Mapping

**Option 1: Deep Reading** (Use `/pseudoctor-paper-reader`)
- Select 5-10 must-read papers from the 20 core papers
- Extract detailed method skeletons, assumptions, experiments
- Get evidence-bound paper cards (10 sections × 40+ fields)

**Option 2: Critical Analysis** (Use `/pseudoctor-paper-criticalreviewer`)
- Critically analyze 3-5 core papers
- Identify innovation deltas, hidden assumptions, unsolved problems
- Get high-density insights (5 sections per paper)

**Option 3: Both** (Recommended for thesis/research proposals)
- Use paper-reader for faithful understanding
- Use paper-criticalreviewer for critical evaluation
- Combine insights to identify research gaps

---

### Common Questions

**Q1: Can I use this skill without pseudoctor-lit-search?**
**A**: Yes, but you need to prepare a screening table yourself with minimum fields (Title, Authors, Year, 1-sentence_Summary).

**Q2: What if I have fewer than 30 papers?**
**A**: The skill works with 20-40 papers. If you have <20, consider expanding your search first.

**Q3: What if I don't have Abstract/Introduction/Conclusion summaries?**
**A**: You can provide just the screening table with 1-sentence summaries. The skill will work with that, but faction analysis will be less nuanced.

**Q4: Which output format should I choose?**
**Recommendations**:
- **Markdown (A)**: Best for comprehensive documentation
- **Comparison Table (B)**: Best for quick faction comparison
- **Notion (C)**: Best if you're using Notion for research management
- **PPT (E)**: Best for group meeting presentations

**Q5: How are factions different from keywords?**
**A**: Keywords group by terminology; factions group by **methodological approach** or **theoretical stance**. Factions may share keywords but have different core ideas.

---

### Integration with Other Skills

**Complete Literature Analysis Pipeline**:

```
Phase 1: pseudoctor-lit-search (6-8 hours)
  → Keyword matrix + Boolean queries + 30-40 screened papers

Phase 2: pseudoctor-literature-mapper (3.5-4.5 hours) ← YOU ARE HERE
  → Faction map + 20 core papers + innovation opportunities

Phase 3: pseudoctor-paper-reader (2.5-5 hours for 5-10 papers)
  → Detailed paper cards with evidence binding

Phase 4: pseudoctor-paper-criticalreviewer (0.75-1.5 hours for 3-5 papers)
  → Critical insights + innovation deltas
```

**Total Time**: ~13-19 hours for complete domain mastery

---

## 中文版本

### 你需要什么？

**输入**:
- 来自Phase 1（pseudoctor-lit-search）的30-40篇筛选后论文
- 每篇论文的摘要+引言+结论总结
- 筛选表（包含必需字段：Title, Authors, Year, 1-sentence_Summary）

**或者**:
- 你手动整理的核心论文列表（最少20篇）

### 你将获得什么？

**8步全面分析**:

1. **领域地图** - 核心论文层级（必读/选读/了解）
2. **派别分类** - 识别3-5个学术派别及代表论文
3. **派别对照表** - 每个派别的优缺点/假设/场景
4. **收敛到20篇** - 从30-40篇 → ~20篇核心论文 + 剔除理由
5. **评价维度** - 领域关心的核心问题 + 共识性指标
6. **深读计划** - 推荐阅读顺序 + 抽取模板
7. **派别总结** - 每个派别的发展脉络+理论+结果+局限性
8. **创新机会矩阵** - 2-3条推荐路线 + 具体创新机会

**最终产出**: 完整的领域理解 + 研究gap + 创新切入点

---

### 3分钟示例

**场景**: Transformer在时间序列预测中的应用

#### 输入（来自pseudoctor-lit-search）
```tsv
Title	Authors	Year	1-sentence_Summary	Is_Review	Candidate_School
Informer: Beyond Efficient Transformer...	Zhou et al.	2021	提出ProbSparse注意力机制降低复杂度至O(L log L)	N	Informer派
Autoformer: Decomposition Transformers...	Wu et al.	2021	引入序列分解+自相关机制	N	Decomposition派
FEDformer: Frequency Enhanced...	Zhou et al.	2022	频域注意力+傅里叶变换	N	Frequency派
... (共24篇)
```

#### Step 1: 选择输出格式
```
选项:
A - Markdown报告
B - 对照表（推荐，快速概览）
C - Notion适配
D - 飞书适配
E - PPT大纲

用户选择: B（对照表）
```

#### Step 2-3: 领域地图 & 派别分类

**输出**: 识别出5个派别

| 派别 | 核心idea | 代表论文 | 优点 | 缺点 |
|------|---------|---------|------|------|
| **Informer派** | ProbSparse注意力降低复杂度 | Informer (AAAI 2021) | O(L log L)复杂度，长序列高效 | 稀疏注意力可能丢失信息 |
| **Decomposition派** | 序列分解为趋势+季节性 | Autoformer (NeurIPS 2021) | 可解释性强，捕获周期性 | 分解假设可能不适用所有数据 |
| **Frequency派** | 频域注意力 | FEDformer (ICML 2022) | 频域计算高效，长期依赖强 | 非周期数据效果差 |
| **线性派** | 简单线性模型 | DLinear (AAAI 2023) | 极快，某些数据集SOTA | 表达能力有限 |
| **Patching派** | 时序Patch化（类似ViT） | PatchTST (ICLR 2023) | Channel-independence，泛化强 | Patch大小需调参 |

#### Step 4: 收敛

**从24篇 → 20篇核心论文**

**剔除（4篇）**:
- P010 (ETSformer) - arXiv预印本，未经同行评审
- P020 (LightTS) - arXiv预印本，验证有限
- P022 (与P004重复)
- P021 (领域特定：地球系统，泛化性差)

**保留**: 20篇核心论文，覆盖5个派别

#### Step 5-7: 深读计划

**推荐阅读顺序**:
1. **综述优先**（2篇）: P012（Transformers综述），P013（深度学习综述）
2. **核心派别**（8篇）: Informer → Autoformer → FEDformer → PatchTST → DLinear → iTransformer → TimesNet → Non-stationary Transformer
3. **重要变体**（5篇）: TFT, Pyraformer, Crossformer, Fedformer, Foundation Model (TimeGPT)
4. **支撑工作**（5篇）: RevIN, Koopa, Adaptive Norm, Scaleformer, MICN

**抽取框架（3A/3B/3C/3D）每篇论文必须回答**:
- **3A - 假设**: 该方法假设什么？在什么条件下有效？这些假设在现实场景难不难成立？
  - 示例："时间序列的自注意力分布是稀疏的"（Informer）
- **3B - 好处**: 在这些假设下的优势是什么？
  - 示例："复杂度从O(L²)降至O(L log L)"
- **3C - 机制**: 如何工作？哪些关键公式/步骤/简化体现了好处？（只抓3-5个关键点，跳过推导）
  - 示例："基于稀疏度度量选择top-K个Query"
- **3D - 缺点**: 什么不适用？哪些失败情形？（来自派别间互相批评）
  - 示例："K需要手动调参，密集依赖场景可能失效"

**3A/3B/3C/3D执行模式**:
- **模式A - 仅提供模板**: 无全文 → 提供空白模板供你读后填写
- **模式B - 基于A/I/C部分填充**（默认）: 仅有摘要/引言/结论 → 部分填写3A/3B/3C/3D，不确定处标注"[需全文验证]"
- **模式C - 全文深度抽取**: 提供全文 → 完整填写所有字段，含证据绑定

**关键警示**:
- 只读概念骨架 - 避免被"证明推导拖死"
- 检查成功案例偏差：样例是否只展示成功案例？哪些风险未被覆盖？

#### Step 8: 创新机会矩阵

| 机会点 | 派别组合 | 潜在改进 | 技术挑战 |
|--------|---------|---------|---------|
| **1. 频域分解融合** | Frequency + Decomposition | 频域+时域双重建模 | 计算开销，如何融合？ |
| **2. 自适应Patching** | Patching + Non-stationary | 根据分布漂移动态调整Patch大小 | Patch边界检测，在线更新 |
| **3. 轻量化Informer** | Informer + 线性 | 结合ProbSparse+线性层平衡性能与效率 | 稀疏模式学习，超参敏感 |

**推荐路线**:
1. **路线A（推荐）**: 频域分解融合
   - **理由**: 结合两个已验证方法的优势（ICML 2022 + NeurIPS 2021）
   - **下一步**: 实现傅里叶分解，在ETT数据集上测试

2. **路线B**: 自适应Patching与非平稳性处理
   - **理由**: 解决真实世界数据的分布漂移问题
   - **下一步**: 设计Patch大小自适应算法，在非平稳基准上验证

3. **路线C**: 轻量化高效Transformer用于边缘部署
   - **理由**: 端侧时序预测需求日益增长
   - **下一步**: 结合ProbSparse+知识蒸馏，针对移动端优化

---

### 工作流程图

```
输入: 来自pseudoctor-lit-search的30-40篇筛选论文
  ↓
Step 1: 选择输出格式（Markdown/对照表/Notion/飞书/PPT）
  ↓
Step 2-3: 领域地图 + 派别分类（识别出5个派别）
  ↓
Step 4: 收敛（40篇 → 20篇核心论文）
  ↓
Step 5: 评价维度（MSE、MAE、效率、可解释性）
  ↓
Step 6-7: 深读计划（阅读顺序 + 抽取模板）
  ↓
Step 8: 创新机会矩阵（3条路线，5个具体机会）
  ↓
输出: 完整领域理解 + 研究gap + 下一步行动
```

---

### 时间投入

| 阶段 | 耗时 | 说明 |
|------|------|------|
| 输入准备 | 30-60分钟 | 整理Phase 1的筛选表 |
| Step 1-3（领域地图+派别） | 1-1.5小时 | 识别派别，比较 |
| Step 4（收敛） | 30-45分钟 | 收敛到20篇 |
| Step 5-7（深读计划） | 1-1.5小时 | 设计阅读顺序+模板 |
| Step 8（机会矩阵） | 1小时 | 识别创新机会 |
| **总计** | **3.5-4.5小时** | 完成领域地图构建 |

---

### 领域地图后的下一步

**选项1: 深度阅读**（使用 `/pseudoctor-paper-reader`）
- 从20篇核心论文中选择5-10篇必读论文
- 提取详细的方法骨架、假设、实验设计
- 获得证据绑定的论文卡片（10 sections × 40+ fields）

**选项2: 批判性分析**（使用 `/pseudoctor-paper-criticalreviewer`）
- 批判性分析3-5篇核心论文
- 识别创新增量、隐藏假设、未解决问题
- 获得高密度洞察（每篇5 sections）

**选项3: 两者结合**（推荐用于论文/研究提案）
- 使用paper-reader进行忠实理解
- 使用paper-criticalreviewer进行批判评估
- 结合洞察识别研究gap

---

### 常见问题

**Q1: 可以不用pseudoctor-lit-search直接使用本skill吗？**
**A**: 可以，但你需要自己准备筛选表，至少包含必需字段（Title, Authors, Year, 1-sentence_Summary）。

**Q2: 如果论文少于30篇怎么办？**
**A**: 本skill适用于20-40篇论文。如果<20篇，建议先扩大检索范围。

**Q3: 如果没有摘要/引言/结论总结怎么办？**
**A**: 可以仅提供带一句话摘要的筛选表。Skill可以工作，但派别分析会不够细致。

**Q4: 应该选择哪种输出格式？**
**推荐**:
- **Markdown (A)**: 适合全面文档
- **对照表 (B)**: 适合快速派别对比
- **Notion (C)**: 适合使用Notion进行研究管理
- **PPT (E)**: 适合组会汇报

**Q5: 派别与关键词有何区别？**
**A**: 关键词按术语分组；派别按**方法路线**或**理论立场**分组。派别可能共享关键词，但核心idea不同。

---

### 与其他Skills的集成

**完整文献分析流程**:

```
Phase 1: pseudoctor-lit-search（6-8小时）
  → 关键词矩阵 + Boolean检索式 + 30-40篇筛选论文

Phase 2: pseudoctor-literature-mapper（3.5-4.5小时）← 你在这里
  → 派别地图 + 20篇核心论文 + 创新机会

Phase 3: pseudoctor-paper-reader（5-10篇×30分钟 = 2.5-5小时）
  → 详细论文卡片，证据绑定

Phase 4: pseudoctor-paper-criticalreviewer（3-5篇×15分钟 = 0.75-1.5小时）
  → 批判性洞察 + 创新增量
```

**总耗时**: ~13-19小时完成领域掌握

---

**Version**: 1.0
**Last Updated**: 2026-01-11
**Status**: ✅ Production Ready - Bilingual Quick Start Guide
