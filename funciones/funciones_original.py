# Una función es un fragmento de codigo que se encarga de realizar una tarea
# y nos entrega un resultado

def saludar(nombre):
    print(f"Holas {nombre}")

#llamar función
nombre = input("ingrese su nombre: ")
saludar(nombre)

def sumar(a,b):
    resultado = a + b
    print(resultado)
a = int(input("ingrese su valor A: "))
b = int(input("ingrese su valor B: "))
sumar(a,b)

# Ejercicio
seg_op = True
a = int(input("ingrese su valor A: "))
b = int(input("ingrese su valor B: "))
op = input("ingrese la operación a realizar: ")

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
    print(f"{a}{op}{b} = {resultado}")

operar(a,b,op)
respuesta = input("desea realizar otra operación? Escriba SI o NO: ")
while True:
    if respuesta.upper() == "SI":
        a = int(input("ingrese su valor A: "))
        b = int(input("ingrese su valor B: "))
        op = input("ingrese la operación a realizar: ")
    else:
        break