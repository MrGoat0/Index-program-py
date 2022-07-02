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

##################################################33            


class search_engine:
    def __init__(self):
        self.file_index=dict()
        self.results=list()
        #self.matches=0
        #self.records=0

    def create_new_index(self, ruta):
        #Crea un nuevo index de la ruta seleccionada
        contenido=os.listdir(ruta)
        rutas_archivos=[]  #almacena las rutas del directorio
        num_pdf=1  
        posicion_pdf=[]  #almacena el numero de pdf para abrir luego
        for nombre in contenido:
            x=es_pdf(ruta+nombre)
            rutas_archivos.append(x)
            posicion_pdf.append(num_pdf)
            num_pdf+=1
        #indice=dict()
        arch=1
        for i in rutas_archivos:
        #palabra: [2, [[1,1],[1,2]]]
            for word in i:
                if word not in self.file_index:
                    self.file_index[word]=[]
                    self.file_index[word].append([arch, i[word]])
                else:
                    self.file_index[word].append([arch, i[word]])
            arch+=1

        # Guarda el 'index.pickle' en el directorio
        with open(ruta+'/index.pickle','wb') as f:
            pickle.dump(self.file_index, f)
        
    def load_existing_index(self):
        #'Load existing index'
        try:
            with open('file_index.pkl','rb') as f:
                self.file_index=pickle.load(f)
        except:
            self.file_index=list()

    def search(self, term, search_type='contains'):
        #'Search for term based on search type'
        #reset variables
        self.results.clear()
        self.matches=0
        self.records=0
        
        #perform search 
        for path, files in self.file_index:
            for file in files:
                self.records+=1
                if (search_type == 'contains' and term.lower() in file.lower() or
                    search_type == 'startswith' and file.lower().startswith(term.lower()) or
                    search_type == 'endswith' and file.lower().endswith(term.lower())):

                    result = path.replace('\\','/') + '/' + file
                    self.results.append(result)
                    self.matches +=1
                else:
                    continue
        #save search results 
        #with open('search_results.txt','w') as f:
        #    for row in self.results:
        #        f.write(row + '\n' )

def test1():
    s = search_engine()
    s.create_new_index('C:/Users/asus/Desktop/pdf prueba')
    #s.load_existing_index()
    #s.search('Charles')

    #print()
    #print('>> There were {:,d} macthes out {:,d} records search.'.format(s.matches,s.records) )
    #print()
    #print('>> This query produced the following matches: \n')
    #for match in s.results:
    #    print(match)

test1()
