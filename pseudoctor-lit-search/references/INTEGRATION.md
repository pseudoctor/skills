# 文献分析工作流集成指南

**两阶段协同**: pseudoctor-lit-search → pseudoctor-literature-mapper

**完整流程**: 检索筛选 → 派别分析 → 深度阅读 → 批判评审

---

## 工作流概览

```
┌─────────────────────────────────────────────────────────────┐
│         Complete Literature Analysis Pipeline               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  【Phase 1】 pseudoctor-lit-search (找全+筛快)              │
│    输入:  研究主题 + 子问题 + 时间范围                       │
│    输出:  30-40篇核心文献 + 筛选表 + 关键词矩阵              │
│    耗时:  6-8小时                                           │
│                                                             │
│         ↓ (筛选表 + 每篇A+I+C摘要 → 直接传递)                │
│                                                             │
│  【Phase 2】 pseudoctor-literature-mapper (派别+深挖)       │
│    输入:  Phase 1 筛选表                                    │
│    输出:  派别对照表 + 核心20篇 + 深读计划 + 创新机会矩阵    │
│    耗时:  3-4小时                                           │
│                                                             │
│         ↓ (必读论文清单 → 选择5-10篇)                        │
│                                                             │
│  【Phase 3】 pseudoctor-paper-reader (忠实提取) [可选]      │
│    输入:  必读论文全文                                       │
│    输出:  证据绑定的详细论文卡片（10 sections × 40+ fields）│
│    耗时:  ~30分钟/篇                                         │
│                                                             │
│         ↓ (核心论文理解完毕)                                 │
│                                                             │
│  【Phase 4】 pseudoctor-paper-criticalreviewer (批判) [可选]│
│    输入:  核心论文                                           │
│    输出:  批判性洞察（5 sections）+ 创新增量评估             │
│    耗时:  ~15分钟/篇                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘

最终产出: 完整的领域理解 + 创新切入点 + 深度论文卡片
```

---

## Phase 1: pseudoctor-lit-search

### 输入

**必需**:
- 研究主题/领域（例如："Transformer在时间序列预测中的应用"）
- 子问题或应用场景（例如："多变量长期预测"）

**可选**:
- 时间范围（默认：近10年）
- 侧重（理论/应用/两者，默认：两者）
- 允许材料类型（期刊/会议/arXiv，默认：期刊+会议+arXiv）
- 主要检索渠道（Google Scholar/PubMed等，默认：不确定就推荐）
- 语言（中/英，默认：中英）

### 输出（5个核心产物）

1. **关键词矩阵**（5个分类）
   - 核心概念词（3-8个）
   - 同义词/变体/缩写（每个核心概念≥5个）
   - 任务/应用词（≥10个）
   - 常见方法/模型/指标词（≥10个）
   - 排除词（≥10个）

2. **Boolean检索式**（3套）
   - 宽召回检索式（OR多，少量AND）
   - 精准召回检索式（AND多）
   - Review专用检索式（含review/survey/overview关键词）
   - 每套包含：适用数据库说明 + 调参建议

3. **快速筛选SOP**
   - 第一轮筛选标准（Title + Abstract，每篇≤2分钟）
   - 第二轮筛选标准（Introduction + Conclusion，每篇≤6分钟）
   - 收敛路径：几百篇 → 30-40篇 → 20-30篇

4. **筛选表模板**（17字段，支持5种格式）
   - TSV（推荐，直接粘贴Excel/Sheets/飞书）
   - CSV（编程处理）
   - Markdown（文档/Notion）
   - Notion属性清单（Notion数据库建表）
   - 飞书/多维表格字段清单

5. **Step 1 阅读指令**
   - Review优先策略（优先读综述 → 高被引 → 近3年 → 核心关键词全命中）
   - 1分钟笔记字段清单（Paper_ID, Title, 1-sentence_Summary, Relevance_Score, Keywords_Matched, Reason_Keep_or_Drop）
   - 回传数据最小包（完整筛选表 + 每篇一句话摘要）

### 执行流程

```
Step 1: 提供输入 → pseudoctor-lit-search
  ↓
Step 2: 获得关键词矩阵 + Boolean检索式
  ↓
Step 3: 复制检索式到Google Scholar/PubMed等
  ↓
Step 4: 执行检索，下载前100-200篇的标题+摘要
  ↓
Step 5: 第一轮筛选（Title + Abstract）
  几百篇 → 30-40篇
  ↓
Step 6: 第二轮筛选（Introduction + Conclusion）
  30-40篇 → 20-30篇
  ↓
Step 7: 填写筛选表（17字段）
  ↓
Step 8: 准备传递给Phase 2
```

### 输出示例

参考 `references/` 目录下的完整示例:
- `example_keywords.md` - 关键词矩阵示例（82个关键词）
- `example_boolean.md` - Boolean检索式示例（3套完整检索式）
- `example_table.md` - 筛选表示例（24篇核心文献）

---

## Phase 2: pseudoctor-literature-mapper

### 输入（来自Phase 1）

**必需字段**:
- `Title` - 论文标题
- `Authors` - 作者
- `Year` - 年份
- `1-sentence_Summary` - 一句话摘要

**推荐字段**（加速派别分析）:
- `Is_Review` - 是否综述（Y/N），优先分析综述
- `Candidate_School` - 候选派别，初步派别判断
- `Keywords_Matched` - 命中关键词，辅助分类

**可选字段**（完整17字段最佳）:
- `Venue`, `URL`, `Material_Type`, `Task`, `First_Read`, `Relevance_Score`, `Reason_Keep_or_Drop`, `Must_Read_Level`, `Notes`

### 输出（8步完整产物）

#### Step 1: 输入确认 & 格式选择
- 确认输入类型（筛选表 / 论文列表+摘要 / 核心论文）
- 选择输出格式（Markdown / Comparison Table / Notion / 飞书 / PPT Outline）

#### Step 2: 领域地图（仅读A+I+C）
- **2A**: 核心论文层级（必读/选读/了解）
- **2B**: 派别分类（派别名称, 边界, 核心idea, 代表论文）
- **2C**: 派别特征（优点/缺点，基于A+I+C支持）

#### Step 3: 派别+时间线组织
- 按派别分组核心论文，按年份排序
- 提取派别间相互批评（mutual criticisms）
- 输出：派别对照表

#### Step 4: 收敛
- 精炼关键词（第二轮检索查询）
- ~20篇核心论文清单 + 剔除理由
- 选择2-3个派别进行深挖 + 选择理由

#### Step 5: 评价维度
- 领域关心的核心问题
- 共识性评价维度
- 场景特定权重

#### Step 6-7: 深读计划
- 阅读顺序推荐
- 每篇论文抽取模板（assumptions, contributions, mechanisms, limitations）
- 派别总结包（发展脉络, 理论基础, 实验结果, 局限性）

#### Step 8: 最终综合
- **机会/对比矩阵**（派别 × 优缺点/假设/场景/成本/改进）
- **推荐路线**（2-3条路线 + 理由）
- **创新机会列表**（从优缺点 × 场景需求对齐推导）
- **下一步行动清单**

### 执行流程

```
Step 1: 粘贴Phase 1筛选表 → pseudoctor-literature-mapper
  ↓
Step 2: 选择输出格式（推荐Markdown或Comparison Table）
  ↓
Step 3: literature-mapper进行8步分析
  ↓
Step 4: 获得派别对照表 + 核心20篇清单
  ↓
Step 5: 获得深读计划 + 抽取模板
  ↓
Step 6: 获得创新机会矩阵 + 推荐路线
  ↓
Step 7: 选择5-10篇必读论文，进入Phase 3（可选）
```

### 输出示例

```markdown
## 派别对照表（示例：Transformer时序预测）

| 派别 | 核心idea | 代表论文 | 优点 | 缺点 | 适用场景 |
|------|---------|---------|------|------|---------|
| **Informer派** | ProbSparse注意力降低复杂度 | Informer (AAAI 2021) | O(L log L)复杂度，长序列高效 | 稀疏注意力可能丢失信息 | 超长序列预测（L>1000） |
| **Decomposition派** | 序列分解+自相关 | Autoformer (NeurIPS 2021) | 分解趋势+季节性，可解释性强 | 分解假设可能不适用所有数据 | 有明显周期性的时序 |
| **Frequency派** | 频域注意力+傅里叶变换 | FEDformer (ICML 2022) | 频域计算效率高，长期依赖强 | 频域转换开销，非周期数据效果差 | 有周期模式的长期预测 |
| **线性派** | 简单线性模型 | DLinear (AAAI 2023) | 极简，计算快，某些数据集SOTA | 表达能力有限，非线性建模弱 | 线性趋势明显的数据 |
| **Patching派** | 时序Patch化（类似ViT） | PatchTST (ICLR 2023) | Channel-independence，泛化强 | Patch划分需调参 | 多变量独立性强的场景 |

## 核心20篇清单（收敛结果）
1. Informer (AAAI 2021) - 必读，开创性
2. Autoformer (NeurIPS 2021) - 必读，分解思想
3. FEDformer (ICML 2022) - 必读，频域方法
...（省略）

## 创新机会矩阵
| 机会点 | 派别组合 | 潜在改进 | 技术挑战 |
|--------|---------|---------|---------|
| **1. 频域分解融合** | Frequency派 + Decomposition派 | 频域分解+时域分解双重建模 | 计算开销，如何融合？ |
| **2. 自适应Patching** | Patching派 + Non-stationary派 | 根据分布漂移动态调整Patch大小 | Patch边界检测，在线更新 |
| **3. 轻量化Informer** | Informer派 + 线性派 | 结合ProbSparse+线性层，平衡性能与效率 | 稀疏模式学习，超参敏感 |
```

---

## 数据传递格式详解

### Phase 1 → Phase 2 数据传递

**最小传递包**（6个字段）:
```tsv
Title	Authors	Year	1-sentence_Summary	Is_Review	Candidate_School
Informer: Beyond...	Zhou et al.	2021	提出ProbSparse注意力...	N	Informer派
Autoformer: Decomposition...	Wu et al.	2021	引入序列分解+自相关...	N	Decomposition派
...
```

**推荐传递包**（完整17字段）:
```tsv
Paper_ID	Title	Authors	Year	Venue	URL	Material_Type	Keywords_Matched	Task	First_Read	1-sentence_Summary	Relevance_Score	Reason_Keep_or_Drop	Is_Review	Candidate_School	Must_Read_Level	Notes
P001	Informer...	Zhou et al.	2021	AAAI	https://...	Conference	Transformer;LSTF	Long Sequence Forecasting	Y	提出ProbSparse...	5	开创性...	N	Informer派	必读	里程碑论文
...
```

### 字段对应关系

| Phase 1 输出字段 | Phase 2 必需/推荐 | 用途 |
|-----------------|------------------|------|
| `Title` | ✅ 必需 | 论文唯一标识 |
| `Authors` | ✅ 必需 | 作者信息 |
| `Year` | ✅ 必需 | 时间线构建 |
| `1-sentence_Summary` | ✅ 必需 | 快速理解论文核心 |
| `Is_Review` | ⭐ 推荐 | 优先分析综述，快速建图 |
| `Candidate_School` | ⭐ 推荐 | 初步派别判断，加速分类 |
| `Keywords_Matched` | ⭐ 推荐 | 辅助派别归类 |
| `Relevance_Score` | 可选 | 优先级排序 |
| `Must_Read_Level` | 可选 | 深读计划参考 |
| 其他字段 | 可选 | 补充信息 |

---

## Phase 3 & 4: 深度阅读与批判（可选）

### Phase 3: pseudoctor-paper-reader

**使用场景**: 需要详细理解核心论文的方法、假设、实验设计时

**输入**:
- Phase 2 选定的5-10篇必读论文全文（PDF）

**输出**:
- 详细论文卡片（10 sections × 40+ fields）
- 证据绑定（每个claim都有excerpt + location marker）
- 自动识别论文类型（经验型/技术型/哲学型/混合型）

**耗时**: ~30分钟/篇

**示例输出章节**:
- Section 1: 元信息（Meta-info）
- Section 2: 研究问题（Research Question）
- Section 3: 方法骨架（Method Skeleton）
- Section 4: 核心假设（Core Assumptions）
- Section 5: 实验设计（Experiment Design）
- Section 6: 结果与证据（Results & Evidence）
- Section 7: 局限性（Limitations）
- Section 8: 贡献清单（Contributions）
- Section 9: 相关工作（Related Work）
- Section 10: 批判性问题（Critical Questions）

### Phase 4: pseudoctor-paper-criticalreviewer

**使用场景**: 需要评估论文创新性、发现问题、寻找改进空间时

**输入**:
- Phase 2/3 的核心论文

**输出**:
- 批判性洞察（5 sections）
  1. 核心痛点（Core Problem）- 一句话问题定义
  2. 解题机制（Solution Mechanism）- "aha moment"洞察
  3. 创新增量（Innovation Delta）- 相比SOTA的具体改进
  4. 批判性边界（Critical Boundaries）- 隐藏假设、未解决问题
  5. 一言以蔽之（Essence）- ASCII图 + 核心公式

**耗时**: ~15分钟/篇

**示例输出**:
```markdown
## 1. 核心痛点
问题: Transformer在长序列时间序列预测中复杂度为O(L²)，无法处理超长序列（L>1000）
根源: 标准自注意力机制需要计算所有时间步对之间的注意力权重

## 2. 解题机制
核心insight: 长时间序列的自相关分布是稀疏的，大部分时间步对的注意力权重接近0
神来之笔: ProbSparse自注意力——只计算top-K最重要的Query，复杂度降至O(L log L)

## 3. 创新增量
vs SOTA（LogTrans）: 速度提升3-5倍，内存占用减少50%
vs SOTA（Transformer）: 在ETTh1数据集上MSE降低18%

## 4. 批判性边界
隐藏假设: 稀疏注意力模式在所有时序数据上都成立（但密集依赖的数据可能失效）
未解决: 如何自适应确定稀疏度（top-K的K需要手动调参）

## 5. 一言以蔽之
[ASCII图展示ProbSparse注意力机制]
核心公式: Attention(Q,K,V) = Softmax(Q_sparse K^T / √d) V
```

---

## 完整示例：从主题到创新机会

### 用户输入
```
研究主题: Transformer在时间序列预测中的应用
子问题: 多变量长期预测
时间范围: 近5年（2019-2024）
```

### Phase 1 输出（pseudoctor-lit-search）
- **关键词矩阵**: 82个关键词（见`example_keywords.md`）
- **Boolean检索式**: 3套检索式（见`example_boolean.md`）
- **筛选表**: 24篇核心文献（见`example_table.md`）

### Phase 2 输入（传递筛选表）
```tsv
Paper_ID	Title	Authors	Year	1-sentence_Summary	Is_Review	Candidate_School
P001	Informer...	Zhou et al.	2021	提出ProbSparse注意力...	N	Informer派
P002	Autoformer...	Wu et al.	2021	引入序列分解+自相关...	N	Decomposition派
...（24篇）
```

### Phase 2 输出（pseudoctor-literature-mapper）
- **派别对照表**: 识别出5个派别（Informer派, Decomposition派, Frequency派, 线性派, Patching派）
- **核心20篇**: 收敛到20篇（剔除4篇重复/边缘论文）
- **深读计划**: 优先阅读顺序（Review → Informer → Autoformer → FEDformer → PatchTST → DLinear）
- **创新机会**: 3个机会点（频域分解融合, 自适应Patching, 轻量化Informer）

### Phase 3 输入（选择必读论文）
```
必读论文（5篇）:
1. Transformers in Time Series: A Survey (综述)
2. Informer (Informer派代表)
3. Autoformer (Decomposition派代表)
4. FEDformer (Frequency派代表)
5. PatchTST (Patching派代表)
```

### Phase 3 输出（pseudoctor-paper-reader）
- **5张详细论文卡片**（每张10 sections × 40+ fields）
- 证据绑定，忠实提取

### Phase 4 输入（核心论文批判）
```
批判对象（3篇）:
1. Informer
2. Autoformer
3. PatchTST
```

### Phase 4 输出（pseudoctor-paper-criticalreviewer）
- **3篇批判性分析**（每篇5 sections）
- 创新增量评估
- 批判性边界识别

### 最终产出
- ✅ 完整领域知识图谱（5个派别，20篇核心论文）
- ✅ 3个具体创新机会（频域分解融合, 自适应Patching, 轻量化Informer）
- ✅ 5张详细论文卡片（忠实提取）
- ✅ 3篇批判性分析（高密度洞察）

---

## 使用建议

### 何时使用完整4阶段流程？
- ✅ 博士开题/课题申请（需要系统性文献调研）
- ✅ 论文写作前的Related Work梳理
- ✅ 新领域学习（需要快速建立知识图谱）
- ✅ 寻找创新点（需要发现研究gap）

### 何时简化流程？
- ⚠️ 仅需快速了解领域 → Phase 1 + Phase 2 (Step 2综述分析)
- ⚠️ 已有核心论文清单 → 直接Phase 3 + Phase 4
- ⚠️ 仅需批判性分析 → 直接Phase 4

### 各阶段时间分配建议

| 阶段 | 耗时 | 占比 | 可否并行 |
|------|------|------|----------|
| Phase 1 | 6-8小时 | 40% | ❌ 必须第一步 |
| Phase 2 | 3-4小时 | 25% | ❌ 依赖Phase 1 |
| Phase 3 | 2.5-5小时（5篇×30分钟） | 20% | ✅ 可并行读多篇 |
| Phase 4 | 0.75-1.5小时（3篇×15分钟） | 10% | ✅ 可并行分析 |
| **总计** | **13-18.5小时** | **100%** | - |

---

## 常见问题

### Q1: Phase 1筛选表必须包含所有17个字段吗？
**A**: 不必须。最小必填项6个（Paper_ID, Title, Authors, Year, 1-sentence_Summary, Relevance_Score）即可传递给Phase 2。但完整17字段效果最佳。

### Q2: Phase 2能否跳过Phase 1直接使用？
**A**: 可以，但需要自己准备筛选表（至少包含Title, Authors, Year, 1-sentence_Summary 4个字段）。

### Q3: Phase 3和Phase 4可以并行吗？
**A**: 可以。Phase 3注重忠实提取（无外部知识），Phase 4注重批判分析（可用外部知识），两者互补，可并行进行。

### Q4: 如何选择Phase 2输出格式？
**推荐**:
- **Markdown**: 适合文档/Notion粘贴，可读性高
- **Comparison Table**: 适合快速对比派别优缺点
- **PPT Outline**: 适合组会汇报

### Q5: 筛选表可以手动修改吗？
**A**: 可以。Phase 1输出筛选表后，可以手动调整（添加论文、修改Candidate_School等），然后传递给Phase 2。

---

## 附录：字段映射表（完整17字段）

| Phase 1字段 | Phase 2使用 | Phase 3使用 | Phase 4使用 | 说明 |
|------------|------------|------------|------------|------|
| Paper_ID | ✅ | ✅ | ✅ | 唯一标识符 |
| Title | ✅ | ✅ | ✅ | 论文标题 |
| Authors | ✅ | ✅ | ✅ | 作者 |
| Year | ✅ | ✅ | ✅ | 年份，时间线构建 |
| Venue | ❌ | ✅ | ❌ | 期刊/会议，元信息 |
| URL | ❌ | ✅ | ✅ | 论文链接，获取全文 |
| Material_Type | ❌ | ❌ | ❌ | 材料类型 |
| Keywords_Matched | ⭐ | ❌ | ❌ | 辅助派别分类 |
| Task | ⭐ | ❌ | ❌ | 任务分类 |
| First_Read | ❌ | ❌ | ❌ | 标记是否已读 |
| 1-sentence_Summary | ✅ | ⭐ | ⭐ | 快速理解核心 |
| Relevance_Score | ⭐ | ❌ | ❌ | 优先级排序 |
| Reason_Keep_or_Drop | ❌ | ❌ | ❌ | 筛选理由 |
| Is_Review | ⭐ | ❌ | ❌ | 优先分析综述 |
| Candidate_School | ⭐ | ❌ | ❌ | 初步派别判断 |
| Must_Read_Level | ⭐ | ❌ | ❌ | 深读计划参考 |
| Notes | ❌ | ❌ | ❌ | 补充信息 |

**图例**:
- ✅ 必需字段
- ⭐ 推荐字段（显著提升效果）
- ❌ 可选字段

---

**Version**: 1.0
**Last Updated**: 2026-01-11
**Status**: ✅ Production Ready - 完整工作流集成指南
