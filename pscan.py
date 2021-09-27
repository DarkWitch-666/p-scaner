import threading
import time
import colorama
import socket
import os
from colorama import init, Fore, Back, Style

# init()
init(autoreset=True)

os.system("clear")
time.sleep(1)
print()

os.system("figlet P - S C A N E R | lolcat") #banner

print()
os.system("date | lolcat")
print(Fore.RED + '-' * 35)

target = input(f'{Fore.LIGHTGREEN_EX}Host ->{Fore.LIGHTWHITE_EX} ')

print(Fore.RED + '-' * 35)
print()

def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        connection = s.connect((target, port))
        print(f"{Back.LIGHTGREEN_EX}{Fore.LIGHTWHITE_EX}Port->> {port} {Back.LIGHTBLUE_EX}open!\n") 
        connection.close()
    except:
        pass


ports = [21, 22, 23, 25, 38, 43, 47, 80, 109, 110, 115, 118, 119, 143,
194, 220, 443, 540, 585, 591, 1112, 1433, 1443, 3128, 3197,
3306, 4000, 4333, 4747, 5100, 5432, 6669, 8000, 8080, 9014, 9200]

for element in ports:
    t = threading.Thread(target=portscan, kwargs={'port': element})



    t.start()

time.sleep(1)
print(f"{Fore.YELLOW}<enter>-exit")
input()
