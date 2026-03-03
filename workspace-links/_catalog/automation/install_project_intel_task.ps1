param(
  [string]$TaskName = "Obsidian_Project_Intel_Update",
  [string]$DailyAt = "08:30",
  [int]$LookbackDays = 30,
  [int]$MaxItems = 10
)

$ErrorActionPreference = "Stop"

if ($DailyAt -notmatch "^\d{2}:\d{2}$") {
  throw "DailyAt 형식이 잘못되었습니다. 예: 08:30"
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$runner = Join-Path $scriptDir "run_project_intel_update.ps1"

if (-not (Test-Path -LiteralPath $runner)) {
  throw "실행 스크립트를 찾을 수 없습니다: $runner"
}

$triggerTime = [datetime]::ParseExact($DailyAt, "HH:mm", $null)
$actionArgs = "-NoProfile -ExecutionPolicy Bypass -File `"$runner`" -LookbackDays $LookbackDays -MaxItems $MaxItems"
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument $actionArgs
$trigger = New-ScheduledTaskTrigger -Daily -At $triggerTime
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($null -ne $existing) {
  Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

Register-ScheduledTask `
  -TaskName $TaskName `
  -Action $action `
  -Trigger $trigger `
  -Settings $settings `
  -Description "Obsidian project intelligence updater" `
  -Force | Out-Null

Write-Output "설치 완료: $TaskName"
Write-Output "실행 시각: 매일 $DailyAt"
Write-Output "실행 인자: $actionArgs"
