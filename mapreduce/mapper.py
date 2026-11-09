
#!/usr/bin/env python3

import sys
import csv
from decimal import Decimal, InvalidOperation

for linea in sys.stdin:
    try:
        datos = next(csv.reader([linea]))

        # Ignorar encabezado y registros incompletos
        if len(datos) != 8 or datos[0] == "id":
            continue

        fecha_hora = datos[1]
        categoria = datos[3]
        cantidad = int(datos[5])
        precio = Decimal(datos[6])

        # Extraer la hora de la fecha
        hora = int(fecha_hora[11:13])

        if not 0 <= hora <= 23:
            continue

        if cantidad < 0 or precio < 0 or not categoria:
            continue

        # Calcular ingreso de cada venta
        ingreso = cantidad * precio

        # Emitir clave y valor
        print(f"{hora:02d}|{categoria}\t{ingreso:.2f}")

    except (ValueError, IndexError, InvalidOperation,
            csv.Error):
        # Ignorar registros mal formados
        continue
