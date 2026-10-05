# PMID 40882030: TNG260 / CoREST 与 STK11 免疫增敏

## 身份、版本与实际阅读范围

- Ahronian LG et al. **TNG260 Is a Small-Molecule CoREST Inhibitor That Sensitizes STK11-Mutant Tumors to Anti-PD-1 Immunotherapy**. Cancer Research. 2025;85(20):3966-3982. DOI: [10.1158/0008-5472.CAN-25-0998](https://doi.org/10.1158/0008-5472.CAN-25-0998); [PMID 40882030](https://pubmed.ncbi.nlm.nih.gov/40882030/). 首次在线 2025-08-29，期刊日期 2025-10-15。
- 供稿版本：publisher_typeset_pdf，原文件 `can-25-0998.pdf`，17 个物理页；SHA-256 `fffdafba514680dd2e3f7c27fb685146ec1e62e5535bd83eee5d9968693bca32`。
- 阅读者：Codex /root，2026-10-02；主文、Figure 1-5 及全部图注已读，主图逐图视觉核查；非科学附录为披露、贡献、致谢和参考文献。外部 Supplementary Methods/Figures S1-S9/Tables S1-S6 未提供，正文对它们的描述不等于补充文件已读。
- `reading_stage=main_text_deep_read_complete`; `review_status=not_reviewed`; `supplement_status=not_supplied`。本记录是首次阅读，不是独立六门复核。
- PDF首页栏目为 Therapeutic Development and Chemical Biology；此为稿件所示标签，未单独验证出版商网页栏目。

## 研究问题与论证链

问题：能否发现依赖适应性免疫、而非单纯杀伤肿瘤细胞的靶点，以解除 STK11 缺失造成的 PD-1 阻断不敏感？从 MC38 等基因背景 CRISPR 筛选获得 HDAC1，研发具有 CoREST 复合物选择性的 TNG260，再以生化、细胞、移植瘤、自发肺瘤和患者配对活检建立转化证据链。

1. MC38 的 STK11 knockout 改变免疫环境及 anti-PD-1 反应；MC38/CT26 是小鼠结直肠肿瘤，不能直接叫肺癌模型。
2. 体内 sgRNA 筛选在免疫完整、裸鼠、anti-PD-1 条件间对照，寻找免疫依赖性靶点；HDAC1 为候选，不等同 CoREST 所有成员均获遗传验证。
3. TNG260 对重组 HDAC1/2、细胞内结合和免疫沉淀复合物的抑制分别测定；HDAC2 共晶结构并不等于 HDAC1 共晶。
4. 药物联合在 STK11-null MC38/CT26、KL 移植瘤及 KL GEMM 中有效；裸鼠和 KP 对照为重要阴性证据。
5. KL/KP RNA-seq 与 H3K9ac ChIP-seq 整合支持染色质乙酰化与免疫相关转录改变；不是 ATAC-seq，也不是单细胞测序。
6. NCT05887492 配对活检显示靶点作用和免疫表型变化。本篇没有提供足以证明患者 ORR/PFS/OS 获益或安全性优势的临床结果。

## 章节与主图覆盖

| 内容 | 物理页 | 核查内容 |
|---|---|---|
| Abstract / Significance / Introduction | 1-2 | 未满足临床需求、发现路径、患者药效学而非疗效；无独立 Translational Relevance |
| Materials and Methods | 2-5 | 细胞鉴定、CRISPR、NanoBRET、复合物、生化测定、RNA/ChIP、动物、统计、流式和患者活检 |
| Results | 5-14 | 筛选、选择性、免疫依赖、肺模型、转录机制及患者活检 |
| Figure 1 | 6 | MC38 N=8/组；筛选体外 n=3、裸鼠 n=15、免疫组各 n=15；FDR 比较 |
| Figure 2 | 7 | 结构、重组酶与细胞 IC50、WB、四复合物抑制热图；生化/细胞实验 N=2 |
| Figure 3 / 跨页图注 | 9-10 | PK/PD、个体曲线、MC38/CT26 生存、再挑战、裸鼠阴性 |
| Figure 4 / 跨页图注 | 11-12 | KL/KP/GEMM、生物学重复和 ChIP/RNA 整合；k 数目矛盾见下 |
| Figure 5 | 14 | 各剂量前后活检、H4K5ac、PD-L1、T细胞、50 μm 标尺 |
| Discussion / closing synthesis / Limitations | 13-15 | 外推边界、KEAP1 WT、模型产生方式、机制未完全解析；无独立 Conclusion 标题 |
| Data availability / administrative / references | 15-17 | GEO/PDB、产业利益披露和资助；不当作新增实验 |

## 中心结果和分母

| 证据 | 数值与比较 | 定位与限制 |
|---|---|---|
| 筛选规模 | 3,176 targeting sgRNAs / 794 genes，加400 non-targeting guides；135 essential、12 tumor suppressor、13 immune-response、634 druggable genes | p5；FDR-adjusted P，不能称全基因组筛选 |
| 重组酶 | HDAC1/2/3 图示 IC50 分别0.005/0.03/1.2 μmol/L | Fig2D p7；正文230/37倍来自未舍入值，勿用图中圆整数重算并替代 |
| 细胞内结合 | HDAC1 0.10、HDAC2 0.17、HDAC3 1.07 μmol/L | Fig2F；与重组酶测定分开 |
| 复合物选择性 | CoREST 0.17 μmol/L；NCoR/NuRD/Sin3均>100 | Fig2G；不是临床选择性/安全性已证实 |
| MC38_sgStk11 联合 | N=8/组，5个完全消退；ORR75% vs anti-PD-1 0%；第11天 TGI83%，对 vehicle P<.001 | pp8-10/Fig3D；鼠ORR定义为部分+完全消退，非患者 RECIST |
| MC38生存 | 联合观察期>35天100%存活；anti-PD-1/TNG260/vehicle 中位23/17/13天；Fig3E联合对anti-PD-1 P=.0002 | p8与Fig3E；有限观察期不是治愈率或长期OS |
| CT26 | 联合生存87.5%，anti-PD-1中位13天；Fig3F P=.001 | 正文写P<.001，与图的精确显示不同，引用时保留定位；ORR88%来自正文所引未供S4 |
| 免疫记忆/阴性 | 5只MC38完全消退鼠停药21天后再挑战均拒瘤；naive N=8。裸鼠N=8/组无药效 | Fig3H-J；非所有肿瘤/人类免疫记忆 |
| 肺癌模型 | KL N=15-20/组，第24天约5.5倍肿瘤体积差；KP N=5/组无生长抑制；KL GEMM N=8-10/组肿瘤负荷停滞 | Fig4A-C/pp10-12；KP与KL还涉及TP53背景差异，非完美单一基因同源对照 |
| RNA/ChIP | 1 μmol/L、7天；细胞ChIP N=2；体内ChIP N=3-5/组 | Fig4；H3K9ac信号延伸不等于直接ATAC可及性测量 |
| 患者药效学 | 文中记录10份两周期后的活检与治疗前比较；80/120mg组6人中 helper T升高4/6、cytotoxic T升高6/6；40mg未诱导相同药效标志 | p13/Fig5；不同检测可评估分母不强行统一；缺S6，不补造癌种/疗效/毒性分母 |
| 选择性/耐受性 | 预临床暴露窗口约11倍；同药效剂量造血祖细胞直接毒性较低 | pp8,10；不能叫“临床安全性优于vorinostat” |

补充图相关结果只在主文报告层面读取：MC38第7天未见明显总T细胞富集但Treg降低；人活检Treg未明显改变。不同物种/时间点不合并。vorinostat对照的87.5% ORR与Fig3的75%来自不同实验，不是可替换值。

## 原文疑点与禁止迁移

- p4 Animal studies 实际排印为 anti-PD-1 **200 mg**，与常用量级及别段 mg/kg 给法不可直接换算。保留原文疑似单位错误；本笔记不擅自改成 μg，不作为可执行给药方案。
- p3 ChIP分析写 k=6；Fig4E图注/图像7簇；Fig4I图注同时写 seven groups 与 k=6。可说明分簇分析，禁止用本页重建确定的k参数。
- p15结尾用 histone methylation，而患者方法/结果/Fig5测的是H4K5 acetylation；科学总结使用实际测量的乙酰化，明确原文用词冲突，不传播甲基化疗效说法。
- p8 CCL22相关段末出现CCL2字样，未供S4H不能补判为另一基因实验。
- 所用小鼠模型均KEAP1 WT（p14）；不能宣称TNG260已克服STK11/KEAP1双缺失耐药。
- 临床联合给药无单药/随机对照；剂量和前后活检关联不能完全分离pembrolizumab贡献；6/6 CD8变化不是100%患者缓解率。

## STK11多轴分类及写作使用

- 关系：`direct_function`，兼有STK11-selected临床药效学，不是验证性疗效预测。
- 设计：experimental-mechanistic + phase-I/II exploratory pharmacodynamics。
- 技术：original pooled_in_vivo_crispr；bulk_rna（KL/KP细胞）；chip_seq（H3K9ac，细胞/小鼠肿瘤）；targeted_rna（NanoString）；interactome_ptm_ms（A549乙酰化肽富集）；targeted_protein（患者H4K5质谱、IHC、WB、ELISA）；spatial_protein（患者mIF）；flow_cytometry、crystallography。
- 治疗：TNG260/CoREST、anti-PD-1、pembrolizumab；vorinostat/entinostat/tucidinostat/domatinostat为各自实验对照，不能统作临床随机臂。
- 适用模块：immune_mechanism、epigenetic_state、therapeutic_vulnerability、early_pharmacodynamics。
- 最强稳妥结论：CoREST抑制在特定STK11缺失模型中产生免疫依赖性增敏，早期患者活检提供靶点作用线索；临床获益与合并KEAP1改变的影响仍待验证。

## Section-language: 词汇、搭配与合成句架

以下短术语可复用；含方括号的句架和段落逻辑是重新抽象的模板，不是原文引文。定位是支持概念的物理页，不表示逐字出现。

| ID | Section | Unit | Expression / frame | 功能、使用限制与定位 |
|---|---|---|---|---|
| TNG01 | Abstract | vocabulary | immune sensitization | 免疫增敏；必须注明model/patient层级，p1 |
| TNG02 | Abstract | sentence-frame | In [model], [combination] altered [immune feature] and reduced [tumor endpoint]; clinical efficacy remains to be established. | 摘要结果和结论分层，pp1,8-14 |
| TNG03 | Introduction | collocation | tumor-cell-intrinsic immune evasion | 肿瘤细胞内在免疫逃逸，非仅bulk相关，pp1-2 |
| TNG04 | Introduction | paragraph-frame | Define [resistant subgroup]; identify [mechanistic gap]; justify [immune-dependent target-discovery strategy]. | 从未满足需求到可检验问题，不宣称全部患者抵抗，pp1-2 |
| TNG05 | Materials and Methods | vocabulary | isogenic knockout model | 等基因敲除对照；KL/KP不是只差STK11，pp2,5 |
| TNG06 | Materials and Methods | collocation | FDR-adjusted guide depletion | 区分guide与gene及FDR，pp2,5-6 |
| TNG07 | Materials and Methods | sentence-frame | [Complexes] were isolated from [cells] and profiled across [concentrations] using [activity assay]. | 不能写成细胞靶点占有率，p3 |
| TNG08 | Materials and Methods | vocabulary | paired pretreatment and on-treatment biopsies | 按可评估患者/检测分母报告，pp4-5,13 |
| TNG09 | Results | collocation | complex-selective deacetylase inhibition | 复合物选择性，不是HDAC1绝对专一，pp7-8/Fig2 |
| TNG10 | Results | sentence-frame | Activity was observed in [immune-intact model] but not in [immune-deficient comparator], supporting an immune-dependent component. | 阴性不等于排除全部非免疫作用，Fig3I-J |
| TNG11 | Results | collocation | increased intratumoral T-cell density | 用cells/mm2而非患者缓解率，p14/Fig5 |
| TNG12 | Results | sentence-frame | Among [n] evaluable paired specimens, [marker] increased in [x]; this was a pharmacodynamic analysis. | 占位分母必须真实，p13 |
| TNG13 | Figure legend | sentence-frame | Lines connect matched [baseline] and [on-treatment] measurements; [symbol] denotes [specified test]. | 不把剂量组当独立随机比较，Fig5 |
| TNG14 | Discussion | collocation | preclinical therapeutic window | 仅给定暴露/模型，不转患者安全性，pp8,10 |
| TNG15 | Discussion | sentence-frame | Although [target engagement] was demonstrated, the contribution of [individual component] cannot be isolated in this combination dataset. | 临床无单药对照，pp13-15 |
| TNG16 | Discussion | paragraph-frame | Link [screen hit] to [orthogonal pharmacology], integrate [mechanistic assays], then delimit [model genotype] and [clinical uncertainty]. | 避免从生物标志物跳到临床获益，pp13-15 |
| TNG17 | Conclusion | sentence-frame | These findings support evaluation of [strategy] in [defined population], without establishing comparative clinical benefit. | closing synthesis转化上限，pp14-15 |

安全迁移示例（合成）：`In the supplied mouse experiments, the combination reduced tumor growth, whereas the patient biopsy data showed pharmacodynamic changes rather than an established survival benefit.` 禁止迁移：`TNG260 improves survival in patients with STK11/KEAP1-mutant NSCLC.`
