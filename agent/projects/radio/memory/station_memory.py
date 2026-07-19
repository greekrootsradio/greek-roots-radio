import json
import os
from datetime import datetime


class StationMemory:

    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/workspace/radio_memory.json"
        )

        self.data = self.load()


    def load(self):

        if os.path.exists(self.file):

            with open(self.file, "r") as f:
                return json.load(f)

        return {

            "station": "Greek Roots Radio",

            "identity": {

                "culture": "Greek Cypriot",

                "audience":
                "Greek Cypriots growing up in the UK",

                "sound": [
                    "Mediterranean",
                    "Reggae",
                    "Laiko",
                    "London Fusion"
                ]

            },

            "shows": [],

            "playlists": [],

            "presenter_history": [],

            "created":
            str(datetime.now())

        }


    def save(self):

        with open(self.file, "w") as f:
            json.dump(
                self.data,
                f,
                indent=4
            )


    def status(self):

        return {

            "station":
            self.data["station"],

            "memory":
            "active",

            "shows":
            len(self.data["shows"]),

            "playlists":
            len(self.data["playlists"])

        }



if __name__ == "__main__":

    memory = StationMemory()

    print(memory.status())

    memory.save()
