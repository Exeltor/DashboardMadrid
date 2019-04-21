#!/usr/bin/env python3
import requests, json, datetime

url = "https://services5.arcgis.com/UxADft6QPcvFyDU1/arcgis/rest/services/M5_Red/FeatureServer/0/query?where=1%3D1&outFields=LINEAS,DENOMINACION,TIPOVIA,PARTICULA,NOMBREVIA,TIPONUMERO,NUMEROPORTAL,CORONATARIFARIA&outSR=4326&f=json"
now = datetime.datetime.now()

response = requests.get(url)

requestJson = json.loads(response.text)

rawData = []
formattedData = []

for sublist in requestJson['features']:
	rawData.append(sublist)

for parada in rawData:
	#Atributos
	atributosParada = parada['attributes']

	nombre = atributosParada['DENOMINACION']
	lineas = atributosParada['LINEAS']
	tarifa = atributosParada['CORONATARIFARIA']

	#Elementos de la direccion
	tipoVia = atributosParada['TIPOVIA']
	particula = atributosParada['PARTICULA']
	nombreVia = atributosParada['NOMBREVIA']
	tipoNumero = atributosParada['TIPONUMERO']
	numeroPortal = atributosParada['NUMEROPORTAL']

	direccionElems = [tipoVia, particula, nombreVia, tipoNumero, numeroPortal]
	usableElems = []

	for elem in direccionElems:
		if elem is not None:
			usableElems.append(elem)

	direccionCompleta = ' '.join(usableElems)

	#Datos geograficos
	geometriaParada = parada['geometry']

	lat = geometriaParada['y']
	lon = geometriaParada['x']

	#Formateo de los datos en forma de diccionario
	paradaFormat = {
		'nombre' : nombre,
		'direccion' : direccionCompleta,
		'lineas' : lineas,
		'tarifa' : tarifa,
		'lat' : lat,
		'lon' : lon,
		'fechaAct' : now.strftime("%Y-%m-%d %H:%M")
	}

	formattedData.append(paradaFormat)  