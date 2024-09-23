def leerSgla():
    while True: 
        try:
            sigla = input("SIGLA del grupo: \n")
            if len(sigla.strip()) == 0: 
                print("Error. Sigla inválida")
                continue
            return sigla
        except Exception as e:
            print("Error al ingresar la sigla", e)

def leerNombre():
    while True: 
        try:
            name = input("Nombre del grupo: \n")
            if len(name.strip()) == 0: 
                print("Error. Nombre inválido")
                continue
            return name 
        except Exception as e:
            print("Error al ingresar el nombre", e)

def leercodigo():
    while True: 
        try:
            cod = input("Código del grupo: \n")
            if len(cod.strip()) == 0:
                print("Error, ingrese un código válido") 
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el código", e)

def registroGrupos(datos):
    print("**Registrar Grupo**")
    print("___________________")
    cod = leercodigo()
    # Validar si el código ya existe en la variable `datos`
    if cod not in datos:  # `datos` es el diccionario que contiene los grupos previos
        nombre = leerNombre()
        sigla = leerSgla()

        # Crear el nuevo grupo como un diccionario
        modelDat = {
            "codigo": cod,
            "nombre": nombre,
            "sigla": sigla
        }
        # Agregar el nuevo grupo a `datos`, utilizando el código como clave
        datos[cod] = modelDat  
        print(f"{cod} registrado correctamente.")
    else:
        print(f"El código {cod} ya existe en el sistema.")
    
    return datos
