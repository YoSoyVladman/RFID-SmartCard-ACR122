import opc,time

numLEDs = 512
cliente = opc.Client('localhost:7890')

negro = [ (0,0,0) ] * numLEDs
blanco = [ (255,255,255) ] * numLEDs

# Fade to white
# 
# 

function encender_led():
	cliente.put_pixels(negro)
	time.sleep(.5)
	cliente.put_pixels(blanco)
	time.sleep(2)
	cliente.put_pixels(negro)



encender_led()