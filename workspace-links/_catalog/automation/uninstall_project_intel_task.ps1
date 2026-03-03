param(
  [string]$TaskName = "Obsidian_Project_Intel_Update"
)

$ErrorActionPreference = "Stop"

schtasks /Delete /TN $TaskName /F
Write-Output "삭제 완료: $TaskName"
