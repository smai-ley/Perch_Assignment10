# Name: Sarah Mahan, Drew Mehlman
# email:  mahansa@mail.uc.edu, mehlmadm@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 11/15/24 (Extension)
# Course #/Section: IS4010 001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Find an API. Communicate with it. Steal the data (joke). Load the json data to a dict, print cool info from dict.

# Brief Description of what this module does: this includes the class that handles and performs actions on the data that is read by the end-user
# Citations:
# Anything else that's relevant:

# dataHandling.py

import json
import requests
import csv

class handleData:
    """
    Handles the data passed from the API Package, loads json into Python dict
    """
    def __init__(self):
        """
        Constructor
        """

    def loadJSONtoDict(self, jsonResponse):
        """
        Loads JSON data into a dictionary
        @param jsonResponse: the JSON data
        @return: the dictionary
        """
        parsed_json = json.loads(jsonResponse)

        return parsed_json
    
    def interpretData(self, parsedData):
        """
        Prints interesting data taken from the API in an easy-to-read format
        @param parsedData: the dictionary to be explored for life changing secrets and information. Huzzah. 
        """
        print("The",parsedData[0]['breeds'][0]['name'], "cat originates from", parsedData[0]['breeds'][0]['origin'],".")
        print("Its temperament can be described as: ", parsedData[0]['breeds'][0]['temperament'])
        print("Short description of the cat:", parsedData[0]['breeds'][0]['description'])
        print("To find more information about",parsedData[0]['breeds'][0]['name'], "cats, visit", parsedData[0]['breeds'][0]['wikipedia_url'])
        
    def writeToNewDict(self, parsedData):
        """
        Writes a larger dict into a new dict 
        @param parsedData: the dict to be put into another dict
        """
        cooler_cat_dict = {"name": parsedData[0]['breeds'][0]['name'], 
                           "origin": parsedData[0]['breeds'][0]['origin'], 
                           "temperament": parsedData[0]['breeds'][0]['temperament'], 
                           "description":parsedData[0]['breeds'][0]['description'], 
                           "weburl":parsedData[0]['breeds'][0]['wikipedia_url']}
        
        return cooler_cat_dict
    
    def writeToCSV(self, dictionary):
        """
        Writes a dictionary to a csv
        @param dictionary: the dictionary to be written to a csv
        """
        with open("coolcat.csv", "w", newline="") as f:
            w = csv.DictWriter(f, dictionary.keys())
            w.writeheader()
            w.writerow(dictionary)
