"""Build downloadable source and standalone-skill ZIPs."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
import shutil
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'downloads'
EXCLUDE = {'.git', '.local', '__pycache__'}


def add(archive, name, content):
    info = ZipInfo(name.replace('\\', '/'), date_time=(2026, 10, 29, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = (0o100755 if name.endswith('.sh') else 0o100644) << 16
    archive.writestr(info, content)


def inspect(path):
    with ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise ValueError('Archive integrity check failed')
        if any(any(p in EXCLUDE for p in Path(n).parts) for n in archive.namelist()):
            raise ValueError('Excluded material in package')
    print(f'{path.name}: {path.stat().st_size:,} bytes')


def skill_package():
    path = OUT / 'yila-clear-writing.zip'
    source = ROOT / 'skills/yila-clear-writing'
    with ZipFile(path, 'w') as archive:
        for item in sorted(source.rglob('*')):
            if item.is_file() and not any(p in EXCLUDE for p in item.relative_to(source).parts):
                if item.is_symlink():
                    raise ValueError(f'Refusing to bundle symlink: {item}')
                add(archive, 'yila-clear-writing/' + item.relative_to(source).as_posix(), item.read_bytes())
        for name in ('install.ps1', 'install.sh'):
            add(archive, 'yila-clear-writing/' + name, (ROOT / name).read_bytes())
        for name in ('USAGE.zh-CN.md', 'USAGE.md', 'WEB-PROMPT.zh-CN.md', 'WEB-PROMPT.md'):
            text = (ROOT / 'docs' / name).read_text(encoding='utf-8')
            text = text.replace('../README.zh-CN.md', '../README.md')
            text = text.replace('(INSTALL.md)', '(../README.md)')
            for lang in ('zh', 'en'):
                text = text.replace(f'library/{lang}/index.md', f'../references/catalog-{lang}.md')
                text = text.replace(f'library/{lang}/examples.md', f'../references/examples-{lang}.md')
            add(archive, 'yila-clear-writing/guides/' + name, text.encode('utf-8'))
        readme = '''# Yila Clear Writing · 安装与使用

60 套双语提示词、24 组情景案例。安装后调用 Skill，或打开 references 文件夹复制提示词。

## Windows

在本文件夹打开 PowerShell，选择客户端：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\\install.ps1 -Agent codex
powershell -NoProfile -ExecutionPolicy Bypass -File .\\install.ps1 -Agent claude
```

## macOS / Linux

```bash
bash ./install.sh --agent codex
bash ./install.sh --agent claude
```

Choose the command for your client. The installer prints its destination.
Defaults: Codex `~/.agents/skills`, Claude Code `~/.claude/skills`.
Use `-Dest` / `--dest` for a custom parent skills directory.
Add `-Force` / `--force` when updating; the installer retains the previous version.
Backups are stored in yila-clear-writing-backups beside the skills directory.

重新打开客户端。Codex 中用 `$yila-clear-writing`，Claude Code 中用 `/yila-clear-writing`。

[中文调用指南](guides/USAGE.zh-CN.md) · [English usage guide](guides/USAGE.md)

网页对话可复制 [中文通用指令](guides/WEB-PROMPT.zh-CN.md) 或 [English web instructions](guides/WEB-PROMPT.md)。

Reopen the client. Invoke `$yila-clear-writing` in Codex or `/yila-clear-writing` in Claude Code.
For manual installation, copy this entire folder into the client's skills directory.
To remove, delete the installed yila-clear-writing folder and reopen the client.

[Yila](https://yila.ai/research) · [OpenAI installation paths](https://learn.chatgpt.com/docs/build-skills) · [Claude Code skills](https://code.claude.com/docs/en/skills)
'''
        manifest = json.loads((source / 'references/manifest.json').read_text(encoding='utf-8'))
        readme = readme.replace('60 套双语提示词、24 组情景案例。', f"{manifest['prompt_count']} 套双语提示词、{manifest['example_count']} 组情景案例。")
        add(archive, 'yila-clear-writing/README.md', readme.encode('utf-8'))
    inspect(path)


def source_package():
    path = OUT / 'awesome-defensive-writing.zip'
    with ZipFile(path, 'w') as archive:
        for item in sorted(ROOT.rglob('*')):
            relative = item.relative_to(ROOT)
            if not item.is_file() or any(p in EXCLUDE for p in relative.parts):
                continue
            if relative.parts[0] == 'downloads' and item.name != 'yila-clear-writing.zip':
                continue
            if item.is_symlink():
                raise ValueError(f'Refusing to bundle symlink: {item}')
            content = item.read_bytes()
            if relative.as_posix() in ('README.md', 'README.zh-CN.md', 'docs/INSTALL.md'):
                text = content.decode('utf-8')
                text = text.replace('[下载完整资料包](downloads/awesome-defensive-writing.zip)', '[资料包使用说明](docs/INSTALL.md)')
                text = text.replace('[Download the full library](downloads/awesome-defensive-writing.zip)', '[Library instructions](docs/INSTALL.md)')
                text = text.replace('[完整资料包 / Full library ZIP](../downloads/awesome-defensive-writing.zip)', '[资料包目录 / Library contents](../README.zh-CN.md)')
                content = text.encode('utf-8')
            add(archive, 'awesome-defensive-writing/' + relative.as_posix(), content)
    inspect(path)


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    skill_package()
    source_package()
    # Keep earlier local download links usable.
    legacy = ROOT / '.local/packages'
    legacy.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(OUT / 'awesome-defensive-writing.zip', legacy / 'awesome-defensive-writing-draft.zip')
    shutil.copyfile(OUT / 'yila-clear-writing.zip', legacy / 'yila-clear-writing-draft.zip')
