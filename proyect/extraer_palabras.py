import string
def extraer_palabras(pdf):
    D=set()
    pal=pdf.split()
    for i in pal:
        D.add(i)
    return D
def quitar_puntuación(pdf):
    letras_espacios=[]
    for i in pdf:
        if i.isalpha() or i.isspace():
            letras_espacios.append(i)
    return ''.join(letras_espacios)
def quitar_simbolos(texto):
    texto1=[]
    simbolos={'?','¿','.',',',';','-','_','(',')','!','¡','"','š','š'}
    for i in texto:
        for k in i:
            if k in simbolos:
                limpia=i.replace(k,'')
                texto1.append(limpia)
    return texto1

texto=['adiós', 'desee', 'característica', 'mucha', 'personalidades']


print(quitar_simbolos(texto))