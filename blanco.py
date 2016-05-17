from smartcard.System import readers
from smartcard.util import toHexString
import opc,time

# se definen los APDUs 
SELECT = [0x00, 0xA4, 0x04, 0x00, 0x0A, 0xA0, 0x00, 0x00, 0x00, 0x62,
    0x03, 0x01, 0x0C, 0x06, 0x01]
COMMAND = [0x00, 0x00, 0x00, 0x00]

numLEDs = 512
cliente = opc.Client('localhost:7890')

negro = [ (0,0,0) ] * numLEDs
blanco = [ (255,255,255) ] * numLEDs



def encender_led():
	cliente.put_pixels(negro)
	time.sleep(.5)
	cliente.put_pixels(blanco)
	time.sleep(2)
	cliente.put_pixels(negro)

####### INDEX #######
r = readers()
print 'lectores disponibles', r

lector = r[0]
print 'Usando :', lector

encender_led()