
# Examen Segundo Parcial - Pipeline de Datos Contenerizado

**Materia:** Manejo Masivo de Datos  
**Matrícula:** 125053108

## Objetivo

Construir un pipeline de datos utilizando Docker, Hadoop
MapReduce, MySQL y una API Flask.

## Pregunta de negocio

Calcular el ingreso total por hora del día (0-23)
y categoría de productos.

Ingreso = cantidad * precio_unitario

## Tecnologías utilizadas

- Docker y Docker Compose
- Debian 12
- Hadoop 3.3.6
- Python 3
- MySQL 8
- Flask
- SSH

## Dataset

Se generaron 5,000,000 de registros de ventas
utilizando la matrícula 125053108.

Tamaño: 352.2 MB.

El archivo CSV no se incluye en GitHub.

## Resultados

Se obtuvieron 240 combinaciones de hora y categoría.

### Comparativa de rendimiento

| Método | Tiempo |
|---|---|
| Hadoop MapReduce | 162.412 segundos |
| Python secuencial | 39.064 segundos |

Los 240 resultados coincidieron entre ambos métodos.

Python secuencial fue aproximadamente 4.16 veces
más rápido. Esto se debe a que Hadoop se ejecutó
en modo standalone y tiene costos adicionales
de inicialización y coordinación de tareas.

## Ejecución

1. Instalar Docker Desktop.
2. Clonar el repositorio.
3. Crear el archivo .env a partir de .env.example
   y configurar contraseñas seguras.
4. Generar el dataset con:

   python generar_dataset.py 125053108

5. Preparar las llaves SSH locales.
6. Construir y levantar los servicios con:

   docker compose up --build

## API

GET /resultados

GET /resultados/Electronica

POST /resultados

URL local: http://localhost:5000

## Persistencia

MySQL utiliza un volumen nombrado para conservar
la información al ejecutar docker compose down.

## Evidencias

Las capturas de Hadoop, SSH, MapReduce,
Flask y MySQL se encuentran en evidencias/.
