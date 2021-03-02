import requests
import ctypes
import os
import time

#color shit
from colorama import init, Fore, Back, Style
init(convert=True)

count = 0

discord = requests.get("https://pastebin.com/raw/gP6pHmFD")

aeiorj = open("working.txt", "w")
aeiorj.close()

ctypes.windll.kernel32.SetConsoleTitleW("Subdomain Scanner | by HTTPTOOLZ")

print("[1] 100 [Might not find all subdomains] [Fast]\n[2] 1000 [Might not find all subdomains] [Slower]\n[3] 10000 [Will find all subdomains] [Slow]")
option = input("> ")

if option not in("1", "2", "3"):
	print(Fore.RED + "Invalid Option")
	time.sleep(10000)

os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.GREEN + f"""
██╗  ██╗████████╗████████╗██████╗ ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██║  ██║╚══██╔══╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     ╚══███╔╝
███████║   ██║      ██║   ██████╔╝   ██║   ██║   ██║██║   ██║██║       ███╔╝  {discord.text}
██╔══██║   ██║      ██║   ██╔═══╝    ██║   ██║   ██║██║   ██║██║      ███╔╝  
██║  ██║   ██║      ██║   ██║        ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
Input domain:
                                                                             
    """)

domain = input("> ")

if option == "1":
	extentions = requests.get("https://raw.githubusercontent.com/rbsec/dnscan/master/subdomains-100.txt")
	count2 = "100"


if option == "2":
	extentions = requests.get("https://raw.githubusercontent.com/rbsec/dnscan/master/subdomains-1000.txt")
	count2 = "1000"

if option == "3":
	extentions = requests.get("https://raw.githubusercontent.com/rbsec/dnscan/master/subdomains-10000.txt")
	count2 = "10000"

file = open("extentions.txt", "w")


file.write(str(extentions.text))
file.close()

file1 = open('extentions.txt', 'r')
Lines = file1.readlines()

for line in Lines:
	url = f"https://{line.strip()}.{domain}"
	try:
		nigger = requests.get(url)
	except requests.ConnectionError:
		print(Fore.RED + url)
		count += 1
		ctypes.windll.kernel32.SetConsoleTitleW(f"Subdomain Scanner | by HTTPTOOLZ | {count}/{count2}")
		pass
	except requests.exceptions.InvalidURL:
		print(Fore.RED + url)
		count += 1
		ctypes.windll.kernel32.SetConsoleTitleW(f"Subdomain Scanner | by HTTPTOOLZ | {count}/{count2}")
		pass
	else:
		print(Fore.GREEN + url)
		count += 1
		ctypes.windll.kernel32.SetConsoleTitleW(f"Subdomain Scanner | by HTTPTOOLZ | {count}/{count2}")
		xd = open("working.txt", "a")
		xd.write(url + "\n")

os.system('cls' if os.name == 'nt' else 'clear')
count = len(open("working.txt").readlines(  ))
print(Fore.GREEN + f"Finished : Found {count} Subdomains")
ctypes.windll.kernel32.SetConsoleTitleW(f"Subdomain Scanner | by HTTPTOOLZ | {count} subdomains found.")
os.system("pause")
