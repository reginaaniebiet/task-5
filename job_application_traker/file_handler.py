import json
import os

FILE_PATH = "applications.json"

def load_applications():
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_applications(applications):
    with open(FILE_PATH, "w") as f:
        json.dump(applications, f, indent=4)
