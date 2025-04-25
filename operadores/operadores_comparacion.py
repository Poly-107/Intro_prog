numero_1 = 5
numero_2 = 4

# Operador equivalente 

equivalente = numero_1 == 5
print(equivalente)

pass_saved ="colmilloxd"
ingreso_pass = input("Ingrese su contraseña:")
acceso = ingreso_pass == pass_saved
if acceso == True:
    print("Acceso concedido")
else:
    print("acceso denegado")

# Operador distinto de
print(" ")
op_distinto = numero_1 != numero_2
print(f"Operador distinto de: {op_distinto}")

# Operador MAYOR QUE

op_mayor = numero_1 > numero_2
print(f"Operador mayor que: {op_mayor}")

# Operador MAYOR o IGUAL QUE

op_mayor_igual_que = numero_1 >= numero_2
print(f"Operador Mayor o igual que {op_mayor_igual_que}")

# Operador MENOR

op_menor_que = numero_1 < numero_2
print(f"Operador menor que: {op_menor_que}")

# Operador MENOR o IGUAL QUE

op_menor_igual_que = numero_1 <= numero_2
print(f"Operador menor o igual que: {op_menor_igual_que}")