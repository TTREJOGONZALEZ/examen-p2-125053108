
$version = "3.3.6"
$archivo = "hadoop/hadoop-$version.tar.gz"

$url = "https://downloads.apache.org/hadoop/common/hadoop-$version/hadoop-$version.tar.gz"

if (Test-Path $archivo) {
    Write-Host "Hadoop ya esta descargado."
}
else {
    Write-Host "Descargando Hadoop $version..."

    Invoke-WebRequest `
        -Uri $url `
        -OutFile $archivo

    Write-Host "Descarga completada."
}

Write-Host "Listo para construir Docker."
