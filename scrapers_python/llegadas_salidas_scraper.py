# Librerias
from urllib.request import urlopen
from bs4 import BeautifulSoup

paginaLlegadas = urlopen("https://www.aeropuertomadrid-barajas.com/llegadas.html")
paginaSalidas = urlopen("https://www.aeropuertomadrid-barajas.com/salidas.html")

def leerLlegadas():
    # Parseo del html
    soup = BeautifulSoup(paginaLlegadas, "html.parser")

    # Encontramos todos los divs que contienen las tarjetas de los vuelos
    vuelos = soup.find_all("div", class_ = "flightListRecord")

    # Iteramos por todos los vuelos para imprimir la informacion
    print("Llegadas")
    for vuelo in vuelos:
        infoVuelo = ""
    
        for origen in vuelo.find_all("div", class_= "flightListOtherAirport"):
            infoVuelo += origen.text + origen.span.text + ", "
        
        for terminal in vuelo.find_all("div", class_= "flightListTerminal"):
            infoVuelo += terminal.text + ", "
        
        for estado in vuelo.find_all("div", class_= "flightListTimeStatus"):
            infoVuelo += estado.text
        
        print(infoVuelo)
    
    
def leerSalidas():
    # Parseo del html
    soup = BeautifulSoup(paginaSalidas, "html.parser")

    # Encontramos todos los divs que contienen las tarjetas de los vuelos
    vuelos = soup.find_all("div", class_ = "flightListRecord")

    # Iteramos por todos los vuelos para imprimir la informacion
    print("Salidas")
    for vuelo in vuelos:
        infoVuelo = ""
    
        for destino in vuelo.find_all("div", class_= "flightListOtherAirport"):
            infoVuelo += destino.text + ", "
        
        for terminal in vuelo.find_all("div", class_= "flightListTerminal"):
            infoVuelo += terminal.text + ", "
        
        for estado in vuelo.find_all("div", class_= "flightListTimeStatus"):
            infoVuelo += estado.div.text
        
        print(infoVuelo)
        
        
leerLlegadas()
leerSalidas()
    