import os
import pickle
direc = 'C:/Users/asus/Desktop/pdf prueba'
files = os.listdir(direc)
#print(files)
x=input()
def index_pickle(file,x):
    index_pickle=open(x+'pdf prueba/index.pickle', 'wb')
    pickle.dump(file, index_pickle)
    index_pickle.close()

def abrir(file):
    archivo=open(file, 'rb')
    return pickle.load(archivo)
    
print(index_pickle(files,x))
