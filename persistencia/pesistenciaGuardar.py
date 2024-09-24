import json
#datos es un dict el cual contiene la informacion a guardar
#nombre se refiere al "nombre" del archivo json donde posteriormente se guardaran los datos.
def guardar(datos, nombre): 
    ruta_archivo = f'SISGESA/archivo/{nombre}.json' #ruta y el nombre del archivo

    # guardar el archivo JSON si existe
    try:
        with open(ruta_archivo, 'r') as fd:
            contenido = json.load(fd) #si exite carga
            if not isinstance(contenido, dict):
                contenido = {}
    except ValueError: #si no lo encuentra muestra este error
        contenido = {}

    # Actualizar el contenido con los nuevos datos
    if datos: 
        contenido.update(datos)  # actualizar datos nuevos con existentes

    # Guardar los datos actualizados en el archivo JSON
    with open(ruta_archivo, 'w') as fd:
        json.dump(contenido, fd, indent=4)
