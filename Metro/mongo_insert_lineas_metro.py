#!/usr/bin/env python3
import pymongo
import urllib.parse
from metroScraper import lineasFormateadas

client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
db = client.TPA.lineasMetro

db.insert_many(lineasFormateadas)