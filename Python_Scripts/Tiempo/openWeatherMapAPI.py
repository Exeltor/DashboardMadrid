#!/usr/bin/env python3
import requests, json #importamos las librerias de requests y json

#Definimos la apiKey y especificamos la id de la ciudad a consultar(Madrid)
apiKey = '08e1f4015006817428c7c5a12dd13f91'
idMadrid = '6359304'

#Parametros a enviar con la request json
getParams = {'id' : idMadrid, 'appid' : apiKey, 'units' : 'metric'}

#Definimos el gateway de la api
url = "http://api.openweathermap.org/data/2.5/forecast/"

#Hacemos una request GET al gateway de la api con los parametros anteriormente definidos, y guardamos la respuesta en una variable
response = requests.get(url, params = getParams)

#Cargamos el json a una variable con la libreria importada al principio
requestJson = json.loads(response.text)

#Preparamos listas auxiliares para el manejo de datos
rawData = []
formattedData = []

for sublist in requestJson['list']: #Iteramos por el json parseado para extraer elementos a la lista rawData
    rawData.append(sublist)

#Iteramos por la lista raw data para extraer los datos necesarios y formatearlos en forma de diccionario
for stats in rawData:
    
    #Conversion a Celsius
    temp = int(stats['main']['temp'])
    minTemp = int(stats['main']['temp_min'])
    maxTemp = int(stats['main']['temp_max'])
    humedad = stats['main']['humidity']
    desc = stats['weather'][0]['description']
    viento = stats['wind']['speed']
    diaHora = stats['dt_txt']
    iconId = stats['weather'][0]['icon']
    
    insert = {
        'temp' : temp,
        'minTemp' : minTemp,
        'maxTemp' : maxTemp,
        'humedad' : humedad,
        'desc' : desc,
        'viento' : viento,
        'icono' : f'http://openweathermap.org/img/w/{iconId}.png',
        'dia/hora' : diaHora
    }
    
    #Insertamos el dato formateado a la lista auxiliar creada anteriormente
    formattedData.append(insert)    