
FROM debian:12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    openjdk-17-jdk-headless \
    python3 \
    openssh-server \
    openssh-client \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV HADOOP_HOME=/opt/hadoop
ENV PATH="${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin:${PATH}"


COPY hadoop-3.3.6.tar.gz /tmp/hadoop.tar.gz

RUN mkdir -p ${HADOOP_HOME} \
    && tar -xzf /tmp/hadoop.tar.gz \
       -C ${HADOOP_HOME} --strip-components=1 \
    && rm /tmp/hadoop.tar.gz


RUN mkdir -p /run/sshd /data/input /data/output

WORKDIR /app


COPY iniciar.sh /usr/local/bin/iniciar.sh

RUN sed -i 's/\r$//' /usr/local/bin/iniciar.sh \
    && chmod +x /usr/local/bin/iniciar.sh

CMD ["/bin/bash", "/usr/local/bin/iniciar.sh"]
