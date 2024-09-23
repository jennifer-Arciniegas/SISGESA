from interfaz.menu import menu
from modelo.R_Grupo import registroGrupos
from modelo.R_Estudiantes import Re_estudiantes
from persistencia.pesistenciaGuardar import guardar
from modelo.R_Modulo import registroModulo




modulos = {}
estudiante={}
grupos= {}
archivo ="SISGESA\archivo\cuenta.json"

while True:
    opc = menu()
    match opc:
        case "a":
            guardar(registroGrupos(),"grupos") 
        case "b":
            guardar(registroModulo(), "Modulo")
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


