import re, sys, signal, os, time, datetime
import requests
from smartcard.System import readers
from smartcard.util import toHexString
import opc


# se definen los APDUs 
# 
COMMAND = [0xff, 0xCA, 0x00, 0x00, 0x00]

####### FACECANDY ####### 
numLEDs = 512
cliente = opc.Client('localhost:7890')
negro = [ (0,0,0) ] * numLEDs
blanco = [ (255,255,255) ] * numLEDs
rojo = [ (255,0,0) ] * numLEDs
####### ID DE LA EXPERIENCIA ########
Z = 1
E = 1

def encender_led():
    cliente.put_pixels(negro)
    time.sleep(.1)
    cliente.put_pixels(blanco)
    time.sleep(1.5)
    cliente.put_pixels(negro)


def encender_error():
    cliente.put_pixels(negro)
    time.sleep(.1)
    cliente.put_pixels(rojo)
    time.sleep(1.5)
    cliente.put_pixels(negro)


def sumar_puntos(rfid,puntos):
    #encender()
    url = 'http://papalote.cocoplan.mx/v0/agregar_puntos'
    data = {'rfid':rfid,'puntos':puntos,'zona':Z,'experiencia':E}
    r = requests.post(url,data)
    print r



if __name__ == '__main__':
    r = readers()
    print 'lectores disponibles', r
    lector = r[0]
    print 'Usando :', lector

    while(1):
        try:
            conexion= lector.createConnection()
            conexion.connect()
            #### enviar datos ####
            data, sw1, sw2 = conexion.transmit(COMMAND)

            print "Command: %02X %02X" % (sw1, sw2)
            a = sw1
            print a
            if a == 144:
                hoy = datetime.datetime.now()
                dia = hoy.day
                print dia
	            mes = hoy.month
                print mes
		        ano = hoy.year
                print ano
                #print 'datos >:', data
                v = data[::-1]
                #print 'invertido',v
                hexa = toHexString(v)
                hexan = hexa.split( )
                #print 'hexa',hexa
                #print 'hexan',hexan
                tam = len(hexan)
                #print 'leng', tam
                cadena = ''

                for x in range(tam):
                    cadena = cadena + str(hexan[x])

                #print 'cadena',cadena
                decimal = int(cadena,16)
                print 'decimal',decimal
                ###### GET #####
                url_v = 'http://papalote.cocoplan.mx/v0/visitante'
                data_v = {'rfid':str(decimal),'experiencia':E,'zona':Z}
                rv  = requests.get(url_v, params = data_v)
                print rv
                print rv.status_code
                ##########
                if rv.status_code == requests.codes.ok:
                    encender_led()
                    sumar_puntos(str(decimal),'10')
                else:
                    encender_error()
                # Read data from RFID reader
                ############
                
        except Exception, e:
            continue
