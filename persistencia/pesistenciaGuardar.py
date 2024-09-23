import json

# Función para guardar los datos en un archivo JSON con clave dinámica
def guardar(datosGrupos, nombre):  # La variable 'nombre' define tanto el archivo como la clave en el JSON
    ruta_archivo = f'SISGESA/archivo/{nombre}.json'  # Ruta dinámica basada en el nombre

    # Cargar los grupos actuales que ya están en el archivo JSON
    try:
        with open(ruta_archivo, 'r') as fd:  # Abrir el archivo JSON
            contenido = json.load(fd)  # Cargar el contenido del archivo
            
            # Verificar si lo que se carga es un diccionario
            if isinstance(contenido, dict):
                # Si el diccionario no tiene la clave con el nombre, la inicializamos
                if nombre not in contenido:
                    contenido[nombre] = []  # Inicializar si no existe
                lista_datos = contenido[nombre]
            else:
                # Si lo que cargamos no es un diccionario, lo tratamos como lista
                lista_datos = contenido

    except FileNotFoundError:
        # Si no existe el archivo, se inicializa como una lista vacía o un diccionario con una clave dinámica
        lista_datos = []
        contenido = {nombre: lista_datos}

    # Registrar el nuevo grupo
    nuevo_grupo = datosGrupos

    # Agregar el nuevo grupo a la lista
    lista_datos.append(nuevo_grupo)

    # Guardar los datos actualizados en el archivo JSON con la clave dinámica
    with open(ruta_archivo, 'w') as fd:  # Guardar en el archivo JSON correspondiente
        json.dump(contenido, fd, indent=4)
