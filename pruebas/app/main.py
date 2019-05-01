from flask import request, url_for, jsonify, render_template
from flask_api import FlaskAPI, status, exceptions
from pymongo import MongoClient
from bson.son import SON

app = FlaskAPI(__name__)

@app.route("/")#, methods=['GET'])
def obtener():
    mongo_uri = "mongodb://mongo-router:27017"

    client = MongoClient(mongo_uri)
    db = client.shdb

    collectionData = db.data

    pipe = [{"$limit": 20}]

    cursor = collectionData.aggregate(pipe)

    result = list(cursor)

    
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
