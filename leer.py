archivo = open("conf.txt",'r') 
contenido = archivo.read()
print contenido

for linea in archivo.readlines():
    print 'as'+linea