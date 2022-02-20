from Bio import Entrez
import re

def download_pubmed(keyword):
    
    """ La función download_pubmed recibe un argumento, que corresponde a palabras claves con las cuales se realizará una búsqueda 
    en Pubmed y  retorna  (explicacion)"""
    
    
    Entrez.email = "salcanshirley1b@gmail.com"
    rec = Entrez.read(Entrez.esearch(db="pubmed", 
                            term=keyword,
                            usehistory="y"))
    webenv = rec["WebEnv"]
    query_key = rec["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                           rettype="medline", 
                           retmode="text", 
                           retstart=0,
                           retmax=543, webenv=webenv, query_key=query_key)
    data = handle.read()
    return data


   # record = Entrez.read(handle)
    
#def mining_pubs(tipo):
 #   """Docstring mining_pubs""" 
#df2 = pd.DataFrame({'a' : [2,3,4,5,6],
 #                   'b' : [3,1,9,12,2],
  #                  'c' : [5.0, 1.4, 1.2, 0.8, 2.3],
   #                 'd' : pd.Categorical(['caballo', 'gato', 'perro', 'tortuga', 'conejo']),
    #                'e' : [13, 11, None, None, 9]}, index=[1,2,3,4,5])
#df2
#    if tipo =='DP':
 #       ....
  #  if tipo =='AU':
   #     
    #if tipo =='AD':
    
 #   return