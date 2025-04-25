# 1.- Escribir un programa que almacene la cadena de caracteres "CONTRASENA"
#     En una variable, luego le pida al usuario que ingrese la "CONTRASENA" y el sistema debe indicar
#     En pantalla si la contraseña ingresada es correcta

def val_con(contrasena_usuario):
    contrasena = "Todos_juntos"
    if contrasena == "Todos_juntos":
        print("contraseña correcta")
    else:
        print("Contrasena incorrecta xd")

contrasena_ingresada = input("Ingrese su contraseña: ")
val_con(contrasena_ingresada)
