# While (mientras) permite repetir un ciclo de acciones
# mientras una condición logica sea verdadera

contador_str = input("ingrese un numero entero menor a 50: ")
contador_int = (int(contador_str))

while contador_int <50 :
    contador_int = contador_int + 1 
    print(f"su contador es: {contador_int}")

print(f"ciclo terminado, ud ingresó el numero: {contador_str}")