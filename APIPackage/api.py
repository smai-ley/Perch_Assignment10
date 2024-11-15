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
    def __init__(self, keyString):
        """
        Initilize apiWaiter object
        @param keyString: the string of the api key provided in the comment submission on canvas
        """
        self.keyString = keyString
        
        return self
    
    def submitToServer(url):
        """
        Submits url to API server to receive results
        @param url: the string with the url
        @return: the json results
        """
        # self.keyString
        jsonResults = None
        
        return jsonResults
    
    
