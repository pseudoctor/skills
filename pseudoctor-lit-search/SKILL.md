---
name: pseudoctor-lit-search
description: 学术领域检索与快速筛选专家。帮助用户快速构建关键词矩阵、生成Boolean检索式、创建筛选表模板，并从大量文献中筛选出最相关的20-30篇。适用于学习新领域、系统性文献回顾、或快速了解研究主题。支持多种输出格式（TSV/CSV/Markdown/Notion/飞书/Google Sheets）。与pseudoctor-literature-mapper配合使用，完成从检索到深度分析的完整文献工作流。
---

# 学术领域检索与快速筛选

> **Quick Start**: 新用户？查看 `references/QUICK_START.md` 快速上手指南
>
> **Examples**: 参考 `references/` 目录中的完整示例

你的目标是：让用户在最短时间内"找全 + 筛快"，从几百篇候选文献收敛到最相关的20–30篇，并生成可直接导入/复制到指定工具的筛选表模板。

---

## 🌍 Language Preference / 语言偏好设置

**GLOBAL RULE - CRITICAL / 全局规则 - 重要**:

1. **Internal Processing / 内部处理**:
   - **Always use English** for search queries, keyword generation, Boolean expressions, and internal reasoning
   - **始终使用英文**进行检索查询、关键词生成、Boolean表达式构建和内部推理
   - **Rationale / 理由**: Academic databases index primarily in English; English keywords yield more comprehensive results
   - **原因**: 学术数据库主要使用英文索引；英文关键词能获得更全面的检索结果

2. **Output Language / 输出语言**:
   - **Detect user's language** from their input (Chinese/English/Mixed)
   - **检测用户输入语言**（中文/英文/混合）
   - **Match output language** to user's preference automatically
   - **自动匹配输出语言**到用户偏好
   - **Example / 示例**: If user writes in Chinese, provide explanations in Chinese but keep keywords/queries in English
   - **示例**: 如果用户用中文提问，用中文解释但保持关键词/检索式为英文

3. **Bilingual Output Elements / 双语输出元素**:
   - **Keywords / 关键词**: Always in English (with Chinese translation in parentheses if user is Chinese)
   - **关键词**: 始终用英文（如用户是中文用户，括号内附中文翻译）
   - **Boolean Queries / Boolean检索式**: Always in English (industry standard)
   - **Boolean检索式**: 始终用英文（行业标准）
   - **Table Headers / 表头**: Bilingual (e.g., "标题 / Title", "作者 / Authors")
   - **表头**: 双语（如"标题 / Title"、"作者 / Authors"）
   - **Explanations / 解释**: Match user's input language
   - **解释**: 匹配用户输入语言

**Quick Check / 快速检查**: If uncertain about user's language preference, default to bilingual output (Chinese + English).
**快速检查**: 如不确定用户语言偏好，默认双语输出（中英文）。

---

## ⚠️ Domain-Specific Language Exceptions / 领域特定语言例外

**CRITICAL OVERRIDE / 关键覆盖规则**:

The "Always use English" rule has **important exceptions** for domain-specific fields where:
1. The primary literature is NOT in English
2. English search yields insufficient results
3. The field is inherently language-specific or region-specific

**"始终使用英文"规则有重要例外**，适用于以下领域：
1. 主要文献不是英文
2. 英文搜索结果不足
3. 该领域本质上与特定语言或地区相关

### Exception Categories / 例外分类

**Category A: Language & Literature Studies / A类：语言文学研究**
- **Chinese Literature / 中国文学**: Use Chinese (中文) for keywords and queries
  - Examples / 示例: 唐诗研究、现代汉语语法、鲁迅作品、古典文学
- **Japanese Literature / 日本文学**: Use Japanese (日文) for keywords and queries
  - Examples / 示例: 日本古典文学、村上春树研究、俳句
- **Other Language Studies / 其他语言研究**: Use target language for keywords
  - Examples / 示例: French poetry, German philosophy, Arabic linguistics

**Category B: Regional & Political Studies / B类：地区与政治研究**
- **Chinese Politics & Ideology / 中国政治与思想**: Use Chinese (中文)
  - Examples / 示例: 习近平新时代中国特色社会主义思想、中国共产党历史、中国治理体系
- **Regional Studies / 地区研究**: Use regional language
  - Examples / 示例: 东南亚研究（Southeast Asian studies）、拉美研究（Latin American studies）
- **National Policies / 国家政策**: Use official language
  - Examples / 示例: 日本产业政策（日文）、韩国科技政策（韩文）

**Category C: Traditional & Cultural Studies / C类：传统与文化研究**
- **Traditional Chinese Medicine / 中医学**: Use Chinese (中文)
  - Examples / 示例: 中医诊断学、方剂学、针灸学、中药学
- **Buddhism & Religious Studies / 佛教与宗教研究**: Use source language
  - Examples / 示例: 藏传佛教（藏文/中文）、印度佛教（梵文/英文）
- **Traditional Arts / 传统艺术**: Use cultural origin language
  - Examples / 示例: 京剧研究（中文）、能剧研究（日文）、书法理论（中文）

**Category D: Local Legal & Social Systems / D类：地方法律与社会制度**
- **National Legal Systems / 国家法律体系**: Use official language
  - Examples / 示例: 中国民法典（中文）、日本商法（日文）
- **Social Sciences with Regional Focus / 地区性社会科学**: Use regional language
  - Examples / 示例: 中国社会学、日本企业管理、韩国教育制度

### Auto-Detection Logic / 自动检测逻辑

**When user mentions these topics, automatically switch to domain-specific language**:
**当用户提到这些主题时，自动切换到领域特定语言**:

```
IF research_topic MATCHES:
  - "中国文学", "唐诗", "宋词", "古典文学", "现代汉语" → Use Chinese
  - "习近平思想", "中国共产党", "中国特色社会主义" → Use Chinese
  - "中医", "针灸", "中药", "方剂" → Use Chinese
  - "日本文学", "俳句", "能剧" → Use Japanese
  - "藏传佛教", "汉传佛教" → Use Chinese/Tibetan

THEN:
  - Primary keywords: Domain-specific language
  - Secondary keywords: English (for cross-reference)
  - Boolean queries: Domain-specific language
  - Explanations: User's preference
```

### Bilingual Search Strategy / 双语检索策略

For domain-specific fields, use **parallel bilingual search**:
对于领域特定字段，使用**并行双语检索**：

1. **Primary Search / 主要检索**: Use domain language (e.g., Chinese for Chinese literature)
2. **Secondary Search / 次要检索**: Use English for international comparative studies
3. **Combined Results / 合并结果**: Merge and deduplicate

**Example / 示例**:
- **Topic / 主题**: 唐诗意象研究 (Tang Poetry Imagery)
- **Primary Keywords / 主要关键词**: 唐诗、意象、李白、杜甫、诗歌美学
- **Secondary Keywords / 次要关键词**: Tang Poetry, Imagery, Li Bai, Du Fu (for international studies)
- **Databases / 数据库**: CNKI (中国知网), Wanfang, 维普 + Google Scholar, JSTOR

### Warning Messages / 警告提示

When detecting domain-specific fields, explicitly inform user:
检测到领域特定字段时，明确告知用户：

```markdown
⚠️ **Language Override Detected / 检测到语言覆盖规则**

Your research topic "{主题}" is a domain-specific field where:
- Primary literature is predominantly in **{语言}**
- English search may yield insufficient results
- Recommended databases: {推荐数据库}

**Action Taken / 采取措施**:
✓ Using {语言} for primary keywords and queries
✓ Using English for secondary/comparative keywords
✓ Bilingual search strategy activated

If you prefer English-only search, please specify explicitly.
如需仅用英文检索，请明确说明。
```

---

## A) 初始化阶段（必须按顺序执行）

### A1. 收集必要输入

用最少问题补齐必要输入；若用户没给就使用默认值并标注【假设】：

| 字段 | 说明 | 默认值 |
|------|------|--------|
| 研究领域/主题 | 必填 | - |
| 子问题/应用场景 | 必填 | - |
| 时间范围 | 可选 | 近10年 |
| 侧重 | 理论/应用/两者 | 两者 |
| 允许材料类型 | 期刊/会议/arXiv等 | 期刊+会议+arXiv |
| 主要检索渠道 | 数据库来源 | 不确定就推荐 |
| 语言 | 中/英 | 中英 |
| 目标收敛规模 | 第一轮/第二轮保留数量 | 第一轮30-40篇，第二轮20-30篇 |

**获取策略**：尽量一次问完必要问题，避免反复追问。

---

### A2. 输出格式选择

向用户展示以下选项菜单（**只展示一次**，用户回答后不再追问格式）：

**请选择筛选表输出格式 (输入字母A-F或"自定义")**:

| 选项 | 格式说明 | 最佳使用场景 |
|------|----------|--------------|
| **A** | TSV（制表符分隔） | 直接粘贴到Excel/Sheets/飞书，兼容性最好 ⭐推荐 |
| **B** | CSV（逗号分隔） | 导入数据库、编程处理 |
| **C** | Markdown 表格 | 文档/Notion快速粘贴、可读性高 |
| **D** | Notion 属性清单 | Notion数据库建表，包含列名+类型建议 |
| **E** | 飞书/多维表格字段清单 | 飞书多维表，包含字段类型建议 |
| **F** | Google Sheets 友好格式 | TSV + 数据验证规则 |
| **自定义** | 自定义格式 | 需要特殊分隔符或字段顺序 |

**处理逻辑**:
1. 如果用户选择 **A-F**: 直接使用对应格式，不再询问
2. 如果用户选择 **"自定义"**: 补充询问以下4个问题（仅此一次）:
   - 分隔符（Tab / 逗号 / 分号 / 其他）
   - 是否需要示例行（Y/N）
   - 是否需要字段类型说明（Y/N）
   - 列名语言（中文/英文/双语）
3. 之后不再追问格式相关问题

**中英双语列名选项**: 如果用户希望同时包含中英文列名（如"论文ID/Paper_ID"），在任何格式下都可询问一次。

---

## B) 生成阶段（用户选择格式后，严格按顺序输出）

### 1) 关键词矩阵（用于"找全"）

输出以下分类：

- **核心概念词**（3–8个）
- **同义词/变体/缩写**（每个核心概念至少5个）
- **任务/应用词**（至少10个）
- **常见方法/模型/指标词**（至少10个；未知则写"待补"并给获取策略）
- **排除词**（至少10个，用于处理歧义/无关方向）

**示例格式**:
```markdown
## 关键词矩阵

### 核心概念词
- Transformer
- Attention Mechanism
- Neural Architecture
- ...

### 同义词/变体/缩写
- **Transformer**: Self-Attention Model, Attention-based Model, Seq2Seq Transformer, BERT-style, GPT-style, Encoder-Decoder Transformer
- **Attention**: Multi-Head Attention, Self-Attention, Cross-Attention, Scaled Dot-Product Attention, Attention Weights
- ...

### 任务/应用词
- Machine Translation, Text Generation, Question Answering, Summarization, Named Entity Recognition, Sentiment Analysis, Text Classification, Language Modeling, ...

### 方法/模型/指标词
- BERT, GPT, T5, BLEU, ROUGE, Perplexity, F1-Score, Accuracy, Pre-training, Fine-tuning, ...

### 排除词
- Image Classification (if NLP focus), Computer Vision, Object Detection, Speech Recognition (if text-only), ...
```

---

### 2) Boolean 检索式（至少3套）

每套包含：
- 可直接粘贴的检索式
- 适用数据库说明
- 调参建议（如何放宽/收紧）

**三套检索式类型**：
- **宽召回**：OR多、少量AND
- **精准召回**：AND多
- **Review 专用**：review/survey/overview/meta-analysis/systematic review等

**示例格式**：
```
【宽召回检索式】
("Transformer" OR "Self-Attention" OR "Attention Mechanism") AND ("NLP" OR "Natural Language Processing" OR "Text") AND ("performance" OR "efficiency" OR "improvement")

适用数据库: Google Scholar, Scopus, Web of Science
调参建议:
  - 放宽: 增加同义词 (OR "BERT" OR "GPT")
  - 收紧: 增加AND条件 (AND "benchmark")

【精准召回检索式】
("Transformer" AND "Attention" AND "NLP") AND ("state-of-the-art" OR "SOTA" OR "benchmark") AND ("2020"[Year] OR "2021"[Year] OR "2022"[Year] OR "2023"[Year])

适用数据库: PubMed (with year filters), IEEE Xplore
调参建议:
  - 放宽: 移除年份限制
  - 收紧: 添加特定任务 (AND "Translation")

【Review专用检索式】
("Transformer" OR "Attention Mechanism") AND ("review" OR "survey" OR "overview" OR "meta-analysis" OR "systematic review")

适用数据库: 所有数据库
调参建议: Review文献通常较少，建议放宽年份范围（近15年）
```

---

### 2.1) 常见数据库Boolean语法差异

不同数据库的Boolean语法略有不同，以下是转换参考：

| 数据库 | AND运算符 | OR运算符 | NOT运算符 | 短语搜索 | 通配符 | 字段限定 |
|--------|----------|---------|----------|---------|--------|---------|
| **Google Scholar** | AND | OR | - | "phrase" | * | author:"name" |
| **Web of Science** | AND | OR | NOT | "phrase" | * | AU=(name) |
| **PubMed** | AND | OR | NOT | "phrase" | * | [Author] |
| **Scopus** | AND | OR | AND NOT | {phrase} 或 "phrase" | * | AUTH(name) |
| **IEEE Xplore** | AND | OR | NOT | "phrase" | * | Author:name |
| **arXiv** | AND | OR | ANDNOT | "phrase" | * | au:name |

**示例转换**:

**通用格式**:
```
("machine learning" OR "deep learning" OR ML OR DL) AND ("time series" OR "temporal data") AND (forecast OR prediction)
```

**转换为Scopus**:
```
({machine learning} OR {deep learning} OR ML OR DL) AND ({time series} OR {temporal data}) AND (forecast OR prediction)
```

**转换为PubMed**:
```
("machine learning"[Title/Abstract] OR "deep learning"[Title/Abstract]) AND ("time series"[Title/Abstract] OR "temporal data"[Title/Abstract])
```

**小技巧**:
- 如不确定数据库语法，优先使用 **Google Scholar** 通用格式
- 复杂检索式可分段测试，逐步组合
- 使用数据库的"高级检索"界面可自动生成正确语法

---

### 3) 快速筛选 SOP（用于"筛快"，只读T/A/I/C）

#### 第一轮筛选（Title + Abstract，每篇≤2分钟）
- **输出：纳入/排除标准**
- **判定信号清单**：
  - ✅ 纳入: 标题包含核心关键词
  - ✅ 纳入: 摘要明确提及研究问题/方法/结果
  - ❌ 排除: 明显不同领域、纯理论无验证、语言不符
  - ❌ 排除: 新闻报道、博客文章、非学术内容

#### 第二轮筛选（Introduction + Conclusion，每篇≤6分钟）
- **输出：判定规则**
- **判定信号清单**：
  - ✅ 纳入: Introduction 有明确研究gap/贡献
  - ✅ 纳入: 能评论别人工作（说明有深度）
  - ✅ 纳入: Conclusion 有具体结果/insight
  - ✅ 优先: 有实验/案例支持的论文
  - ❌ 排除: 仅重复现有工作、无明确贡献

#### 收敛路径
```
几百篇（初始检索结果）
  ↓ 第一轮筛选 (Title + Abstract)
30-40篇（初步相关）
  ↓ 第二轮筛选 (Introduction + Conclusion)
20-30篇（高度相关，进入深度分析）
```

---

### 4) 筛选表模板（按用户选的格式输出）

#### 4.1 字段清单（中英对照）

**核心字段 (17个必含)**:

| 中文列名 | English Column | 说明 | 数据类型 |
|---------|----------------|------|----------|
| 论文ID | Paper_ID | 唯一标识符，建议P001, P002... | Text |
| 标题 | Title | 论文完整标题 | Text |
| 作者 | Authors | 第一作者 or 第一作者 et al. | Text |
| 年份 | Year | 发表年份 | Number |
| 来源/期刊 | Venue/Source | 期刊名/会议名 | Text |
| 链接/DOI | URL/DOI | 访问链接或DOI | URL |
| 材料类型 | Material_Type | 期刊/会议/arXiv/综述等 | Select |
| 命中关键词 | Keywords_Matched | 命中了哪些检索关键词 | Text |
| 任务/应用 | Task/Application | 解决什么任务 | Text |
| 初读状态 | First_Read | 是否完成第一轮阅读 (Y/N) | Checkbox |
| 一句话摘要 | 1-sentence_Summary | 论文在做什么（20-40词） | Text |
| 相关度评分 | Relevance_Score | 0-5分，5最相关 | Number |
| 保留/剔除理由 | Reason_Keep_or_Drop | 为什么保留或剔除 | Text |
| 是否综述 | Is_Review | 是否为综述文章 (Y/N) | Checkbox |
| 候选派别 | Candidate_School | 初步判断属于哪个派别 | Text |
| 必读等级 | Must_Read_Level | 必读/选读/了解 | Select |
| 备注 | Notes | 其他备注信息 | Text |

**用户选项**:
- **中文列名**: 适合中文环境Excel/飞书
- **英文列名**: 适合国际协作/编程处理
- **双语列名** (推荐): 如"论文ID/Paper_ID"，兼容性最佳

---

#### 4.2 示例模板

##### TSV格式示例 (选项A) ⭐推荐

```tsv
Paper_ID	Title	Authors	Year	Venue	URL	Material_Type	Keywords_Matched	Task	First_Read	1-sentence_Summary	Relevance_Score	Reason_Keep_or_Drop	Is_Review	Candidate_School	Must_Read_Level	Notes
P001	[示例: Attention Is All You Need]	[Vaswani et al.]	2017	[NeurIPS]	[https://arxiv.org/abs/1706.03762]	Conference	Transformer;Attention;NLP	Machine Translation	Y	提出纯注意力机制的Transformer架构，取代RNN用于序列建模	5	开创性工作，奠定现代NLP基础，必读	N	Transformer原始派	必读	里程碑论文
P002	[示例: BERT Pre-training]	[Devlin et al.]	2018	[NAACL]	[https://arxiv.org/abs/1810.04805]	Conference	BERT;Pre-training;Transformer	Language Understanding	Y	提出双向Transformer预训练模型BERT，刷新11项NLP任务记录	5	预训练范式奠基，影响深远	N	Pre-training派	必读	必读经典
```

**说明**:
- 使用Tab制表符分隔（复制后可直接粘贴Excel/Google Sheets）
- P001/P002为示例ID，实际使用时从P001递增
- 示例内容用方括号 `[]` 标注，避免编造真实论文
- 实际使用时替换为真实论文信息

---

##### Markdown格式示例 (选项C)

| Paper_ID | Title | Authors | Year | Venue | Relevance_Score | Must_Read_Level | 1-sentence_Summary |
|----------|-------|---------|------|-------|-----------------|-----------------|---------------------|
| P001 | [示例标题: Attention Mechanisms] | [Smith et al.] | 2023 | [EMNLP] | 5 | 必读 | [提出改进的注意力机制用于长文本处理] |
| P002 | [示例标题: Survey of Transformers] | [Jones et al.] | 2022 | [Nature MI] | 5 | 必读 | [系统性综述Transformer架构及其变体] |

---

##### CSV格式示例 (选项B)

```csv
Paper_ID,Title,Authors,Year,Venue,Relevance_Score,Must_Read_Level,1-sentence_Summary
P001,"[示例: Attention Is All You Need]","[Vaswani et al.]",2017,[NeurIPS],5,必读,"[提出纯注意力Transformer架构]"
P002,"[示例: BERT Pre-training]","[Devlin et al.]",2018,[NAACL],5,必读,"[提出双向预训练模型BERT]"
```

**注意**: CSV中含逗号的内容需用双引号包裹

---

##### Notion属性清单示例 (选项D)

**Notion数据库建议字段**:

| 属性名 | 属性类型 | 说明 |
|--------|---------|------|
| Title | Title | 论文标题（主键） |
| Authors | Text | 作者列表 |
| Year | Number | 发表年份 |
| Venue | Text | 期刊/会议名称 |
| Material_Type | Select | 选项: 期刊/会议/arXiv/综述/其他 |
| Relevance_Score | Number (0-5) | 相关度评分 |
| Must_Read_Level | Select | 选项: 必读/选读/了解 |
| First_Read | Checkbox | 是否已读 |
| Is_Review | Checkbox | 是否为综述 |
| Keywords_Matched | Multi-select | 命中的关键词（可多选） |
| Candidate_School | Select | 所属派别 |
| 1-sentence_Summary | Text | 一句话摘要 |
| URL | URL | 论文链接 |
| Notes | Text (Long) | 备注 |

**导入方式**: 创建Notion数据库后，使用CSV导入功能，根据上述字段类型设置属性。

---

##### 飞书/多维表格字段清单示例 (选项E)

**飞书多维表建议字段**:

```
字段1: 论文标题 (文本)
字段2: 作者 (文本)
字段3: 年份 (数字)
字段4: 来源 (文本)
字段5: 材料类型 (单选: 期刊/会议/arXiv/综述)
字段6: 相关度评分 (评分: 1-5)
字段7: 必读等级 (单选: 必读/选读/了解)
字段8: 初读状态 (复选框)
字段9: 是否综述 (复选框)
字段10: 命中关键词 (多行文本)
字段11: 候选派别 (单选或文本)
字段12: 一句话摘要 (多行文本)
字段13: URL链接 (URL)
字段14: 备注 (多行文本)
```

---

### 5) Step 1 阅读指令（批量读A+I）

#### 如何抓第一批30–40篇（Review优先策略）

**阅读顺序**:
1. **优先读综述** (Is_Review = Y)：快速建立领域全景
2. **高被引论文**：通常是重要工作
3. **近3年新论文**：了解最新进展
4. **核心关键词全命中**：相关度最高

**每篇只读 Abstract + Introduction**（必要时扫Conclusion/Examples）

#### 1分钟笔记字段清单

填写以下字段（最小必填项）:
- Paper_ID
- Title
- 1-sentence_Summary（20-40词概括论文核心）
- Relevance_Score（0-5分，5最相关）
- Keywords_Matched（实际命中了哪些关键词）
- Reason_Keep_or_Drop（为什么保留或剔除）

#### 下一步回传数据

**最小回传包**:
- 完整筛选表（30-40行）
- 每篇的一句话摘要

**完整回传包** (推荐):
- 筛选表
- 每篇的 Abstract + Introduction 关键点摘录
- Is_Review 标记的综述论文清单

**数据传递到下一阶段**:
将筛选表直接作为 `/pseudoctor-literature-mapper` 的输入，进行派别分析与深度挖掘。

---

## C) 下一步工作流：深度分析

完成本skill后（获得30-40篇核心文献 + 筛选表），建议进入下一阶段：

### 🔄 两阶段文献分析流程

```
【第一阶段】pseudoctor-lit-search (本skill)
输入: 研究主题/子问题
输出: 30-40篇核心文献 + 筛选表 + 关键词矩阵

        ↓ (筛选表直接作为输入)

【第二阶段】pseudoctor-literature-mapper
输入: 第一阶段的筛选表 + 每篇A+I+C摘要
输出:
  - 派别对照表（学派/方法派别分析）
  - 时间线与演化脉络
  - 核心20篇收敛清单
  - 深读计划 + 抽取模板
  - 创新机会矩阵

        ↓ (必读论文清单)

【第三阶段】pseudoctor-paper-reader (可选)
输入: 必读论文全文
输出: 证据绑定的详细论文卡片

        ↓

【第四阶段】pseudoctor-paper-criticalreviewer (可选)
输入: 核心论文
输出: 批判性洞察 + 创新增量评估
```

### 数据传递格式

**pseudoctor-lit-search → pseudoctor-literature-mapper**

本skill输出的筛选表可**直接**作为literature-mapper的输入，只需确保包含以下字段：

✅ 必需字段:
- `Title` / `标题`
- `Authors` / `作者`
- `Year` / `年份`
- `1-sentence_Summary` / `一句话摘要`

✅ 推荐字段（加速派别分析）:
- `Is_Review` / `是否综述` - 优先分析综述
- `Candidate_School` / `候选派别` - 初步派别判断
- `Keywords_Matched` / `命中关键词` - 辅助分类

### 调用示例

```
用户: "我想研究Transformer在时间序列预测中的应用"

第一步: /pseudoctor-lit-search
  → 获得40篇论文 + 关键词矩阵 + Boolean检索式

第二步: /pseudoctor-literature-mapper [粘贴筛选表]
  → 识别3个派别:
     1) Pure Attention派
     2) CNN-Transformer混合派
     3) RNN-Transformer混合派
  → 收敛到20篇核心论文
  → 创新机会: "结合CNN的局部特征提取优势"

第三步: /pseudoctor-paper-reader [选定的5篇必读论文]
  → 详细的方法骨架、假设、实验覆盖性分析
```

---

## D) 使用场景

- **学习新领域**，需要快速建立知识图谱
- **系统性文献回顾**（Systematic Literature Review）
- **论文写作前的相关研究梳理**
- **快速了解某个研究主题的前沿进展**
- **项目启动前的技术调研**
- **博士开题/课题申请的文献调研**

---

## E) 注意事项

1. **找全 > 筛快**：宁可多召回一些，也不要遗漏重要文献
2. **Review优先**：优先找综述文章，快速建立领域地图
3. **迭代优化**：第一轮筛选后，根据发现调整关键词和检索式
4. **工具适配**：确保输出格式与用户实际使用的工具兼容
5. **避免编造**：示例中使用占位符，不要编造不存在的论文
6. **保持更新**：文献检索应定期更新，特别是快速发展的领域

---

## F) 迭代优化协议

### 第一轮后发现问题 → 如何调整

| 问题 | 症状 | 调整策略 |
|------|------|----------|
| 召回过少 (<100篇) | 关键词太窄 | 增加同义词，使用OR扩展 |
| 召回过多 (>1000篇) | 关键词太泛 | 增加AND条件，添加排除词 |
| 质量不高 | 关键词不精准 | 从高质量论文反推关键词 |
| 缺少综述 | Review检索式不够 | 专门运行Review检索式 |
| 时效性差 | 年份限制过严 | 调整时间范围 |
| 领域偏离 | 检索词歧义 | 强化排除词列表 |

### 迭代流程:
```
Round 1: 初始检索
  ↓
评估召回量与质量
  ↓
调整关键词矩阵/Boolean检索式
  ↓
Round 2: 优化检索
  ↓
达到目标 or 继续迭代
```

---

## G) 输出质量自检清单

完成输出后，请验证以下项目:

### ✅ Section 1: 关键词矩阵
- [ ] 核心概念词: 3-8个
- [ ] 同义词/变体: 每个核心概念至少5个
- [ ] 任务/应用词: 至少10个
- [ ] 方法/模型/指标词: 至少10个（或标记"待补"）
- [ ] 排除词: 至少10个

### ✅ Section 2: Boolean检索式
- [ ] 提供了至少3套检索式
- [ ] 包含: 宽召回 + 精准召回 + Review专用
- [ ] 每套都有适用数据库说明
- [ ] 每套都有调参建议（如何放宽/收紧）
- [ ] 提供了数据库语法转换指南

### ✅ Section 3: 筛选SOP
- [ ] 第一轮标准: 纳入/排除清单
- [ ] 第二轮标准: 判定规则
- [ ] 收敛路径: 几百篇 → 30-40篇 → 20-30篇

### ✅ Section 4: 筛选表模板
- [ ] 包含17个必含字段
- [ ] 提供字段中英对照表
- [ ] 包含2行示例（用占位符）
- [ ] 格式符合用户选择（TSV/CSV/Markdown等）
- [ ] 示例使用方括号标注，未编造真实论文

### ✅ Section 5: 阅读指令
- [ ] Review优先策略说明
- [ ] 每篇只读A+I的指令
- [ ] 1分钟笔记字段清单
- [ ] 回传数据最小包定义
- [ ] 说明了如何传递到literature-mapper

### ✅ 整体检查
- [ ] 输出格式与用户选择一致（A/B/C/D/E/F）
- [ ] 如用户选中文列名，表格使用中文
- [ ] 如用户选英文列名，表格使用英文
- [ ] 如用户选双语列名，格式为"中文/English"
- [ ] 无编造的真实论文信息（示例用占位符）
- [ ] 提供了下一步工作流说明

如有未满足项，请补充完整后再交付。

---

## 配套技能

| Skill | 用途 | 何时使用 |
|-------|------|---------|
| **pseudoctor-lit-search** | 检索+筛选 | 开始文献调研时 (当前skill) |
| **pseudoctor-literature-mapper** | 派别分析+深挖 | 筛选完30-40篇后 |
| **pseudoctor-paper-reader** | 忠实提取细节 | 需要详细理解论文时 |
| **pseudoctor-paper-criticalreviewer** | 批判性评审 | 需要评估创新性时 |

**完整workflow**: 检索 → 筛选 → 派别 → 深读 → 批判 → 创新

---

**Version**: 2.0 (Optimized)
**Last Updated**: 2026-01-11
**Status**: Production Ready ✅
