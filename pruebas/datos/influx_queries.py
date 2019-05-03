from influxdb import InfluxDBClient
import json

def clean_json(list_json):
	for i in range (len(list_json)):
		x = json.dumps(list_json[0])
		x = json.loads(x)
	return list_json

client = InfluxDBClient(host='127.0.0.1', port=8086, database='pfprueba')
client.switch_database('pfprueba')
measurements = client.get_list_measurements()

#print(measurements)
rs = client.query('SELECT * from Temperatura limit 2')
rs = list(rs.get_points())
#print(rs)
#print("\n\n\n\n")
query = clean_json(rs)
#print(query[0]["temperatura"])


for i in range(len(query)):
	for key, value in query[i].items():
		print (key, value)

print("Time")
print(query[0]["time"])

print("Query")
estados = client.query('show tag values on "pfprueba" from "Temperatura" with key="estado"')
estados = list(estados.get_points())
estados = clean_json(estados)
#print(estados[0]["value"])

ciudad = client.query('show tag values on "pfprueba" from "Temperatura" with key="ciudad"')
ciudad = list(ciudad.get_points())
ciudad = clean_json(ciudad)
#print(ciudad[0]["value"])

get_time_ciudadstr="select "+'"clima"'+" from Clima where ciudad='Acambaro' and time='2019-01-01T01:00:00Z'"
get_time_ciudad = client.query(get_time_ciudadstr)
get_time_ciudad = list(get_time_ciudad.get_points())
get_time_ciudad = clean_json(get_time_ciudad)
print(get_time_ciudad[0]["clima"])

get_time_estado_str="select "+'"clima"'+" from Clima where estado='CDMX' and time='2019-01-01T01:00:00Z'"
get_time_estado = client.query(get_time_estado_str)
get_time_estado = list(get_time_estado.get_points())
get_time_estado = clean_json(get_time_estado)
print(get_time_estado[0]["clima"])
