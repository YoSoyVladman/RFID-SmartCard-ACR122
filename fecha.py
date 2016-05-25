import time, datetime

hoy = datetime.datetime.now()
dia = str(hoy.day)
l_d = len(dia)
if l_d == 1:
        dia = '0'+dia
print dia
mes = str(hoy.month)
l_m = len(mes)
if l_m == 1:
        mes = '0'+mes
print mes
ano = str(hoy.year)
print ano
fecha = dia + mes + ano[2:]
print fecha


rfid = '123'
x = rfid + fecha

print x
