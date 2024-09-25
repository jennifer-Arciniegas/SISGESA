import json
import hashlib

def consultaruser():
    with open ("SISGESA/archivo/cuenta.json", "r") as archivo:
        dato = json.load(archivo)
        return dato.get("administrados")
    
def consultarclave():
    with open ("SISGESA/archivo/cuenta.json", "r") as archivo:
        dato = json.load(archivo)
        return dato.get('password')
      
def leerPassword():
    while True:
        password = input("Ingrese la contraseña: \n")
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        try: 
            if len(password.strip()) == 0:
                print("error en ingreso.")
            return password
        except Exception as e:
            print("Error al ingresar la contraseña" + e)
                      
def leerUser():
    try:
      user = input("Ingrese su usuario: \n")
      if len(user.strip()) == 0:
            print("Error en el ingreso.")
          
      return user
    except Exception as e:
         print("Error al ingresar usuario" + e) 


def login(): #funcion para cargar credenciales almacenadas
  user = leerUser()
  administrador = consultaruser()

  if user == administrador.get('user'):
        userpassword = leerPassword()
        if userpassword == administrador.get('password'):
            print("contraseña correcta")
            return administrador
        else: 
            print("la contraceña es incorrecta")
            return None
  else:
    print("el usuario es incorrecto")
    return None


def cambiarpassword():
    user = leerUser()
    with open ("SISGESA/archivo/cuenta.json", "r") as archivo:
        dato = json.load(archivo)
    newPass = input("ingrese la nueva contraseña:\n")
    dato["administrados"]["password"] = hashlib.sha256(newPass.encode('utf-8')).hexdigest()
    with open("SISGESA/archivo/cuenta.json", 'w') as archivo:
        json.dump(dato, archivo, indent=4)
    print("contraseña actualizada")









