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
import requests

class handleData:
    """
    Handles the data passed from the API Package, loads json into Python dict
    """
    def __init__(self, url):
        """
        Constructor
        @url string: the url of the website
        """
        self.__url = url

    def getUrl(self):
        """
        Returns URL member
        """
        return f"{self.__url}"

    def interpretJSON(self):
        json_cat = """
                    {
                    "cats": {
                            "id": "a3f",
                            "url": """ + {self.__url} +""", #https://cdn2.thecatapi.com/images/a3f.jpg
                            "width": 1200,
                            "height": 900"
                            }
                    }
        """
        data = json.loads(json_string)  
        parsed_json = json.loads(json_string)
        
        cat_dict = json.loads(json_cat)
        self.iterate_dictionary(cat_dict)
        print(cat_dict)
        
        
     
        
    def iterate_dictionary(self, myDictionary):
        for k, v in myDictionary.items():
            print ("key is " + str(type(k)) + ", value is " + str(type(v)))
            if isinstance(v, dict):
                self.iterate_dictionary(v)
            else:
            print("{0} : {1}".format(k, v))
                if (isinstance(v, list)):
                    for vv in v:
                        if (isinstance(vv, dict)):
                        self.iterate_dictionary(vv)

                        



