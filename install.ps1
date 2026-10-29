[CmdletBinding()]
param(
    [ValidateSet('codex', 'claude')][string]$Agent = 'codex',
    [string]$Dest,
    [switch]$Force
)
$ErrorActionPreference = 'Stop'

if (-not $Dest) {
    $Dest = if ($Agent -eq 'claude') { Join-Path $HOME '.claude/skills' } else { Join-Path $HOME '.agents/skills' }
}
$source = Join-Path $PSScriptRoot 'skills/yila-clear-writing'
if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md'))) { $source = $PSScriptRoot }
if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md'))) { throw 'Cannot find yila-clear-writing/SKILL.md beside this installer.' }
$source = (Resolve-Path -LiteralPath $source).Path
$installRoot = [IO.Path]::GetFullPath($Dest)
New-Item -ItemType Directory -Path $installRoot -Force | Out-Null
$installRoot = (Resolve-Path -LiteralPath $installRoot).Path.TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
$target = [IO.Path]::GetFullPath((Join-Path $installRoot 'yila-clear-writing'))
if ([IO.Path]::GetDirectoryName($target) -ne $installRoot) { throw 'Invalid installation path.' }
if ($source -eq $target) { Write-Output "Already installed: $target"; return }
if ($target.StartsWith($source.TrimEnd([IO.Path]::DirectorySeparatorChar) + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { throw 'Choose an installation path outside the source skill folder.' }
if (Test-Path -LiteralPath $target) {
    if ((Get-Item -LiteralPath $target).Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Choose an installation directory without a link at yila-clear-writing.' }
    if (-not $Force) { throw "Already installed: $target. Use -Force to update and keep a backup." }
}
$suffix = [Guid]::NewGuid().ToString('N')
$installParent = [IO.Path]::GetDirectoryName($installRoot)
$stage = [IO.Path]::GetFullPath((Join-Path $installParent ".yila-clear-writing-stage-$suffix"))
if ([IO.Path]::GetDirectoryName($stage) -ne $installParent) { throw 'Invalid staging path.' }
$backupRoot = [IO.Path]::GetFullPath((Join-Path $installParent 'yila-clear-writing-backups'))
$backup = [IO.Path]::GetFullPath((Join-Path $backupRoot "backup-$suffix"))
if ([IO.Path]::GetDirectoryName($backup) -ne $backupRoot) { throw 'Invalid backup path.' }
Copy-Item -LiteralPath $source -Destination $stage -Recurse
if (-not (Test-Path -LiteralPath (Join-Path $stage 'references/manifest.json'))) { throw "Incomplete package at $stage" }
if (Test-Path -LiteralPath $target) {
    New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
    if ((Get-Item -LiteralPath $backupRoot).Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Choose a backup directory without a link.' }
    Move-Item -LiteralPath $target -Destination $backup
    Write-Output "Previous version: $backup"
}
Move-Item -LiteralPath $stage -Destination $target
Write-Output "Installed: $target"
if ($Agent -eq 'claude') { Write-Output 'Use: /yila-clear-writing' } else { Write-Output 'Use: $yila-clear-writing' }
