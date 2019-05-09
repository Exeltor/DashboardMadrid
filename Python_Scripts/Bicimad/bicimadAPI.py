import requests, json, urllib, datetime
    
user = 'calvocalvoantonio@hotmail.com' 
password = '591785E3-8913-491A-ACDE-84E5F64B2E75'
now = datetime.datetime.now()

with urllib.request.urlopen(f"https://rbdata.emtmadrid.es:8443/BiciMad/get_stations/WEB.SERV.{user}/{password}") as bicimadAPI: 
    data = json.loads(bicimadAPI.read().decode())

jsonData = json.loads(data['data']) 
estaciones = [] 
for st in jsonData['stations']:
    bcm = {} 
    bcm['lat'] = st['latitude']
    bcm['lon'] = st['longitude']
    bcm['nombre'] = st['name']
    bcm['direccion'] = st['address']
    bcm['bases'] = st['total_bases']
    bcm['ancladas'] = st['dock_bikes']
    bcm['vacias'] = st['free_bases']
    bcm['operativo'] = 'No' if st['no_available'] == 1 else 'Si'
    bcm['fechaAct'] = now.strftime("%Y-%m-%d %H:%M")

    estaciones.append(bcm)