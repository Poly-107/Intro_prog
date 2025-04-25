# Se pueden usar herramientas con las variables, "F" para formatear como texto
# "del" que permite borrar variables

nom_com = input("ingrese su nombre completo: ")
saludar =  f"Buen día don(a) {nom_com}, ¿como estás?"
# del saludar
print(saludar)

texto = """
hola
soy un mensaje
de varias lineas xdd
xdd
"""

busqueda_in = input("ingrese lo que quiere buscar: ")
bus_tex = busqueda_in in texto

print(bus_tex)
# ".find" te permite buscar en que caracter exactamente está el texto que buscas
# si .find no encuentra el texto para comparar tirará un valor negativo
print(" ")
busqueda_find = input("ingrese otro texto: ")
busqueda_2 = texto.find(busqueda_find)
print(busqueda_2)
# ".index" tambien sirve para buscar exactamente donde está el texto que buscas
# si .index no encuentra el texto, el codigo simplemente fallará
print(" ")
busqueda_index = input("ingrese otro texto: ")
busqueda_3 = texto.index(busqueda_index)
print(busqueda_3)
# ".rfind" te entrega la ultima posición del texto que quieres comparar
print(" ")
busqueda_find = input("ingrese otro texto: ")
busqueda_2 = texto.find(busqueda_find)
print(busqueda_2)
nueva_busqueda_2 = texto.rfind(busqueda_find)
print(nueva_busqueda_2)
# ".count" te entrega la cantidad de veces que hay una coincidencia
num_ocurrencias = texto.count(busqueda_find)
if num_ocurrencias < 2:
    print(f"{busqueda_find} se repite: {num_ocurrencias} vez")
else:
    print(f"{busqueda_find} se repite: {num_ocurrencias} veces")