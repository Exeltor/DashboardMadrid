#Importamos los scripts de los diferentes servicios de sus correspondientes Packages
from Aeropuerto import mongo_insert_llegadas_salidas as aero
from EMT import mongo_insert_paradas_emt as emt
from Tiempo import insert_tiempo_mongo as tiempo
from Metro import api_scraper_unifier as metro
from Cercanias import mongo_insert_paradas_cercanias as cercanias

#Funcion para ejecutar todas las funciones de los modulos importados anteriormente.
def insertAll():
	aero.insert()
	emt.insert()
	tiempo.insert()
	metro.insert()
	cercanias.insert()

#Comprobamos si este script ha sido ejecutado como principal, y no importado como un modulo.
if __name__ == '__main__':
	insertAll()