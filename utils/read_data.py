import json
import os


def get_data():
    file_path = os.path.join(os.path.dirname(__file__), "..", "config", "data.json")

    with open(file_path, "r") as f:
        return json.load(f)