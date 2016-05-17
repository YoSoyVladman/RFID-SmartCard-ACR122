import re, sys, signal, os, time, datetime
import requests
from smartcard.System import readers
from smartcard.util import toHexString
##import opc

# se definen los APDUs 
# 
COMMAND = [0xff, 0xCA, 0x00, 0x00, 0x00]

####### FACECANDY ####### 
numLEDs = 512
#cliente = opc.Client('localhost:7890')
negro = [ (0,0,0) ] * numLEDs
blanco = [ (255,255,255) ] * numLEDs



def encender_led():
    cliente.put_pixels(negro)
    time.sleep(.5)
    cliente.put_pixels(blanco)
    time.sleep(2)
    cliente.put_pixels(negro)


def sumar_puntos(rfid,puntos):
    #encender()
    url = 'http://papalote.cocoplan.mx/v0/agregar_puntos'
    data = {'rfid':rfid,'puntos':puntos}
    r = requests.post(url,data)
    print r



if __name__ == '__main__':
    r = readers()
    print 'lectores disponibles', r
    lector = r[0]
    print 'Usando :', lector
    conexion= lector.createConnection()
    conexion.connect()
    #### enviar datos ####
    data, sw1, sw2 = conexion.transmit(COMMAND)

    print "Command: %02X %02X" % (sw1, sw2)
    a = sw1
    print a
    if a == 144:
        print 'datos >:', data
        v = data[::-1]
        print v
        hexa = toHexString(v)
        hexan = hexa.split( )
        print hexa, hexan
        tipo = type(hexan)
        print 'tipo ', tipo
        tam = len(hexan)
        print 'leng', tam
        cadena = ''


      # Read data from RFID reader
