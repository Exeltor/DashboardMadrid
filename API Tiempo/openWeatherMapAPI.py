#!/usr/bin/env python3
import requests, json

apiKey = '08e1f4015006817428c7c5a12dd13f91'
idMadrid = '6359304'

url = "http://api.openweathermap.org/data/2.5/forecast?id="+idMadrid+"&APPID=" + apiKey


headers = {
    'cache-control': "no-cache"
}

response = requests.get(url)

requestJson = json.loads(response.text)
rawData = []
formattedData = []

for sublist in requestJson['list']:
    rawData.append(sublist)
    
for stats in rawData:
    
    #Conversion a Celsius
    temp = int(stats['main']['temp']) - 273.15
    minTemp = int(stats['main']['temp_min']) - 273.15
    maxTemp = int(stats['main']['temp_max']) - 273.15
    humedad = stats['main']['humidity']
    desc = stats['weather'][0]['description']
    viento = stats['wind']['speed']
    diaHora = stats['dt_txt']
    
    insert = {
        'temp' : temp,
        'minTemp' : minTemp,
        'maxTemp' : maxTemp,
        'humedad' : humedad,
        'desc' : desc,
        'viento' : viento,
        'dia/hora' : diaHora
    }
    
    formattedData.append(insert)
    
    

    
    
    




