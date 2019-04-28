#!/usr/bin/env python3
#Importamos las librerias necesarias de mongo y el script de la API
import pymongo
import urllib.parse
from .api_estaciones_emt import formattedData

#Funcion de conexion a MongoDB, borrado de datos anteriores e insercion de datos nuevos
def insert():
	client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
	db = client.TPA.paradasEMT

	db.delete_many({})
	db.insert_many(formattedData)