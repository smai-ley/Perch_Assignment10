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

# dataHandling.py

import json

class handleData:
    """
    Handles the data passed from the API Package, loads json into Python dict
    """
    def __init__(self, url):
        """
        Constructor
        """
        self.__url = url
    
    def getUrl(self):
        """
        Returns URL member
        """
        return f"{self.__url}"

    def interpretJSON(self):
        json_string = """
                    {
                    "cats": {
                            "id": "a3f",
                            "url": """ + {self.__url} +""",
                            "width": 1200,
                            "height": 900"
                            }
                    }
        """
        data = json.loads(json_string)  
        parsed_json = json.loads(json_string)
        
        return parsed_json
        
    def iterate_json_string(myDictionary):
        for k, v in myDictionary.items():
            print("key is " + str(type(k)) + ", value is " + str(type(v)))
            if isinstance(v, dict):
                iterate_json_string(v)
            else:
                print("{key} : {value}".format(k, v))
                if (isinstance(v, list)):
                    for vv in v:
                        if (isinstance(vv, dict)):
                            iterate_json_string(vv)



