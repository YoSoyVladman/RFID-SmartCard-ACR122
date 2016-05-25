import requests

url_v = 'http://papalote.cocoplan.mx/v0/visitante'
rfid = "34928319042016"
zona = 1
experiencia = 1

data_v = {'rfid':rfid,'experiencia':'1','zona':'1'}
rv  = requests.get(url_v, params = data_v)

print rv
print rv.status_code

if rv.status_code == requests.codes.ok:
	
	print rv.json()
