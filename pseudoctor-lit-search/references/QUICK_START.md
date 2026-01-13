# Quick Start: 3分钟了解学术检索与筛选

## 你需要什么？

**输入**:
- 研究主题/领域（例如："Transformer在时间序列预测中的应用"）
- 子问题或应用场景（例如："多变量时间序列预测"）
- 时间范围（可选，默认近10年）

## 你将获得什么？

**5个核心输出**:
1. **关键词矩阵** - 核心词 + 同义词 + 任务词 + 方法词 + 排除词（用于"找全"）
2. **Boolean检索式** - 3套检索式（宽召回/精准/Review专用），可直接粘贴到Google Scholar/PubMed等
3. **筛选SOP** - 两轮筛选标准（Title+Abstract → Introduction+Conclusion）
4. **筛选表模板** - 17字段表格（TSV/CSV/Markdown等格式，可直接导入Excel/Notion/飞书）
5. **阅读指令** - Review优先策略 + 1分钟笔记模板

**最终成果**: 从几百篇候选文献收敛到 **20-30篇核心文献**

## 3分钟示例

### 场景: 研究"Transformer在时间序列预测中的应用"

**Step 1: 提供输入**
```
研究领域: Transformer在时间序列预测中的应用
子问题: 多变量时间序列预测
时间范围: 近5年（2019-2024）
侧重: 应用+理论
```

**Step 2: 选择输出格式**
```
选择: A (TSV格式，可直接粘贴Excel)
列名: 双语（中文/English）
```

**Step 3: 获得输出**

#### 输出1: 关键词矩阵（部分）
```markdown
核心概念词:
- Transformer
- Time Series Forecasting
- Temporal Modeling

同义词/变体（Transformer）:
- Self-Attention Model
- Attention-based Time Series Model
- Temporal Transformer
- Informer
- Autoformer
- ...

任务/应用词:
- Multivariate Forecasting
- Long-term Prediction
- Stock Price Prediction
- Energy Demand Forecasting
- ...

排除词:
- Image Recognition（排除CV领域）
- NLP-only applications（仅NLP）
- Speech Recognition
- ...
```

#### 输出2: Boolean检索式（部分）
```
【宽召回检索式】
("Transformer" OR "Self-Attention" OR "Attention Mechanism") AND ("time series" OR "temporal" OR "forecasting" OR "prediction") AND ("multivariate" OR "multi-variate")

适用数据库: Google Scholar, arXiv, Scopus
预计召回: 200-500篇

【精准召回检索式】
("Transformer" AND "time series forecasting") AND ("multivariate" OR "long-term") AND ("2019"[Year] OR "2020"[Year] OR "2021"[Year] OR "2022"[Year] OR "2023"[Year] OR "2024"[Year])

适用数据库: PubMed, IEEE Xplore
预计召回: 50-150篇
```

#### 输出3: 筛选表模板（前2行示例）
```tsv
Paper_ID	Title	Authors	Year	Venue	Relevance_Score	Must_Read_Level	1-sentence_Summary
P001	[示例: Informer: Beyond Efficient Transformer]	[Zhou et al.]	2021	[AAAI]	5	必读	[提出ProbSparse自注意力机制，专门用于长时间序列预测（LSTF）]
P002	[示例: Autoformer: Decomposition Transformers]	[Wu et al.]	2021	[NeurIPS]	5	必读	[引入序列分解架构，结合自注意力用于长期预测]
```

**Step 4: 执行检索与筛选**

1. 复制Boolean检索式到Google Scholar
2. 下载前100篇论文的标题+摘要
3. 按筛选SOP进行两轮筛选:
   - **第一轮** (Title + Abstract, ≤2分钟/篇): 100篇 → 30-40篇
   - **第二轮** (Introduction + Conclusion, ≤6分钟/篇): 30-40篇 → 20-30篇
4. 填写筛选表（Paper_ID, Title, 1-sentence_Summary, Relevance_Score等）

**Step 5: 下一步工作流**

完成筛选后，将筛选表直接传递给 `/pseudoctor-literature-mapper`:
```
输入: 筛选表（20-30篇核心论文）
输出: 派别对照表 + 深读计划 + 创新机会矩阵
```

## 完整流程图

```
用户输入研究主题
    ↓
pseudoctor-lit-search 生成关键词矩阵 + Boolean检索式
    ↓
用户执行检索（Google Scholar/PubMed等）
    ↓
第一轮筛选 (Title + Abstract): 几百篇 → 30-40篇
    ↓
第二轮筛选 (Introduction + Conclusion): 30-40篇 → 20-30篇
    ↓
填写筛选表模板
    ↓
传递给 pseudoctor-literature-mapper 进行派别分析
```

## 常见问题

**Q1: 第一轮检索召回太少（<50篇），怎么办？**
- 使用**宽召回检索式**
- 增加同义词（OR扩展）
- 扩大时间范围（近10年 → 近15年）

**Q2: 第一轮检索召回太多（>1000篇），怎么办？**
- 使用**精准召回检索式**
- 增加AND条件（如添加特定任务词）
- 强化排除词（NOT条件）

**Q3: 筛选表应该用什么格式？**
- **推荐TSV格式（选项A）**：可直接粘贴到Excel/Google Sheets/飞书，兼容性最好
- 如需导入Notion，选择选项D（Notion属性清单）
- 如需编程处理，选择选项B（CSV）

**Q4: 17个字段太多，能简化吗？**
- 最小必填项（6个）：Paper_ID, Title, Authors, Year, 1-sentence_Summary, Relevance_Score
- 推荐必填项（10个）：最小必填项 + Venue, Keywords_Matched, First_Read, Is_Review
- 完整字段（17个）：用于后续派别分析时效果最佳

**Q5: 如何判断是否需要第三轮筛选？**
- 如果第二轮后仍有>40篇，建议第三轮筛选（读完整Method部分）
- 目标：收敛到20-30篇核心文献

## 预期时间投入

| 阶段 | 时间投入 | 说明 |
|------|---------|------|
| 生成关键词+检索式 | 10-15分钟 | 使用本skill自动生成 |
| 执行检索 | 5-10分钟 | 复制粘贴到数据库 |
| 第一轮筛选 (100篇→40篇) | 2-3小时 | 每篇≤2分钟 |
| 第二轮筛选 (40篇→25篇) | 2-4小时 | 每篇≤6分钟 |
| 填写筛选表 | 30-60分钟 | 整理笔记 |
| **总计** | **6-8小时** | 完成高质量文献筛选 |

## 下一步

完成本skill后，进入深度分析阶段:
- 使用 `/pseudoctor-literature-mapper` 进行派别分析（识别学派、构建领域地图）
- 使用 `/pseudoctor-paper-reader` 进行必读论文的详细提取
- 使用 `/pseudoctor-paper-criticalreviewer` 进行批判性评审

**完整workflow**: 检索筛选 → 派别分析 → 深度阅读 → 批判评审 → 创新机会

---

**准备好了吗？** 开始使用 `/pseudoctor-lit-search` 进行你的文献调研！
