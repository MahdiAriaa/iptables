# utf-8
# create by : Mahdi Aria
# script Language => Python

import os


os.system("clear")


print("your ip address")
os.system("hostname -I")
print(" ")

tunnel_ip = input("Enter tunnel IP : ")
panel_ip = input("Enter Panel IP : ")

os.system("sysctl net.ipv4.ip_forward=1")
os.system(f"iptables -t nat -A PREROUTING -p tcp --dport 22 -j DNAT --to-destination {tunnel_ip}")
os.system(f"iptables -t nat -A PREROUTING -j DNAT --to-destination {panel_ip}")
os.system("iptables -t nat -A POSTROUTING -j MASQUERADE")

os.system("iptables -L -n -t nat")
