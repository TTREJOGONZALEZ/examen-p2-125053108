
import csv
import time
from decimal import Decimal, InvalidOperation
from collections import defaultdict

inicio = time.perf_counter()

archivo = "data/ventas_125053108.csv"
salida = "resultados/secuencial.txt"

totales = defaultdict(lambda: Decimal("0.00"))
registros_validos = 0

with open(archivo, "r", newline="", encoding="utf-8") as f:
    lector = csv.reader(f)
    next(lector, None)

    for datos in lector:
        try:
            if len(datos) != 8:
                continue

            hora = int(datos[1][11:13])
            categoria = datos[3]
            cantidad = int(datos[5])
            precio = Decimal(datos[6])

            if not 0 <= hora <= 23:
                continue

            if cantidad < 0 or precio < 0 or not categoria:
                continue

            ingreso = cantidad * precio
            clave = f"{hora:02d}|{categoria}"

            totales[clave] += ingreso
            registros_validos += 1

        except (ValueError, IndexError, InvalidOperation):
            continue

with open(salida, "w", encoding="utf-8") as f:
    for clave in sorted(totales):
        f.write(f"{clave}\t{totales[clave]:.2f}\n")

fin = time.perf_counter()

print("Procesamiento secuencial completado")
print(f"Registros procesados: {registros_validos}")
print(f"Resultados generados: {len(totales)}")
print(f"Tiempo total: {fin - inicio:.3f} segundos")
print(f"Archivo generado: {salida}")
