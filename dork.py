from googlesearch import search
import os
import time
import webbrowser
def banner():
    print("""
    ########   #######  ########  ##    ## 
    ##     ## ##     ## ##     ## ##   ##  
    ##     ## ##     ## ##     ## ##  ##   
    ##     ## ##     ## ########  #####    
    ##     ## ##     ## ##   ##   ##  ##   
    ##     ## ##     ## ##    ##  ##   ##  
    ########   #######  ##     ## ##    ## 

    """)
    time.sleep(3)

    dork()
def dork():
    query = input("Enter your query: ")
    res = int(input("Enter how many search result you need default = 10: "))
    for scan in search(query, num_results=res):
        print("please wait i am analysing data.....")
        webbrowser.open(scan)
        print("These are my results!")
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