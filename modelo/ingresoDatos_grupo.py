#se presentan las fuciones que permitiran almacenar el dicionario de grupos.
from persistencia.pesistenciaGuardar import guardar

def leerSgla():
    while True: #validar que se ha ingresado un valor 
        try:
            sigla = input("Codigo del grupo: \n")
            if len(sigla.strip()) == 0: 
                print("Error. Codigo invalido")
                continue
            return sigla
        except Exception as e: #valida cualquier error
            print("Error al ingresar el codigo" + e)


def leerNombre():
     while True: #validar que se ha ingresado un valor 
        try:
            name = input("Codigo del grupo: \n")
            if len(name.strip()) == 0: 
                print("Error. Codigo invalido")
                continue
            return name 
        except Exception as e: #valida cualquier error
            print("Error al ingresar el codigo" + e)

def leercodigo():
    while True: #validar que se ha ingresado un valor 
        try:
            cod = input("Codigo del grupo: \n")
            if len(cod.strip()) == 0: 
                print("Error. Codigo invalido")
                continue
            return cod 
        except Exception as e: #valida cualquier error
            print("Error al ingresar el codigo" + e)



def registroGrupos(grup, datagrup):
    print("**Registrar Grupo**")
    print("___________________")
    cod = leercodigo()
    if cod not in grup: # si el codigo no esta en la libreria entonces lo guardara, si esta enviara al else
        nombre = leerNombre()
        sigla = leerSgla()

        datgrup = {
            "nombre": nombre,
            "sigla": sigla
        }

        grup[cod] = datgrup   #cod es el codigo y en datagrup estan los valores de esa llave 
        grup = dict(sorted(grup.items())) #ordena los valores ingresados 

        guardar(grup)
    else:
        print("El codigo ya esta registrado, por lo tanto el grupo ya esta registrado")
        print("ingrese cualquier tecla para volver al menu. \n")

    return grup 

