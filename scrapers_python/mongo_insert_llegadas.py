import pymongo
import urllib.parse
from scraper_llegadas_aeropuerto import vuelosFormateados


client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
db = client.TPA.llegadasAeropuerto

db.insert_many(vuelosFormateados)