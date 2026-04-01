import json

def get_data():
    with open("config/data.json") as f:
        return json.load(f)