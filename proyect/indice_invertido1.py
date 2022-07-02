import PyPDF2 as p2
import string
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import os
import pickle
def stemming(w):
    ps=PorterStemmer()
    return ps.stem(w)

def quitar_puntuación(pdf):
    letras_espacios=[]
    for i in pdf:
        if i.isalpha() or i.isspace():
            letras_espacios.append(i)
    return ''.join(letras_espacios)

def limpiador(texto):
    x=texto.keys()
    texto2=[]
    texto3=[]
    stopwords={'segundo', 'también', 'seis', 'propios', 'expresó', 'tercera', 'incluso', 'casi', 'está', 'cosas', 'ellas', 'donde', 'ella',
     'muy', 'podrían', 'dicho', 'siempre', 'consigue', 'entre', 'eras', 'hecho', 'estas', 'largo', 'atras', 'consiguen', 'agregó', 'sigue', 
     'hacia', 'muchos', 'tenido', 'eres', 'informó', 'haya', 'mismas', 'ambos', 'sus', 'mi', 'vaya', 'podria', 'que', 'algún', 'la', 'quien', 
     'ningunas', 'podeis', 'trabajo', 'quedó', 'estos', 'consideró', 'existe', 'gran', 'ninguna', 'varios', 'empleas', 'otra', 'ese', 'tan', 
     'misma', 'algo', 'se', 'puede', 'aquel', 'parte', 'trabajas', 'de', 'da', 'estais', 'pueda', 'haber', 'anterior', 'cuenta', 'sabemos', 
     'además', 'tienen', 'sí', 'tengo', 'intentamos', 'sean', 'decir', 'nuevos', 'aquellas', 'eramos', 'nuestros', 'solos', 'propio', 'dan', 
     'alguno', 'fue', 'unas', 'principalmente', 'quienes', 'junto', 'tal', 'otras', 'realizado', 'cierta', 'estamos', 'son', 'tras', 'su', 
     'ningún', 'partir', 'dos', 'estar', 'nadie', 'pero', 'primero', 'menos', 'han', 'hacemos', 'conseguir', 'unos', 'sin', 'consigues', 
     'realizar', 'mientras', 'arriba', 'bastante', 'sólo', 'desde', 'ser', 'sois', 'ciertas', 'dijeron', 'este', 'dice', 'ampleamos', 'través', 
     'considera', 'tres', 'aquellos', 'parece', 'el', 'cualquier', 'diferentes', 'voy', 'ver', 'había', 'explicó', 'última', 'realizó', 'en', 
     'manifestó', 'alrededor', 'sobre', 'ultimo', 'cerca', 'tener', 'hicieron', 'nuestras', 'nuevo', 'intenta', 'respecto', 'dejó', 'podrán', 
     'a', 'al', 'podriais', 'o', 'llevar', 'siendo', 'solas', 'tiene', 'eran', 'dado', 'hacerlo', 'debe', 'ha', 'tenemos', 'después', 'yo', 
     'por qué', 'y', 'uso', 'aseguró', 'aún', 'los', 'no', 'tuvo', 'alguna', 'dar', 'ellos', 'hemos', 'tendrán', 'fuimos', 'conseguimos', 
     'verdad', 'algunos', 'dieron', 'indicó', 'vais', 'encuentra', 'vamos', 'tampoco', 'debido', 'habrá', 'emplean', 'pocas', 'momento', 'será', 
     'adelante', 'están', 'poca', 'estan', 'fui', 'hacen', 'existen', 'van', 'podriamos', 'tiempo', 'actualmente', 'cierto', 'pueden', 'aunque', 
     'bajo', 'contra', 'ni', 'cinco', 'mencionó', 'somos', 'cual', 'eso', 'sea', 'ciertos', 'primeros', 'esas', 'ahí', 'así', 'fuera', 'vosotras', 
     'apenas', 'sola', 'va', 'dijo', 'uno', 'trabajar', 'trabajan', 'nos', 'mismo', 'nada', 'fin', 'es', 'tenía', 'para', 'encima', 'le', 'pasado', 
     'cuando', 'sabeis', 'usa', 'las', 'manera', 'modo', 'saben', 'si', 'diferente', 'intento', 'e', 'grandes', 'podría', 'aproximadamente', 
     'podemos', 'pesar', 'éstos', 'demás', 'pasada', 'solamente', 'estará', 'porque', 'buen', 'mucha', 'lado', 'serán', 'tendrá', 'últimas', 
     'poder', 'nuestra', 'intentais', 'creo', 'ahora', 'saber', 'haces', 'mio', 'embargo', 'toda', 'hizo', 'usais', 'me', 'sabes', 'estuvo', 
     'esto', 'llegó', 'trata', 'empleo', 'antes', 'era', 'ocho', 'haciendo', 'nosotros', 'usar', 'soy', 'vez', 'comentó', 'dio', 'estaban', 
     'vosotros', 'queremos', 'poco', 'usamos', 'igual', 'sido', 'varias', 'siete', 'éstas', 'otros', 'trabaja', 'muchas', 'esta', 'luego', 
     'solo', 'ningunos', 'hacer', 'quiere', 'verdadero', 'próximo', 'ayer', 'durante', 'todas', 'podrias', 'gueno', 'bien', 'segunda', 'algunas',
      'buenos', 'hasta', 'posible', 'aqui', 'lleva', 'trabajamos', 'hago', 'lo', 'propias', 'todos', 'tenga', 'nosotras', 'todo', 'conocer', 
      'señaló', 'intentan', 'mayor', 'cuales', 'consigo', 'mediante', 'propia', 'ante', 'estoy', 'les', 'ejemplo', 'estado', 'trabajais', 
      'mejor', 'del', 'valor', 'estaba', 'aquí', 'bueno', 'qué', 'quién', 'por', 'esa', 'habían', 'veces', 'nuestro', 'puedo', 'lugar', 'sería', 
      'dicen', 'todavía', 'pudo', 'intentas', 'él', 'hay', 'otro', 'más', 'un', 'verdadera', 'pues', 'con', 'ninguno', 'Ã©sta', 'empleais', 
      'último', 'usas', 'afirmó', 'he', 'ex', 'teneis', 'tuyo', 'dentro', 'podrá', 'esos', 'una', 'total', 'éste', 'cada', 'cómo', 'primer', 
      'usted', 'usan', 'podrian', 'cuatro', 'hubo', 'intentar', 'nuevas', 'fueron', 'sabe', 'mismos', 'sino', 'ello', 'haceis', 'hace', 
      'siguiente', 'pocos', 'según', 'últimos', 'próximos', 'ir', 'tanto', 'entonces', 'buenas', 'ya', 'poner', 'primera', 'como', 'nunca', 
      'buena', 'cuanto', 'nueva', 'mucho', 'emplear', 'hoy', 'deben'}
    
    for i in x:
        texto2.append(i.lower())
    for i in texto2:
        if i not in stopwords:
            texto3.append(stemming(i))
    return texto3

def es_pdf(pdf):
    d=dict()
    if '.PDF' in pdf:
        pdf=open(pdf,'rb')
        pdfread=p2.PdfFileReader(pdf)
        i=0
        while i<pdfread.getNumPages():
            pageinfo=pdfread.getPage(i)
            x=pageinfo.extractText().split()
            for j in x:
                word=quitar_puntuación(j)
                if word not in d:
                    d[word]=[]
                    d[word].append(1)
                else:
                    d[word][0]+=1  
            i+=1
    else:
        with open(pdf) as line:
            lines=line.readlines()
            #D+=lines
            for j in lines:
                x=j.split()
                for k in x:
                    word=quitar_puntuación(k)
                    if word not in d:
                        d[word]=[]
                        d[word].append(1)
                    else:
                        d[word][0]+=1
    return d

def es_txt(txt):
    d=dict()
    with open(txt) as line:
        lines=line.readlines()
        #D+=lines
        for i in lines:
            word=quitar_puntuación(i)
            if word not in d:
                d[word]=[]
                d[word].append(1)
            else:
                d[word][0]+=1
    return d
##################################################33            
ruta='C:/Users/asus/Desktop/pdf prueba'
contenido=os.listdir(ruta)
d=[]
num_pdf=1
pdf=[]
for nombre in contenido:
    x=es_pdf('C:/Users/asus/Desktop/pdf prueba/'+nombre)
    #print(x)
    d.append(x)
    y=pdf.append(num_pdf)
    num_pdf+=1
indice=dict()
arch=1
for i in d:
    #palabra: [2, [[1,1],[1,2]]]
    for word in i:
        if word not in indice:
            indice[word]=[]
            indice[word].append([arch, i[word]])
        else:
            indice[word].append([arch, i[word]])
    arch+=1 

#print(indice)










#archivos=[nombre for nombre in contenido]
#print('C:/Users/asus/Desktop/pdf prueba/'+archivos)
#pdf1='C:/Users/asus/Desktop/pdf prueba/Julio Cortazar_Bestiario.pdf'
#print(limpiador(es_pdf(pdf1)))