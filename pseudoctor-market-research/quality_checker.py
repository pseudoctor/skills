#!/usr/bin/env python3
"""
Quality Checker for Market Research Reports - 报告质量自动检查器

功能：
1. 页数检查
2. 表格数量检查
3. 数据点密度检查
4. 来源引用检查
5. 置信度标注检查
6. 章节完整性检查

使用：
    from quality_checker import ReportQualityChecker

    checker = ReportQualityChecker("report.md")
    report = checker.check_all()
    print(report)
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, field


@dataclass
class QualityIssue:
    """质量问题"""
    severity: str  # 'critical', 'warning', 'info'
    category: str  # 'page_count', 'tables', 'data_points', 'sources', 'confidence'
    message: str
    location: str = ""  # 问题位置，如"第二章 2.1.3节"

    def __str__(self):
        emoji = {
            'critical': '❌',
            'warning': '⚠️',
            'info': 'ℹ️'
        }
        return f"{emoji.get(self.severity, '')} {self.message}"


@dataclass
class QualityReport:
    """质量检查报告"""
    total_issues: int = 0
    critical_issues: List[QualityIssue] = field(default_factory=list)
    warnings: List[QualityIssue] = field(default_factory=list)
    info: List[QualityIssue] = field(default_factory=list)

    passed: bool = False
    grade: str = "N/A"
    summary: str = ""

    def add_issue(self, issue: QualityIssue):
        """添加问题"""
        self.total_issues += 1
        if issue.severity == 'critical':
            self.critical_issues.append(issue)
        elif issue.severity == 'warning':
            self.warnings.append(issue)
        else:
            self.info.append(issue)


class ReportQualityChecker:
    """报告质量检查器"""

    def __init__(self, report_path: str):
        """
        初始化检查器

        Args:
            report_path: 报告文件路径（Markdown/Word）
        """
        self.report_path = Path(report_path)

        if not self.report_path.exists():
            raise FileNotFoundError(f"报告文件不存在: {report_path}")

        self.content = ""
        self._load_content()

        # 质量标准
        self.standards = {
            'min_pages': 50,
            'min_tables': 35,
            'min_data_points': 200,
            'min_data_density': 4.0,  # 每页最少数据点
            'require_sources': True,
            'require_confidence': True,
        }

        # 检查结果
        self.metrics = {}
        self.issues = []

    def _load_content(self):
        """加载报告内容"""
        suffix = self.report_path.suffix.lower()

        if suffix == '.md':
            with open(self.report_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
        elif suffix in ['.docx', '.doc']:
            try:
                from docx import Document
                doc = Document(str(self.report_path))
                self.content = "\n".join([p.text for p in doc.paragraphs])
            except ImportError:
                raise ImportError("需要安装python-docx库: pip install python-docx")
        else:
            raise ValueError(f"不支持的文件格式: {suffix}")

    def check_all(self) -> QualityReport:
        """
        执行所有检查

        Returns:
            QualityReport对象
        """
        report = QualityReport()

        # 1. 页数检查
        self._check_page_count(report)

        # 2. 表格检查
        self._check_tables(report)

        # 3. 数据点检查
        self._check_data_points(report)

        # 4. 来源引用检查
        self._check_sources(report)

        # 5. 置信度检查
        self._check_confidence(report)

        # 6. 章节完整性检查
        self._check_chapters(report)

        # 计算总体评级
        self._calculate_grade(report)

        # 生成摘要
        self._generate_summary(report)

        return report

    def _check_page_count(self, report: QualityReport):
        """检查页数"""
        # 估算页数（简化方法：按字数估算）
        # 中文约2000字/页，英文约500词/页
        char_count = len(self.content)

        # 检测语言
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', self.content))
        if chinese_chars > char_count * 0.3:
            # 中文为主
            estimated_pages = char_count / 2000
        else:
            # 英文为主
            word_count = len(self.content.split())
            estimated_pages = word_count / 500

        estimated_pages = int(estimated_pages)
        self.metrics['page_count'] = estimated_pages

        if estimated_pages < self.standards['min_pages']:
            report.add_issue(QualityIssue(
                severity='critical',
                category='page_count',
                message=f"页数不足：{estimated_pages}页 < {self.standards['min_pages']}页",
                location=f"全文（约{estimated_pages}页）"
            ))
        else:
            report.info.append(QualityIssue(
                severity='info',
                category='page_count',
                message=f"页数通过：{estimated_pages}页（目标≥{self.standards['min_pages']}页）"
            ))

    def _check_tables(self, report: QualityReport):
        """检查表格数量"""
        # Markdown表格：以|开头和结尾的行
        tables = re.findall(
            r'^\|.*\|$\n^\|[-:\s|]+\|$\n(^\|.*\|$\n?)+',
            self.content,
            re.MULTILINE
        )

        table_count = len(tables)
        self.metrics['table_count'] = table_count

        if table_count < self.standards['min_tables']:
            report.add_issue(QualityIssue(
                severity='critical',
                category='tables',
                message=f"表格不足：{table_count}个 < {self.standards['min_tables']}个",
                location=f"全文（共{table_count}个表格）"
            ))
        else:
            report.info.append(QualityIssue(
                severity='info',
                category='tables',
                message=f"表格数量通过：{table_count}个（目标≥{self.standards['min_tables']}个）"
            ))

        # 检查每章表格数
        chapters = re.split(r'^#+\s+', self.content, flags=re.MULTILINE)
        chapter_tables = []

        for i, chapter in enumerate(chapters[1:], 1):  # 跳过空开头
            if not chapter.strip():
                continue
            chapter_table_count = len(re.findall(r'^\|.*\|$', chapter, re.MULTILINE))
            chapter_tables.append((i, chapter_table_count))

            if chapter_table_count < 4:  # 每章至少4个表格
                report.add_issue(QualityIssue(
                    severity='warning',
                    category='tables',
                    message=f"第{i}章表格不足：{chapter_table_count}个 < 4个",
                    location=f"第{i}章"
                ))

    def _check_data_points(self, report: QualityReport):
        """检查数据点数量"""
        # 数据点模式
        patterns = [
            r'\d+\.\d+[亿元万千百十]',  # 金额
            r'\d+\.?\d*%',  # 百分比
            r'20[12]\d年?',  # 年份
            r'\d{4}年?',  # 四位数年份
            r'[第]\d+[章节条]',  # 序号
            r'TAM|SAM|SOM',  # 市场层级
        ]

        total_matches = 0
        for pattern in patterns:
            matches = re.findall(pattern, self.content)
            total_matches += len(matches)

        # 去重估算
        data_points = min(total_matches, len(self.content) // 50)
        self.metrics['data_points'] = data_points

        # 计算密度
        page_count = self.metrics.get('page_count', 1)
        data_density = data_points / page_count if page_count > 0 else 0
        self.metrics['data_density'] = data_density

        # 检查总数
        if data_points < self.standards['min_data_points']:
            report.add_issue(QualityIssue(
                severity='critical',
                category='data_points',
                message=f"数据点不足：{data_points}个 < {self.standards['min_data_points']}个",
                location=f"全文（共{data_points}个数据点）"
            ))
        else:
            report.info.append(QualityIssue(
                severity='info',
                category='data_points',
                message=f"数据点数量通过：{data_points}个（目标≥{self.standards['min_data_points']}个）"
            ))

        # 检查密度
        if data_density < self.standards['min_data_density']:
            report.add_issue(QualityIssue(
                severity='warning',
                category='data_points',
                message=f"数据密度不足：{data_density:.1f}个/页 < {self.standards['min_data_density']}个/页",
                location=f"全文（平均{data_density:.1f}个/页）"
            ))
        else:
            report.info.append(QualityIssue(
                severity='info',
                category='data_points',
                message=f"数据密度通过：{data_density:.1f}个/页（目标≥{self.standards['min_data_density']}个/页）"
            ))

    def _check_sources(self, report: QualityReport):
        """检查来源引用"""
        # 来源引用模式
        source_patterns = [
            r'来源[:：]\s*[^。\n]+',
            r'\[来源[:：][^\]]+\]',
            r'数据来源[:：]\s*[^。\n]+',
            r'据[^\n]{2,10}?(报道|统计|数据)',
        ]

        total_sources = 0
        for pattern in source_patterns:
            matches = re.findall(pattern, self.content)
            total_sources += len(matches)

        # 检测数字后的来源（简化）
        number_with_source = len(re.findall(
            r'\d+[\.\d%]*[^\n]{0,50}(来源|Source|据)',
            self.content
        ))

        self.metrics['source_count'] = total_sources + number_with_source

        # 检查是否所有数据都有来源（抽样检查）
        # 查找没有来源的数据
        data_without_source = len(re.findall(
            r'(?<!来源)(?<!据)(?<!Source)\d+\.\d+[亿元万千百%]+(?!\s*(来源|Source|据))',
            self.content
        ))

        if data_without_source > 100:  # 阈值
            report.add_issue(QualityIssue(
                severity='warning',
                category='sources',
                message=f"发现{data_without_source}处数据可能缺少来源标注",
                location="全文"
            ))
        else:
            report.info.append(QualityIssue(
                severity='info',
                category='sources',
                message=f"来源引用检查通过：发现{self.metrics['source_count']}处来源标注"
            ))

        # 检查单一来源问题
        sources_text = re.findall(r'(来源|数据来源)[：:]\s*([^\n]+)', self.content)
        source_counts = {}
        for _, source in sources_text:
            source = source.strip()[:30]  # 取前30字符
            source_counts[source] = source_counts.get(source, 0) + 1

        # 检查过度依赖单一来源
        if source_counts:
            max_count = max(source_counts.values())
            max_source = max(source_counts, key=source_counts.get)
            if max_count > 50:  # 单一来源超过50次
                report.add_issue(QualityIssue(
                    severity='warning',
                    category='sources',
                    message=f"过度依赖单一来源：'{max_source}'使用{max_count}次，建议交叉验证",
                    location="全文"
                ))

    def _check_confidence(self, report: QualityReport):
        """检查置信度标注"""
        # 置信度模式
        confidence_patterns = [
            r'置信度[:：]\s*\d+%',
            r'置信度[:：]\s*[高中低]',
            r'\[置信度[:：][^\]]+\]',
        ]

        total_confidence = 0
        for pattern in confidence_patterns:
            matches = re.findall(pattern, self.content)
            total_confidence += len(matches)

        self.metrics['confidence_count'] = total_confidence

        # 检查预测数据是否有置信度
        # 查找预测相关的关键词附近的置信度
        prediction_keywords = ['预测', '预计', ' forecast', 'E$', '2030', '2029', '2028', '2027', '2026', '2025']
        prediction_contexts = []

        for keyword in prediction_keywords:
            matches = re.finditer(
                rf'.{{0,50}}{re.escape(keyword)}.{{0,50}}',
                self.content
            )
            for match in matches:
                context = match.group()
                prediction_contexts.append(context)

        # 检查这些上下文是否有置信度
        predictions_without_confidence = 0
        for context in prediction_contexts:
            has_confidence = any(
                re.search(pattern, context)
                for pattern in confidence_patterns
            )
            if not has_confidence:
                predictions_without_confidence += 1

        if predictions_without_confidence > 20:
            report.add_issue(QualityIssue(
                severity='warning',
                category='confidence',
                message=f"预测数据中{predictions_without_confidence}处未标注置信度",
                location="预测相关章节"
            ))

        if total_confidence == 0:
            report.add_issue(QualityIssue(
                severity='warning',
                category='confidence',
                message="未发现置信度标注，建议为预测数据添加置信度",
                location="全文"
            ))
        else:
            report.info.append(QualityIssue(
                severity='info',
                category='confidence',
                message=f"置信度标注：{total_confidence}处"
            ))

    def _check_chapters(self, report: QualityReport):
        """检查章节完整性"""
        # 必需章节
        required_chapters = [
            '执行摘要',
            '核心产品',
            '市场宏观',
            '消费者洞察',
            '销售渠道',
            '分销体系',
            '发展趋势',
            '战略建议',
            '投资研究',
            '投资建议',
        ]

        missing_chapters = []
        for chapter in required_chapters:
            if chapter not in self.content:
                missing_chapters.append(chapter)

        if missing_chapters:
            report.add_issue(QualityIssue(
                severity='critical',
                category='chapters',
                message=f"缺少必需章节：{', '.join(missing_chapters)}",
                location="目录"
            ))
        else:
            report.info.append(QualityIssue(
                severity='info',
                category='chapters',
                message="章节完整性检查通过：所有必需章节存在"
            ))

        # 检查执行摘要元素
        if '执行摘要' in self.content:
            # 提取执行摘要部分
            es_match = re.search(
                r'#+\s*执行摘要.*?(?=#+\s+\w+|$)',
                self.content,
                re.DOTALL
            )
            if es_match:
                es_content = es_match.group()

                # 检查必需元素
                required_elements = {
                    '市场快照': ['市场快照', '关键指标'],
                    '核心发现': ['核心发现', '主要发现'],
                    '战略建议': ['战略建议', '建议'],
                }

                for element_name, keywords in required_elements.items():
                    if not any(kw in es_content for kw in keywords):
                        report.add_issue(QualityIssue(
                            severity='warning',
                            category='chapters',
                            message=f"执行摘要缺少'{element_name}'部分",
                            location="执行摘要"
                        ))

    def _calculate_grade(self, report: QualityReport):
        """计算总体评级"""
        critical_count = len(report.critical_issues)
        warning_count = len(report.warnings)

        if critical_count == 0 and warning_count == 0:
            report.grade = "A+"
            report.passed = True
        elif critical_count == 0 and warning_count <= 2:
            report.grade = "A"
            report.passed = True
        elif critical_count == 0 and warning_count <= 5:
            report.grade = "B+"
            report.passed = True
        elif critical_count == 0:
            report.grade = "B"
            report.passed = True
        elif critical_count <= 2:
            report.grade = "C"
            report.passed = False
        else:
            report.grade = "D"
            report.passed = False

    def _generate_summary(self, report: QualityReport):
        """生成摘要"""
        summary_parts = []

        summary_parts.append(f"质量评级：{report.grade}")
        summary_parts.append(
            f"问题统计：{report.total_issues}个"
            f"（严重{len(report.critical_issues)}个/警告{len(report.warnings)}个）"
        )

        # 建议行动
        if report.passed:
            summary_parts.append("建议行动：质量合格，可交付使用")
        else:
            if report.critical_issues:
                summary_parts.append("建议行动：")
                for issue in report.critical_issues[:3]:
                    summary_parts.append(f"  - {issue.message}")
                if len(report.critical_issues) > 3:
                    summary_parts.append(f"  - 还有{len(report.critical_issues) - 3}个严重问题")

        report.summary = "\n".join(summary_parts)

    def generate_report_text(self) -> str:
        """
        生成文本格式的质量报告

        Returns:
            报告文本
        """
        report = self.check_all()

        lines = []
        lines.append("=" * 60)
        lines.append("🔍 市场研究报告质量检查报告")
        lines.append("=" * 60)
        lines.append("")

        # 总体评估
        lines.append("## 总体评估")
        grade_emoji = {
            'A+': '✅',
            'A': '✅',
            'B+': '✓',
            'B': '✓',
            'C': '⚠️',
            'D': '❌'
        }
        lines.append(f"{grade_emoji.get(report.grade, '')} 质量评级：{report.grade}")
        lines.append(f"是否通过：{'是' if report.passed else '否'}")
        lines.append("")
        lines.append(report.summary)
        lines.append("")

        # 指标统计
        lines.append("## 指标统计")
        lines.append(f"- 页数：{self.metrics.get('page_count', 'N/A')}页")
        lines.append(f"- 表格：{self.metrics.get('table_count', 'N/A')}个")
        lines.append(f"- 数据点：{self.metrics.get('data_points', 'N/A')}个")
        lines.append(f"- 数据密度：{self.metrics.get('data_density', 0):.1f}个/页")
        lines.append(f"- 来源标注：{self.metrics.get('source_count', 'N/A')}处")
        lines.append(f"- 置信度标注：{self.metrics.get('confidence_count', 'N/A')}处")
        lines.append("")

        # 详细问题
        if report.critical_issues:
            lines.append("## ❌ 严重问题")
            for i, issue in enumerate(report.critical_issues, 1):
                lines.append(f"{i}. {issue.message}")
                if issue.location:
                    lines.append(f"   位置：{issue.location}")
            lines.append("")

        if report.warnings:
            lines.append("## ⚠️ 警告")
            for i, issue in enumerate(report.warnings, 1):
                lines.append(f"{i}. {issue.message}")
                if issue.location:
                    lines.append(f"   位置：{issue.location}")
            lines.append("")

        if report.info:
            lines.append("## ✓ 通过项")
            for issue in report.info[:10]:  # 只显示前10个
                lines.append(f"- {issue.message}")
            if len(report.info) > 10:
                lines.append(f"- ... (还有{len(report.info) - 10}项)")
            lines.append("")

        lines.append("=" * 60)

        return "\n".join(lines)


def quick_check(report_path: str) -> str:
    """
    快速检查报告质量

    Args:
        report_path: 报告文件路径

    Returns:
        质量报告文本
    """
    try:
        checker = ReportQualityChecker(report_path)
        return checker.generate_report_text()
    except Exception as e:
        return f"❌ 检查失败: {str(e)}"


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("用法: python quality_checker.py <报告文件路径>")
        print("示例: python quality_checker.py market_report.md")
        sys.exit(1)

    report_path = sys.argv[1]
    report_text = quick_check(report_path)
    print(report_text)

    # 保存报告
    report_file = Path(report_path).parent / "质量检查报告.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report_text)

    print(f"\n✅ 质量报告已保存: {report_file}")
