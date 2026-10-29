# Contributing · 参与贡献

欢迎通过 Issue 或 PR 提交提示词、改写案例、条件保留纠错和翻译修订。投稿表单分为内容、问题反馈和翻译三类。

Submit prompts, cases, boundary corrections and translations through Issues or pull requests. Issue forms cover content, bugs and translation changes.

## 一个有用的投稿 / A useful submission

提供使用场景、完整输入、提示词、输出、修改理由、必须保留的边界和来源授权。删除私人信息；不能把他人的论文、邮件或平台截图直接当成自己的开放许可材料。

Include the task, full input, prompt, output, reasoning, material boundaries and source permissions. Remove private information and do not relicense other people's papers, emails or screenshots as your own work.

- 编辑示例：明确标记为人工编写，示例事实应完整支持推荐改写。
- 模型记录：保留完整原始输入输出、模型与日期；人工修改另列，不能伪装成原始输出。
- 翻译：保留稳定 ID，重点检查主张强度、责任、时间、数字和礼貌是否漂移。

- Editorial examples: label authorship and supply all facts needed for the revision.
- Model runs: retain original input/output, model and date; distinguish subsequent editorial changes.
- Translations: keep stable IDs and review claim strength, responsibility, timing, numbers and courtesy.

不要只用“更短了”证明更好。应解释删掉的部分有什么功能，删后有没有损失信息。

Shorter text alone is not evidence of improvement. Explain the removed material's function and any information loss.

## 维护数据 / Maintain the source

编辑 `data/prompts.json` 和 `data/examples.json`，运行：

Edit the JSON source and run:

```text
python tools/build_library.py
python tools/build_library.py --check
python tools/package_draft.py
python tools/check_packages.py
```

`docs/library` 和 Skill 的分类、案例与清单文件由脚本生成，不要直接维护重复副本。入口 Skill 与领域路由说明可独立编辑。

The library pages and the skill's category, example and manifest files are generated. Edit their JSON source rather than maintaining duplicate copies. The skill entrypoint and scenario guidance are maintained separately.

原创内容的贡献应按 [许可说明](LICENSE.md) 中对应的许可证提交；保留第三方作者与许可信息。

Contribute original work under the applicable [license](LICENSE.md) and retain third-party attribution.
