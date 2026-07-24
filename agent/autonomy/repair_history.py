import json
import os
from datetime import datetime


class RepairHistory:

    def __init__(self):

        self.name = "ZETA Repair History"

        self.file = os.path.expanduser(
            "~/cyprus/workspace/memory/repair_history.json"
        )


        os.makedirs(
            os.path.dirname(self.file),
            exist_ok=True
        )


        if not os.path.exists(self.file):

            with open(self.file, "w") as f:
                json.dump([], f)



    def record_repair(
        self,
        failure,
        repair,
        result="unknown"
    ):

        with open(self.file, "r") as f:
            data = json.load(f)


        entry = {

            "failure":
                failure,

            "repair":
                repair,

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



    def get_history(
        self,
        failure
    ):

        with open(self.file, "r") as f:
            data = json.load(f)


        return [

            item for item in data
            if item["failure"] == failure

        ]
