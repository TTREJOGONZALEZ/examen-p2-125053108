
$ErrorActionPreference = "Stop"

$version = "3.3.6"
$carpeta = Join-Path $PSScriptRoot "hadoop"
$archivo = Join-Path $carpeta "hadoop-$version.tar.gz"

$url = "https://archive.apache.org/dist/hadoop/common/hadoop-$version/hadoop-$version.tar.gz"

if (!(Test-Path $carpeta)) {
    New-Item -ItemType Directory -Path $carpeta | Out-Null
}

if (Test-Path $archivo) {
    Write-Host "Hadoop ya esta descargado."
}
else {
    Write-Host "Descargando Hadoop $version..."

    Invoke-WebRequest -Uri $url -OutFile $archivo

    Write-Host "Descarga completada."
}

Write-Host "Preparacion de Hadoop finalizada."
s