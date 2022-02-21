from Bio import Entrez
import re

def download_pubmed(keyword):
    
    """ La función download_pubmed recibe un argumento, que corresponde a palabras claves con las cuales se realizará una búsqueda 
    en Pubmed y  retorna la búsqueda en la base de datos antes nombrada, tal cual una descarga tipo PubMed.
    keyword: son palabras claves de búsqueda"""
    
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
    datapub = re.sub(r'\n\s{6}','', data)
    return datapub


    
def mining_pubs(tipo,archivo):
    """ La función mining_pubs recibe dos argumentos, que corresponde al tipo de minado de datos que se desea y el documento del 
    cual se va a extraer los datos.
    Tipo: puede ser DP, AU o AD.
           "DP" --> recupera el año de publicación del artículo. El retorno es un dataframe con el PMID y el DP_year.
           "AU" --> recupera el número de autores por PMID. El retorno es un dataframe con el PMID y el num_auth.
           "AD" -->recupera el conteo de autores por país. El retorno es un dataframe con el country y el num_auth.
    Archivo: corresponde al archivo del cual se extraerá la infomarción""" 
    
#df2 = pd.DataFrame({'a' : [2,3,4,5,6],
 #                   'b' : [3,1,9,12,2],
  #                  'c' : [5.0, 1.4, 1.2, 0.8, 2.3],
   #                 'd' : pd.Categorical(['caballo', 'gato', 'perro', 'tortuga', 'conejo']),
    #                'e' : [13, 11, None, None, 9]}, index=[1,2,3,4,5])
#df2
  #  if tipo =='DP':
    #    z=re.findall(r'[DIMP]{4}.*\d\n',archivo)
   #     y=re.findall(r'[DP]{2}\s\s.*\d.*\n+[IT]{2}',archivo)
 #       ....
  #  if tipo =='AU':
   #     
 #   if tipo =='AD':
    
 #   return