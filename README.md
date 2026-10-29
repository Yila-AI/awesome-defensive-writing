# Awesome Defensive Writing · by Yila

**Anti-defensive writing prompts & agent skill**

Turn empty qualifications into clear judgments, evidence and action.

**English** | [简体中文](README.zh-CN.md)

**The problem at a glance: how an author's claim changes through AI revision and review.**

[![Research overview: author claims, GPT revisions, AI reviews and human readers](assets/paper/figure-1-overview.png)](assets/paper/figure-1-overview.png)

Image: Liao et al., [Defensive Writing in GPT Models](https://arxiv.org/abs/2610.11355v2), Figure 1, CC BY 4.0. [Figure guide and complete charts](docs/RESEARCH.md).

**60 bilingual prompts · 25 worked scenarios · 10 categories**

Copy a template for an occasional edit, or install the skill for repeat work.

[Quickstart](#quickstart) · [Catalog](#catalog) · [Install](#installation) · [Agent interface](#agent-interface) · [FAQ](docs/FAQ.md)

[Download the full library](downloads/awesome-defensive-writing.zip) · [Download the skill](downloads/yila-clear-writing.zip)

## What it helps you do

AI revisions can turn clear judgments into “may potentially suggest,” “should be interpreted cautiously” and “further research is needed.” Use this library to identify empty qualifications and state the claim, evidence, conditions and action across research, work, collaboration and product writing.

| Scenario | Before | After |
|---|---|---|
| A confirmed prototype delivery | We may try to aim for Thursday, although the situation is complex. | The prototype will be delivered on Thursday, followed by testing. |
| An observational finding | The results may to some extent suggest some connection between A and B. | In this single-center observational study, A and B were positively correlated. |

[Read the complete cases: facts, revisions and reasoning →](docs/library/en/examples.md)


<a id="quickstart"></a>

## Quickstart

```text
Edit the passage so the reader can identify the point, evidence and next step.
Remove empty qualifications and repeated self-protection.
Keep the facts, scope, uncertainty and actual commitments.
Correct claims that overstate the supplied evidence.
Return the revised copy, then explain material changes.

Passage: [paste text]
Audience and purpose: [fill in]
Supporting material: [paste facts or sources]
```

<a id="catalog"></a>

## Find your task

| Category | Prompts | A useful starting point |
|---|---:|---|
| [Clear expression](docs/library/en/clarity.md) | 6 | Diagnose what a sentence contributes |
| [Research writing](docs/library/en/research.md) | 6 | Polish prose without changing claim strength |
| [Proposals](docs/library/en/proposals.md) | 6 | Turn vague risks into triggers and responses |
| [Work updates](docs/library/en/work.md) | 6 | State a delay, blocker and revised arrangement |
| [Collaboration](docs/library/en/collaboration.md) | 6 | Ask, disagree or apologize without empty retreat |
| [Product writing](docs/library/en/product.md) | 6 | Describe capabilities with real access conditions |
| [Public communication](docs/library/en/public.md) | 6 | Explain a point without universal claims |
| [Technical guidance](docs/library/en/technical.md) | 6 | Keep prerequisites and operational restrictions |
| [Data interpretation](docs/library/en/analysis.md) | 6 | Retain denominators, intervals and trade-offs |
| [Learning and everyday writing](docs/library/en/learning.md) | 6 | Give checkable next steps without false mastery |

## Selected templates

<!-- FEATURED_START -->
<details>
<summary>DW-002 · Minimal editing</summary>

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Keep the author's voice and sentence structure where they work. Separate
grammar and organization edits from changes in claim strength; do not
mechanically make mild phrasing forceful.

Output: Replacement copy followed by the most important language or structural
edits.

Input material:
Draft: [fill in]
Tone to preserve: [fill in]
```

[See facts, revision and reasoning](docs/library/en/examples.md#ex-01)

</details>

<details>
<summary>DW-012 · Reviewer response</summary>

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: Assess each objection and answer its substance before reporting completed
edits and locations. Label unperformed analyses as plans; do not invent
agreement, page numbers or experiments.

Output: A point-by-point response: assessment, answer, completed changes and
remaining work.

Input material:
Reviewer comments: [fill in]
Evidence: [fill in]
Completed changes: [fill in]
```

[See facts, revision and reasoning](docs/library/en/examples.md#ex-04)

</details>

<details>
<summary>DW-020 · Delay notice</summary>

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: State the original plan, change, known cause and recovery arrangement.
Distinguish committed dates from estimates; acknowledge responsibility and
avoid invented remedies.

Output: A sendable delay notice containing the original plan, change, cause and
revised arrangement.

Input material:
Original schedule: [fill in]
Status: [fill in]
Cause: [fill in]
Revised arrangement: [fill in]
```

[See facts, revision and reasoning](docs/library/en/examples.md#ex-07)

</details>

<details>
<summary>DW-031 · Feature description</summary>

```text
Make the supplied material clear, direct and informative. Organize it around
the judgment or action the reader needs. Remove repetitive retreat and empty
preambles. Ground facts, numbers, scope, responsibility and commitments in
the material; keep meaningful conditions next to the claims they qualify.
List missing facts separately.

Task: State what eligible users can do, then steps and conditions. Use verified
capabilities and retain access, pricing, formats and beta scope without
unverified quality promises.

Output: One sentence describing the user capability, followed by actions and
necessary conditions.

Input material:
Verified feature: [fill in]
Eligible users: [fill in]
Conditions: [fill in]
Placement: [fill in]
```

[See facts, revision and reasoning](docs/library/en/examples.md#ex-11)

</details>
<!-- FEATURED_END -->


<a id="installation"></a>

## Install the skill

**Windows:** extract the skill ZIP and open PowerShell in the folder containing install.ps1:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent codex
```

**macOS / Linux:**

```bash
bash ./install.sh --agent codex
```

For Claude Code, replace `codex` with `claude`. The installer prints the destination. Reopen your client, then follow the invocation guide below.

[Full installation guide: manual copy, custom paths, updates and removal →](docs/INSTALL.md)

<a id="agent-interface"></a>

## Agent interface

After installation, send a request in your agent conversation:

### Codex

```text
$yila-clear-writing Revise the passage for a clear point and evidence.
Passage: [paste text]
Audience and purpose: [fill in]
Supporting material: [paste facts, data or sources]
Output: revised copy first, then reasons for material changes.
```

### Claude Code

```text
/yila-clear-writing Revise the passage for a clear point and evidence.
Passage: [paste text]
Audience and purpose: [fill in]
Supporting material: [paste facts, data or sources]
Output: revised copy first, then reasons for material changes.
```

### Web conversations: ChatGPT / Claude / Gemini / Yila

Copy the [standalone web instructions](docs/WEB-PROMPT.md) into a new conversation, then add your task and passage. You can also attach that file with your request. For a specific scenario, copy a complete template from the [catalog](docs/library/en/index.md).

**Web instructions** support diagnosis, revision and drafting. The **installed skill** also recommends prompts from its local library. Add “return clean copy only” for text you can replace directly.

[Full usage guide: modes, output controls and a worked request →](docs/USAGE.md)


<a id="research"></a>

## Research background

The library turns the paper's discussion of ungrounded qualifications into sentence-level diagnosis, passage revision and task-specific prompts. The research guide explains the writing and review process, comparison measures and prompt contexts.

[Read the research background, original figures and figure guide →](docs/RESEARCH.md)

## Use in the Yila workbench

Copy a suitable prompt from this library, then send it with papers, data or research notes to the [Yila workbench](https://yila.ai/research) to diagnose, revise and check the passage against that material. Use copied prompts for everyday writing or install the local skill in your agent.

## Contribute and reuse

[Contribute prompts and cases](CONTRIBUTING.md) · [FAQ](docs/FAQ.md) · [Boundary quick reference](docs/BOUNDARIES.md) · [Sources and acknowledgments](docs/SOURCES.md) · [Licensing](LICENSE.md)

Star the collection to keep it handy. Share a useful prompt, a worked case or a translation to help it grow.

## License

An open-source project created and maintained by [Yila](https://yila.ai/research), helping people write with clarity, directness and evidence.

Original prompts, cases and documentation: [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Skill entrypoint, installers and tooling: [Apache-2.0](LICENSE). Paper images retain the original authors' attribution and license.

[Open the Yila workbench →](https://yila.ai/research)
