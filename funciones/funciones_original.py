# Una función es un fragmento de codigo que se encarga de realizar una tarea
# y nos entrega un resultado
# if __name__ == "__main__":
#     def saludar(nombre):
#         print(f"Holas {nombre}")

#     #llamar función
#     nombre = input("ingrese su nombre: ")
#     saludar(nombre)

# def sumar(a,b):
#     resultado = a + b
#     print(resultado)
#     a = int(input("ingrese su valor A: "))
#     b = int(input("ingrese su valor B: "))
#     sumar(a,b)

# Ejercicio
seg_op = True
a = int(input("ingrese su valor A: "))
b = int(input("ingrese su valor B: "))
op = input("ingrese la operación a realizar: ")
while True:
    def operar (a,b,op):
        resultado = 0
        if op == "+":
            resultado = a + b
        elif op == "-":
            resultado = a - b
        elif op == "/":
            if b != 0:
                resultado = a / b
            else:
                print("el divisor de un numero no puede ser 0")
                return
        elif op == "*":
            resultado = a * b
        else:
            print("operacion invalida")
            return None
        return resultado
    operar(a,b,op)
    respuesta = input("desea realizar otra operación? Escriba SI o NO: ")
    while True:
        if respuesta.upper() == "SI":
            a = int(input("ingrese su valor A: "))
            b = int(input("ingrese su valor B: "))
            op = input("ingrese la operación a realizar: ")
            resultado = operar(a,b,op)
            if resultado is not None:
                print(f"el resultado de {a} {op} {b} es: {resultado}")
            respuesta = input("¿Desea realizar otra operación? Escriba SI o NO: ")  
        else:
            break