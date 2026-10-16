# CCR full-text Methods and molecular Results sentence audit

Date: 2026-10-15. Scope: the 15 CCR articles in the unified 64-paper STK11 collection, using the registered supplied PDF versions. This rereading was performed by three delegated source-reading agents; each read the main narrative and inspected the reported visual pages. It is language-learning work, not a new independent six-gate acceptance review. Existing reading dates, article review states and supplement states remain separate.

## What was checked

The main narrative was reread to reconstruct the question, implemented analyses, molecular/experimental findings and their limitations. Selected Methods and Results sentences were inspected visually at their one-based physical PDF pages. Only whitespace, line-break hyphenation and typographic styling may be normalized in a source sentence. Main figure/table inspection scope is stated per paper below; it does not certify a full independent statistical reanalysis. Reference/administrative pages and unprovided supplementary material are distinguished from scientific reading.

The actual original sentence, registered PDF hash/version and page, content type, use scenario, synthetic rewrite template and transfer boundary are stored in [the sentence catalog](stk11-ccr-sentence-templates.json). [The writing guide](stk11-ccr-omics-methods-writing.md) provides paragraph structures. No source-specific number, software setting, gene or experimental claim is a default for the user's study.

## Per-paper rereading records

# CCR 正文重新学习记录：A 组

日期：2026-10-15。负责范围：5 篇、93 个物理页。基于任务 private-source-manifest.json 中登记的原 PDF 版本、SHA-256 和页数；未获取或阅读独立补充文件。本文记录本次同一代理正文重新阅读与视觉核句，不升级既有 review_status，也不代表独立科学复现、原始数据重分析或全部图表独立统计复核。

本批新增 31 条完整句来源记录：14 条 Methods、17 条非生存 Results。5 篇均至少 2 条 Methods 和 2 条 Results。原句只归一空白、断行连字符、字体连字及上下标；有语法问题的原句保留原措辞。模板由本次学习抽象合成，非作者原句。证据边界、研究背景、算法版本与数值不得随模板迁移。

机械文本复核补记：31 条无 slot 缺失或来源专属词泄漏。双栏 sort=True 文本会穿插其他列；应同时检查 sort=False 与图像。Voom+limma 的加号被 PDF 字体映射为 þ；部分 = 被提取为 ¼；上/下标、>= 及引用范围也有抽取差异。32709715 p3 的 `468-gene` 与 33323404 p11 的 `CB-839-induced` 在行末有需要保留的真实复合词连字符，不能用一律删除断行横线来做逐字校验。上述差异均按所见 PDF 字形核准，未为迎合机械匹配改变原措辞。

## PMID 32709715

The Genomic Landscape of SMARCA4 Alterations and Associations with Outcomes in Patients with Lung Cancer。登记版本 author_manuscript，SHA-256 `123cd6740a620ed3c818b3411b3cc2aa38262f4b51d5b9486a10b886e983843a`，16 页。

阅读覆盖：p1 题录/披露扫读；p2 Abstract 和 Introduction、p3 Introduction/Methods、p4 Methods、p5–6 Results、p6–8 Discussion 连续重读；p8–10 参考文献/致谢扫读；p11 translational relevance 阅读；p12–16 主图表及图注阅读。实际视觉检查 p3、p5、p12、p13、p14、p15、p16；入库原句均在 p3 或 p5。

主图表清单及视觉页：Fig.1 p12（变异位置/类别与蛋白保留或缺失）；Fig.2 p13（共变异、条件频率、富集、四基因交叠）；Fig.3 p14（生存及协变量模型，检查图意和分组，未重新估计）；Fig.4 p15（TMB、PD-L1、缓解与生存，保留不同终点结果不一致）；Table 1 p16（基线人群/分母）。所有主图表均已看图和图注，未重新计算统计量。

研究问题和证据链：将 SMARCA4 的变异事件先分为截短/融合/纯合缺失与错义/VUS 两类，再在有组织的子集中以 IHC 检验基因型与蛋白表型的关系，之后进入全队列共变异背景和临床终点。其整合是靶向基因组 + 定向蛋白表达 + 临床资料，不是全蛋白组、单细胞或空间组学。需分别保留 4813 总体、407 变异病例、86 例 IHC 的分母。

Methods 段落推进：队列来源及检测时间窗 → 分类规则及重叠类别优先级 → 基因/蛋白检测 → 不同 panel 版本的 TMB 分母归一 → 治疗资料与结局判读 → 模型和偏倚控制。本次学入“多类重叠如何归组”和“计数/覆盖分母/版本/单位”两条整句；学到的是可复现的定义顺序，不只是 assay 词汇。

Results 段落推进：总体发生率和变异图谱 → 类别内蛋白缺失/保留 → 共变异排序和对照富集 → 在未伴随常见共事件的病例中检验泛化边界 → 临床关联。新增 3 条 Results 分别练习基因型到蛋白表型、条件频率排序、常见共现并非必然共现。蛋白缺失集中于 Class 1 不等于全部 Class 1 均缺失；IHC 缺失也不完整等同蛋白功能丧失。

负结果与边界：ICI 缓解率差异与 PFS/OS 不显著并存；不能让较好 ORR 取代阴性时间终点。该研究单机构回顾性、IHC 可用组织有限；未完成 zygosity 层面的解释。来源内提醒：Fig.1B 图注写 Class 2 n=95，而 Results p5 写 195；Fig.2C 图注把显著基因标签解释成 PD-L1 expression，图/正文实为变异频率比较。均记录，不擅自修正为统一数字或把这些冲突转入用户稿件。

## PMID 33077574

NRF2 Activation Promotes Aggressive Lung Cancer and Associates with Poor Clinical Outcomes。登记版本 not_classified_by_header，SHA-256 `758747dacfc448ee96e212d42e64fbf07f8e0f125df525821154c53f81e7cf91`，13 页。

阅读覆盖：p1 Abstract/Introduction；p2 Introduction、Materials and Methods、Results 起始；p3–10 Results 与主图表/图注、p9–11 Discussion 全部连续重读；p11–12 参考文献及披露扫读；p13 期刊后台/权限信息扫读。实际视觉 p2–10；源句在 p2、p4、p6，均核对双栏顺序和断行。

主图表清单及视觉页：Fig.1 p3（GEMM 生存、表达热图、肺密度/生理、病理）；Fig.2 p5（组织分化、表达标志、ROS、脂质过氧化、GSH）；Table 1 p6（按基因型/时点的病理分类）；Fig.3 p7（signature 基因、富集、临床/模型表达、STK11 mRNA）；Fig.4 p8（OAK 分层及 PD-L1）；Fig.5 p10（IMpower131 结局、免疫表达signature、PD-L1）。全部主图表已视觉看图及图注，未复算。

研究问题和证据链：GEMM 三种遗传事件的组合检验 → 病理/肺功能表型 → 小鼠肺及同背景人细胞 redox readout/救援 → TCGA 人肿瘤中建立表达 signature → 跨临床/模型检验同向基因 → 独立试验队列的预后及免疫背景。鼠肺表达用芯片，人临床试验用 RNA Access；不能统称都做了 RNA-seq。signature 是表达表型，KEAP1/NFE2L2 mutation 是基因型，两者不完全重合。

Methods 段落推进：模型构建及基础测量 → 不同物种/来源的表达平台 → 临床队列 DNA/RNA 资料 → 差异表达 → 通路分析 → 关联和交互检验。新增 3 条 Methods 为“物种与平台一一对应”“同队列各组学检测如何交代”“差异表达到通路分析的流程句”。主文将 signature 详细构建、阈值和部分免疫评分细节指向补充材料；本次未读补充，不声称掌握这些全部参数。

Results 段落推进：实验系统的共同表型 → 基因型间差异 → 以直接 redox readout 衔接机制 → 用恢复/敲低救援检验功能关系 → 说明 signature 所含生物学过程 → 展示临床/模型一致和不一致的基因子集 → 对照基因型与表达表型 → 队列外检验。新增 4 条 Results 分别覆盖通路内容、跨系统保守表达、mutation-negative/signature-high 表型、条件依赖救援。模板把作者“universal targets”的概括收窄到已测系统的一致表达；富集不等同通量增加，表达一致不等同直接转录因子结合。

负结果与边界：多个正式治疗×signature 交互检验不显著，不能用亚组一显著一不显著替代交互证据。immune signature 是 bulk 表达代理，不等于直接细胞计数。GEMM 与人体差异还受采样时点、组织构成和模型背景影响；signature-high 的无已知突变病例不能据此认定突变检测漏检，也不能确认为某一特定表观遗传机制。救援句引用主文中对补图的叙述；核实的是主文整句，未声称已检查未提供的补图 S2。

## PMID 33323404

STK11/LKB1 Mutations in NSCLC Are Associated with KEAP1/NRF2-Dependent Radiotherapy Resistance Targetable by Glutaminase Inhibition。登记版本 author_manuscript，SHA-256 `62ed98bd908b24800e28f8759c3cff246129b27a141da6582b794f6468a97630`，27 页。

阅读覆盖：p1–2 Abstract、p2–3 Introduction、p3–6 Materials and methods、p6–11 Results、p11–13 Discussion 连续重读；p13–16 参考文献及行政内容扫读；p17 translational relevance 阅读；p18–22 主图/图注及 p23–27 主表阅读。实际视觉 p4、p5、p9、p11、p18–27。源句在 p4、p5、p9、p11，均视觉核对。

主图表清单及视觉页：Fig.1 p18（LRR、DFS、OS、DM）；Fig.2 p19（KRAS 共变异分组与结局）；Fig.3 p20（恢复/敲低、克隆形成、ROS、凋亡）；Fig.4 p21（移植瘤体积/倍增）；Fig.5 p22（CB-839 联合 IR 的 ROS、凋亡、克隆形成）；Tables 1–5 p23–27（人群、竞争风险、单/多变量模型）。全主图表已视觉看图/图注，未复算。

研究问题和证据链：临床 RT 后复发关联 → 33 细胞系筛查 → LKB1 双向遗传操作的同背景模型 → KEAP1 复表达/敲低 → ROS、凋亡和克隆形成分开测量 → 移植瘤验证 → GLS 抑制测试可干预脆弱性。本文自己的实验以功能、定向蛋白和 redox readout 为主，没有新做转录组、单细胞、空间组学或全蛋白组，不能为了“多组学”套标签。

Methods 段落推进：患者纳入/排除及 panel → 模型来源和双向遗传操作 → 认证/传代控制 → 蛋白实验 → 克隆形成的处理时序、剂量、计数定义 → ROS/凋亡时点 → 动物实验启动和随机分配 → 分开处理临床和实验统计。新增 3 条 Methods 分别学习双向同背景构建、克隆终点操作化、按体积触发随机分配；模板要求实际随机化，不能补入源文没有提供的盲法或功效分析。

Results 段落推进：明确临床观察 → 提出可检验的功能问题 → 相反方向扰动/救援 → 共享反应与效应幅度差异 → 下游 readout → 体内体系 → 药理可干预性 → “at least in part”有界机制总结。新增 3 条 Results 为所有模型共享的 ROS 变化、恢复表达使药物敏化消失、部分通路依赖的总结。短期凋亡与长期克隆形成结果不完全一致，应分别报告，不能让任一替代全部结论。

负结果与来源边界：小型细胞系筛查和多个临床亚组/凋亡比较不显著；不能把全部实验概括成一致显著。临床 panel 没覆盖 KEAP1，因此临床中不能检验其效应；裸鼠/细胞自主实验也没有解释免疫机制。Methods p4 的 ROS 检测写 DCFDA，而 Fig.3G 图注和 Fig.3/5 横轴写 MitoSOX；该实质检测标记冲突已视觉确认，入库共同ROS变化句明确提示，未复制未决的具体试剂。p11 rescue 原句有 “with a DER ... were 0.8”语法错误，原句保留，模板仅修正通用句法。

## PMID 37097610

Clinicopathologic, Genomic, and Immunophenotypic Landscape of ATM Mutations in Non-Small Cell Lung Cancer。登记版本 author_manuscript，SHA-256 `4bbdf5563fd45f7d42ec88f21ebbaf6f70411e05e133e8754ed40141717ddecd`，22 页。

阅读覆盖：p1 披露/行政扫读；p2–3 Abstract、p3–4 Introduction、p4–7 Methods、p7–12 Results、p12–14 Discussion 连续重读；p14–16 参考文献/致谢扫读；p17 translational relevance 阅读；p18–22 主图及图注阅读。实际视觉 p4、p5、p6、p8、p9、p11、p12、p18–22。源句 p4、p6、p9、p11、p12 均视觉核对。

主图表清单及视觉页：Fig.1 p18（位置、变异类、TMB、PD-L1、富集）；Fig.2 p19（oncoprint）；Fig.3 p20（突变类与 IHC、代表性瘤内异质性）；Fig.4 p21（按蛋白保留/缺失分层的共变异）；Fig.5 p22（治疗结局）。没有主表，补表未提供。全主图和图注已视觉看，未重算统计。

研究问题和证据链：靶向 NGS 突变类别/潜在LOH → 配对可用组织 IHC → 共变异对比 → 临床治疗结局 → 临床 mIF 指定区域免疫细胞 → H&E 数字病理 → TCGA bulk RNA 的免疫推断。此处不同组学层不是统一完整配对队列；mIF 的535样本、IHC182样本与TCGA反卷积不能写成相同样本的三重验证。putative LOH 是突变+拷贝丢失的代理，不等同已完成等位基因定相。

Methods 段落推进：中心/同意/人群 → 各中心靶向panel和样本纯度 → 变异类别及致病性推断 → IHC内部对照及评分 → mIF标记、ROI和区域定义 → bulk RNA免疫估计 → 数字病理 → 对照统计。新增 3 条 Methods 为样本纯度到捕获测序、bulk RNA推断工具和输出、ROI内按标记判定细胞；不同技术的输入/输出/直接或推断性质必须写明。

Results 段落推进：总体与变异数 → 共变异谱并队列外检验 → 基因组类别到蛋白表型 → 解释不一致并深入IHC异质性 → 分层结局 → mIF阴性结果 → 按共变异进一步分层 → 其他数据/模态补充。新增 3 条 Results 为有表达病例中的异质性子集、直接mIF的阴性细胞比较、bulk RNA反卷积的细胞富集评分差异。后两者不矛盾到必须择一：队列、数据类型、细胞集和测量方式不同，必须逐层报告。

负结果与来源边界：IHC类与蛋白表达不是一一对应；missense预测致病不等同实验证实。多个治疗结局无显著差异，不能写成免疫疗效确定提高。来源数字提醒：p7–8 TMB数对的排列先WT后MUT，但正文比较以MUT为主语；p8句“median PD-L1 ... higher among ATMWT (10% vs.3%)”与Fig.1D及后续阳性率方向不一致。p8的71.4%/28.6%涉及 Fig.3A 按蛋白表达分组的变异类构成，与 p9中“类内蛋白缺失率”58.8%/21.3%的条件分母不同，不能直接当成同一概率，也不能擅自替换。入库不选这些争议数字句。

## PMID 37733794

ATM Mutations Associate with Distinct Co-Mutational Patterns and Therapeutic Vulnerabilities in NSCLC。登记版本 not_classified_by_header，SHA-256 `c233223884b13f02f9ec63568d9d1520d2b9303b0fdf4e74bb575bc6010d5c6b`，15 页。

阅读覆盖：p1 Abstract/Introduction、p2 Introduction/Methods、p3–4 Methods、p5–6及p10 Results、p10及p13 Discussion 连续重读；p6–12所有主图/主表和图注阅读；p14披露/贡献及p14–15参考文献扫读。实际视觉 p2–12。入库句在 p2、p3、p5、p10，均核对版面。

主图表清单及视觉页：Fig.1 p6（五队列设计和基因组谱）；Table 1 p7（五队列基线）；Fig.2 p8（KRAS背景分层共变异、ATM变异类、RPPA）；Fig.3 p9（分层TMB、突变signature）；Fig.4 p11（临床未校正/校正结局）；Fig.5 p12（上下游STING蛋白、IFN转录、CXCL10分泌、化疗处理）。全部主图/表及图注视觉看过，未复算模型或蛋白条带定量。

研究问题和证据链：五队列基因组共变异meta分析 → KRAS背景分层 → 变异类与RPPA/RNA关联 → WES突变signature解释负荷差异 → 独立限制条件的真实世界治疗队列 → 同背景鼠细胞ATM敲除 → 上下游信号和细胞因子 → 化疗条件下的响应。DNA突变signature与RNA表达signature是不同对象；RPPA是定向蛋白阵列，不能自动表述为全蛋白组。

Methods 段落推进：每个数据源的病例/样本选择规则 → 每个队列真实可用的测量 → 不同分析目的使用不同ATM变异定义 → 按panel长度计算负荷或明确排除不适配指标 → WES适配的signature参考版本 → 实验模型和定向readout → 多队列合并与临床协变量。新增 3 条 Methods 为重复样本选取、突变signature算法/参考/模态理由、因检测范围未验证而不计算指标。这一“不做某分析的理由”本身是应学入的方法写作。

Results 段落推进：先报告分布和构成 → 总体共变异 → 在关键背景内重新评估 → 用蛋白与RNA不一致限制功能推断 → signature差异在分层后消失 → 调整临床混杂 → 定向机制测量并保留上下游不一致。新增 4 条 Results 为位置/类别构成、RNA对蛋白的弱替代性、分层后signature无显著差异、上游与下游输出不同步。最后一条模板刻意止于实际细胞readout，不把作者“possible impaired antitumor immune response”变成已经测到的体内免疫结果。

负结果与边界：基线 cGAS/STING 增加不显著；总/磷酸IRF3未随之确定增加，CXCL10分泌反而下降。药理ATM抑制与基因敲除不必等同。临床治疗分层并非随机，不能仅凭ICI+chemo组有差异宣布预测交互。人H2030/H23为不同遗传背景，作者明确未做同背景人细胞验证。来源提醒：p10截短ATM组 HR=0.731 与列出95%CI=0.899–1.038不包含该点估计，作为来源内数值冲突保留；没有选此句进新模板。p3签名方法选取版本理由属于本文该WES数据的选择，不能推广为当前普遍推荐。

## 本批可迁移的段落结构与使用约束

组学 Results 的主要推进可根据实际证据采用：先定义被分析的样本/事件/表达表型及分母，再描绘位置或构成，给出比较和背景分层，追查RNA–蛋白或基因型–表型的不一致，最后用独立队列或直接功能读出检验有限解释。无需每段强行写生存HR或P值；有价值的完整句还包括分类、分母、部分一致性、未检出共事件、异质性、替代指标不足、上下游不一致和救援。

Methods 应把“谁/什么样本—用什么检测—怎样定义或处理—输出什么量—如何比较或验证”连成可追踪链。占位模板只提供句法与信息组织，不能替用户补做平台、质控、阈值、模型构建、随机化、配对样本或外部验证。每一项均需用户自己的研究记录。

本批是同一代理阅读和视觉核句。没有新增独立审读者，没有读取未提供的独立补充方法，没有验证所有原始数据或代码，也没有因模板入库改变任何旧阅读/验收状态。

# CCR 正文重读与句式学习：Batch B

日期：2026-10-15。执行者：`/root/reread_ccr_b`。这是当前子任务的实际阅读、视觉核对和语言迁移记录，不是独立科学复现，也不自动改变既有 reading/review 状态。

范围：5 篇，主 PDF 63 个物理页；主叙事逐页重读，参考文献/作者贡献/行政内容扫读。共选择 33 条正文原句（16 Methods、17 Results）；原句仅做空白、断行连字符和字体表达归一，模板是另行抽象的 synthetic frame。所有 33 条均检查过所在页 PNG，源 PDF 哈希由 render helper 再次确认与 private manifest 一致。主图表按图、图注和正文对照检查；没有声称重新计算全部统计量或独立核验原始数据。没有打开任何单独补充文件。

## PMID 38300729

《Combining Genomic Biomarkers to Guide Immunotherapy in Non-Small Cell Lung Cancer》。12 页，publisher_typeset_pdf。SHA-256：`e6fe17f7403bcb66e94d6aaad03137c6ea95e62e0c04f5d84b33ac7f5554ad19`。

覆盖：p1 Abstract/Introduction；p2 Introduction、Translational Relevance、Methods；p3 Methods、数据可用性、Results；p4–9 Results、图表与图注；p10 Results收尾、Discussion/结论；p11–12 行政及参考文献扫读。PNG 实际检查页：2、3、4、5、6、7、8、9。主图表：Table 1 p4，Figure 1 p5，Figure 2 p7，Figure 3 p8，Figure 4 p9；均看图及图注。

研究问题：既有STK11/KEAP1/EGFR“耐药标志物”为何仍有应答者，是否在TMB背景中组合后提高识别无获益者的特异性。发现队列75人做肿瘤/正常WGS，验证队列169人来自MSK-IMPACT panel；限PD-(L)1单药，纯度≥20%，有至少一次RECIST可评价记录。主要证据链为：样本/检测定义→连续和分组TMB→PD-L1未充分补足→逐基因、克隆性、双等位与乘客过滤→组合规则→独立队列复用→少见反例与前瞻性验证边界。这是基因组与临床/IHC组合，不是RNA/单细胞/空间组学。

真正学到的 Methods 段落推进：先分别说明发现与验证队列的来源和共同入排，再定义结局；随后按“WGS整合管线→克隆性计算→TMB分母→致病变异过滤”推进。平台所需输入不同，克隆性及VUS判读规则也分别交代。可复用段落骨架：
> Samples from [cohorts] were profiled using [platforms]. [Eligibility/QC] defined the evaluable set. [Metric] was calculated using [variant classes and denominator]. [Alteration classes] were assigned using [classification rules], with [platform-specific exceptions] reported separately.

真正学到的 Results 段落推进：不是只报P值，而是先说“为检验互补信息我们分析什么”，再交代总变异数、携带者数、VUS剔除、克隆性/双等位证据，之后才进入分层结局；段末明确“组合增加了什么信息”。本批结果句选择事件-患者分母和双等位状态，避免全部模板落在生存终点。可复用段落骨架：
> We next evaluated [qualified genomic feature]. [Event count] events were detected in [carrier count] patients. After [filtering], [retained events] remained, of which [subset] had [allelic evidence]. These qualified events were then assessed within [prespecified strata].

负结果与限制：单用TMB低组仍有DCB；PD-L1+TMB仍不足；原STK11+KRAS共变异无明显DCB关联；验证队列存在低TMB/STK11变异仍获益的患者。WGS与panel分布相近不等于测量等效；无治疗对照不能建立治疗交互；当前数据不能直接支持临床停用ICB。纯度≥20%筛选本身限制泛化。补充材料未提供，正文引用的补图不算已读。

来源问题：p3正文将57/75写成57%，而同段及Table 1对应57例；Table 1 smoking available counts与正文64例及never-smoker数字也不完全一致。句式不使用这些冲突数据。p6两枚远距KEAP1突变是否in trans未能确证，不能自动称双等位基因失活。主模板刻意保留“10 alterations”事件分母。

新增6条：Methods integrated-genome-processing、tmb-definition、pathogenic-variant-rule；Results filtered-variant-yield、biallelic-state、alterations-and-carriers。

## PMID 38980931

《Transcriptional Phenocopies of Deleterious KEAP1 Mutations Correlate with Survival Outcomes in Lung Cancer Treated with Immunotherapy》。15 页，publisher_typeset_pdf。SHA-256：`93eb22b1aa149270f5e592b3317fe5c8cfe7b7681c1d67433d36378829838480`。

覆盖：p1 Abstract/Introduction；p2 Introduction、Translational Relevance、Methods；p3 Methods及Results起始；p4–12 Results和图注，p12–13 Discussion/结论；p14–15 行政和参考文献扫读。PNG 实际检查页：3、4、5、6、7、8、9、10、11、12。主图：Figure 1 p4及p5续注，Figure 2 p5，Figure 3 p6及p7续注，Figure 4 p8，Figure 5 p9–10，Figure 6 p11及p12续注；没有正文表。全部主图/续注已看。

研究设计与组学证据链：TCGA差异表达与无监督聚类得到共表达12基因集合→定义KEAPness分数→在SU2C非鳞无先前TKI的93人用缺乏DCB目标、ROC/Youden/2000次bootstrap确定阈值→固定阈值用于SU2C、OAK/POPLAR及TRACERx421→bulk RNA免疫分型、PROGENy与DoRothEA→多区域WES/RNA连接选择压力与REVOLVER演化轨迹→WES T-cell ExTRECT给出跨模态免疫估计。这里没有单细胞或空间转录组。multiregion是区域采样，不能称连续空间表达成像。

Methods 段落推进学习：其关键是明确“特征推导、分数计算、阈值选择、固定阈值迁移”四件事，不能一笔写成‘validated signature’。之后按功能安排工具：通路/TF推断回答表型含义，RNA免疫分型回答微环境，dN/dS/REVOLVER回答遗传选择与演化，WES估计回答异模态一致性。
> [Gene set] was derived using [discovery procedure] in [derivation data]. A score was computed by [aggregation]. The cutoff was selected in [explicit training subset] against [target] using [criterion and resampling], then applied unchanged to [validation/characterization cohorts]. [Independent modality] was used to assess consistency of [biological feature].

Results 段落推进学习：先建立“无突变也有共同转录足迹”，再描述通路与免疫相关表型；临床外部应用后，构造纯表型/基因型组合模型；最后借多区域数据问“由哪些遗传路线产生、同一瘤不同区域是否稳定、免疫状态是否同步变化”。不是把热图转述为显著差异列表。典型段内链：
> [Transcriptional phenotype] occurred across [genotypes]. It showed [inferred pathway/immune features]. The phenotype was then evaluated in [independent data]. Across [regions/evolutionary clusters], [shared pattern] persisted, while [specific heterogeneity] remained.

本批结果句覆盖转录phenocopy、免疫状态相似但子型不同、31%至少一个非表型区域的异质性、不同driver路径的表型收敛。31%不能写成全部空间均一，更不能用横断面区域一致性证明时间稳定。RNA免疫排斥推断不是直接空间测量；ExTRECT为WES计算估计，不是直接细胞计数，也不是新患者队列。

阴性/不一致与限制：KEAPness与KEAPness-free TMB无差异；共享clonal nonsynonymous负荷和genome doubling相近；KEAPness不只是STK11高突变亚组；部分KEAP1突变转录静默。低样本量及缺少PD-L1/TMB等限制校正，OAK/POPLAR临床变量有限；某些结果同样见于docetaxel队列，不能直接称ICB特异性预测。阈值训练使用结局，bootstrap不是外部验证；合并SU2C/OAK数据不产生第三个独立验证集。

原文保留‘receiver operator characteristic’等实际措辞。补充文件未提供；本文直接引用的补充图、基因列表补表没有被声称重读。新增8条：Methods signature-definition、cutoff-derivation、fixed-cutoff-transfer、orthogonal-immune-estimation；Results transcriptional-phenocopy、immune-phenotype-resemblance、multiregion-heterogeneity、phenotypic-convergence。

## PMID 39545922

《Divergent Clinical and Immunologic Outcomes Based on STK11 Co-mutation Status in Resectable KRAS-Mutant Lung Cancers Following Neoadjuvant Immune Checkpoint Blockade》。13 页，not_classified_by_header。SHA-256：`29c4ac351e2abb1ff9b8478390b84146debed3f7e318459c7def256aec280588`。

覆盖：p1 Abstract/Introduction；p2 Introduction、Translational Relevance、Methods；p3–4 Methods，p4–10 Results；p10–11 Discussion/结论；p11–13行政和参考文献扫读。PNG 实际检查页：3、4、5、6、7、8、9。主图表：Table 1 p5，Figure 1 p6，Figure 2 p8，Figure 3 p9；全部看图/图注，尤其区分Fig2D患者样本层pseudobulk与Fig3细胞层Wilcoxon。

设计：多机构多臂phase I/II的回顾性探索分析，总61人、52有基线测序、21 KRASmut；单细胞核心来自6例KRAS/STK11双突变及7例KRASmut/STK11wt肿瘤。切除后冻存T细胞分选，10x 5′ V(D)J与5′DGE来自同一细胞。原文有TCR捕获，但未据此证明所有CD8 TIL为肿瘤抗原特异性，不能把TCR技术名称当功能验证。

Methods 推进：患者与治疗/终点→基线基因型与IHC→样本消化/冻存/FACS→同细胞RNA/TCR捕获及测序深度→Cell Ranger和细胞/基因QC→Seurat整合与两轮聚类/注释→sample/cluster pseudobulk降维→SAVER及mixed-effect DE→预定义基因集score。每步交代分析单位，尤其避免把细胞层样本量当患者层重复。
> [Cells] from [sample context] were isolated and profiled with paired [assays]. After [QC], [clustering procedure] was used to identify and annotate [states]. Counts were aggregated within [biological sample/cluster unit] for [sample-level analysis]. Differential expression used [model], and [scores] were calculated using [imputation and gene-set rules].

技术细节读到而非凭空扩充：细胞基因数<250或偏离中位数3×MAD、线粒体>10%、核糖体<10%过滤；VDJ只保留full-length；聚类排除应激、TCR等相关基因；CD8A cutoff 1.5；global CD3 pseudobulk按样本汇总并按library size归一，ComBat校正，cluster HVGs拼接进入PCA；DE mixed-effect由raisin实现并BH FDR<0.05；个别表达图的Wilcoxon是在细胞层。可迁移的是交代方法与单位的结构，不能复制软件、阈值或替用户声称做过imputation。

Results 推进：临床风险差异提出“数量还是质量”的问题→先给QC后92,525细胞/14簇和marker注释→两组比例类似→cluster-pseudobulk显示状态分离→effector转录增强却同时checkpoint/驻留与terminal dysfunction→PGE2/OXPHOS/IL-2相关表达→另一个KRASwt数据背景核查关联。不能把cytotoxic gene高表达直接等同杀伤功能增强，不能把OXPHOS转录score称代谢通量实测。段落骨架：
> We profiled [cell population] to examine [biological question]. [QC yield and annotated states] defined the atlas. Although [composition observation], [sample-level analysis] showed [within-cell-state difference]. [Marker programs] were then examined, revealing [coexisting programs] and motivating [bounded hypothesis].

负结果/边界：MPR两组17%/25%未显著，不能称等效；STK11wt组较高PGE2相关表达是反直觉观察，作者给出多种解释，不是PGE2促进免疫的机制定论。样本小、治疗异质、仅术后组织，无法确定表达差异来自固有TME还是治疗诱导；缺KRASwt/STK11mut足够组织，不能泛化为STK11单独作用。功能机制研究尚需开展。Fig3很多P<2.22e–16源于细胞层检验，不可转为强患者层显著性或独立生物学重复。

来源内部差异：p7正文写adjacent normal lung n=8，Fig2 p8图注写n=7；p4正文pretreatment PD-L1缺16例而Table1 p5缺10例。记录差异，不用这些冲突数字组建模板。补充状态继承not_recorded，本次无单独补充材料可读。

新增8条：Methods paired-single-cell-assays、single-cell-quality-control、sample-level-pseudobulk、single-cell-mixed-effects；Results single-cell-atlas-yield、similar-composition-distinct-state、pseudobulk-state-separation、paradoxical-effector-program。

## PMID 39804166

《Impact of Co-mutations and Transcriptional Signatures in Non-Small Cell Lung Cancer Patients Treated with Adagrasib in the KRYSTAL-1 Trial》。13 页，publisher_main_pdf。SHA-256：`238c89c029a713a161255a6c9bddc5f9fe03424ccbf92e6f1650239613795f03`。

覆盖：p1 Abstract/Introduction；p2 Introduction、Translational Relevance、Methods；p3–4 Methods；p4–9 Results，p8–10 Discussion/结论；p10–13行政和参考文献扫读。PNG 实际检查页：2、3、5、6、7、8、9。主图：Figure 1、2均p5；Figure 3 p6；Figure 4 p7；Figure 5 p8；Figure 6 p9；均看图及图注，正文无主表（临床特征在补表）。

证据设计：KRYSTAL-1 129例中121例NGS可评价、68例靶向转录panel可评价，50例同时有KEAP1/STK11状态与转录数据。临床共突变关联→多个细胞系回补→CDX/PDX→LU99 in vivo CRISPR筛选与KO→组合药筛与clonogenic/pS6→NRF2和LKB1等signature→组合基因型/转录状态。原文HTG EdgeSeq是特定transcriptome panel，不能称所有转录本均测到，也不能把它写成泛蛋白组。

Methods 推进：先界定每个分析的evaluable denominator，再明确TSG deleterious规则和每基因panel覆盖分母；表达方法按“平台→library-size normalization/log2CPM→表达过滤→已覆盖signature基因→聚合score”展开；功能方法按细胞认证/污染、剂量时间、对照、读出、重复与模型随机化、筛选覆盖/阴阳性对照展开。
> [Analysis set] included samples with [required assay availability]. Raw counts from [targeted platform] were processed using [normalization]. Scores used [covered and expressed genes] with [aggregation rule]. To test [candidate mechanism], [perturbation] and [rescue] were evaluated in [models] against [controls] using [specified assay].

Results 段落推进：临床关联提出候选→回补改变药物敏感性→筛选将基因定位为候选耐药调节因子→KO后体内再生长支持模型内适应性耐药→再检验可干预组合→表达signature扩展突变之外的表型。每层保留独立结论，尤其CRISPR富集不能代替KO验证，也不能把preclinical combination自动写成临床有效。
> Following [clinical association], we tested [gene] in [models]. [Rescue/perturbation] changed [assay readout]. A [screen] independently prioritized [candidate], whereas [negative candidate] was not enriched in [model]. Subsequent [validation assay] supported [model-bounded conclusion].

关键非生存学习点：KEAP1回补在三个细胞系均增加敏感性；LKB1回补有模型差异，H23未增加；LU99筛选KEAP1最富集、STK11未富集；KO开始时仍缩瘤但day20后再生长；NRF2高signature在KEAP1MUT中富集，但野生型也可有高转录表型。Methods对sgRNA筛选约1000基因的文库设计与Results的over900最终筛选不应混为一谈。

负结果/边界：STK11突变与ORR无差异、NRF2分数与ORR无差异、EMT signature未关联临床结局；STK11WT/KEAP1WT亚组个别相关分析不显著。NRF2-high KEAP1WT的OS相关在Fig5F P=0.165，不能照摘要/Discussion概括为所有相关都显著。转录分数是信号替代量，pS6是有针对性蛋白读出，均不等同代谢/全蛋白组。mTOR组合只在模型有支持，尚无临床验证。免疫缺陷移植模型不能证明免疫完整TME机制。

补充文件未提供，本次只读到正文对补图/补方法的陈述，未声称打开Supplementary Methods S1。p4正文non-targeting sgRNA所列序列与KEAP1 sgRNA相同，保留为需回原作者/补充方法核查的来源疑点，不将该序列纳入可复用模板。

新增7条：Methods targeted-transcriptome-normalization、panel-aware-signature-scoring、crispr-screen-controls；Results reexpression-sensitization、screen-prioritized-gene、screen-negative-context、genotype-signature-concordance。

## PMID 41417462

《Molecular and Clinical Characteristics of Patients with Non-Small Cell Lung Cancer Harboring KRAS G12V Mutations》。10 页，not_classified_by_header。SHA-256：`3532ee70eef471e66046f91cdccae0621581006f8941e502f5a3d124a93f9556`。

覆盖：p1 Abstract/Introduction；p2 Introduction、Translational Relevance和Methods；p3–4 Methods/Results；p4–7 Results/图表，p6–8 Discussion/结论；p9–10行政和参考文献扫读。PNG 实际检查页：2、3、4、5、6、7。主图表：Figure 1 p3、Table 1 p4、Figure 2 p5、Figure 3/4 p6、Figure 5 p7；全部看图与图注。

设计与实际测量：nNGM真实世界回顾性636例KRAS G12V患者，四种不同诊断panel（14–26基因）和PD-L1/CD8 IHC，治疗子集151例；CD8定量仅16例G12V对40例non-G12V。有基因组检测和有限免疫组织化学，不是完整多组学平台，更没有scRNA或空间组学。数字切片ROI分析不等于空间组学。

Methods 推进：数据库/入组日期/病理核查与排除→四版panel变异检出→PD-L1检测及TPS解释→CD8 IHC、组织可得性、每例五个400μm×400μm ROI、排除伪影与非肿瘤上皮、watershed tumor detection、positive cell detection、CD8/肿瘤细胞比→real-world endpoint定义和每基因受检分母。
> [Index genotype] cases were identified from [registry] and verified by [pathology/chart review]. Co-alterations were assessed using [panel versions]. [Immune marker] was quantified in [selected regions] using [detection algorithms], and [ratio] was calculated with [specified denominator].

Results 推进：先描述研究群体和可得性分母→报告按受检基因计算的共变异排序与panel内未检出→按吸烟暴露比较PD-L1/共变异→小组织子集CD8比例的数值差异及不显著→治疗关联。该结构可学习“基因组分布→临床暴露关联→独立测量层”的组织方式，但没有把检测范围扩大。
> Among [assessed patients], [co-alterations] were most frequently detected. No additional alterations were detected within [assayed scope] in [fraction]. [Molecular features] were then compared by [exposure group]. In the tissue-evaluable subset, [immune metric] showed [observed difference and uncertainty].

来源问题：p4写45.7%(274/636)与算术不相符（274/636约43.1%，这里仅作审计派生核查）；Figure2图注也给274无共突变。原句保留实际45.7%(274/636)，模板不硬编码该比例；需实际填入用户核实的分母。p4正文男性52.8%(300/636)与Table1男性336/52.8%不一致，不能默默选一个。p6高PD-L1治疗比较中个别HR方向与曲线/表述不易对齐，未将这些HR写进新增模板。

阴性与边界：CD8/肿瘤细胞比0.19对0.09，P=0.687，不代表免疫浸润确证升高；样本少且有离群值。有限panel未检出不等于全基因组无共变异。real-world治疗组有PD-L1/PS选择差异，不能直接宣称因果疗效。吸烟分层中STK11未见明显差异，不应按TP53/KEAP1泛化。未做本队列双checkpoint治疗，Discussion的潜力不等于已验证组合效果。补充材料未提供。

新增4条：Methods panel-ascertainment、cell-ratio-quantification；Results coalteration-landscape、no-panel-coalteration-detected。

# CCR正文组学与方法学重新学习：Batch C

日期：2026-10-15。执行者：同一代理重新阅读及视觉检查，不是独立统计复核。来源为本任务 private-source-manifest.json 登记的5份PDF，哈希及物理页数由任务helper核验。没有改变任何文章审读状态，也没有将未提供的补充材料标记为已读。原文句子只归一空白、断行连字符与字体表示；模板均为人工抽象，不能作为用户研究结果的证据。

本批共26条：13条正文Methods、13条正文Results；其中一条Results中解释panel分母的句子亦可迁移至Methods。每篇至少2条Methods、2条非生存统计Results。选句所在整页与主图表均实际打开PNG视觉检查；图表检查覆盖轴、分组、图注与证据链对应关系，不声称每个数字或统计模型已独立重算。

## PMID 41870274

文章：The Pan-Tumor Landscape of Gene Amplifications and Copy Number Amplification Ratio for Established and Emerging Clinical Targets。登记SHA-256：926c2d776ad197b858c3af1ccf7e32f47347d4382e8a491b5c503e0d7f5b157a；14个物理页。

重新阅读覆盖：p1摘要、Introduction；pp1–2完整Introduction；pp2–4 Materials and Methods（含CGP、CN建模、IHC/FISH抽取、统计和伦理）；pp4–9全部Results；pp9–12 Discussion及结论性段落；pp12–13数据可用性、披露与贡献等行政信息扫读；pp13–14参考文献扫读。pp4–6、9–11图文交织的图注完整阅读。没有独立读取Supplementary Figures S1–S42及补充表。

实际视觉页：3、4、5、6、9、10。主Table 1在p3；Figure 1在p4；Figure 2在p5；Figure 3在p6；Figure 4在p9；Figure 5在p10，延续图注p11在正文阅读中覆盖。选句页：Methods p3两条；Results p6、p9各一条。输出4条。

研究问题与设计：在大规模临床靶向测序中，拷贝数扩增如何跨基因/癌种分布；以肿瘤倍性归一化的AmpRatio能否改善定量，并与IHC/FISH及配对组织/液体检测相互对照。486,340组织和85,635液体样本用于景观，不是同一配对集合；临床结局另用FH-FMI疾病特异子集；组织液体检测一致性使用≤30天的2,440对样本。DNA靶向CGP并非全基因组测序，且本文不是RNA/全蛋白质组研究。

组学证据链：靶向覆盖与SNP等位基因频率→纯度/倍性/片段CN模型→gene CN/sample ploidy定量→基因与癌种的频率/幅度分布→疾病特异co-alteration景观→IHC/FISH匹配→不同肿瘤分数下组织液体检出一致性。变异类别的总体优势允许报告例外；所有共现仍是关联。ERBB2定义与其他基因不同，组织/液体也使用不同临床报告阈值。

负结果、边界：HER2结果没有一个跨癌种最佳界值；乳腺中第二与第三三分位差异多次不显著。液体PPA总体38.5%，TF≥20%时88.1%，不能把高TF子集敏感度外推全部液体样本。323个共同检出扩增中的R=.87不是全样本检测敏感度，也不能证明绝对定量无偏。该相关句在正文p9，所引S41未独立提供。STK11是NSCLC共变异比较的背景，不是直接STK11功能干预。

学到的Methods段落推进：先列样本来源和可用数据集合→说明DNA提取/捕获/coverage→明确病原性过滤和变异类别→CN模型输入及归一化公式→事件阈值及组织/液体差异→正交检测的同日配对规则→按分析目标写统计。不能把完整平台验证细节从引文自动当作本研究执行。

学到的Results段落推进：整体景观与例外→按具体靶标展示癌种特异分布/幅度→共变异情境→跨检测一致性→临床关联→检出技术边界。本文特别适合学习先报类别模式再保留exception，以及先限制共同检出分母再报相关性的整句结构。

## PMID 42268349

文章：Molecular and Clinical Characteristics of Patients with Non-Small Cell Lung Cancer Harboring KRAS Q61 Mutations to Assess Therapeutic Responses。登记SHA-256：13b1e175a3abd35ebab4757b894277bf29274068d00d98d01197b68ffc01f766；24个物理页。

重新阅读覆盖：p1作者/披露扫读；p2 Translational Relevance和摘要，p3摘要延续与Introduction，pp3–5全部Introduction；pp5–8 Methods（patients、NGS、IHC、临床数据和统计）；pp8–11全部Results；pp11–15完整Discussion与Conclusion；pp15–17参考文献扫读；p18完整主图注；pp19–22主图，pp23–24主Table 1。没有独立读取补充表/图。

实际视觉页：5、6、8、9、19、20、21、22、23、24。主Figure 1 p19；Figure 2 p20；Figure 3 p21；Figure 4 p22；Table 1 pp23–24。选句页：Methods p5、p6；Results p8、p9。输出5条，其中p9 panel-specific分母句保留来源Results，可迁移Methods。

研究问题与设计：诊断时KRAS Q61X阳性NSCLC的变异亚型、共变异和真实世界治疗结局。8862个KRAS阳性个体中487个Q61，排除后365；不同年代4种14–26基因panel，另3例只测选定基因。它是基因组及IHC临床描述，未执行转录组、单细胞、空间组学或新的细胞机制实验。Introduction中SHP2/SOS1/RAF机制来自背景文献，不是本篇新结果。

组学证据链：诊断分子状态定义队列→NGS的VAF和coverage判读门槛→热点内substitution构成→PD-L1可用子集→以各基因被覆盖患者为分母的共变异→亚型间共变异差异→治疗结局。学习重点是分母随基因/panel变化，和“没有检出”对检测范围的依赖。

负结果、边界：原文把Q61L与STK11称mutually exclusive，但本次模板不搬用该结论；零观察共现不能自行建立统计互斥。42.1%未发现共变异，受较窄panel影响，模板明确no detected和assay_scope。Q61H/Q61L生存差异需要共变异校正，不能直接归因于KRAS亚型；治疗非随机、ICB单药组高度PD-L1-high，有选择偏倚。二线正文42 patients却多处22/44、2/44等；Table 1一线111与正文105、某些亚组人数及图值亦不一致。这些未静默修正、未用于新的句子数据。图3/4的p=0.000不能改写为P=0，模板未选用这些数值。

学到的Methods段落推进：初诊分子入选条件→排除复发取样/同步肿瘤等→随着年份变化的panel与判读门槛→IHC平台/clone和TPS定义→真实世界结局及缺失数据处理→探索性统计说明。伦理和标准操作不能从模板推定适用于用户研究。

学到的Results段落推进：筛选人数→临床可用性与缺失→从常见至罕见的变异谱→可检测分母→总体共变异→亚型对比→结局。完整句式可表达分子组成而不依赖显著性；不可把热点内比例误作全部NSCLC的患病率。

## PMID 42456046

文章：Intratumoral Immune Heterogeneity Drives Divergent Outcomes to PD-(L)1 Blockade in Lung Cancer。登记SHA-256：c795f9d233acd688cca4a87407fe7a0a2c8e863c69b8c9833d696982ced28855；44个物理页。

重新阅读覆盖：pp1–5作者/贡献/披露/缩略语及空白行政段扫读；p6 Translational Relevance；pp7–8全部摘要；pp9–10完整Introduction；pp10–16全部Methods，包括ITIH、clinical cohorts、digital pathology、IRE RNA/WES、bioinformatics、PD-L1 imputation；pp16–17数据可用性；pp17–23全部Results；pp24–27完整Discussion及结论性段落；pp27–28致谢扫读；pp28–35参考文献扫读；pp35–38完整主图注；pp39–44全部6幅主图视觉读取。这些主图在文本抽取中近乎空白，因此没有将“文本提取成功”替代图像阅读。未独立读取18幅补充图及7张补充表。

实际视觉页：10、11、14、18、19、22、39、40、41、42、43、44。Figure 1 p39流程；Figure 2 p40多区域immune signature/分类；Figure 3 p41病理TIL及cell segmentation；Figure 4 p42各队列survival/BOR/类别构成；Figure 5 p43 PD-L1/ITIH与immune signatures；Figure 6 p44 MFP、STK11/KEAP1及结局。正文无独立主表。选句页：Methods p10、p11、p14；Results p19两条、p22一条。输出6条。

研究问题与设计：用TRACERx多区域bulk RNA的免疫状态差异训练单样本ITIH推断模型，然后在单样本临床队列、TCGA和IRE数字病理中评估模式。计算特征为29种MFP相关表达signature，经ssGSEA、离散化、CatBoost；后续三队列A291/B439/C355是单区域资料。IRE64片H&E以QuPath细胞分类作正交读出，部分ROI因技术原因选择；未专门评估肿瘤中心/侵袭边缘。不能称为新的空间转录组或单细胞测序研究。

组学证据链：多区域bulk RNA区域状态→肿瘤内状态不一致定义→29 immune signatures→单样本机器学习推断→多队列表达梯度重现→病理TIL模式/细胞比例正交支持→与PD-L1、MFP、STK11/KEAP1联合分层。新句子学习包括特征构建的完整动作顺序、采样不足的排除理由、不同免疫标志物不一致时的程序得分描述。

负结果、问题与边界：Methods pp10–11训练明确746区域/246患者，Results p17/Figure 2A使用80/285作为约30%异质性频率。两个分母的具体关系没有在本次自行修复。Figure 2图流程存在训练/validation划分，但主文未明确是否患者分组后划分，不能擅自声称patient-wise leakage-free split。IRE64例病理cell proportion p=.07/.06，不能概括为所有正交检测均显著。TCGA图3A/B显著，故选句限定此读出。缺独立多区域外部ground truth；单样本队列的模式/结局重复不能替代该验证。C队列缺细致临床/分子信息；PD-L1缺失与imputation保留为推断，且A模型用了BOR等临床变量，不能把其结果写作完全独立基线检测验证。KEAP1/STK11为合并基因状态，不分离gene-specific效应；本文标题含Drives不授权把观察性signature写成因果。

学到的Methods段落推进：定义区域级与肿瘤级不同单位→解释单区域样本排除→建立MFP/ssGSEA表达特征并离散化→模型训练/调参/评价→明确推断类别相对所取区域的含义→列独立队列与可用数据→正交病理的扫描/ROI/细胞分类→RNA/WES实验与计算处理→缺失标志物推断。每种验证回答不同问题，不能一句“validated”覆盖所有层级。

学到的Results段落推进：先给异质性频率和免疫程序梯度→报告单样本模型构建与内部性能→跨临床队列重现表达模式→独立模态病理支持→临床结局→传统PD-L1和MFP分类中的额外分辨→基因状态叠加。可迁移的组学结果写法是“模式重现—正交读出—原有类别内差异”，同时保留inferred和具体测量单位。

## PMID 42485106

文章：Utilizing machine learning to identify multimodal signatures for patients who would benefit from the addition of tremelimumab to durvalumab and chemotherapy (TRIDENT)。登记SHA-256：4844b3589ded1523689287e2216b87d50240e0ff44a9581c55c6e6972dfdffee；13个物理页。

重新阅读覆盖：p1全部摘要及Introduction，pp1–2完整Introduction和Translational Relevance；pp2–6全部Methods（data、HTE、super T-learner、aggregation、NCV、analyses、software）；pp6–8全部Results；pp8–10完整Discussion；pp10–11数据可用性/披露/贡献/致谢扫读；pp11–13参考文献扫读。所有主图注和表脚注已读。未独立读取补充Methods、S1–S11或其他补充资料。

实际视觉页：3、4、5、6、7、8、9。Figure 1 p3 HTE工作流；Figure 2 p4样本流失/模态可用性；Figure 3 p9各模型全部/模型排序子集及feature importance；Table 1 p6全部19模型NCV结果；Table 2 p8基线及missing footnotes。选句页：Methods p5三条；Results p7、p8。输出5条。

研究问题与设计：POSEIDON随机试验资料上的post hoc HTE建模，估计在共同durvalumab+chemotherapy背景上增加tremelimumab的24个月RMST CATE。不是该实验组合vs化疗单药的比较。974被纳入TRIDENT，但实际两治疗臂临床资料652、影像616、genomic557、全模态526；按组织学再分样本。genomic为基因层级变异编码，不是表达/蛋白/variant-specific机制测量。

建模证据链：可用性决定analysis set→clinical/genomic/radiomic预处理→KNN临床缺失填补→各治疗臂feature selection及生存模型→super T-learner CATE排序→模态特异模型post hoc Bayesian averaging→repeated stratified nested CV→相同分析集内modality ablation→permutation importance及partial dependence解释。学习重点是把同患者集内模态增量比较与跨数据可用人群差异分开。

负结果、边界：clinical+genomic再加radiomics未改善model13性能；鳞癌未建立有表现的signature。STK11只是多个重要模型特征之一，不构成独立基因治疗交互或机制。无独立external validation/test set，NCV是内部估计。文中某Methods叙述出现“on top of durvalumab versus chemotherapy”的措辞，与正式定义及图示对比不完全一致，本批不搬用该句，按公式和正文其余明确对比保留共同背景。单纯HR的跨模型比较受分析集不同影响，不能归因新增组学。重要性不是因果，也不必与单变量显著性一致。

学到的Methods段落推进：明确counterfactual estimand与治疗对比→说明每模态输入/可用性→预处理和缺失→feature selection与learner→模态aggregation→内部验证的内外层职责→同分析集fold匹配及ablation→置换重要性定义。Methods不是模型名堆砌，要交代每一步输入、输出和评估单位。

学到的Results段落推进：样本可用性及analysis sets→总体效应/特征相关性→模型比较和同组参照→模态增益或阴性结果→组织学限定→多变量feature importance。新模板专门保留“增加一个模态未改善”和“key variables according to feature importance”，避免把模型重要性写成单基因预测结论。

## PMID 42507545

文章：The genomic landscape and treatment outcomes associated with CDKN2A/MTAP loss in patients with non-small cell lung cancer。登记SHA-256：54b667455f7662b67a11643f6e741a7cdab3dac36965a549f956c578e89ddf7b；14个物理页。

重新阅读覆盖：p1全部摘要、Introduction开始；pp1–2完整Introduction与Translational Relevance；pp2–3、p5起始的Methods余句全部阅读；pp5–9全部Results；pp9–12完整Discussion及结论性段落；pp12–13数据/代码可用性、披露/贡献/致谢扫读；pp13–14参考文献扫读。全部6幅主图及图注已读；没有主表。未独立读取补充图S1–S10、补充表与代码。

实际视觉页：2、3、4、5、6、7、8、9、10、11。Figure 1 pp4–5筛选/clinicogenomic/9p地图；Figure 2 p6 AGA/共变异；Figure 3 p7 TTNT/BOR/校正；Figure 4 p8不一致缺失和TCGA/MYSTIC；Figure 5 p10缺失长度景观；Figure 6 p11按IFNK的临床结果。选句页：Methods p2一条、p3两条；Results p5两条、p9一条。输出6条。

研究问题与设计：用Tempus配对DNA xT与RNA xR资料描述9p21双基因/邻近基因缺失、行动性驱动、免疫状态与治疗结局，并用时间区分的Tempus数据、TCGA和MYSTIC作不同维度验证。主要genomic16,947，时间验证10,996；purity<40%及不一致CDKN2A/MTAP主分析排除；治疗结局还有单独可用性及风险集筛选。validation cohort没有因成熟度而纳入临床疗效分析，不能说所有临床终点都独立复现。

组学证据链：targeted DNA CN判读并定义CMdel/CMwt→邻位缺失、driver和histology context→whole-transcriptome xR表达→IFNK表达分位阈值（RNA surrogate）→quanTIseq immune fractions→Hallmark ssGSEA→缺失长度/相邻IFN基因→跨资料的基因组/临床验证。特别注意quanTIseq结果重新表达为各immune subset占所有immune cells（排除other）的比例，不是全部组织细胞百分比；低IFNK表达不是IFNK基因组缺失。

负结果、边界：KRAS热点间CMdel未明显不同，STK11/KEAP1共变异无差异；临床TTNT中ICI单药/TKI阴性，ICI+chemo经调整后变弱。扩大缺失并不自动呈更免疫抑制；广泛缺失较少、子组估计不精确。IFNK低表达也与其他基因状态相关，不能把免疫冷全部归因CMdel。主要RNAimmune/pathway图为正文引用补充S2/S8，选句本身已在正文视觉核对，但这些补充图未独立读。低纯度排除既改善CN判读又排除潜在免疫浸润高的样本，是可迁移的技术与生物选择边界。

学到的Methods段落推进：primary/temporal validation队列及排除→DNA CN与RNA平台实际范围→pathogenicity/AGA定义→IFNK阈值→临床结局单独分析集→PD-L1实测→RNA去卷积的算法和分母→per-sample基因集评分→其他验证队列→统计及left-truncation处理。要分别写测量、计算推断、分类规则与验证目标。

学到的Results段落推进：筛选/发生率→邻近基因和coalteration→现有行动性driver重叠→基因组、免疫构成、通路程序多层表型→时间验证→结局及校正→拆解局灶/广泛缺失→表达surrogate提供额外分层。句子本身可按“低PD-L1/TMB—低推断免疫细胞—免疫程序降低—增殖程序升高”的方向串联，仍只能表述association；不能据此从观察资料建立因果机制。

## Mechanical location follow-up

The final 90 new sentences were checked against fresh sorted and native-order PDF text. Sixty-seven matched after whitespace/line-break normalization; the remaining 23 were reopened by their respective source readers and visually confirmed without wording changes. The differences involved two-column extraction, manuscript line numbers, equals signs extracted as a fraction glyph, 5-prime/multiplication/plus glyph mappings, slash-separated terms split across lines, and genuine compound-word hyphens that a generic dehyphenation routine would remove. Mechanical mismatch was not treated as evidence that the sentence was absent or that its wording should be changed to extraction artifacts. The primary agent additionally inspected physical page 3 of PMID 39545922, page 11 of PMID 42456046, and page 5 of PMID 37733794.

The task-local source-text match report preserves the 67 mechanical matches and 23 mismatch observations separately from the readers' visual dispositions. All selected source sentences retain their actual visual verification status. No original-study result, method, cutoff, denominator, or software setting is supplied as a default when rendering a new user's sentence.
