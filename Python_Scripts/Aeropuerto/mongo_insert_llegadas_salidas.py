#Importamos las librerias de mongo, y las listas auxiliares de los Scrapers de llegadas y salidas
import pymongo
import urllib.parse
from .scraper_llegadas_aeropuerto import vuelosFormateados as llegadas
from .scraper_salidas_aeropuerto import vuelosFormateados as salidas

#Funcion para la conexion a MongoDB, seleccion de las colecciones correspondientes, borrado de datos antiguos e insercion de datos nuevos
def insert():
	client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
	dbSalidas = client.TPA.salidasAeropuerto
	dbLlegadas = client.TPA.llegadasAeropuerto

	dbSalidas.delete_many({})
	dbLlegadas.delete_many({})

	dbSalidas.insert_many(salidas)
	dbLlegadas.insert_many(llegadas)