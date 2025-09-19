"""
El propósito de este programa es que basado en un año dado, este te dira si es bisiesto o no, siguiendo unas reglas
Eduardo Caleb Castillo Llanas 18/Sep/25
"""

# Declaraciones
#CONSTANTE = valor

# Entradas
año = int(input())

# Proceso
if (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0):
    print("Así")
else:
    print("No")
