import geocoder
import time
import os
import webbrowser
# ip = geocoder.ip("161.185.160.93")
def banner():

    #os.system("clear")
    print("""

    ::::::::::: :::::::::      :::     :::::::::  :::::::::  :::::::::  
        :+:     :+:    :+:   :+: :+:   :+:    :+: :+:    :+: :+:    :+: 
        +:+     +:+    +:+  +:+   +:+  +:+    +:+ +:+    +:+ +:+    +:+ 
        +#+     +#++:++#+  +#++:++#++: +#+    +:+ +#+    +:+ +#++:++#:  
        +#+     +#+        +#+     +#+ +#+    +#+ +#+    +#+ +#+    +#+ 
        #+#     #+#        #+#     #+# #+#    #+# #+#    #+# #+#    #+# 
    ########### ###        ###     ### #########  #########  ###    ### 

    
    """)

    time.sleep(3)
    
    Recon()

def Recon():
    target =  input("type your target IP here: ")

    ip = geocoder.ip(target)
    print(ip.city)
    print(ip.latlng)

    menu()

def menu ():
    goback = input("Do You want to Go back to main menu y/n: ")
    if (goback == "y"):
        print("Thanks for Using this tool!!!")
        time.sleep(1)
        os.system('python hunter.py')
    elif(goback == "n"):
        print("Here we go again!")
        time.sleep(1)
        banner()


banner()