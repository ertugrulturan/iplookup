import argparse
import requests
import json
import socket
import sys
from sys import argv
import os

parser = argparse.ArgumentParser()

parser.add_argument("-host", type=str, dest='target', required=True)

args = parser.parse_args()

lightblue =  '\033[94m'
clear =      '\033[0m'
bold =       '\033[01m'
red =        '\033[31m'
yellow =     '\033[93m'
gray =      '\033[90m'

agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}

ip  = args.target

api2 = "https://ipapi.co/" 

api = "http://ip-api.com/json/"

apic = "?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"

ipv4 = "https://ifconfig.me/all.json"

coun = "https://api.myip.com/"

opmap = "https://www.openstreetmap.org/#map=8/"

try:
        data = requests.get(api+ip+apic, headers=agent ).json()
        data2 = requests.get(api2+ip+"/json/", headers=agent).json() 
        ipv4 = requests.get(ipv4, headers=agent).json()
        coun = requests.get(coun, headers=agent).json()
        a432 = requests.get(api+ipv4['ip_addr']+apic, headers=agent).json()
        sys.stdout.flush()
        blue = lightblue+bold+"[➛]"
        yell = yellow+bold+"[➛]"
        gray1 = gray+bold+"[↷]"
        print("Coders: https://obir.ninja/")
        print(yell, "Target:", data['query'])
        print(yell, "Lookup Status:", data['status'])
        print(blue, "ISP:", data['isp'])
        print(blue, "Organisation:", data['org'])
        print(blue, "City:", data['city'])
        print(blue, "Region name:", data['regionName'])
        print(blue, "AS Number:", data['as'])
        print(blue, "Zip:", data['zip'])
        print(blue, "Proxy:", data['proxy'])
        print(blue, "Reverse:", data['reverse'])
        print(blue, "Hosting:", data['hosting'])
        print(blue, "Latitude:", data['lat'])
        print(blue, "Longitude:", data['lon'])
        print(blue, "Map:", opmap+str(data['lat'])+"/"+str(data['lon']))
        print(" "+clear)
        print(gray1, "What they can see about you"  )
        print(yell, "Your Public IPV4:", ipv4['ip_addr'])
        print(blue, "Your Country:", coun['country'])
        print(blue, "ISP:", a432['isp'])
        print(blue, "Reverse:", a432['reverse'])
        print(blue, "Hostname:",socket.gethostname())
        print(blue, "Latitude:", a432['lat'])
        print(blue, "Longitude:", a432['lon'])
        print(blue, "Map:", opmap+str(a432['lat'])+"/"+str(a432['lon']))

except KeyboardInterrupt:
        print('User requested exit'+clear)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
    print(red+bold+"[!]"+"Connection Error!"+clear)
    sys.exit(1)
