import requests
import time
from colorama import Fore, Back, Style, init
import subprocess
from lolpython import lol_py
import ping3
import socket

ascii = f"""



 ██▓ ██▓███     ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓██▒▓██░  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▒██▒▓██░ ██▓▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
░██░▒██▄█▓▒ ▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
░██░▒██▒ ░  ░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
░▓  ▒▓▒░ ░  ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░1.
 ▒ ░░▒ ░            ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
 ▒ ░░░            ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
 ░                           ░ ░      ░ ░      ░  ░      ░  
                                                            
"""
lol_py(ascii)
                                                            


dev = """\
> Software Developer <
|    ch3rry root     |
"""
lol_py(dev)


options = """\
> Options <    
1- IP Lookup
2- IP Pinger
3- TCP Ping    
"""

lol_py(options)
option = input(f"{Fore.MAGENTA}Plz chosee an option: ")
print(Fore.RESET)

if option == '1':
    ip = input(f"{Fore.MAGENTA}IP: ")

    response = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query')

    data = response.json()

    continentt = data['continent']
    countryy = data['country']
    zipcode = data['zip']
    latt = data['lat']
    lonn = data['lon']
    ispp = data['isp']
    orgg = data['org']
    proxyy = data['proxy']
    hostingg = data['hosting']

    ip_info = (
    f"Continent: {continentt}\n"
    f"Country: {countryy}\n"
    f"Zip Code: {zipcode}\n"
    f"Lat: {latt}\n"
    f"Lon: {lonn}\n"
    f"Isp: {ispp}\n"
    f"Org: {orgg}\n"
    f"Proxy: {proxyy}\n"
    f"Hosting: {hostingg}"
    )
    lol_py(ip_info)
    

elif option == '2':
    ip2 = input(f"{Fore.MAGENTA}Enter skid IP: ")

    num_pings = input("Enter the number of pings: ")
    print(Fore.RESET)

    try:
        num_pings = int(num_pings)
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a valid number.")
        exit(1)
    print(Fore.RESET)

    for _ in range(num_pings):
        response_time = ping3.ping(ip2)

        if response_time is not None:
            formatted_time = round(response_time, 2)
            print(f"{Fore.GREEN}Reply from: {ip2} time: {formatted_time} ms.")
        else:
            print(f"{Fore.RED}Connection timed out {ip2} Downed...")




elif option == '3':

    ip3 = input(f"{Fore.MAGENTA}Enter IP: ")
    port = int(input("Enter port: "))
    
    try:
        num_pings = int(input("Enter the number of pings: "))
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a valid number.")
        exit(1)
    print(Fore.RESET)

    try:
        num_pings = int(num_pings)
        error_shown = False
        for _ in range(num_pings):
            try:
                start_time = time.time()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((ip3, port))
                end_time = time.time()

                if result == 0:
                    elapsed_time = end_time - start_time
                    formatted_time = round(elapsed_time * 1000, 2)
                    print(f"{Fore.GREEN}Connected to {ip3}: time={formatted_time}ms protocol=TCP port={port}")
                else:
                    print(f"{Fore.RED}Connection timed out {ip3}:{port}")

                sock.close()
            except socket.error:
                if not error_shown:
                    print(f"{Fore.RED}An error occurred while trying to establish the connection.")
                    error_shown = True
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a valid number.")
        exit(1)
else:
        print(f"{Fore.RED}Invalid number!")
        print(Fore.RESET)
        exit(1)
