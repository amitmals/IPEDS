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
    '2017.admissions.act_scores.midpoint.writing,2017.completion.completion_rate_4yr_150nt,'\
    '2017.cost.attendance.academic_year,2016.cost.attendance.academic_year,2015.cost.attendance.academic_year,'\
    '2014.cost.attendance.academic_year,2013.cost.attendance.academic_year,2013.earnings.10_yrs_after_entry.median,'\
    '2010.academics.program_reporter.program_1.cip_6_digit.title,'


    url = base_url + "api_key=" + api_key + "&" + filter_by + "&fields=" + display_fields

    programs = ['program_percentage.agriculture',
    'program_percentage.resources',
    'program_percentage.architecture',
    'program_percentage.ethnic_cultural_gender',
    'program_percentage.communication',
    'program_percentage.communications_technology',
    'program_percentage.computer',
    'program_percentage.personal_culinary',
    'program_percentage.education',
    'program_percentage.engineering',
    'program_percentage.engineering_technology',
    'program_percentage.language',
    'program_percentage.family_consumer_science',
    'program_percentage.legal',
    'program_percentage.english',
    'program_percentage.humanities',
    'program_percentage.library',
    'program_percentage.biological',
    'program_percentage.mathematics',
    'program_percentage.military',
    'program_percentage.multidiscipline',
    'program_percentage.parks_recreation_fitness',
    'program_percentage.philosophy_religious',
    'program_percentage.theology_religious_vocation',
    'program_percentage.physical_science',
    'program_percentage.science_technology',
    'program_percentage.psychology',
    'program_percentage.security_law_enforcement',
    'program_percentage.public_administration_social_service',
    'program_percentage.social_science',
    'program_percentage.construction',
    'program_percentage.mechanic_repair_technology',
    'program_percentage.precision_production',
    'program_percentage.transportation',
    'program_percentage.visual_performing',
    'program_percentage.health',
    'program_percentage.business_marketing',
    'program_percentage.history']

    string = '2017.academics.'
    program_list = [string + x for x in programs]
    sentence = ','.join(program_list)
    url_string = url + sentence

    response = requests.get(url_string)
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
        new_school["grad_rate"] = school["2017.completion.completion_rate_4yr_150nt"]
        new_school["cost_2017"] = school["2017.cost.attendance.academic_year"]
        new_school["cost_2016"] = school["2016.cost.attendance.academic_year"]
        new_school["cost_2015"] = school["2015.cost.attendance.academic_year"]
        new_school["cost_2014"] = school["2014.cost.attendance.academic_year"]
        new_school["cost_2013"] = school["2013.cost.attendance.academic_year"]
        new_school["earnings"] = school["2013.earnings.10_yrs_after_entry.median"]
        new_school["top_program"] = school["2010.academics.program_reporter.program_1.cip_6_digit.title"]
        new_school["agriculture"] = school["2017.academics.program_percentage.agriculture"]
        new_school["resources"] = school["2017.academics.program_percentage.resources"]
        new_school["architecture"] = school["2017.academics.program_percentage.architecture"]
        new_school["ethnic_cultural_gender"] = school["2017.academics.program_percentage.ethnic_cultural_gender"]
        new_school["communication"] = school["2017.academics.program_percentage.communication"]
        new_school["communications_technology"] = school["2017.academics.program_percentage.communications_technology"]
        new_school["computer"] = school["2017.academics.program_percentage.computer"]
        new_school["personal_culinary"] = school["2017.academics.program_percentage.personal_culinary"]
        new_school["education"] = school["2017.academics.program_percentage.education"]
        new_school["engineering"] = school["2017.academics.program_percentage.engineering"]
        new_school["engineering_technology"] = school["2017.academics.program_percentage.engineering_technology"]
        new_school["language"] = school["2017.academics.program_percentage.language"]
        new_school["family_consumer_science"] = school["2017.academics.program_percentage.family_consumer_science"]
        new_school["legal"] = school["2017.academics.program_percentage.legal"]
        new_school["english"] = school["2017.academics.program_percentage.english"]
        new_school["humanities"] = school["2017.academics.program_percentage.humanities"]
        new_school["library"] = school["2017.academics.program_percentage.library"]
        new_school["biological"] = school["2017.academics.program_percentage.biological"]
        new_school["mathematics"] = school["2017.academics.program_percentage.mathematics"]
        new_school["military"] = school["2017.academics.program_percentage.military"]
        new_school["multidiscipline"] = school["2017.academics.program_percentage.multidiscipline"]
        new_school["parks_recreation_fitness"] = school["2017.academics.program_percentage.parks_recreation_fitness"]
        new_school["philosophy_religious"] = school["2017.academics.program_percentage.philosophy_religious"]
        new_school["theology_religious_vocation"] = school["2017.academics.program_percentage.theology_religious_vocation"]
        new_school["physical_science"] = school["2017.academics.program_percentage.physical_science"]
        new_school["science_technology"] = school["2017.academics.program_percentage.science_technology"]
        new_school["psychology"] = school["2017.academics.program_percentage.psychology"]
        new_school["security_law_enforcement"] = school["2017.academics.program_percentage.security_law_enforcement"]
        new_school["public_administration_social_service"] = school["2017.academics.program_percentage.public_administration_social_service"]
        new_school["social_science"] = school["2017.academics.program_percentage.social_science"]
        new_school["construction"] = school["2017.academics.program_percentage.construction"]
        new_school["mechanic_repair_technology"] = school["2017.academics.program_percentage.mechanic_repair_technology"]
        new_school["precision_production"] = school["2017.academics.program_percentage.precision_production"]
        new_school["transportation"] = school["2017.academics.program_percentage.transportation"]
        new_school["visual_performing"] = school["2017.academics.program_percentage.visual_performing"]
        new_school["health"] = school["2017.academics.program_percentage.health"]
        new_school["business_marketing"] = school["2017.academics.program_percentage.business_marketing"]
        new_school["history"] = school["2017.academics.program_percentage.history"]

        new_school_data.append(new_school)
        # print(new_school_data)

    colleges = mongo.db.colleges
    colleges.remove()
    colleges.insert_many(new_school_data)
    
    print(new_school_data)
    return "RETURN!"


schools()

if __name__ == "__main__":
    app.run(debug=True)

