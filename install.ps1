$ErrorActionPreference = "Stop"

Write-Host "🤖 Installing Awesome OpenCode Skills..." -ForegroundColor Cyan

$InstallDir = Join-Path $HOME ".config\opencode\skills"
$TmpDir = Join-Path $env:TEMP "opencode-skills-tmp-$(Get-Random)"
$ZipFile = Join-Path $TmpDir "repo.zip"

if (-not (Test-Path $TmpDir)) {
    New-Item -ItemType Directory -Path $TmpDir | Out-Null
}

Write-Host "📥 Downloading skills pack..."
$Url = "https://github.com/jshsakura/awesome-opencode-skills/archive/refs/heads/main.zip"
Invoke-WebRequest -Uri $Url -OutFile $ZipFile

Write-Host "📦 Extracting files..."
Expand-Archive -Path $ZipFile -DestinationPath $TmpDir -Force

Write-Host "📂 Installing to $InstallDir..."
if (-not (Test-Path $InstallDir)) {
    New-Item -ItemType Directory -Path $InstallDir | Out-Null
}

Copy-Item -Path "$TmpDir\awesome-opencode-skills-main\skills\*" -Destination $InstallDir -Recurse -Force

Write-Host "🧹 Cleaning up..."
Remove-Item -Path $TmpDir -Recurse -Force

Write-Host "✅ Successfully installed all skills to $InstallDir" -ForegroundColor Green
Write-Host "🚀 You can now use these skills in OpenCode!" -ForegroundColor Yellow
