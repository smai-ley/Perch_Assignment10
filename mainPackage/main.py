# Name: Sarah Mahan, Drew Mehlman
# email:  mahansa@mail.uc.edu, mehlmadm@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 11/15/24 (Extension)
# Course #/Section: IS4010 001
# Semester/Year: Fall 2024
# Brief Description of the assignment:  

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations:
# Anything else that's relevant:

#main.py

import json
import requests

json_string = """
{
"researcher": {
"name": "Ford Prefect",
"species": "Betelgeusian",
"relatives": [
{
"name": "Zaphod Beeblebrox",
"species": "Betelgeusian"
}
]
}
}
"""
data = json.loads(json_string)  

response = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=acad&api_key=pfJKDXPzTykVL73ehnPyY8pkDQLjfq5cz5LqCkl3')
json_string = response.content
parsed_json = json.loads(json_string) # Now we have a python dictionary
#print(parsed_json)
#print(parsed_json['data'][0]['description'])
#print(parsed_json['data'][0]['directionsInfo'])
total = int(parsed_json['total']) # The number of parks that were returned
for park in parsed_json['data']:
    print(park)

def iterate_dictionary(myDictionary):
    for k, v in myDictionary.items():
        print("key is " + str(type(k)) + ", value is " + str(type(v)))
        if isinstance(v, dict):
            iterate_dictionary(v)
        else:
            print("{0} : {1}".format(k, v))
            if (isinstance(v, list)):
                for vv in v:
                    if (isinstance(vv, dict)):
                        iterate_dictionary(vv)

if __name__ == "__main__":
    None
 