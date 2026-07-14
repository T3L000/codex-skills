[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Name,

    [string]$Destination,

    [switch]$Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ($Name -notmatch '^[a-z0-9]+(?:-[a-z0-9]+)*$') {
    throw 'Skill ID may contain only lowercase letters, digits, and hyphens.'
}

$RepoRoot = Split-Path -Parent $PSScriptRoot
$CatalogPath = Join-Path $RepoRoot 'catalog\skills.yaml'
$Resolver = Join-Path $PSScriptRoot 'validate-catalog.py'

if (-not $Destination) {
    if ($env:CODEX_HOME) {
        $Destination = Join-Path $env:CODEX_HOME 'skills'
    } else {
        $Destination = Join-Path $env:USERPROFILE '.codex\skills'
    }
}

$Source = (& python $Resolver $CatalogPath --resolve $Name 2>&1 | Out-String).Trim()
if ($LASTEXITCODE -ne 0) {
    throw $Source
}

$Source = [System.IO.Path]::GetFullPath($Source)
$Destination = [System.IO.Path]::GetFullPath($Destination)
$Target = Join-Path $Destination $Name

New-Item -ItemType Directory -Path $Destination -Force | Out-Null
if (Test-Path -LiteralPath $Target) {
    if (-not $Force) {
        throw "Target already exists: $Target. Use -Force to replace it explicitly."
    }
    Remove-Item -LiteralPath $Target -Recurse -Force
}

Copy-Item -LiteralPath $Source -Destination $Target -Recurse
Write-Output "Installed $Name to $Target"
