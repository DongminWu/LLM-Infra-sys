# LLM-AI-Infra-system好文分享 (文章标题是链接可以点击)


## 202511

## [Kimi最新的KimiLinear技术亮点是什么？一起来看下](https://mp.weixin.qq.com/s?__biz=MzYyMjA5NzMwOQ==&mid=2247485745&idx=1&sn=3763b72b5bfb05f8dcec02f2c38ae8b0&chksm=fea43da56d00d4e52c13a1b6ab8af128f5ac24839da11bbb0884ac7c0774fddb72c79cc03e93&mpshare=1&scene=1&srcid=1103STYR0YREZY4TdUrofNBw&sharer_shareinfo=4d4b9ac6e960bf61712271087482ec1a&sharer_shareinfo_first=4d4b9ac6e960bf61712271087482ec1a#rd)

Kimi最新推出的KimiLinear技术核心在于KDA（Kimi Delta Attention）模块，通过将传统线性注意力中的单一衰减因子α扩展为与隐藏维度dk对应的对角化多α矩阵，实现对状态记忆的精细化衰减控制，显著提升长序列建模能力。该技术融合Gated Delta Networks架构，并与MLA以1:3比例混合使用，兼顾效率与性能。其创新在于突破了线性注意力中全局统一衰减的局限，同时保持O(L)计算复杂度，为超长上下文推理提供高效解决方案，代表了Attention机制向状态空间模型演进的重要实践。


## [KV cache池化传输会比重算更快吗？一起算一算](https://mp.weixin.qq.com/s?__biz=MzYyMjA5NzMwOQ==&mid=2247485425&idx=1&sn=4043737cca93af32847367626977cd3b&chksm=fe239d4145e887d9057f6530dda3b40536304ae2aa18cbbece21f1e9b0f1aef7da63faac48d4&mpshare=1&scene=1&srcid=1027EwvUx9qYUT9AzsQNFTJ7&sharer_shareinfo=385013e3ce82c6a072d8383c97952ac0&sharer_shareinfo_first=385013e3ce82c6a072d8383c97952ac0#rd)

本文通过理论建模与多场景计算，系统分析了KV cache池化传输与重计算的性能权衡。研究表明：在高带宽（如NVLink）和算力密集型模型（如DeepSeekV3）下，池化传输更优；但在低带宽（<1GB/s）或存储密集型模型（如GQA）中，重计算更具优势。文章量化了传输带宽、GPU算力、序列长度、通信链路（D2D/H2D/RDMA等）及模型结构对延迟的影响，并指出实际部署需综合考虑软件调度开销与硬件配置，建议采用自适应策略动态选择方案，避免通信与集合通信冲突。


## [阿里云秘密武器亮相顶会：狂砍82%英伟达含量，213块GPU干了1192块的活](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247834923&idx=2&sn=aa053bff8bce65699f1b554650b49ce8&chksm=e92f7e003fc4317936bf36da16c44371749ced9dc52198318dc2575446192ade14c01c753360&mpshare=1&scene=1&srcid=1022vlu5iNn1tq0dsn5OWpy0&sharer_shareinfo=b56ed76a919e802e88f9078cfcf98ced&sharer_shareinfo_first=b56ed76a919e802e88f9078cfcf98ced#rd)

阿里云联合北京大学在SOSP顶会上发布新型GPU池化系统Aegaeon，通过token级动态调度技术，将GPU需求从1192块降至213块，削减82%英伟达GPU用量。系统突破传统请求级调度限制，实现单GPU并行服务7个模型，结合组件复用、显存管理与KV缓存同步等优化，将扩缩容开销降低97%，吞吐量提升1.5–9倍。在阿里云百炼平台实测中，GPU利用率从13.3%–33.9%提升至48.1%，服务47个模型无SLO违规，显著提升长尾模型资源效率，为大模型服务提供高性价比新范式。


## [SGLang × RoleBasedGroup（RBG）：打通大模型推理PD分离架构规模化落地的“最后一公里”](https://mp.weixin.qq.com/s?__biz=MjM5MDE0Mjc4MA==&mid=2651256455&idx=2&sn=bb66bf6cd3f113924ab94e8975601948&chksm=bc52bfb3b094284699955426f3995ab14764176f7b1211f699b3ad918e813775f39d36281e90&mpshare=1&scene=1&srcid=1020JNia0BzJCbrOnk6ipY86&sharer_shareinfo=5efe6d758f880ad05f745e31e8871a5f&sharer_shareinfo_first=5efe6d758f880ad05f745e31e8871a5f#rd)

SGLang与RoleBasedGroup（RBG）协同推出大模型PD分离架构的生产级落地解决方案。PD分离通过解耦预填充（Prefill）与解码（Decode）阶段，显著提升吞吐与资源利用率，但其状态依赖性导致Kubernetes环境部署复杂、弹性困难、故障恢复低效。RBG作为轻量级K8s原生编排框架，以“角色组”抽象多角色服务，支持声明式拓扑、原地升级、优雅扩缩容与智能故障恢复，无缝集成SGLang等推理引擎，解决KVCache管理、服务发现、级联故障等核心运维难题，使性能提升从实验室走向稳定生产，填补了大模型推理云原生化“最后一公里”空白。


## [理解大模型推理中的KV Cache](https://mp.weixin.qq.com/s?__biz=MzI0NjQzMjk0MA==&mid=2247483861&idx=1&sn=0638f63459988d66462e2ab7fe7b825e&chksm=e832f2b5f72ff25608bf2ace9d0301a6d1bd87975ffe27016b885d4ec7fccd8ac5d6a953cf4c&mpshare=1&scene=1&srcid=1019Oe3YANAK9xn6qAMBWr4K&sharer_shareinfo=fb4df97c413edc0b987b64eb8936637f&sharer_shareinfo_first=fb4df97c413edc0b987b64eb8936637f#rd)

KV Cache是提升大语言模型推理效率的关键技术，其核心源于因果解码器的自回归特性与因果掩码机制。在Prefill阶段，模型并行计算输入序列的所有Key和Value并缓存；在Decode阶段，仅需计算新生成token的Query，复用缓存的历史K/V，避免重复计算，使注意力计算复杂度从O(n²)降至O(n)。该机制显著降低计算开销，成为LLM推理优化的基础。为进一步提升资源利用率，工业界常采用Prefill与Decode阶段分离部署，需跨服务器传输KV Cache，带来新的系统设计挑战。


## [聊聊大模型推理系统之RServe如何实现66%延迟降低与109%吞吐提升？](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA==&mid=2247547073&idx=1&sn=85e2f9d508894676c02691017475fdcf&chksm=cf645525f485c95c752682a65e91134037780bfc1f12056feefeae578c2201ab426d858c4032&mpshare=1&scene=1&srcid=101519AAqKp1QiEVOfpKm2V2&sharer_shareinfo=70bb2c072f2ea583f670f14beaf770f8&sharer_shareinfo_first=70bb2c072f2ea583f670f14beaf770f8#rd)

中山大学与小红书团队提出RServe，一种面向多模态大模型（LMM）的高效推理系统，通过“嵌入追踪器”与“可调度令牌”机制，首次实现请求内编码与语言模型prefill的细粒度流水线重叠，以及请求间动态批处理协同调度。在Qwen2.5-VL-72B模型上，RServe相较vLLM和gLLM将首令牌延迟降低66%、吞吐提升109%，且兼容Tensor/Pipeline并行，不损失模型精度。该系统突破传统EPD串行架构，显著提升多模态AI服务的实时性与资源利用率，为智能客服、视觉问答等低延迟场景提供通用推理底座。


## [万字长文｜大语言模型结构化输出（Structured Output）的技术原理和实现](https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247553794&idx=1&sn=4d87268b65f2c1a968861d54731515fb&chksm=e8e24a20978d8df38711b109526e0f08718fceffafb9d488c4717268c276d82b25277c265ef2&mpshare=1&scene=1&srcid=10157BC7JQPqgGucXU02pVIh&sharer_shareinfo=2db4dd630bcf09aabd8175985d77a5d4&sharer_shareinfo_first=2db4dd630bcf09aabd8175985d77a5d4#rd)

本文系统阐述大语言模型（LLM）结构化输出的技术演进与实现路径，涵盖从提示工程、验证修复、约束解码、监督微调（SFT）、强化学习（SRL）到API接口化六大核心方法。文章指出，传统Prompt引导可靠性不足（约85%），而约束解码可实现100%格式合规，SFT面临“高原瓶颈”，SRL通过结构化思维与奖励机制显著提升复杂结构生成能力。主流API已内化Pydantic/JSON Schema支持，实现类型安全输出。评估需分层：先验结构合规性，再测语义准确性。技术趋势指向多模态生成、自适应解码与SFT-RL融合，推动LLM从文本生成器转型为可信赖的数据引擎。


## [从零实现 vLLM (1.1）：并行词嵌入 VocabParallelEmbedding](https://mp.weixin.qq.com/s?__biz=MzU4MTgyOTk1Mw==&mid=2247484630&idx=1&sn=215458fd1c45540a379ba710d9b8fc3a&chksm=fcb603e98f0060093e8ad2910fa759a80175bbdbb76f7de3dbb4ca1893eccbeffc5bf50091e0&mpshare=1&scene=1&srcid=101185Omf8unchtaiU1PHeQM&sharer_shareinfo=ac87111fe41a6201c5d26f3e0f161dea&sharer_shareinfo_first=ac87111fe41a6201c5d26f3e0f161dea#rd)

本文深入解析了vLLM中关键组件VocabParallelEmbedding的分布式实现机制，以Qwen3模型为背景，阐明其如何通过词汇表分片与All-Reduce通信实现高效并行词嵌入。在多GPU环境下，每个设备仅存储和计算部分词汇的嵌入向量，利用掩码过滤无效ID、本地查表后清零无关输出，最终通过All-Reduce聚合得到完整嵌入结果，既降低显存占用，又保持计算一致性。文章结合模拟代码与nano-vllm源码，系统拆解了初始化、权重加载与前向传播全流程，揭示了其“分而治之—合作汇总”的MapReduce范式，为构建高性能大模型推理引擎奠定核心基础。


## [突破四足机器人实时控制瓶颈！QUART-Online如何让MLLM告别推理延迟？](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA==&mid=2247546726&idx=1&sn=b4dcc4751ab4dd2c130164b7720946ce&chksm=cf52c37de1e913f22dfc2baa240ae55f2899aeccc15168c91361aef3df4503ed7e5aae60f76a&mpshare=1&scene=1&srcid=1010Fb7Wxxeq2jHlWkYovwoZ&sharer_shareinfo=07e9cbd99a362835f72c5d3a198982db&sharer_shareinfo_first=07e9cbd99a362835f72c5d3a198982db#rd)

本文提出QUART-Online，一种突破四足机器人实时控制瓶颈的多模态大语言模型（MLLM）架构，通过“动作块离散化”（ACD）与“动作-感知对齐”技术，将MLLM推理频率从2Hz提升至50Hz，实现与底层控制器的无延迟同步。该方法不依赖参数压缩，而是将连续动作编码为高维压缩块，结合视觉与语言指令联合微调，在保持原模型语义理解能力的前提下，任务成功率提升65%，动态避障成功率从48%跃至90%。实验验证其在未知物体与指令泛化场景中表现卓越，为具身智能的实时决策提供了高效、高精度的新范式。


## [拆解vLLM DP技术栈：特性原理、演进瓶颈与优化方案](https://mp.weixin.qq.com/s?__biz=MzYyMjA5NzMwOQ==&mid=2247484800&idx=1&sn=e07da1a571bcb1718c55c20f81860e66&chksm=feb25a4d02a6acc523e634ce1d4ca1633fa4ed2bcb3d10699e20c41e5608338828f1edda38a9&mpshare=1&scene=1&srcid=1010tNXYhWfdTEdMomm33LKh&sharer_shareinfo=34350d2c61e90382fd9319c26ad746ae&sharer_shareinfo_first=34350d2c61e90382fd9319c26ad746ae#rd)

本文系统拆解vLLM数据并行（DP）技术栈的实现原理、演进瓶颈与优化路径。V1版本采用ZMQ通信、主从架构，通过“wave”机制与dummy batch实现多引擎同步，但存在主节点CPU/流量瓶颈与负载不均问题。社区提出两大演进方向：一是多API Server+Coordinator方案，利用SO_REUSEPORT实现请求负载均衡，但引入新通信链路与复杂性；二是基于Ray的轻量级部署方案，简化启动流程。文章对比分析了两种方案的优劣，并指出当前PR存在同步死锁风险，为vLLM DP规模化部署提供关键技术参考。


## [腾讯发布1.58Bit大模型量化新算法Tequila！突破"死区陷阱"，效果性能刷新SOTA](https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649796078&idx=1&sn=7c19fcbb318fd27cd60c8cf7bb90db5f&chksm=bf9e1ba27b6f9eabc227cb5e7de6ff549ee9e262931fe54f9e531d469bfe2ee59d529ce644d1&mpshare=1&scene=1&srcid=1010Sxvejv5aw7y9cbPfUZEg&sharer_shareinfo=dcb49f6e6d23e37a607eda5de0acde99&sharer_shareinfo_first=dcb49f6e6d23e37a607eda5de0acde99#rd)

腾讯推出1.58Bit三值量化新算法Tequila，创新性提出“死区陷阱”解决方案，通过可微量化与动态离线偏置机制，将原失效的零权重转化为与输入无关的偏置项，既保留三值运算的硬件效率，又显著提升模型表达能力。该方法在不增加推理开销前提下，实现梯度稳定传播，训练收敛速度与模型性能全面超越BitNet等SOTA方案，在10B token数据上逼近全精度模型，多个基准提升约3%，CPU推理速度提升2–3倍，为大模型高效部署提供低功耗、高精度的实用路径。


## [字节 RhythmRL：基于投机采样+长度预测的 RL 加速](https://mp.weixin.qq.com/s?__biz=Mzk0ODU3MjcxNA==&mid=2247490496&idx=1&sn=30c34a697d96fd58789e209d6035bde4&chksm=c240feb7717303ff76d63304a66d7f3c3323e2593421c34841d18da6857eec0a04fdc7ddad0c&mpshare=1&scene=1&srcid=1001HY4grWSxFVzQUIX9IWpV&sharer_shareinfo=76514cd4851857485c72e7072ace3ae2&sharer_shareinfo_first=76514cd4851857485c72e7072ace3ae2#rd)

字节跳动提出RhythmRL，通过投机采样（HistoSpec）与长度预测（HistoPipe）双机制加速大模型强化学习（RL）的Rollout阶段。该方法利用相邻训练Epoch中响应的高度相似性，以历史输出作为草稿提升生成效率，结合动态草稿长度调整与奖励感知后缀树，使Token接受率达65%-79%；同时基于历史长度分布实现跨Step的负载均衡，采用双层调度与迁移机制缓解长尾效应。在8K/16K序列长度下，相较veRL实现2.6倍加速，GPU利用率显著提升，且训练精度无损，适用于数十至数千GPU的规模化部署。


## [DeepSeek-V3.2背后的国产算子编程语言TileLang是什么？如何保持性能领先的同时减少6倍代码量？](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA==&mid=2247546203&idx=1&sn=e28b308689b51a2854690a7a49282a89&chksm=cfb608c9957abd6668ca287f51176e4bf2777a6413520f38ed9a3f48aa52edcaff8181059bec&mpshare=1&scene=1&srcid=0930Xsj9Vrvc4usS7lM4GfA1&sharer_shareinfo=53dcdac9030e11ed6e5d89dc3bc99e76&sharer_shareinfo_first=53dcdac9030e11ed6e5d89dc3bc99e76#rd)

TileLang是由北京大学杨智团队研发的开源AI算子编程语言，通过创新的“Tile级抽象”与自动调度机制，将高性能算子开发代码量减少6倍以上（如FlashAttention从500行降至80行），性能媲美手写CUDA/AscendC代码。其多层级编程范式支持从算法工程师到硬件专家的差异化开发需求，并原生支持国产昇腾芯片，推动AI底层工具链自主化。项目开源两个月即获超1800星，已与SGLang等生态集成，成为提升国产AI算力软件生态效率的关键基础设施。


## [使用 NVIDIA Dynamo 部署 PD 分离推理服务](https://mp.weixin.qq.com/s?__biz=MzkxOTIwMDgxMg==&mid=2247489617&idx=1&sn=33e7b60594bba624c30114c06d01921e&chksm=c01358dcc910b8964645c986c2ea7b904ae6c23f14258d1920550f71d272878aa4c06399a3ef&mpshare=1&scene=1&srcid=0929QqiIcVps3gSRZAzcIrZK&sharer_shareinfo=b9dea4bf157d540056e8ab48b3a5d002&sharer_shareinfo_first=535f9c41ecd5ab9ebb48869e5a5bef78#rd)

NVIDIA Dynamo 是一个开源分布式推理框架，专为生成式AI模型的高效服务化部署设计，支持TensorRT-LLM、vLLM等主流引擎。其核心通过Planner智能调度、Smart Router KV感知路由、Distributed KV Cache Manager分层缓存管理及NIXL高速传输库，实现prefill与decode阶段的动态分离（PD Disaggregation），显著提升GPU利用率与吞吐量。文章详述了其在本地与Kubernetes环境中的部署流程，展示如何通过CRD声明式编排构建高可用推理集群，有效降低长上下文推理延迟与内存开销，为生产级大模型服务提供低延迟、高扩展的解决方案。


## [LLM推理优化:MLA算力均衡实践(提升0.3x)](https://mp.weixin.qq.com/s?__biz=MzYyMjA5NzMwOQ==&mid=2247484706&idx=1&sn=1e8e0b5ce5ae284c8415eede4656de17&chksm=feb94d574851601702939a3f4d361ddca2ef04dbf42d458377a6e236cd686498f9e33c893a87&mpshare=1&scene=1&srcid=0928w9lHoPwnAs0DVqMPbp1h&sharer_shareinfo=80ab55665e730e4fe4f4d42720d04d7a&sharer_shareinfo_first=80ab55665e730e4fe4f4d42720d04d7a#rd)

本文针对LLM推理中MLA架构在Prefill阶段因输入序列长度差异导致的算力不均衡问题，提出一种跨DP域的SP-TP-SP混合并行优化方案。通过序列混合分配与Head维度张量并行，实现token级负载均衡，显著提升吞吐。在vLLM框架上实现，仅需少量修改，于DP4/TP4配置下，定长输入提升20%+，随机长度提升50%+。同时引入LayerShardLinear降低显存开销，并适配Ascend芯片格式约束。该方案有效平衡计算负载，为MoE模型高效推理提供轻量级优化路径。


## 202509

## [vLLM Office Hours #33 的核心内容！](https://mp.weixin.qq.com/s?__biz=Mzg2MzY3OTc2Mw==&mid=2247484161&idx=1&sn=aee756fa749e4951fbeceecc168ea704&chksm=cfd83db7c8339ecf4a23b844871e12546323bedf06eba688c470923b750d00788835a74e0d0e&mpshare=1&scene=1&srcid=0927cL2ag7znrsk8dWcOe5Q8&sharer_shareinfo=4f10267e7edf5894aa8e5a9c2a196779&sharer_shareinfo_first=4f10267e7edf5894aa8e5a9c2a196779#rd)

vLLM Office Hours #33 重磅发布0.10.2版本，标志着V0引擎正式进入退役倒计时，V1引擎全面成熟。核心更新包括：全面支持Qwen3系列（含多模态Omni与VL）、Mamba-2混合架构（SSM+Transformer）的高效推理，显著提升长序列处理效率与显存利用率；新增20+模型支持，覆盖多模态、OCR、金融等领域；深度优化FP8/FP4量化、FlashAttention与CUDA图，NVIDIA B200推理速度提升2-3倍；扩展Apple Silicon、Intel XPU、IBM Z等平台支持；引入SpinQuant、QuIP等新型量化技术，4bit下精度损失可控。同时，社区正推进音频/视频输出插件，推动vLLM向全栈大模型服务平台演进。


## [PD 分离推理架构详解](https://mp.weixin.qq.com/s?__biz=MzkxOTIwMDgxMg==&mid=2247489668&idx=1&sn=549ba8672471dd1f88da5c600d73d00f&chksm=c0b21b6320344f7dda137c2e77de42275115090e456d3935f6bf3a44d386161346dbe6d678da&mpshare=1&scene=1&srcid=09261WT0Ph9o0ym4WV1ruTQb&sharer_shareinfo=05ddb0ed069abcf00d2ef77d6263c16a&sharer_shareinfo_first=05ddb0ed069abcf00d2ef77d6263c16a#rd)

PD分离推理架构通过将大语言模型推理的prefill（预填充）与decode（解码）阶段解耦至独立GPU实例，针对其计算密集型与内存密集型特性分别优化，显著提升满足TTFT与TPOT服务等级目标（SLO）的有效吞吐量（Goodput）。传统共置架构因阶段干扰导致延迟恶化，而PD分离通过高速互联（如NVLink/PCIe 5.0）传输KV Cache，开销可被隐藏，并支持灵活的批处理、并行策略与KV Cache管理。vLLM、Mooncake、Dynamo等主流系统已实现该架构，结合NIXL、LMCache等组件优化传输与缓存，在长上下文场景下可提升吞吐达5倍以上，成为高并发、低延迟LLM服务的核心方案。


## [LLM推理EPLB原理:用可视化深度解析DeepEP](https://mp.weixin.qq.com/s?__biz=MzYyMjA5NzMwOQ==&mid=2247484589&idx=1&sn=1e43f65ca700e086ac97b1a0d247c7f5&chksm=fe413fe5c3c572a385ded940f5d2c3f659a8ccce33d11f6feaee6303ebadb2341b8ec9e968d2&mpshare=1&scene=1&srcid=0925zrx4GIyueoeesBDr2BlO&sharer_shareinfo=1916548245395ee9d050e06aae0c7980&sharer_shareinfo_first=1916548245395ee9d050e06aae0c7980#rd)

本文深度解析DeepSeek开源的EPLB（Expert Parallelism Load Balancer）推理负载均衡机制，聚焦MoE架构中专家计算负载不均问题。EPLB结合冗余副本与分组排序策略，在不重训前提下动态构建物理专家映射，通过预测专家热度、分组复制高负载专家、贪心分配至GPU，实现跨节点负载均衡。作者基于原代码开发可视化工具，清晰呈现输入权重到部署映射的全过程，并区分Prefill（小粒度分组）与Decoding（全局排序）场景下的策略差异。该方案适用于推理阶段，避免频繁权重加载，兼顾通信效率与算力利用率，为大规模MoE推理系统提供高效、可落地的负载均衡范式。


## [vLLM 核心机密（二）：生成函数的「请求处理→循环执行」全流程](https://mp.weixin.qq.com/s?__biz=Mzg2MzY3OTc2Mw==&mid=2247484156&idx=1&sn=ace9725a9471b516d29dd21c40e2005d&chksm=cf1506c68840ce79142ff578b077d0527172f20651d535dc670acee72a728bf509c3e33d6566&mpshare=1&scene=1&srcid=0925fhIqLlzGesie6ltuGsaf&sharer_shareinfo=5cd5d6d25d57786e749e3b5f6b0ceea7&sharer_shareinfo_first=5cd5d6d25d57786e749e3b5f6b0ceea7#rd)

vLLM生成函数的核心流程分为请求处理与循环执行两大阶段：请求进入后，先经唯一ID标记、文本分词（tokenization）为token ID序列，并封装含采样参数与优先级的EngineCoreRequest，入队等待调度；引擎通过step()函数持续循环，执行“调度→前向推断→后处理”三阶段：调度器动态选择预填充（prefill）与解码（decode）请求组成批处理，模型以连续批处理方式高效计算，生成新token后，系统检查停止条件（如max_tokens、EOS、自定义停止词），完成请求则释放KV缓存并返回结果，未完成则重新入队。该流程实现高吞吐、低延迟的异步生成，为vLLM性能基石。


## [vLLM性能密码：prefix cache为何能实现“零开销”加速？](https://mp.weixin.qq.com/s?__biz=MzYyMjA5NzMwOQ==&mid=2247484579&idx=1&sn=d42b6db4973bea475a19e2b37dcd410a&chksm=fe7bfe4819fa2b9d1f6fbdf3324c6796a84daa8cd356aa5f6127e3265495b8f6f350ad1e188b&mpshare=1&scene=1&srcid=0924HLc6WWy3lDF6UAaJxLq4&sharer_shareinfo=98d48ff1be86f4ed1ed757c40c2af53e&sharer_shareinfo_first=98d48ff1be86f4ed1ed757c40c2af53e#rd)

vLLM V1通过重构KV缓存管理架构，实现“零开销”前缀缓存（Prefix Caching），即使命中率为0，推理性能也与关闭缓存基本一致。其核心改进包括：将缓存单元简化为仅含block ID、引用计数和哈希值的轻量结构；用双向链表替代LRU淘汰器，降低管理开销；以int/str替代复杂Python对象，减少内存与计算负担；并通过块池与请求映射分离，实现高效复用与快速查找。该设计在保证高命中率下显著加速prefill阶段的同时，彻底消除低命中场景下的性能损耗，使前缀缓存可默认开启，大幅提升系统整体吞吐效率。


## [vLLM 核心机密：大模型推理引擎内部长啥样？](https://mp.weixin.qq.com/s?__biz=Mzg2MzY3OTc2Mw==&mid=2247484151&idx=1&sn=c97c969a0537cac63cdcf6b4af6c2078&chksm=cf44d05e6f23edd51398fd9da5d827c19ed204e4982fba705c9aa1074efeaa529c715bb37e2c&mpshare=1&scene=1&srcid=0922qxwUL5jYkkeTaGyL0Hdn&sharer_shareinfo=042a04963d778443f6525111b95fa964&sharer_shareinfo_first=042a04963d778443f6525111b95fa964#rd)

vLLM 是当前主流的高性能大模型推理引擎，其核心通过分页注意力（PagedAttention）与 KV 缓存动态管理显著提升吞吐量与显存利用率。文章深度解析其架构：由配置模块、请求处理器、引擎核心与输出处理器构成，引擎核心含模型执行器、调度器与结构化输出管理器。启动阶段完成设备适配、模型加载、KV 缓存预分配及 CUDA 图优化，支持 FP8/INT4 量化与 Marlin、CUTLASS 等底层加速库自动调度。通过块大小（block_size）、KV 类型（dtype）、CPU 卸载等参数精细调控显存，实现单卡高并发推理，性能可达传统方案 5–10 倍，为分布式、异步、多 GPU 推理服务奠定高效基础。


## [LLM推理提速新路径：Attention与FFN分离方案深度解析](https://mp.weixin.qq.com/s?__biz=MzYyMjA5NzMwOQ==&mid=2247484487&idx=1&sn=0ebc8a4139a810bd15b4379ed43c02c3&chksm=fe4eb7f249f56bf4d5b530dcfd38c5538862392de49d49edffa59294d822478e8726d95211d2&mpshare=1&scene=1&srcid=0921CaGib6lbv9g6EThqFX54&sharer_shareinfo=736db6cd151e1615b56ec81e08846797&sharer_shareinfo_first=736db6cd151e1615b56ec81e08846797#rd)

本文深入解析LLM推理加速新范式——Attention与FFN分离（AFD）技术。针对Transformer中Attention（访存瓶颈）与FFN（计算瓶颈）在Decode阶段的异构负载特性，AFD通过将二者部署于不同硬件（如高带宽GPU与高算力NPU），实现资源精准匹配，显著提升集群利用率。文章系统对比Step3（开源StepMesh通信库）、xDS（超节点DMA架构）与MegaScale-Infer（Ping-Pong流水）三大方案，分析其通信机制、并行策略与硬件适配逻辑，并探讨vLLM、SGLang等主流框架的集成路径。该技术突破单卡限制，支持异构混搭、弹性伸缩与跨集群部署，为大模型高效推理提供新架构方向，但尚面临通信开销、系统复杂性与框架成熟度等挑战。


## [论文推荐 | （中国科学院计算所崔慧敏、赵家程团队等） 面向昇腾处理器的高性能同步原语自动插入方法](https://mp.weixin.qq.com/s?__biz=MzI1NDEyNTIyNg==&mid=2649581568&idx=1&sn=53d164b85595145b6880c1bf4a375da3&chksm=f0bc9b2e2302c66304248e965af89417d68a2371a358e46fbd1cb648272c9f06b6943442da8e&mpshare=1&scene=1&srcid=0919y2e8EAAXARLwW88ox1WK&sharer_shareinfo=58367c493e48f679d0d60c5412e9eefb&sharer_shareinfo_first=58367c493e48f679d0d60c5412e9eefb#rd)

中国科学院计算所崔慧敏、赵家程团队联合华为，提出一种面向昇腾处理器的高性能同步原语自动插入方法，首次解决其set-wait同步机制下编译器自动化难题。该方法创新引入“虚拟同步资源”抽象，解耦同步插入与物理资源分配，结合启发式插入、冗余消除与图着色映射技术，在严苛的硬件资源限制下实现指令级并行优化。实验表明，其在昇腾910A平台上的性能可媲美专家手动调优，显著降低异构编程门槛，为领域定制架构的自动化编译提供新范式。


## [抢先 Qwen Next？腾讯自研 FastMTP 重磅开源：推理速度暴涨 203%，消费级显卡也能跑出无损速度翻倍！](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA==&mid=2247545326&idx=1&sn=3ed8a7c5c9e3556efbc6ffec5c29c7b5&chksm=cf87ae7ceba45534aee1fb1f2eeab9c0b10723d5bc0f77469e11e6ec669330c58e5a0712d940&mpshare=1&scene=1&srcid=09192wIcTvRFmiiXPKHGSa9S&sharer_shareinfo=ee3207a649f13a8e2f6a4e9a600b647b&sharer_shareinfo_first=ee3207a649f13a8e2f6a4e9a600b647b#rd)

腾讯PCG团队开源FastMTP，一种基于投机解码的高效LLM推理加速框架，通过共享权重的单MTP头、自蒸馏训练与语言感知词汇压缩三大创新，在不修改主模型前提下，实现平均2.03倍推理加速（最高达2.5倍），且输出质量无损。该方法仅需210.8M参数的轻量模块，适配消费级GPU（如RTX 4090），在数学推理与代码生成等结构化任务中表现尤为突出，训练仅需单台H20服务器一天完成，开源代码与权重已全面开放，显著降低大模型部署门槛。


## [通义DeepResearch震撼发布！性能比肩OpenAI，模型、框架、方案完全开源](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650991480&idx=1&sn=92ce450ac097f172c6ac89350be8d56f&chksm=85b86fd49cf96273eed8067f27864d9a7411e7832843a8e09d91adfa37d8b710035c66847220&mpshare=1&scene=1&srcid=091889GLEaOM3GAVHs8BD57h&sharer_shareinfo=67f6242ba516b38e8a864ca07d356b04&sharer_shareinfo_first=67f6242ba516b38e8a864ca07d356b04#rd)

通义DeepResearch重磅开源，推出30B-A3B轻量级模型，在Humanity's Last Exam、GAIA、WebWalkerQA等权威基准上全面超越闭源竞品，性能比肩OpenAI。团队首创“Agentic CPT+SFT+RL”端到端训练范式，依托全合成数据构建高质量训练集，突破人工标注依赖；创新IterResearch推理框架，通过多轮研究循环与并行合成机制提升复杂任务表现；并构建稳定仿真环境与自动化数据引擎，实现高效强化学习。模型已落地高德导航、通义法睿等真实场景，全面开源模型、框架与方法论，推动AI研究范式变革。


## [一文全解析：AI 智能体 8 种常见的记忆（Memory）策略与技术实现](https://mp.weixin.qq.com/s?__biz=Mzk1NzQ1ODk5NQ==&mid=2247523993&idx=1&sn=af3cb2b1d7d0154690d91ae92cd1e438&chksm=c2bfc530190c4b37f627cf6e69a74fb3e14fbc79f3518f6f2507d90bd6d08e320bcbd16becec&mpshare=1&scene=1&srcid=0917v8NTyXVSGoFiXCWWvJPS&sharer_shareinfo=5fe20b5cce46fa19f9a2b8eac273f391&sharer_shareinfo_first=5fe20b5cce46fa19f9a2b8eac273f391#rd)

本文系统解析了AI智能体的8种核心记忆策略：全量记忆、滑动窗口、相关性过滤、摘要压缩、向量数据库检索、知识图谱结构化存储、分层记忆（短期+长期）及类OS内存管理（Swap机制）。文章从原理、实现代码、优缺点与适用场景出发，全面对比各方案在上下文长度限制、计算成本与记忆持久性间的权衡，指出全量记忆仅适配短对话，而向量库与知识图谱更适合长程、语义化需求，分层与Swap机制则兼顾效率与扩展性。为开发者提供选型依据，助力构建高效、可扩展的智能体记忆系统。


## [GPU虚拟内存与线程束调度技术分析](https://mp.weixin.qq.com/s?__biz=MzIzNDY5NDg5NQ==&mid=2247487400&idx=1&sn=ad8ba0a96d35a2a79d4cd12dc708fcb0&chksm=e94101e80171b3d646acbb33dce345d013436c38bf7fd6f86a63d8332519db7980debfd474cd&mpshare=1&scene=1&srcid=0915mvAE1eAMomiJK5uMuzXM&sharer_shareinfo=f360a769f5badd0ce6336040d2214917&sharer_shareinfo_first=f360a769f5badd0ce6336040d2214917#rd)

本文系统分析了GPU虚拟内存管理与线程束调度两大核心机制。虚拟内存方面，重点探讨了四级页表、TLB未命中爆发、统一虚拟地址空间（UVA）的页错误开销及大页、预取等优化策略，指出共享PTW与细粒度本地补页是缓解跨总线延迟的关键。线程束调度方面，对比轮询（RR）与贪心最老（GTO）策略，揭示调度决策显著影响缓存工作集与命中率：RR易导致缓存颠簸，GTO则更利于局部性利用；进而提出两级调度与缓存感知调度，通过限制活跃Warp数降低冲突缺失。研究强调，智能内存管理与调度协同优化是提升GPU性能的核心路径。


## [LLM时代AI加速器设计：被忽视的Vector算力瓶颈](https://mp.weixin.qq.com/s?__biz=MzkzNzQzMDg3NA==&mid=2247483905&idx=1&sn=55f4f9f85d5eaabb2bae0ecebabf459e&chksm=c34cfcb32b158e88f5d95f583602a3347dacc97c348c5413be22ca32fd91d1e8263190e63ebd&mpshare=1&scene=1&srcid=0914qBKPCFIHBkPfwOcFDRId&sharer_shareinfo=49ce1c0e804de57eed22933e41cbee90&sharer_shareinfo_first=49ce1c0e804de57eed22933e41cbee90#rd)

本文揭示LLM时代AI加速器设计中被长期忽视的vector算力瓶颈，尤其聚焦exp2指数运算在FlashAttention中的关键作用。作者指出，NVIDIA B200因exp2算力不足，被迫用CUDA Core近似计算，严重制约性能；昇腾910B则因GEMM与Vector单元间缺乏共享缓存，导致数据搬运开销巨大。文章通过量化分析提出合理架构原则：GEMM与Vector单元需共享高速缓存、算力配比应匹配计算负载比例，并指出NVIDIA后续B300与Rubin CPX通过2倍、3倍提升exp2算力逐步优化。结论强调，未来大head_dim注意力机制或成缓解vector瓶颈的硬件友好趋势。


## [不会 CUDA 也能轻松看懂的 FlashAttention 教程（算法原理篇）](https://mp.weixin.qq.com/s?__biz=MzkyMTM0Mjc3NA==&mid=2247486929&idx=1&sn=36faa2b6b5b67212ecb4e726d270dff9&chksm=c0591c12727da858d2c25a134f1b9c6369615f83b4024566bb8e0b91afce2dc383f3a853ecc0&mpshare=1&scene=1&srcid=0913iLYeN15ReJRWpBShzagZ&sharer_shareinfo=b05aa094c85abe59c28a9f0b3af1d5ea&sharer_shareinfo_first=b05aa094c85abe59c28a9f0b3af1d5ea#rd)

本文以零CUDA基础为前提，深入浅出地解析FlashAttention的核心算法原理。作者从GPU存储层次（HBM与SRAM）与并行计算模型切入，揭示传统Attention因softmax中间变量（[SL×SL]）频繁访存导致的性能瓶颈；进而通过算子融合与计算重排，巧妙将softmax拆解为“先累加指数再归一化”的流式计算，消除长中间变量，实现仅需O(D)显存的高效前向计算。全文以伪代码逐步演进，无需CUDA术语，系统阐明FlashAttention如何通过“分块+循环合并+分母延迟除法”策略，大幅降低显存占用与带宽压力，为大模型训练提供关键优化路径。


## [性能暴涨50%:PD分离KV cache传输的实战干货](https://mp.weixin.qq.com/s/s-UapW7XsO8RmH7mmqSDaw)

在LLM推理的PD（Prefill-Decode）分离场景中，高效传输键值缓存（KV Cache）是提升整体性能的关键。本文介绍了基于vLLM框架开发的​​KV Cache传输connector​​，通过优化传输机制，实现了​​传输性能提升0.5倍​​，相关代码已全面开源。
文章系统分析了KV Cache传输中的核心挑战，包括​​异构传输​​（如MLA与GQA/MHA结构差异）、​​内存对齐要求​​、​​传输聚合策略​​及与vLLM调度器的深度协同。针对Ascend 910B硬件环境，团队设计了基于​​RDMA​​的高效传输方案，并集成至Mooncake传输引擎（TE），显著提高了带宽利用率和传输可靠性。
此外，本文探讨了进一步优化方向，如​​分层传输（Layer-wise Strategy）​​、​​异构拓扑下的广播优化​​、​​传输-计算流水线设计​​等，为LLM分布式推理中的数据传输提供了重要实践参考和理论支撑。

<audio controls="">
  <source src="https://github.com/user-attachments/files/22303607/KV%2BCache.Ascend.mp3" type="audio/mp3" />
</audio>


## [PyTorch torch.compile 训练编译技术现状与展望（2025年8月）](https://mp.weixin.qq.com/s/cNTkNZyyETQrHDDYdSSyvw)

本文系统综述了 PyTorch torch.compile 在训练场景，特别是自动并行领域的最新进展与未来方向。作为 PyTorch 的核心编译技术，torch.compile 通过即时编译（JIT）实现训练性能 1.5–2 倍提升，并支持包括自动激活检查点（Automatic Activation Checkpointing） 和异步张量并行（Async Tensor Parallelism） 在内的全局内存与通信优化。

文章重点对比了 PyTorch 与 JAX 在分布式编译路径上的根本差异：JAX 以 XLA 为核心、编译优先，而 PyTorch 坚持用户体验优先，从全手动模式逐步引入自动化机制。DTensor 作为核心分布式抽象，支持 SPMD 风格的张量分片与自动微分，并与 FSDP2、AutoParallel 等生态深度集成，是实现自动并行的基础。

当前，torch.compile 已支持多种图捕获机制（包括 make_fx 和 symbolic_trace），并依托 Inductor 编译器后端实现算子融合、动态代码生成与 CUDA Graphs 集成。此外，诸如 Flex Attention、FP8 训练优化等功能也极大丰富了模型开发与部署的能力。

尽管在动态形状、编译时间与跨秩一致性方面仍存在挑战，PyTorch 团队正积极推进预编译（AOTInductor） 与统一运行时，旨在为超大规模训练提供稳定、高效的编译解决方案。本文为研究者与工程师理解 PyTorch 编译技术栈提供了系统且前沿的参考。

<audio controls>
  <source src="https://github.com/DongminWu/LLM-Infra-sys/raw/refs/heads/main/202509/PyTorch+%E7%9A%84+torch.compile+%E7%8E%B0%E7%8A%B6.mp3" type="audio/mp3">
</audio>


## [高级矩阵乘法在NVIDIA GPU上的优化](https://mp.weixin.qq.com/s/IvnvHkWogIrWMjV8j-kZPw)

本文系统阐述了在NVIDIA GPU架构上实现高性能单精度矩阵乘法（SGEMM）的优化方法与关键技术。SGEMM作为科学计算与深度学习的核心运算，其高效实现对提升计算性能至关重要。现有的教育性实现通常难以达到工业级库（如cuBLAS）的性能水平，而高性能实现又缺乏足够的可解释性。

本研究以CUTLASS算法设计为基础，深入探讨了在CUDA环境中通过**内联PTX汇编**、**异步内存拷贝**、**双缓冲**机制、**共享内存优化**及**向量化内存访问**等多项关键技术，显著提升计算效率。特别针对NVIDIA RTX 3090（GA102芯片）进行细致调优，在实现过程中注重避免存储体冲突与实现合并存储。

实验结果表明，在锁定频率和未锁定频率两种条件下，所提出的实现方案在多种矩阵规模下均表现出优于或接近cuBLAS的**性能表现**，尤其在较大矩阵乘法中显示出良好的扩展性与稳定性。本文不仅提供了详实的实现细节，还为CU学习者理解高性能SGEMM实现提供了清晰的技术路径与优化思路。


<audio controls>
  <source src="https://github.com/DongminWu/LLM-Infra-sys/raw/refs/heads/main/202509/%E4%BC%98%E5%8C%96+CUDA+SGEMM+%E6%80%A7%E8%83%BD.mp3" type="audio/mp3">
</audio>

## [简单聊聊 NVIDIA 最新的 Vera Rubin NVL144 CPX 系统](https://mp.weixin.qq.com/s/f-3RLqe-m_g6NY8JmT5ksg)
近年来，大语言模型（LLM）推理过程中的**Prefill阶段**（计算密集型）和**Decoding阶段**（存储带宽密集型）表现出显著不同的性能特征，推动了对**分离式推理（PD分离）** 系统的需求。为优化系统效率与成本，NVIDIA最新推出了专为Prefill阶段设计的**Rubin CPX GPU**，采用成本较低的**GDDR7显存**，提供30 PFLOPS的FP4算力及2 TB/s的显存带宽，显著提升了大上下文推理任务的性价比。

与之配套，NVIDIA提出两种系统级解决方案：**Vera Rubin NVL144 CPX Rack** 和 **Vera Rubin CPX Dual Rack**。前者为高集成度单机架系统，整合144个Rubin CPX GPU与72个标准Rubin GPU（配备HBM4），总算力达8 EFLOPS FP4，显存总带宽约1.2 PB/s；后者采用双机架配置，提供相等的算力与更高的扩展灵活性。两者均依托**Vera CPU**和高速**NVLink-C2C**互连，实现CPU与GPU间的高带宽通信。

目前公开数据中存在部分未明确的细节，如系统级存储带宽（官方标注为1.7 PB/s）的计算方式、**NVLink7**的实际带宽，以及Vera CPU与Rubin CPX GPU之间的互联支持等。这些系统在集成度、网络成本、故障率和部署灵活性方面各有优势，适合不同规模的推理负载需求。

该项发展标志着GPU架构正朝着更精细化负载优化的方向发展，特别是在支持超长上下文推理场景中，体现出重要的工程与架构创新。


<audio controls>
  <source src="https://github.com/DongminWu/LLM-Infra-sys/raw/refs/heads/main/202509/NVIDIA+%E5%8F%91%E5%B8%83+Vera+Rubin+NVL144+CPX+%E7%B3%BB%E7%BB%9F.mp3" type="audio/mp3">
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
  <source src="https://github.com/DongminWu/LLM-Infra-sys/raw/refs/heads/main/202509/%E5%8D%8E%E4%B8%BA%E5%BB%96%E6%81%92%E5%8D%9A%E5%A3%AB%E8%AE%B2%E8%A7%A3+UB-Mesh+%E6%9E%B6%E6%9E%84.mp3" type="audio/mp3">
</audio>

## [一文梳理主流大模型推理部署框架：vLLM、SGLang、TensorRT-LLM、ollama、XInference](https://mp.weixin.qq.com/s/Fsaz7PAUSiKizl_lw-KSeg)

​​vLLM​​ 通过 ​​PagedAttention​​ 和 ​​连续批处理（Continuous Batching）​​ 显著提升显存利用率和吞吐量，适用于企业级高并发场景。​​SGLang​​ 基于 ​​RadixAttention​​ 实现前缀复用和结构化输出，在高吞吐和多轮对话任务中表现突出。​​TensorRT-LLM​​ 依托 NVIDIA 硬件深度优化，在低延迟场景中性能卓越。​​Ollama​​ 以轻量化和跨平台特性适合本地开发与快速原型验证。​​XInference​​ 和 ​​LightLLM​​ 则专注于分布式推理和边缘计算部署，支持国产硬件与多模态任务。

本文为不同业务需求（如实时响应、高吞吐、资源受限环境或国产化部署）提供选型参考，旨在推动大模型技术的高效落地与应用创新。

<audio controls>
  <source src="https://github.com/DongminWu/LLM-Infra-sys/raw/refs/heads/main/202509/%E4%B8%BB%E6%B5%81%E5%A4%A7%E6%A8%A1%E5%9E%8B%E6%8E%A8%E7%90%86%E9%83%A8%E7%BD%B2%E6%A1%86%E6%9E%B6%E6%A2%B3%E7%90%86%20(online-audio-converter.com).mp3" type="audio/mp3">
</audio>


## [打破瓶颈，让RAG学会思考：中科大、智源等发布推理检索框架BGE-Reasoner](https://mp.weixin.qq.com/s/hDBJ998nc9kO6vnTpx9exA)

随着 RAG 和 AI Agent 技术的快速发展，**推理密集型信息检索（Reasoning-Intensive IR）** 成为制约大模型智能体与深度研究应用的核心挑战。该类任务需综合多步逻辑推理、语义链与背景知识，传统检索方法在复杂查询下表现显著不足。为此，中国科学技术大学、智源研究院等机构联合提出 **BGE-Reasoner**，一套创新的端到端解决方案，在权威基准 **BRIGHT** 上以 **45.2** 的得分刷新纪录，领先原最优结果 **3.6 分**。

BGE-Reasoner 的核心创新体现为三方面：  
1. **模块化框架设计**：提出由 **Rewriter**（查询理解与改写）、**Embedder**（向量检索）与 **Reranker**（重排序）构成的三阶段流程，显著提升复杂查询的处理能力；  
2. **合成数据驱动**：基于大模型生成多领域高质量推理训练数据，有效解决数据稀缺问题；  
3. **强化学习优化**：在 Reranker 训练中引入强化学习，增强模型对困难样本的推理与泛化能力。  

此外，BGE-Reasoner 的嵌入模型 **BGE-Reasoner-Embed** 在 BRIGHT 基准下同样达到最优性能，超越 Seed1.5-Embedding、Qwen3-Embedding 等基线模型。该研究不仅提供了性能领先的检索系统，更为推理密集型任务提供了可复制的技术范式。相关模型、代码与数据将开源，推动领域进一步发展。

<audio controls>
  <source src="https://github.com/DongminWu/LLM-Infra-sys/raw/refs/heads/main/202509/BGERAG.mp3" type="audio/mp3">
</audio>

