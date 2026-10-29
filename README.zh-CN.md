# Awesome Defensive Writing · by Yila

**反防御性写作提示词与 Agent Skill**

把空泛退让改成清楚的判断，让观点、证据与行动直接出现。

[English](README.md) | **简体中文**

**从一张图看懂问题：作者的主张，如何在 AI 改写与评审中发生变化。**

[![研究概览：作者主张、GPT改写、AI审稿与人类读者](assets/paper/figure-1-overview.png)](assets/paper/figure-1-overview.png)

图源：Liao et al., [Defensive Writing in GPT Models](https://arxiv.org/abs/2610.11355v2)，Figure 1，CC BY 4.0。[读图指南与完整图表](docs/RESEARCH.zh-CN.md)。

**60 套中英文提示词 · 24 组情景案例 · 10 类场景**

偶尔修改文字，复制模板即可；经常使用，安装到自己的 Agent。

[快速使用](#quickstart) · [分类目录](#catalog) · [安装](#installation) · [调用指南](#agent-interface) · [常见问题](docs/FAQ.zh-CN.md)

[下载完整资料包](downloads/awesome-defensive-writing.zip) · [下载 Skill](downloads/yila-clear-writing.zip)

## 它解决什么问题

文字交给 AI 后，明确的判断有时会变成“可能在一定程度上”“需要谨慎看待”“仍有待进一步研究”。这套提示词帮助你识别空泛限定，写清观点、证据、条件与行动，适用于论文、项目、汇报、邮件、产品文案和技术说明。

| 场景 | 修改前 | 修改后 |
|---|---|---|
| 已确认的交付安排 | 我们可能尽量争取周四交付，情况比较复杂。 | 原型周四交付，随后进入测试。 |
| 观察研究的发现 | 结果可能在一定程度上提示 A 或许与 B 存在某种联系。 | 在本单中心观察研究中，A 与 B 呈正相关。 |

[查看完整案例：输入事实、修改结果和理由 →](docs/library/zh/examples.md)


<a id="quickstart"></a>

## 快速使用

```text
请把下面文字改得清楚、直接，让读者看见观点、依据和下一步。
删除空泛限定与重复的自我保护句。
保留事实、适用范围、真实不确定性与已经作出的承诺。
原文超出证据的地方，依据材料纠正。
先给修改后的正文，再简要说明重要修改。

正文：[粘贴正文]
读者与用途：[填写]
支持材料：[粘贴事实或来源]
```

<a id="catalog"></a>

## 按任务选择

| 类别 | 模板数 | 可以先解决的问题 |
|---|---:|---|
| [清晰表达](docs/library/zh/clarity.md) | 6 | 这句话到底增加了什么信息 |
| [论文与研究](docs/library/zh/research.md) | 6 | 润色时保持结论强度 |
| [项目与基金](docs/library/zh/proposals.md) | 6 | 把泛泛风险变成具体触发条件与措施 |
| [职场汇报](docs/library/zh/work.md) | 6 | 说明延期、阻塞与新安排 |
| [邮件与协作](docs/library/zh/collaboration.md) | 6 | 清楚求助、异议、拒绝和道歉 |
| [产品与营销](docs/library/zh/product.md) | 6 | 写清能力、资格和实际条件 |
| [内容与公共表达](docs/library/zh/public.md) | 6 | 有观点，也不夸大证据 |
| [教学与技术说明](docs/library/zh/technical.md) | 6 | 精简说教，保留操作前提 |
| [数据与分析](docs/library/zh/analysis.md) | 6 | 保留分母、区间与性能代价 |
| [学习与日常](docs/library/zh/learning.md) | 6 | 给出具体下一步，不虚构熟练程度 |

## 精选模板

<!-- FEATURED_START -->
<details>
<summary>DW-002 · 最小改动润色</summary>

```text
将给定材料写得清楚、直接、有信息量。
以读者需要知道的判断或行动为主线，删除重复退让与空泛铺垫。
事实、数字、范围、责任与承诺性质以材料为准；
真实条件放在对应结论旁。
缺失的关键事实单列待确认。

任务：优先保留原句结构与作者声音，只改影响理解的词句。
区分语法、组织和主张强度的变化，不把温和措辞机械改成强硬措辞。

输出：可直接替换的正文；
再列最重要的语言或结构修改。

输入材料：
原文：[填写]
作者希望保留的语气：[填写]
```

[看输入、改写与理由](docs/library/zh/examples.md#ex-01)

</details>

<details>
<summary>DW-012 · 回复审稿意见</summary>

```text
将给定材料写得清楚、直接、有信息量。
以读者需要知道的判断或行动为主线，删除重复退让与空泛铺垫。
事实、数字、范围、责任与承诺性质以材料为准；
真实条件放在对应结论旁。
缺失的关键事实单列待确认。

任务：逐点判断意见成立程度，先回应实质问题，再说明已完成修改与位置。
未执行的分析写成计划；
不自动完全同意，不虚构页码或实验。

输出：逐点回复：意见判断、回应、实际修改、待补工作。

输入材料：
审稿意见：[填写]
证据：[填写]
实际完成的修改：[填写]
```

[看输入、改写与理由](docs/library/zh/examples.md#ex-04)

</details>

<details>
<summary>DW-020 · 延期说明</summary>

```text
将给定材料写得清楚、直接、有信息量。
以读者需要知道的判断或行动为主线，删除重复退让与空泛铺垫。
事实、数字、范围、责任与承诺性质以材料为准；
真实条件放在对应结论旁。
缺失的关键事实单列待确认。

任务：直接写原计划、当前变化、已知原因和恢复安排。
区分承诺日期与预计日期；
有责任时明确承担，不用情况复杂代替原因，不虚构补偿。

输出：一段可直接发送的延期说明，包含原计划、变化、原因和新安排。

输入材料：
原排期：[填写]
当前状态：[填写]
原因：[填写]
新安排：[填写]
```

[看输入、改写与理由](docs/library/zh/examples.md#ex-07)

</details>

<details>
<summary>DW-031 · 功能介绍</summary>

```text
将给定材料写得清楚、直接、有信息量。
以读者需要知道的判断或行动为主线，删除重复退让与空泛铺垫。
事实、数字、范围、责任与承诺性质以材料为准；
真实条件放在对应结论旁。
缺失的关键事实单列待确认。

任务：先写特定用户能完成什么，再写步骤与必要条件。
只用已确认能力，保留权限、费用、支持格式和内测范围，不承诺直接可投稿等未验证结果
。

输出：先用一句话说明用户能做什么，再给操作与必要条件。

输入材料：
已确认功能：[填写]
适用用户：[填写]
条件：[填写]
展示位置：[填写]
```

[看输入、改写与理由](docs/library/zh/examples.md#ex-11)

</details>
<!-- FEATURED_END -->


<a id="installation"></a>

## 安装 Skill

**Windows：**下载并解压 Skill 包，在解压后的文件夹中打开 PowerShell：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent codex
```

**macOS / Linux：**

```bash
bash ./install.sh --agent codex
```

Claude Code 用户将 `codex` 换成 `claude`。安装脚本会显示安装目录。完成后重新打开客户端，按下方调用指南使用。

[完整安装说明：手动复制、自定义目录、更新和卸载 →](docs/INSTALL.md)

<a id="agent-interface"></a>

## 调用指南 / Agent Interface

安装后，将下面内容发送到智能体对话中：

### Codex

```text
$yila-clear-writing 修改下面的段落，删去重复退让，写清观点和依据。
正文：[粘贴正文]
读者与用途：[填写]
支持材料：[粘贴事实、数据或来源]
输出：先给正文，再列重要修改理由。
```

### Claude Code

```text
/yila-clear-writing 修改下面的段落，删去重复退让，写清观点和依据。
正文：[粘贴正文]
读者与用途：[填写]
支持材料：[粘贴事实、数据或来源]
输出：先给正文，再列重要修改理由。
```

### 网页对话：ChatGPT / Claude / Gemini / Yila

复制[网页通用指令](docs/WEB-PROMPT.zh-CN.md)到新对话，随后发送自己的任务和正文；也可将该文件作为附件提供。按场景使用时，直接复制下方分类中的完整提示词。

**四种工作方式：**逐句诊断、直接改写、依据材料起草、推荐模板。想直接替换原文，在任务末尾加上“只输出修改后的正文”。

[完整调用指南：工作方式、输出控制和练习示例 →](docs/USAGE.zh-CN.md)


<a id="research"></a>

## 研究依据

本项目将论文讨论的无依据限定问题，转化为逐句诊断、段落改写与场景模板。研究说明按图解释了写作与评审过程、比较指标及提示词情境。

[阅读论文说明、原始图表与读图指南 →](docs/RESEARCH.zh-CN.md)

## 在 Yila 工作台使用

带论文、数据或研究笔记到 [Yila 工作台](https://yila.ai/research)，选择科研模板，完成段落诊断、改写和证据核对。日常写作可直接复制提示词，Agent 用户可安装本地 Skill。

## 参与与复用

[贡献提示词与案例](CONTRIBUTING.md) · [常见问题](docs/FAQ.zh-CN.md) · [来源与致谢](docs/SOURCES.md) · [许可说明](LICENSE.md)

觉得这套方法有用，可以 Star 留存；有实际改写经验，欢迎补充模板、案例与翻译。

## 开源协议 / License

本项目由 [Yila](https://yila.ai/research) 发起并开源维护，帮助更多人写出清楚、直接、有依据的文字。

原创提示词、案例与文档采用 [CC BY 4.0](LICENSES/CC-BY-4.0.txt)；Skill 入口、安装脚本与工具采用 [Apache-2.0](LICENSE)。论文图片保留原作者署名与许可。

[进入 Yila 工作台 →](https://yila.ai/research)
