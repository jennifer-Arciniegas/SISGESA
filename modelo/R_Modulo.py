def leerDuracion():
    while True: 
        try:
            duracion = int(input("duracion en semanas: \n"))
            return duracion
        except Exception as e:
            print("Error solo digite numeros")

def leerNombre():
    while True: 
        try:
            name = input("Nombre del modulo: \n")
            if len(name.strip()) == 0: 
                print("Error. Codigo invalido")
                continue
            return name 
        except Exception as e:
            print("Error al ingrese nombre", e)

def leercodigo():
    while True: 
        try:
            cod = input("Codigo del modulo: \n")
            if len(cod.strip()) == 0:
                print("Error, ingrese un codigo") 
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el codigo", e)

def registroModulo(datos):
    print("**Registrar Modulo**")
    print("___________________")
    cod = leercodigo()
    if cod not in datos:
        nombre = leerNombre()
        duracion = leerDuracion()

        modelDat = {
            "codigo": cod,
            "nombre": nombre,
            "Duracion": duracion
        }
        datos[cod] = modelDat
        print(f"{cod} registrado correctamente.")

    else:
        print(f"El código {cod} ya existe en el sistema.")
    return datos
