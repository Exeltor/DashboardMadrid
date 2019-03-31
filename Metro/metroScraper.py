#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen("https://www.metromadrid.es/es")

soup = BeautifulSoup(page, "html.parser")

lineasLi = soup.find_all("li", class_="list__lineas__element")
lineasFormateadas = []

for linea in lineasLi:
    if linea.find("span") is not None: 
        nombreLinea = ''.join(linea.find("img").get("class"))
        status = ''.join(linea.find("span").get("class")).replace('state--', '')
        desc = ""
        
        if status == "top":
            desc = linea.find("span").get("title")
            status = ''.join(linea.find("span").find("span").get("class")).replace("state--", " ")
    
        infoLinea = {
                'nombre' : nombreLinea,
                'estado' : status,
                'desc' : desc
        }
        
        lineasFormateadas.append(infoLinea)
        