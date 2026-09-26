# 来源标签与PDF定位修正：2026-09-26

本轮针对当前词句库的212篇来源论文，不是279篇全部登记记录的重新精读，也不是新的来源复核验收。原始阅读状态、精读日期、补充材料状态、期刊归属和13篇STK11 highlight均不因补标签/查页码而升级。

## 已修正

- 在原有39篇细标签记录之外，依据现有逐篇精读笔记/证据表及部分疑点的PDF文本检查，为其余173篇整理来源疾病、模型、用途等标签。依据文件与行号保存在[source-scope-backfill.json](source-scope-backfill.json)。这不是仅凭标题自动打标签，也不是173篇重新阅读全文。
- 212篇均有疾病、模型、用途标签；164篇有明确组织/标本标签，48篇该字段仍未细化。所有非空标签均为“已识别、非穷尽”，空值为“未整理、不能据此认定不存在”。当前字段覆盖见[source-provenance-summary.json](source-provenance-summary.json)，待补篇目见[source-scope-pending.csv](source-scope-pending.csv)。
- 标签同时进入总目录CSV和词句检索。论文级多标签不证明各个组织、瘤种、组学技术来自同一子队列。保留混合队列边界：例如甲状腺癌肺转移不归为原发NSCLC，LCMV感染小鼠不归为肺癌模型，重新鉴定的SMARCA4缺陷肿瘤不因旧名而归为真实SCLC。
- 重新打开212份与版本登记SHA-256相符的本地PDF，建立文件名、哈希、版本与物理页数关联。词句的原文页码只来自该具体文件的规范化字面匹配，不从笔记行号或印刷页码猜填。
- 将词汇/搭配、改写句式/段落模板分开。合成模板没有必须存在的逐字原文，不应为了“补全页码”制造引用。

## 页码状态与保留事项

修正时6755条词句中：563条在登记PDF文本中找到字面匹配；2784条常规词汇/搭配未取得字面匹配，需进一步上下文核查；3408条为合成句式/段落等，不作为原文引用。另有2942条带旧笔记页码提示，与上述类别交叉，不能相加。这些提示保留原数字，但页码体系尚未确认，不自动当作PDF物理页。

未匹配可能源于归纳措辞、词形/断行差异或PDF抽取问题，不等同于“没读过”“没提供PDF”或“原文肯定没有”。自动排除参考文献依赖文本标题识别，不能替代看原页；机械命中也不代表该词适用于原索引标注的每一论文段落。所有引用、数值结论仍需回看原页上下文。当前队列见[source-locator-pending.csv](source-locator-pending.csv)；机器定位见[source-pdf-locators.json](source-pdf-locators.json)。

## 有界图像抽查

本次同一助手另查看了以下3张原PDF整页渲染图，仅核对短语存在及所在小节，不是独立审查、全文复读或整批逐字验收。自动匹配记录仍按机械检查记载，不以这3个抽查推及其余条目。

| PMID | 检索ID | 字面短语 | PDF物理页 | 图像检查范围 |
|---|---|---|---:|---|
| 37097610 | ccr-lang-ad922ea5b1ddb2f6827b | putative loss of heterozygosity | 5 | Determination of ATM mutation status段落中跨行可见；不是旧笔记p4自动换算 |
| 37733794 | ccr-lang-5830b2260d2e4966eb1c | reverse-phase protein array | 2 | Materials and Methods下TCGA段落可见；印刷页4959不当作物理页 |
| 39864548 | jto-lang-43ecce2662bdf4f9b88e | paired genomic and transcriptomic data | 4 | 基因型与mRNA表达相关性小节可见；印刷页728不当作物理页 |

本轮不宣称所有历史细标签或每条原PDF引文定位全部补齐。`original_wording_verified`、`original_pdf_location_verified`和`quotation_verified`未被整体升级；原文定位、科学含义核查、阅读完成和来源验收是不同层次。
