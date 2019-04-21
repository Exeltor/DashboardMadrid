from Aeropuerto import mongo_insert_llegadas_salidas as aero
from EMT import mongo_insert_paradas_emt as emt
from Tiempo import insert_tiempo_mongo as tiempo
from Metro import api_scraper_unifier as metro
from Cercanias import mongo_insert_paradas_cercanias as cercanias

def insertAll():
	aero.insert()
	emt.insert()
	tiempo.insert()
	metro.insert()
	cercanias.insert()


if __name__ == '__main__':
	insertAll()