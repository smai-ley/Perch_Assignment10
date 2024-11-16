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

#api.py

import json
import requests

class apiWaiter:
    """
    Performs interactions and requests data with API Server
    """
    def __init__(self, keyString):
        """
        Constructor
        @param keyString string: the api key provided in the comment submission on Canvas
        """
        self.__keyString = keyString
        
    def getKeyString(self):
        """
        @return: the key as a string
        """
        return f"{self.__keyString}"
    
    def submitToServer(self):
        """
        Submits url to API server to receive results
        @return: the json results
        """
        response = requests.get('https://api.thecatapi.com/v1/images/search?limit=10&breed_ids=beng&api_key=' + self.__keyString)

        jsonResults = response.content
        
        return jsonResults
    