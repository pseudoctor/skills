# 关键词矩阵完整示例

**研究主题**: Transformer在时间序列预测中的应用
**子问题**: 多变量长期时间序列预测
**时间范围**: 近5年（2019-2024）
**侧重**: 应用+理论

---

## 1. 核心概念词（6个）

- Transformer
- Time Series Forecasting
- Temporal Modeling
- Self-Attention
- Sequence Prediction
- Neural Architecture

---

## 2. 同义词/变体/缩写

### Transformer 同义词（7个）
- Self-Attention Model
- Attention-based Model
- Encoder-Decoder Architecture
- Transformer Network
- Multi-Head Attention Model
- Seq2Seq Transformer
- Attention Mechanism

### Time Series Forecasting 同义词（8个）
- Temporal Forecasting
- Time Series Prediction
- Sequential Prediction
- Temporal Prediction
- Future Value Estimation
- Trend Prediction
- Time-dependent Forecasting
- Temporal Extrapolation

### Self-Attention 同义词（6个）
- Multi-Head Attention
- Scaled Dot-Product Attention
- Attention Weights
- Query-Key-Value Attention
- Cross-Attention
- Temporal Attention

### 领域特定缩写（5个）
- TSF (Time Series Forecasting)
- LSTF (Long Sequence Time-series Forecasting)
- LTSF (Long-term Time Series Forecasting)
- MTS (Multivariate Time Series)
- MTSF (Multivariate Time Series Forecasting)

---

## 3. 任务/应用词（15个）

### 预测任务类型
- Multivariate Forecasting
- Long-term Prediction
- Short-term Prediction
- Multi-horizon Forecasting
- Rolling Forecast

### 应用领域
- Stock Price Prediction
- Energy Demand Forecasting
- Weather Forecasting
- Traffic Flow Prediction
- Electricity Load Forecasting
- Financial Forecasting
- Sensor Data Prediction
- IoT Time Series Analysis
- Climate Prediction
- Healthcare Time Series

---

## 4. 常见方法/模型/指标词（20个）

### 经典Transformer变体
- Informer
- Autoformer
- FEDformer
- Pyraformer
- LogTrans
- Reformer
- Temporal Fusion Transformer (TFT)

### 相关方法
- LSTM (对比baseline)
- GRU (对比baseline)
- CNN-based Time Series
- RNN
- Seq2Seq
- Encoder-Decoder
- Attention Mechanism

### 评价指标
- MSE (Mean Squared Error)
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)
- R-squared
- Forecasting Accuracy

---

## 5. 排除词（15个）

### 排除非时间序列领域
- Image Classification
- Computer Vision
- Object Detection
- Image Segmentation
- Face Recognition

### 排除纯NLP应用（保留时序NLP）
- Machine Translation (ONLY translation)
- Text Generation (ONLY text)
- Question Answering (ONLY QA)
- Named Entity Recognition
- Sentiment Analysis (ONLY sentiment)

### 排除非预测任务
- Anomaly Detection (ONLY detection)
- Classification (ONLY classification)
- Clustering (ONLY clustering)
- Dimensionality Reduction
- Feature Extraction (ONLY feature)

**注意**: 使用"ONLY"标记表示仅排除纯XX任务，如果论文涉及时间序列预测+XX则不排除

---

## 关键词矩阵总结

| 分类 | 数量 | 质量评估 |
|------|------|---------|
| 核心概念词 | 6个 | ✅ 符合要求（3-8个） |
| 同义词/变体 | 26个 | ✅ 每个核心概念>5个 |
| 任务/应用词 | 15个 | ✅ 符合要求（≥10个） |
| 方法/模型/指标词 | 20个 | ✅ 符合要求（≥10个） |
| 排除词 | 15个 | ✅ 符合要求（≥10个） |

**总计**: 82个关键词

---

## 如何使用该矩阵

### 构建宽召回检索式（使用核心词+同义词）
```
("Transformer" OR "Self-Attention Model" OR "Attention-based Model")
AND
("time series forecasting" OR "temporal forecasting" OR "temporal prediction" OR "TSF" OR "LSTF")
AND
("multivariate" OR "multi-variate" OR "long-term" OR "long sequence")
```

### 构建精准检索式（使用核心词+特定模型+任务）
```
("Transformer" AND "time series forecasting")
AND
("Informer" OR "Autoformer" OR "FEDformer" OR "Temporal Fusion Transformer")
AND
("multivariate" OR "long-term")
```

### 构建排除式（使用排除词）
```
("Transformer" AND "time series forecasting")
NOT
("image classification" OR "computer vision" OR "object detection" OR "NLP-only")
```

### 构建Review专用检索式
```
("Transformer" OR "Self-Attention")
AND
("time series" OR "temporal")
AND
("review" OR "survey" OR "overview" OR "meta-analysis" OR "systematic review")
```

---

## 迭代优化记录

**Round 1 初始版本**:
- 核心概念词: 4个
- 同义词: 12个
- 问题: 召回过少（<50篇）

**Round 1 调整**:
- 增加同义词: "Temporal Forecasting", "Sequential Prediction"
- 增加缩写: TSF, LSTF, LTSF
- 结果: 召回增加到150篇

**Round 2 优化**:
- 增加模型名称: Informer, Autoformer, FEDformer
- 增加应用领域: Energy, Traffic, Healthcare
- 结果: 召回250篇，质量提升

**Round 3 精炼**:
- 强化排除词: 添加"ONLY"标记避免过度排除
- 结果: 保留相关论文，最终收敛到200篇高质量文献

---

## 数据库适配建议

### Google Scholar（推荐首选）
使用通用格式，无需特殊语法

### PubMed（医疗健康领域）
```
("Transformer"[Title/Abstract] OR "Self-Attention"[Title/Abstract])
AND
("time series"[Title/Abstract] OR "temporal forecasting"[Title/Abstract])
```

### IEEE Xplore（工程技术领域）
```
("Transformer" OR "Self-Attention")
AND
("time series forecasting" OR "temporal prediction")
AND
(Stock OR Energy OR Traffic OR IoT)
```

### arXiv（最新预印本）
```
ti:Transformer AND ti:"time series"
OR
abs:Informer OR abs:Autoformer
```

---

**Version**: 1.0
**Last Updated**: 2026-01-11
**Domain**: Transformer + Time Series Forecasting
**Status**: ✅ Production Ready
