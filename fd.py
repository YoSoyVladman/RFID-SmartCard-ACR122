import opc,time

numLEDs = 512
cliente = opc.Client('localhost:7890')

negro = [ (0,0,0) ] * numLEDs
blanco = [ (255,255,255) ] * numLEDs

# Fade to white
cliente.put_pixels(negro)
time.sleep(0.5)
cliente.put_pixels(blanco)
time.sleep(1)
cliente.put_pixels(negro)