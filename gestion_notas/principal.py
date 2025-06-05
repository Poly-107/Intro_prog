import os
from datos.asignaturas import asignaturas

def obetener_listado_asignaturas():
    print()
    print("listado de asignaturas")
    print("======================")
    contador = 0
    for asignatura in sorted(asignaturas):
        contador += 1
        print(f"[{contador}] {asignatura}")

def obtener_asignatura_individual():
    asignatura_encontrada = "Asignatura no encontrada :c "
    busqueda = input("Ingrese que asignatura desea buscar: ")
    for asignatura in asignaturas:
        if busqueda.lower() in asignaturas.lower():
            asignatura_encontrada = asignaturas
    return asignatura_encontrada

def guardar_nueva_asignatura():
    obetener_listado_asignaturas()
    nueva_asignatura = input("Ingrese nueva asignatura: ")
    asignaturas.append(nueva_asignatura.title())

    archivo_datos = "asignaturas.py"
    ubicacion_archivo = os.path.join("gestion_notas/datos", archivo_datos)
    ubicacion_archivo = os.path.abspath(ubicacion_archivo)
    ubicacion_archivo = os.path.realpath(ubicacion_archivo)
    archivo = open(f"{ubicacion_archivo}", "w+")
    archivo.write(f"asignaturas = {asignaturas}")
    archivo.close()
    obetener_listado_asignaturas()

guardar_nueva_asignatura()