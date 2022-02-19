from Bio import Entrez
import re

c = []

def download_pubmed(keyword):
    """Docstring download_pubmed (explicacion)"""
    Entrez.email = "gualapuro.moises@gmail.com"
    handle = Entrez.esearch(db="pubmed", 
                            term="Dengue network[Title/Abstract]",
                            usehistory="y")
    record = Entrez.read(handle)
    handle.close()
    id_list = record["IdList"]
    a=[]
    a.extend(record.values())
    return a

def mining_pubs(tipo):
    """Docstring mining_pubs"""
    return