"""Compare committed downloads with freshly built archive contents, recursively."""
import io
from pathlib import Path
import runpy
import tempfile
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def compare(actual, expected, label):
    with ZipFile(io.BytesIO(actual)) as left, ZipFile(io.BytesIO(expected)) as right:
        if left.testzip() is not None or right.testzip() is not None:
            raise ValueError(f'Corrupt package: {label}')
        if set(left.namelist()) != set(right.namelist()):
            raise ValueError(f'Package entries are stale: {label}')
        for name in left.namelist():
            a, b = left.read(name), right.read(name)
            if left.getinfo(name).external_attr != right.getinfo(name).external_attr:
                raise ValueError(f'Package permissions differ: {label}/{name}')
            if name.endswith('.zip'):
                compare(a, b, f'{label}/{name}')
            elif a != b:
                raise ValueError(f'Package content is stale: {label}/{name}')


if __name__ == '__main__':
    local = ROOT / '.local'
    local.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='package-check-', dir=local) as directory:
        namespace = runpy.run_path(str(ROOT / 'tools/package_draft.py'), run_name='package_builder')
        namespace['skill_package'].__globals__['OUT'] = Path(directory)
        namespace['skill_package']()
        namespace['source_package']()
        for filename in ('yila-clear-writing.zip', 'awesome-defensive-writing.zip'):
            compare((ROOT / 'downloads' / filename).read_bytes(), (Path(directory) / filename).read_bytes(), filename)
    print('Download packages match the current source, guides and nested skill archive.')
