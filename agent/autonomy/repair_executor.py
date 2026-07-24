import json
import os
from datetime import datetime


class RepairExecutor:

    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/workspace/repair_execution.json"
        )

        os.makedirs(
            os.path.dirname(self.file),
            exist_ok=True
        )

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:
                json.dump([], f, indent=4)


    def _load(self):

        with open(self.file, "r") as f:
            return json.load(f)


    def _save(self, data):

        with open(self.file, "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )


    def execute(self, proposal):

        task = {

            "agent": "ZETA Repair Executor",

            "proposal": proposal,

            "action": "prepare repair task",

            "status": "awaiting validation",

            "created": str(datetime.now())

        }


        history = self._load()

        history.append(task)

        self._save(history)

        return task


    def validate(self, proposal, result):

        task = {

            "agent": "ZETA Repair Executor",

            "proposal": proposal,

            "validation": result,

            "status": "completed",

            "created": str(datetime.now())

        }


        history = self._load()

        history.append(task)

        self._save(history)

        return task


    def history(self):

        return self._load()
