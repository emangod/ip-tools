import socket
import subprocess
import sys
from datetime import datetime

subprocess. call("clear", shell = True)

print ("""██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═""")

rememoteServer = input("Enter the host: ")
rememoteServerIP = socket.gethostbyname(rememoteServer)

print ("")
print ("Scanning host", rememoteServer)
print ("")

t1 = datetime.now()

try:
  for port in range (1, 5000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((rememoteServerIP, port))
    if result == 0:
      print ("port {}:  open".format(port))
      sock.close()

except KeyboardInterrupt:
  print ("You pressed [CRTL+C]")
  sys.exit

except socket.gaierror:
  print ("Host faild to connect")
  sys.exit()

except socket.error:
  print ("could not connect")
  sys.exit()

t2 = datetime.now()

total = t2 - t1

print ("Scanning Completed in", total)