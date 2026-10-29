"""Build the bilingual Markdown library from editorial JSON. Standard library only."""
import argparse
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/yila-clear-writing'


def read_data():
    catalog = json.loads((ROOT / 'data/prompts.json').read_text(encoding='utf-8'))
    examples = json.loads((ROOT / 'data/examples.json').read_text(encoding='utf-8'))['examples']
    ids = [p['id'] for p in catalog['prompts']]
    example_ids = [e['id'] for e in examples]
    if len(ids) != len(set(ids)) or len(example_ids) != len(set(example_ids)):
        raise ValueError('Duplicate prompt or example ID')
    categories = {c['id'] for c in catalog['categories']}
    prompts = set()
    for p in catalog['prompts']:
        if p['category'] not in categories or p['example_id'] not in example_ids:
            raise ValueError(f"Invalid category or example: {p['id']}")
        for lang in ('zh', 'en'):
            if not p['title'][lang].strip() or len(p['prompt'][lang]) < 100:
                raise ValueError(f"Missing content: {p['id']} {lang}")
            if not p['required_inputs'][lang] or not p['output'][lang].strip():
                raise ValueError(f"Missing input/output contract: {p['id']} {lang}")
            if p['prompt'][lang] in prompts:
                raise ValueError(f"Duplicate prompt: {p['id']}")
            prompts.add(p['prompt'][lang])
    for e in examples:
        for field in ('title', 'facts', 'verbose_or_flawed', 'revision', 'why', 'preserve'):
            if any(not e[field][lang].strip() for lang in ('zh', 'en')):
                raise ValueError(f"Missing example content: {e['id']} {field}")
    return catalog, examples


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='\n') as handle:
        handle.write(text.rstrip() + '\n')


def build(catalog, examples):
    count = len(catalog['prompts'])
    case_count = len(examples)
    example_map = {e['id']: e for e in examples}
    for lang in ('zh', 'en'):
        zh = lang == 'zh'
        target = ROOT / 'docs/library' / lang
        title = '按场景找提示词' if zh else 'Browse prompts by task'
        intro = ('选择任务，复制提示词，填入自己的材料；点击案例查看输入事实、修改结果与理由。' if zh else 'Choose a task, copy a prompt and add your material. Follow the case link for supplied facts, a revision and the reasoning behind it.')
        index = [f'# {title}', '', f'{count} prompts · {case_count} examples · 中文 / English', '', intro, '', '[简体中文](../zh/index.md) | [English](../en/index.md)', '', ('先看 [完整案例](examples.md) 或 [安装说明](../../INSTALL.md)。' if zh else 'Start with [complete examples](examples.md) or [installation](../../INSTALL.md).'), '', '| ' + ('类别 | 模板数 |' if zh else 'Category | Prompts |'), '|---|---:|']
        for cat in catalog['categories']:
            items = [p for p in catalog['prompts'] if p['category'] == cat['id']]
            index.append(f"| [{cat['title'][lang]}]({cat['id']}.md) | {len(items)} |")
            switch = f"[English](../en/{cat['id']}.md) | **简体中文**" if zh else f"**English** | [简体中文](../zh/{cat['id']}.md)"
            lines = [f"# {cat['title'][lang]}", '', switch, '', ('[全部分类](index.md)' if zh else '[All categories](index.md)'), '', intro, '']
            lines += [f"- [{p['id']} {p['title'][lang]}](#{p['id'].lower()})" for p in items]
            for p in items:
                e = example_map[p['example_id']]
                lines += ['', f'<a id="{p["id"].lower()}"></a>', '', f"## {p['id']} · {p['title'][lang]}", '', '```text', p['prompt'][lang], '```', '', '<details>', f"<summary>{'查看相关案例' if zh else 'See a related case'} · {e['id']} · {e['title'][lang]}</summary>", '']
                for field, label in [('facts', '输入事实' if zh else 'Facts'), ('verbose_or_flawed', '修改前' if zh else 'Before'), ('revision', '修改后' if zh else 'After'), ('why', '修改理由' if zh else 'Reason')]:
                    lines += [f'**{label}**', '', e[field][lang], '']
                lines += [f"[{'完整案例与保留条件' if zh else 'Full case and conditions to preserve'}](examples.md#{e['id'].lower()})", '', '</details>']
            write(target / f"{cat['id']}.md", '\n'.join(lines))
            # The installed skill contains local copies: it needs no network or repo-level paths.
            skill_switch = f"[English]({cat['id']}-en.md) | **简体中文**" if zh else f"**English** | [简体中文]({cat['id']}-zh.md)"
            skill_lines = [f"# {cat['title'][lang]}", '', skill_switch, '', intro]
            for p in items:
                skill_lines += ['', f"## {p['id']} · {p['title'][lang]}", '', p['prompt'][lang], '', f"Related case: {p['example_id']} in examples-{lang}.md"]
            write(SKILL / 'references' / f"{cat['id']}-{lang}.md", '\n'.join(skill_lines))
        write(target / 'index.md', '\n'.join(index))
        local_index = [f'# {title}', '', ('选择分类，再复制对应提示词。' if zh else 'Choose a category and copy the matching prompt.'), '']
        local_index += [f"- [{c['title'][lang]}]({c['id']}-{lang}.md)" for c in catalog['categories']]
        local_index += ['', f"[{'完整案例' if zh else 'Worked examples'}](examples-{lang}.md)"]
        write(SKILL / 'references' / f'catalog-{lang}.md', '\n'.join(local_index))
        example_switch = '[English](../en/examples.md) | **简体中文**' if zh else '**English** | [简体中文](../zh/examples.md)'
        lines = [('# 完整改写案例' if zh else '# Complete writing examples'), '', example_switch, '', '[目录 / Index](index.md)', '', ('以下情景案例依次给出输入事实、问题稿、推荐改写与修改理由。选取相近的任务，替换为自己的材料即可练习。' if zh else 'These constructed scenarios provide the facts, a flawed draft, a suggested revision and editing reasons. Choose a similar task and substitute your own material to practice.'), '']
        lines += [f"- [{e['id']} {e['title'][lang]}](#{e['id'].lower()})" for e in examples]
        for e in examples:
            lines += ['', f'<a id="{e["id"].lower()}"></a>', f"## {e['id']} · {e['title'][lang]}"]
            for field, label_zh, label_en in [('facts', '输入事实', 'Supplied facts'), ('verbose_or_flawed', '冗余或错误稿', 'Verbose or flawed draft'), ('revision', '推荐改写', 'Suggested revision'), ('why', '为什么这样改', 'Why'), ('preserve', '必须保留的边界', 'Boundary to preserve')]:
                lines += ['', f'**{label_zh if zh else label_en}**', '', e[field][lang]]
        write(target / 'examples.md', '\n'.join(lines))
        # Remove the repository navigation link for the standalone install.
        standalone = '\n'.join(lines).replace('[目录 / Index](index.md)\n', '')
        standalone = standalone.replace('../en/examples.md', 'examples-en.md').replace('../zh/examples.md', 'examples-zh.md')
        write(SKILL / 'references' / f'examples-{lang}.md', standalone)
    manifest = {'schema_version': 1, 'prompt_count': count, 'example_count': case_count, 'languages': ['zh', 'en'], 'content_type': 'prompt-library', 'categories': []}
    for c in catalog['categories']:
        manifest['categories'].append({'id': c['id'], 'title': c['title'], 'files': {lang: f"{c['id']}-{lang}.md" for lang in ('zh', 'en')}})
    write(SKILL / 'references/manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2))
    print(f'Built {count} bilingual prompts and {case_count} bilingual editorial examples.')


def markdown_anchors(text):
    result = set(re.findall(r'\bid=["\']([^"\']+)["\']', text))
    seen = {}
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, flags=re.M):
        heading = re.sub(r'<[^>]+>', '', heading).strip().lower()
        slug = ''.join(c for c in heading if not unicodedata.category(c).startswith('P') or c in '-_')
        slug = re.sub(r'\s', '-', slug)
        index = seen.get(slug, 0)
        seen[slug] = index + 1
        result.add(slug + (f'-{index}' if index else ''))
    return result


def check_links():
    errors = []
    for path in ROOT.rglob('*.md'):
        if any(part in ('.local', '.git') for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding='utf-8')
        text = re.sub(r'```.*?```', '', text, flags=re.S)
        for raw in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', text):
            if re.match(r'^[a-z]+:', raw):
                continue
            if raw.startswith('#'):
                if unquote(raw[1:]) not in markdown_anchors(text):
                    errors.append(f'Missing page anchor: {path.relative_to(ROOT)} -> {raw}')
                continue
            target, _, anchor = raw.partition('#')
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f'{path.relative_to(ROOT)} -> {raw}')
            elif anchor and resolved.suffix == '.md':
                body = resolved.read_text(encoding='utf-8')
                if unquote(anchor) not in markdown_anchors(re.sub(r'```.*?```', '', body, flags=re.S)):
                    errors.append(f'Missing anchor: {raw}')
    if errors:
        raise ValueError('\n'.join(errors))
    print('Local Markdown links and generated case anchors are valid.')


def update_featured(catalog, examples):
    for language, filename in [('zh', 'README.zh-CN.md'), ('en', 'README.md')]:
        path = ROOT / filename
        text = path.read_text(encoding='utf-8')
        n, e, c = len(catalog['prompts']), len(examples), len(catalog['categories'])
        if language == 'zh':
            text = re.sub(r'\*\*\d+ 套中英文提示词 · \d+ 组情景案例 · \d+ 类场景\*\*', f'**{n} 套中英文提示词 · {e} 组情景案例 · {c} 类场景**', text)
        else:
            text = re.sub(r'\*\*\d+ bilingual prompts · \d+ worked scenarios · \d+ categories\*\*', f'**{n} bilingual prompts · {e} worked scenarios · {c} categories**', text)
        for category in catalog['categories']:
            count = sum(p['category'] == category['id'] for p in catalog['prompts'])
            pattern = rf'(\]\(docs/library/{language}/{category["id"]}\.md\) \| )\d+( \|)'
            text = re.sub(pattern, lambda m: m[1] + str(count) + m[2], text)
        cards = []
        for prompt_id in ('DW-002', 'DW-012', 'DW-020', 'DW-031'):
            p = next(p for p in catalog['prompts'] if p['id'] == prompt_id)
            case_label = '看输入、改写与理由' if language == 'zh' else 'See facts, revision and reasoning'
            cards.append(f"<details>\n<summary>{p['id']} · {p['title'][language]}</summary>\n\n```text\n{p['prompt'][language]}\n```\n\n[{case_label}](docs/library/{language}/examples.md#{p['example_id'].lower()})\n\n</details>")
        replacement = '<!-- FEATURED_START -->\n' + '\n\n'.join(cards) + '\n<!-- FEATURED_END -->'
        text, count = re.subn(r'<!-- FEATURED_START -->.*?<!-- FEATURED_END -->', lambda _: replacement, text, flags=re.S)
        if count != 1:
            raise ValueError(f'Missing featured-template markers: {filename}')
        write(path, text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Validate data and links without regenerating')
    args = parser.parse_args()
    catalog, examples = read_data()
    if not args.check:
        build(catalog, examples)
        update_featured(catalog, examples)
    check_links()
