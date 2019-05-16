# DashboardMadrid https://www.madrid-dashboard.com/
Dashboard informativa para Madrid


# Deployment del servidor Node
El deployment se hace en otro repositorio aparte. Todos los cambios finales son sincronizados con ese repositorio y subidos
a la plataforma para su build y deployment.

# Periodicidad de actualizacion de la base de datos
Los siguientes elementos son actualizados cada **5 minutos**:
* Aeropuerto -- Llegadas, Salidas
* EMT
* Metro
* Tiempo
* Cercanias

La API de Uber tiene un funcionamiento **a demanda**, por tanto, no esta implementado **de momento** y tiene que ser implementado en la web

# ¿Cuales son los modulos necesarios para ejecutar los elementos de forma local?
Todos los modulos necesarios de Python vienen se instalan en batch con el siguiente comando: \
**pip install -r path/requirements.txt** \
Este archivo se encuentra en la carpeta principal del proyecto. Recomiendo hacer uso de un VirtualEnv, pero no es necesario.

# Cosas interesantes

## Mongo API private key
e0e11ec0-baa6-425e-ab54-fc920a171f3c

## Formato request de icono API tiempo
http://openweathermap.org/img/w/<id_icono_aqui>.png
