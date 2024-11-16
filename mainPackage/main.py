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

from APIPackage.api import *
from dataHandlingPackage.dataHandling import *

if __name__ == "__main__":
    apiBuddy = apiWaiter("live_D4aC1GI9UzjP0oipQsrgcE8lUIlHTQ3VzBCjujD4vOTa3oV1gCeRnB0W2bDr0PtC") # init an apiWaiter object with the key to the API
    apiBuddy.submitToServer() # submits key to API server and returns JSON data
 