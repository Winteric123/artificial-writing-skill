# PMID 32312757 语言资产

以下表达来自对本文论证功能的抽象，不是可直接大段复制的原句。定位均按 PDF 物理页。

## Section-aware vocabulary and collocations

| 表达 | 适用部分 | 功能 | 来源锚点 | 安全迁移 |
|---|---|---|---|---|
| `observational real-world cohort` | Methods/Discussion | 准确标示非随机证据层级 | p1–2 | 可用于真实世界回顾性队列；不可省略 observational 后暗示试验性比较 |
| `clinico-genomic database` | Methods | 概括临床资料与肿瘤测序链接 | p2 | 仅在确有临床—基因组数据链接时使用 |
| `treatment-by-biomarker interaction` | Methods/Results | 区分预测性检验与单纯分层 HR | p2、p4–5 | 仅在模型明确含交互项时使用 |
| `no observable treatment interaction` | Results/Discussion | 报告交互阴性而不声称等效 | p4–5 | 同时报告效应量、CI 与 p 值；避免写成 “no predictive effect” |
| `adverse prognostic association` | Discussion | 把跨治疗不良关联校准为预后性 | p4–5 | 适用于观察性关联；不能替代因果表述 |
| `co-occurring alterations` | Results | 描述同一肿瘤内两个基因共同变异 | p3–5 | 不可自动推导协同作用 |

## Synthetic sentence frames

- Results：`[Biomarker] alterations were associated with poorer [endpoint] across treatment classes, whereas the biomarker-by-treatment interaction was not statistically supported.`
- Results：`The interaction estimate was [HR] (95% CI [x–y]; p=[p]), providing no detectable evidence of differential relative benefit in this dataset.`
- Discussion：`Taken together, the cross-regimen pattern is more consistent with a prognostic association than with treatment-specific prediction.`
- Limitation：`Because treatment allocation was non-random, residual confounding may have influenced both regimen selection and outcome.`
- Claim ceiling：`A non-significant interaction should not be interpreted as proof of equivalence or as exclusion of a modest effect modifier.`

## Paragraph logic

可复用的结果段落顺序：先报告各基因频率与共变异；再说明突变组和野生型组的基线失衡；随后给出各治疗内结局关联；最后以正式交互项回答“是否预测相对治疗获益”。这种顺序可避免把“某亚组 HR 显著、另一亚组不显著”误写成亚组间差异。

可复用的讨论段落顺序：先陈述跨治疗一致的不良方向；再给出交互阴性；据此将解释限制为预后相关；最后加入非随机治疗、交互效能和真实世界端点局限。

## Unsafe transfer

- 不要写 `STK11 predicts resistance to PD-(L)1 blockade`：本文没有验证治疗特异性预测作用。
- 不要把 `STK11 and/or KEAP1` 并集结果改写为 `STK11` 单基因结果。
- 不要把 `p>0.05` 改写成两种治疗等效。
- 不要忽略 Figure 2 勘误版本，也不要把未提供的在线补充材料写成已审阅。

## Indexed language units

- `frequency and baseline imbalance → within-regimen associations → formal interaction → calibrated prognostic interpretation`
