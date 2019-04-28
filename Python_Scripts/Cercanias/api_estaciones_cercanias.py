#!/usr/bin/env python3
import requests, json, datetime #Importamos las librerias de requests, json y fecha

#Especificamos los links de las APIs a usar
url = "https://services5.arcgis.com/UxADft6QPcvFyDU1/arcgis/rest/services/M5_Red/FeatureServer/0/query?where=1%3D1&outFields=LINEAS,DENOMINACION,TIPOVIA,PARTICULA,NOMBREVIA,TIPONUMERO,NUMEROPORTAL,CORONATARIFARIA&outSR=4326&f=json"
now = datetime.datetime.now() #Guardamos la fecha y hora actual

#Realizamos una request GET a la URL especificada, y guardamos el response
response = requests.get(url)

#Formateamos la response a JSON
requestJson = json.loads(response.text)

#Declaramos listas auxiliares para el manejo de los datos
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

	direccionElems = [tipoVia, particula, nombreVia, tipoNumero, numeroPortal] #Declaracion de elementos de direccion
	usableElems = []

	#Rellenamos una lista auxiliar unicamente con los elementos de la direccion que existan, asi evitando excepciones.
	for elem in direccionElems:
		if elem is not None:
			usableElems.append(elem)

	#Concatenamos la lista auxiliar generada anteriormente con un espacio de separacion.
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

	#Añadimos la estacion formateada a una lista auxiliar
	formattedData.append(paradaFormat)  