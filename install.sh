#!/bin/sh
set -eu
agent=codex
dest=
force=0
while [ "$#" -gt 0 ]; do
    case "$1" in
        --agent) [ "$#" -ge 2 ] || { echo 'Missing --agent value' >&2; exit 2; }; agent=$2; shift 2 ;;
        --dest) [ "$#" -ge 2 ] || { echo 'Missing --dest value' >&2; exit 2; }; dest=$2; shift 2 ;;
        --force) force=1; shift ;;
        --help) echo 'Usage: bash install.sh [--agent codex|claude] [--dest SKILLS_DIRECTORY] [--force]'; exit 0 ;;
        *) echo "Unknown option: $1" >&2; exit 2 ;;
    esac
done
case "$agent" in codex|claude) ;; *) echo 'Choose codex or claude' >&2; exit 2 ;; esac
script_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
source_dir=$script_root/skills/yila-clear-writing
[ -f "$source_dir/SKILL.md" ] || source_dir=$script_root
[ -f "$source_dir/SKILL.md" ] || { echo 'Cannot find SKILL.md beside the installer' >&2; exit 1; }
if [ -z "$dest" ]; then
    if [ "$agent" = claude ]; then dest=$HOME/.claude/skills; else dest=$HOME/.agents/skills; fi
fi
mkdir -p -- "$dest"
dest=$(CDPATH= cd -- "$dest" && pwd -P)
target=$dest/yila-clear-writing
if [ "$source_dir" = "$target" ]; then echo "Already installed: $target"; exit 0; fi
case "$target" in "$source_dir"/*) echo 'Choose an installation path outside the source skill folder' >&2; exit 1 ;; esac
[ ! -L "$target" ] || { echo 'Choose a destination without a link at yila-clear-writing' >&2; exit 1; }
if [ -e "$target" ] && [ "$force" -ne 1 ]; then
    echo "Already installed: $target. Use --force to update and keep a backup." >&2
    exit 1
fi
stage=$(mktemp -d "$(dirname -- "$dest")/.yila-clear-writing-stage.XXXXXX")
cp -R "$source_dir/." "$stage/"
[ -f "$stage/references/manifest.json" ] || { echo "Incomplete package at $stage" >&2; exit 1; }
if [ -e "$target" ]; then
    backup_root=$(dirname -- "$dest")/yila-clear-writing-backups
    [ ! -L "$backup_root" ] || { echo 'Choose a backup directory without a link' >&2; exit 1; }
    mkdir -p -- "$backup_root"
    backup_root=$(CDPATH= cd -- "$backup_root" && pwd -P)
    backup=$backup_root/backup-$(date +%Y%m%d%H%M%S)-$$
    [ ! -e "$backup" ] || { echo 'Backup path already exists' >&2; exit 1; }
    mv -- "$target" "$backup"
    echo "Previous version: $backup"
fi
mv -- "$stage" "$target"
echo "Installed: $target"
if [ "$agent" = claude ]; then echo 'Use: /yila-clear-writing'; else echo 'Use: $yila-clear-writing'; fi
