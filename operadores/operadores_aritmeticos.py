# Operadores arimeticos, permiten realizar operaciones entre variables

numero_1 = 5
numero_2 = 7
numero_3 = 9

nombre = "Leonardo"
apellido = "Gonzalez"

# Operador suma

suma = numero_1 + numero_2
print(suma)
concatenacion = nombre + " " + apellido
print(concatenacion)

# Permite unir unidades numericas o textos, eso se llama "concatenación"

# Operador Resta

resta = numero_1 - numero_2
print(resta)

# Operador Multiplicación

multiplicacion = numero_1 * numero_2
print(multiplicacion)
multiplicar_texto = nombre * numero_1
print(multiplicar_texto)
exponente= numero_1 ** numero_2
print(exponente) 

# puedes multiplicar textos con lentras, ademas de numeros con numeros

# Operador division
division = numero_3 / numero_1
print(type(division))

division_baja = numero_3 // numero_1
print(division_baja)
print(type(division_baja))

print(f"{numero_3 / numero_2:.10f}")

# (f"{numero_3 / numero_2:.10f}") ":.X" determina la cantida de decimales que quieres mostrar

# Operador RESTO

op_resto = numero_3 % numero_2
print(op_resto)