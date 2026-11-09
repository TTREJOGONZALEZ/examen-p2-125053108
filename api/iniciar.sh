#!/bin/bash
set -e

mkdir -p /root/.ssh
chmod 700 /root/.ssh

if [ -f /tmp/cliente_ssh ]; then
    cp /tmp/cliente_ssh /root/.ssh/id_ed25519
    chmod 600 /root/.ssh/id_ed25519
fi

echo "Configuracion SSH completada"

# Iniciar Flask
python /app/app.py &

# Cargar resultados si existen
if [ -f /data/output/resultado/part-00000 ]; then
    echo "Cargando resultados en MySQL..."
    python /app/scripts/cargar_resultados.py
fi

wait