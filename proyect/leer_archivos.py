import PyPDF2 as p2
import string
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

pdf2='C:/Users/asus/Desktop/pdf prueba/Carl Sagan_Cosmos.pdf'

def es_pdf(pdf):
    pdf=open(str(pdf),'rb')
    pdfread=p2.PdfFileReader(pdf)
    D=set()
    i=0
    while i<pdfread.getNumPages():
        pageinfo=pdfread.getPage(i)
        
        x=pageinfo.extractText().split()
        for j in x:
            
            #print(j)
            D.add(j)
        i+=1
    return D

es_pdf(pdf2)