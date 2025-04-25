#los datos compuesto son una colección de datos que pueden pertenecer a una variable

#listas, colección ORDENADA de elementos, mutables
lista = ["Leonardo", 24, True]
print(lista)
print(type(lista))
#Los corchetes "[]" definen las listas, tu agregas los datos ordenados
print(lista[0])
lista[0]="Leonardo G"
print(lista)
#puedes modificar las listas, siempre mediante su indice (0, 1, 2, etc...)

# Diccionarios, Coleccion ordenada de pares de elementos mutables
# Un diccionario se define con las llaves "{}"
diccionario = {
    "nombre": "Leonardo",
    "edad": 24,
    "Es chido, a veces": True 
}
print(diccionario)
print(type(diccionario))
print(diccionario["nombre"])
# En los diccionarios accedes a los ementos unicamente por los nombres, en lugar del indice
# siempre se accede a los ementos para modficarlos con corchetes "[]"
diccionario["nombre"]="Leonardo G"
print(diccionario)

# conjuntos, colección DESORDENADA de elementos
conjunto = {"Leonardo", 24, True}
print(conjunto)
print(type(conjunto))
# estos tambien se definen con "{}", no se pueden acceder a los elementos, no es indexable
# print(conjunto[0])=ERROR
# a los conjuntos si se les puede agregar mas alementos
conjunto.add(45)
print(conjunto)
conjunto.pop()
print(conjunto)

# Tuplas, colección inmutable de elementos
tupla = ("leonardo", 24, True)
print(tupla)
print(type(tupla))
# La tupla es una colección ordenada, lo que quiere decir que pomodes
# modificar sus valores a través del indice
print(tupla[0])
# tupla[0]="Leonardo G" = Error