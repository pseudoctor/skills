# 示例输入

下面给出可直接粘贴给 `Codex`、`Claude Code`、`Gemini CLI` 的最小可复制输入示例。主 skill 为通用版，不依赖特定 CLI 的私有语法。

## 示例 1：完整综述任务（全文较齐）

```text
请使用 literature-review-cartographer。

我这里有 18 篇关于“平台劳动与算法治理”的论文，大部分有全文，少数只有摘要和结论。
请先做材料盘点，再按 skill 的完整流程输出：
1. 论文总表
2. 学术地图
3. 冲突矩阵
4. 3 个高频核心概念的谱系
5. 5 个未解问题
6. 方法比较
7. 400 字综述
8. 隐含假设
9. 知识图谱
10. 5 分钟外行讲解

要求：
- 中文输出
- 强证据绑定
- 没有把握的地方直接标“需全文核验”
```

## 示例 2：只有摘要/引言/结论

```text
请使用 literature-review-cartographer。

我给你 25 篇关于“生成式 AI 在高等教育中的应用”的论文，但目前只有标题、作者、年份、摘要、引言、结论。
请先说明哪些模块可以稳定做，哪些只能做初步判断。
然后继续输出：
- 论文总表
- 学术地图
- 初步冲突矩阵
- 初步概念谱系
- 初步研究空白
- 方法比较

要求：
- 所有高风险判断标注“需全文核验”
- 不要假装已经形成学界共识
```

## 示例 3：题录为主，先做补料规划

```text
请使用 literature-review-cartographer。

我这里有 42 篇关于“正确义利观与中国外交”的论文，目前只有题录和少量摘要。
不要直接写综述，先做：
1. 材料盘点
2. 哪些问题现在能分析，哪些不能
3. 优先补读的 10 篇论文
4. 一个后续可复用的信息提取模板
5. 如果我补到摘要+引言+结论，你下一轮可以怎么做
```

## 示例 4：只做某个模块

```text
请使用 literature-review-cartographer。

下面是 12 篇论文的摘要和结论。你先不要写完整综述，只做两件事：
1. 找出作者观点直接冲突的地方，做成冲突矩阵
2. 列出这些论文默认接受但很少论证的隐含假设

要求：
- 中文
- 表格优先
- 证据不足就直说
```

## 示例 5：大语料先缩池再分析

```text
请使用 literature-review-cartographer。

我这里有 96 篇关于“正确义利观与中国外交”的 PDF，大多数还没提取摘要。
这轮不要假装你已经通读全部全文，请按大语料流程做：
1. 材料盘点
2. 判断当前属于全文级、摘要级还是题名级
3. 如果证据不够，先做题名级预分析
4. 根据文献内容判断是否需要缩核心池，并决定核心池规模
5. 说明每篇入选或暂缓的理由
6. 给出预学术地图
7. 给出“直接冲突 / 解释性张力 / 潜在分歧线”的初步区分
8. 告诉我下一轮最该补哪几篇的摘要、引言和结论

要求：
- 不要把题名级判断写成定论
- 证据层级必须标清楚
- 中文输出
```

## 示例 6：大语料但必须先读摘要、导言、结论

```text
请使用 literature-review-cartographer。

我这里有 82 篇论文。刚开始不要只按题名分组，也不要只凭标题挑核心文献。
请按下面顺序工作：
1. 先盘点材料
2. 优先读取每篇的摘要、导言和结论
3. 先做一个“最小阅读卡总表”：摘要主张 + 导言问题 + 结论判断 + 方法/论证方式
4. 再根据这些阅读卡判断是否需要缩核心池，并决定核心池规模
5. 基于阅读卡而不是题名，给出学术地图和初步冲突矩阵

要求：
- 如果某篇缺摘要或结论，要明确标缺口
- 不要把题名级预分组当成正式结果
- 找核心文献时，优先看摘要、导言和结论里的信息
- 不要预设固定篇数，核心池大小应由文献内容决定
```

## 示例 7：PDF 先抽关键页面再分析

```text
请使用 literature-review-cartographer。

我上传的是一批 PDF，不是已经整理好的摘要表。
请不要先按文件名或题名分组，先做 PDF 轻量抽取：
1. 先从每篇 PDF 抽题名页
2. 再优先抽摘要/内容提要/关键词
3. 再抽导言或“问题提出”
4. 再抽结论/结语/结束语
5. 基于这些内容做“最小阅读卡总表”
6. 再据此筛核心文献、画学术地图、找冲突

要求：
- 如果 PDF 抽取失败，要说明失败在哪一步
- 不要因为个别 PDF 乱码就退回纯题名分析
- 每条核心判断尽量标明来自摘要、导言还是结论
```

## 示例 8：中英文混合论文一起处理

```text
Please use literature-review-cartographer.

I have 24 papers on platform governance. Some are in English and some are in Chinese.
Do not split them by language. First extract each paper's abstract, introduction, and conclusion, then build a minimal reading-card table.
After that:
1. identify the core papers,
2. group them by shared assumptions and research questions,
3. find direct conflicts and interpretive tensions,
4. build concept lineages across both Chinese and English terms,
5. write the final review in Chinese.

Requirements:
- keep paper titles in the original language,
- keep evidence quotes in the original language,
- if a Chinese and an English paper use the same concept, show both terms together instead of treating them as different concepts.
```

## 示例 9：输出中文核心期刊风格脚注版短稿

```text
请使用 literature-review-cartographer。

下面这些论文我已经让你完成了材料盘点、学术地图、冲突矩阵和研究空白。
现在请继续做一步成稿：
1. 把前面的分析压缩成 800-1200 字的综述短稿
2. 改成更像中文核心期刊论文的语体
3. 在正文中使用上标序号脚注
4. 在正文后给出页下注释

要求：
- 只根据已经确认过的文献信息写脚注
- 不要编造卷期页码
- 如果页码没核实，就用保守格式
- 正文不要写成提纲，要像正式论文综述段落
```

## 示例 10：先做核心池评分表再缩池

```text
请使用 literature-review-cartographer。

我给你一批论文，请不要直接拍脑袋决定哪些是核心文献。
请先按最小阅读卡读取摘要、导言和结论，然后输出一个“核心池评分表”，至少包含：
- 代表性
- 分歧性
- 枢纽性
- 方法独特性
- 重复度

再根据评分表：
1. 判断哪些论文进入核心池
2. 哪些论文作为补充保留
3. 哪些论文暂缓纳入

要求：
- 不要只给总分，要说明每篇论文为什么这样判
- 核心池规模由文献内容决定，不预设固定篇数
```

## 示例 11：评分后补学术化解释句

```text
请使用 literature-review-cartographer。

在输出核心池评分表之后，请不要只写“高 / 中 / 低”。
请为每篇候选论文补 1-2 句学术化解释，说明：
- 为什么它代表性高或低
- 为什么它处于主要分歧线之中或之外
- 为什么它具有或不具有枢纽作用
- 为什么它的方法独特性明显或有限
- 为什么它与已有文献重复度高或不高

要求：
- 解释句保持正式学术语体
- 不要写口语化判断
- 不要只说“很重要”或“比较一般”，要说明依据
```

## 三种 CLI 的调用建议

### Codex

```text
Use literature-review-cartographer. Start with a corpus audit, then follow the output contract module by module.
```

### Claude Code

```text
Please use the literature-review-cartographer skill. Work only from the papers I provide and mark any unsupported claim explicitly.
```

### Gemini CLI

```text
Use the literature-review-cartographer skill and keep the output structured. If the evidence is partial, downgrade the certainty instead of guessing.
```
