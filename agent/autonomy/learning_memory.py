import os
import json
from datetime import datetime


class LearningMemory:

    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/data/development_history.json"
        )

        os.makedirs(
            os.path.dirname(self.file),
            exist_ok=True
        )

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:
                json.dump([], f, indent=4)


    def remember(self, event):

        with open(self.file, "r") as f:
            history = json.load(f)


        event["time"] = str(datetime.now())

        history.append(event)


        with open(self.file, "w") as f:
            json.dump(
                history,
                f,
                indent=4
            )


        print(
            "[ZETA Learning] Memory updated"
        )


    def recall(self):

        with open(self.file, "r") as f:
            return json.load(f)
