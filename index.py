from interfaz.menu import menu
from modelo.R_Grupo import registroGrupos
from modelo.R_Estudiantes import Re_estudiantes
from persistencia.pesistenciaGuardar import guardar
from modelo.R_Modulo import registroModulo
from persistencia.cargar import *
from modelo.R_Docentes import registroDocentes
from modelo.iniciosesion import login
from modelo.iniciosesion import cambiarpassword
from modelo.R_Asistencia import registroAsistencia

if login() is not None:
    while True:
        opc = menu()
        match opc:
            case "a":
                guardar(registroGrupos(cargar_archivo_json("grupos")),"grupos") 
            case "b":
                guardar(registroModulo(cargar_archivo_json("Modulo")), "Modulo")
            case "c":
                guardar(Re_estudiantes(cargar_archivo_json("Estudiantes")),"Estudiantes")
            case "d":
                guardar(registroDocentes(cargar_archivo_json("Docentes")), "Docentes")
            case "e":
                guardar(registroAsistencia(cargar_archivo_json("Estudiantes"),cargar_archivo_json("Modulo"),cargar_archivo_json("asistencia")),"asistencia")
            case "f":
                consultaIfo = consultaInfor(consultaIfo, archivo)
            case "g":
                Ginformes = genInformes(Ginformes, archivo)
            case "h":
                guardar(cambiarpassword(cuenta), "cuenta")
            case "i":
                guardar(cambiarpassword(cuenta), "cuenta")
            case "j":
                print("Gracias por usar el software")
                break 
