import json
from modelo.R_Grupo import registroGrupos

#codigo 
#cargar cursos 
def guardarCursos():
    cursos = ['Cursos'].append(registroGrupos) #agregar el nuevo estudiante a la lista
    with open ('SISGESA\\archivo\\Cursos.json', 'w') as fd:
        json.dump(cursos, fd)

        if fd.closed:
            fd.close()




""""
def guardar(grup, arch):
    with open("SISGESA\archivo\cuenta.json", "w") as fd:
        json.dump(grup,fd)
    
    if fd.closed:
        fd.close()

def cargar(arch):
    archivo = Path(arch)
    grup = {}
    if archivo.is_file(): #True si existe y es un archivo
        try:
            with open("arch", "r") as fd:
                grup = json.load(fd)
            if not fd.closed():
                fd.close()
        except Exception as e:
           print("El archivo no extiste" + e)  
    else:
        print("Error. el archivo no existe")
        print("Presione cualquier tecla para volver al menu. \n")"""
                
