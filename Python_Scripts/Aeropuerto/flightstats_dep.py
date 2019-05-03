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
	'numHours': 1
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

	return json.loads(reponse.text)

#Si isDeparture = True, recogemos las salidas, si no, las llegadas
def getData(isDeparture):
	for flight in requestToJson(domainDep, getParams)['flightStatuses']:
		flightId = flight['carrierFsCode'] + flight['flightNumber']
		otherFs = flight['arrivalAirportFsCode'] if isDeparture else flight['departureAirportFsCode']
		status = statusDict[flight['status']]
		terminal = flight['airportResources']

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

		#TODO terminal y formateo diccionario
		flightF = {
			'id' : flightId,
			'aerolinea' : airlineName,
			'destino' if isDeparture else 'origen' : otherName,
			'estado': status,
			'horaSalida' : time
		}

		formattedList.append(flightF)
