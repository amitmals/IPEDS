#Dependencies
from flask import Flask, render_template, jsonify
import requests
import json
from bson import json_util
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

#Local dependencies
from config import api_key

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/college_app"
mongo = PyMongo(app)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

def toJson(data):
    """Convert Mongo object(s) to JSON"""
    return json.dumps(data, default=json_util.default)

@app.route("/coldata")
def coldata():
    results = mongo.db.colleges.find()
    all_data = [result for result in results]
    return toJson(all_data)

if __name__ == "__main__":
    app.run(debug=True)

