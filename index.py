from interfaz.menu import menu
from modelo.ingresoDatos_grupo import registroGrupos
from modelo.R_Estudiantes import Re_estudiantes




estudiante={}
grupos= {}
archivo ="SISGESA\archivo\cuenta.json"

while True:
    opc = menu()
    match opc:
        case "a":
            grupos = registroGrupos(grupos, archivo)
        case "b":
            modulos = registroModulos(modulos, archivo)
        case "c":
            estudiante = Re_estudiantes(estudiante, archivo)
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


