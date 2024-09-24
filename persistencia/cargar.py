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


