#Hacer directorio para datos locales
#cambiarse a ese directorio

#Iniciar contenedor con influx
docker run --name influxdb -d -p 8086:8086 -v $PWD:/var/lib/influxdb influxdb

#Copiar archivos de datos al contenedor
docker cp influx_data.txt influxdb:/

#Ejecutar influxdb en terminal
docker exec -it influxdb bash

#Importar archivo a influx
influx -import -path=data.txt -precision=s

#Meterse a la db
influx

#Meterse a la db imprimiendo las fechas de una forma entendible
influx -precision rfc3339