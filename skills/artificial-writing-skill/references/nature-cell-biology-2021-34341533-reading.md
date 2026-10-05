# PMID 34341533 — LKB1/SIK、染色质状态与转移阶段依赖性

## 身份、版本与实际阅读边界

Pierce SE, Granja JM, Corces MR, et al. **LKB1 inactivation modulates chromatin accessibility to drive metastatic progression**. Nature Cell Biology. 2021;23(8):915–924. DOI [10.1038/s41556-021-00728-4](https://doi.org/10.1038/s41556-021-00728-4)；[PMID34341533](https://pubmed.ncbi.nlm.nih.gov/34341533/)。本地是author manuscript，46物理页；PMC available date2022-02-02不是发表日期。

来源 `nihms-1725816.pdf`；8,219,478 bytes；SHA-256 `bb29824252c1e7caf63fbf87b8ada507c034c1533bb936fd8892f8a461388ba8`。阅读者Codex /root/intake_registry_audit，2026-10-02。主文、Methods、Fig1–6及全部图注、内嵌Extended Data Fig1–10及图注全部阅读；16张科学图逐图视觉核查。References/admin surveyed。外部Supplementary Information、Supplementary Tables1–6、Source Data及原始数据文件未提供，不能声称已核阅。

`reading_stage=main_text_deep_read_complete`；`review_status=not_reviewed`。内嵌Extended Data完整覆盖；外部补充资料仍缺失。本记录仅整理非操作性科学证据、图表、统计、限制与写作语言，不记录实验配方、剂量、基因改造步骤、移植操作或可执行流程。

## 研究问题与论证结构

研究的是同一驱动基因异常为何能在原发与转移阶段对应不同细胞状态。作者将LKB1功能模型、增殖筛选、原始bulk RNA/ATAC、原始小鼠scATAC、既往人类ATAC/scRNA资料与组织学证据结合，提出两阶段的表观遗传重塑框架。

1. LKB1状态变化伴随大范围染色质可及性改变；遗传比较指向SIK家族的集体作用，AMPK等家族在此测定中不是同等必需因子。
2. 人类21例原发LUAD和8条细胞系提供跨体系一致性，不等于临床分类器验证。
3. 共同Kras/Trp53背景的小鼠原发瘤与转移瘤比较提示LKB1缺失相关状态具有阶段特异性；原发瘤和转移瘤的差别不能只用是否STK11异常概括。
4. SOX17相关状态在部分LKB1缺失原发瘤中已出现，并在所观察的LKB1缺失转移瘤中富集。scATAC识别的是“metastatic-like”状态，不是直接谱系追踪证明这些细胞实际播散。
5. 功能证据支持SOX17对特定染色质状态和模型转移表型的作用；不等于SOX17单独解释全部转移步骤，或构成已经验证的临床靶点。

## 全文与内嵌扩展图覆盖

| 单元 | 物理页 | 核查的证据内容 |
|---|---|---|
| Abstract / Introduction | 1–2 | 基因型与阶段依赖性问题；无独立Translational Relevance |
| Results | 2–8 | 恢复模型、筛选、SIK、人类一致性、原发/转移状态、SOX17关联与功能 |
| Discussion / closing synthesis | 8–9 | 两波重塑、未知第二信号、早期转移样状态；无独立Conclusion |
| Materials and Methods | 9–18 | 研究体系、原始/再分析来源、重复单位、组学统计与偏倚说明；不转录操作流程 |
| Fig1 | 36–37 | 筛选rank/FDR、31,248差异峰、SIK与其他家族对比、技术重复 |
| Fig2 | 38 | TCGA21例、13/8分型、TEAD/SOX、8人细胞系；图注轴/显著性冲突 |
| Fig3 | 39–40 | 25原发瘤分型、9转移瘤、NKX2与SOX状态、位点可及性 |
| Fig4 | 41–42 | 组织学、7原发瘤scATAC、14,413 nuclei、12簇、cluster12与footprints |
| Fig5 | 43–44 | RNA/ATAC共同指向SOX17、扰动与回补的证据逻辑；非全基因组单一路径 |
| Fig6 | 45–46 | 肺部负荷与从局部瘤播散的区别；局部瘤大小阴性；整合模型 |
| Extended Data1 | 19–20 | LKB1蛋白/转录验证、可恢复与不可恢复对照、增殖和筛选相关性；panel l有图但缺单独图注 |
| Extended Data2 | 21–22 | ATAC QC、178,783峰、可恢复/不可恢复对照、时间趋势 |
| Extended Data3 | 22–23 | 染色质因子缺失仅延迟而非完全阻断变化，非单一必需介质结论 |
| Extended Data4 | 23–24 | SIK家族冗余、独立比较一致性、各单个成员阴性 |
| Extended Data5 | 25 | STK11人类富集FDR=.088、其他motif、13/8样本 |
| Extended Data6 | 26–27 | 8细胞系、FOXA边缘结果、LKB1功能评分关联、KEAP1对照 |
| Extended Data7 | 27–28 | 自发模型结局、2/7对7/7转移、原发瘤数/肺重阴性、SOX/NKX2比较 |
| Extended Data8 | 29–30 | IHC分母117/203/14/8、人类10例再分析、R=−.81 |
| Extended Data9 | 30–31 | 单细胞QC、样本来源、cluster12构成、bulk与scATAC一致性及计数/对比标注冲突 |
| Extended Data10 | 31–32 | SOX17表达/蛋白/可及性、肺重验证、肝终点P=.055 |
| Data availability / references | 33–35 | GSE167381、TCGA来源、已有文献/代码引用；未实际复算原始数据 |

## 中心结果与样本单位

| 证据层 | 数值及关键结果 | 解释边界 |
|---|---|---|
| 筛选 | 六个染色质相关基因位于top20；Fig1b列Lkb1第1、Suv39h1第6、Arid1a第7、Eed第10、Suz12第13、Trim28第15、Smarce1第20 | 不是六者均FDR<.01，见警示；筛选为增殖表型而非转移直接筛选 |
| 原始ATAC | ED2d：178,783峰中LKB1恢复相关增加14,684、减少16,564，总31,248；不可恢复对照增加118、减少15 | 差异阈值为|log2FC|>.5及FDR<.05；峰不是基因，更不是同数目直接靶点 |
| SIK轴 | 家族集体功能变化显著影响LKB1相关可及性；单个SIK成员及AMPK/NUAK/MARK家族在所示比较中未造成同等阻断 | Fig1/ED4；技术重复通常n=2；不能推广为所有LKB1生物学均与AMPK无关 |
| 染色质因子 | EED/SUZ12/TRIM28/SUV39H1等比较显示状态转换延迟，但最终改变未完全消失 | ED3；不将筛选hit写成全部必要下游 |
| 人原发LUAD | TCGA ATAC共21；Chromatin Type1 n13，Type2 n8；STK11富集FDR=.088 | p4/ED5；相对最强富集不等于FDR<.05，不是临床分型准确率 |
| 人细胞系 | 8条细胞系，LKB1状态与可及性分层一致；功能缺失表达评分与变化规模R=.96；KEAP1对照变化较小 | ED6；不同细胞系还存在其他遗传差异；FOXA组间P=.066不能写显著P<.05 |
| 自发模型bulk | KPT原发12、LKB1缺失原发13、KPT转移4、缺失转移5 | p5/Fig3；样本为肿瘤，不将技术重复或多瘤当独立小鼠；共同Kras/Trp53背景 |
| 自发转移频率 | KPT2/7与LKB1缺失7/7，作者one-sided binomial P=.00016 | ED7；保留原检验，不误写Fisher或随机临床效应；肺重/原发瘤数比较未显著 |
| SOX17组织学 | LKB1缺失原发203中63存在SOX17+亚群，约31%；缺失转移8/8存在；KPT原发117和转移14均未见相同阳性 | p6/ED8；分母为组织样本，不能声称所有STK11患者转移瘤必阳性 |
| 人类scRNA再分析 | 10例含所选转移细胞簇的LUAD样本，供者均值SOX17与STK11表达R=−.81 | ED8c/Methods14–15；外部Laughney2020再分析，不是10例新测定或单细胞之间的独立相关 |
| 原始scATAC | 4 KPT原发8,392 nuclei；3缺失原发6,021 nuclei；合计14,413、12簇 | Fig4；7瘤不是14,413独立生物学重复；非同一细胞RNA+ATAC multiome |
| cluster12 | SOX17邻近高可及性/NKX2.1低可及性；主要来自同一mouse13的13A/13B两瘤 | p6/Fig4/ED9；n112与n116冲突，不给确定频率；“转移样”不是直接祖先谱系证据 |
| 肺负荷功能终点 | Fig6c：两项SOX17比较P=.0031/.0072；另一背景比较P=.0031；参考组n3，其余各n4小鼠 | 非生存研究；归一化肿瘤面积不是患者ORR，不从柱高臆造精确效应量 |
| 局部瘤与播散 | Fig6f每组4鼠、各2局部瘤；SOX17相关比较的局部瘤大小未显著，肺表面病灶P=.0471 | 不能把8局部瘤当8独立小鼠；肺部播散改变不等于普遍加快局部生长 |
| 肝终点阴性边界 | ED10k对照n9、比较组n8；P=.055 | 数值趋势未达常用.05标准，不写“显著促进肝转移” |

图中可及性、motif deviation和footprint并非直接TF结合的同义词；结合表达、遗传比较及回补后才形成更强功能支持。肿瘤负荷与metastatic-like细胞状态不转换为患者OS、免疫治疗耐药或疗效预测。人类数据主要为支持性再分析，功能结论主要来自细胞和小鼠。

## 原文疑点、统计与可迁移上限

1. **筛选FDR冲突**：Fig1b图注称六个染色质基因FDR<.01；图内Suz12=.0354、Trim28=.0571、Smarce1=.0804。安全结论是top20中含六个染色质相关基因，不能说六个均通过.01或.05门槛。
2. **人类突变富集**：STK11 FDR=.088；“最显著”是相对排名，不是通过常用.05阈值。Methods描述以TCGA230例背景频率作binomial enrichment，与ED5图注“Type2 vsType1”简化措辞不同；不编造直接两组Fisher检验。
3. **cluster12计数和比较范围**：正文p6写112cells，ED9图注p31写116且漏列cluster10；ED9d图注写cluster12 vs1–11，图中轴写vs6–11。均保留冲突，不补造统一细胞比例或确切比较集合。
4. **随机化说明冲突**：特定allograft描述p12有randomized，p18总括写实验未随机化；同时说明未正式盲法、未用统计方法预定样本量。不宣称整体随机/盲法设计或假定全部动物比较都随机。
5. **图注阈值与定位问题**：Fig2c的TEAD精确P=9×10−6与四星定义P<10−6不一致，优先保留精确值及定位，不套通用星号；Fig2b图注把两个轴均称x-axis，实际图为人类x、鼠y。Fig5d的full heatmap指ED7f，但对应图在ED10f。正文p7部分ED10面板引用也与当前排列不符，以可见图内容与图注定位，不盲从交叉引用。
6. **测定上限**：“SOX17+”组织学与scATAC基因体可及性不是同一测定；metastatic-like cluster没有直接原位谱系追踪证明。TF motif跨家族共享，单独motif富集不等于直接、唯一SOX17结合。
7. **模型上限**：模型包含Kras/Trp53背景；移植功能终点来自免疫缺陷动物，不用于证明免疫逃逸或ICI耐药。不同播散模型覆盖的转移环节不同，不合并为完整自然转移全过程。
8. **未解问题**：并非所有LKB1缺失细胞表达SOX17；触发后续状态的第二信号未知。SIK与classIIaHDAC可能的联系属于讨论假说，本文没有直接建立完整中介链。KEAP1在所测细胞系中的对照不能否定KEAP1所有表观遗传作用。
9. **补充范围**：内嵌ED1–10已读，但外部Supplementary Tables1–6、additional ATAC-analysis information和Source Data未读；GSE167381是存储标识，不等于本次下载/重分析。已有scRNA使用Laughney2020，不能把此人类队列记作本研究新招募。

统计报告以unpaired t-test、图示FDR/q阈值、binomial enrichment、Pearson相关与mean±SEM为主；多个细胞实验为technical duplicates，动物或肿瘤才是对应生物学单位。确切数值未报告时不从图像估算CI、HR或生存中位数。无患者干预、无已验证临床预测工具、无用药建议。

## 分类与STK11专题支持

- `stk11_relation=direct_function`；次级`direct_mutation`。不是仅标题提及LKB1。
- 主类别：阶段依赖的表观遗传重塑与转移相关细胞状态；主场景LUAD/Kras-Trp53背景，跨人鼠证据。
- 原始模态：bulk ATAC、single-cell ATAC、bulk RNA、遗传功能比较、蛋白/组织学；再分析模态：TCGA bulk ATAC和已发表人类scRNA。不是原始人类scRNA、空间转录组、全蛋白组或直接单细胞多组学联测。
- 治疗分类：无治疗干预试验；遗传机制研究，不将实验性调控工具归作抗癌药物方案。
- 可用模块：epigenetic_state、metastatic_progression、sequence_context、single_cell_state。归入专题支持，不自动提升为用户定义核心精选。
- 最强稳妥结论：LKB1缺失相关染色质状态在肺癌进展中具有阶段差异；SOX17关联的后续状态受到模型功能证据支持，但人类预测效用和完整分子中介链尚未确立。

## Section-language curation

以下术语为短常规表达，句架和段落架为重新抽象的合成模型；定位支持概念而非声称逐字原句。不得迁移为实验操作或扩大为人体疗效结论。

| ID | Section | Unit | Expression / synthetic frame | 用途与约束；来源定位 |
|---|---|---|---|---|
| NCB01 | Abstract | vocabulary | chromatin accessibility | 染色质可及性，不等于RNA或直接结合；pp1–4/Fig1 |
| NCB02 | Abstract | sentence-frame | The association between [driver alteration] and [cell state] differed across [disease stages] in the studied models. | 限定模型与阶段，非普遍规律；pp1–2,8–9 |
| NCB03 | Introduction | collocation | stage-specific regulatory programs | 进展阶段依赖的调控问题；p2 |
| NCB04 | Introduction | paragraph-frame | Describe [shared genotype]; contrast [stage-dependent phenotype]; identify the unresolved contribution of [regulatory state]. | 不假设观察差异必然来自新突变；p2 |
| NCB05 | Methods | vocabulary | technical replicates | 与独立生物学样本分开；Fig1,5/ED4 |
| NCB06 | Methods | collocation | donor-level expression summary | 人scRNA为供者均值，不把细胞作供者；pp14–15/ED8 |
| NCB07 | Methods | sentence-frame | Data from [original assay] were analyzed alongside [published dataset], with the two evidence sources distinguished. | 标明原始scATAC与既往scRNA；pp14–18 |
| NCB08 | Methods | sentence-frame | The analysis included [number] tumors from [number] animals; technical measurements were not counted as independent samples. | 只填真实独立分母；Fig3–4 |
| NCB09 | Results | collocation | metastasis-associated chromatin state | 关联状态，不代表已追踪转移祖细胞；pp5–7 |
| NCB10 | Results | sentence-frame | A rare subset shared [features] with [reference state], consistent with a [state-like] phenotype rather than demonstrated lineage ancestry. | 保留谱系证据缺口；Fig4/ED9 |
| NCB11 | Results | sentence-frame | The endpoint differed in [comparison], whereas [related endpoint] did not show a statistically significant difference. | 可描述播散与局部瘤大小差别；Fig6f |
| NCB12 | Results | sentence-frame | The ranked association had an FDR of [value] and did not meet the specified [threshold]. | 排名不替代显著性；p4/ED5 |
| NCB13 | Figure legend | sentence-frame | Each point represents [biological unit]; repeated measurements and technical replicates are described separately. | 明确mouse/tumor/nucleus；Fig4–6 |
| NCB14 | Discussion | collocation | context-dependent epigenetic remodeling | 染色质状态不直接转临床预测；pp8–9 |
| NCB15 | Discussion | sentence-frame | The findings support a role for [regulator] in [model-specific phenotype], but do not identify the upstream signal that initiates the state transition. | 第二信号未知；p8 |
| NCB16 | Discussion | paragraph-frame | Integrate [functional evidence] with [human association]; retain [negative result]; delimit [model and validation gaps]. | 人鼠层级不混合，保留P=.055；pp8–9/ED10 |
| NCB17 | Conclusion | sentence-frame | These findings define a model-supported regulatory relationship whose clinical predictive value remains to be established. | closing synthesis，非临床实施建议；p9 |

安全迁移示例（合成）：`A SOX17-associated chromatin state was observed in a subset of LKB1-deficient primary tumors and was supported by functional evidence in experimental models; the study did not establish a clinically validated metastasis predictor.`
禁止迁移：`All STK11-mutant cancers inevitably activate SOX17 and can be clinically managed by targeting this pathway.`
