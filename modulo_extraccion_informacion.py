import json
import re
import socket
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



equipo = socket.gethostname()
print('Nombre Equipo Local: ', equipo)
iplocal = socket.gethostbyname(equipo)
print('IP LOCAL:  ', iplocal)


#IPv4
show =  urllib.request.urlopen('https://api.ipify.org?format=json')
data = show.read()
data = data.decode()
iprex = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]")
ip = iprex.search(data)
#print('IPv4:   ', ip.group())

show2 = urllib.request.urlopen('https://api.ipify.org')
data2 = show2.read().decode()
print('IPv4:   ', data2)

#IPv6

showip6 = urllib.request.urlopen('https://api6.ipify.org').read().decode()
print('IPv6:   ', showip6)

#API Geo
ip = data2
apikey = 'at_0GtZVBopnvev81eKk6AicxbX81rUI'
geollamada = 'https://geo.ipify.org/api/v1?apiKey='+ apikey+ '&ipAddress='+ data2
geo = urllib.request.urlopen(geollamada).read().decode()
try:
    js = json.loads(str(geo))
except:
    js = None

print(json.dumps(js, indent=4))

ip = js['ip']
pais = js['location']['country']
region = js['location']['region']
latitude = js['location']['lat']
longitude = js['location']['lng']
postalcode = js['location']['postalCode']
route = js['as']['route']
asn = js['as']['asn']
isp = js['isp']
domain = js['as']['domain']
type = js['as']['type']
name = js['as']['name']
geonameId = js['location']['geonameId']

print(ip)