import pymongo
import urllib.parse
from .openWeatherMapAPI import formattedData


def insert():
	client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
	db = client.TPA.tiempoPorHora

	db.delete_many({})
	db.insert_many(formattedData)