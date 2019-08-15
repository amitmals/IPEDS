#Dependencies
from flask import Flask, render_template
import requests
import json
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


@app.route("/schools")
def schools():
        # get data from API
    base_url = "https://api.data.gov/ed/collegescorecard/v1/schools?"
    filter_by = 'school.state=CA'
    display_fields = 'school.name,school.state,school.zip,location.lon,'\
        'location.lat,2017.admissions.admission_rate.overall,2017.student.size,'\
        'school.ownership,2017.admissions.sat_scores.midpoint.critical_reading,'\
        'id,school.school_url,2017.admissions.sat_scores.midpoint.math,'\
        '2017.admissions.sat_scores.midpoint.writing,2017.admissions.act_scores.midpoint.cumulative,'\
        '2017.admissions.act_scores.midpoint.english,2017.admissions.act_scores.midpoint.math,'\
        '2017.admissions.act_scores.midpoint.writing'


    url = base_url + "api_key=" + api_key + "&" + filter_by + "&fields=" + display_fields
    response = requests.get(url)
    data = response.json()
    school_data = data["results"]
    
    new_school_data = []

    for school in school_data:
        new_school = {}
        new_school["name"] = school["school.name"]
        new_school["state"] = school["school.state"]
        new_school["zip"] = school["school.zip"]
        new_school["lon"] = school["location.lon"]
        new_school["lat"] = school["location.lat"]
        new_school["amdissions_rate"] = school["2017.admissions.admission_rate.overall"]
        new_school["size"] = school["2017.student.size"]
        new_school["ownership"] = school["school.ownership"]
        new_school["sat_reading"] = school["2017.admissions.sat_scores.midpoint.critical_reading"]
        new_school["id"] = school["id"]
        new_school["school_url"] = school["school.school_url"]
        new_school["sat_math"] = school["2017.admissions.sat_scores.midpoint.math"]
        new_school["sat_writing"] = school["2017.admissions.sat_scores.midpoint.writing"]
        new_school["act_cumulative"] = school["2017.admissions.act_scores.midpoint.cumulative"]
        new_school["act_writing"] = school["2017.admissions.act_scores.midpoint.writing"]
        new_school["act_english"] = school["2017.admissions.act_scores.midpoint.english"]
        new_school["act_math"] = school["2017.admissions.act_scores.midpoint.math"]

        new_school_data.append(new_school)
        # print(new_school_data)
    

    colleges = mongo.db.colleges
    colleges.insert_many(new_school_data)
    # colleges.update({}, new_school_data, upsert=True)
    print(new_school_data)
    return "RETURN!"


schools()

if __name__ == "__main__":
    app.run(debug=True)

