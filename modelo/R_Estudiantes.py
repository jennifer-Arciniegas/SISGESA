def leerEdad():
    while True: #validar que tenga un caracter
        try: 
            edad = int(input("Ingrese la edad. \n"))
            if edad < 3:
                print(">>> error al ingresar la edad")
                continue
            return edad
        except Exception as e: #valida cualquier error
            print(">>> error" + e)

def leerSexo():
    while True:
        try:
            sexo = input("Ingrese el sexo: \n")
            if len(sexo.strip()) == 0:
                print("Error sexo invalido")
                continue
            return sexo
        except Exception as e:
            print("Error al ingresar el sexo. \n" + e)

def leerNombre():
    while True:
        try:
            name = input("Ingrese el nombre: \n")
            if len(name.strip()) == 0:
                print("Error nombre invalido")
                continue
            return name
        except Exception as e:
            print("Error al ingresar el nombre. \n" + e)


def leerCodigo():
    while True:
        try:
            cod = input("Ingrese el codigo:  \n")
            if len(cod.strip()) == 0:
                print("Error. Codigo invalido")
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el codigo. \n" + e)
    

def Re_estudiantes(datos):
    print("** Registrar Estudiante **")
    print("___________________________")
    cod = leerCodigo()
    if cod not in datos:
        nombre = leerNombre()
        sexo = leerSexo()
        edad = leerEdad()

        datEstudiante={
            "codigo": cod,
            "Nombre": nombre,
            "Sexo": sexo,
            "Edad": edad
        }

        datos[cod] =datEstudiante
        print(f"{cod} registrado correctamente.")
    else:
        print(f"El código {cod},
               ya existe en el sistema.")
    
    return datos



