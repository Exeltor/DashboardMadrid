from .metroScraper import lineasFormateadas as lineas
from .api_estaciones_metro import formattedEstaciones as estaciones
from bson import ObjectId
import urllib.parse
import pymongo

def insert():
	for linea in lineas:
		objId = ObjectId()

		linea.update(_id = objId)

		for estacion in estaciones:
			if linea['nombre'] == estacion['linea']:
				estacion.update(_idLinea = objId)
			elif (linea['nombre'] == 'Línea 6 Circular') and (estacion['linea'] == 'Línea 6'):
				estacion.update(_idLinea = objId)
			elif (linea['nombre'] == 'Línea 12 MetroSur') and (estacion['linea'] == 'Línea 12'):
				estacion.update(_idLinea = objId)


	client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
	dbEstaciones = client.TPA.estacionesMetro
	dbLineas = client.TPA.lineasMetro

	dbLineas.delete_many({})
	dbEstaciones.delete_many({})

	dbLineas.insert_many(lineas)
	dbEstaciones.insert_many(estaciones)