[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$TargetPath,

    [string]$Category = "projects",

    [string]$LinkName,

    [string]$VaultPath,

    [switch]$NoIndexRefresh
)

$ErrorActionPreference = "Stop"

$resolvedTarget = Resolve-Path -LiteralPath $TargetPath -ErrorAction Stop
$targetFullPath = $resolvedTarget.ProviderPath
$targetItem = Get-Item -LiteralPath $targetFullPath -Force

if (-not $targetItem.PSIsContainer) {
    throw "Target path must be a directory: $targetFullPath"
}

if ([string]::IsNullOrWhiteSpace($LinkName)) {
    $LinkName = Split-Path -Path $targetFullPath -Leaf
}

if ([string]::IsNullOrWhiteSpace($Category)) {
    throw "Category cannot be empty."
}

if ($LinkName -match '[\\/:*?"<>|]') {
    throw "LinkName contains invalid path characters: $LinkName"
}

$workspaceLinksPath = Split-Path -Path $PSScriptRoot -Parent
if ([string]::IsNullOrWhiteSpace($VaultPath)) {
    $VaultPath = Split-Path -Path $workspaceLinksPath -Parent
}

$base = Join-Path $VaultPath "workspace-links"
$categoryPath = Join-Path $base $Category
$linkPath = Join-Path $categoryPath $LinkName

New-Item -ItemType Directory -Path $categoryPath -Force | Out-Null

if (Test-Path -LiteralPath $linkPath) {
    $existing = Get-Item -LiteralPath $linkPath -Force
    if ($existing.Attributes -band [IO.FileAttributes]::ReparsePoint) {
        $existingTarget = (Get-Item -LiteralPath $linkPath -Force).Target
        if ($existingTarget -is [array]) {
            $existingTarget = ($existingTarget -join ", ")
        } else {
            $existingTarget = [string]$existingTarget
        }

        if ($existingTarget -eq $targetFullPath) {
            Write-Output "OK_EXISTS :: $linkPath -> $targetFullPath"
        } else {
            throw "Link exists with a different target: $linkPath -> $existingTarget"
        }
    } else {
        throw "Path already exists and is not a junction: $linkPath"
    }
} else {
    New-Item -ItemType Junction -Path $linkPath -Target $targetFullPath | Out-Null
    Write-Output "CREATED :: $linkPath -> $targetFullPath"
}

$mdCount = 0
if (Get-Command rg -ErrorAction SilentlyContinue) {
    $mdCount = (rg --files -g '*.md' $linkPath | Measure-Object).Count
} else {
    $mdCount = (Get-ChildItem -Path $linkPath -Recurse -File -Filter '*.md' | Measure-Object).Count
}
Write-Output "MD_COUNT :: $mdCount"

if (-not $NoIndexRefresh) {
    $toolsPath = Join-Path $base "_tools"
    $refreshScript = Join-Path $toolsPath "refresh-workspace-index.ps1"
    if (Test-Path -LiteralPath $refreshScript) {
        & $refreshScript -VaultPath $VaultPath | ForEach-Object { Write-Output $_ }
    }
}
