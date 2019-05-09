#Importamos la librerias necesarias y las lista generada del script API
import pymongo
import urllib.parse
from .bicimadAPI import estaciones


#Funcion que efectua la conexion a la coleccion apropiada de MongoDB
def insert():
    client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
    db = client.TPA.bicimad

    #Borrado de datos viejos e insercion de datos nuevos.
    #Funcion preventiva para no sobreescribir los datos si la API esta caida
    if estaciones:
        db.delete_many({})
        db.insert_many(estaciones)