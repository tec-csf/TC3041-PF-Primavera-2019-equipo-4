from flask import request, url_for, jsonify, render_template
from flask_api import FlaskAPI, status, exceptions
from backend import api

#options
state="state"
newdate="date"
date="date"
time="time"
state="state"
listCities="list"

#API object
databases = api.API()

app = FlaskAPI(__name__)

#startup
@app.route("/")#, methods=['GET'])
def obtener():
    
	listStates = databases.getStates()

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
		listCities = databases.getCities(state)

		#convert Hour to make queries
		global newdate;
		newdate = databases.clean_time(date, time)

		climate="default"
		
		#Fill template
		return render_template("city_select.html", date=date, time=time, state=state, listCities=listCities, climate=climate)

@app.route("/query_atractions", methods=['POST'])
def query_atractions():
	#Get selected city from form
	if request.method == 'POST':
		city = request.form['city-selector']

		climate = databases.getClimaFromCiudad(city, newdate)
		climate = climate[0]["clima"]

		#convert climate to lowecase
		climate = climate.lower()

		#Query atractions on MongoDB based on climate
		suitableAtractions = databases.queryAtractionsBasedOnClimate(climate, city)

		return render_template("city_select.html", date=date, time=time, state=state, city=city, listCities=listCities, newdate=newdate, climate=climate, suitableAtractions=suitableAtractions)

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
