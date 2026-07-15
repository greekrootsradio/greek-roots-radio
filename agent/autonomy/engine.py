import json
import os
import time
from datetime import datetime


UPGRADE_FILE = "data/upgrades.json"


class AutonomyEngine:

    def __init__(self):
        self.running = False

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(UPGRADE_FILE):
            self.create_file()


    def create_file(self):

        data = {
            "ideas": [],
            "completed": []
        }

        with open(UPGRADE_FILE, "w") as f:
            json.dump(data, f, indent=2)


    def load(self):

        with open(UPGRADE_FILE, "r") as f:
            return json.load(f)


    def save(self, data):

        with open(UPGRADE_FILE, "w") as f:
            json.dump(data, f, indent=2)


    def add_upgrade(self, idea):

        data = self.load()

        existing = [
            x["idea"]
            for x in data["ideas"]
        ]

        completed = [
            x["idea"]
            for x in data["completed"]
        ]


        if idea in existing or idea in completed:
            return


        data["ideas"].append(
            {
                "time": str(datetime.now()),
                "idea": idea,
                "status": "pending"
            }
        )

        self.save(data)


    def think(self):

        upgrades = [

            "Improve memory recall system",
            "Add project management skills",
            "Add calendar integration",
            "Improve conversation history",
            "Create web research module"

        ]


        for upgrade in upgrades:
            self.add_upgrade(upgrade)



    def heartbeat(self):

        print("[ZETA] autonomy thinking...")

        self.think()


    def start(self):

        self.running = True

        print("ZETA Autonomy Engine Started")


        while self.running:

            self.heartbeat()

            time.sleep(300)



if __name__ == "__main__":

    engine = AutonomyEngine()
    engine.start()
