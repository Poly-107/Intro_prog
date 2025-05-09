import operacion_suma 

def bienvenida():
    print()
    print("Bienvenido a la Super Calculadora Python")
    print("=============================================")
    print()

def menu():
    print()
    print("Super Calculadora Python")
    print("Seleccione una operación: ")
    print("1: suma")
    print("2: resta")
    print("3: Multiplicación")
    print("4: División")
    print("0: Salir")
    print()

def ejecutar_calculadora():
    bienvenida()
    while True:
        print()
        num_1 = float(input("Ingrese el primer número: "))
        num_2 = float(input("Ingrese el segundo número: "))
        menu()
        opcion = input("Seleccione una opción (0-4): ")

        resultado = 0
        operacion = ""
        if opcion == "1":
            resultado = operacion_suma.op_suma(num_1, num_2)
            operación = "+"
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "0":
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            return
        print(f"{num_1} {operacion} {num_2} = {resultado}")

ejecutar_calculadora()