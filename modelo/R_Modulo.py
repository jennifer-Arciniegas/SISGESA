modulo = []

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

def registroModulo():
    global modulo  # Indicar que queremos modificar la variable global
    print("**Registrar Modulo**")
    print("___________________")
    cod = leercodigo()
    if not any(grupo['codigo'] == cod for grupo in modulo):  # Verificar si el código ya existe
        nombre = leerNombre()
        duracion = leerDuracion()

        datgrup = {
            "codigo": cod,
            "nombre": nombre,
            "Duracion": duracion
        }
        modulo.append(datgrup) #agrega al final de la lista el registro 
        modulo.sort(key=lambda x: x['codigo'])  # Ordenar la lista por el código del grupo
    else:
        print("El código ya existe.")
    return modulo
