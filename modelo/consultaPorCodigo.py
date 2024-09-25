def buscarEstudiantePorGrupo(asignacion):
    codGrupo = input("Ingrese el código del grupo: \n").upper()  # Usar input para capturar el valor
    estudiantes_en_grupo = []
    for codigo, info in asignacion.items():
        if info["Grupo"] == codGrupo:
            estudiantes_en_grupo.append(codigo)  # Agrega el estudiante si está en el grupo
    if not estudiantes_en_grupo:  # Si la lista está vacía
        print("No hay estudiantes en este grupo")
    return estudiantes_en_grupo

def consultarEstudiantePorGrupo(asignacion, estudiantes):
    codEstudiante = buscarEstudiantePorGrupo(asignacion)
    for codigos in codEstudiante:
        if codigos in estudiantes:
            print(f"cod: {codigos}| Nombre: {estudiantes[codigos]['Nombre']}")
        else:
            print("No hay estudiantes")
def buscarEstudiantePorModulo(asignacion):
    codModulo = input("Ingrese el codigo del modulo: \n").upper()
    estudiante_en_modulo =[]
    for codigo, info in asignacion.items():
        # Verificar si el módulo está en la lista de módulos asignados al estudiante
        if codModulo in info.get("modulo", {}).values():
            estudiante_en_modulo.append(codigo)  # Agregar el código del estudiante
    
    if not estudiante_en_modulo:  # Si no se encuentra ningún estudiante
        print("No hay estudiantes asignados a este módulo")
    
    return estudiante_en_modulo
def consultarEstudiantePorModulo(asignacion, estudiantes):
    codEstudiantes = buscarEstudiantePorModulo(asignacion)
    for codigo in codEstudiantes:
        if codigo in estudiantes:
            print(f"Nombre del estudiante: {estudiantes[codigo]['Nombre']}")
        else:
            print(f"No se encontró información del estudiante con código {codigo}")

def consultasPorCodigo(asignacion, estudiantes):
    while True:
        
        op = int(input("Consultas:\n\t1. Estudiantes por Grupo:\n\t2. Estudiantes por Modulo\n\t3. Salir\n"))
        if op == 1:
            consultarEstudiantePorGrupo(asignacion, estudiantes)
        elif op == 2:
            consultarEstudiantePorModulo(asignacion, estudiantes)
        elif op == 3:
            break