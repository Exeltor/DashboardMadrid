#!/usr/bin/env python3
import requests, json, datetime #Importamos las librerias de requests, json y fecha.

#Especificamos los links de las APIs a usar
apiEstaciones = 'https://services5.arcgis.com/UxADft6QPcvFyDU1/arcgis/rest/services/Red_Metro/FeatureServer/0/query?where=1%3D1&outFields=CORONATARIFARIA,DENOMINACION,CODIGOESTACION,TIPOVIA,PARTICULA,NOMBREVIA,TIPONUMERO,NUMEROPORTAL&outSR=4326&f=json'
apiParadas = 'https://services5.arcgis.com/UxADft6QPcvFyDU1/arcgis/rest/services/Red_Metro/FeatureServer/5/query?where=1%3D1&outFields=CODIGOESTACION,NUMEROLINEAUSUARIO&returnGeometry=false&returnDistinctValues=true&outSR=4326&f=json'

#Funcion para parsear el json devuelto por una API, e insercion de los datos a una lista auxiliar
def fillRawInfo(apiJson):
    rawList = []
    for sublist in apiJson['features']:
        rawList.append(sublist)

    return rawList


#Funcion para el formateo de datos de la API de estaciones
def listEstaciones():
    estList = [] #Lista auxiliar para el guardado de datos formateados

    #Iteramos por la lista de estaciones para extraer los datos necesarios y formatearlos
    for estacion in rawDataEstaciones:
        atributosEstacion = estacion['attributes']

        nombre = atributosEstacion['DENOMINACION']
        codEstacion = atributosEstacion['CODIGOESTACION']
        tarifa = atributosEstacion['CORONATARIFARIA']

        #Elementos de la direccion
        tipoVia = atributosEstacion['TIPOVIA']
        particula = atributosEstacion['PARTICULA']
        nombreVia = atributosEstacion['NOMBREVIA']
        tipoNumero = atributosEstacion['TIPONUMERO']
        numeroPortal = atributosEstacion['NUMEROPORTAL']

        direccionElems = [tipoVia, particula, nombreVia, tipoNumero, numeroPortal] #Declaracion de elementos de direccion
        usableElems = []

        #Rellenamos una lista auxiliar unicamente con los elementos de la direccion que existan, asi evitando excepciones.
        for elem in direccionElems:
            if elem is not None:
                usableElems.append(elem)

        #Concatenamos la lista auxiliar generada anteriormente con un espacio de separacion.
        direccionCompleta = ' '.join(usableElems)

        #Datos geograficos
        geometriaEstacion = estacion['geometry']

        lat = geometriaEstacion['y']
        lon = geometriaEstacion['x']

        #Formateamos cada estacion en forma de diccionario para su posterior insercion a la BD
        estacion = {
            'nombre' : nombre,
            'direccion' : direccionCompleta,
            'lat' : lat,
            'lon' : lon,
            'tarifa' : tarifa,
            'codEstacion' : codEstacion
        }

        #Añadimos la estacion formateada a una lista auxiliar
        estList.append(estacion)

    return estList

#Funcion para el formateo de los datos de la API de paradas
def listParadas():
    paradasList = []

    #Iteramos por la lista de estaciones para extraer los datos necesarios y formatearlos
    for parada in rawDataParadas:
        atributosParada = parada['attributes']

        codEstacion = atributosParada['CODIGOESTACION']
        linea = atributosParada['NUMEROLINEAUSUARIO']

        lineaFormat = ''.join([n for n in linea[0:2] if n.isdigit()])

        #Formateamos cada estacion en forma de diccionario para su posterior insercion a la BD
        parada = {
            'codEstacion' : codEstacion,
            'linea' : 'Línea ' + lineaFormat
        }

        #Añadimos la estacion formateada a una lista auxiliar
        paradasList.append(parada)

    return paradasList

#Funcion de agregacion entre dos listas de datos para combinar estaciones y lineas a las que corresponden
def agreggate():
    for estacion in formattedEstaciones:
        codEstacion = estacion['codEstacion']

        for parada in formattedParadas:
            if parada['codEstacion'] == codEstacion:
                estacion.update(linea = parada['linea'])


#Orden de ejecucion de las funciones
responseEstaciones = requests.get(apiEstaciones)
responseParadas = requests.get(apiParadas)

estacionesJson = json.loads(responseEstaciones.text)
paradasJson = json.loads(responseParadas.text)

rawDataEstaciones = fillRawInfo(estacionesJson)
rawDataParadas = fillRawInfo(paradasJson)
formattedEstaciones = listEstaciones()
formattedParadas = listParadas()
agreggate()