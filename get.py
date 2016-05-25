import requests

url = 'http://papalote.cocoplan.mx/v0/visitante'
rfid = "34928319042016"
zona = 1
experiencia = 1

data = {'rfid':rfid,'experiencia':'1','zona':'1'}
r = requests.get(url , params = data)

print r
print r.status_code

if r.status_code == requests.codes.ok:
	print r.json()
