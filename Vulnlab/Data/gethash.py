#!/usr/bin/env python3

import sqlite3
import base64
import hashlib

# Nos conectamos
conn = sqlite3.connect('grafana.db')
cursor = conn.cursor()

# Filtramos directamente por la data que nos interesa
cursor.execute("SELECT email, password, salt, is_admin FROM user")

# Obtenemos todas las filas
rows = cursor.fetchall()

# Recorremos las filas con un bucle for
for row in rows:
    email, password, salt, is_admin = row

    # Decodifimos la contraseña de hexadecimal
    decoded_hash = bytes.fromhex(password)

    # Codificamos la contraseña y la sal a base64
    hash64 = base64.b64encode(decoded_hash).decode('utf-8')
    salt64 = base64.b64encode(salt.encode('utf-8')).decode('utf-8')

    # Lo guardamos en un archivo hash_file.txt
    with open("hash_file.txt", "a") as hash_file:
        hash_file.write(f"sha256:10000:{salt64}:{hash64}\n")

# cerramos la conexion ala base de datos
conn.close()
