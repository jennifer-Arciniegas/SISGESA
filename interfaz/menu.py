

def menu():
    while True:
        print("** MENU**")
        print("a. Registro de grupos.")
        print("b. Registro de módulos.")
        print("c. Registro de estudiantes.")
        print("d. Registro de docentes.")
        print("e. Registro de asistencia.")
        print("f. Consultas de información.")
        print("g. Generación de informes.")
        print("h. Cambio de contraseña.")
        print("i. Salida del sistema.")

        print(">> Ingresar a opcion: ", end="")
        try:
            opciones = ["a", "b", "c","d","e","f", "g", "h", "i"]
            opc = input().lower()
            if opc not in opciones:
                print("Error opcion invalida")
                print("presione cualquier tecla para volver al menu")
            return opc
        
        except ValueError:
            print("ingreso una opcion incorrecta")
            print("presione cualquier tecla para volver al menu")
         

            