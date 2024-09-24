import json

def guardar(datos, nombre):
    ruta_archivo = f'SISGESA/archivo/{nombre}.json'

    # Cargar el archivo JSON actual si existe
    try:
        with open(ruta_archivo, 'r') as fd:
            contenido = json.load(fd)
            if not isinstance(contenido, dict):
                contenido = {}
    except FileNotFoundError:
        contenido = {}

    # Actualizar el contenido con los nuevos datos
    if datos:  # Solo actualiza si 'datos' no está vacío
        contenido.update(datos)  # Usar 'update' para fusionar los datos nuevos con los existentes

    # Guardar los datos actualizados en el archivo JSON
    with open(ruta_archivo, 'w') as fd:
        json.dump(contenido, fd, indent=4)
