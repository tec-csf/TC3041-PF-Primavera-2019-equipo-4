from flask import request, url_for, jsonify, render_template
from flask_api import FlaskAPI, status, exceptions
from pymongo import MongoClient
from bson.son import SON

app = FlaskAPI(__name__)

@app.route("/")#, methods=['GET'])
def obtener():
    mongo_uri = "mongodb://mongo-router:27017"

    client = MongoClient(mongo_uri)
    db = client.atractions
    collectionData = db.places

    #Query1: All atractions
    pipe = [{"$limit": 20}]
    cursor = collectionData.aggregate(pipe)
    result = list(cursor)

    #Query2: Get all dates since today (from influx)

    #Query3: Get all states (from influx)

    #Query4: Get all cities (from influx)
    
    return render_template("index.html", result=result, dates)

@app.route("/query_atractions", methods=['POST'])
def query_atractions():
    if request.method == 'POST':
        date = request.form['date-selector']
        state = request.form['state-selector']
        city = request.form['city-selector']

        #Query atractions based on input

        #Fill template
        return render_template("test.html", date=date, state=state, city=city)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
