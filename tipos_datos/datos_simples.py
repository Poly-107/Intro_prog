# textos de una sola linea
Texto_1 = "Texto 1: texto de una sola linea"
Texto_2 = 'Texto 2: texto de una sola linea'

# textos de varias lineas
texto_3 ='''texto 3: texto con
Multiples
Lineas'''

print(Texto_1)
print(Texto_2)
print(texto_3)

# tipo de darto numerico
# numeros enteros = INTEGERS = INT
numero_entero = 49
numtxt = "50"
print(numero_entero)
print(type(numero_entero))

# Decimales, float
numero_decimal = 49.5
print(numero_decimal)
print(type(numero_decimal))

# Datos lógicos, booleano, BOOL, boolean (falso, verdadero)
dato_booleano = True
print(dato_booleano)
print(type(dato_booleano))

#saludo xd
Nombre = "Leonardo xdd"
edad = 24
print("kiubo " + Nombre)
print("kiubo", Nombre)
#sin "STR" (string) no puedes concatenar un dato INT en tu cadena de codigo
print("kiubo " + Nombre + ", tas viejo, tienes " + str(edad) + " años xd")

print(numero_entero*numero_entero)
#en este caso, "int(numtxt)" convierte lo que es un texto, a un dato integer
print(numero_entero+int(numtxt))

#el str y el int son conversiones explicitas
print(f"kiubo {Nombre}, tas viejo, tines {edad} años xd ")
#en ese caso "F" se refiere a que es necesario formatear todos los datos como texto
#una conversión implicita