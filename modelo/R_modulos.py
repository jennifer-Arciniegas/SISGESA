from persistencia.pesistenciaGuardar import guardar
""" estructura
modulo = {
    codigo1(str):{
        nombre:(str)
        duracion: (int)
        
    },
    codigo2(str):{
       nombre:(str)
       duracion: (int)
    },

}
"""
def Duracion():
    while True: #validar que tenga un caracter
        try: 
            edad = int(input("Ingrese la duracion en semanas. \n"))
            if edad < 3:
                print(">>> error al ingresar la duracion en semanas")
                continue
            return edad
        except Exception as e: #valida cualquier error
            print(">>> error" + e)

def leernombre():
    while True:
        try:
            name = input("Ingrese el modulo: \n")
            if len(name.strip()) == 0:
                print("Error nombre invalido")
                continue
            return name
        except Exception as e:
            print("Error al ingresar el nombre del modulo. \n" + e)

def leerCodigo():
    while True:
        try:
            cod = input("Ingrese el codigo del modulo:  \n")
            if len(cod.strip()) == 0:
                print("Error. Codigo invalido")
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el codigo del modulo. \n" + e)
    


def R_modulos (registro, arch):
    print("\n\n ** Registrar Modulo**")
    cod = leerCodigo()
    if cod not in registro:
        nombre = leernombre()
        D_semanas = Duracion()

        datModulo={
            "Nombre": nombre,
            "Duracion": D_semanas

        }
        registro[cod]= datModulo
        registro = dict(sorted(registro.items()))
        guardar(registro)


    else:
         print("El modulo ya esta registrado")
        
    input("Precione cualquier tecla para volver al menu. \n")
    guardar(registro)

    