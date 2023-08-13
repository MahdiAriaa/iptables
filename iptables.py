import os
from colorama import Fore
import pyfiglet
from time import sleep

logo = pyfiglet.figlet_format("IP Tables", font="standard")
print(Fore.GREEN, logo, Fore.RESET)

print("your ip address")
os.system("hostname -I")

tunnel_ip = input("Enter tunnel IP : ")
panel_ip = input("Enter Panel IP : ")

os.system("sysctl net.ipv4.ip_forward=1")
os.system(f"iptables -t nat -A PREROUTING -p tcp --dport 22 -j DNAT --to-destination {tunnel_ip}")
os.system(f"iptables -t nat -A PREROUTING -j DNAT --to-destination {panel_ip}")
os.system("iptables -t nat -A POSTROUTING -j MASQUERADE")

print(Fore.YELLOW + " iptables STATUS " + Fore.RESET)
sleep(3)
os.system("iptables -L -n -t nat")