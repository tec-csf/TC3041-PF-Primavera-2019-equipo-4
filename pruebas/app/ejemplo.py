from influxdb import InfluxDBClient
from pymongo import MongoClient
from bson.son import SON
import json

#Mongo configuration
mongo_uri = "mongodb://mongo-router:27017"
client = MongoClient(mongo_uri)
db = client.atractions
collectionData = db.places

#Influxdb configuration
client = InfluxDBClient(host='influxdb', port=8086, database='pfprueba')
client.switch_database('pfprueba')

def getClimaFromCiudad(ciudad, date):
	get_time_ciudadstr="select "+'"clima"'+" from Clima where ciudad='" + ciudad + "' and time='" + date + "'"
	get_time_ciudad = client.query(get_time_ciudadstr)
	get_time_ciudad = list(get_time_ciudad.get_points())
	get_time_ciudad = clean_json(get_time_ciudad)

	return get_time_ciudad

def clean_time(date, hour):
	hour = clean_hour(hour)
	time_str = date+"T"+hour+":00Z"
	return time_str

def clean_hour(hour):
	newhour = hour[0] + hour[1] + hour[2] + "00"
	return newhour	

newdate = clean_time("2019-05-08", "14:02")
clima = getClimaFromCiudad("Guadalajara", newdate)
print(clima)