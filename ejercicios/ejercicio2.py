# Escribir un programa que pida al usuario un numero entero e indique si indique si es par o impar.

def par_impar(num_ing):
    if num_ing % 2 == 0:
        print(f"Su numero {num_ing} es par")
    else:
        print(f"Su numero {num_ing} es impar")    

numero_ingresado = int(input("Ingrese un numero entero: "))
par_impar(numero_ingresado)