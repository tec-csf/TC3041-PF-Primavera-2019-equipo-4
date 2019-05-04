from flask import request, url_for, jsonify, render_template
from flask_api import FlaskAPI, status, exceptions
from pymongo import MongoClient
from influxdb import InfluxDBClient
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

#options
state="state"
newdate="date"
date="date"
time="time"
state="state"
listCities="list"

#Clean influxdb queries output
def clean_json(list_json):
	for i in range (len(list_json)):
		x = json.dumps(list_json[0])
		x = json.loads(x)
	return list_json

#Convert form date format into influxdb date format
def clean_time(date, hour):
	hour = clean_hour(hour)
	time_str = date+"T"+hour+":00Z"
	return time_str

def clean_hour(hour):
	newhour = hour[0] + hour[1] + hour[2] + "00"
	return newhour	

def getStates():
	#Query3: Get all states (from influx)
	states = client.query('show tag values on "pfprueba" from "Temperatura" with key="estado"')
	states = list(states.get_points())
	states = clean_json(states)

	listStates = []
	for i in range(len(states)):
		listStates.append(states[i]['value'])

	return listStates

def getCities(state):
	cities = client.query('show tag values on "pfprueba" from "Temperatura" with key="ciudad" where "estado"=' + "'" + state + "'")
	cities = list(cities.get_points())
	cities = clean_json(cities)

	listCities = []
	for i in range(len(cities)):
		listCities.append(cities[i]['value'])

	return listCities


def getClimaFromCiudad(ciudad, date):
	get_time_ciudadstr="select "+'"clima"'+" from Clima where ciudad='" + ciudad + "' and time='" + date + "'"
	get_time_ciudad = client.query(get_time_ciudadstr)
	get_time_ciudad = list(get_time_ciudad.get_points())
	get_time_ciudad = clean_json(get_time_ciudad)

	return get_time_ciudad

def getClimaFromEstado(estado, date):
	get_time_estado_str="select "+'"clima"'+" from Clima where estado='" + estado + "' and time='" + date + "'"
	get_time_estado = client.query(get_time_estado_str)
	get_time_estado = list(get_time_estado.get_points())
	get_time_estado = clean_json(get_time_estado)

	return get_time_estado

app = FlaskAPI(__name__)

#startup
@app.route("/")#, methods=['GET'])
def obtener():
    
	listStates = getStates()

	return render_template("index.html", listStates=listStates)

#Obtain data from filters
@app.route("/city_select", methods=['POST'])
def city_select():

	global date
	global time
	global state
	global listCities

	if request.method == 'POST':
		date = request.form['date-selector']
		time = request.form['time-selector']
		state = request.form['state-selector']

		#get selected state
		listCities = getCities(state)

		#convert Hour to make queries
		global newdate;
		newdate = clean_time(date, time)
		
		#Fill template
		return render_template("city_select.html", date=date, time=time, state=state, listCities=listCities)

@app.route("/query_atractions", methods=['POST'])
def query_atractions():
	#Get selected city from form
	if request.method == 'POST':
		city = request.form['city-selector']

		climate = getClimaFromCiudad(city, newdate)

		return render_template("city_select.html", date=date, time=time, state=state, listCities=listCities, newdate=newdate)

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
