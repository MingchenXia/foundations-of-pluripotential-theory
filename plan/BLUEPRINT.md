# 写作蓝图

## 目标与边界

从经典 potential theory 建立 pluripotential theory，把样本书实际依赖的基础定义、定理、技术、极限与几何背景放在自然位置，并给出完整证明。预设读者具备本科实分析（积分与收敛定理）、线性代数、点集拓扑和单复变基础；测度正则性、分布、泛函分析中实际使用的工具、复微分几何及相关 SCV 工具都需要补足。不能把“读者懂复几何”当作跳过证明的理由。

两部分：I. Potential theory；II. Pluripotential theory。附录处理复空间与明确的外部几何接口，末尾历史与书目说明。章节 ID 保持稳定，数字编号随正文自然生成。先写 P01–P06，再沿依赖图写复理论；不是照抄样本章节顺序。

## self-contained 的具体承诺

每个实际使用的结果都有完整证明、此前已证明的准确内部接口，或列在 `external-inputs.json` 的允许输入。resolution/principalization 是当前明确允许不展开长证明的输入，但需要精确陈述和核对来源。其他同类长结果逐项评估，不能把任意困难结果列入“标准事实”。Hörmander、OT、乘子理想 coherent/subadditive/strong openness、Siu、Bedford–Taylor、Demailly、Monge–Ampère mass monotonicity、能量/metric completeness、trace 等首先按证明义务规划。

若某个证明依赖章内稍后尚未完成的内容，记录 DAG 和缺口；不以“standard”封口。PSHD 的分布刻画不能循环依赖其自动上半连续性；先独立证明局部有界情形的分布刻画。其 Borel 选择工具也必须给出足够的自包含证明，或单独作为待决定输入，不能隐形假定。

## 样本的覆盖方式

基础从全部样本正文和附录抽取，不能只读 Part I。`sample-inventory.json` 保存每个 theorem-like statement、label、位置、citation 和嵌套输入；`SAMPLE_COVERAGE.md` 为每章分配自然归属。自动提取是建立待审队列，不证明每条 claim 正确。后续逐条标记 foundational / application / duplicate / external candidate，并对应新书 result label 与任务 ID。样本自有研究结果以基础接口或进阶篇章承接，不默认必须重写整部原书的全部研究结论。

## 新来源

PSHD：保留通常的 psh 定义，紧随其后证明 USC 冗余；不改动样本其它 conventions。前置证明 Borel 可测、uniform star energy、复超平面 L2 投影、incidence 和点态代表识别。Nakamaye：将 `lem:patching`、`lem:regularization` 放在 Q06，证明常数只依赖固定 (Z,omega_Z)；与样本 gentle/quasi-equisingular approximation 分开陈述。其 trace、rooftop、restricted volumes 和 relative principalization 给出对应基础；完整 Nakamaye 主定理作为可选应用，不扩大这次初始化的写作单位。

## 严谨性与发布

一个 coherent unit 的交付包括全部 recursive inputs、定义/结果/证明/例子、过渡、索引、参考来源，以及 first read、build/visual、second complete read、最终 affected build/visual。只有这些证据齐全才能设为 verified。最后通读检查 circular references、符号首次出现、dimension-zero、共同极点、empty envelopes、limit topology、uniform constants、background scope 和真实 open problems。

排版沿用样本。书目使用一个 `ComplexGeometry.bib`，保留原键；新增元数据只在核对后追加。数学正文给确切依赖，历史章给精确归属，不写工作进度或 AI 审计语言。源码与 PDF 仅留在私有仓库/私有 Actions artifacts，公开发布另需作者指令。

当前范围：初始化工程、来源保全、结构/依赖蓝图和首个写作任务。任何“verified=0”是诚实的书稿进度，不是工程未配置。
