import os
ruta='C:/Users/asus/Desktop/pdf prueba'
def indice_titulos():
    palabras=[]
    contenido=os.listdir(ruta)
    for i in contenido:
        x=i.split()
        for j in x:
            palabras.append(j)
    return palabras

print(indice_titulos())