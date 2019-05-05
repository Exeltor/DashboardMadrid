#Importamos las librerias y scripts de obtencion de datos
from .metroScraper import lineasFormateadas as lineas
from .api_estaciones_metro import formattedEstaciones as estaciones
from bson import ObjectId #Importamos la libreria de formateo de datos de MongoDB, especificamente el objecto ObjectID
import urllib.parse
import pymongo

#Funcion de insercion de datos a MongoDB
def insert():
	#Iteramos por cada elemento de lineas
	for linea in lineas:
		objId = ObjectId()

		#Asignamos una ObjectID a cada linea
		linea.update(_id = objId)

		#Iteramos por cada estacion para comparar si la estacion corresponde a la linea.
		#Si corresponden, añadimos el ObjectID de la linea a la estacion para asi poder relacionar los 2 elementos
		for estacion in estaciones:
			if linea['nombre'] == estacion['linea']:
				estacion.update(_idLinea = objId)
			elif (linea['nombre'] == 'Línea 6 Circular') and (estacion['linea'] == 'Línea 6'):
				estacion.update(_idLinea = objId)
			elif (linea['nombre'] == 'Línea 12 MetroSur') and (estacion['linea'] == 'Línea 12'):
				estacion.update(_idLinea = objId)


	#Conexion a la base de datos, seleccion de las colecciones correspondientes, borrado de datos antiguos e insercion de datos nuevos.
	client = pymongo.MongoClient("mongodb+srv://Master:" + urllib.parse.quote_plus('masterP@ss') + "@tpa-whplr.mongodb.net/test?retryWrites=true")
	dbEstaciones = client.TPA.estacionesMetro
	dbLineas = client.TPA.lineasMetro

	#Funcion preventiva para no sobreescribir los datos si las APIs o pagina web estan caidas
	if lineas and estaciones:
		dbLineas.delete_many({})
		dbEstaciones.delete_many({})

		dbLineas.insert_many(lineas)
		dbEstaciones.insert_many(estaciones)