import json

# Función para guardar los datos en un archivo JSON con clave dinámica
def guardar(datos, nombre):  # La variable 'nombre' define tanto el archivo como la clave en el JSON
    ruta_archivo = f'SISGESA/archivo/{nombre}.json'  # Ruta dinámica basada en el nombre

    # Cargar los grupos actuales que ya están en el archivo JSON
    try:
        with open(ruta_archivo, 'r') as fd:  # Abrir el archivo JSON
            contenido = json.load(fd)  # Cargar el contenido del archivo
            
            # Verificar si lo que se carga es un diccionario
            if not isinstance(contenido, dict):
                contenido = {}  # Si no es un diccionario, inicializamos uno vacío
    except FileNotFoundError:
        # Si no existe el archivo, se inicializa como un diccionario vacío
        contenido = {}

    # Registrar el nuevo grupo en el diccionario 'contenido'
    contenido[f'{nombre}'] = datos

    # Guardar los datos actualizados en el archivo JSON con la clave dinámica
    with open(ruta_archivo, 'w') as fd:  # Guardar en el archivo JSON correspondiente
        json.dump(contenido, fd, indent=4)

