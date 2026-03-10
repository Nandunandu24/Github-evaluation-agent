import json
import os

DB_FILE = "candidates.json"


def load_candidates():
    
    if not os.path.exists(DB_FILE):
        return []
    
    with open(DB_FILE, "r") as file:
        data = json.load(file)
    
    return data


def save_candidate(candidate):

    candidates = load_candidates()

    candidates.append(candidate)

    with open(DB_FILE, "w") as file:
        json.dump(candidates, file, indent=4)