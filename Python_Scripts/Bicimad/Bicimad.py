
import requests #importamos libreria de peticiones
import urllib.request
import time #importamos modulo que nos permitirá jugar con fechas y horas
from bs4 import BeautifulSoup #importamos la librería con la cual vamos a poder "coger" el html de la web
url = ‘https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/'
response = requests.get(url)

soup = BeautifulSoup(response.text, “html.parser”)
soup.findAll('x') #buscamos todos los tags a esto nos devuelve todos los datos que contengan el tag a , ahora lo que tendremos que hacer sera filtrarlo y separarlo

#actualmente el servidor Bicimad se encuentra caido por eso no puedo continuar codigo con los tags.
#quedamos a la espera de que restablezcan el server





print (datosBicimad)#variable ultima final con el obejtivo de que me muestre los datos recopilados por pantalla







