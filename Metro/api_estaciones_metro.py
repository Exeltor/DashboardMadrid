#!/usr/bin/env python3
import requests, json, datetime

apiEstaciones = 'https://services5.arcgis.com/UxADft6QPcvFyDU1/arcgis/rest/services/Red_Metro/FeatureServer/0/query?where=1%3D1&outFields=CORONATARIFARIA,DENOMINACION,CODIGOESTACION,TIPOVIA,PARTICULA,NOMBREVIA,TIPONUMERO,NUMEROPORTAL&outSR=4326&f=json'
apiParadas = 'https://services5.arcgis.com/UxADft6QPcvFyDU1/arcgis/rest/services/Red_Metro/FeatureServer/5/query?where=1%3D1&outFields=CODIGOESTACION,NUMEROLINEAUSUARIO&returnGeometry=false&returnDistinctValues=true&outSR=4326&f=json'

def fillRawInfo(apiJson):
    rawList = []
    for sublist in apiJson['features']:
        rawList.append(sublist)

    return rawList


def listEstaciones():
    estList = []

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

        direccionElems = [tipoVia, particula, nombreVia, tipoNumero, numeroPortal]
        usableElems = []

        for elem in direccionElems:
            if elem is not None:
                usableElems.append(elem)

        direccionCompleta = ' '.join(usableElems)

        #Datos geograficos
        geometriaEstacion = estacion['geometry']

        lat = geometriaEstacion['y']
        lon = geometriaEstacion['x']

        estacion = {
            'nombre' : nombre,
            'direccion' : direccionCompleta,
            'lat' : lat,
            'lon' : lon,
            'tarifa' : tarifa,
            'codEstacion' : codEstacion
        }

        estList.append(estacion)

    return estList

def listParadas():
    paradasList = []

    for parada in rawDataParadas:
        atributosParada = parada['attributes']

        codEstacion = atributosParada['CODIGOESTACION']
        linea = atributosParada['NUMEROLINEAUSUARIO']

        lineaFormat = ''.join([n for n in linea[0:2] if n.isdigit()])

        parada = {
            'codEstacion' : codEstacion,
            'linea' : 'Línea ' + lineaFormat
        }

        paradasList.append(parada)

    return paradasList

def agreggate():
    for estacion in formattedEstaciones:
        codEstacion = estacion['codEstacion']

        for parada in formattedParadas:
            if parada['codEstacion'] == codEstacion:
                estacion.update(linea = parada['linea'])


responseEstaciones = requests.get(apiEstaciones)
responseParadas = requests.get(apiParadas)

estacionesJson = json.loads(responseEstaciones.text)
paradasJson = json.loads(responseParadas.text)

rawDataEstaciones = fillRawInfo(estacionesJson)
rawDataParadas = fillRawInfo(paradasJson)
formattedEstaciones = listEstaciones()
formattedParadas = listParadas()
agreggate()