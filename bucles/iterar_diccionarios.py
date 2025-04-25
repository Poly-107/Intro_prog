diccionario = {
    "Nombre":"Leonardo",
    "Apellido":"Gonzalez",
    "Edad":24,
    "estudiante":True
}

for clave in diccionario:
    print(f"la clave es: {clave}")

for dato in diccionario.items():
    clave = dato[0]
    valor = dato[1]
    print(f"la clave es: {clave} y el valor es: {valor}")