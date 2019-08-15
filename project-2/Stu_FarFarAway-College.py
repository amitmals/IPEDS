
# Dependencies
import requests
import json
from config import api_key
from pprint import pprint
import pandas as pd
# import pymongo

# URL for GET requests to retrieve school data
base_url = "https://api.data.gov/ed/collegescorecard/v1/schools?"

# api_key = "rjhyKFWn0g9PsqjQC1dH9vRABMgQOMzdY5msysWA"
filter_by = 'school.state=CA'
display_fields = 'school.name,school.state,school.zip'
# url = base_url + "api_key=" + api_key + "&id=" + character_id + "&fields=" + fields
url = base_url + "api_key=" + api_key + "&" + filter_by + "&fields=" + display_fields
# print(url)

# Perform a get request for this character
response = requests.get(url)
# print(response.url)

# Storing the JSON response within a variable
data = response.json()
# print(json.dumps(data, indent=4, sort_keys=True))
school_data = data["results"]
print(school_data)








