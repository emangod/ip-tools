import os
import urllib.request as urllib2
import json
import sys
import time

while True:

  print("""██╗██████╗     ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██║██╔══██╗    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
██║██████╔╝    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
██║██╔═══╝     ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
██║██║         ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
╚═╝╚═╝         ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝""")

  ip = input("What is the ip you want to lookup: ")
  url = "http://ip-api.com/json/"
  response = urllib2.urlopen(url + ip)
  data = response.read()
  values = json.loads(data)

  print("IP: " + str(values['query']))
  print("Status: " + str(values['status']))
  print("Country: " + str(values['country']))
  print("Country Code: " + str(values['countryCode']))
  print("Region: " + str(values['region']))
  print("Region Name: " + str(values['regionName']))
  print("City: " + str(values['city']))
  print("Zip Code: " + str(values['zip']))
  print("Latitude: " + str(values['lat']))
  print("Longitude: " + str(values['lon']))
  print("Timezone: " + str(values['timezone']))
  print("Isp: " + str(values['isp']))
  print("Organization: " + str(values['org']))
  print("As: " + str(values['as']))