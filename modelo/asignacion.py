import json

# Asignación de Estudiantes a Grupos y Módulos: 
#Los estudiantes se asignarán a un único grupo y podrán estar matriculados en entre 1 y 3 módulos.
#  El sistema debe permitir asociar a los estudiantes con sus respectivos grupos y módulos. 
# formar deseada en el dict:
"""
    asignacion:{
    01:{ "id_Estudiante": "12034433",
      "id_grupo": "A1", 
      "id_modulo": {
      "HD2": {
            "codigo": "HD2",
            "nombre": "Historia deporte",
            "Duracion": 5
        },
        "M1": {
            "codigo": "M1",
            "nombre": "Musica",
            "Duracion": 5
      }
    
    }
    }


    """
# se llamaran los datos alojados en los json para realizar a modo tabla de relacion la asignacion de estudiantes a un unico curso y maximo 3 modulos 

with open("SISGESA/archivo/Estudiantes.json", "r") as f1, open("SISGESA/archivo/grupos.json", "r") as f2, open("SISGESA/archivo/Modulo.json", "r") as f3:
    estudiantes = json.load(f1)
    grupos = json.load(f2)
    modulos = json.load(f3)

Asignacion = {} #se crea un dicionario para subir las asignaciones de estudiantes al grupo y modulos

for student in estudiantes:


#selecionar uno o dos modulos 



