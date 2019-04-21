import pymongo
import urllib.parse
from .scraper_llegadas_aeropuerto import vuelosFormateados as llegadas
from .scraper_salidas_aeropuerto import vuelosFormateados as salidas

def insert():
	client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
	dbSalidas = client.TPA.salidasAeropuerto
	dbLlegadas = client.TPA.llegadasAeropuerto

	dbSalidas.delete_many({})
	dbLlegadas.delete_many({})

	dbSalidas.insert_many(salidas)
	dbLlegadas.insert_many(llegadas)