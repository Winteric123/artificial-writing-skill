# STK11文献：组学、治疗与设计分层

## 入口与状态

- [本批19篇阅读清单](stk11-2026-09-29-reading-manifest.csv)记录2026-09-29提供PDF的主文阅读、版本、补充材料范围和词句数。
- [逐篇细标签](stk11-assay-treatment-tags.json)记录稳定编号、真实期刊/年份/题名、STK11关系、研究方式、具体药物、检测技术、数据来源及样本上下文。依据链接进入逐篇阅读笔记，笔记含物理页码与高风险结果限制。
- [检索候选目录](stk11-reference-candidates.json)保存此前高影响文献检索的候选范围；候选不是全部已读。其旧摘要/题名筛选标签不能替代本批全文标签。
- 权威阅读状态从当前期刊quality/ledger和library-index读取；13篇用户核心highlight保持不变。新论文作为有依据的补充参考，不因影响因子或入库自动升级核心名单。

## 多轴分类，不建立互斥的单文件夹主题

实体PDF仅以真实期刊→年份→含PMID的文件名归档。同一篇可同时用于基因组学、免疫治疗和机制写作，主题标签不要求复制三份PDF。主分类是内容导航，不冒充CCR/JTO官网栏目。

1. STK11关系：direct_mutation（直接突变分析）、direct_function（LKB1功能机制）、contextual_analysis（伴随背景/他基因分析）、structural_analogue（方法或结构类比）。
2. 数据层：targeted_dna、wes、wgs、bulk_rna、targeted_rna、microarray、single_cell_rna、single_cell_atac、atac_seq、cut_and_tag、chip_seq、spatial_protein、targeted_protein、interactome_ptm_ms、tcr_sequencing等。保留方法名称，不能统称“多组学”后丢失区别。
3. 数据产生方式：original、reanalysis、mixed_new_and_previous；每个技术单独附sample_context，不把鼠来源scRNA转为患者scRNA，不把外部TCGA与患者临床队列写成配对多组学。
4. 研究方式：临床试验、临床相关、实验机制、计算方法可多选。IHC、mIF与磷酸化/细胞因子面板不是全蛋白组；mIF空间蛋白定位不是空间转录组；bulk去卷积不是单细胞测量。
5. 治疗：ICI单药/联合/围手术期、化疗、抗血管、EGFR/KRAS抑制剂、ATR/PARP抑制剂、STAT3 ASO及实验靶点，保留具体药物和临床/模型语境。treatment_covariates_not_efficacy是模型协变量，不是疗效验证。
6. 改变：跨基因序列共突变、同基因复合变异、CNA/LOH、融合、工程组合、功能失活分别记录。基因列表包含互斥及阴性比较，不保证每对都正共现。

## 如何用于STK11写作

| 任务模块 | 本批可用参考 | 使用边界 |
|---|---|---|
| 共突变零模型、负荷校正、跨队列复现 | PMID42432246；34450259；37121400 | SelectSim不证明协同机制；临床测序队列与病理阶段可能混杂；泛癌结论须分层 |
| 克隆性/LOH及突变与功能的区别 | PMID36526124；38177135 | 等位推断、蛋白表达、酶活和序列突变不是同一变量 |
| 免疫治疗临床结果 | PMID35190375；36709038；42587156；38351187 | 随机总体效应、事后亚组、非随机跨臂比较各自分开；不同P值不是交互作用 |
| 获得性耐药与纵向免疫表型 | PMID38207230；41690367 | 配对数量及检测分母各异；蛋白空间距离不是受体直接结合 |
| 基因型到机制实验 | PMID34230008；38402609；38177135 | CT26为小鼠结肠癌；KRAS G12C/G12D模型区分；假时序不是谱系示踪 |
| 基因组/转录组及计算结构类比 | PMID41345544；42749049；36535627；36948245；37806383；37981218 | SCLC/EGFR文章不自动成为STK11直接证据；C797X等位相位是同基因复合背景 |

特别联合阅读PMID34230008与38351187：前者提供STAT3相关实验依据，后者HUDSON的danvatirsen模块没有客观缓解；不能把机制合理性写成已验证患者获益。

## 检索示例

从skill根目录运行，使用AND组合不同维度；重复同类过滤也要求同时满足：

```powershell
python scripts/search_stk11_references.py --assay single_cell_rna --origin original
python scripts/search_stk11_references.py --treatment perioperative_ici
python scripts/search_stk11_references.py --relation direct_mutation --method computational-methods
python scripts/search_stk11_references.py --pmid 42432246 --json
python scripts/search_stk11_references.py --all-candidates --markdown
```

`--origin`与`--assay`必须匹配同一条技术记录；不是一篇论文有“原创IHC”和“再分析单细胞”就匹配“原创单细胞”。候选只有旧筛选主题，不具备逐技术全文标签时不匹配技术过滤。现阶段细标签覆盖本批19篇，其余候选的缺标签是待补，不是没有该技术。序列共突变更细的旧全库标签仍通过search_language的co-alteration过滤检索。

段落/语句在原期刊section catalog，使用search_language按Abstract/Introduction/Methods/Results/Discussion/Conclusion检索；该目录不复制语言条目，也不额外累加词句数。合成句架不是原文引文，PDF页码是支撑概念的阅读定位，不是所有词句逐字出现的证明。
