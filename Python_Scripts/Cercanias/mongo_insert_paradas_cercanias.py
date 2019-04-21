#!/usr/bin/env python3
import pymongo
import urllib.parse
from .api_estaciones_cercanias import formattedData

def insert():
	client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
	db = client.TPA.paradasCercanias

	db.delete_many({})
	db.insert_many(formattedData)