param(
    [string]$OutDir = "C:\Users\jhk92\OneDrive\문서\Obsidian Vault\copilot\perplexity-tools\out",
    [int]$Index = 0
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $OutDir)) {
    Write-Host "[FAIL] out dir not found: $OutDir"
    exit 1
}

$files = Get-ChildItem -Path $OutDir -File -Filter "*.prompt.md" | Sort-Object Name
if (-not $files -or $files.Count -eq 0) {
    Write-Host "[FAIL] no prompt files in: $OutDir"
    exit 1
}

$cursorPath = Join-Path $OutDir ".cursor.txt"
if ($Index -le 0) {
    $cursor = 1
    if (Test-Path $cursorPath) {
        $raw = (Get-Content $cursorPath -ErrorAction SilentlyContinue | Select-Object -First 1)
        if ($raw -match "^[0-9]+$") { $cursor = [int]$raw + 1 }
    }
    $Index = $cursor
}

if ($Index -gt $files.Count) {
    Write-Host "[DONE] no more prompts. total=$($files.Count)"
    exit 0
}

$file = $files[$Index - 1]
$content = Get-Content -Raw -Path $file.FullName
Set-Clipboard -Value $content
Set-Content -Path $cursorPath -Value $Index -Encoding UTF8

Write-Host "[OK] copied index=$Index file=$($file.Name)"
Write-Host "Paste into Perplexity, then run this script again for next file."
