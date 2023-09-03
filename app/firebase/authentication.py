# Pyrebase guide url: https://github.com/nhorvath/Pyrebase4
# Handles user authentication with Firebase.

# Pyrebase is a Firebase API wrapper
import pyrebase
import json
import os

config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'app', 'config.json')

def initialize_firebase():
    try:
        with open(config_path, "r") as config_file:
            config_data = json.load(config_file)
            
        connect = pyrebase.initialize_app(config_data)
        
        print("All clear")
        
        return connect

    except Exception as e:
        print(f"Error in connection/n{e}")

firebase = initialize_firebase()

authenticate = firebase.auth()
database = firebase.database()