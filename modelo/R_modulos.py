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
def leerCodigo():
    while True:
        try:
            

    



def R_modulos (registro, arch):
    print("\n\n ** Registrar Estudiante **")
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

    