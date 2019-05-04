import requests, json, datetime

#Formateo del GET
appID = '041718fe'
appKey = 'e59974c8cfedf8945fecc291da4e04ab'
airportID = 'MAD'
restProtocol = 'rest'
frmt = 'json'

#Today
now = datetime.datetime.now()

#Currdate
year = now.year
month = now.month
day = now.day
hour = now.hour


getParams = {
	'appId' : appID, 
	'appKey' : appKey,
	'utc': False,
	'numHours': 3
}

domainDep = f'https://api.flightstats.com/flex/flightstatus/{restProtocol}/v2/{frmt}/airport/status/{airportID}/dep/{year}/{month}/{day}/{hour}'
domainArr = f'https://api.flightstats.com/flex/flightstatus/{restProtocol}/v2/{frmt}/airport/status/{airportID}/arr/{year}/{month}/{day}/{hour}'

#Tipos de estado de vuelo
statusDict = {
	'A' : 'Activo',
	'C' : 'Cancelado',
	'S' : 'Programado',
	'L' : 'Aterrizado',
	'D' : 'Desviado',
	'NO' : 'No Operativo',
	'U' : 'Desconocido',
	'DN' : 'Requiere fuente de informacion',
	'R' : 'Redirigido'
}

def requestToJson(URl, getReqParams):
	response = requests.get(URl, params = getReqParams)

	return json.loads(response.text)

#Si isDeparture = True, recogemos las salidas, si no, las llegadas
def getData(isDeparture):
	flightList = []

	requestJson = requestToJson(domainDep if isDeparture else domainArr, getParams)

	for flight in requestJson['flightStatuses']:
		flightId = flight['carrierFsCode'] + flight['flightNumber']
		otherFs = flight['arrivalAirportFsCode'] if isDeparture else flight['departureAirportFsCode']
		status = statusDict[flight['status']]

		#Extraccion de hora de salida/llegada
		depDateTime = flight['departureDate']['dateLocal'] if isDeparture else flight['arrivalDate']['dateLocal']
		time = depDateTime[depDateTime.index('T') + 1:]

		#Busqueda de nombre de Aerolinea por codigo FS
		for airline in requestJson['appendix']['airlines']:
			if airline['fs'] == flight['carrierFsCode']:
				airlineName = airline['name']

		#Busqueda nombre aeropuerto por codigo FS
		for airport in requestJson['appendix']['airports']:
			if airport['fs'] == otherFs:
					otherName = airport['name']

		#Asignacion de terminal
		try:
			terminal = flight['airportResources']['departureTerminal'] if isDeparture else flight['airportResources']['arrivalTerminal']
		except KeyError:
			terminal = 'Desconocido'


		flightF = {
			'id' : flightId,
			'aerolinea' : airlineName,
			'destino' if isDeparture else 'origen' : otherName,
			'estado': status,
			'terminal' : terminal,
			'horaSalida' if isDeparture else 'horaLlegada' : time
		}

		flightList.append(flightF)

	return flightList


def getDepartures():
	return getData(True)

def getArrivals():
	return getData(False)