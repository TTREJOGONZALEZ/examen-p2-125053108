
$ErrorActionPreference = "Stop"

$carpeta = Join-Path $PSScriptRoot "ssh"
$llave = Join-Path $carpeta "id_ed25519"
$publica = "$llave.pub"

if (!(Test-Path $carpeta)) {
    New-Item -ItemType Directory -Path $carpeta | Out-Null
}

if (!(Test-Path $llave)) {
    Write-Host "Generando llaves SSH..."

    ssh-keygen -t ed25519 -N '""' -f $llave

    if ($LASTEXITCODE -ne 0) {
        throw "No se pudieron generar las llaves SSH."
    }
}

if (!(Test-Path $publica)) {
    Write-Host "Recuperando llave publica..."

    ssh-keygen -y -f $llave | Out-File `
        -FilePath $publica `
        -Encoding ascii

    if ($LASTEXITCODE -ne 0) {
        throw "No se pudo generar la llave publica."
    }
}

Write-Host "Llaves SSH listas."
