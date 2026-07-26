import json
import os
from datetime import datetime


class RadioMemory:


    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/workspace/radio_memory/broadcast_history.json"
        )


        if not os.path.exists(self.file):

            self.save([])



    def save(self, data):

        with open(self.file, "w") as f:

            json.dump(
                data,
                f,
                indent=4
            )



    def load(self):

        with open(self.file, "r") as f:

            return json.load(f)



    def remember_broadcast(self, broadcast):


        history = self.load()


        record = {

            "created": str(datetime.now()),

            "show": broadcast["show"]["show"],

            "playlist": broadcast["music_playlist"]["playlist"],

            "presenter": broadcast["presenter_intro"]["presenter"]

        }


        history.append(record)


        self.save(history)


        return {

            "status": "broadcast remembered",

            "total_broadcasts": len(history)

        }



    def get_history(self):

        return self.load()
