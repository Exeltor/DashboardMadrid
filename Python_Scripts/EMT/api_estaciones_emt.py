#!/usr/bin/env python3
import requests, json, datetime #Importamos las librerias de requests, json y fecha

#Especificamos la URL de la API y declaramos la fecha y hora actual
url = "https://services5.arcgis.com/UxADft6QPcvFyDU1/arcgis/rest/services/M6_Red/FeatureServer/0/query?where=1%3D1&outFields=DENOMINACION,LINEAS,TIPOVIA,PARTICULA,NOMBREVIA,TIPONUMERO,NUMEROPORTAL&outSR=4326&f=json"
now = datetime.datetime.now()

#Realizamos una request GET a la URL especificada anteriormente
response = requests.get(url)

#Cargamos la request en formato JSON
requestJson = json.loads(response.text)

#Declaramos listas auxiliares para el manejo de los datos
rawData = []
formattedData = []

for sublist in requestJson['features']: #Iteramos por el JSON declarado anteriormente y guardamos los elementos en una lista
	rawData.append(sublist)

for parada in rawData: #Iteramos por cada elemento de la lista auxiliar rellenada en el paso anterior
	#Atributos
	atributosParada = parada['attributes']

	nombre = atributosParada['DENOMINACION']
	lineas = atributosParada['LINEAS']

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
		'lat' : lat,
		'lon' : lon,
		'fechaAct' : now.strftime("%Y-%m-%d %H:%M")
	}

	#Añadimos el elemento formateado a la lista auxiliar declarada anteriormente
	formattedData.append(paradaFormat)  