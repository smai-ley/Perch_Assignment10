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


def JSON():
    
    json_string = """
    {
    "cats": {
        "id": "a3f",
        "url": "https://cdn2.thecatapi.com/images/a3f.jpg",
        "width": 1200,
        "height": 900"
            }
    }
    """
    data = json.loads(json_string)  
    print(data)


    


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
                        
API()

if __name__ == "__main__":
    None
 