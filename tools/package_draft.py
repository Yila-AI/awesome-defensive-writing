"""Build downloadable source and standalone-skill ZIPs."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
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
        manifest = json.loads((source / 'references/manifest.json').read_text(encoding='utf-8'))
        readmes = json.loads((ROOT / 'data/package-readmes.json').read_text(encoding='utf-8'))
        for language, filename in [('en', 'README.md'), ('zh', 'README.zh-CN.md')]:
            text = readmes[language].replace('[PROMPT_COUNT]', str(manifest['prompt_count'])).replace('[EXAMPLE_COUNT]', str(manifest['example_count']))
            add(archive, 'yila-clear-writing/' + filename, text.encode('utf-8'))
    inspect(path)


def source_package():
    path = OUT / 'awesome-defensive-writing.zip'
    with ZipFile(path, 'w') as archive:
        for item in sorted(ROOT.rglob('*')):
            relative = item.relative_to(ROOT)
            if not item.is_file() or any(p in EXCLUDE for p in relative.parts):
                continue
            if relative.parts[0] == 'downloads':
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
        add(archive, 'awesome-defensive-writing/downloads/yila-clear-writing.zip', (OUT / 'yila-clear-writing.zip').read_bytes())
    inspect(path)


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    skill_package()
    source_package()
