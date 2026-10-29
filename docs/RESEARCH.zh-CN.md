# 研究依据与读图指南

[返回首页](../README.zh-CN.md) · [English](RESEARCH.md)

**Defensive Writing in GPT Models**

Junchi Liao, Xiao Huang, Yucheng Liu, Jiawen Deng, Fuji Ren

[论文与摘要](https://arxiv.org/abs/2610.11355v2) · [全文](https://arxiv.org/html/2610.11355v2)

## 1. 论文研究的问题

论文区分了两种改写：根据材料修正过度主张，以及加入没有材料依据的限定。它还比较了写作请求、模型版本与评审反馈带来的变化。

[![论文标题、作者与摘要](../assets/paper/paper-title.png)](../assets/paper/paper-title.png)

## 2. 图 1：写作与评审如何形成循环

图从左到右展示作者主张、GPT 改写，以及 AI 审稿人与人类读者的反应。先看改写框中新增的限定，再看右侧评分与阅读感受的差异。

[![Figure 1：写作与评审过程](../assets/paper/figure-1-overview.png)](../assets/paper/figure-1-overview.png)

## 3. 表 1：指标分别表示什么

- **Rᵤ**：每 100 词中的无依据限定数量。
- **Nov / Con / Res / Dis**：新颖性、贡献、结果分析、讨论四类段落。
- **Ret / Soft**：作者主张被撤回或弱化的比例。
- **Rewriting / Writing from evidence**：根据原段落改写，或根据证据表起草。

[![Table 1：不同模型与段落类型的结果](../assets/paper/table-1-models.png)](../assets/paper/table-1-models.png)

## 4. 图 2：模型版本与改写变化

横轴为 GPT 版本；左轴显示无依据限定数量，右轴显示主张弱化与撤回比例。阅读时先对照图例，再区分左右两套刻度。

[![Figure 2：不同版本的限定、弱化与撤回指标](../assets/paper/figure-2-versions.svg)](../assets/paper/figure-2-versions.svg)

## 5. 图 3：不同提示词情境

横轴 P1–P9 对应不同的写作要求；纵轴为每 100 词的无依据限定数量。

| 编号 | 写作要求概述 |
|---|---|
| P1 | 普通润色 |
| P2 | 研究组内部技术报告的润色 |
| P3 | 面向会议投稿的润色 |
| P4 | 修改到能经受同行评审 |
| P5 | 预先回应审稿人可能提出的问题 |
| P6 | 提高录用机会 |
| P7 | 面向严苛审稿人的修改 |
| P8 | 按科学准确性修改 |
| P9 | 让每项主张的强度与证据匹配 |

[![Figure 3：不同提示词情境下的无依据限定](../assets/paper/figure-3-prompts.svg)](../assets/paper/figure-3-prompts.svg)

## 6. 对应的写作练习

| 你要做的事 | 模板 |
|---|---|
| 修改语言与结构 | [DW-002 最小改动润色](library/zh/clarity.md#dw-002) |
| 检查每句的信息作用 | [DW-001 逐句功能诊断](library/zh/clarity.md#dw-001) |
| 回应实际审稿意见 | [DW-012 回复审稿意见](library/zh/research.md#dw-012) |

图片署名：Liao et al., arXiv:2610.11355v2，CC BY 4.0。曲线图采用论文矢量文件，概览图采用原始 PNG；点击图片可查看独立大图。[图片来源与规格](../assets/paper/README.md)
