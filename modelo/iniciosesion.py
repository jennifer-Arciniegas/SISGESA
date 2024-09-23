

def login(): #funcion para cargar credenciales almacenadas
 cuenta = cargarLogin()
 userLogin = leeruser()
 passlogin = input("Ingrese su contraceña:  \n")
  #buscar el usuario en las cuentas ingresadas 
  for codigo, datos in cuenta.items():
    userjson = datos.get("User")
    passJson = datos.get("Password")

    if userLogin == userjson:
        #verificar la contraseña ingresada con la almacenada