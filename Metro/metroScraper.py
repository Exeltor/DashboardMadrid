#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen

mainDom = "https://www.metromadrid.es/es/linea/"
lineasEndPoint = ['linea-1','linea-2','linea-3','linea-4','linea-5','linea-6-circular','linea-7',
                'linea-8','linea-9','linea-10','linea-11','linea-12-metrosur','ramal','ml1','ml2','ml3']  

lineasFormateadas = [] 

for endPoint in lineasEndPoint:
    currDom = mainDom + endPoint
    page = urlopen(currDom)
    soup = BeautifulSoup(page, 'html.parser')


    nombre = soup.find('p', class_='tit-line__text color__line').find('span', class_='text-line').text
    estado = soup.find('div', class_='box__line-state').text
    img = soup.find('img', class_=endPoint)['src']

    if soup.find('div', {'id': 'line-incidents'}) is not None:
        desc = soup.find('div', {'id': 'line-incidents'}).find('div', class_='text__incidencia').text
    else:
        desc = 'No hay incidencias'

    infoLinea = {
        'nombre' : nombre.replace('\n', ''),
        'estado' : estado.strip(),
        'desc' : desc.strip().replace('\n', ''),
        'img' : 'https://www.metromadrid.es/' + img
    }

    lineasFormateadas.append(infoLinea)