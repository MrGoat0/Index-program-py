import os
ruta='C:/Users/asus/Desktop/pdf prueba'
contenido=os.listdir(ruta)

archivos=[nombre for nombre in contenido]
print(archivos)
