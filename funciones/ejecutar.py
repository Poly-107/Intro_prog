# IMPORTANTE: siempre revisa que la función que quieras importar esté dentro de tu carpeta
# Si quieres trabajar con una función fuera de tu carpeta
# usa el comando "From [carpeta].[programa] import [función]"
# Si la función que quieres llamar está dentro de tu misma carpeta
# solo necesitas "From [pograma] import [función]"

from funciones_original import operar as ope

respuesta = "SI"
while True:
    if respuesta.upper() == "SI":
        a = int(input("ingrese su valor A: "))
        b = int(input("ingrese su valor B: "))
        op = input("ingrese la operación a realizar: ")

        resultado = ope(a,b,op)
        if resultado is not None:
            print(f"el resultado de {a} {op} {b} es" )

        respuesta = input("¿Desea realizar otra operación? SI/NO: ")
    else:
        break