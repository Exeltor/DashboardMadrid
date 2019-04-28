# Librerias de apertura de url y beautifulSoup para Scraping
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime #Libreria de fecha y hora

page = urlopen("https://www.aeropuertomadrid-barajas.com/salidas.html") #Abrimos la url de salidas
now = datetime.datetime.now() #Guardamos la fecha y hora actual

# Parseo del html
soup = BeautifulSoup(page, "html.parser")

# Encontramos todos los divs que contienen las tarjetas de los vuelos
vuelos = soup.find_all("div", class_ = "flightListRecord")
vuelosFormateados = []

# Iteramos por todos los vuelos para encontrar la informacion
for vuelo in vuelos:  
    
    #Buscamos la ID del vuelo mediante sus respectivos tags obtenidos de HTML
    for ids in vuelo.find_all("div", class_ = "flightListFlightIDs", limit = 1):
        for ID in ids.find_all("a", class_= "flightListFlightIDLink", limit = 1):
            ident = ID.text
    
    #Buscamos el destino del vuelo mediante sus respectivos tags obtenidos de HTML
    for destino in vuelo.find_all("div", class_= "flightListOtherAirport", limit = 1):
         hora = destino.span.text
         destino.find("span").replace_with('')
         dest = destino.text.replace(" - ","")
    
    #Buscamos el terminal del vuelo mediante sus respectivos tags obtenidos de HTML  
    for terminal in vuelo.find_all("div", class_= "flightListTerminal", limit = 1):
         term = terminal.text
       
    #Buscamos el estado del vuelo mediante sus respectivos tags obtenidos de HTML 
    for estado in vuelo.find_all("div", class_= "flightListTimeStatus", limit = 1):
        status = estado.div.text
        
    #Formateamos el vuelo en forma de diccionario
    flight = {
        'id' : ident,
        'hora' : hora,
        'destino' : dest,
        'terminal' : term,
        'estado' : status,
        'fechaComprobacion' : now.strftime("%Y-%m-%d %H:%M")
    }
        
    #Insertamos el vuelo formateado a una lista auxiliar anteriormente definida
    vuelosFormateados.append(flight)
    
    
    
    