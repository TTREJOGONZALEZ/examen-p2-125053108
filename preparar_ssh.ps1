
$carpeta = "ssh"
$llave = "$carpeta/id_ed25519"

if (!(Test-Path $carpeta)) {
    New-Item -ItemType Directory -Path $carpeta | Out-Null
}

if (!(Test-Path $llave)) {
    Write-Host "Generando llaves SSH..."

    ssh-keygen -t ed25519 -N '""' -f $llave

    Write-Host "Llaves SSH generadas."
}
else {
    Write-Host "Las llaves SSH ya existen."
}

Write-Host "Configuracion SSH lista."
