# Librerias
from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen("https://www.aeropuertomadrid-barajas.com/llegadas.html")

# Parseo del html
soup = BeautifulSoup(page, "html.parser")

# Encontramos todos los divs que contienen las tarjetas de los vuelos
vuelos = soup.find_all("div", class_ = "flightListRecord")

# Iteramos por todos los vuelos para imprimir la informacion
for vuelo in vuelos:
    infoVuelo = ""
    
    for origen in vuelo.find_all("div", class_= "flightListOtherAirport"):
        infoVuelo += origen.text + origen.span.text + ", "
        
    for terminal in vuelo.find_all("div", class_= "flightListTerminal"):
        infoVuelo += terminal.text + ", "
        
    for estado in vuelo.find_all("div", class_= "flightListTimeStatus"):
        infoVuelo += estado.text
        
    print(infoVuelo)
