# Métodos de conversion de datos

texto = "25"
decimal = 45
booleana = False
Entero = 40.5

print(f"variable de tipo {type(texto)}")
print(f"variable de tipo {type(booleana)}")
print(f"variable de tipo {type(Entero)}")
print(f"variable de tipo {type(decimal)}")

texto_entero = int(texto) # convierte a INTEGER
booleano_texto = bool(booleana) # Convierte a Booleano
decimal_entero = str(decimal) # Convierte a String
float() # Convierte a float
print("")
print(f"variable de tipo {type(texto_entero)}")
print(f"variable de tipo {type(booleano_texto)}")
print(f"variable de tipo {type(Entero)}")
print(f"variable de tipo {type(decimal_entero)}")