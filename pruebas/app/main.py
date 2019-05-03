from flask import request, url_for, jsonify, render_template
from flask_api import FlaskAPI, status, exceptions
from pymongo import MongoClient
from influxdb import InfluxDBClient
from bson.son import SON

#Clean influxdb queries output
def clean_json(list_json):
	for i in range (len(list_json)):
		x = json.dumps(list_json[0])
		x = json.loads(x)
	return list_json

app = FlaskAPI(__name__)

@app.route("/")#, methods=['GET'])
def obtener():
	mongo_uri = "mongodb://mongo-router:27017"
	
	client = MongoClient(mongo_uri)
	db = client.atractions
	collectionData = db.places

	client = InfluxDBClient(host='127.0.0.1', port=8086, database='pfprueba')
	client.switch_database('pfprueba')
    

	#influx Queries

    #Query3: Get all states (from influx)
	states = client.query('show tag values on "pfprueba" from "Temperatura" with key="estado"')
	states = list(estados.get_points())
	states = clean_json(estados)

    #Query4: Get all cities (from influx)
	cities = client.query('show tag values on "pfprueba" from "Temperatura" with key="ciudad"')
	cities = list(ciudad.get_points())
	cities = clean_json(ciudad)

    return render_template("index.html", states=states, cities=cities)

@app.route("/query_atractions", methods=['POST'])
def query_atractions():
    if request.method == 'POST':
        date = request.form['date-selector']
        state = request.form['state-selector']
        city = request.form['city-selector']

        #Query atractions based on input
        atractions = 

        #Fill template
        return render_template("index.html", date=date, state=state, city=city)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
