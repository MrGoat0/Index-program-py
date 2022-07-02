import os
import pickle

class SearchEngine:
    def __init__(self):
        self.file_index=list()
        self.results=list()
        self.matches=0
        self.records=0
    def create_new_index(self, root_path):
        #Aqui llama a función que construye index para guardarlo
        # INSERT INDEX_MACHINE #

        #Guarda el Archivo
        with open(root_path+'/file_index.pkl','wb') as f:
            pickle.dump(self.file_index, f)
    def load_existing_index(self):
        # Revisa y carga un Index ya creado 
        try:
            with open('file_index.pkl','rb') as f: #no esta leyendo el .pkl
                self.file_index=pickle.load(f)
        except:
            self.file_index=list()
    def search(self, term, search_engine='contains'):
        #'Search for term based on search type'
        #reset variables
        self.results.clear()
        self.matches=0
        self.records=0
        
        #perform search 
        
