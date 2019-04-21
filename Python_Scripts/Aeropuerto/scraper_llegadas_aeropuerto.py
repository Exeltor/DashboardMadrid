# Librerias
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

page = urlopen("https://www.aeropuertomadrid-barajas.com/llegadas.html")
now = datetime.datetime.now()

# Parseo del html
soup = BeautifulSoup(page, "html.parser")

# Encontramos todos los divs que contienen las tarjetas de los vuelos
vuelos = soup.find_all("div", class_ = "flightListRecord")
vuelosFormateados = []

# Iteramos por todos los vuelos para imprimir la informacion
for vuelo in vuelos:  
    
    for ids in vuelo.find_all("div", class_ = "flightListFlightIDs", limit = 1):
        for ID in ids.find_all("a", class_= "flightListFlightIDLink", limit = 1):
            ident = ID.text
    
    for origen in vuelo.find_all("div", class_= "flightListOtherAirport", limit = 1):
         hora = origen.span.text
         origen.find("span").replace_with('')
         orig = origen.text.replace(" - ","")
        
    for terminal in vuelo.find_all("div", class_= "flightListTerminal", limit = 1):
         term = terminal.text
        
    for estado in vuelo.find_all("div", class_= "flightListTimeStatus", limit = 1):
        status = estado.div.text
        
    flight = {
        'id' : ident,
        'hora' : hora,
        'origen' : orig,
        'terminal' : term,
        'estado' : status,
        'fechaComprobacion' : now.strftime("%Y-%m-%d %H:%M")
    }
        
    vuelosFormateados.append(flight)
