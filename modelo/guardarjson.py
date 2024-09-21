import json

administrador = {"user": "administrador", "password": "SISGESA"}



with open("archivo/cuenta.json", "r") as fd:
    clave = json.dump(administrador, fd)

if not fd.closed:
    fd.close()