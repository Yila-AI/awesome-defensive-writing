# Agent interface and usage

[Home](../README.md) · [简体中文](USAGE.zh-CN.md) · [Installation](INSTALL.md)

## 1. Codex

After installation, send this in the Codex conversation:

```text
$yila-clear-writing Revise the passage for a clear point and evidence.

Passage: [paste text]
Audience and purpose: [fill in]
Supporting material: [paste facts, data or sources]
Output: usable copy first, then the reasons for material changes.
```

## 2. Claude Code

Send this in the Claude Code conversation:

```text
/yila-clear-writing Revise the passage for a clear point and evidence.

Passage: [paste text]
Audience and purpose: [fill in]
Supporting material: [paste facts, data or sources]
Output: usable copy first, then the reasons for material changes.
```

## 3. Web conversations: ChatGPT / Claude / Gemini / Yila

Open the [standalone web instructions](WEB-PROMPT.md), copy the complete instructions into a new conversation and add your text and supporting material. You can also attach that file with your task.

For a specific writing task, copy the matching template from the [catalog](library/en/index.md) and fill in its material.

## 4. Choose a mode

| Mode | Request | Output |
|---|---|---|
| Diagnose | Identify what each suspect sentence contributes and explain the proposed action. | Original, function, action and reason |
| Revise | Make the necessary edits while preserving facts and voice. | Usable revised copy |
| Draft | Write for the given audience using the supplied facts. | A new task-focused draft |
| Recommend | Find a complete delay-notice prompt with its ID and case link. | A copyable template and case |

Example diagnostic request in Codex:

```text
$yila-clear-writing Diagnose this passage.
Return original wording, information function, proposed action and reason.
Passage: [paste text]
Supporting material: [paste material]
```

## 5. Control the output

- **Clean copy:** return only the revised passage.
- **Review changes:** show original wording, revision and reason; list missing evidence separately.
- **Preserve voice:** keep the author's tone and terminology, making minimal changes.
- **Translate:** output Chinese while retaining facts and claim strength.
- **Limit length:** keep it under 150 words while preserving essential facts and actions.

## 6. A complete practice request

```text
$yila-clear-writing Revise this update. Return clean copy only.

Facts: page development is complete; API access is pending; integration testing has not started.
The meeting confirmed moving delivery of a testable build from Tuesday to Thursday.
The project manager is asked to coordinate access today.
Draft: Overall progress is good and we are working very hard.
Due to complexity, there might be a slight delay; thank you for understanding.
```

Example revision:

> Page development is complete, but API access is pending and integration testing has not started. Delivery of a testable build moves from Tuesday to Thursday. Please coordinate API access today.

For Claude Code, use `/yila-clear-writing`. For web conversations, provide the [standalone instructions](WEB-PROMPT.md) before the task.

[Explore 24 worked scenarios →](library/en/examples.md)
