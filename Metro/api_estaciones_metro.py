#!/usr/bin/env python3
import requests, json, datetime

url = "https://services5.arcgis.com/UxADft6QPcvFyDU1/arcgis/rest/services/Red_Metro/FeatureServer/4/query?where=1%3D1&outFields=DENOMINACION,DIRECCION,NUMEROLINEAUSUARIO,MUNICIPIO,CORONATARIFARIA&returnGeometry=false&returnDistinctValues=true&outSR=4326&f=json"
now = datetime.datetime.now()

response = requests.get(url)

requestJson = json.loads(response.text)

rawData = []
formattedData = []

for sublist in requestJson["features"]:
    rawData.append(sublist["attributes"])
    
for estacion in rawData:
    nombre = estacion["DENOMINACION"]
    direccion = estacion["DIRECCION"]
    municipio = estacion["MUNICIPIO"]
    linea = estacion["NUMEROLINEAUSUARIO"]
    tarifa = estacion["CORONATARIFARIA"]
    
    estacion = {
        'nombre' : nombre,
        'direccion' : direccion,
        'municipio' : municipio,
        'linea/anden' : linea,
        'tarifa' : tarifa,
        'fechaHoraActualizacion' : now.strftime("%Y-%m-%d %H:%M")
    }
    
    formattedData.append(estacion)
    