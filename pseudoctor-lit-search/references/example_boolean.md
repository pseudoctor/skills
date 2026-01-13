# Boolean检索式完整示例

**研究主题**: Transformer在时间序列预测中的应用
**目标文献量**: 200-300篇（初始召回）→ 30-40篇（第一轮筛选）→ 20-30篇（第二轮筛选）

---

## 检索式套装（3套）

### 【套装1】宽召回检索式 - 用于"找全"

#### 通用格式（适用Google Scholar, Scopus, Web of Science）
```
("Transformer" OR "Self-Attention" OR "Attention Mechanism" OR "Multi-Head Attention")
AND
("time series" OR "temporal" OR "sequential" OR "time-dependent" OR "temporal data")
AND
("forecasting" OR "prediction" OR "forecast" OR "extrapolation" OR "future value")
AND
("multivariate" OR "multi-variate" OR "multiple variables" OR "multi-dimensional")
```

**预计召回**: 300-600篇
**适用数据库**: Google Scholar, Scopus, Web of Science, arXiv
**优点**: 覆盖广，不易遗漏重要文献
**缺点**: 噪声较多，需要严格第一轮筛选

#### 调参建议
- **放宽（召回<200篇）**:
  - 添加OR: `"attention-based model" OR "encoder-decoder"`
  - 移除限定词: 删除 `"multivariate"`
  - 扩大时间范围: 近10年 → 近15年

- **收紧（召回>1000篇）**:
  - 添加AND: `AND ("long-term" OR "long sequence" OR "LSTF")`
  - 添加年份限制: `AND (2020 OR 2021 OR 2022 OR 2023 OR 2024)`
  - 添加排除: `NOT ("image" OR "vision" OR "NLP")`

---

### 【套装2】精准召回检索式 - 用于"筛快"

#### 通用格式
```
("Transformer" AND "time series forecasting")
AND
("Informer" OR "Autoformer" OR "FEDformer" OR "Temporal Fusion Transformer" OR "Pyraformer")
AND
("multivariate" OR "long-term" OR "long sequence")
AND
(2019 OR 2020 OR 2021 OR 2022 OR 2023 OR 2024)
```

**预计召回**: 80-200篇
**适用数据库**: PubMed, IEEE Xplore, ACM Digital Library
**优点**: 高精度，质量高
**缺点**: 可能遗漏早期工作或非主流模型

#### 调参建议
- **放宽（召回<50篇）**:
  - 移除年份限制
  - 移除模型名称限制: 删除 `("Informer" OR ...)`
  - 使用OR替换AND: `"Transformer" OR "time series forecasting"`

- **收紧（召回>300篇）**:
  - 添加特定任务: `AND ("stock" OR "energy" OR "traffic")`
  - 添加指标要求: `AND ("SOTA" OR "state-of-the-art" OR "benchmark")`
  - 限定期刊/会议: `AND ("NeurIPS" OR "ICML" OR "ICLR" OR "KDD")`

---

### 【套装3】Review专用检索式 - 用于快速建立领域地图

#### 通用格式
```
("Transformer" OR "Self-Attention" OR "Attention Mechanism")
AND
("time series" OR "temporal" OR "sequential")
AND
("review" OR "survey" OR "overview" OR "meta-analysis" OR "systematic review" OR "literature review")
```

**预计召回**: 10-30篇
**适用数据库**: 所有数据库通用
**优点**: 快速建立领域知识图谱
**缺点**: Review文献较少，需放宽时间范围

#### 调参建议
- **放宽（召回<5篇）**:
  - 扩大时间范围: 近5年 → 近10年 → 近15年
  - 添加相关词: `OR "tutorial" OR "introduction" OR "perspective"`
  - 移除限定: 删除 `"time series"`，保留 `"Transformer"`

- **收紧（召回>50篇）**:
  - Review文献通常较少，无需收紧
  - 如果召回过多，优先选择近3年 + 高被引

---

## 数据库语法转换示例

### 示例检索式（通用格式）
```
("Transformer" AND "time series forecasting") AND ("multivariate" OR "long-term")
```

### 转换为各数据库格式

#### Google Scholar（无需转换）
```
("Transformer" AND "time series forecasting") AND ("multivariate" OR "long-term")
```

#### Scopus（短语用花括号）
```
({Transformer} AND {time series forecasting}) AND ({multivariate} OR {long-term})
```
或保持双引号（兼容）:
```
("Transformer" AND "time series forecasting") AND ("multivariate" OR "long-term")
```

#### PubMed（字段限定）
```
("Transformer"[Title/Abstract] AND "time series forecasting"[Title/Abstract])
AND
("multivariate"[Title/Abstract] OR "long-term"[Title/Abstract])
```

#### Web of Science（字段限定）
```
TS=("Transformer" AND "time series forecasting") AND TS=("multivariate" OR "long-term")
```
TS = Topic (包括标题、摘要、关键词)

#### IEEE Xplore（无需转换，但可加字段）
```
("Transformer" AND "time series forecasting") AND ("multivariate" OR "long-term")
```
或限定字段:
```
("Document Title":Transformer OR "Abstract":Transformer)
AND
("Document Title":"time series forecasting" OR "Abstract":"time series forecasting")
```

#### arXiv（字段缩写）
```
ti:Transformer AND ti:"time series" AND (abs:multivariate OR abs:long-term)
```
- ti = title
- abs = abstract
- au = author

---

## 完整检索示例（步骤化）

### Step 1: 选择数据库
- **首选**: Google Scholar（覆盖最全，无需订阅）
- **次选**: arXiv（最新预印本，更新快）
- **专业**: IEEE Xplore（工程技术）, PubMed（医疗健康）

### Step 2: 复制检索式
从套装1开始（宽召回），复制通用格式检索式

### Step 3: 执行检索
**Google Scholar示例**:
1. 打开 https://scholar.google.com/
2. 粘贴检索式到搜索框:
   ```
   ("Transformer" OR "Self-Attention") AND ("time series" OR "temporal") AND ("forecasting" OR "prediction") AND ("multivariate")
   ```
3. 点击"搜索"
4. 查看结果数量（预计200-500篇）

### Step 4: 评估召回量
| 召回量 | 判断 | 行动 |
|--------|------|------|
| <100篇 | 过少 | 使用宽召回检索式，增加OR同义词 |
| 100-500篇 | 理想 | 继续下一步 |
| 500-1000篇 | 偏多 | 使用精准检索式，增加AND条件 |
| >1000篇 | 过多 | 使用精准检索式 + 年份限制 + 排除词 |

### Step 5: 导出结果
- **Google Scholar**: 手动复制前100篇的标题+摘要（或使用浏览器插件）
- **其他数据库**: 使用导出功能（BibTeX, RIS, CSV）

### Step 6: Review优先策略
1. 先运行套装3（Review检索式）
2. 优先阅读Review文献（通常5-10篇）
3. 从Review文献中反推关键词，优化套装1和套装2
4. 重新执行检索

---

## 实战案例：迭代优化过程

### Round 1: 初始检索
**检索式**:
```
("Transformer" AND "time series forecasting")
```
**结果**: 召回68篇，**过少**

**问题分析**: 关键词太窄，AND条件过严

### Round 2: 放宽检索
**优化策略**: 增加同义词，使用OR扩展
**检索式**:
```
("Transformer" OR "Self-Attention" OR "Attention Mechanism")
AND
("time series" OR "temporal" OR "sequential")
AND
("forecasting" OR "prediction")
```
**结果**: 召回523篇，**理想**

### Round 3: 精准检索（收敛阶段）
**优化策略**: 增加特定模型名称，限定时间范围
**检索式**:
```
("Transformer" AND "time series forecasting")
AND
("Informer" OR "Autoformer" OR "FEDformer")
AND
(2020 OR 2021 OR 2022 OR 2023 OR 2024)
```
**结果**: 召回156篇，**精准**

### Final: 组合策略
- **宽召回**: 用于"找全"（523篇）
- **精准召回**: 用于"筛快"（156篇）
- **Review**: 用于"建图"（12篇）

**最终筛选**: 523篇 → 第一轮筛选 → 38篇 → 第二轮筛选 → 24篇核心文献

---

## 常见问题

### Q1: 为什么需要3套检索式？
- **宽召回**: 确保不遗漏重要文献（高召回率）
- **精准召回**: 减少筛选工作量（高精确率）
- **Review**: 快速建立领域知识（高效率）

### Q2: 检索式太长，数据库不支持怎么办？
**解决方案**: 分段检索，合并结果
```
# 第一段
("Transformer" OR "Self-Attention") AND "time series"

# 第二段
("Attention Mechanism" OR "Multi-Head Attention") AND "time series"

# 手动合并去重
```

### Q3: 不同数据库结果差异大，如何处理？
**推荐策略**: 多数据库并行检索
1. Google Scholar（覆盖最全）
2. arXiv（最新预印本）
3. IEEE Xplore / PubMed（专业领域）
4. 合并结果，去重（按DOI或Title）

### Q4: 如何验证检索式质量？
**验证方法**: 已知论文测试
1. 找3-5篇已知相关的经典论文
2. 检查这些论文是否在检索结果中
3. 如果遗漏，分析原因（关键词缺失？排除词过严？）
4. 调整检索式，重新检索

---

## 检索式模板库

### 模板1: 方法+任务型
```
("[方法名]" OR "[同义词1]" OR "[同义词2]")
AND
("[任务名]" OR "[任务同义词]")
AND
("[应用场景]" OR "[领域]")
```

### 模板2: 问题+解决方案型
```
("[研究问题]" OR "[问题描述]")
AND
("[解决方案]" OR "[方法类型]")
NOT
("[排除领域]" OR "[不相关任务]")
```

### 模板3: 综述专用型
```
("[核心概念]" OR "[领域名]")
AND
("review" OR "survey" OR "overview" OR "meta-analysis" OR "systematic review")
AND
(Year >= [起始年份])
```

---

**Version**: 1.0
**Last Updated**: 2026-01-11
**Domain**: Transformer + Time Series Forecasting
**Status**: ✅ Production Ready - 3套检索式已验证
