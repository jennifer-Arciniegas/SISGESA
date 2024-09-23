from interfaz.menu import menu
from modelo.R_Grupo import registroGrupos
from modelo.R_Estudiantes import Re_estudiantes
from persistencia.pesistenciaGuardar import guardar
from modelo.R_Modulo import registroModulo
from persistencia.cargar import *



while True:
    opc = menu()
    match opc:
        case "a":
            guardar(registroGrupos(grupos),"grupos") 
        case "b":
            guardar(registroModulo(modulo), "Modulo")
        case "c":
            guardar(Re_estudiantes(estudiantes),"Estudiantes")
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
