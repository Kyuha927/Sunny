[CmdletBinding()]
param(
    [string]$VaultPath
)

$ErrorActionPreference = "Stop"

$workspaceLinksPath = Split-Path -Path $PSScriptRoot -Parent
if ([string]::IsNullOrWhiteSpace($VaultPath)) {
    $VaultPath = Split-Path -Path $workspaceLinksPath -Parent
}

$base = Join-Path $VaultPath "workspace-links"
if (-not (Test-Path -LiteralPath $base)) {
    throw "workspace-links folder not found: $base"
}

$categories = Get-ChildItem -Path $base -Directory -Force |
    Where-Object { $_.Name -notin @("_tools", "_catalog") } |
    Sort-Object Name

$lines = @()
$lines += "# Workspace Links"
$lines += ""
$lines += "Obsidian vault entry points to external work folders via junction."
$lines += ""
$lines += "## Project Classification"
$lines += "- [[workspace-links/_catalog/00_project_dashboard]]"
$lines += "- [[workspace-links/_catalog/01_classification_taxonomy]]"
$lines += "- [[workspace-links/_catalog/02_project_intake_checklist]]"
$lines += "- [[workspace-links/_catalog/03_relationship_dashboard]]"
$lines += "- [[workspace-links/_catalog/04_execution_overview]]"
$lines += "- [[workspace-links/_catalog/05_kanban_execution]]"
$lines += ""

foreach ($category in $categories) {
    $lines += "## $($category.Name)"

    $entries = Get-ChildItem -Path $category.FullName -Directory -Force | Sort-Object Name
    if ($entries.Count -eq 0) {
        $lines += "- (none)"
        $lines += ""
        continue
    }

    foreach ($entry in $entries) {
        $rel = "workspace-links/$($category.Name)/$($entry.Name)"
        $targetText = ""

        if ($entry.Attributes -band [IO.FileAttributes]::ReparsePoint) {
            $targetRaw = (Get-Item -LiteralPath $entry.FullName -Force).Target
            if ($targetRaw -is [array]) {
                $targetText = ($targetRaw -join ", ")
            } else {
                $targetText = [string]$targetRaw
            }
        }

        if ([string]::IsNullOrWhiteSpace($targetText)) {
            $lines += "- [[${rel}]]"
        } else {
            $lines += ('- [[{0}]] -> `{1}`' -f $rel, $targetText)
        }
    }

    $lines += ""
}

$lines += "## Usage"
$lines += '- Add link: `.\workspace-links\_tools\add-workspace-link.ps1 -TargetPath "C:\Projects\MyProject" -Category "projects"`'
$lines += "- Rename link target folder? Recreate the matching junction."

$indexPath = Join-Path $base "_index.md"
Set-Content -Path $indexPath -Value ($lines -join "`r`n") -Encoding UTF8

Write-Output "INDEX_UPDATED :: $indexPath"
