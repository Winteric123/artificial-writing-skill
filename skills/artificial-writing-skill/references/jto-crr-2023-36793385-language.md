# PMID 36793385 语言资产

这些单元抽象自本文的写作功能，并非长句照录。页码为 PDF 物理页。

## Section-aware vocabulary and collocations

| 表达 | 适用部分 | 功能 | 来源锚点 | 安全迁移 |
|---|---|---|---|---|
| `retrospective exploratory biomarker analysis` | Methods/Discussion | 在随机试验背景中标明分析仍属探索性 | p2–4 | 不要因为母研究随机化就省略 exploratory |
| `biomarker-evaluable population` | Methods/Results | 区分全分析集与有可用组织/WES 的子集 | p3–4 | 必须同时给出分子与母队列的分母 |
| `prespecified cutpoint` | Methods | 描述事先确定的阈值 | p3–4 | 仅在阈值确实预设时使用；仍需报告连续分析 |
| `descriptive gene-level analysis` | Methods/Discussion | 限定单基因亚组的推断强度 | p3–4、p10–11 | 不得写成 confirmatory analysis |
| `no adjustment for multiplicity` | Methods/Discussion | 透明说明多重比较 | p3–4、p11 | 与名义 p 值和多个终点同时报告 |
| `clinical utility was not established` | Discussion/Conclusion | 比绝对“无效”更准确地总结阴性标志物研究 | p10–11 | 仅限当前治疗组合、样本与分析框架 |

## Synthetic sentence frames

- Methods：`The biomarker-evaluable population comprised [n/N] participants, of whom [n1] received [intervention] and [n2] received [control].`
- Results：`Treatment benefit was observed in both biomarker strata, although the estimate in the altered subgroup was imprecise because of the small sample size.`
- Results：`Continuous [biomarker] was not associated with [ORR/PFS/OS] in either treatment arm under the prespecified analysis.`
- Discussion：`Differences between subgroup-specific hazard ratios do not by themselves demonstrate effect modification in the absence of a formal interaction test.`
- Claim ceiling：`These exploratory findings do not establish the biomarker as a treatment-selection tool for [regimen].`

## Paragraph logic

适合生物标志物结果段的结构：先报告可评估比例与组内人数；再报告连续变量分析；随后报告预设阈值或基因分层的绝对反应率与 HR/CI；最后明确是否存在 formal interaction 与 multiplicity control。这样可以把“描述性异质性”与“已验证预测效应”分开。

讨论段可采用：母试验的随机化优势 → biomarker-evaluable subset 的选择与样本量限制 → 单基因结果的精度和多重性 → 对临床效用的保守结论。

## Unsafe transfer

- 不要用“一组显著、另一组不显著”推导 biomarker-by-treatment interaction。
- 不要把宽 CI 跨 1 写成治疗无效；应写效应估计不精确。
- 不要把 tTMB 的当前阴性结果外推到免疫单药、其他癌种或其他检测平台。
- 不要无警示地引用 Discussion 中与 Figure 4/Results 冲突的 KEAP1 OS HR。
- 不要把 `STK11` 与 `KEAP1` 合并成并集结论；本文的核心分析是分基因的。

## Indexed language units

- `evaluable fraction → continuous biomarker analysis → prespecified subgroup estimates → interaction and multiplicity caveats → clinical-utility ceiling`
