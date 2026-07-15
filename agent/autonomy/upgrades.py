import json
import os
from datetime import datetime


UPGRADE_FILE = "data/upgrades.json"


DEFAULT = {
    "ideas": [],
    "completed": []
}


def ensure_file():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(UPGRADE_FILE):
        with open(UPGRADE_FILE, "w") as f:
            json.dump(DEFAULT, f, indent=2)



def load_upgrades():

    ensure_file()

    with open(UPGRADE_FILE, "r") as f:
        return json.load(f)



def save_upgrades(data):

    with open(UPGRADE_FILE, "w") as f:
        json.dump(data, f, indent=2)



def add_upgrade(description):

    data = load_upgrades()

    data["ideas"].append(
        {
            "time": str(datetime.now()),
            "idea": description,
            "status": "pending"
        }
    )

    save_upgrades(data)

    return "Upgrade idea saved."



def list_upgrades():

    data = load_upgrades()

    return data
