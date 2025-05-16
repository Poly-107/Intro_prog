# IMPORTANTE: siempre revisa que la función que quieras importar esté dentro de tu carpeta
# Si quieres trabajar con una función fuera de tu carpeta
# usa el comando "From [carpeta].[programa] import [función]"
# Si la función que quieres llamar está dentro de tu misma carpeta
# solo necesitas "From [pograma] import [función]"

# Asegúrate de que el archivo "operacion_suma.py" esté en la misma carpeta que este script y que contenga las funciones necesarias.
from modulos.operacion_suma import op_division, op_multiplicacion, op_resta, op_suma as ope

def menu():
    print("Seleccione su opción: ")
    print("[1] Realizar cálculo aritmético")
    print("[2] Salir")

def programa_principal():
    print()
    print("【S u p e r】 【c a l c u l a d o r a】 【p y t h o n】")
    print("**===**===**===**===**===**===**===**===**===**===**")
    print()
    while True:
        menu()
        respuesta = input("Seleccione su opción: ")
        if respuesta == "2":
            print("¡Hasta luego!")
            break
        elif respuesta == "1":
            a = float(input("Ingrese su valor A: "))
            b = float(input("Ingrese su valor B: "))
            op = input("Ingrese la operación a realizar (+, -, *, /): ")

            if op == "+":
                resultado = ope(a, b)
            elif op == "-":
                resultado = op_resta(a, b)
            elif op == "*":
                resultado = op_multiplicacion(a, b)
            elif op == "/":
                if b == 0:
                    print("Error: División por cero no permitida.")
                    continue
                resultado = op_division(a, b)
            else:
                print("Operación no válida.")
                continue

            print(f"El resultado de {a} {op} {b} es: {resultado}")
        else:
            print("Opción no válida. Intente de nuevo.")

# Llama a la función principal
programa_principal()