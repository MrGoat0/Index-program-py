import PyPDF2 as p2
import string
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize
import os   
import pickle
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
indice=dict()
#indice_titulos=[]
pdf=[]
ruta=''
primera_busqueda=list()
posible_pdf=[]
######################################################################################################
def stemming(w):  #Retorna la palabra en su 'raíz'
    ps=PorterStemmer()
    return ps.stem(w)

def quitar_puntuación(pdf):  #Quita espacios en blanco y puntuación
    letras_espacios=[]
    for i in pdf:
        if i.isalpha() or i.isspace():
            letras_espacios.append(i)
    return ''.join(letras_espacios)

def limpiador(w):  #Quita stopwords, vuelve todo minuscula, y aplica la función de stemming
    global stopwords
    x=w.lower()
    if x not in stopwords:
        return stemming(x)
####################################################################################################################################################

#######################################################################################################

def es_pdf(pdf):  #Esta función lee un .pdf o .txt y le saca un indice
    d=dict()
    if ('.PDF' in pdf) or ('.pdf' in pdf):  # Si es .pdf va aqui
        pdf=open(pdf,'rb')
        pdfread=p2.PdfFileReader(pdf)
        i=0
        while i<pdfread.getNumPages():
            pageinfo=pdfread.getPage(i)
            x=pageinfo.extractText().split()
            for j in x:
                word=limpiador(quitar_puntuación(j))
                if word not in d:
                    d[word]=[]
                    d[word].append(1)
                else:
                    d[word][0]+=1  
            i+=1
    else:
        with open(pdf) as line:   # Si es .txt va aqui 
            lines=line.readlines()
            for j in lines:
                x=j.split()
                for k in x:
                    word=limpiador(quitar_puntuación(k))
                    if word not in d:
                        d[word]=[]
                        d[word].append(1)
                    else:
                        d[word][0]+=1
    return d

##############################################################################################################

def crear_indice(ruta): #Esta función crea un indice de la ruta seleccionada y devuelve una lista para buscar 
    #ruta='C:/Users/asus/Desktop/pdf prueba'
    global indice
    global pdf
    contenido=os.listdir(ruta)
    d=[]
    num_pdf=0
    pdf=[]
    for nombre in contenido:
        x=es_pdf(ruta+'/'+nombre)
        #print(x)
        d.append(x)
        pdf.append(num_pdf)
        num_pdf+=1

    indice=dict()
    arch=1
    for i in d:
        #palabra: [2, [[1,1],[1,2]]]. Este es el formato dentro del indice, al tratarse de un diccionario, será rápido buscar con un for
        for word in i:        
            if word not in indice:
                indice[word]=[]
                indice[word].append([arch, i[word]])
            else:
                indice[word].append([arch, i[word]])
        arch+=1 

    #Guarda un archivo 'index.pickle' en la ruta seleccionada
    fichero=open(ruta+'/index.pickle','wb')
    pickle.dump(indice,fichero)
    fichero.close()
###########################################################################################################################

###########################################################################################################################
def crear_txt_titulos():  #Crea un .txt con los titulos de los archivos
    global ruta
    contenido=os.listdir(ruta)
    archivo=open(ruta+'/titulos.txt','w')
    for i in contenido:
        archivo.write(i+'\n')
    archivo.close() 

#############################################################################################################################
def cargar_index(ruta):
    #Carga un 'index.pickle' que ya existe
    contenido=os.listdir(ruta)
    if 'index.pickle' in contenido:
        menu_main2()       
    else:
        if 'titulos' not in contenido:
            crear_txt_titulos()
            crear_indice(ruta)
        #crear_indice(ruta)  #Si no encuentra el 'index.pickle' en la ruta llama a la función para crear un indice
#i=cargar_index('C:/Users/asus/Desktop/pdf prueba')
#print(i)
#####################################################################################################################
def menu_main2(): #Este menu muestra la opción de hacer una busqueda
    global salir
    print(
    '                   |LISTO PARA BUSCAR|'+'\n'+
    '_________________________________________________________'+'\n'+
    'Para entrar en la opción deseada pulsa el botón indicado.'+'\n'+
    'Tienes las siguientes opciones: '+'\n'+
    '\n'+
    'Selección del directorio de búsqueda: 1'+'\n'+ 
    'Hacer una nueva busqueda: 2\n'+
    'Créditos: 3'+'\n'+
    'Salir del motor de busqueda: q')
    x=str(input())
    if x == 'q':
        salir=1
        return
    if x == '1':   #Por si se quiere buscar en otro directorio
        menu_busqueda1()
    elif x== '2':
        hacer_busqueda()
    elif x == '3':
        print('       Programa creado por:\n'.upper()+
        '_Kevin Sebastian Barrera Castañeda_\n'+
        '_Jonathan Steven Roa Benavides_\n'+
        '_juan Carlos Vargas Cisneros_\n')
        menu_main2()
    else:
        print('Intenta seleccionar una opción.\n')
    if salir !=1:
        menu_main2()
#####################################################################################################################
def lanzar_pdf(path): #Esta opción toma una ruta de acceso y abre el .pdf o.txt de esa ruta
    os.startfile(path)

###################################################################################################################
#INTERFAZ#

def abrir_archivos():  #Esta función muestra al usuario los posibles resultados y el número para abrir el archivo,
    
    contenido=os.listdir(ruta)
    print()
    print('Tienes las siguientes opciones para buscar; selecciona según el numero indicado. ')
    print('| Ruta del archivo | Número para abrir el archivo | Repetición del termino de busqueda en el texto |')
    term=int(input('¿Cuál quieres abrir? '))
    if term not in posible_pdf:
        print('Vuelva a intentar\n')
        abrir_archivos()
    else:
        lanzar_pdf(ruta+'/'+contenido[term]) #llama a la función para abrir el archivo del numero que diga el usuario
        
####################################################################################################################
salir=0
def hacer_busqueda(): #NO FUNCIONA
    #global indice_titulos
    #global indice
    #index_titulos()    
    #contenido=os.listdir(ruta)
    #primera_busqueda=list()
    #primera=[]
    #search_type='constains'
    #posibles_sol=[(root, files) for root, dirs, files in os.walk(ruta) if files]
    #print('Vamos a hacer una busqueda, solamente escribe la palabra sobre lo que quieres saber.\n')
    #term=input('¿Sobre qué o quién quieres leer? ')
    #print(posibles_sol)
    #term_ready=stemming(term.lower())
    #for path,files in posibles_sol:
    #    for file in files:
    #        if (term.lower() in file.lower()):
    #            result = path.replace('\\','/') + '/' + file
    #            primera_busqueda.append(result)
     #       elif file.lower().startswith(term.lower()):
      #          result = path.replace('\\','/') + '/' + file
       #         primera_busqueda.append(result)
        #    elif file.lower().endswith(term.lower()):
         #       result = path.replace('\\','/') + '/' + file
          #      primera_busqueda.append(result)
           # else:
            #    continue
    global primera_busqueda
    global posible_pdf
    busqueda_uno=[]
    posible_pdf=[]
    contenido=os.listdir(ruta)
    term=input('palabra a buscar: ').split()
    terminos_de_busqueda=[]
    inter=[]
    for i in term:
        terminos_de_busqueda.append(stemming(quitar_puntuación(i.lower())))
    x=open(ruta+'/index.pickle','rb')
    indice=pickle.load(x)
    for i in terminos_de_busqueda:
        for j in indice:
            if i==j:               
                if len(terminos_de_busqueda)==1:
                    busqueda_uno.append(indice.get(i))
                else:
                    for k in terminos_de_busqueda:
                        for p in indice:
                            if k==p:
                                inter.append(indice.get(k))
    print('Tienes las siguientes opciones: \n')
    if len(terminos_de_busqueda)==1:
        for i in busqueda_uno:
            for j in i:
                if ('titulos.txt'==j or 'index.pickle'==j):
                    continue
                else:   
                    print(ruta+'/'+contenido[j[0]-1],'|||',j[0]-1)
                    posible_pdf.append(j[0]-1)
                abrir_archivos()
    elif len(terminos_de_busqueda)>1:
        for i in inter:
            for j in i:
                if ('titulos.txt'==j or 'index.pickle'==j):
                    continue
                else:   
                    print(ruta+'/'+contenido[j[0]-1],'|||',j[0]-1)
                    posible_pdf.append(j[0]-1)
                abrir_archivos()
    else:
        menu_main2()

    
    
##################################################################################################################



#########################################################################################################################################

##########################################################################################################################################
def menu_busqueda1(): #Crea el index del directorio colocado y devuelve al siguiente menu donde se realiza la busqueda
    global ruta
    print()
    print('_Tu directorio debe contener '"letra"':/ para ser valido.\n')
    print('_La creación de un nuevo indice de busqueda puede tardar. ¡No desesperes!\n')
    ruta=str(input('Escribe el directorio donde quieres buscar: '))
    if ':/' or ':\'' in ruta: 
        cargar_index(ruta)
        menu_main2()
    else: menu_busqueda1() #confirma si lo ingresado sirve como directorio
    print()
    

##################################################################################################################    

def main():  #Este es el primer menu y no muestra la opción de hacer una nueva busqueda
    global salir
    print(
    '            |Bienvenido al motor de búsqueda|'+'\n'+
    '_________________________________________________________'+'\n'+
    'Para entrar en la opción deseada pulsa el botón indicado.'+'\n'+
    'Tienes las siguientes opciones: '+'\n'+
    '\n'+
    'Selección del directorio de búsqueda: 1'+'\n'+
    'Créditos: 2'+'\n'+
    'Salir del motor de busqueda: q')
    x=str(input())
    if x == 'q':
        salir=1
        return
    if x == '1':
        menu_busqueda1()        
    elif x == '2':
        print('       Programa creado por:\n'.upper()+
        '_Kevin Sebastian Barrera Castañeda_\n'+
        '_Jonathan Steven Roa Benavides_\n'+
        '_juan Carlos Vargas Cisneros_\n')
        main()
    else:
        print('Intenta seleccionar una opción.\n')
    if salir !=1:
        main()
main()

