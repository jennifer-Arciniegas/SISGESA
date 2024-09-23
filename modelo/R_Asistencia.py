def registroDocentes(estudiantes, modulos, datos):
    print("**Registrar Docente**")
    print("___________________")
    codEstudiante = leercodigoEstudiante()
    codModulo = leerCodigoModulo()
    # Validar si el código ya existe en la variable `datos`
    if codEstudiante in estudiantes and codModulo in modulos:  # `datos` es el diccionario que contiene los grupos previos
        fechaEntrada = leerFechaEntrada()
        fechaSalida = leerFechaSalida()
        

        # Crear el nuevo grupo como un diccionario
        modelDat = {
            "codigoEstudiante": codEstudiante,
            "codigoModulo": codModulo,
            "fechaEntrada": fechaEntrada,
            "fechaSalida": fechaSalida           
        }
        cod = len(datos) + 1 # el contador es la consulta 
        # Agregar el nuevo grupo a `datos`, utilizando el código como clave
        datos[cod] = modelDat  
        print(f"{cod} registrado correctamente.")
    else:
        print(f"El código {cod} ya existe en el sistema.")
    
    return datos