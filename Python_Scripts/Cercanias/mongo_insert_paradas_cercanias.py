#!/usr/bin/env python3
#Importamos las librerias de mongo y el la lista generada por el script de la API
import pymongo
import urllib.parse
from .api_estaciones_cercanias import formattedData

#Funciond de conexion a MongoDB, seleccion de la coleccion correspondiente, borrado de datos anteriores e insercion de nuevos
def insert():
	client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
	db = client.TPA.paradasCercanias

	#Funcion preventiva para no sobreescribir los datos existentes si la API esta caida
	if formattedData:
		db.delete_many({})
		db.insert_many(formattedData)