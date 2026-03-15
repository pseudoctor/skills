# literature-review-cartographer

用于把一组用户已提供的论文，转化为结构化文献综述、学术地图、冲突矩阵、概念谱系、研究空白、方法比较、隐含假设分析、知识图谱与压缩版综述短稿的 skill。

This skill turns a user-provided paper set into a structured literature review workflow with academic maps, contradiction matrices, concept lineages, research gaps, method comparisons, hidden assumptions, knowledge graphs, and review-ready short prose.

它适合“多论文综合分析”，不适合把单篇论文做成普通摘要。  
It is designed for cross-paper synthesis, not single-paper summarization.

## 快速开始 / Quick Start

最常见的调用方式：

```text
请使用 literature-review-cartographer。

我这里有一组关于[主题]的论文。请先做材料盘点，优先读取摘要、导言和结论，再根据证据情况输出：
1. 论文总表或最小阅读卡总表
2. 学术地图
3. 冲突矩阵
4. 核心概念谱系
5. 研究空白
6. 方法比较
7. 压缩综述

要求：
- 只基于我提供的材料
- 证据不足时明确降级
- 不要只按题名分组
```

Common English invocation:

```text
Please use literature-review-cartographer.

I have a set of papers on [topic]. Start with a corpus audit, read abstracts, introductions, and conclusions first, then produce:
1. a paper table or minimal reading-card table
2. an academic map
3. a contradiction matrix
4. concept lineages
5. research gaps
6. a methods comparison
7. a compressed review

Requirements:
- work only from the materials I provide
- explicitly downgrade claims when evidence is weak
- do not group papers by title alone
```

如果最终要写进论文，可继续要求：

```text
请把前面的分析压缩成 800-1200 字综述短稿，并改成中文核心期刊风格的脚注版。
不要编造卷期页码。
```

If the output needs to be paper-ready:

```text
Please compress the analysis into an 800-1200 word review-style short essay and provide a Chinese core-journal-style footnote version.
Do not fabricate issue or page metadata.
```

## 适用场景 / When To Use

当用户想做以下事情时，优先使用本 skill：

- 写文献综述
- 比较一组论文的共同点与分歧
- 画学术地图或知识图谱
- 找研究空白、争议区、未解问题
- 梳理一个领域的核心概念谱系
- 从几十到上百篇论文中筛核心文献
- 把分析压缩成中文核心期刊风格的脚注版综述短稿
- 处理中英文混合论文，而不是把中文和英文论文拆开各做一套

Use this skill when the user wants to:

- write a literature review from a paper set
- compare papers across agreements and disagreements
- build an academic map or knowledge graph
- identify research gaps, controversies, or unresolved questions
- trace the lineage of core concepts in a field
- narrow a large corpus into a justified core set
- convert structured analysis into a footnote-style short review
- analyze mixed Chinese-English corpora as one corpus

不适合的场景：

- 只读一篇论文
- 需要先全网搜文献、补 DOI、做真实被引检索
- 只是改写一段已有综述文字

Not a good fit when the task is:

- single-paper reading only
- external literature search, DOI completion, or citation lookup
- rewriting an existing review paragraph without cross-paper analysis

## 核心能力 / Core Capabilities

### 1. 结构化综述 / Structured Review

默认输出：

- 材料盘点
- 论文总表或最小阅读卡总表
- 学术地图
- 冲突矩阵
- 核心概念谱系
- 研究空白
- 方法比较
- 400 字压缩综述
- 隐含假设
- 知识图谱
- 5 分钟外行讲解

Default outputs include:

- corpus audit
- paper table or minimal reading-card table
- academic map
- contradiction matrix
- concept lineages
- research gaps
- method comparison
- compressed review
- hidden assumptions
- knowledge graph
- 5-minute plain-language explanation

这套输出的重点不是“逐篇复述”，而是把论文集合内部的结构关系讲清楚。  
The point is not paper-by-paper summary, but corpus-level structure.

### 2. 大语料处理 / Large-Corpus Handling

当论文很多时，不会直接拍脑袋缩到固定篇数，而是先看内容，再判断是否需要缩核心池。核心池规模由文献内容、领域结构和分歧密度决定，不预设固定篇数。

For large corpora, the skill does not force a fixed-size core set. It first reads content, then decides whether a core pool is needed and how large it should be based on representativeness, disagreement density, and field structure.

如果需要缩核心池，skill 会先做：

- 最小阅读卡总表
- 核心池评分表
- 入选/补充/暂缓理由

### 3. PDF 优先抽取 / PDF-First Extraction

如果输入主要是 PDF，默认先抽：

1. 题名页
2. 摘要/内容提要
3. 导言/问题提出
4. 结论/结语

Only when these cannot be extracted does the skill fall back to title-level pre-analysis.

### 4. 中英文混合支持 / Mixed Chinese-English Support

支持：

- 中文论文
- 英文论文
- 中英文混合论文

Rules:

- output language follows the user by default
- titles, author names, and key concepts stay in the original language when possible
- grouping is based on claims, questions, and conclusions rather than language
- equivalent concepts may be shown as `中文概念 / English term`

### 5. 核心池评分表 / Core-Pool Scoring Table

为了让筛选更稳定，skill 支持先输出“核心池评分表”，再决定是否纳入核心池。

Default dimensions:

- 代表性 / representativeness
- 分歧性 / disagreement value
- 枢纽性 / hub value
- 方法独特性 / methodological distinctiveness
- 重复度 / redundancy

常见判断结果：

- `核心保留 / keep as core`
- `补充保留 / keep as support`
- `暂缓纳入 / defer`

### 6. 综述短稿与脚注版成稿 / Review-Ready Short Prose

在结构化分析完成后，用户可以要求继续输出：

- `800-1200` 字综述短稿
- 中文核心期刊风格脚注版综述短稿

Footnote rules:

- use superscript markers
- place notes after the main body
- cite only confirmed metadata from user-provided materials
- do not fabricate issue or page details

## 模式与证据层级 / Modes And Evidence Levels

skill 会先判断当前材料属于哪一档，再决定输出力度：

- `Mode A`：大部分论文可读到全文或正文关键部分，可做强分析
- `Mode B`：只有摘要、引言、结论，可做较强初步分析
- `Mode C`：只有题录和少量文本，先做补料规划
- `Mode D`：当前只能稳定读取题名或题名页，只能做题名级预分析

The skill also marks certainty explicitly.

常用证据标记：

- `[证据充分]`
- `[证据有限]`
- `[需全文核验]`
- `[当前材料无法判断]`

常用证据层级：

- `[题名级预分析]`
- `[摘要级判断]`
- `[引言/结论级判断]`
- `[正文片段级判断]`
- `[全文级判断]`

默认原则：

- 先读摘要、导言、结论
- 先看内容，再决定是否缩核心池
- 不能把低证据层级写成高确定性结论

## 典型输出 / Typical Output Flow

一个完整回合中，最常见的输出顺序是：

1. 材料盘点
2. 最小阅读卡总表
3. 核心池评分表
4. 学术地图
5. 冲突矩阵
6. 核心概念谱系
7. 研究空白
8. 方法比较
9. 400 字综述
10. 隐含假设
11. 知识图谱
12. 5 分钟讲解
13. 可选：800-1200 字综述短稿
14. 可选：中文核心期刊风格脚注版短稿

## 工作流 / Workflow

推荐流程如下：

1. 盘点材料层级
2. 先读摘要、导言、结论
3. 必要时建立最小阅读卡总表
4. 若语料过大，再做核心池评分表
5. 决定核心池与边界文献
6. 输出地图、冲突、谱系、空白和方法比较
7. 最后压缩成短综述、知识图谱或脚注版综述短稿

## 输入建议 / Recommended Inputs

最低建议每篇至少提供：

- 标题
- 作者
- 年份
- 至少一段可分析文本

更理想的输入包括：

- 摘要
- 导言或问题提出
- 结论
- 方法或论证方式

如果给的是 PDF，优先保证能抽到：

- 题名页
- 摘要页
- 导言页
- 结论页

## 目录说明 / Directory Layout

- [SKILL.md](/Users/armewang/Downloads/paper/literature-review-cartographer-skill/SKILL.md)  
  主技能说明，包含触发描述、工作流、证据层级、语言规则和可选成稿模式。

- [references/output-contract.md](/Users/armewang/Downloads/paper/literature-review-cartographer-skill/references/output-contract.md)  
  输出契约，规定各模块的表格字段、降级规则、评分表模板和脚注版短稿格式。

- [references/example-input.md](/Users/armewang/Downloads/paper/literature-review-cartographer-skill/references/example-input.md)  
  可直接复用的 prompt 示例，覆盖大语料、PDF、中英文混合、脚注短稿、核心池评分表等场景。

- [agents/openai.yaml](/Users/armewang/Downloads/paper/literature-review-cartographer-skill/agents/openai.yaml)  
  UI 层显示名、短描述与默认 prompt。

## 使用建议 / Usage Notes

- 如果只有题录，不要急着做综述，先做补料规划。
- 如果有 PDF，优先抽摘要、导言和结论。
- 如果文献很多，先做最小阅读卡，再考虑缩核心池。
- 如果用户最终目标是写论文，前面的结构化分析完成后，最好顺手输出一版短稿或脚注版综述。

## 示例调用 / Example Prompts

中文：

```text
请使用 literature-review-cartographer。

我给你 32 篇关于“平台治理”的论文。请先做材料盘点，优先读取摘要、引言和结论，然后基于阅读卡识别核心文献、画学术地图、找冲突和研究空白。不要只按题名分组。
```

英文：

```text
Please use literature-review-cartographer.

I have a mixed Chinese-English corpus on digital sovereignty. Start with a corpus audit, extract abstracts, introductions, and conclusions where available, then build a reading-card table, identify core papers, and produce an academic map and contradiction matrix without splitting the corpus by language.
```

## 快速入口 / Recommended Entry Files

最推荐先看的两个文件：

- [SKILL.md](/Users/armewang/Downloads/paper/literature-review-cartographer-skill/SKILL.md)
- [references/example-input.md](/Users/armewang/Downloads/paper/literature-review-cartographer-skill/references/example-input.md)
