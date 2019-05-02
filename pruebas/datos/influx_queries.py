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

print(measurements)
rs = client.query('SELECT * from Temperatura limit 2')
rs = list(rs.get_points())
print(rs)
print("\n\n\n\n")
query = clean_json(rs)
print(query[0]["temperatura"])


for i in range(len(query)):
	for key, value in query[i].items():
		print (key, value)