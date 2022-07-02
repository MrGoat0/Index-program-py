import os
import pickle

class search_engine:
    def __init__(self):
        self.file_index=list()
        self.results=list()
        self.matches=0
        self.records=0

    def create_new_index(self, root_path):
        #'Create a new index and save to file'
        #cont_root=os.listdir(root_path)
        #self.file_index=[name for name in cont_root]
        self.file_index=[(root, files) for root, dirs, files in os.walk(root_path) if files]

        # Save to file
        with open(root_path+'/file_index.pkl','wb') as f:
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
    s.search('Charles')

    print()
    print('>> There were {:,d} macthes out {:,d} records search.'.format(s.matches,s.records) )
    print()
    print('>> This query produced the following matches: \n')
    for match in s.results:
        print(match)

test1()