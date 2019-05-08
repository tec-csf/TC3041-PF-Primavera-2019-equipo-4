from pymongo import MongoClient
from influxdb import InfluxDBClient
from bson.son import SON
import json

class API(object):
	#Mongo configuration
	mongo_uri = "mongodb+srv://demo:1234@cluster0-26vpf.gcp.mongodb.net/test?retryWrites=true"
	client = MongoClient(mongo_uri)
	db = client.atractions
	collectionData = db.places

	#Influxdb configuration
	client = InfluxDBClient(host='influxdb', port=8086, database='pfprueba')
	client.switch_database('pfprueba')

	#Clean influxdb queries output
	def clean_json(self, list_json):
		for i in range (len(list_json)):
			x = json.dumps(list_json[0])
			x = json.loads(x)
		return list_json

	#Convert form date format into influxdb date format
	def clean_time(self, date, hour):
		hour = self.clean_hour(hour)
		time_str = date+"T"+hour+":00Z"
		return time_str

	def clean_hour(self, hour):
		newhour = hour[0] + hour[1] + hour[2] + "00"
		return newhour	

	def getStates(self):
		#Query3: Get all states (from influx)
		states = self.client.query('show tag values on "pfprueba" from "Temperatura" with key="estado"')
		states = list(states.get_points())
		states = self.clean_json(states)

		listStates = []
		for i in range(len(states)):
			listStates.append(states[i]['value'])

		return listStates

	def getCities(self, state):
		cities = self.client.query('show tag values on "pfprueba" from "Temperatura" with key="ciudad" where "estado"=' + "'" + state + "'")
		cities = list(cities.get_points())
		cities = self.clean_json(cities)

		listCities = []
		for i in range(len(cities)):
			listCities.append(cities[i]['value'])

		return listCities


	def getClimaFromCiudad(self, ciudad, date):
		get_time_ciudadstr="select "+'"clima"'+" from Clima where ciudad='" + ciudad + "' and time='" + date + "'"
		get_time_ciudad = self.client.query(get_time_ciudadstr)
		get_time_ciudad = list(get_time_ciudad.get_points())
		get_time_ciudad = self.clean_json(get_time_ciudad)

		return get_time_ciudad

	def getClimaFromEstado(self, estado, date):
		get_time_estado_str="select "+'"clima"'+" from Clima where estado='" + estado + "' and time='" + date + "'"
		get_time_estado = self.client.query(get_time_estado_str)
		get_time_estado = list(get_time_estado.get_points())
		get_time_estado = self.clean_json(get_time_estado)

		return get_time_estado

	def queryAtractionsBasedOnClimate(self, climate, city):
		pipe = [{"$match":{climate:1, "ciudad":city}},{"$project":{"_id":0, "nombre":1, "ciudad":1, "direccion":1, "nivel de precios":1, "tipo":1, "path_imagen":1}}]
		cursor = self.collectionData.aggregate(pipe)
		suitableAtractions = list(cursor)

		return suitableAtractions