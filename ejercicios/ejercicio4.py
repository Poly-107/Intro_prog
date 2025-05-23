# from prettytable import PrettyTable

# tabla = PrettyTable()

# tabla.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# tabla.add_rows([
#     ["Adelaide", 1295, 1158259, 600.5],
#     ["Brisbane", 5905, 1857594, 1146.4],
#     ["Darwin", 112, 120900, 1714.7],
#     ["Hobart", 1357, 205556, 619.5],
#     ["Sydney", 2058, 4336374, 1214.8],
#     ["Melbourne", 1566, 3806092, 646.9],
#     ["Perth", 5386, 1554769, 869.4]
# ])

# print(tabla)


# animales = [
#     ["mamíferos",["vaca lechera","Hamster dorado","pony salvaje","chancho con chaleco"]],
#     ["reptiles",["kobra kai","balano","dragón de komodo","mamba negra"]],
#     ["Oviparos",["pato","pingüino","Canario","Gallina"]]
# ]

# print()

# for i in range(len(animales)):
#     for x in range(len(animales[i][1])):
#         print(animales[i][1])

lista_comidas = ["lasaña","pollo asado","curanto","sopaipilla"]
print("""           **==EJERCICIOS==**
      
1.- imprimir la cantidad de elementos de la lista
2.- imprimir la lista completa de comidas
3.- imprimir todas las comidas una a una
4.- preguntar  al usuario que comida busca, numero = indice
      
      """)

print("1.- La lista tiene", len(lista_comidas),"elementos")
print()

print("2.- la lista de comida completa es", lista_comidas)
print()

print("3.- las comidas son:")
for i in range(len(lista_comidas)):
    print(lista_comidas[i])
print()

print("4.- ¿Que comida desea comer?")
comida = input("Ingrese el nombre de la comida: ")
if comida in lista_comidas:
    print("la comida", comida, "se encuentra en la lista")
else:
    print("la comida", comida, "no se encuentra en nuestra lista :( ")
print()