def leerNombre():
    while True: 
        try:
            name = input("Nombre del docente: \n")
            if len(name.strip()) == 0: 
                print("Error. Nombre inválido")
                continue
            return name 
        except Exception as e:
            print("Error al ingresar el nombre", e)

def leercodigo():
    while True: 
        try:
            cod = input("Cedula del docente: \n")
            if len(cod.strip()) == 0:
                print("Error, ingrese un código válido") 
                continue
            return cod
        except Exception as e:
            print("Error al ingresar la cedula", e)

def registroDocentes(datos):
    print("**Registrar Docente**")
    print("___________________")
    cod = leercodigo()
  
    if cod not in datos: 
        nombre = leerNombre()
        

        # Crear el nuevo grupo como un diccionario
        modelDat = {
            "codigo": cod,
            "nombre": nombre
            
        }
        # Agregar el nuevo grupo a datos, utilizando el código como clave
        datos[cod] = modelDat  
        print(f"{cod} registrado correctamente.")
    else:
        print(f"El código {cod} ya existe en el sistema.")
    
    return datos
