from Bio import Entrez
import re
import pandas as pd

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
    
    contentsse = re.sub(r'\s+[Eceinlort]{10}\s+[aders]{7}.*','',archivo)
    contentssc = re.sub(r'\s[\w._%+-]+@[\w.-]+\.[a-zA-Z]{1,4}','',contentsse)
    contentsna = re.sub(r'\..*\d.*\,',',',contentssc)
    contentsnu = re.sub(r'\..*\d.*','',contentsna)
    x=contentsnu[1:].split('PMID-')
    ID=[]
    AU=[]
    DP=[]
    pre_AD=[]
    for PMID in x:
        w=PMID.split('\n')
        AUc=0
        ID.append(w[0])
        for fila in w:
            v=fila.split(' ')
            if v[0] == 'DP':
                DP.append(v[3])
            if v[0] == 'AU':
                AUc=AUc+1
            if v[0] == 'AD':
                u=fila.split(',')
                pre_AD.append(u[-1])
        AU.append(AUc)
    ID.pop(0)
    AU.pop(0)
    pre_AD.pop(-5)

    AP=[]
    for dire in pre_AD:
        s=dire
        t=dire.split(' ')
        if t[0] == 'AD':
            s=t[-1]   
        AP.append(s)


    b=0
    AD =[0]*len(AP)

    for obj in AP:
        bytes(obj,encoding="utf8")
        if obj != '':
            g=obj
            if g[0] == ' ':
                g = re.sub (r'^\s','',g)
            if g[-1] == '.':
                g = re.sub (r'\.$','',g)
            g = re.sub (r'\.$','',g)
            g = re.sub (r'\s$','',g)
        AD[b]=g
        b=b+1

#Se cambio Netherlands por The Netherlands
    Countries_molde=['Andorra','United Arab Emirates ','Afghanistan','Antigua and Barbuda','Anguilla','Albania','Armenia','Netherlands Antilles','Angola','Antarctica','Argentina','American Samoa','Austria','Australia','Aruba','Azerbaijan','Bosnia and Herzegovina','Barbados','Bangladesh','Belgium','Burkina Faso','Bulgaria','Bahrain', 'Burundi','Benin','Bermuda','Brunei','Bolivia', 'Brazil','Bahamas','Bhutan','Bouvet Island','Botswana','Belarus','Belize','Canada','Cocos [Keeling] Islands','Congo [DRC]','Central African Republic','Congo [Republic]', 'Switzerland',"Côte d'Ivoire",'Cook Islands','Chile','Cameroon','China','Colombia','Costa Rica','Cuba', 'Cape Verde','Christmas Island','Cyprus','Czech Republic','Germany','Djibouti','Denmark','Dominica','Dominican Republic','Algeria','Ecuador' ,'Estonia','Egypt','Western Sahara','Eritrea','Spain','Ethiopia','Finland','Fiji','Falkland Islands [Islas Malvinas]','Micronesia','Faroe Islands','France','Gabon', 'United Kingdom','Grenada','Georgia','French Guiana','Guernsey','Ghana','Gibraltar','Greenland','Gambia', 'Guinea','Guadeloupe','Equatorial Guinea','Greece','South Georgia and the South Sandwich Islands','Guatemala','Guam','Guinea-Bissau','Guyana','Gaza Strip','Hong Kong','Heard Island and McDonald Islands','Honduras','Croatia', 'Haiti','Hungary','Indonesia','Ireland' ,'Israel','Isle of Man','India','British Indian Ocean Territory','Iraq', 'Iran','Iceland','Italy','Jersey','Jamaica','Jordan', 'Japan','Kenya','Kyrgyzstan','Cambodia','Kiribati','Comoros','Saint Kitts and Nevis','North Korea','South Korea','Kuwait','Cayman Islands','Kazakhstan','Laos','Lebanon','Saint Lucia','Liechtenstein','Sri Lanka','Liberia','Lesotho','Lithuania','Luxembourg','Latvia' ,'Libya','Morocco','Monaco','Moldova','Montenegro','Madagascar','Marshall Islands','Macedonia [FYROM]','Mali','Myanmar [Burma]','Mongolia' ,'Macau','Northern Mariana Islands','Martinique','Mauritania','Montserrat','Malta','Mauritius','Maldives','Malawi','Mexico','Malaysia' ,'Mozambique','Namibia','New Caledonia','Niger','Norfolk Island','Nigeria','Nicaragua','The Netherlands','Norway','Nepal','Nauru', 'Niue','New Zealand','Oman','Panama','Peru','French Polynesia', 'Papua New Guinea','Philippines','Pakistan','Poland','Saint Pierre and Miquelon' ,'Pitcairn Islands','Puerto Rico','Palestinian Territories','Portugal','Palau','Paraguay','Qatar','Réunion','Romania', 'Serbia','Russia' ,'Rwanda','Saudi Arabia','Solomon Islands','Seychelles','Sudan','Sweden','Singapore','Saint Helena','Slovenia', 'Svalbard and Jan Mayen','Slovakia','Sierra Leone','San Marino','Senegal','Somalia','Suriname','São Tomé and Príncipe','El Salvador','Syria', 'Swaziland' ,'Turks and Caicos Islands','Chad','French Southern Territories','Togo','Thailand','Tajikistan','Tokelau','Timor-Leste','Turkmenistan' ,'Tunisia','Tonga','Turkey','Trinidad and Tobago','Tuvalu','Taiwan','Tanzania','Ukraine','Uganda','U.S. Minor Outlying Islands','United States of America','Uruguay','Uzbekistan','Vatican City','Saint Vincent and the Grenadines','Venezuela', 'British Virgin Islands','U.S. Virgin Islands','Vietnam','Vanuatu','Wallis and Futuna','Samoa','Kosovo','Yemen','Mayotte','South Africa','Zambia','Zimbabwe']

    o=AD
    f=Countries_molde
    i=len(f)
    ADh=[0]*i
    k=0
    for elem in f:
        d=0
        for comp in o:
            if elem == str(comp):
                d=d+1
        ADh[k]=d
        k=k+1


    AD=[]
    CO=[]
    n=0
    for elem in ADh:
        if str(elem) != '0':
            AD.append(elem)
            m=Countries_molde[n]
            CO.append(m)
        n=n+1

    TableA = pd.DataFrame({'PMID' : ID,
                           'DP_year' : DP})

    TableB = pd.DataFrame({'PMID' : ID,
                           'num_auth' : AU})

    TableC = pd.DataFrame({'Country' : CO,
                           'num_auth' : AD})
    
    if tipo =='DP':
        return TableA
    if tipo == 'AU':
        return TableB
    if tipo == 'AD':
        return TableC