"""Exercise installer behavior in temporary destinations, without changing user skills."""
import argparse
import hashlib
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def run(command, cwd, success=True):
    result = subprocess.run(command, cwd=str(cwd), capture_output=True, text=True, timeout=45)
    if (result.returncode == 0) != success:
        raise AssertionError(f'{command}: {result.stdout}\n{result.stderr}')


def check(name, command, flag, force_flag, cwd, destination, source):
    run(command + [flag, str(destination)], cwd)
    resolved_destination = destination if destination.is_absolute() else (cwd / destination).resolve()
    target = resolved_destination / 'yila-clear-writing'
    assert (target / 'references/manifest.json').is_file()
    for item in source.rglob('*'):
        if item.is_file():
            relative = item.relative_to(source)
            assert (target / relative).read_bytes() == item.read_bytes(), relative
    marker = target / 'keep-my-notes.txt'
    marker.write_text('previous version customization', encoding='utf-8')
    before = hashlib.sha256((target / 'SKILL.md').read_bytes()).digest()
    run(command + [flag, str(destination)], cwd, success=False)
    assert marker.exists()
    assert hashlib.sha256((target / 'SKILL.md').read_bytes()).digest() == before
    backup_root = resolved_destination.parent / 'yila-clear-writing-backups'
    previous_backups = set(backup_root.glob('backup-*'))
    run(command + [flag, str(destination), force_flag], cwd)
    assert not (target / marker.name).exists()
    backups = list(set(backup_root.glob('backup-*')) - previous_backups)
    assert len(backups) == 1 and (backups[0] / marker.name).read_text(encoding='utf-8') == 'previous version customization'
    discovered = list(resolved_destination.glob('*/SKILL.md'))
    assert discovered == [target / 'SKILL.md'], discovered
    assert (target / 'SKILL.md').read_bytes() == (source / 'SKILL.md').read_bytes()
    print(f'PASS {name}: initial install, intact references, duplicate refusal, backup update')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--powershell', default=shutil.which('pwsh') or shutil.which('powershell'))
    parser.add_argument('--bash', default=shutil.which('bash'))
    args = parser.parse_args()
    work = ROOT / '.local/installer-tests'
    work.mkdir(parents=True, exist_ok=True)
    session = Path(tempfile.mkdtemp(prefix='run-', dir=work))
    with zipfile.ZipFile(ROOT / 'downloads/yila-clear-writing.zip') as archive:
        archive.extractall(session / 'extracted')
    packed = session / 'extracted/yila-clear-writing'
    source = ROOT / 'skills/yila-clear-writing'
    if args.powershell:
        for mode, cwd, folder in [('source', ROOT, source), ('zip', packed, packed)]:
            command = [args.powershell, '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', str(cwd / 'install.ps1')]
            check(f'PowerShell {mode}', command, '-Dest', '-Force', cwd, session / ('ps ' + mode), folder)
    if args.bash:
        # Relative destinations keep this portable between POSIX and Git Bash on Windows.
        for mode, cwd, folder in [('source', ROOT, source), ('zip', packed, packed)]:
            destination = session / ('shell ' + mode)
            import os
            relative = os.path.relpath(destination, cwd).replace('\\', '/')
            command = [args.bash, './install.sh']
            check(f'Bash {mode}', command, '--dest', '--force', cwd, Path(relative), folder)
