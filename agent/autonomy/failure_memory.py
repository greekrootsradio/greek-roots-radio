import json
import os
from datetime import datetime


class FailureMemory:

    def __init__(self):

        self.name = "ZETA Failure Memory"

        self.file = os.path.expanduser(
            "~/cyprus/workspace/memory/failure_history.json"
        )

        os.makedirs(
            os.path.dirname(self.file),
            exist_ok=True
        )

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:
                json.dump([], f)


    def record(
        self,
        failure,
        action,
        result="unknown"
    ):

        with open(self.file, "r") as f:
            data = json.load(f)


        entry = {

            "failure":
                failure,

            "action":
                action,

            "result":
                result,

            "created":
                str(datetime.now())

        }


        data.append(entry)


        with open(self.file, "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )


        return entry



    def recall(
        self,
        failure
    ):

        with open(self.file, "r") as f:
            data = json.load(f)


        matches = [

            item for item in data
            if item["failure"] == failure

        ]


        return matches

