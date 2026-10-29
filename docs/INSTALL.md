# 下载与安装 / Download and install

[中文首页](../README.zh-CN.md) · [English home](../README.md)

## 1. 下载 / Download

| 你要做什么 / Goal | 下载 / Download |
|---|---|
| 浏览全部提示词、案例和论文图片 / Browse everything | [完整资料包 / Full library ZIP](../downloads/awesome-defensive-writing.zip) |
| 在自己的 Agent 中使用 / Install in your agent | [Skill ZIP](../downloads/yila-clear-writing.zip) |
| 直接复制 / Copy a prompt | [中文目录](library/zh/index.md) · [English catalog](library/en/index.md) |

下载后解压，进入包含 `install.ps1` 和 `install.sh` 的文件夹。完整资料包和 Skill 单独包都提供这两个安装文件。

Extract the ZIP and open the folder containing `install.ps1` and `install.sh`. Both packages include these installers.

## 2. Windows

在该文件夹打开 PowerShell，选择你的客户端：

Open PowerShell in that folder and choose your client:

**Codex**

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent codex
```

**Claude Code**

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent claude
```

## 3. macOS / Linux

在解压后的文件夹打开终端：

Open a terminal in the extracted folder:

**Codex**

```bash
bash ./install.sh --agent codex
```

**Claude Code**

```bash
bash ./install.sh --agent claude
```

## 4. 安装位置 / Destinations

| 客户端 / Client | 用户目录 / User-level directory | 项目目录 / Project-level directory |
|---|---|---|
| Codex | `~/.agents/skills/yila-clear-writing/` | `.agents/skills/yila-clear-writing/` |
| Claude Code | `~/.claude/skills/yila-clear-writing/` | `.claude/skills/yila-clear-writing/` |

`~` 表示用户主目录。安装脚本默认选择用户目录，并在完成后显示完整路径。

`~` means your home directory. The installer uses the user-level location by default and prints the full path.

路径依据：[OpenAI 官方说明](https://learn.chatgpt.com/docs/build-skills) · [Claude Code 官方说明](https://code.claude.com/docs/en/skills)。

## 5. 开始使用 / Invoke

重新打开客户端，输入：

Reopen the client and enter:

**Codex**

```text
用 $yila-clear-writing 修改下面这段文字，给出正文和重要修改理由。
正文：……
读者与用途：……
支持材料：……
```

**Claude Code**

```text
/yila-clear-writing 修改下面这段文字，给出正文和重要修改理由。
正文：……
读者与用途：……
支持材料：……
```

也可以让它找模板：`给我一套用于延期说明的完整提示词`。

You can also ask for a template: `Find a complete prompt for a delay notice.`

## 6. 手动安装 / Manual installation

完整资料包中，复制 `skills/yila-clear-writing`；Skill 单独包中，复制解压得到的 `yila-clear-writing` 文件夹，放到上表对应的 skills 目录。保留整个文件夹结构：

From the full library, copy `skills/yila-clear-writing`. From the skill ZIP, copy the extracted `yila-clear-writing` folder into the corresponding skills directory, keeping its structure:

```text
skills/
└── yila-clear-writing/
    ├── SKILL.md
    ├── agents/
    ├── references/
    ├── LICENSES/
    └── LICENSE.md
```

## 7. 自定义目录 / Custom destination

`Dest` / `--dest` 指向 skills 父目录，脚本会在其中创建 `yila-clear-writing`。

The destination is the parent skills directory. The installer creates `yila-clear-writing` inside it.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Dest "D:\My Project\.agents\skills"
```

```bash
bash ./install.sh --dest "/path/to/project/.agents/skills"
```

使用自己配置的目录时，把实际路径传给安装脚本。

For a custom client configuration, pass its actual skills directory.

## 8. 更新 / Update

在新版解压目录中运行原安装命令，并添加 `-Force` 或 `--force`。脚本保留旧版备份，并显示备份路径。

Run the installer from the new package with `-Force` or `--force`. It preserves the previous version and prints the backup location.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent codex -Force
```

```bash
bash ./install.sh --agent codex --force
```

## 9. 卸载 / Remove

在安装目录删除 `yila-clear-writing` 文件夹，重新打开客户端。备份文件夹可按需要保留。

Delete the installed `yila-clear-writing` folder and reopen the client. Keep backup folders if you need them.

## 10. 直接用提示词 / Use prompts directly

打开 [中文目录](library/zh/index.md) 或 [English catalog](library/en/index.md)，复制模板并填入材料，即可在自己的写作工具中使用。也可带论文材料到 [Yila](https://yila.ai/research) 处理研究写作。

Open a catalog, copy a prompt and add your material in your preferred tool. For research writing, you can also bring your paper to [Yila](https://yila.ai/research).
