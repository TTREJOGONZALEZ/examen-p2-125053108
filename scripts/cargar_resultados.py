
import os
import mysql.connector
from decimal import Decimal

archivo = "/data/output/resultado/part-00000"

conexion = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "db"),
    port=int(os.getenv("MYSQL_PORT", "3306")),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cursor = conexion.cursor()
registros = 0

with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
        clave, ingreso = linea.strip().split("\t")
        hora, categoria = clave.split("|")

        cursor.execute("""
            INSERT INTO resultados (hora, categoria, ingreso_total)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
                ingreso_total = VALUES(ingreso_total)
        """, (int(hora), categoria, Decimal(ingreso)))

        registros += 1

conexion.commit()

print(f"Resultados procesados y cargados: {registros}")

cursor.close()
conexion.close()
