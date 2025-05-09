def ope(a, b, op):
    resultado = 0
    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "/":
        if b != 0:
            resultado = a / b
        else:
            print("El divisor de un número no puede ser 0")
            return None
    elif op == "*":
        resultado = a * b
    else:
        print("Operación inválida")
        return None
    return resultado  # Devuelve el resultado como un número

# Código principal solo si se ejecuta este archivo directamente
if __name__ == "__main__":
    a = int(input("Ingrese su valor A: "))
    b = int(input("Ingrese su valor B: "))
    op = input("Ingrese la operación a realizar ")

    resultado = ope(a, b, op)
    if resultado is not None:
        print(f"El resultado es: {resultado}")

    respuesta = input("¿Desea realizar otra operación? Escribe SI/NO: ")
    while True:
        if respuesta.upper() == "SI":
            a = int(input("Ingrese su valor A: "))
            b = int(input("Ingrese su valor B: "))
            op = input("Ingrese la operación a realizar: ")
            resultado = ope(a, b, op)
            if resultado is not None:
                print(f"El resultado es: {resultado}")
            respuesta = input("¿Desea realizar otra operación? Escribe SI/NO: ")
        else:
            break