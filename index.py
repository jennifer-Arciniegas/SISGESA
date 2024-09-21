from interfaz.menu import menu
from modelo.ingresoDatos import registroGrupos

print(menu())




grupos= {}
archivo =""

while True:
    opc = menu()
    match opc:
        case "a":
            grupos = registroGrupos(grupos, archivo)
        case "b":
            modulos = registroModulos(modulos, archivo)
        case "c":
            estudiante = registroEstudiante(estudiante, archivo)
        case "d":
            docente = registroDocente(docente, archivo)
        case "e":
            asistencia = registroAsistencia(asistencia, archivo)
        case "f":
            consultaIfo = consultaInfor(consultaIfo, archivo)
        case "g":
            Ginformes = genInformes(Ginformes, archivo)
        case "h":
            cambio_clave = cambioClave(cambio_clave, archivo)
        case "i":
            print("Gracias por usar el software")
            break 


