
#!/usr/bin/env python3

import sys
from decimal import Decimal, InvalidOperation

clave_actual = None
total = Decimal("0.00")

for linea in sys.stdin:
    try:
        clave, valor = linea.strip().split("\t", 1)
        ingreso = Decimal(valor)

        if clave_actual == clave:
            total += ingreso
        else:
            if clave_actual is not None:
                print(f"{clave_actual}\t{total:.2f}")

            clave_actual = clave
            total = ingreso

    except (ValueError, InvalidOperation):
        continue

# Mostrar el ultimo grupo
if clave_actual is not None:
    print(f"{clave_actual}\t{total:.2f}")
