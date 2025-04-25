'''
Clase AB: $7,177,530.
Clase C1a: $3,010,391
Clase 1B: $2,072,853
Clase C2: $1,500,774
Clase C3: $1,003,426
Clase D: $640,667
Clase E: $361,583
'''
print("ingrese su sueldo:")
sueldo = input()
int(sueldo)
sueldo_int = int(sueldo)

# Al menos en python tendrás que crear una nueva variable que guardé el valor de la primera
# Variable una vez modificada debido a que siempre que sea "input" es considerado texto
# "sueldo = input()
# int(sueldo)
# sueldo_int = int(sueldo)"


if sueldo_int > 3010391:
    print("usted pernetece a la clase AB")
elif sueldo_int > 2072853:
    print("Usted pertenece a la clase C1a")
elif sueldo_int > 1500774:
    print("usted pertenecea a la clase 1B")
elif sueldo_int > 1003426:
    print("usted pertenece a la clase C2")
elif sueldo_int > 640667:
    print("usted pertenece a la clase C3")
elif sueldo_int > 361583:
    print("usted pertenece a la clase E")
else:
    print("usted es muy pobre :( ")
# "elif" es una mezcla entre "else" e "if", una condicon extra dentro de la elección"
# Es una pregunta dentro de la pregunta