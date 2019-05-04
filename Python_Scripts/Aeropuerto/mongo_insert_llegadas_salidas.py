#Importamos las librerias de mongo, y las listas auxiliares de los Scrapers de llegadas y salidas
import pymongo
import urllib.parse
from .flightstats_API import getArrivals, getDepartures

#Funcion para la conexion a MongoDB, seleccion de las colecciones correspondientes, borrado de datos antiguos e insercion de datos nuevos
def insert():
	client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
	dbSalidas = client.TPA.salidasAeropuerto
	dbLlegadas = client.TPA.llegadasAeropuerto

	salidas = getDepartures()
	llegadas = getArrivals()

	if salidas:
		dbSalidas.delete_many({})
		dbSalidas.insert_many(salidas)

	if llegadas:
		dbLlegadas.delete_many({})
		dbLlegadas.insert_many(llegadas)