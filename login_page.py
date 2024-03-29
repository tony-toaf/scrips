import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Desactivar las advertencias de verificación de certificados SSL
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

opciones = int(input("Seleccione una opción: \n1. Inicio de sesión \n2. Cerrar sesión \nNúmero de elección: "))
print(opciones)

if opciones == 1:  # para iniciar la sesión
    login_url = 'https://conex.rnp.hn/LoginUsuario.aspx'
    username = input("Usuario: ")
    password = input("Contraseña: ")

    payload = {
        'username': username,
        'password': password
    }

    response = requests.post(login_url, data=payload, verify=False)

    if response.status_code == 200:
        print("Inicio de sesión exitoso")
    else:
        print("Error en el inicio de sesión")

elif opciones == 2:  # para cerrar la sesión
    # Desactivar las advertencias de verificación de certificados SSL
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    logout_url = 'https://conex.rnp.hn/CerrarSesio'

    response = requests.get(logout_url, verify=False)

    if response.status_code == 200:
        print("Sesión cerrada exitosamente")
    else:
        print("Error al cerrar la sesión")

else:
    print("Ninguna opción seleccionada")

0801198714619
e08011987146198
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