
#!/bin/bash
set -e

mkdir -p /run/sshd /root/.ssh /data/output
chmod 700 /root/.ssh

# Configurar llave SSH local
if [ ! -f /root/.ssh/id_ed25519 ]; then
    ssh-keygen -t ed25519 -N "" \
        -f /root/.ssh/id_ed25519
fi

chmod 600 /root/.ssh/id_ed25519
touch /root/.ssh/authorized_keys

grep -qxF "$(cat /root/.ssh/id_ed25519.pub)" \
    /root/.ssh/authorized_keys \
    || cat /root/.ssh/id_ed25519.pub \
       >> /root/.ssh/authorized_keys

# Autorizar llave de Flask
if [ -f /tmp/cliente_ssh.pub ]; then
    grep -qxF "$(cat /tmp/cliente_ssh.pub)" \
        /root/.ssh/authorized_keys \
        || cat /tmp/cliente_ssh.pub \
           >> /root/.ssh/authorized_keys
fi

chmod 600 /root/.ssh/authorized_keys

/usr/sbin/sshd
echo "SSH iniciado correctamente"

# Procesar dataset si no existen resultados
if [ ! -f /data/output/resultado/part-00000 ]; then
    echo "Iniciando procesamiento MapReduce..."

    rm -rf /data/output/resultado

    hadoop jar "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -D mapreduce.framework.name=local \
        -D mapreduce.job.reduces=1 \
        -input /data/input/ventas_125053108.csv \
        -output /data/output/resultado \
        -mapper "python3 /app/mapreduce/mapper.py" \
        -reducer "python3 /app/mapreduce/reducer.py"

    echo "MapReduce completado"
else
    echo "Los resultados de Hadoop ya existen"
fi

exec tail -f /dev/null
