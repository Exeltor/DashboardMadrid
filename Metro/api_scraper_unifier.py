from metroScraper import lineasFormateadas as lineas
from api_estaciones_metro import formattedEstaciones as estaciones
from bson import ObjectId
import urllib.parse
import pymongo

for linea in lineas:
	objId = ObjectId()

	linea.update(_id = objId)

	for estacion in estaciones:
		if linea['nombre'].startswith(estacion['linea']):
			estacion.update(_idLinea = objId)

client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
dbEstaciones = client.TPA.estacionesMetro
dbLineas = client.TPA.lineasMetro

dbLineas.insert_many(lineas)
dbEstaciones.insert_many(estaciones)