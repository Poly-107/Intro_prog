cervezas = {"Royal Guard", "Stella Artois", "Coors", "Heineken", "Dolbek"}
numeros = {10,20,30,40,50}

for chela in cervezas:
    print(f"Lo más hermoso de la comida: {chela}")

print(" ")

for Num in numeros:
    resulado = Num * Num
    print(f"{Num}*{Num}= {resulado}")

print(" ")
print(type(numeros))
for Num in enumerate(numeros):
    indice = Num[0]
    valor = Num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")