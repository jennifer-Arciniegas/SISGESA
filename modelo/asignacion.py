import json

def buscarGrupo(grupo):
    codGrupo = input("Ingrese el código del grupo: ")
    if codGrupo in grupo:
        return codGrupo
    else:
        print("Grupo no existe")
        return None  # Retorna None si el grupo no existe

def asignarModulo(modulo):
    cont = int(input("¿Cuántos módulos desea ingresar? "))
    if cont > 3:
        print("maximo de modulos son 3")
    else:
        modulos_asignados = {}  # Diccionario para almacenar los módulos

        for i in range(1, cont + 1):
            codModulo = input(f"Ingrese el código del módulo {i}: ")
            if codModulo in modulo:
                modulos_asignados[f"m{i}"] = codModulo  # Asignar el código al diccionario
            else:
                print("Módulo no existe")

    return json.dumps(modulos_asignados)  # Retornar el diccionario como JSON

def buscarEstudiante(estudiantes):
    codEstudiante = input("Ingrese el código del estudiante: ")
    if codEstudiante in estudiantes:
        return codEstudiante
    else:
        print("Estudiante no existe")
        return None  # Retorna None si el estudiante no existe

def asignacion(estudiantes, modulos, grupos, datos):
    datosEstudiante = buscarEstudiante(estudiantes)
    if datosEstudiante is None:
        return  # Salir si el estudiante no existe

    if datosEstudiante not in datos:
        datosGrupo = buscarGrupo(grupos)
        if datosGrupo is None:
            return  # Salir si el grupo no existe
        datosAsignacion = {
            "codigo": datosEstudiante,
            "Grupo": datosGrupo,
            "modulo": json.loads(asignarModulo(modulos))  # Convertir el JSON en diccionario
        }
        datos[datosEstudiante] = datosAsignacion
        print(f"Asignación completada para el estudiante {datosEstudiante}.")
    else:
        print("Estudiante ya asignado.")

    return datos  # Devolver los datos actualizados
