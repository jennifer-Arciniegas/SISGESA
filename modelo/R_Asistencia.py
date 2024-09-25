from datetime import datetime
import json

def leercodigoEstudiante():
    while True:
        try:
            cod = input("Ingrese el código:  \n")
            if len(cod.strip()) == 0:
                print("Error. Código inválido")
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el código. \n" + str(e))
    
def leerCodigoModulo():
    while True:
        try:
            cod = input("Ingrese el código:  \n")
            if len(cod.strip()) == 0:
                print("Error. Código inválido")
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el código. \n" + str(e))

def leerFechaEntrada():
    # Retorna la fecha actual como una cadena en formato DD/MM/YYYY
    return datetime.now().strftime("%d/%m/%Y %H:%M")


def registroAsistencia(estudiantes, modulos, datos):
    print("**Registrar**")
    print("___________________")
    codEstudiante = leercodigoEstudiante()
    codModulo = leerCodigoModulo()
  
    if codEstudiante in estudiantes and codModulo in modulos:  
        fechaEntrada = leerFechaEntrada()  # Fecha actual como cadena
   
        # Crear el nuevo registro como un diccionario
        modelDat = {
            "codigoEstudiante": codEstudiante,
            "codigoModulo": codModulo,
            "fechaEntrada": fechaEntrada,
                   
        }
        cod = len(datos) + 1  # el contador es la consulta 
        # Agregar el nuevo registro a `datos`, utilizando el código como clave
        datos[cod] = modelDat  
        print(f"{cod} registrado correctamente.")
    else:
        print(f"El código {codEstudiante} o {codModulo} no existe en el sistema.")
    
    return datos