#cargar archivos
import json


# Función para cargar archivos JSON
def cargar_archivo_json(nombre_archivo):
    ruta = f'SISGESA/archivo/{nombre_archivo}.json'
    try:
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo}.json no existe.")
        return {}

# Cargar cada archivo JSON en una variable independiente
cuenta = cargar_archivo_json('cuenta')
docentes = cargar_archivo_json('Docentes')
grupos = cargar_archivo_json('grupos')
modulo = cargar_archivo_json('Modulo')
estudiantes = cargar_archivo_json('Estudiantes')
