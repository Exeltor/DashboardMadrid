#!/usr/bin/env python3
from bs4 import BeautifulSoup #Importamos la libreria de Scraping
from urllib.request import urlopen #Importamos la libreria de apertura de URL

#Declaramos en dominio principal y los diferentes subdominios existentes
mainDom = "https://www.metromadrid.es/es/linea/"
lineasEndPoint = ['linea-1','linea-2','linea-3','linea-4','linea-5','linea-6-circular','linea-7',
                'linea-8','linea-9','linea-10','linea-11','linea-12-metrosur','ramal','ml1','ml2','ml3']  

#Creamos una lista auxiliar para almacenar los elementos formateados
lineasFormateadas = [] 

#Iteramos por la lista de subdominios generada anteriormente
for endPoint in lineasEndPoint:
    currDom = mainDom + endPoint #Concatenamos el dominio principal con el subdominio para obtener la direccion final
    page = urlopen(currDom) #Abrimos la URL resultante
    soup = BeautifulSoup(page, 'html.parser') #Inicializamos la pagina abierta en el Scraper

    #Parseamos los elementos de nombre, estado e imagen de la linea usando sus respectivos tags obtenidos de HTML
    nombre = soup.find('p', class_='tit-line__text color__line').find('span', class_='text-line').text
    estado = soup.find('div', class_='box__line-state').text
    img = soup.find('img', class_=endPoint)['src']

    #Comprobamos si existe la division de incidencias de linea
    #Si existe, el mensaje se guarda en la descripcion
    #Si no existe, se especifica que no hay incidencias
    if soup.find('div', {'id': 'line-incidents'}) is not None:
        desc = soup.find('div', {'id': 'line-incidents'}).find('div', class_='text__incidencia').text
    else:
        desc = 'No hay incidencias'

    #Formateamos cada linea obtenida en forma de diccionario para su posterior insertcion a la DB
    infoLinea = {
        'nombre' : nombre.replace('\n', ''), #Eliminamos la extra new line que existe en el parseo del nombre
        'estado' : estado.strip(), #Eliminamos los espacios innecesarios al principio y al final del estado
        'desc' : desc.strip().replace('\n', ''), #Eliminamos los espacion de comienzo y fin y quitamos la newline
        'img' : 'https://www.metromadrid.es/' + img #Concatenamos el dominio principal con el subdominio de la imagen obtenido.
    }

    #Insertamos el dato formateado en la lista auxiliar creada anteriormente
    lineasFormateadas.append(infoLinea)