# Name: Sarah Mahan, Drew Mehlman
# email:  mahansa@mail.uc.edu, mehlmadm@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 11/15/24 (Extension)
# Course #/Section: IS4010 001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Find an API. Communicate with it. Steal the data (joke). Load the json data to a dict, print cool info from dict.

# Brief Description of what this module does: the main function which performs the actions to demonstrate functionality
# Citations:
# Anything else that's relevant:

#main.py

from APIPackage.api import *
from dataHandlingPackage.dataHandling import *


if __name__ == "__main__":
    apiBuddy = apiWaiter("live_D4aC1GI9UzjP0oipQsrgcE8lUIlHTQ3VzBCjujD4vOTa3oV1gCeRnB0W2bDr0PtC") # init an apiWaiter object with the key to the API
    jsonResponse = apiBuddy.submitToServer() # submits key to API server and returns JSON data, storing to a variable
    
    dataHandler = handleData() # init the data handler
    dataDictionary = dataHandler.loadJSONtoDict(jsonResponse) # loading jsonResponse to function to turn to dictionary
    dataHandler.interpretData(dataDictionary) # Demurely printing out dictionary response in an informative statement
    coolerDataDictionary = dataHandler.writeToNewDict(dataDictionary) # Creating a new dictionary to be written to csv file
    dataHandler.writeToCSV(coolerDataDictionary) # Writing the dictionary to a csv file
    
    
    

 