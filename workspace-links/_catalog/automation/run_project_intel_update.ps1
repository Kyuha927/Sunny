param(
  [int]$LookbackDays = 30,
  [int]$MaxItems = 10,
  [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonExe = "python"
$runner = Join-Path $scriptDir "update_project_intel.py"
$config = Join-Path $scriptDir "project_intel_sources.json"

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$updatesLogDir = Join-Path (Split-Path -Parent $scriptDir) "updates\\_logs"
if (-not (Test-Path -LiteralPath $updatesLogDir)) {
  New-Item -ItemType Directory -Path $updatesLogDir | Out-Null
}
$logPath = Join-Path $updatesLogDir "project_intel_update_$timestamp.log"

$args = @(
  $runner,
  "--config", $config,
  "--lookback-days", $LookbackDays,
  "--max-items", $MaxItems
)

if ($DryRun) {
  $args += "--dry-run"
}

"[INFO] Start: $(Get-Date -Format s)" | Tee-Object -FilePath $logPath -Append | Out-Null
"[INFO] Command: $pythonExe $($args -join ' ')" | Tee-Object -FilePath $logPath -Append | Out-Null

& $pythonExe @args 2>&1 | Tee-Object -FilePath $logPath -Append

$exitCode = $LASTEXITCODE
"[INFO] ExitCode: $exitCode" | Tee-Object -FilePath $logPath -Append | Out-Null
"[INFO] End: $(Get-Date -Format s)" | Tee-Object -FilePath $logPath -Append | Out-Null

exit $exitCode
