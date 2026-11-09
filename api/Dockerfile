
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       openssh-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

COPY ../scripts/cargar_resultados.py .

EXPOSE 5000

COPY iniciar.sh /usr/local/bin/iniciar.sh

RUN sed -i 's/\r$//' /usr/local/bin/iniciar.sh \
    && chmod +x /usr/local/bin/iniciar.sh

CMD ["/bin/bash", "/usr/local/bin/iniciar.sh"]
