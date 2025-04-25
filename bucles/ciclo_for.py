# el ciclo For se usa normalmente para iterar elementos
# elementos que vienen de diccionarios, listas o conjuntos de datos
# (listas, conjuntos, diccionarios, tuplas)

Juegos = ["Dota 2", "Counter Strike", "Mario Party 9", "Hades"]
Numeros = [10,20,30,40,50]

for juego in Juegos:
    print(juego)

print("")

for Numero in Numeros:
    resultado = Numero * Numero
    print(f"{Numero}*{Numero}= {resultado}")

print(" ")

for Num in range(10):
    print(Num)

print(" ")

for Num in range(10,21): # desde donde hasta donde
    print(Num)

print(" ")

for Num in range(5,51,5):  # desde donde hasta donde y en que intervalo
    print(Num)

print("")

lista_num = [] # Engloba todo en una lista
for num in range(5,51,5):
    lista_num.append(num)
print(lista_num)

print(" ")

for num in enumerate(lista_num):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")
print()
print(type(enumerate(lista_num)))