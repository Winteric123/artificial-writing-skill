# PMID 39637943 语言资产

以下为从文章论证功能中提炼的短语和合成句框，锚定本地 NIH author manuscript 的物理页。最终逐字引用需回到出版社 VOR。

## Section-aware vocabulary and collocations

| 表达 | 适用部分 | 功能 | 来源锚点 | 安全迁移 |
|---|---|---|---|---|
| `mucinous histologic component` | Methods | 定义组织学纳入特征 | p3–4 | 必须说明病理判定和 pure/features 规则 |
| `multi-institutional retrospective cohort` | Methods | 交代多中心观察性证据 | p3–5 | 不可暗示中央评审或统一检测，除非实际存在 |
| `analysis-specific denominator` | Methods/Results | 提醒每个分析集因缺失而不同 | p4–10、Table 1 | 每项结果都应给出相应 n，不能沿用总体分母 |
| `genomically enriched but not gene-defined` | Discussion | 区分组织学富集与单基因定义 | p5–12、Figure 2 | 不能从富集推导因果或充分性 |
| `immune-cell density by multiplex immunofluorescence` | Methods/Results | 准确描述免疫微环境测量 | p4、p7–8、Figure 3 | 需写组织区域、细胞标记和样本量 |
| `STK11/KEAP1/SMARCA4 alteration union` | Results | 标记并集而非单基因 | p8–10 | 每次解释都保留 union 标签，禁止归因给 STK11 单独 |

## Synthetic sentence frames

- Results：`Compared with nonmucinous tumors, tumors with a mucinous component were enriched for [alteration] but depleted for [alteration], alongside lower [genomic metric].`
- Results：`The adjusted association persisted for [endpoint] (HR [x], 95% CI [a–b]), although treatment selection remained non-random.`
- Results：`Response and survival estimates diverged within the small [histologic] subgroup, suggesting that ORR should not be used as a surrogate for overall prognosis in this analysis.`
- Discussion：`Enrichment of [gene] within a histologic subtype does not establish that the gene defines the subtype or mediates its treatment outcomes.`
- Claim ceiling：`Because the comparison lacked a randomized treatment interaction, the findings are associative rather than evidence of treatment-specific resistance.`

## Paragraph logic

组织学综合段落可按：队列定义与分母 → 分期内自然史 → 驱动/共变异谱 → mIF 免疫表型 → 分治疗队列的 ORR/PFS/OS → 多变量结果 → 病理、缺失、检测与选择偏倚。不要将不同治疗队列或不同分母拼成一个统一效应。

STK11 专题段落可按：先报告 Figure 2 的频率富集；再说明 pure/features 差异；随后把三基因 union 结果单独命名；最后明确缺乏 STK11 单基因治疗交互。这样既保留 STK11 证据，又不会把组织学或 union 效应错误归因于单基因。

## Unsafe transfer

- 不要把 `STK11/KEAP1/SMARCA4` union 简写成 “STK11-mutant”。
- 不要把组织学下的较差 ICI/chemoICI 结局称为已验证的治疗特异性耐药。
- 不要从 `STK11` 富集写成其导致黏液分化或免疫贫乏。
- 不要忽略 pure 亚组中 ORR 与 OS 的方向不一致。
- 不要把作者手稿的物理页当作最终出版社页码，也不要声称未提供的补充材料已精读。

## Indexed language units

- `The adjusted association persisted for [endpoint] (HR [x], 95% CI [a-b]), although treatment selection remained non-random.`
- `histology definition → stage-specific prognosis → genomic enrichment → immune phenotype → treatment-specific cohorts → adjustment and causal ceiling`
