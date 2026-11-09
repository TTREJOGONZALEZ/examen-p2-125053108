
# Parte E - Teoría del Segundo Parcial

**Matrícula:** 125053108

## 1. Modos de Hadoop

En modo standalone, Hadoop trabaja en una sola máquina
sin utilizar HDFS. En modo pseudo-distribuido, los
servicios funcionan en una misma máquina, pero como
procesos independientes y utilizando HDFS. En modo
totalmente distribuido, Hadoop trabaja con varios
servidores conectados y también utiliza HDFS.

## 2. ¿Por qué utilizar volúmenes en Docker?

Utilizamos volúmenes porque permiten acceder al dataset
sin copiarlo dentro de la imagen. Esto evita aumentar
innecesariamente el tamaño de la imagen de Docker.
También permite actualizar los archivos sin tener que
reconstruir toda la imagen.

## 3. Diferencia entre docker compose down y down -v

El comando docker compose down elimina los contenedores
y las redes creadas por Compose, pero conserva los
volúmenes nombrados de la base de datos.
En cambio, docker compose down -v también elimina
esos volúmenes, provocando la pérdida de sus datos.

## 4. ¿Por qué MapReduce no siempre es más rápido?

MapReduce necesita tiempo para iniciar y coordinar
sus tareas. Con archivos relativamente pequeños,
como nuestro CSV de 352 MB, ese tiempo adicional
puede hacerlo más lento que Python secuencial.
Conviene más cuando se procesan grandes cantidades
de datos distribuidos entre varios equipos.

## 5. Diferencias entre instrucciones de Docker

CMD establece el comando predeterminado al iniciar
un contenedor, mientras que ENTRYPOINT define su
ejecutable principal. COPY copia archivos locales
a la imagen. ADD también puede extraer archivos
comprimidos locales y obtener recursos desde URLs,
pero COPY suele ser preferible para copias simples.
