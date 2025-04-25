import math
# funciones con numeros

numeros = [4,6,2,9,25]

print(f"El numero mayor es: {max(numeros)}")
print(f"El numero menor es: {min(numeros)}")

numero = 12.3456
print("")
print(f"Redondear un decimal {round(numero)}")
print(f"Redondear un decimal {round(numero,2)}")
print(f"Truncar un decimal {math.trunc(numero)}")
print(f"aproximar al entero superior {math.ceil(numero)}")
print(f"valor abosulto de {math.fabs(-45)}")
print(f"Raíz cuadrada de 9= {math.sqrt(9)}")
print(f"Raíz cúbica de 16 = {math.cbrt(16)}")
print(f"sumatoria de 4+6+2+9+25 = {math.fsum(numeros)}")