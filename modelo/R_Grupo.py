grup = []

def leerSgla():
    while True: 
        try:
            sigla = input("SIGLA del grupo: \n")
            if len(sigla.strip()) == 0: 
                print("Error. Codigo invalido")
                continue
            return sigla
        except Exception as e:
            print("Error al ingresar el codigo", e)

def leerNombre():
    while True: 
        try:
            name = input("Nombre del grupo: \n")
            if len(name.strip()) == 0: 
                print("Error. Codigo invalido")
                continue
            return name 
        except Exception as e:
            print("Error al ingresar el codigo", e)

def leercodigo():
    while True: 
        try:
            cod = input("Codigo del grupo: \n")
            if len(cod.strip()) == 0:
                print("Error, ingrese un codigo") 
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el codigo", e)

def registroGrupos():
    global grup  # Indicar que queremos modificar la variable global
    print("**Registrar Grupo**")
    print("___________________")
    cod = leercodigo()
    if not any(grupo['codigo'] == cod for grupo in grup):  # Verificar si el código ya existe
        nombre = leerNombre()
        sigla = leerSgla()

        datgrup = {
            "codigo": cod,
            "nombre": nombre,
            "sigla": sigla
        }
        grup.append(datgrup)
        grup.sort(key=lambda x: x['codigo'])  # Ordenar la lista por el código del grupo
    else:
        print("El código ya existe.")
    return grup
