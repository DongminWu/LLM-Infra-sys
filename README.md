# LLM-AI-Infra-system好文分享 (文章标题是链接可以点击)

## 202509

## [性能暴涨50%:PD分离KV cache传输的实战干货](https://mp.weixin.qq.com/s/s-UapW7XsO8RmH7mmqSDaw)

在LLM推理的PD（Prefill-Decode）分离场景中，高效传输键值缓存（KV Cache）是提升整体性能的关键。本文介绍了基于vLLM框架开发的​​KV Cache传输connector​​，通过优化传输机制，实现了​​传输性能提升0.5倍​​，相关代码已全面开源。
文章系统分析了KV Cache传输中的核心挑战，包括​​异构传输​​（如MLA与GQA/MHA结构差异）、​​内存对齐要求​​、​​传输聚合策略​​及与vLLM调度器的深度协同。针对Ascend 910B硬件环境，团队设计了基于​​RDMA​​的高效传输方案，并集成至Mooncake传输引擎（TE），显著提高了带宽利用率和传输可靠性。
此外，本文探讨了进一步优化方向，如​​分层传输（Layer-wise Strategy）​​、​​异构拓扑下的广播优化​​、​​传输-计算流水线设计​​等，为LLM分布式推理中的数据传输提供了重要实践参考和理论支撑。

[ppppp](https://github.com/user-attachments/files/22303607/KV%2BCache.Ascend.mp3)
<audio controls="">
  <source src="https://github.com/user-attachments/files/22303607/KV%2BCache.Ascend.mp3" type="audio/mp3" />
</audio>


## [PyTorch torch.compile 训练编译技术现状与展望（2025年8月）](https://mp.weixin.qq.com/s/cNTkNZyyETQrHDDYdSSyvw)

本文系统综述了 PyTorch torch.compile 在训练场景，特别是自动并行领域的最新进展与未来方向。作为 PyTorch 的核心编译技术，torch.compile 通过即时编译（JIT）实现训练性能 1.5–2 倍提升，并支持包括自动激活检查点（Automatic Activation Checkpointing） 和异步张量并行（Async Tensor Parallelism） 在内的全局内存与通信优化。

文章重点对比了 PyTorch 与 JAX 在分布式编译路径上的根本差异：JAX 以 XLA 为核心、编译优先，而 PyTorch 坚持用户体验优先，从全手动模式逐步引入自动化机制。DTensor 作为核心分布式抽象，支持 SPMD 风格的张量分片与自动微分，并与 FSDP2、AutoParallel 等生态深度集成，是实现自动并行的基础。

当前，torch.compile 已支持多种图捕获机制（包括 make_fx 和 symbolic_trace），并依托 Inductor 编译器后端实现算子融合、动态代码生成与 CUDA Graphs 集成。此外，诸如 Flex Attention、FP8 训练优化等功能也极大丰富了模型开发与部署的能力。

尽管在动态形状、编译时间与跨秩一致性方面仍存在挑战，PyTorch 团队正积极推进预编译（AOTInductor） 与统一运行时，旨在为超大规模训练提供稳定、高效的编译解决方案。本文为研究者与工程师理解 PyTorch 编译技术栈提供了系统且前沿的参考。

<audio controls>
  <source src="https://github.com/user-attachments/files/22303609/PyTorch%2B.%2Btorch.compile%2B.mp3" type="audio/mp3">
</audio>


## [高级矩阵乘法在NVIDIA GPU上的优化](https://mp.weixin.qq.com/s/IvnvHkWogIrWMjV8j-kZPw)

本文系统阐述了在NVIDIA GPU架构上实现高性能单精度矩阵乘法（SGEMM）的优化方法与关键技术。SGEMM作为科学计算与深度学习的核心运算，其高效实现对提升计算性能至关重要。现有的教育性实现通常难以达到工业级库（如cuBLAS）的性能水平，而高性能实现又缺乏足够的可解释性。

本研究以CUTLASS算法设计为基础，深入探讨了在CUDA环境中通过**内联PTX汇编**、**异步内存拷贝**、**双缓冲**机制、**共享内存优化**及**向量化内存访问**等多项关键技术，显著提升计算效率。特别针对NVIDIA RTX 3090（GA102芯片）进行细致调优，在实现过程中注重避免存储体冲突与实现合并存储。

实验结果表明，在锁定频率和未锁定频率两种条件下，所提出的实现方案在多种矩阵规模下均表现出优于或接近cuBLAS的**性能表现**，尤其在较大矩阵乘法中显示出良好的扩展性与稳定性。本文不仅提供了详实的实现细节，还为CU学习者理解高性能SGEMM实现提供了清晰的技术路径与优化思路。


<audio controls>
  <source src="https://github.com/user-attachments/files/22303611/%2BCUDA%2BSGEMM%2B.mp3" type="audio/mp3">
</audio>

## [简单聊聊 NVIDIA 最新的 Vera Rubin NVL144 CPX 系统](https://mp.weixin.qq.com/s/f-3RLqe-m_g6NY8JmT5ksg)
近年来，大语言模型（LLM）推理过程中的**Prefill阶段**（计算密集型）和**Decoding阶段**（存储带宽密集型）表现出显著不同的性能特征，推动了对**分离式推理（PD分离）** 系统的需求。为优化系统效率与成本，NVIDIA最新推出了专为Prefill阶段设计的**Rubin CPX GPU**，采用成本较低的**GDDR7显存**，提供30 PFLOPS的FP4算力及2 TB/s的显存带宽，显著提升了大上下文推理任务的性价比。

与之配套，NVIDIA提出两种系统级解决方案：**Vera Rubin NVL144 CPX Rack** 和 **Vera Rubin CPX Dual Rack**。前者为高集成度单机架系统，整合144个Rubin CPX GPU与72个标准Rubin GPU（配备HBM4），总算力达8 EFLOPS FP4，显存总带宽约1.2 PB/s；后者采用双机架配置，提供相等的算力与更高的扩展灵活性。两者均依托**Vera CPU**和高速**NVLink-C2C**互连，实现CPU与GPU间的高带宽通信。

目前公开数据中存在部分未明确的细节，如系统级存储带宽（官方标注为1.7 PB/s）的计算方式、**NVLink7**的实际带宽，以及Vera CPU与Rubin CPX GPU之间的互联支持等。这些系统在集成度、网络成本、故障率和部署灵活性方面各有优势，适合不同规模的推理负载需求。

该项发展标志着GPU架构正朝着更精细化负载优化的方向发展，特别是在支持超长上下文推理场景中，体现出重要的工程与架构创新。


<audio controls>
  <source src="https://github.com/user-attachments/files/22303612/NVIDIA%2B.%2BVera%2BRubin%2BNVL144%2BCPX%2B.mp3" type="audio/mp3">
</audio>

## [华为Fellow廖恒博士Hot Chips 2025演讲：UB-Mesh超节点互联架构详解（视频+演讲实录）](https://mp.weixin.qq.com/s/cGsc5ZEa3lLOCLV2TSisrg)

**华为UB-Mesh超节点互联架构：面向大规模AI训练的高效互连方案**  

在AI训练集群向超大规模、高带宽、低成本和强可靠性发展的背景下，华为提出**UB-Mesh超节点互联架构**，通过**统一总线协议（Unified Bus, UB）** 和**层次化多维全互联拓扑**，显著提升系统性能与经济性。该架构支持从单机架到百万级处理器规模的灵活扩展，尤其适用于千兆瓦级AI数据中心。  

UB-Mesh的核心创新包括：  
1. **拓扑优化**：采用**多维Full-Mesh直连结构**，通过局部高带宽域（如板内、机架内）与全局低带宽收敛域的结合，降低物理部署成本，相比传统Clos架构，在4000节点规模下可实现**5倍成本节约**。  
2. **协议统一**：基于**UB协议**原生兼容以太网，支持多类型设备（GPU、CPU、内存池、SSD等）的直接负载/存储访问，消除协议转换开销，降低延迟并提升资源利用率。  
3. **光链路容错**：针对光链路误码率高、易闪烁的问题，设计**链路级重试机制**和**交叉路由方案**，实现零丢包传输，将系统平均无故障时间（MTBF）提升百倍。  
4. **分层容灾**：引入**节点级与机架级冗余备份**，通过备用芯片和机架的动态切换，将百万芯片集群的故障修复窗口从1小时延长至1个月，大幅增强系统弹性。  

该架构已应用于实际产品，支持单机架64节点至超节点8192芯片的灵活组网，为未来万亿参数AI模型训练提供底层支撑。相关工作详情可参考华为在Arxiv.org发布的论文。  

随着大语言模型（LLM）技术的快速发展，​​高效推理部署​​成为连接模型与实际应用的核心环节。本文系统梳理了当前主流的大模型推理框架，包括 ​​vLLM​​、​​SGLang​​、​​TensorRT-LLM​​、​​Ollama​​、​​XInference​​ 及 ​​LightLLM​​ 等，从核心技术、架构设计、性能指标和适用场景等多维度进行深入分析。

<audio controls>
  <source src="https://github.com/user-attachments/files/22303619/%2BUB-Mesh%2B.mp3" type="audio/mp3">
</audio>

## [一文梳理主流大模型推理部署框架：vLLM、SGLang、TensorRT-LLM、ollama、XInference](https://mp.weixin.qq.com/s/Fsaz7PAUSiKizl_lw-KSeg)

​​vLLM​​ 通过 ​​PagedAttention​​ 和 ​​连续批处理（Continuous Batching）​​ 显著提升显存利用率和吞吐量，适用于企业级高并发场景。​​SGLang​​ 基于 ​​RadixAttention​​ 实现前缀复用和结构化输出，在高吞吐和多轮对话任务中表现突出。​​TensorRT-LLM​​ 依托 NVIDIA 硬件深度优化，在低延迟场景中性能卓越。​​Ollama​​ 以轻量化和跨平台特性适合本地开发与快速原型验证。​​XInference​​ 和 ​​LightLLM​​ 则专注于分布式推理和边缘计算部署，支持国产硬件与多模态任务。

本文为不同业务需求（如实时响应、高吞吐、资源受限环境或国产化部署）提供选型参考，旨在推动大模型技术的高效落地与应用创新。

<audio controls>
  <source src="https://github.com/user-attachments/files/22303621/online-audio-converter.com.mp3" type="audio/mp3">
</audio>


## [打破瓶颈，让RAG学会思考：中科大、智源等发布推理检索框架BGE-Reasoner](https://mp.weixin.qq.com/s/hDBJ998nc9kO6vnTpx9exA)

随着 RAG 和 AI Agent 技术的快速发展，**推理密集型信息检索（Reasoning-Intensive IR）** 成为制约大模型智能体与深度研究应用的核心挑战。该类任务需综合多步逻辑推理、语义链与背景知识，传统检索方法在复杂查询下表现显著不足。为此，中国科学技术大学、智源研究院等机构联合提出 **BGE-Reasoner**，一套创新的端到端解决方案，在权威基准 **BRIGHT** 上以 **45.2** 的得分刷新纪录，领先原最优结果 **3.6 分**。

BGE-Reasoner 的核心创新体现为三方面：  
1. **模块化框架设计**：提出由 **Rewriter**（查询理解与改写）、**Embedder**（向量检索）与 **Reranker**（重排序）构成的三阶段流程，显著提升复杂查询的处理能力；  
2. **合成数据驱动**：基于大模型生成多领域高质量推理训练数据，有效解决数据稀缺问题；  
3. **强化学习优化**：在 Reranker 训练中引入强化学习，增强模型对困难样本的推理与泛化能力。  

此外，BGE-Reasoner 的嵌入模型 **BGE-Reasoner-Embed** 在 BRIGHT 基准下同样达到最优性能，超越 Seed1.5-Embedding、Qwen3-Embedding 等基线模型。该研究不仅提供了性能领先的检索系统，更为推理密集型任务提供了可复制的技术范式。相关模型、代码与数据将开源，推动领域进一步发展。

<audio controls>
  <source src="https://github.com/user-attachments/files/22303533/BGERAG.mp3" type="audio/mp3">
</audio>

