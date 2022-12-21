import time 
import os

def banner():
    print("""
    ##  ##  ##   ##  ##   ##   # ##### #######  ######   
    ##  ##  ##   ##  ###  ##  ## ## ##  ##   #   ##  ##  
    ##  ##  ##   ##  #### ##     ##     ##       ##  ##  
    ######  ##   ##  #######     ##     ####     #####   
    ##  ##  ##   ##  ## ####     ##     ##       ## ##   
    ##  ##  ##   ##  ##  ###     ##     ##   #   ## ##   
    ##  ##   #####   ##   ##    ####   #######  #### ##  

    Hello investigator this is hunter madde by Natnael Sendeku 
    this tool is made for investigation and OSINT purpose
    ===========================================================1===
    ||  if you need any help you can find me on twitter and github ||
    ||       https://twitter.com/NatnaelSendeku                    ||
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    Happy investigation!!                               
    """)
    time.sleep(3)
    print("""
    please choose tool you want to use
        1 IP location
        2 IMAGE Data
        3 Who is that
    """)
    picker()

def picker():
    menu = int(input("hunter@cybersecurity $ "))    
    if(menu == 1):
        os.system('python3 ip2location.py')
    elif(menu == 2):
        os.system('python3 exify.py')
    elif(menu == 3):
        os.system('python3 dork.py')
    else:
       os.system('clear')
       banner()

banner()
