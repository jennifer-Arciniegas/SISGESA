#cargar archivos
import json


# Función para cargar archivos JSON dado su nombre y devuelve el contenido 
#como un diccionario
def cargar_archivo_json(nombre_archivo):
    ruta = f'SISGESA/archivo/{nombre_archivo}.json'
    try:
        with open(ruta, 'r') as archivo:
            return json.load(archivo) #devuelve el contenido del diccionario
    except ValueError: #manejo de errores
        print(f"El archivo {nombre_archivo}.json no existe.")
        return {}# retorna el diccionario vacio en caso de error
    



