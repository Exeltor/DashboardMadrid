#Importamos la librerias necesarias y las lista generada del script API
import pymongo
import urllib.parse
from .openWeatherMapAPI import formattedData


#Funcion que efectua la conexion a la coleccion apropiada de MongoDB
def insert():
	client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
	db = client.TPA.tiempoPorHora

	#Borrado de datos viejos e insercion de datos nuevos.
	db.delete_many({})
	db.insert_many(formattedData)