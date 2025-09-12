# LLM-AI-Infra-system好文分享

## 202509

## [性能暴涨50%:PD分离KV cache传输的实战干货](https://mp.weixin.qq.com/s/s-UapW7XsO8RmH7mmqSDaw)

在LLM推理的PD（Prefill-Decode）分离场景中，高效传输键值缓存（KV Cache）是提升整体性能的关键。本文介绍了基于vLLM框架开发的​​KV Cache传输connector​​，通过优化传输机制，实现了​​传输性能提升0.5倍​​，相关代码已全面开源。
文章系统分析了KV Cache传输中的核心挑战，包括​​异构传输​​（如MLA与GQA/MHA结构差异）、​​内存对齐要求​​、​​传输聚合策略​​及与vLLM调度器的深度协同。针对Ascend 910B硬件环境，团队设计了基于​​RDMA​​的高效传输方案，并集成至Mooncake传输引擎（TE），显著提高了带宽利用率和传输可靠性。
此外，本文探讨了进一步优化方向，如​​分层传输（Layer-wise Strategy）​​、​​异构拓扑下的广播优化​​、​​传输-计算流水线设计​​等，为LLM分布式推理中的数据传输提供了重要实践参考和理论支撑。

<audio controls>
  <source src="/202509/性能暴涨50%PD分离KVcache传输的实战干货.mp3" type="audio/mp3">
</audio>
